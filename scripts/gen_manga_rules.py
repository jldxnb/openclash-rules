#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""漫画规则集同步脚本：把上游域名增量合并进 rules/MangaCN.list / rules/MangaProxy.list。

两个清单文件的结构（脚本按标记定位，标记缺失会拒绝写入）：

    # 头部说明（脚本不碰）
    # ===== 手工维护区开始（脚本原样保留，按行增删即可）=====
    DOMAIN-SUFFIX,xxx        ← 手工条目，脚本永远不动
    # ===== 手工维护区结束 =====
    # ===== 自动同步区开始（由 scripts/gen_manga_rules.py 重写，勿手改）=====
    DOMAIN-SUFFIX,yyy        ← 上游增量，每次运行整个重算（会随上游增删）
    # ===== 自动同步区结束 =====

用法：
    python scripts/gen_manga_rules.py            # 检查模式：只报告变化，不写文件（有变化退出码 1）
    python scripts/gen_manga_rules.py --apply    # 有变化时写回文件
退出码：0 = 无变化 / 已写入；1 = 检查模式发现变化；2 = 清单文件缺标记（结构损坏，未写入）

上游与归属策略（改这里 = 改分流语义）：
    - 每个上游文件映射到一个目标清单；only/exclude 用于拆同一个文件里的不同归属。
    - 想固定某个域名不被上游增删影响，把它挪到对应文件的「手工维护区」。
