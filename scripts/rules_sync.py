#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""漫画 / 动漫规则集同步的公共实现：把上游域名增量合并进 rules/*.list 的「自动同步区」。

清单文件结构（脚本按标记定位，标记缺失会拒绝写入）：

    # 头部说明（脚本不碰）
    # ===== 手工维护区开始（脚本原样保留，按行增删即可）=====
    DOMAIN-SUFFIX,xxx        ← 手工条目，脚本永远不动
    # ===== 手工维护区结束 =====
    # ===== 自动同步区开始（由 scripts/gen_*_rules.py 重写，勿手改）=====
    DOMAIN-SUFFIX,yyy        ← 上游增量，每次运行整个重算（会随上游增删）
    # ===== 自动同步区结束 =====

具体「清单 / 上游」配置在 gen_manga_rules.py 与 gen_anime_rules.py 里；本模块只提供机器。
安全设计：① 只重写自动区，手工区原样保留；② 任何上游拉取失败则拒绝写入（除非 --allow-partial）；
③ 自动区条目数骤降（>40%）时拒绝写入（突变保护，防上游改版把清单清空，除非 --force）。
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "openclash-rules-sync/1.0 (+https://github.com/jldxnb/openclash-rules)"

MANUAL_START = "# ===== 手工维护区开始（脚本原样保留，按行增删即可）====="
MANUAL_END = "# ===== 手工维护区结束 ====="
AUTO_START = "# ===== 自动同步区开始（由 scripts/gen_*_rules.py 重写，勿手改）====="
AUTO_END = "# ===== 自动同步区结束 ====="

DOMAIN_RE = re.compile(r"^[a-z0-9][a-z0-9.\-]*\.[a-z]{2,}$")


@dataclass
class Source:
    """一个上游文件。kind: v2fly（domain-list 格式）| markdown（按小节标题抓链接域名）"""
    name: str
    urls: list[str]
    kind: str = "v2fly"
    sections: list[str] = field(default_factory=list)   # markdown 用：要抓哪些小节标题（子串匹配）
    skip_hosts: str = ""                                # markdown 用：跳过这些域名的正则
    only: list[str] = field(default_factory=list)       # 只收这些（域或其后缀）
    exclude: list[str] = field(default_factory=list)    # 排除这些（域或其后缀）


@dataclass
class Target:
    key: str
    path: Path
    header: str
    sources: list[Source] = field(default_factory=list)


@dataclass
class Config:
    name: str
    targets: list[Target]
    dead_exclude: set[str] = field(default_factory=set)
    sanity_ratio: float = 0.6      # 自动区条目数低于上次的该比例 → 拒绝写入


# ---------------- 基础 ----------------
def fetch(urls: list[str], retries: int = 2):
    """按顺序尝试多个 URL（jsDelivr 优先、raw 兜底），各试 retries 次。返回 (文本, 用到的 URL) 或 (None, 最后尝试的 URL)。"""
    last = urls[0]
    for url in urls:
        last = url
        for _ in range(retries):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=30) as resp:
                    return resp.read().decode("utf-8", "replace"), url
            except Exception:
                continue
    return None, last


def parse_v2fly(text: str):
    """解析 v2fly domain-list 格式 → (规则列表, 跳过统计)。支持 plain / full: / domain: / keyword:；
    跳过 regexp: / include: / @ads。"""
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
        if rtype == "DOMAIN-KEYWORD" or DOMAIN_RE.match(value):
            rules.append((rtype, value))
        else:
            skipped["invalid"] += 1
    return rules, skipped


def parse_markdown_sections(text: str, sections: list[str], skip_hosts: str = ""):
    """FMHY 风格 markdown：按小节标题（子串匹配）提取所有 markdown 链接的域名。"""
    lines = text.split("\n")
    secs, cur = [], None
    for ln in lines:
        m = re.match(r"^(#{2,4})\s+(.*)$", ln)
        if m:
            if cur:
                secs.append(cur)
            cur = [m.group(2).strip(), []]
        elif cur is not None:
            cur[1].append(ln)
    if cur:
        secs.append(cur)
    skip = re.compile(skip_hosts) if skip_hosts else None
    out = []
    for title, body in secs:
        if not any(s.lower() in title.lower() for s in sections):
            continue
        for u in re.findall(r"\]\((https?://[^)\s]+)", "\n".join(body)):
            d = re.sub(r"^www\.", "", re.sub(r"https?://", "", u).split("/")[0].lower()).rstrip(".")
            if DOMAIN_RE.match(d) and not (skip and skip.search(d)):
                out.append(d)
    return out


def pick(rules, only, exclude):
    """按 only/exclude（域或其后缀）过滤。"""
    def hit(v, pats):
        return any(v == p or v.endswith("." + p) for p in pats)
    out = []
    for t, v in rules:
        if only and not hit(v, only):
            continue
        if exclude and hit(v, exclude):
            continue
        out.append((t, v))
    return out


# ---------------- 清单读写 ----------------
def parse_rules(lines):
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
    parts = domain.split(".")
    return any(".".join(parts[i:]) in others for i in range(1, len(parts)))


def compact_suffixes(entries):
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
    if not path.exists():
        return header.rstrip("\n").split("\n"), []
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    for marker in (MANUAL_START, MANUAL_END, AUTO_START, AUTO_END):
        if marker not in text:
            raise SystemExit(f"[结构错误] {path.name} 缺少标记：{marker}（未做任何写入）")
    header_lines = text.split(MANUAL_START, 1)[0].rstrip("\n").split("\n")
    manual = text.split(MANUAL_START, 1)[1].split(MANUAL_END, 1)[0].strip("\n").split("\n")
    auto = text.split(AUTO_START, 1)[1].split(AUTO_END, 1)[0].strip("\n").split("\n")
    return header_lines, [ln.rstrip() for ln in manual], [ln.rstrip() for ln in auto if ln.strip()]


