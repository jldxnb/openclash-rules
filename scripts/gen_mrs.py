#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 rules/*.list（手工维护的文本源）转换成 mrs/ 下的二进制规则集。

为什么要转 mrs
--------------
classical 文本规则集（`behavior: classical, format: text`）匹配时是**逐条线性扫描**，
条目越多、每个连接的匹配就越慢；mrs 走索引查找，代价与条目数基本无关。所以配置里
域名类清单一律用 mrs，文本 `.list` 只作为**唯一的手工维护源**留在 rules/。

mrs 能表达什么（源码核过，别凭直觉）
------------------------------------
`behavior: domain` 的规则集把每行文本原样喂给 `trie.DomainSetBuilder.Insert`，
只认这几种写法：`example.com`（精确）、`+.example.com`（本域及子域）、
`.example.com`、`*.example.com`。**没有 DOMAIN-KEYWORD**——关键词是"包含即可"，
而 mrs 是域名前缀树，表达不了；把 `DOMAIN-KEYWORD,x` 整行喂进去只会变成一个
永远匹配不到的怪域名（这正是第一版脚本踩的坑，且"转回文本再比对"看不出来，
因为转回来就是原样那行）。

所以本脚本把每个清单拆成两半：

- **域名部分**（`DOMAIN` / `DOMAIN-SUFFIX`）→ `mrs/<同名>.mrs`（转换时改写为
  `x` / `+.x` 语法后交给 mihomo 的 `convert-ruleset`）
- **其余部分**（`DOMAIN-KEYWORD` / `IP-CIDR` / `PROCESS-NAME` 等）→
  `rules/<同名>.rest.list`（生成物，仍是 classical 文本，配置里照旧按文本引用）

只有域名部分的清单（如 `ProxyLite.list`）只产出 mrs；只有非域名规则的清单
（如 `download.list`）不产出任何东西，配置直接引用原清单。

用法
----
    python scripts/gen_mrs.py                  # 生成/更新 mrs/ 与 rules/*.rest.list
    python scripts/gen_mrs.py --check          # 只校验产物与源清单是否一致（CI 用），不一致退出码 1
    python scripts/gen_mrs.py --mihomo PATH    # 指定 mihomo 二进制

