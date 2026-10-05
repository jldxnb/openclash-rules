#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""仓库自检：引用完整性 + 规则集格式 + 配置一致性。

存在的意义：这个仓库历史上多次出现「文件改名/删除后忘记更新引用」，
导致配置里的规则集 URL 全部 404，直到路由器上拉取失败才发现。
本脚本把这类问题变成提交前就能发现的错误。

用法：
    python scripts/validate.py            # 离线检查（默认，CI 每次提交都跑）
    python scripts/validate.py --online   # 额外探测外部 URL 可达性（定期跑，抓上游链接腐烂）

退出码：0 = 通过（可能有警告）；1 = 存在 ERROR。

检查范围只包括"被消费的"目录：configs/ 与 rules/。
docs/ 与 archive/ 不参与检查——前者是文档（里面的 URL 只是示例），
后者是历史快照（保留它被归档时的原样，不追着修）。
"""

from __future__ import annotations

import argparse
import re
import struct
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
REPO = "jldxnb/openclash-rules"
BRANCH = "main"

# 指向本仓库自身的 raw URL，例如
# https://raw.githubusercontent.com/jldxnb/openclash-rules/main/rules/AI.list
SELF_RE = re.compile(rf"raw\.githubusercontent\.com/{re.escape(REPO)}/([^/\s\"`,)]+)/([^\s\"`,)]+)")
URL_RE = re.compile(r"https?://[^\s\"`,)]+")

# mihomo classical 文本规则集支持的规则类型（用于抓笔误和格式错误）
RULE_TYPES = {
    "DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "DOMAIN-REGEX", "DOMAIN-WILDCARD",
    "GEOSITE", "GEOIP", "IP-CIDR", "IP-CIDR6", "IP-SUFFIX", "IP-ASN",
    "SRC-IP-CIDR", "SRC-IP-CIDR6", "SRC-IP-SUFFIX", "SRC-GEOIP", "SRC-IP-ASN",
    "SRC-PORT", "DST-PORT", "IN-PORT", "IN-TYPE", "IN-USER", "IN-NAME",
    "IN-PROCESS-NAME", "IN-PROCESS-PATH",
    "PROCESS-NAME", "PROCESS-PATH", "PROCESS-NAME-REGEX", "PROCESS-PATH-REGEX",
    "UID", "NETWORK", "DSCP",
}
# classical 规则集里不允许出现的类型（mihomo 会直接报 unsupported）
RULE_TYPES_FORBIDDEN = {"MATCH", "RULE-SET", "SUB-RULE", "AND", "OR", "NOT"}

BUILTIN_POLICIES = {
    "DIRECT", "REJECT", "REJECT-DROP", "PASS", "COMPATIBLE", "GLOBAL", "PROXY",
}

# 需要人工替换的占位符（保留它们是设计如此，只提示不报错）
PLACEHOLDERS = ("订阅", "订阅链接", "你的订阅")

issues: list[tuple[str, str, int, str]] = []


def add(level: str, path, line: int, message: str) -> None:
    issues.append((level, str(path).replace("\\", "/"), line, message))


def find_issues(level: str) -> list[tuple[str, str, int, str]]:
    return [i for i in issues if i[0] == level]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def source_files() -> list[Path]:
    """参与检查的文件：configs/ 与 rules/ 下的文本文件。"""
    out: list[Path] = []
    for sub in ("configs", "rules"):
        base = ROOT / sub
        if not base.is_dir():
            add("ERROR", sub, 0, f"目录不存在：{sub}/")
            continue
        out += sorted(p for p in base.rglob("*") if p.is_file() and p.suffix in (".ini", ".yaml", ".yml", ".list"))
    return out


# --------------------------------------------------------------------------
# 1. 引用完整性：配置里指向本仓库的 URL，必须在仓库里真实存在
# --------------------------------------------------------------------------
def check_self_references(files: list[Path]) -> None:
    for path in files:
        for lineno, line in enumerate(read_text(path).splitlines(), 1):
            for ref, rel in SELF_RE.findall(line):
                if ref != BRANCH:
                    add("WARN", path.relative_to(ROOT), lineno,
                        f"引用了非 {BRANCH} 分支（{ref}）：{rel}")
                if not (ROOT / rel).is_file():
                    add("ERROR", path.relative_to(ROOT), lineno,
                        f"引用的文件不存在：{rel}（URL 会 404）")


def referenced_rule_files(files: list[Path]) -> set[str]:
    """收集被 configs/ 真正引用（未被注释掉）的 rules/ 文件相对路径。"""
    used: set[str] = set()
    for path in files:
        if path.suffix not in (".ini", ".yaml", ".yml"):
            continue
        for line in read_text(path).splitlines():
            stripped = line.lstrip()
            if stripped.startswith(("#", ";", "//")):
                continue  # 注释掉的引用不算使用
            for _, rel in SELF_RE.findall(line):
                used.add(rel)
    return used


def check_unused_rule_files(used: set[str]) -> None:
    for path in sorted((ROOT / "rules").glob("*.list")):
        rel = f"rules/{path.name}"
        if rel not in used:
            add("INFO", rel, 0, "未被 configs/ 中任何配置引用（保留备用可以忽略）")


# --------------------------------------------------------------------------
# 2. 规则集文件格式
# --------------------------------------------------------------------------
def check_rule_lists() -> None:
    rules_dir = ROOT / "rules"
    if not rules_dir.is_dir():
        return
    for path in sorted(rules_dir.glob("*.list")):
        rel = path.relative_to(ROOT)
        if path.read_bytes().startswith(b"\xef\xbb\xbf"):
            add("WARN", rel, 1, "文件带 UTF-8 BOM，部分工具解析会出错")

        seen: dict[str, int] = {}
        effective = 0
        for lineno, raw in enumerate(read_text(path).splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith(("#", ";", "//")):
                continue
            if line.startswith("-"):
                add("ERROR", rel, lineno,
                    "规则行带 YAML 列表前缀 '- '，classical 文本规则集不支持（该行会被跳过）")
                line = line.lstrip("-").strip()

            rule_type, _, payload = line.partition(",")
            rule_type = rule_type.strip().upper()
            payload = payload.strip()

            if rule_type in RULE_TYPES_FORBIDDEN:
                add("ERROR", rel, lineno, f"{rule_type} 不能出现在 classical 规则集中")
            elif rule_type not in RULE_TYPES:
                add("ERROR", rel, lineno,
                    f"未知规则类型 {rule_type}（若确认 mihomo 支持，请加入脚本白名单）")
            if not payload:
                add("ERROR", rel, lineno, f"{rule_type} 缺少匹配内容")
            # mihomo 解析文本规则集时只把「整行以 # 开头」当注释（源码 rules/provider/
            # provider.go 的 rulesParse：if str[0] == '#' { continue }），行内 # 不会被剥掉，
            # 会被算进匹配内容 → 该条规则永远不命中。REGEX 类型的 payload 可能合法含 #
            if "#" in line and not rule_type.endswith("REGEX"):
                add("ERROR", rel, lineno,
                    "规则行内有 '#'（行内注释无效）：会被当成匹配内容，该条规则实际不会命中；"
                    "请把注释挪到单独一行")
            if " " in payload.split(",")[0] and rule_type.startswith("DOMAIN"):
                add("WARN", rel, lineno, f"域名含空格：{payload}")

            if line in seen:
                add("WARN", rel, lineno, f"与第 {seen[line]} 行重复")
            else:
                seen[line] = lineno
            effective += 1

        if effective == 0:
            add("WARN", rel, 0, "规则集内没有有效规则（引用它的策略组不会命中任何流量）")


# --------------------------------------------------------------------------
# 3. mihomo 配置（configs/mihomo/*.yaml）
# --------------------------------------------------------------------------
def check_mihomo_configs() -> None:
    base = ROOT / "configs" / "mihomo"
    if not base.is_dir():
        return
    try:
        import yaml  # type: ignore
    except ImportError:
        add("WARN", "configs/mihomo", 0,
            "未安装 PyYAML，跳过 mihomo 配置的结构校验（pip install pyyaml 可启用）")
        return

    for path in sorted(base.glob("*.y*ml")):
        rel = path.relative_to(ROOT)
        try:
            cfg = yaml.safe_load(read_text(path))
        except yaml.YAMLError as exc:
            add("ERROR", rel, getattr(exc, "problem_mark", None) and exc.problem_mark.line + 1 or 0,
                f"YAML 语法错误：{exc}")
            continue
        if not isinstance(cfg, dict):
            add("ERROR", rel, 0, "顶层不是映射结构")
            continue

        providers = cfg.get("rule-providers") or {}
        proxy_providers = cfg.get("proxy-providers") or {}
        groups = cfg.get("proxy-groups") or []
        group_names = {g.get("name") for g in groups if isinstance(g, dict)}

        # rule-providers 必填字段
        for name, spec in providers.items():
            if not isinstance(spec, dict):
                add("ERROR", rel, 0, f"rule-provider {name} 结构异常")
                continue
            for field in ("type", "behavior", "format"):
                if field not in spec:
                    add("ERROR", rel, 0, f"rule-provider {name} 缺少 {field} 字段")
            url = str(spec.get("url", ""))
            if url and not url.startswith("http"):
                add("INFO", rel, 0, f"rule-provider {name} 的 url 是占位符：{url}")

        # RULE-SET 必须指向已定义的 rule-provider
        for entry in cfg.get("rules") or []:
            text = str(entry)
            if not text.upper().startswith("RULE-SET,"):
                continue
            name = text.split(",")[1].strip() if "," in text else ""
            if name.startswith(("geosite:", "geoip:")):
                continue
            if name not in providers:
                add("ERROR", rel, 0, f"rules 里引用了未定义的 rule-provider：{name}")

        # 策略组引用
        for group in groups:
            if not isinstance(group, dict):
                continue
            gname = group.get("name")
            for ref in group.get("proxies") or []:
                if ref in group_names or ref in BUILTIN_POLICIES:
                    continue
                add("WARN", rel, 0, f"策略组「{gname}」引用的 {ref} 既不是已定义策略组也不是内建策略")
            for ref in group.get("use") or []:
                if ref not in proxy_providers:
                    add("ERROR", rel, 0, f"策略组「{gname}」引用了未定义的 proxy-provider：{ref}")

        # 订阅地址占位符
        for name, spec in proxy_providers.items():
            if isinstance(spec, dict):
                url = str(spec.get("url", ""))
                if url and not url.startswith("http"):
                    add("WARN", rel, 0, f"proxy-provider {name} 的订阅地址是占位符「{url}」，需替换后才能用")

        check_exposure(rel, cfg)


def check_exposure(rel, cfg: dict) -> None:
    """安全相关的默认值：控制面板与局域网代理的暴露面。"""
    controller = str(cfg.get("external-controller", ""))
    secret = str(cfg.get("secret", "") or "")
    if controller and not controller.startswith(("127.0.0.1", "localhost", "[::1]")):
        if not secret:
            add("WARN", rel, 0,
                f"external-controller 监听 {controller} 且 secret 为空："
                "同网段任何人都能无密码访问控制面板，建议改为 127.0.0.1:9090 并设置 secret")
    if cfg.get("allow-lan") is True:
        auth = cfg.get("authentication") or []
        if not auth or any("name:passwd" in str(a) for a in auth):
            add("WARN", rel, 0,
                "allow-lan 已开启但代理认证仍是占位符 name:passwd，"
                "局域网内任何人可白嫖机场流量，请改成真实凭据")

    dns = cfg.get("dns") or {}
    ns = [str(x) for x in (dns.get("nameserver") or [])]
    if any(n.startswith("127.0.0.1:5225") for n in ns):
        add("INFO", rel, 0, "DNS 指向 127.0.0.1:5225，需要设备上有对应的本地 DNS 服务，否则解析失败")


# --------------------------------------------------------------------------
# 4. subconverter 模板（configs/subconverter/*.ini）
# --------------------------------------------------------------------------
def check_subconverter_templates(files: list[Path]) -> None:
    for path in files:
        if path.suffix != ".ini":
            continue
        rel = path.relative_to(ROOT)
        defined: dict[str, int] = {}
        ruleset_groups: list[tuple[str, int]] = []
        group_refs: list[tuple[str, str, int]] = []

        for lineno, raw in enumerate(read_text(path).splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith((";", "#", "//")):
                continue
            if line.startswith("custom_proxy_group="):
                body = line.split("=", 1)[1]
                parts = body.split("`")
                name = parts[0].strip()
                defined[name] = lineno
                for part in parts[1:]:
                    for ref in re.findall(r"\[\]([^`]+)", part):
                        ref = ref.strip()
                        if ref and not ref.startswith(("[]",)):
                            group_refs.append((name, ref, lineno))
            elif line.startswith(("ruleset=", "ruleset =")) or "ruleset=" in line:
                body = line.split("ruleset=", 1)[1]
                name = body.split(",", 1)[0].strip()
                if name:
                    ruleset_groups.append((name, lineno))

        for name, lineno in ruleset_groups:
            if name not in defined:
                add("ERROR", rel, lineno,
                    f"ruleset 指向的策略组「{name}」在 custom_proxy_group 中没有定义")
        for owner, ref, lineno in group_refs:
            if ref in BUILTIN_POLICIES or re.match(r"^(DIRECT|REJECT)$", ref):
                continue
            if ref not in defined:
                add("WARN", rel, lineno,
                    f"策略组「{owner}」里引用的「{ref}」没有定义（subconverter 会忽略该引用）")
        if not defined:
            add("WARN", rel, 0, "没有解析到任何 custom_proxy_group 定义，请确认文件格式")


# --------------------------------------------------------------------------
# 5. 外部 URL 可达性（--online）
# --------------------------------------------------------------------------
def collect_external_urls(files: list[Path]) -> list[str]:
    urls: set[str] = set()
    for path in files:
        for line in read_text(path).splitlines():
            stripped = line.lstrip()
            if stripped.startswith(("#", ";", "//")):
                continue
            for url in URL_RE.findall(line):
                url = url.rstrip('",\'')
                if REPO in url:
                    continue  # 自引用由离线检查覆盖
                if not url.startswith("http"):
                    continue
                urls.add(url)
    return sorted(urls)


def _dns_query_packet(name: str = "example.com") -> bytes:
    """构造一个最小的 DNS 查询报文（A 记录），用于探测 DoH 端点。"""
    header = struct.pack(">HHHHHH", 0x1234, 0x0100, 1, 0, 0, 0)
    qname = b"".join(bytes([len(p)]) + p.encode() for p in name.split(".")) + b"\x00"
    return header + qname + struct.pack(">HH", 1, 1)


def probe(url: str, timeout: int = 20) -> tuple[str, int | str]:
    original = url
    headers = {"User-Agent": "validate.py"}
    method, data = "HEAD", None
    # DoH 端点（…/dns-query）是 DNS 查询 API：直接 GET/HEAD 会返回 400，
    # 必须发一个真正的查询报文（各家 JSON API 路径不统一，线格式才是通用做法）
    if url.rstrip("/").endswith("/dns-query"):
        headers = {"User-Agent": "validate.py",
                   "content-type": "application/dns-message",
                   "accept": "application/dns-message"}
        method, data = "POST", _dns_query_packet()

    req = Request(url, method=method, headers=headers, data=data)
    try:
        with urlopen(req, timeout=timeout) as resp:
            return original, resp.status
    except HTTPError as exc:
        if exc.code in (403, 405):  # 部分 CDN 不允许 HEAD，退回 Range GET
            try:
                req = Request(url, headers={"User-Agent": "validate.py", "Range": "bytes=0-0"})
                with urlopen(req, timeout=timeout) as resp:
                    return original, resp.status
            except Exception as exc2:  # noqa: BLE001
                return original, str(exc2)
        return original, exc.code
    except (URLError, TimeoutError) as exc:
        return original, str(exc.reason if isinstance(exc, URLError) else exc)


def check_online(files: list[Path]) -> None:
    urls = collect_external_urls(files)
    print(f"探测 {len(urls)} 个外部 URL …")
    with ThreadPoolExecutor(max_workers=8) as pool:
        for url, status in pool.map(probe, urls):
            if isinstance(status, int) and 200 <= status < 300:
                # 注意：健康检查用的 generate_204 按设计返回 204，属于正常
                add("INFO", "外部链接", 0, f"[{status}] {url}")
            elif isinstance(status, int) and 400 <= status < 500:
                add("ERROR", "外部链接", 0, f"[{status}] {url}（链接已失效，需要更换来源）")
            else:
                add("WARN", "外部链接", 0, f"[{status}] {url}（可能是临时故障，下次再确认）")


# --------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(description="校验 openclash-rules 仓库")
    parser.add_argument("--online", action="store_true", help="额外探测外部 URL 可达性")
    args = parser.parse_args()

    files = source_files()
    check_self_references(files)
    check_unused_rule_files(referenced_rule_files(files))
    check_rule_lists()
    check_mihomo_configs()
    check_subconverter_templates(files)
    if args.online:
        check_online(files)

    for level in ("ERROR", "WARN", "INFO"):
        items = find_issues(level)
        if not items:
            continue
        print(f"\n=== {level} ({len(items)}) ===")
        for _, path, line, message in items:
            where = f"{path}:{line}" if line else path
            print(f"  {where}  {message}")

    errors = len(find_issues("ERROR"))
    warnings = len(find_issues("WARN"))
    print(f"\n结果：{errors} 个错误，{warnings} 个警告（共检查 {len(files)} 个文件）")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