def render(header_lines, manual_lines, auto_rules) -> str:
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


# ---------------- 主流程 ----------------
def run(cfg: Config, apply: bool, allow_partial: bool = False, force: bool = False) -> int:
    docs, manual_values, manual_suffixes = {}, {}, {}
    for tg in cfg.targets:
        docs[tg.key] = read_target(tg.path, tg.header)
        entries = parse_rules(docs[tg.key][1])
        manual_values[tg.key] = {v for _, v in entries}
        manual_suffixes[tg.key] = {v for t, v in entries if t == "DOMAIN-SUFFIX"}

    report, failed = [], []
    buckets = {tg.key: [] for tg in cfg.targets}
    for tg in cfg.targets:
        for src in tg.sources:
            text, used = fetch(src.urls)
            if text is None:
                failed.append(f"{src.name}（{tg.key}）")
                report.append(f"[警告] 上游 {src.name} 拉取失败（已跳过）")
                continue
            if src.kind == "v2fly":
                rules, skipped = parse_v2fly(text)
                note = "".join(f"/{k}×{v}" for k, v in skipped.items() if v)
            else:
                rules = [("DOMAIN-SUFFIX", d) for d in parse_markdown_sections(text, src.sections, src.skip_hosts)]
                note = ""
            picked = pick(rules, src.only, src.exclude)
            n = 0
            for t, v in picked:
                if v in cfg.dead_exclude or covered_by(v, cfg.dead_exclude):
                    continue
                buckets[tg.key].append((t, v))
                n += 1
            report.append(f"[上游] {src.name} → {tg.key}: {n} 条{('（跳过 ' + note + '）') if note else ''}")

    rendered, stat, changes = {}, {}, []
    for tg in cfg.targets:
        others = {k: v for k, v in manual_values.items() if k != tg.key}
        kept, dropped_m, dropped_o = [], [], []
        for rule in sorted(set(buckets[tg.key])):
            t, v = rule
            if v in manual_values[tg.key] or covered_by(v, manual_values[tg.key]):
                dropped_m.append(rule)
                continue
            if any(v in ov or covered_by(v, ov) for ov in others.values()):
                dropped_o.append(rule)
                continue
            kept.append(rule)
        kept, dropped_self = compact_suffixes(kept)
        header_lines, manual_lines, prev_auto = docs[tg.key]
        rendered[tg.key] = render(header_lines, manual_lines, kept)
        stat[tg.key] = (len(manual_lines), len(kept), len(prev_auto), dropped_self, dropped_m, dropped_o)
        old = tg.path.read_text(encoding="utf-8-sig").replace("\r\n", "\n") if tg.path.exists() else ""
        if old != rendered[tg.key]:
            old_auto = set(parse_rules(prev_auto))
            new_auto = set(kept)
            changes.append((tg.key, tg.path, sorted(new_auto - old_auto), sorted(old_auto - new_auto),
                            len(prev_auto), len(kept)))

    print(f"== {cfg.name} ==")
    for line in report:
        print(line)
    for tg in cfg.targets:
        m, a, prev, d_self, d_m, d_o = stat[tg.key]
        print(f"[{tg.key}] 手工 {m} 行 / 自动 {a} 条（上次 {prev}；同表压缩 -{len(d_self)}、被手工覆盖 -{len(d_m)}、被另一清单覆盖 -{len(d_o)}）")

    if not changes:
        print("== 无变化 ==")
        return 0

    for key, path, added, removed, prev, now in changes:
        print(f"== {path.name}：新增 {len(added)}，移除 {len(removed)} ==")
        for r in added[:40]:
            print(f"   + {r[0]},{r[1]}")
        for r in removed[:20]:
            print(f"   - {r[0]},{r[1]}")

    if failed and apply and not allow_partial:
        print(f"== 有上游拉取失败（{', '.join(failed)}），为避免误删本次不写入；确认可加 --allow-partial ==")
        return 3
    for key, path, added, removed, prev, now in changes:
        if prev and now < prev * cfg.sanity_ratio and removed and not force:
            print(f"== [突变保护] {path.name} 自动区从 {prev} 掉到 {now}（超 {int((1-cfg.sanity_ratio)*100)}%），"
                  f"疑似上游改版/解析失败，拒绝写入；确认无误可加 --force ==")
            return 4
    if not apply:
        print("（检查模式：未写文件；加 --apply 写入）")
        return 1

    by_key = {k: (p, r) for k, p, _a, _r, _p, _n in changes for r in [rendered[k]]}
    for key, (path, text) in by_key.items():
        path.write_text(text.replace("\n", "\r\n"), encoding="utf-8", newline="")
        print(f"已写入 {path.relative_to(ROOT)}")
    return 0


def cli(cfg: Config) -> int:
    ap = argparse.ArgumentParser(description=f"同步{cfg.name}的自动同步区")
    ap.add_argument("--apply", action="store_true", help="写回文件（默认只检查报告）")
    ap.add_argument("--allow-partial", action="store_true",
                    help="有上游拉取失败时也照常写入（默认拒绝，避免把失败当成“域名消失”误删条目）")
    ap.add_argument("--force", action="store_true", help="跳过突变保护（自动区条目数骤降时也写入）")
    args = ap.parse_args()
    return run(cfg, apply=args.apply, allow_partial=args.allow_partial, force=args.force)