mihomo 二进制查找顺序：`--mihomo` → 环境变量 `MIHOMO_BIN` → PATH 里的 mihomo →
自动下载官方 release 到 `.cache/`（版本固定在 MIHOMO_VERSION）。
"""

from __future__ import annotations

import argparse
import gzip
import io
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "rules"
MRS_DIR = ROOT / "mrs"
CACHE_DIR = ROOT / ".cache"

# 固定版本：mrs 输出可复现，CI 与本地跑出一样的结果
MIHOMO_VERSION = "v1.19.32"
RELEASE_URL = "https://github.com/MetaCubeX/mihomo/releases/download/{v}/{asset}"

# mrs 只认精确域名与后缀（关键词表达不了），见文件头说明
MRS_TYPES = {"DOMAIN", "DOMAIN-SUFFIX"}
REST_SUFFIX = ".rest.list"
REST_HEADER = (
    "# 自动生成（scripts/gen_mrs.py）：从 rules/{stem}.list 拆出的非域名规则。\n"
    "# mrs 只能表达 DOMAIN / DOMAIN-SUFFIX，这些条目编不进去，仍以 classical 文本提供。\n"
    "# 不要手改本文件——改 rules/{stem}.list 后重新生成。\n"
)

ASSETS = {
    ("linux", "x86_64"): "mihomo-linux-amd64-compatible-{v}.gz",
    ("linux", "aarch64"): "mihomo-linux-arm64-{v}.gz",
    ("windows", "amd64"): "mihomo-windows-amd64-compatible-{v}.zip",
    ("darwin", "arm64"): "mihomo-darwin-arm64-{v}.gz",
    ("darwin", "x86_64"): "mihomo-darwin-amd64-{v}.gz",
}


def norm(entries) -> set[tuple[str, str]]:
    """规则集合：类型大写、内容小写（mrs 里域名一律小写）。"""
    return {(t.upper(), p.lower()) for t, p, *_ in entries}


def read_list(path: Path) -> list[tuple[str, str, str]]:
    """读文本规则集 → [(类型, 内容, 整行)]，跳过空行与整行注释。"""
    out: list[tuple[str, str, str]] = []
    text = path.read_text(encoding="utf-8-sig")
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith(("#", ";", "//")):
            continue
        rule_type, _, rest = line.partition(",")
        payload = rest.split(",")[0].strip()
        out.append((rule_type.strip().upper(), payload, line))
    return out


def split_list(entries) -> tuple[list, list]:
    """拆成（域名部分, 其余部分），顺序保持。"""
    mrs_part = [e for e in entries if e[0] in MRS_TYPES]
    rest_part = [e for e in entries if e[0] not in MRS_TYPES]
    return mrs_part, rest_part


def mrs_text(mrs_part) -> str:
    """转成 mihomo 域名规则集认的写法：DOMAIN → `x`，DOMAIN-SUFFIX → `+.x`。"""
    lines: list[str] = []
    for rule_type, payload, _ in mrs_part:
        lines.append(payload if rule_type == "DOMAIN" else f"+.{payload}")
    return "\n".join(lines) + "\n"


def expand_export(keys) -> set[tuple[str, str]]:
    """把 mrs 导出的模式展开成规则集合（`+.x` 同时代表精确与后缀两条）。"""
    out: set[tuple[str, str]] = set()
    for key in keys:
        key = key.strip().lower().rstrip(".")
        if key.startswith("+."):
            domain = key[2:]
            out.add(("DOMAIN", domain))
            out.add(("DOMAIN-SUFFIX", domain))
        elif key.startswith("."):
            out.add(("DOMAIN-SUFFIX", key[1:]))
        else:
            out.add(("DOMAIN", key))
    return out


def diff_rules(expected: set[tuple[str, str]], actual: set[tuple[str, str]],
               allow_merge: bool) -> list[str]:
    """比较两组规则。allow_merge 时放行 `+.x` 合并出来的精确条目。"""
    problems = []
    missing = {e for e in expected if e not in actual}
    if missing:
        problems.append("mrs 里缺：" + ", ".join(f"{t}:{p}" for t, p in sorted(missing)[:5]))
    extra = set()
    for rule in actual:
        if rule in expected:
            continue
        if allow_merge and rule[0] == "DOMAIN" and ("DOMAIN-SUFFIX", rule[1]) in expected:
            continue  # "+.x" 展开出的精确条目，源里只有后缀条目，属正常合并
        extra.add(rule)
    if extra:
        problems.append("mrs 里多：" + ", ".join(f"{t}:{p}" for t, p in sorted(extra)[:5]))
    return problems


def run(mihomo: Path, *args: str) -> None:
    proc = subprocess.run([str(mihomo), *args], capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"mihomo {' '.join(args)} 失败：\n{proc.stdout}{proc.stderr}")


def export_keys(mihomo: Path, mrs: Path, workdir: Path) -> list[str]:
    """把 mrs 转回文本——mihomo 没有别的"查看 mrs 内容"手段。"""
    out = workdir / (mrs.stem + ".export.txt")
    run(mihomo, "convert-ruleset", "domain", "mrs", str(mrs), str(out))
    return [line.strip() for line in out.read_text(encoding="utf-8").splitlines() if line.strip()]


def convert(mihomo: Path, text: str, dst: Path, workdir: Path) -> None:
    src = workdir / (dst.stem + ".src.txt")
    tmp = workdir / (dst.stem + ".mrs")
    src.write_text(text, encoding="utf-8")
    run(mihomo, "convert-ruleset", "domain", "text", str(src), str(tmp))
    if not tmp.is_file() or tmp.stat().st_size == 0:
        raise RuntimeError(f"{dst.name} 转换后为空文件")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(tmp), str(dst))


def rest_text(stem: str, rest_part) -> str:
    body = "".join(line + "\r\n" for _, _, line in rest_part)
    return REST_HEADER.format(stem=stem).replace("\n", "\r\n") + body


def find_mihomo(explicit: str | None) -> Path:
    if explicit:
        p = Path(explicit)
        if not p.is_file():
            raise SystemExit(f"--mihomo 指定的文件不存在：{p}")
        return p
    if os.environ.get("MIHOMO_BIN"):
        p = Path(os.environ["MIHOMO_BIN"])
        if not p.is_file():
            raise SystemExit(f"MIHOMO_BIN 指向的文件不存在：{p}")
        return p
    found = shutil.which("mihomo")
    if found:
        return Path(found)
    return download_mihomo()


def download_mihomo() -> Path:
    system = platform.system().lower()
    machine = platform.machine().lower()
    key = (system, machine)
    if key not in ASSETS:
        raise SystemExit(
            f"没有 {system}/{machine} 的预编译包，请手动下载 mihomo 后用 --mihomo 指定，"
            f"或设置环境变量 MIHOMO_BIN。可用平台：{sorted(ASSETS)}"
        )
    asset = ASSETS[key].format(v=MIHOMO_VERSION)
    url = RELEASE_URL.format(v=MIHOMO_VERSION, asset=asset)
    binary = CACHE_DIR / f"mihomo-{MIHOMO_VERSION}{'.exe' if system == 'windows' else ''}"
    if binary.is_file():
        return binary

    CACHE_DIR.mkdir(exist_ok=True)
    print(f"下载 mihomo {MIHOMO_VERSION}（{asset}）…")
    try:
        with urllib.request.urlopen(url, timeout=180) as resp:
            blob = resp.read()
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(
            f"下载失败：{exc}\n可手动下载 {url} 解压后放进 {CACHE_DIR} 或设置 MIHOMO_BIN。"
        ) from exc

    if asset.endswith(".gz"):
        raw = gzip.decompress(blob)
    else:
        with zipfile.ZipFile(io.BytesIO(blob)) as zf:
            names = [n for n in zf.namelist() if not n.endswith("/")]
            raw = zf.read(names[0])
    binary.write_bytes(raw)
    if system != "windows":
        binary.chmod(0o755)
    return binary


def source_lists() -> list[Path]:
    """手工源清单：rules/*.list，排除自己生成的 *.rest.list。"""
    return sorted(p for p in SRC_DIR.glob("*.list") if not p.name.endswith(REST_SUFFIX))


def main() -> int:
    parser = argparse.ArgumentParser(description="生成/校验 mrs 规则集")
    parser.add_argument("--check", action="store_true",
                        help="只校验产物与 rules/*.list 是否一致（不写文件），不一致退出码 1")
    parser.add_argument("--mihomo", help="mihomo 可执行文件路径")
    args = parser.parse_args()

    if not SRC_DIR.is_dir():
        raise SystemExit("找不到 rules/ 目录，请在仓库根目录运行")

    lists = source_lists()
    if not lists:
        raise SystemExit("rules/ 下没有 .list 文件")

    problems: list[str] = []
    rows: list[tuple[str, int, int, str]] = []
    mihomo: Path | None = None

    with tempfile.TemporaryDirectory() as tmpdir:
        workdir = Path(tmpdir)
        for path in lists:
            entries = read_list(path)
            mrs_part, rest_part = split_list(entries)
            dst = MRS_DIR / (path.stem + ".mrs")
            rest_path = SRC_DIR / (path.stem + REST_SUFFIX)
            status: list[str] = []

            # ── 域名部分 → mrs ──
            if mrs_part:
                if mihomo is None:
                    mihomo = find_mihomo(args.mihomo)
                if args.check:
                    if not dst.is_file():
                        problems.append(f"{path.name}：缺少 mrs/{dst.name}（跑 python scripts/gen_mrs.py）")
                        status.append("缺 mrs")
                    else:
                        actual = expand_export(export_keys(mihomo, dst, workdir))
                        problems += [f"{path.name}：{p}" for p in
                                     diff_rules(norm(mrs_part), actual, allow_merge=True)]
                        if not diff_rules(norm(mrs_part), actual, allow_merge=True):
                            status.append("mrs 一致")
                else:
                    before = dst.read_bytes() if dst.is_file() else None
                    convert(mihomo, mrs_text(mrs_part), dst, workdir)
                    actual = expand_export(export_keys(mihomo, dst, workdir))
                    bad = diff_rules(norm(mrs_part), actual, allow_merge=True)
                    if bad:
                        problems += [f"{path.name}：{p}" for p in bad]
                        status.append("校验失败")
                    else:
                        after = dst.read_bytes()
                        status.append("mrs 生成" if before != after else "mrs 未变化")
            else:
                status.append("无域名部分")

            # ── 其余部分 → rules/<同名>.rest.list ──
            if rest_part and mrs_part:
                want = rest_text(path.stem, rest_part)
                if args.check:
                    if not rest_path.is_file():
                        problems.append(f"{path.name}：缺少 {rest_path.name}（跑 python scripts/gen_mrs.py）")
                        status.append("缺 rest")
                    elif norm(read_list(rest_path)) != norm(rest_part):
                        problems.append(f"{path.name}：{rest_path.name} 与源清单的非域名规则不一致")
                        status.append("rest 不一致")
                    else:
                        status.append("rest 一致")
                else:
                    have = rest_path.read_text(encoding="utf-8") if rest_path.is_file() else None
                    changed = have != want
                    if changed:
                        rest_path.write_text(want, encoding="utf-8", newline="")
                    status.append("rest 生成" if changed else "rest 未变化")
            elif rest_part:
                status.append(f"仅非域名规则（{len(rest_part)} 条）")

            rows.append((path.name, len(mrs_part), len(rest_part), "，".join(status)))

            # ── 只有域名部分的清单不该留 rest 文件 ──
            if rest_path.is_file() and not rest_part:
                problems.append(f"{rest_path.name} 已无对应规则，应当删除")

    print(f"\n{'清单':<20}{'域名':>5}{'其余':>5}  产物")
    for name, n_mrs, n_rest, status in rows:
        print(f"{name:<20}{n_mrs:>5}{n_rest:>5}  {status}")
    print(f"\n（结果在 {MRS_DIR.relative_to(ROOT)}/ 与 {SRC_DIR.relative_to(ROOT)}/*{REST_SUFFIX}）")

    orphans = [p for p in sorted(MRS_DIR.glob("*.mrs"))
               if not (SRC_DIR / (p.stem + ".list")).is_file()]
    for p in orphans:
        problems.append(f"{p.relative_to(ROOT)} 没有对应的 rules/{p.stem}.list（源清单已删？）")

    if problems:
        print("\n问题：")
        for line in problems:
            print(f"  - {line}")
        return 1
    print("\n产物与源清单一致。" if args.check else "\n完成。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
