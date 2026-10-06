#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""动漫规则集同步（AnimeCN / AnimeProxy）：把 FMHY 上游的动漫域名增量合并进自动同步区。

自动上游说明：FMHY（fmhy.net，FMHY/FMHY wiki 的 Streaming 页）的四个动漫小节
（Anime Streaming / Downloading / Torrenting / Tracking）持续跟踪海外动漫站的**当前域名**，
聚合站换域后这里会自动跟上——这正是「聚合站域名高频轮换」的自动维护手段。
国内站（AnimeCN）都是稳定的大平台域名，不设自动上游，全靠手工区维护。

用法：
    python scripts/gen_anime_rules.py            # 检查模式：只报告变化（有变化退出码 1）
    python scripts/gen_anime_rules.py --apply    # 有变化时写回文件
结构、安全设计与通用逻辑见 scripts/rules_sync.py。
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rules_sync import ROOT, Config, Source, Target, cli  # noqa: E402

# FMHY 的 wiki 页（jsDelivr 不服务 wiki，raw 是唯一入口；CI 在 GitHub 上跑，raw 稳定）
FMHY_STREAMING = "https://raw.githubusercontent.com/wiki/fmhy/FMHY/Streaming.md"

# 小节标题（子串匹配）：Anime Streaming 也会覆盖 Anime Streaming Apps
FMHY_ANIME_SECTIONS = ["Anime Streaming", "Anime Downloading", "Anime Torrenting", "Anime Tracking"]

# FMHY 里顺带出现的通用/社交/工具域名，跳过（它们不属于动漫站）；用 re.search，
# 所以「cse.google.com」「docs.google.com」这类子域也会命中
FMHY_SKIP_HOSTS = (
    r"(^|\.)(github\.com|discord\.(gg|com)|reddit\.com|t\.me|telegram\.me|youtube\.com|google\.com|"
    r"rentry\.co|greasyfork\.org|x\.com|twitter\.com|patreon\.com|ko-fi\.com|"
    r"wikipedia\.org|fmhy\.net|trakt\.tv|simkl\.com|anilist\.co|myanimelist\.net)$"
    r"|^(api|cdn|static)\."
)

# 已确认失效 / 仿冒 / 停运：上游若还留着也不收（2026-10-06 调研，证据见 anime-sites.md §7）
DEAD_EXCLUDE = {"2dgal.com", "36dm.club", "36dm.com", "36dm.net", "acgnx.club", "acgnx.eu",
    "acgnx.net", "acgnx.pro", "acgnx.top", "acgnx.xyz", "acgrip.com",
    "anime-times.jp", "anime4up.tv", "animedao.to", "animefox.io", "animekai.to",
    "animekisa.tv", "animelab.com", "animeskip.io", "anitaku.bz", "anitaku.pe", "anitaku.to",
    "aniwatch.to", "aniwatchtv.to", "aniwave.live", "aniwave.to", "anix.me", "ayakawa.moe",
    "cn.nyaa.net", "dm519.fans", "dm530.com", "dm530w.org", "dmhy.b168.net",
    "dmhy.gate.flag.moe", "dmhy.ye1213.com", "dmla.fans", "dmzj.com", "funimation.com",
    "gogo-load.com", "gogoanime.vc", "gogoanime3.co", "gogocdn.net", "gyao.yahoo.co.jp",
    "hanime1.one", "hanime1.org", "hanime1.pw", "hentaidude.com", "hentaidude.net",
    "hentaidude.to", "hentaihaven.org", "hianime.to", "huameng.net", "jysub.com", "jysub.net",
    "jysub.org", "kaido.to", "kitauji.net", "lightnovel.us", "lknovel.cn", "loli.house",
    "lolihouse.cafe", "mikanani.tv", "moonsub.org", "nyaa.eu", "nyaa.net", "nyaa.se",
    "paravi.jp", "popgo.net", "saku.rip", "sakurato.com", "sakurato.moe", "sakurato.net",
    "sccqygs.com", "shikimori.me", "sub.jysub.net", "sumisora.org", "sweet-sub.com",
    "tsdm.live", "tsdm.love", "tsdm39.net", "tsdm39.org", "uha-c9.com", "v.vrv.co", "vrv.co",
    "wakanim.tv", "ww38.aniwave.to", "yhdmp.net", "zoro.to", "zzzfun.one"
}

