#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""漫画规则集同步（MangaCN / MangaProxy）：把 v2fly 上游的漫画域名增量合并进自动同步区。

用法：
    python scripts/gen_manga_rules.py            # 检查模式：只报告变化（有变化退出码 1）
    python scripts/gen_manga_rules.py --apply    # 有变化时写回文件
结构、安全设计与通用逻辑见 scripts/rules_sync.py。
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rules_sync import ROOT, Config, Source, Target, cli  # noqa: E402

V2FLY = "https://cdn.jsdelivr.net/gh/v2fly/domain-list-community@master/{rel}"
V2FLY_RAW = "https://raw.githubusercontent.com/v2fly/domain-list-community/master/{rel}"


def v2fly(rel, **kw):
    return Source(name=f"v2fly {rel}", urls=[V2FLY.format(rel=rel), V2FLY_RAW.format(rel=rel)], **kw)


# 拷贝漫画：copy 数字别名是官方给大陆用的入口，进 CN；其余（主域 / 图片域）进代理
COPY_CN_ALIASES = ["2025copy.com", "copy-manga.com", "copy20.com", "copy2000.online"]

# 已确认失效、但上游还留着的域名：不入清单（2026-10-05 三方 DoH 复测，证据见 manga-sites.md §8）
DEAD_EXCLUDE = {
    "18comic.company", "boylove.live", "jmcomic.group", "jmcomic.city", "jmcomic1.city",
    "cdnxxx-proxy.co", "cdnxxx-proxy.xyz", "jmapiproxy4.cc", "jmapiproxyxxx.vip",
    "jmapinode1.top", "jmapinode2.top", "jmapinode3.top",
    "cdnmhws.cc", "jmapiproxy1.cc", "jmapiproxy3.cc", "mangafuna.xyz",
}

HEADER_CN = """# MangaCN.list —— 漫画站域名清单 · 国内直连
#
# 内容：漫画/网漫/同人站点中「用国内网络可以直接访问」的域名（按域名分，不按站点分——
#       同一站点的直连域与需代理域会分别落在本清单与 MangaProxy.list）。
# 用法：RULE-SET 指到直连策略组，例：
#         - RULE-SET,manga_cn,🎯 全球直连
# 来源：manga-sites.md（根目录，729 域名调研 + 实测）；自动同步区来自 v2fly/domain-list-community。
# 维护：手工条目写在「手工维护区」（脚本不动）；「自动同步区」由 scripts/gen_manga_rules.py
#       每日重写（CI: .github/workflows/update-rules.yml），会随上游增删，勿手改。
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
#       每日重写（CI: .github/workflows/update-rules.yml），会随上游增删，勿手改。
#       想固定某条不被上游影响，把它挪到手工区。
#
# 高变动提示：韩国盗版站（mato31 / newto31 / bookto31 / toonkor### 等）与 JM / raw 系
#   域名轮换很快，清单里收了「稳定入口 + 关键词兜底」；长期跟进入口见 manga-sites.md §3/§10。
# 共用域未收录（避免连带非漫画流量，需要时自行加）：Kindle=amazon.co.jp、
#   Kobo=www.kobo.com、U-NEXT=video.unext.jp。ebookjapan 的图片 CDN
#   （prod-contents-br-page.akamaized.net）因是专用主机名，已收录。
"""

CONFIG = Config(
    name="漫画规则集（MangaCN / MangaProxy）",
    dead_exclude=DEAD_EXCLUDE,
    targets=[
        Target(
            key="cn",
            path=ROOT / "rules" / "MangaCN.list",
            header=HEADER_CN,
            sources=[
                v2fly("data/manhuagui"),
                v2fly("data/manhuaren"),
                v2fly("data/copymanga", only=COPY_CN_ALIASES),
            ],
        ),
        Target(
            key="proxy",
            path=ROOT / "rules" / "MangaProxy.list",
            header=HEADER_PROXY,
            sources=[
                v2fly("data/18comic"),
                v2fly("data/copymanga", exclude=COPY_CN_ALIASES),
                v2fly("data/haitang"),
                v2fly("data/boylove"),
                v2fly("data/ehentai"),
                v2fly("data/pixiv"),
                v2fly("data/dlsite"),
                v2fly("data/dmm-porn"),
            ],
        ),
    ],
)

if __name__ == "__main__":
    sys.exit(cli(CONFIG))