"""
import argparse
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "openclash-rules-manga-sync/1.0 (+https://github.com/jldxnb/openclash-rules)"

MANUAL_START = "# ===== 手工维护区开始（脚本原样保留，按行增删即可）====="
MANUAL_END = "# ===== 手工维护区结束 ====="
AUTO_START = "# ===== 自动同步区开始（由 scripts/gen_manga_rules.py 重写，勿手改）====="
AUTO_END = "# ===== 自动同步区结束 ====="

# ===== 头部模板（只在文件不存在时用来起头；已存在则原样保留头部）=====
HEADER_CN = """# MangaCN.list —— 漫画站域名清单 · 国内直连
#
# 内容：漫画/网漫/同人站点中「用国内网络可以直接访问」的域名（按域名分，不按站点分——
#       同一站点的直连域与需代理域会分别落在本清单与 MangaProxy.list）。
# 用法：RULE-SET 指到直连策略组，例：
#         - RULE-SET,manga_cn,🎯 全球直连
# 来源：manga-sites.md（根目录，729 域名调研 + 实测）；自动同步区来自 v2fly/domain-list-community。
# 维护：手工条目写在「手工维护区」（脚本不动）；「自动同步区」由 scripts/gen_manga_rules.py
#       每日重写（CI: .github/workflows/update-manga-rules.yml），会随上游增删，勿手改。
#       想固定某条不被上游影响，把它挪到手工区。
# 注意：暂未在 configs/ 里引用时，validate.py 会提示「未被引用」，属正常提示而非错误。
#
# 已知取舍（要改就是改分流语义，留意）：
#   - 拷贝漫画：按官方公告，大陆入口 copy4000.com 等 copy 系别名收录在本清单；
#     主域 mangacopy.com / copymanga.site 与图片 CDN mangafunb.fun 归 MangaProxy.list。
#     若你在大陆实测 mangafunb.fun 直连也正常，把它挪进本清单手工区。
#   - 漫画柜 / 漫画DB / 包子漫画 系为境外托管但国内常用的站，按「国内可直连」收录；
#     若实测直连不通，把它们挪到 MangaProxy.list 手工区。
"""

HEADER_PROXY = """# MangaProxy.list —— 漫画站域名清单 · 海外代理
#
# 内容：漫画/网漫/同人站点中「需要走代理」的域名：日/韩官方平台与商店、聚合与生肉站、
#       成人/本子站、被墙的汉化站域名（如拷贝漫画主域）。国内可直连的部分见 MangaCN.list。
# 用法：RULE-SET 指到代理策略组，例：
#         - RULE-SET,manga_proxy,🚀 节点选择      （想细分可再拆，如日漫走 🇯🇵 日本节点）
# 来源：manga-sites.md（根目录，729 域名调研 + 实测）；自动同步区来自 v2fly/domain-list-community。
# 维护：手工条目写在「手工维护区」（脚本不动）；「自动同步区」由 scripts/gen_manga_rules.py
#       每日重写（CI: .github/workflows/update-manga-rules.yml），会随上游增删，勿手改。
#       想固定某条不被上游影响，把它挪到手工区。
#
# 高变动提示：韩国盗版站（mato31 / newto31 / bookto31 / toonkor### 等）与 JM / raw 系
#   域名轮换很快，清单里收了「稳定入口 + 关键词兜底」；长期跟进入口见 manga-sites.md §3/§10。
"""

# ===== 上游配置 =====
# v2fly/domain-list-community 的 data/ 文件
UPSTREAM_FILES = {
    "18comic": "data/18comic",
    "copymanga": "data/copymanga",
    "haitang": "data/haitang",
    "boylove": "data/boylove",
    "ehentai": "data/ehentai",
    "pixiv": "data/pixiv",
    "dlsite": "data/dlsite",
    "dmm-porn": "data/dmm-porn",
    "manhuagui": "data/manhuagui",
    "manhuaren": "data/manhuaren",
}

# 拷贝漫画：copy 数字别名是官方给大陆用的入口，进 CN；其余（主域/图片域）进代理
COPY_CN_ALIASES = ["2025copy.com", "copy-manga.com", "copy20.com", "copy2000.online"]

# 已确认失效、但上游还留着的域名：不入清单（2026-10-05 三方 DoH 复测，证据见 manga-sites.md §8）
# 上游哪天删了这些域名，本排除表会变成无效条目，可随手清掉。
DEAD_EXCLUDE = {
    # AliDNS 返回污染 IP、Cloudflare/Google 均 NXDOMAIN
    "18comic.company", "boylove.live", "jmcomic.group", "jmcomic1.city",
    "cdnxxx-proxy.co", "cdnxxx-proxy.xyz", "jmapiproxy4.cc", "jmapiproxyxxx.vip",
    "jmapinode1.top", "jmapinode2.top", "jmapinode3.top",
    # 解析存在但无 A 记录 / 暂未启用
    "cdnmhws.cc", "jmapiproxy1.cc", "jmapiproxy3.cc", "mangafuna.xyz",
}

# (上游文件, 目标清单, only, exclude)
UPSTREAM_PLAN = [
    ("manhuagui", "cn", None, None),
    ("manhuaren", "cn", None, None),
    ("copymanga", "cn", COPY_CN_ALIASES, None),
    ("18comic", "proxy", None, None),
    ("copymanga", "proxy", None, COPY_CN_ALIASES),
    ("haitang", "proxy", None, None),
    ("boylove", "proxy", None, None),
    ("ehentai", "proxy", None, None),
    ("pixiv", "proxy", None, None),
    ("dlsite", "proxy", None, None),
    ("dmm-porn", "proxy", None, None),
]

TARGETS = {
    "cn": (ROOT / "rules" / "MangaCN.list", HEADER_CN),
    "proxy": (ROOT / "rules" / "MangaProxy.list", HEADER_PROXY),
}

DOMAIN_RE = re.compile(r"^[a-z0-9][a-z0-9.\-]*\.[a-z]{2,}$")


def fetch(rel_path: str):
    """拉上游文件：jsDelivr 优先（国内可达性好），失败退 raw.githubusercontent；各试两次。"""
    urls = [
        f"https://cdn.jsdelivr.net/gh/v2fly/domain-list-community@master/{rel_path}",
        f"https://raw.githubusercontent.com/v2fly/domain-list-community/master/{rel_path}",
    ]
    for url in urls:
        for _ in range(2):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=30) as resp:
                    return resp.read().decode("utf-8", "replace"), url
            except Exception:
                continue
    return None, urls[0]


def parse_v2fly(text: str):
    """解析 v2fly domain-list 格式 → (规则列表, 跳过统计)。
    支持 plain / full: / domain: / keyword:；跳过 regexp: / include: / @ads。
    """
    rules, skipped = [], {"regexp": 0, "include": 0, "ads": 0, "invalid": 0}
    for line in text.split("\n"):
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        item, attrs = parts[0], parts[1:]
        if "@ads" in attrs:
            skipped["ads"] += 1
            continue
        if item.startswith("include:"):
            skipped["include"] += 1
            continue
        if item.startswith("regexp:"):
            skipped["regexp"] += 1
            continue
        if item.startswith("full:"):
            rtype, value = "DOMAIN", item[5:]
        elif item.startswith("keyword:"):
            rtype, value = "DOMAIN-KEYWORD", item[8:]
        elif item.startswith("domain:"):
            rtype, value = "DOMAIN-SUFFIX", item[7:]
        else:
            rtype, value = "DOMAIN-SUFFIX", item
        value = value.lower().strip(". ")
        if not value:
            continue
        if rtype == "DOMAIN-KEYWORD":
            rules.append((rtype, value))
        elif DOMAIN_RE.match(value):
            rules.append((rtype, value))
        else:
            skipped["invalid"] += 1
    return rules, skipped


def parse_rules(lines):
    """把文件内容拆成 (类型, 值) 列表（跳过注释、空行、非域名类规则）。"""
    out = []
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        parts = [p.strip() for p in s.split(",")]
        if len(parts) >= 2 and parts[0].upper().startswith("DOMAIN"):
            out.append((parts[0].upper(), parts[1].lower()))
    return out


def covered_by(domain: str, others) -> bool:
    """domain 是否能被 others 中某个更短的父后缀覆盖（严格父级，不含自身）。"""
    parts = domain.split(".")
    for i in range(1, len(parts)):
        if ".".join(parts[i:]) in others:
            return True
    return False


def compact_suffixes(entries):
    """同一清单内压缩：DOMAIN-SUFFIX 条目若被同表的父后缀覆盖则去掉；顺带按 (类型,值) 去重排序。"""
    suffix_set = {v for t, v in entries if t == "DOMAIN-SUFFIX"}
    kept, dropped = [], []
    for rule in sorted(set(entries)):
        t, v = rule
        if t == "DOMAIN-SUFFIX" and covered_by(v, suffix_set):
            dropped.append(rule)
            continue
        kept.append(rule)
    return kept, dropped


def read_target(path: Path, header: str):
    """读清单文件 → (头部行, 手工区文本行)。文件不存在时用模板起头。"""
    if not path.exists():
        return header.rstrip("\n").split("\n"), []
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    for marker in (MANUAL_START, MANUAL_END, AUTO_START, AUTO_END):
        if marker not in text:
            raise SystemExit(f"[结构错误] {path.name} 缺少标记：{marker}（未做任何写入）")
    header_lines = text.split(MANUAL_START, 1)[0].rstrip("\n").split("\n")
    manual = text.split(MANUAL_START, 1)[1].split(MANUAL_END, 1)[0].strip("\n").split("\n")
    return header_lines, [ln.rstrip() for ln in manual]


def render(header_lines, manual_lines, auto_rules):
    out = list(header_lines)
    out.append(MANUAL_START)
    out.extend(manual_lines)
    out.append(MANUAL_END)
    out.append("")
    out.append(AUTO_START)
    for t, v in auto_rules:
        out.append(f"{t},{v}")
    out.append(AUTO_END)
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description="同步漫画规则集的自动同步区")
    ap.add_argument("--apply", action="store_true", help="写回文件（默认只检查报告）")
    ap.add_argument("--allow-partial", action="store_true",
                    help="有上游拉取失败时也照常写入（默认拒绝，避免把失败当成“域名消失”而误删条目）")
    args = ap.parse_args()

    # 1) 先读两个文件的头部与手工区
    docs = {}
    for key, (path, header) in TARGETS.items():
        docs[key] = read_target(path, header)
    manual_suffix_sets = {}
    manual_value_sets = {}
    for key, (header_lines, manual_lines) in docs.items():
        entries = parse_rules(manual_lines)
        manual_value_sets[key] = {v for _, v in entries}
        manual_suffix_sets[key] = {v for t, v in entries if t == "DOMAIN-SUFFIX"}

    # 2) 拉上游 → 按计划分到两个清单
    report = []
    buckets = {"cn": [], "proxy": []}
    fetched_ok = 0
    failed = []
    for name, target, only, exclude in UPSTREAM_PLAN:
        text, used_url = fetch(UPSTREAM_FILES[name])
        if text is None:
            failed.append(UPSTREAM_FILES[name])
            report.append(f"[警告] 上游 {UPSTREAM_FILES[name]} 拉取失败（已跳过）")
            continue
        fetched_ok += 1
        rules, skipped = parse_v2fly(text)
        picked = 0
        for t, v in rules:
            if v in DEAD_EXCLUDE:
                continue
            if only is not None and not any(v == o or v.endswith("." + o) for o in only):
                continue
            if exclude is not None and any(v == e or v.endswith("." + e) for e in exclude):
                continue
            buckets[target].append((t, v))
            picked += 1
        note = "".join(f"/{k}×{v}" for k, v in skipped.items() if v)
        report.append(f"[上游] {UPSTREAM_FILES[name]} → {target}: {picked} 条{('（跳过 ' + note + '）') if note else ''}")

    # 3) 生成两个清单的正式内容
    rendered = {}
    stat = {}
    for key in ("cn", "proxy"):
        other = "proxy" if key == "cn" else "cn"
        kept, dropped_manual, dropped_other = [], [], []
        for rule in sorted(set(buckets[key])):
            t, v = rule
            if v in manual_value_sets[key] or covered_by(v, manual_value_sets[key]):
                dropped_manual.append(rule)
                continue
            if v in manual_value_sets[other] or covered_by(v, manual_value_sets[other]):
                dropped_other.append(rule)
                continue
            kept.append(rule)
        kept, dropped_self = compact_suffixes(kept)
        header_lines, manual_lines = docs[key]
        rendered[key] = render(header_lines, manual_lines, kept)
        stat[key] = (len(manual_lines), len(kept), dropped_self, dropped_manual, dropped_other)

    # 4) 对比新旧 → 是否变化 / 新增了什么
    changes = []
    for key, (path, _h) in TARGETS.items():
        old = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n") if path.exists() else ""
        new = rendered[key]
        if old == new:
            continue
        old_auto = set(parse_rules(old.split(AUTO_START, 1)[1].split(AUTO_END, 1)[0].split("\n"))) if AUTO_START in old else set()
        new_auto = set(parse_rules(new.split(AUTO_START, 1)[1].split(AUTO_END, 1)[0].split("\n")))
        added = sorted(f"{t},{v}" for t, v in new_auto - old_auto)
        removed = sorted(f"{t},{v}" for t, v in old_auto - new_auto)
        changes.append((key, path, added, removed))

    print(f"上游拉取：{fetched_ok}/{len(UPSTREAM_PLAN)} 成功")
    for line in report:
        print(line)
    if failed and args.apply and not args.allow_partial:
        print(f"== 有上游拉取失败（{', '.join(failed)}），为避免误删条目本次不写入；"
              f"确认没问题可加 --allow-partial 强制 ==")
        return 3
    for key in ("cn", "proxy"):
        m, a, d_self, d_m, d_o = stat[key]
        print(f"[{key}] 手工 {m} 行 / 自动 {a} 条（同表压缩去掉 {len(d_self)}、被手工覆盖 {len(d_m)}、被另一清单覆盖 {len(d_o)}）")

    if not changes:
        print("== 无变化，两个清单都是最新的 ==")
        return 0

    for key, path, added, removed in changes:
        print(f"== {path.name}：新增 {len(added)} 条，移除 {len(removed)} 条 ==")
        for r in added[:40]:
            print(f"   + {r}")
        if len(added) > 40:
            print(f"   + …（其余 {len(added) - 40} 条省略）")
        for r in removed[:20]:
            print(f"   - {r}")
        if len(removed) > 20:
            print(f"   - …（其余 {len(removed) - 20} 条省略）")

    if not args.apply:
        print("（检查模式：未写文件；加 --apply 写入）")
        return 1

    for key, path, _a, _r in changes:
        path.write_text(rendered[key].replace("\n", "\r\n"), encoding="utf-8", newline="")
        print(f"已写入 {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