HEADER_CN = """# AnimeCN.list —— 动漫站域名清单 · 国内直连
#
# 内容：动漫（番剧/动画）站点中「用国内网络可以直接访问」的域名——国内视频平台的动漫区
#       （B站/爱奇艺/腾讯视频/优酷/芒果/AcFun/咪咕/乐视/搜狐/PPTV/弹弹play 等）
#       及其图片/视频 CDN、国际版里实测未被墙的域名（iq.com / wetv.vip / youku.tv，
#       依据 GreatFire 未封锁记录）、蜜柑计划的国内入口 mikanime.tv。
# 用法：RULE-SET 指到直连策略组，例：
#         - RULE-SET,anime_cn,🎯 全球直连
# 来源：anime-sites.md（根目录，736 域名调研 + 实测）；本清单无自动上游（国内站域名稳定）。
# 维护：直接改「手工维护区」即可（脚本不动它）。
# 注意：暂未在 configs/ 里引用时，validate.py 会提示「未被引用」，属正常提示而非错误。
#
# 已知取舍：
#   - iq.com / wetv.vip / youku.tv 是「大陆平台的国际版」，实测未被墙（GreatFire），
#     按直连收；若你实测不畅，把它们挪到 AnimeProxy.list 手工区。
#   - 中文动漫聚合站（樱花/风车/AGE/稀饭等）虽然面向大陆用户，但托管墙外、未验证直连，
#     统一放 AnimeProxy.list 的「代理·存疑」区（实测直连可用再挪到本清单）。
"""

HEADER_PROXY = """# AnimeProxy.list —— 动漫站域名清单 · 海外代理
#
# 内容：动漫（番剧/动画）站点中「需要走代理」的域名：日系与海外正版平台、海外聚合站、
#       BT/字幕组站、追番社区、成人向动漫。国内可直连的部分见 AnimeCN.list。
# 用法：RULE-SET 指到代理策略组，例：
#         - RULE-SET,anime_proxy,🚀 节点选择      （想细分可再拆，如日漫走 🇯🇵 日本节点）
# 维护：
#   - 「手工维护区」脚本不动，随便改；
#   - 「自动同步区」由 scripts/gen_anime_rules.py 重写（CI: .github/workflows/update-rules.yml，
#     每天一次）：来源是 FMHY 的 Anime Streaming / Downloading / Torrenting / Tracking 四个小节，
#     聚合站换域后这里会跟着更新；想固定某条不被上游影响，把它挪到手工区。
#
# 已知取舍：
#   - 「代理·存疑」区：面向大陆用户的中文聚合站（樱花/风车/AGE/稀饭/次元城等），托管墙外、
#     未验证直连，默认按代理放；你实测直连可用的话，把它挪到 AnimeCN.list 手工区。
#   - 屏蔽 / 限制日本 IP 的站（hanime1 家族、hanime.tv 系，证据见 anime-sites.md §5/§8.4）
#     就收在本清单尾部：原 rules/AnimeNoJP.list（更早叫 NoJP.list）于 2026-10-06 删除、
#     内容并入本清单。配置里 anime_proxy 排在漫画清单之前命中，它们仍落「🎌 漫画动漫」
#     ——该组默认就是非日本链。
#   - 共用域未收录：Netflix / Disney+ / Prime Video 这类大平台官网与 Amazon、Kobo 等综合商城
#     不收（会连带非动漫流量）；它们的 CDN 单独出现在 FMHY 里的专用子域会被自动区收进来。
"""

CONFIG = Config(
    name="动漫规则集（AnimeCN / AnimeProxy）",
    dead_exclude=DEAD_EXCLUDE,
    sanity_ratio=0.6,
    targets=[
        Target(key="cn", path=ROOT / "rules" / "AnimeCN.list", header=HEADER_CN, sources=[]),
        Target(
            key="proxy",
            path=ROOT / "rules" / "AnimeProxy.list",
            header=HEADER_PROXY,
            sources=[
                Source(
                    name="FMHY Streaming（Anime 小节）",
                    urls=[FMHY_STREAMING],
                    kind="markdown",
                    sections=FMHY_ANIME_SECTIONS,
                    skip_hosts=FMHY_SKIP_HOSTS,
                ),
            ],
        ),
    ],
)

if __name__ == "__main__":
    sys.exit(cli(CONFIG))
