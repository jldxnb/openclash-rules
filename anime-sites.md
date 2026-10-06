# 动漫站点域名清单（Clash / mihomo 分流用）

> 生成日期：**2026-10-06** ｜ 用途：动漫（番剧 / 动画）站点域名，供分流规则参考
> 全部域名来自当日联网调研（每条附来源 URL），并在当天做了统一实测（方法见 §6）
> 同类文档：[manga-sites.md](manga-sites.md)（漫画 / 网漫 / 同人，2026-10-05）

## 阅读说明

### 四类标记

| 标记 | 含义 | 用法 |
|---|---|---|
| 🟢 **直连** | 国内网络可直连（国内平台，或 GreatFire 未封锁 + 证据） | 建议指向直连策略组（如 🎯 全球直连） |
| 🔴 **代理** | 需代理（被墙 / 海外服务 / 地区限制） | 建议指向代理组（如 🚀 节点选择） |
| 🟡 **代理·存疑** | 面向大陆用户但托管墙外、或未验证直连 | **默认按代理放**；实测直连可用再挪去直连 |
| ⚠️ **非日本** | 屏蔽 / 限制日本 IP 的站（hanime1 家族等） | 必须走「非日本节点」组（现为 `rules/AnimeNoJP.list`，原 NoJP.list） |

### 分流建议

- 优先 `DOMAIN-SUFFIX`；**图片 / 视频 CDN 单独列出的必须收**（漏了会「网页能开、图挂」）。
- **同一站的国内入口与海外入口要分开**，本清单里就有三个典型：
  - 蜜柑计划：`mikanime.tv` 直连（官方标注"仅限国内使用"）／`mikanani.me` 已被墙；
  - hanime1：`hanime1.me` 非日本节点可用／`hanime1.com` 是官方给"只有日本节点"用户的替代域名；
  - ACGNX：`share.acgnx.cc` / `.net` 官方定位"仅供大陆地区访问"，`acgnx.se` 为源站。
- 本清单 2026 年最大的变化：**英文聚合站成批阵亡**（HiAnime/AniWatch、AniWave、AnimeKai、Gogoanime、KissAnime、AniDude 等，见 §7），主流已换成 `aniwaves.ru` / `hianimes.ru` 等新站。

### 可靠性声明

- 实测经本机（Windows + 路由器 OpenClash，**出口是日本**）出网：快测只能证明「站点存活」，**不能证明大陆可达**。「大陆可达性」依据的是官方公告、GreatFire 封锁记录、社区实测（各条目里已注明）。
- 因出口在日本，**看着能打开的站也可能在大陆被墙**——「存疑」类请按代理放，实测后再调整。
- 本清单只做域名收集，不构成对站点内容的背书。

---

## 1. 国内动漫站（国内平台 + 中文聚合）

调研日期: 2026-10-06 | 调研范围: 国内正版平台（动漫区）+ 国内盗版聚合站 + 追番工具 + 已失效站

说明:
- 本机网络流量经路由器代理（出口非大陆），curl 快测结果只反映"经代理可达性"，**超时/000 ≠ 站点死亡**，已逐条标注。
- 「大陆可达性」是综合判断（IP 归属 ip-api 实测 + 官网可访问性 + 常见认知），不是实测大陆直连。
- 盗版聚合站域名轮换极快，任何清单都会过期；失效域名单列一节。

---

#### 哔哩哔哩（B站）
- 类别: 国内正版（番剧/国创）
- 域名: bilibili.com | www.bilibili.com | m.bilibili.com | bangumi.bilibili.com | live.bilibili.com | space.bilibili.com | api.bilibili.com | data.bilibili.com | b23.tv | i0.hdslb.com | i1.hdslb.com | i2.hdslb.com | s1.hdslb.com | bilivideo.com | upos-sz-mirrorcos.bilivideo.com
- 性质: 番剧子域 bangumi.bilibili.com；b23.tv 为短链域；hdslb.com 系图片/静态 CDN；bilivideo.com 系视频 CDN（upos-* 前缀）
- 来源: [bilibili 首页 HTML 实测](https://www.bilibili.com/)（引用 i0/i1/i2/s1.hdslb.com、live/space.bilibili.com）；[bangumi 子域实测](https://bangumi.bilibili.com/) 标题「番剧」；b23.tv 短链 302→www.bilibili.com/video/BV1GJ411x7h7 实测
- 后续更新入口: 无（主域稳定）
- 快测: bilibili.com 301 / api.bilibili.com 301 / i0,i1.hdslb.com 200 / bangumi.bilibili.com 200 / b23.tv 根路径 404、短链 302 / upos-sz-mirrorcos.bilivideo.com 403（存在）/ data.bilibili.com 404（存在）
- 大陆可达性: 直连（境内公司+境内 CDN）
- 备注: b23.tv 是规则常见遗漏项；hdslb.com 建议全系覆盖（i0-i2、s1、data 等）

#### 爱奇艺 iQiyi
- 类别: 国内正版（动漫频道）
- 域名: iqiyi.com | www.iqiyi.com | static.iqiyi.com | mesh.if.iqiyi.com | cache.video.iqiyi.com | so.iqiyi.com | search.video.iqiyi.com | qy.net | iqiyipic.com | img7.iqiyipic.com | pic0.iqiyipic.com | m.iqiyipic.com
- 性质: qy.net 为品牌短域（302→www.iqiyi.com）；iqiyipic.com 系图片 CDN；cache.video.iqiyi.com 视频接口；mesh.if.iqiyi.com 数据接口
- 来源: [iqiyi 首页 HTML 实测](https://www.iqiyi.com/)（引用 static.iqiyi.com、mesh.if.iqiyi.com）；[搜索 API 实测](https://search.video.iqiyi.com/o?if=html5&key=%E7%81%AB%E5%BD%B1%E5%BF%8D%E8%80%85)（返回 JSON 内引用 img7.iqiyipic.com）；qy.net 302 实测
- 后续更新入口: 无
- 快测: iqiyi.com 301 / mesh.if.iqiyi.com 200 / cache.video.iqiyi.com 200 / static.iqiyi.com 404（存在）/ qy.net 302 / pic0.iqiyipic.com 404（存在）/ m.iqiyipic.com 403（存在）
- 大陆可达性: 直连（境内公司）
- 备注: 爱奇艺国际版 iq.com 由另一路调研负责，此处不含

#### 腾讯视频
- 类别: 国内正版（动漫频道）
- 域名: v.qq.com | film.qq.com | puui.qpic.cn | vv.video.qq.com | vfiles.gtimg.cn | vm.gtimg.cn
- 性质: puui.qpic.cn 图片 CDN；vv.video.qq.com 视频接口；vfiles.gtimg.cn/vm.gtimg.cn 腾讯云 CDN
- 来源: [腾讯视频动漫频道 HTML 实测](https://v.qq.com/channel/anime)（引用 puui.qpic.cn×16、vfiles.gtimg.cn×46、vm.gtimg.cn×3）
- 后续更新入口: 无
- 快测: v.qq.com 200 / vv.video.qq.com 200 / puui.qpic.cn 400（存在）/ vfiles.gtimg.cn 400（存在）/ vm.gtimg.cn 200
- 大陆可达性: 直连（境内公司）
- 备注: qpic.cn 为腾讯系共用图片域；gtimg.cn 为腾讯通用 CDN

#### 优酷 Youku
- 类别: 国内正版（动漫区）
- 域名: youku.com | www.youku.com | t.youku.com | acg.youku.com | ykimg.alicdn.com | m.ykimg.com | img.alicdn.com | liangcang-material.alicdn.com
- 性质: acg.youku.com 动漫频道子域；ykimg.alicdn.com/m.ykimg.com 图片 CDN（阿里系）
- 来源: [优酷首页 HTML 实测](https://www.youku.com/)（引用 ykimg.alicdn.com、m.ykimg.com、t.youku.com、acg.youku.com、img.alicdn.com、liangcang-material.alicdn.com）
- 后续更新入口: 无
- 快测: youku.com 302 / ykimg.alicdn.com 403（存在）/ acg.youku.com 403（存在）
- 大陆可达性: 直连（境内公司）
- 备注: acg.youku.com 与动漫内容相关，建议单列覆盖

#### 芒果TV
- 类别: 国内正版（动漫区）
- 域名: mgtv.com | www.mgtv.com | static.hitv.com | img.mgtv.com | tb.mgtv.com | honey.mgtv.com
- 性质: hitv.com 系为芒果静态/CDN 域
- 来源: [芒果TV首页 HTML 实测](https://www.mgtv.com/)（引用 static.hitv.com×41、img.mgtv.com、tb.mgtv.com、honey.mgtv.com）
- 后续更新入口: 无
- 快测: mgtv.com 302 / static.hitv.com 403（存在）/ img.mgtv.com 403（存在）
- 大陆可达性: 直连（境内公司，湖南广电系）
- 备注: 无

#### AcFun（A站）
- 类别: 国内正版/二次元社区（番剧区）
- 域名: acfun.cn | www.acfun.cn | live.acfun.cn | imgs.aixifan.com | tx-free-imgs.acfun.cn | static.yximgs.com
- 性质: imgs.aixifan.com 图片 CDN；static.yximgs.com 为快手系 CDN（AcFun 被快手收购后部分资源走快手 CDN）
- 来源: [AcFun 首页 HTML 实测](https://www.acfun.cn/)（引用 imgs.aixifan.com×98、tx-free-imgs.acfun.cn、live.acfun.cn、static.yximgs.com）
- 后续更新入口: 无
- 快测: acfun.cn 301 / imgs.aixifan.com 200
- 大陆可达性: 直连（境内公司）
- 备注: 视频播放 CDN 未稳定提取到独立域名，暂只列图片/静态域

#### 咪咕视频
- 类别: 国内正版（动漫区）
- 域名: miguvideo.com | www.miguvideo.com | m.miguvideo.com | display-sc.miguvideo.com | img.cmvideo.cn | wapx.cmvideo.cn | migu.cn | www.migu.cn | passport.migu.cn
- 性质: cmvideo.cn 为咪咕核心图片/CDN 域（img.cmvideo.cn 首页引用 2100+ 次）
- 来源: [咪咕视频首页 HTML 实测](https://www.miguvideo.com/)（引用 img.cmvideo.cn、wapx.cmvideo.cn、display-sc.miguvideo.com、passport.migu.cn）；ip-api 实测归属 China Mobile（境内）
- 后续更新入口: 无
- 快测: miguvideo.com 302 / img.cmvideo.cn 200
- 大陆可达性: 直连（中国移动，ip-api 显示境内 IP）
- 备注: 原「咪咕动漫」migudm.cn 实测已转为咪咕新空平台，不再是动漫站；动漫内容走 miguvideo.com 动漫频道

#### 乐视视频
- 类别: 国内正版（动漫区，已边缘化）
- 域名: letv.com | www.letv.com | le.com | www.le.com
- 性质: le.com 为乐视品牌短域，301→www.le.com
- 来源: [letv.com](https://www.letv.com/) 与 [le.com](https://le.com/) 重定向链实测（301→www.le.com 200，SPA 空壳）
- 后续更新入口: 无
- 快测: letv.com 301 / le.com 301→www.le.com 200
- 大陆可达性: 直连（境内公司；业务萎缩）
- 备注: 页面为 JS 单页应用，未能提取到独立图片/视频 CDN 域；社区曾用 letvimg.com，本次实测超时未确认

#### 搜狐视频
- 类别: 国内正版（动漫区）
- 域名: tv.sohu.com | sohu.com | my.tv.sohu.com | itc.cn | css.tv.itc.cn | js.tv.itc.cn | i3.itc.cn | a1.itc.cn
- 性质: itc.cn 系为搜狐静态/图片 CDN
- 来源: [搜狐视频首页 HTML 实测](https://tv.sohu.com/)（引用 css.tv.itc.cn×113、js.tv.itc.cn、i3.itc.cn、a1.itc.cn）
- 后续更新入口: 无
- 快测: tv.sohu.com 200 / my.tv.sohu.com 301（存在）
- 大陆可达性: 直连（境内公司）
- 备注: 页面为 GBK 编码

#### PP视频（原PPTV聚力）
- 类别: 国内正版（动漫频道）
- 域名: pptv.com | www.pptv.com | cartoon.aplus.pptv.com
- 性质: cartoon.aplus.pptv.com 为 PP视频动漫频道子域（实测标题「动漫频道_动画电影_动画片大全 - PP视频」）
- 来源: [PP视频动漫频道实测](https://cartoon.aplus.pptv.com/)；[pptv.com](http://www.pptv.com/) http 301 实测；[ACG导航收录](https://nav.acgsq.com/)
- 后续更新入口: 无
- 快测: cartoon.aplus.pptv.com 200 / pptv.com（https 经代理超时 000，http 301；搜索显示App仍在更新、域名续费至2028）
- 大陆可达性: 直连（境内公司；上海聚力传媒）——本机经代理 https 超时，可能限制境外 IP
- 备注: 平台热度低，但仍运营

#### 弹弹play（dandanplay）
- 类别: 工具（本地播放器+弹幕库）
- 域名: dandanplay.net | www.dandanplay.net | api.dandanplay.net
- 性质: 追番弹幕工具官网+开放 API
- 来源: [官网实测](https://dandanplay.net/)（标题「弹弹play - 为本地视频加上弹幕的全功能播放器」）；api.dandanplay.net 401 实测（接口存在，需鉴权）
- 后续更新入口: 官网下载页/API 文档（dandanplay.net）
- 快测: dandanplay.net 200 / api.dandanplay.net 401
- 大陆可达性: 直连（面向国内用户的产品；ip-api 显示服务器在加拿大 AWS，实测可达）
- 备注: 弹幕库另有配套域名（如弹弹play API 子域），未展开

#### Bangumi 番组计划
- 类别: 工具（番剧目录/评分/追番）
- 域名: bangumi.tv | bgm.tv | api.bgm.tv
- 性质: 番剧数据库与社区；bgm.tv 为其短域；api.bgm.tv 开放 API
- 来源: [bangumi.tv 实测](https://bangumi.tv/)（标题「Bangumi 番组计划」）；[bgm.tv 实测](https://bgm.tv/)；api.bgm.tv 200 实测
- 后续更新入口: 无
- 快测: bangumi.tv 200 / bgm.tv 200 / api.bgm.tv 200
- 大陆可达性: 直连（常见认知：多年可直连；ip-api 显示服务器在英国 Linode、未备案，偶发波动）
- 备注: 域名清单常见项

#### Animeko
- 类别: 工具（开源追番/弹幕播放器）
- 域名: myani.org
- 性质: 开源播放器官网（实测标题「Animeko」）
- 来源: [myani.org 实测](https://myani.org/)；[ACG导航收录](https://nav.acgsq.com/)（条目「Animeko」）
- 后续更新入口: 官网/GitHub 仓库
- 快测: myani.org 200
- 大陆可达性: 存疑（小站，境外托管，未逐一验证大陆直连）
- 备注: 与弹弹play同类的开源工具

---

#### 樱花动漫（高变动 · 原始站点已被刑事打击）
- 类别: 国内聚合（盗版）
- 域名: yhdmtv.cc | www.yhdmtv.cc | fcdmtv.cc | cn-yinghuadm.com.cn | cn-yinghuadman.com.cn | yinghuafanju.com.cn | mobile.meinadi.cn | img.lzipic.com | img.picbf.com | p.bfvp26.com
- 性质: 原站（yhdm/imomoe.ai）2024-12 一审、2025-07-04 二审维持原判（运营者获刑 2 年 3 个月）；现为第三方克隆群。yhdmtv.cc 页脚互链同网络域名（见备注）
- 来源: [yhdmtv.cc 首页实测](https://www.yhdmtv.cc/)（标题「樱花动漫－专注动漫的门户网站」；页脚互链 xkytv.cc/hjtv5.cc/mjtt2.cc/hjwtv.cc/ccytv.cc/cbhtv.top/zbkatv.cc 等；图床 img.lzipic.com、img.picbf.com）；[搜狐报道 2025-07-30（imomoe.ai 成都案）](https://www.sohu.com/a/919233868_195499)；必应搜索结果（各克隆域标题实测）
- 后续更新入口: 无官方发布页（克隆站无权威公告，靠搜索/导航站；建议正则匹配 yhdm/yinghua 关键词）
- 快测: yhdmtv.cc 200 / fcdmtv.cc 200（标题实为「风车动漫」，同网络） / cn-yinghuadm.com.cn 200 / cn-yinghuadman.com.cn 200 / yinghuafanju.com.cn 403 / img.lzipic.com 200 / img.picbf.com 200 / p.bfvp26.com 超时 / yinghuacd.com DNS 解析失败 / yhdm.so 200（域名挂牌出售页） / yhpdm.net 200（停放页，跳 parklogic.com）
- 大陆可达性: 存疑（yhdmtv.cc IP 在香港 [Cogent/SonderCloud]，面向大陆用户；盗版站域名易被墙、随时更换）
- 备注: 同网络域名群横跨多品牌（樱花/风车/星空影院/韩剧tv），封一个换一个；各克隆域系不同 SEO 团伙，勿当"官方"

#### 风车动漫
- 类别: 国内聚合（盗版）
- 域名: dm530.org | www.dm530.org | fcdmtv.cc | apps.fengctv.com.cn
- 性质: dm530.org 实测标题即「风车动漫」；fcdmtv.cc 为同网络（yhdmtv.cc 系）风车入口；apps.fengctv.com.cn 疑为 App 分域
- 来源: [dm530.org 实测](http://dm530.org/)（标题「风车动漫」）；[fcdmtv.cc 实测](https://fcdmtv.cc/)（标题「风车动漫－专注动漫的门户网站 | 风车动漫官网」）；必应搜索（apps.fengctv.com.cn 标题「风车动漫 - 专注动漫的门户网站」；旧域 dm530.in/dm530w6.com/fcdm22.com 已过期/证书过期）
- 后续更新入口: 无（无发布页）
- 快测: dm530.org 200 / fcdmtv.cc 200 / apps.fengctv.com.cn 400（存在，拒绝裸请求）
- 大陆可达性: 存疑（dm530.org 走 Cloudflare [ip-api: Cloudflare AS13335]，墙外 IP 常见盾）
- 备注: 与樱花克隆网络有交叉（fcdmtv.cc 同页脚域名群）

#### AGE动漫（agefans）
- 类别: 国内聚合（盗版 · 有官方发布页）
- 域名: agedm.io | www.agedm.io | age.tv | agedm.com | agedm.org | agefans.com | ageapp.app
- 性质: 官方 GitHub 发布页维护的域名体系；agedm.io 为「最新域名」，age.tv/agedm.com/agefans.com/agedm.org 为「易记域名」，ageapp.app 为 App 下载页
- 来源: [官方发布页 agefanscom/website](https://github.com/agefanscom/website)（README 最后编辑 2025.09.12：最新域名 agedm.io；易记域名 age.tv、agedm.com、agefans.com、www.agefans.com[已被重置]；弃用 agedm.vip/agedm.live/agedm.me/agefans.la「已阵亡」）；实测
- 后续更新入口: GitHub 发布页 + 备用发布页 rentry.la/agefans + 百度贴吧 age动漫吧
- 快测: agedm.io 403（Cloudflare 盾，站点存活） / ageapp.app 200 / age.tv、agedm.com、agedm.org、agefans.com 经代理超时 000（盾或区域性拦截，不能判死）
- 大陆可达性: 存疑（ip-api: agedm.io 美国 CNSERVERS + Cloudflare；靠多个易记域漂移，大陆时通时断）
- 备注: 该站体系完整（发布页+App），是聚合站里最好跟踪的一类

#### 稀饭动漫 / 稀饭ACG
- 类别: 国内聚合（盗版）
- 域名: xifan.moe | dm.xifanacg.com | next.xifanacg.com | xifanacg.com | app.xifandm.net | img2.xfmanga.top
- 性质: dm.xifanacg.com 为在线动漫站（「稀饭动漫 Next」）；xifan.moe 为社区/入口页（「稀饭ACG」）；img2.xfmanga.top 为图床 CDN
- 来源: [dm.xifanacg.com 首页实测](https://dm.xifanacg.com/)（标题「稀饭动漫 Next」；引用 img2.xfmanga.top×169、next.xifanacg.com）；[xifan.moe 实测](https://xifan.moe/)（标题「稀饭ACG - 连接动漫、漫画、游戏与二次元世界」）；[app.xifandm.net 实测](https://app.xifandm.net/)（标题「下载 App · 稀饭动漫 Next」）
- 后续更新入口: App 下载页 app.xifandm.net（随站更新）
- 快测: dm.xifanacg.com 200 / xifan.moe 200 / app.xifandm.net 200
- 大陆可达性: 存疑（ip-api: xifan.moe 日本 Tencent Cloud；站点为大陆用户向盗版站，时通时断）
- 备注: 搜索另见 dick.xfani.com 等备用域（未逐一验证）

#### 次元城动漫
- 类别: 国内聚合（盗版 · 有发布页）
- 域名: cycity.pro | www.cycity.pro | cycani.org | cycdm01.top | cycanime.com
- 性质: cycity.pro 为官方「发布页」（页内标注官网 WWW.CYCITY.PRO 及备用 cycani.org）；cycani.org 实测「不提供服务」
- 来源: [cycity.pro 发布页实测](https://www.cycity.pro/)（标题「次元城动画 发布页」，页内互相引用 www.cycani.org / www.cycity.pro）；[知乎教程/公告](https://zhuanlan.zhihu.com/p/11349191286)；搜索整理的旧域（cyc-anime.net 已过期、cycdm01.top「不提供服务」）
- 后续更新入口: cycity.pro 发布页（换域名/新版在此更新）
- 快测: cycity.pro 200 / www.cycity.pro 200 / cycani.org 200（返回「不提供服务」页） / cycdm01.top 200（「不提供服务」） / cycanime.com 无标题响应
- 大陆可达性: 存疑（发布页在线；标注的主站当前拒绝服务，处于轮换/维护状态）
- 备注: 属于「发布页制」聚合站，规则难以锁死

#### girigiri 爱动漫
- 类别: 国内聚合（盗版 · 弹幕追番）
- 域名: girigirilove.com | www.girigirilove.com | anime.girigirilove.com | girigiri.cn
- 性质: 主站为弹幕动漫站；anime. 子域为内容入口；girigiri.cn 为 2026-08 新注册的相关域（标题「Girigiri动漫 - 全球新番漫画同步追更神器」，运营方存疑）
- 来源: [www.girigirilove.com 实测](https://www.girigirilove.com/)（标题「GiriGiriLove 爱站 - 免费高清动漫在线观看｜追番弹幕动漫网站」）；[girigiri.cn 实测](https://girigiri.cn/)（标题「Girigiri动漫 - 全球新番漫画同步追更神器」）
- 后续更新入口: 无固定发布页
- 快测: girigirilove.com 200 / www.girigirilove.com 200 / anime.girigirilove.com 空响应（200 链路异常，疑 JS/区域限制） / girigiri.cn 200
- 大陆可达性: 存疑（ip-api: girigirilove.com Cloudflare；社区有「需挂梯子更流畅」的反馈）
- 备注: 无

#### 嘀哩嘀哩（D站）
- 类别: 国内聚合（盗版 · 老牌）
- 域名: dilidili51.com | www.dilidili51.com | 5dm.dev | dlidli.app | www.dlidli.app
- 性质: dilidili51.com 实测标题「嘀哩嘀哩,这里是兴趣使然的无名小站(D站)」；ACG导航另收录 5dm.dev（标注「D站」，本机 Cloudflare 盾）；dlidli.app 为「打驴动漫官网发布页」
- 来源: [dilidili51.com 实测](https://dilidili51.com/)；[ACG导航 nav.acgsq.com 收录](https://nav.acgsq.com/)（5dm.dev、dlidli.app 等条目）；[dlidli.app 实测](https://www.dlidli.app/)（标题「打驴动漫官网发布页」）
- 后续更新入口: dlidli.app 发布页（打驴动漫品牌）
- 快测: dilidili51.com 200 / 5dm.dev 200（Just a moment... CF 盾） / dlidli.app 200
- 大陆可达性: 存疑（ip-api: dilidili51.com 美国 NetLab Global；老牌站多次被打击后重建）
- 备注: D站历史上多次换域+被查，域名寿命短

#### ACG饭团（饭团动漫）
- 类别: 国内聚合（盗版）
- 域名: fantuantv.com | www.fantuantv.com
- 性质: 动漫站（实测标题「饭团动漫 - ACG饭团」）
- 来源: [ACG导航收录](https://nav.acgsq.com/)（条目「ACG饭团」）；[fantuantv.com 实测](https://fantuantv.com/)
- 后续更新入口: 无
- 快测: fantuantv.com 200
- 大陆可达性: 存疑（小站，未验证大陆直连）
- 备注: 无

#### OmoFun动漫
- 类别: 国内聚合（盗版）
- 域名: omofuns.com | www.omofuns.com
- 性质: 动漫分享门户（实测标题「OmoFun动漫-一个免费的动漫分享门户」）
- 来源: [ACG导航收录](https://nav.acgsq.com/)；[www.omofuns.com 实测](https://www.omofuns.com/)
- 后续更新入口: 无
- 快测: www.omofuns.com 200
- 大陆可达性: 存疑（ip-api: 美国 Cnservers）
- 备注: 无

#### 咕咕番
- 类别: 国内聚合（盗版）
- 域名: gugu3.com | www.gugu3.com
- 性质: 在线日漫站（实测标题「咕咕番 - 在线日漫」）
- 来源: [ACG导航收录](https://nav.acgsq.com/)；[www.gugu3.com 实测](https://www.gugu3.com/)
- 后续更新入口: 无
- 快测: www.gugu3.com 200
- 大陆可达性: 存疑（ip-api: Cloudflare）
- 备注: 无

#### TvTFun
- 类别: 国内聚合（盗版）
- 域名: tvtfun.net | www.tvtfun.net
- 性质: 番剧站（实测标题「TvTFun - 番剧自由，从这里开始」）
- 来源: [ACG导航详情页收录](https://nav.acgsq.com/sites/605.html)；[www.tvtfun.net 实测](https://www.tvtfun.net/)
- 后续更新入口: 无
- 快测: www.tvtfun.net 200
- 大陆可达性: 存疑
- 备注: 无

#### XDM动漫
- 类别: 国内聚合（盗版）
- 域名: xuandm.com | www.xuandm.com
- 性质: 动漫+影视在线站（实测标题「XDM动漫 - 海量动漫、电影、电视剧在线观看」）
- 来源: [ACG导航详情页收录](https://nav.acgsq.com/sites/141.html)；[www.xuandm.com 实测](https://www.xuandm.com/)
- 后续更新入口: 无
- 快测: www.xuandm.com 200
- 大陆可达性: 存疑
- 备注: 无

#### 动漫岛 / 天天动漫 / 趣动漫 / AniFun / 番组百科（2025-26 新兴小站群）
- 类别: 国内聚合（多为盗版/新站）
- 域名: dmmandao.com.cn | ttiandman.com.cn | qudman.com.cn | anifun.cn | anibk.com
- 性质: 各站实测标题依次为「动漫岛 - 专注动漫的门户网站」「天天动漫 · 动漫爱好者聚集地」「趣动漫_沉浸追番_二次元社区」「AniFun 一起发现动漫与ACG的乐趣」「番组百科 AniBK」
- 来源: [必应检索实测](https://cn.bing.com/search?q=%E5%8A%A8%E6%BC%AB%E5%B2%9B)（标题逐一实测）；各站根域 curl 实测
- 后续更新入口: 无
- 快测: dmmandao.com.cn 200 / ttiandman.com.cn 200 / qudman.com.cn 200 / anifun.cn 200 / anibk.com 200
- 大陆可达性: 存疑（.com.cn 新域，IP 归属混杂 [如 dmmandao.com.cn 南非 IP]，未验证大陆直连）
- 备注: 2025 年以来出现一批 .com.cn 后缀动漫克隆站，疑似 SEO 批量建站，寿命短

#### 动漫屋（漫画站）
- 类别: 国内聚合（以漫画为主，非番剧视频）
- 域名: dm5.com | www.dm5.com | cdndm5.com | mhfm5tel.cdndm5.com | css99tel.cdndm5.com
- 性质: 老牌在线漫画站（实测标题「动漫屋_在线漫画_为看漫画的人而生」）；cdndm5.com 为图片 CDN
- 来源: [www.dm5.com 首页 HTML 实测](https://www.dm5.com/)（引用 mhfm5tel.cdndm5.com、css99tel.cdndm5.com 等）
- 后续更新入口: 无
- 快测: dm5.com 200 / www.dm5.com 200
- 大陆可达性: 直连（常见认知：长期可访问；ip-api 显示 IP 在美国 GorillaServers，未备案）
- 备注: 任务点名项；实际是漫画站，番剧视频不在此

#### 妮可动漫
- 类别: 国内聚合（状态未确认）
- 域名: nikedm.com | nkdm.hkdrj.cn（均未能实测确认）
- 性质: 搜索资料显示品牌「妮可动漫」，但候选域 nikedm.com、nkdm.hkdrj.cn 经代理实测均不可达（000）
- 来源: 必应/搜索引擎整理（未见官方发布页）；本机 000 实测
- 后续更新入口: 无
- 快测: nikedm.com 000 / nkdm.hkdrj.cn 000
- 大陆可达性: 存疑（无法确认存活，勿入正式规则）
- 备注: 如后续确认新域再补；本次未找到可信的当前域名

#### 看看动漫
- 类别: 国内聚合（疑似已失效）
- 域名: kkdm3.com
- 性质: 候选域 kkdm3.com 实测为英文广告停放页（含 CMP 广告框架，无动漫内容、无标题），疑似域名过期后被停放
- 来源: [kkdm3.com 实测](https://kkdm3.com/)（内容为广告域停放模板）；搜索显示域名 2024-09 已过期
- 后续更新入口: 无
- 快测: kkdm3.com 200（停放页，非站点）
- 大陆可达性: 不适用（已非动漫站）
- 备注: App「看看动漫」（漫剧）与网站非同一主体

---

#### 已确认失效 / 已停运（含证据）

#### 动漫之家（dmzj.com）
- 类别: 国内聚合（漫画社区，原最大之一）
- 域名: dmzj.com
- 性质: 2025-09-10 正式停止运营（官网/APP 全面不可访问）；本机 2026-10-06 实测 dmzj.com DNS 失败（000）
- 来源: [知乎《20年的动漫之家，结束了！》](https://zhuanlan.zhihu.com/p/1949644948107420932)（称「2025年9月，正式停运」）；[知乎讨论「动漫之家」于 9 月 10 日正式停止运营](https://www.zhihu.com/question/1949429874117808409)；[百度贴吧讨论](https://tieba.baidu.com/p/9999558486)
- 后续更新入口: 无
- 快测: dmzj.com 000（DNS 解析失败）
- 备注: 动漫漫画 APP/域名均勿再入规则

#### ZzzFun
- 类别: 国内聚合（盗版，刑事办结）
- 域名: zzzfun.one | zzzfun.org | zzzfun.com
- 性质: 运营者 2025-02-11 被石家庄公安逮捕，2025-11-18 判刑（有期徒刑 1 年、罚金 3.5 万元，已生效）；zzzfun.org 于 2025-02 域名过期
- 来源: [CODA 官方新闻稿（日）](https://coda-cj.jp/news/2651/)；[CODA 官方新闻稿（英）](https://coda-cj.jp/en/news/853/)
- 后续更新入口: 无
- 快测: 未测（已刑事关站，导航站标注「已关闭」）
- 备注: 该类站偶有山寨复活域，勿信

#### 樱花动漫原站相关域（补充）
- 域名: yinghuacd.com | imomoe.ai | yhdm.so | yhpdm.net | yhdm.la
- 性质: yinghuacd.com DNS 失败；imomoe.ai 为刑事案涉案站（已关）；yhdm.so 域名挂牌出售页；yhpdm.net 停放页（跳 router.parklogic.com）；yhdm.la 不可达
- 来源: [搜狐报道 2025-07-30（成都案、imomoe.ai）](https://www.sohu.com/a/919233868_195499)；本机逐域实测（见上文「樱花动漫」节）
- 快测: yinghuacd.com DNS 失败 / yhdm.so 200（出售页） / yhpdm.net 200（停放） / yhdm.la 000
- 备注: 切勿把克隆域当"官方"

#### AGE动漫弃用域 / 风车已过期域 / 次元城旧域（汇总）
- 域名: agedm.vip | agedm.live | agedm.me | agefans.la | dm530.in | dm530w6.com | fcdm22.com | cyc-anime.net
- 性质: 官网发布页标注「已阵亡」（AGE 系）；搜索资料显示已过期/证书过期（风车系）；cyc-anime.net 2025-09-30 过期
- 来源: [AGE 官方发布页](https://github.com/agefanscom/website)；必应/站长工具类查询（dm530.in 过期、dm530w6.com 过期、fcdm22.com 证书过期）
- 快测: 未逐一（已属弃用）
- 备注: 规则中如出现这些域应删除

---

### 本轮实测方法备忘
- 快测命令: `curl -s -o /dev/null -w '%{http_code}' --connect-timeout 6 -m 10 -A 'Mozilla/5.0' https://域名/`（本机流量经路由器代理，非大陆直连）
- IP 归属: `http://ip-api.com/json/域名?fields=country,isp`（2026-10-06）
- 未在本文覆盖: B站国际版 bilibili.tv、爱奇艺国际版 iq.com（另一路调研负责）；B站漫画 manga.bilibili.com（已有清单）

## 2. 日本系 / 海外正版平台

调研日期: 2026-10-06 | 范围: 华语区正版（巴哈動畫瘋/Muse/Ani-One/Viu/myTV/LiTV）、国际正版（Crunchyroll/HIDIVE/Hulu/RetroCrush/MidnightPulp）、大陆平台国际版（bilibili.tv/iQ.com/WeTV/优酷国际版）、日本本土（ABEMA/dアニメ/ニコニコ/U-NEXT/DMM TV/FOD/Lemino/TELASA/バンダイチャンネル/アニメタイムズ/Hulu JP）、已失效与合并站

说明:
- 本机流量经路由器代理（快测时出口为日本/台湾），curl 快测只反映"经代理可达性"，**超时/000 ≠ 站点死亡**。
- 「大陆可达性」依据三类证据：① [GreatFire 实时测试](https://en.greatfire.org/)（逐域查证，附测试日期）② [Loyalsoldier/clash-rules gfw.txt 社区 GFW 名单](https://github.com/Loyalsoldier/clash-rules/blob/release/gfw.txt) ③ 针对性公开报告/开源代码。两方证据冲突时标"存疑"并注明各自出处。
- 标注口径: 直连=可直连（未被 GFW 名单收录且无封锁测试记录）；需代理=有封锁证据；存疑=证据不足或互相矛盾（附倾向）。
- 海外聚合站（hianime/gogoanime 系）由另一路负责；bilibili.com/iqiyi.com/v.qq.com/youku.com 等大陆主站见 cn.md。

---

#### 巴哈姆特動畫瘋（ani.gamer.com.tw）
- 类别: 华语区正版（台湾）
- 域名: ani.gamer.com.tw | gamer.com.tw | www.gamer.com.tw | forum.gamer.com.tw | gnn.gamer.com.tw | home.gamer.com.tw | user.gamer.com.tw | wall.gamer.com.tw | buy.gamer.com.tw | search.gamer.com.tw | ref.gamer.com.tw | ani.baha.tw | bahamut.com.tw | i2.bahamut.com.tw | p2.bahamut.com.tw | truth.bahamut.com.tw | avatar2.bahamut.com.tw | bahamut.akamaized.net | gamer-cds.cdn.hinet.net | gamer2-cds.cdn.hinet.net
- 性质: 台湾最大动画配信平台；i2/p2/truth.bahamut.com.tw 为图片 CDN；ani.baha.tw 为短链（302→ani.gamer.com.tw）；bahamut.akamaized.net 为 Akamai 视频 CDN；gamer-cds/gamer2-cds.cdn.hinet.net 为中华电信 HiNet 视频 CDN
- 来源: [ani.gamer.com.tw 首页 HTML 实测](https://ani.gamer.com.tw/)（2026-10-06，引用 i2/p2/truth.bahamut.com.tw、ani.baha.tw 等，另见 [www.gamer.com.tw 实测](https://www.gamer.com.tw/)）；[ACL4SSR Bahamut.list](https://github.com/ACL4SSR/ACL4SSR/blob/master/Clash/Ruleset/Bahamut.list)；[v2fly/domain-list-community PR #781 "Add bahamut.akamaized.net to fix bahamut region limited"](https://github.com/v2fly/domain-list-community/pull/781)
- 后续更新入口: 无（官方无规则公告页，跟随站内引用/CDN 变化）
- 快测: ani.gamer.com.tw 200 / www.gamer.com.tw 200 / ani.baha.tw 302→ani.gamer.com.tw
- 大陆可达性: 需代理（依据: GreatFire [gamer.com.tw 100% blocked @2026-09-28](https://en.greatfire.org/gamer.com.tw)、[ani.gamer.com.tw blocked @2026-05-04](https://en.greatfire.org/ani.gamer.com.tw)、forum.gamer.com.tw blocked @2026-02-22；gfw.txt 收录 gamer.com.tw/bahamut.com.tw/hinet.net；且仅台湾 IP 可看片）
- 备注: 仅限台湾/（部分）港澳地区 IP 观看，免费用户需看广告；视频 CDN（akamaized/hinet 系）必须一并覆盖，否则会出现区域限制报错

#### Muse 木棉花（Muse Communication）
- 类别: 华语区正版（台湾动画代理发行商，非流媒体）
- 域名: e-muse.com | www.e-muse.com | e.e-muse.com | mall.e-muse.com.tw | e-muse.com.tw（旧官网，已失效）
- 性质: 台湾最大动画代理商官网（国际版域）+ 周边商城；e.e-muse.com 为短链/活动域（Cloudflare 防护）；e-muse.com.tw 旧官网 2026-10 已无解析
- 来源: 動畫瘋首页 Muse 推广位实测（https://e.e-muse.com/03I）；[木棉花樂園商城实测](https://mall.e-muse.com.tw/)（title「Muse木棉花樂園」）；[Wayback 快照 www.e-muse.com 2025-11-04](https://web.archive.org/web/20251104192640/https://www.e-muse.com/)
- 后续更新入口: https://mall.e-muse.com.tw/
- 快测: www.e-muse.com 403（Cloudflare 反爬，站点存在）/ e.e-muse.com/03I 403 / mall.e-muse.com.tw 200 / www.e-muse.com.tw DNS NXDOMAIN、e-muse.com.tw 无 A 记录
- 大陆可达性: 存疑（依据: GFW 名单未收录、GreatFire 未测；403 为 Cloudflare 反爬而非封锁）→ 倾向直连
- 备注: 授权播出在 YouTube（MuseTW 等频道）+ 各流媒体平台，无自有流媒体；YouTube 为共用域不收

#### Ani-One（羚邦集团 Medialink）
- 类别: 华语区正版（香港动画代理/官方频道品牌）
- 域名: medialink.com.hk | www.medialink.com.hk（Ani-One 品牌页 /en/Anione.aspx）
- 性质: 羚邦 Medialink 旗下动画品牌（YouTube 频道为主要发行渠道）；无独立域名站点（ani-one.net/anione.net 域名无法连接，疑似不存在）
- 来源: [Medialink Ani-One 品牌页实测](https://www.medialink.com.hk/en/Anione.aspx)（200，页面引用 ani-one-logo.jpg 等品牌素材）
- 后续更新入口: 无（仅集团官网/YouTube 频道）
- 快测: medialink.com.hk 200
- 大陆可达性: 存疑（依据: GFW 名单未收录、GreatFire 未测）→ 倾向直连（品牌页无视频内容）
- 备注: 若规则只为动画内容分类，收录 medialink.com.hk 即可；Ani-One Asia 等 YouTube 频道属 youtube.com 共用域

#### Viu / ViuTV（PCCW 电讯盈科）
- 类别: 华语区正版（香港/东南亚 OTT + 香港 ViuTV 频道）
- 域名: viu.com | www.viu.com | api-gateway-global.viu.com | viuapi.io | um.viuapi.io | viu.tv | www.viu.tv | d2anahhhmp1ffz.cloudfront.net
- 性质: viu.com 为区域 OTT（港澳/东南亚）；viu.tv 为 ViuTV（香港免费电视频道+应用）；viuapi.io 为播放/DRM API 域；d2anahhhmp1ffz.cloudfront.net 为其 CloudFront 分布（缩略图/资源）
- 来源: [yt-dlp viu.py](https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/extractor/viu.py)（api-gateway-global.viu.com、um.viuapi.io、cloudfront 主机）；[viu.tv 首页实测](https://viu.tv/)（title「ViuTV」）；[www.viu.com 实测](https://www.viu.com/)（出口日本→/ott/no-service/）
- 后续更新入口: 无
- 快测: www.viu.com 200（no-service 页）/ viu.tv 200
- 大陆可达性: 需代理/存疑混合（依据: GreatFire [viu.tv 100% disrupted @2026-10-04](https://en.greatfire.org/viu.tv)；[viu.com not blocked @2026-09-25](https://en.greatfire.org/viu.com)、[www.viu.com 可达 @2026-03-06](https://en.greatfire.org/www.viu.com)；但 gfw.txt 收录 viu.com+viu.tv）→ 按需代理更稳
- 备注: 内容库按地区授权（HK/SG/MY/ID 等），香港区动画/日剧最全

#### myTV SUPER（TVB）
- 类别: 华语区正版（香港 TVB OTT）
- 域名: mytvsuper.com | www.mytvsuper.com | assets.mytvsuper.com | promo.mytvsuper.com | lf3-data.volccdn.com（图片 CDN）| tvbanywhere.com（TVB 海外版）
- 性质: TVB 旗下 OTT；assets/promo 为静态/CDN 子域；lf3-data.volccdn.com 为火山引擎 CDN（站点图片）；tvbanywhere.com 为 TVB 海外版服务
- 来源: [www.mytvsuper.com/tc/home/ 首页 HTML 实测](https://www.mytvsuper.com/tc/home/)（引用 assets/promo.mytvsuper.com、lf3-data.volccdn.com、tvbanywhere.com）
- 后续更新入口: 无
- 快测: www.mytvsuper.com 200（跳转 /tc/home/）
- 大陆可达性: 存疑（依据: GreatFire [not blocked @2026-07-18](https://en.greatfire.org/www.mytvsuper.com)；但 gfw.txt 收录 +.mytvsuper.com）→ 建议按需代理
- 备注: 香港内容锁区；动画以 TVB 粤语配音番组为主

#### LiTV 立视（台湾）
- 类别: 华语区正版（台湾 OTT，含动漫馆）
- 域名: litv.tv | www.litv.tv | fino.svc.litv.tv（API）| p-cdnstatic.svc.litv.tv | 2fp-cdnstatic.svc.litv.tv | litvfreemobile-hichannel.cdn.hinet.net（HiNet 视频 CDN）
- 性质: 台湾 OTT；*.svc.litv.tv 为服务子域（API/静态 CDN）；视频走中华电信 HiNet CDN（hinet 子域来自第三方规则清单，未独立实测）
- 来源: [www.litv.tv 首页 HTML 实测](https://www.litv.tv/)（引用 fino/p-cdnstatic.svc.litv.tv）；规则清单来源见 gfw.txt 同源的 ACL4SSR 系清单与搜索汇总（litvfreemobile-hichannel.cdn.hinet.net）
- 后续更新入口: 无
- 快测: www.litv.tv 200
- 大陆可达性: 直连（依据: GreatFire [not blocked @2026-09-05](https://en.greatfire.org/litv.tv)；GFW 名单未收录）
- 备注: 部分内容需台湾 IP；动漫馆有木棉花等授权番

#### Crunchyroll
- 类别: 国际正版（全球最大动漫流媒体，Sony 旗下）
- 域名: crunchyroll.com | www.crunchyroll.com | beta.crunchyroll.com | static.crunchyroll.com | imgsrv.crunchyroll.com | sso.crunchyroll.com | help.crunchyroll.com | crunchyrollsvc.com | cr-play-service.prd.crunchyrollsvc.com | crunchyrollexpo.com
- 性质: imgsrv.crunchyroll.com 图片 CDN；static 静态资源；crunchyrollsvc.com 为其后端服务域（播放 API cr-play-service，manifest 由 …/v1/manifest/ 下发）；视频流主机由播放接口动态下发（历史代码证据为 *.vrv.co，2026-10 实测 v.vrv.co 已无 DNS 解析，勿硬编码）
- 来源: [www.crunchyroll.com 首页 HTML 实测](https://www.crunchyroll.com/)（引用 imgsrv/static/sso/cr-play-service.prd.crunchyrollsvc.com）；[multi-downloader-nx #732](https://github.com/anidl/multi-downloader-nx/issues/732)（manifest 与 https://fy.v.vrv.co/evs3/ 流地址）
- 后续更新入口: https://help.crunchyroll.com/
- 快测: www.crunchyroll.com 200（出口日本→currently-unavailable-in-your-location 页）
- 大陆可达性: 存疑偏需代理（依据: GreatFire 最后测试 2026-06-23 "reachable"；但 gfw.txt 收录 +.crunchyroll.com，且多方报告被墙 + 大陆不在其服务区）→ 建议代理
- 备注: 日本区不可用（实测跳转）；Funimation/Wakanim/VRV 均已于 2022-03 宣布并入；避免漏 crunchyrollsvc.com 系

#### HIDIVE
- 类别: 国际正版（AMC/Sentai 系）
- 域名: hidive.com | www.hidive.com | dce-frontoffice.imggaming.com | static.diceplatform.com | content-images.onvesper.com | vod-images.onvesper.com
- 性质: 应用壳 preconnect 显示后端平台为 IMGGaming（imggaming.com）+ DICE（diceplatform.com），图片 CDN 为 onvesper.com（content/vod 双子域）
- 来源: [www.hidive.com 首页 HTML 实测](https://www.hidive.com/)（<link rel=preconnect/dns-prefetch> 三域 + og:image 于 static.diceplatform.com）
- 后续更新入口: 无
- 快测: www.hidive.com 200（5KB 应用壳 HTML）
- 大陆可达性: 存疑偏直连（依据: GreatFire [not blocked @2026-09-26](https://en.greatfire.org/hidive.com)；GFW 名单未收录）
- 备注: 服务区含美/加/英/爱/澳/新等非亚洲市场（据 2026 年官方 simulcast 公告）；亚洲不可用

#### Hulu（美国）
- 类别: 国际正版（动漫区，Disney 体系）
- 域名: hulu.com | www.hulu.com | auth.hulu.com | edge-api.hulu.com | home.hulu.com | signup.hulu.com | secure.hulu.com | img1.hulu.com | img2.hulu.com | img4.hulu.com | huluim.com
- 性质: img1-4.hulu.com 与 huluim.com 为图片 CDN；auth/edge-api 为接口；首页与 Disney+/Max 互链（Disney 体系）
- 来源: [www.hulu.com 首页 HTML 实测](https://www.hulu.com/)（huluim 出现 7 次、img1/2/4.hulu.com、auth/edge-api 等）；gfw.txt 收录 hulu.com、huluim.com
- 后续更新入口: https://help.hulu.com/
- 快测: www.hulu.com 200
- 大陆可达性: 存疑偏需代理（依据: GreatFire [not blocked @2026-08-28](https://en.greatfire.org/hulu.com)；但 gfw.txt 收录 hulu.com/huluim.com，且服务仅美国 IP）→ 建议代理
- 备注: 仅美国可用；大量 simulcast 动画；与 Hulu Japan（hulu.jp）是两家不同公司/域

#### RetroCrush
- 类别: 国际正版（经典/复古动画）
- 域名: retrocrush.tv | www.retrocrush.tv | matchpoint.tv | cdn.matchpoint.tv | metax.api.matchpoint.tv | asiancrush.com（姊妹站）
- 性质: 经典动画流媒体；播放与 CDN 由 Matchpoint 平台提供（matchpoint.tv 系）；AsianCrush 为同体系姊妹站（日韩影剧+动画）
- 来源: [www.retrocrush.tv 首页 HTML 实测](https://www.retrocrush.tv/)（引用 cdn.matchpoint.tv、metax.api.matchpoint.tv、asiancrush.com）
- 后续更新入口: 无
- 快测: retrocrush.tv 200
- 大陆可达性: 存疑（依据: GreatFire 未测、GFW 名单未收录）→ 倾向直连
- 备注: 免费看广告+订阅制；锁区（美区为主）

#### Midnight Pulp
- 类别: 国际正版（恐怖/邪典影剧，含少量动画）
- 域名: midnightpulp.com | www.midnightpulp.com | matchpoint.tv | cdn.matchpoint.tv | metax.api.matchpoint.tv
- 性质: 与 RetroCrush 同平台（Matchpoint）挂载的垂直站
- 来源: [www.midnightpulp.com 首页 HTML 实测](https://www.midnightpulp.com/)（引用 cdn.matchpoint.tv、metax.api.matchpoint.tv）
- 后续更新入口: 无
- 快测: www.midnightpulp.com 200
- 大陆可达性: 存疑（依据: GreatFire 未测、GFW 名单未收录）→ 倾向直连
- 备注: 动画占比小；订阅制

#### bilibili.tv（B站国际版）
- 类别: 大陆平台国际版
- 域名: bilibili.tv | www.bilibili.tv | api.bilibili.tv | passport.bilibili.tv | biliintl.com | www.biliintl.com | bstarstatic.com | p.bstarstatic.com | pic.bstarstatic.com | p1.bstarstatic.com | pic1.bstarstatic.com | s1.bstarstatic.com | p-bstarstatic.akamaized.net | upos-bstar-mirrorakam.akamaized.net | upos-bstar1-mirrorakam.akamaized.net
- 性质: B站国际版；biliintl.com 为别名域（实测 200）；bstarstatic.com 系为图片/静态 CDN（p/pic 前缀）；upos-bstar* akamaized.net 为视频镜像 CDN；api/passport 为接口与登录子域
- 来源: [yt-dlp bilibili.py](https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/extractor/bilibili.py)（api.bilibili.tv/intl/gateway、passport.bilibili.tv、pic.bstarstatic.com/.net、biliintl.com）；upos-bstar*/p-bstarstatic 实测 DNS 存在（Akamai A 记录）+ 第三方规则清单/urlscan 观测汇总
- 后续更新入口: 无
- 快测: www.bilibili.tv 200（对无浏览器指纹请求返回 0 字节空体，属反爬）/ api.bilibili.tv/intl/gateway 404（存在）/ pic.bstarstatic.com 403（存在）/ www.biliintl.com 200
- 大陆可达性: 需代理/受限（依据: GreatFire [100% disrupted @2026-09-30](https://en.greatfire.org/bilibili.tv)；用户报告运营商屏蔽 + Error 1003 地区码）→ 需代理
- 备注: 内容按东南亚/日韩/港澳台分区授权；i0/s1.hdslb.com 与大陆主站共用（归 cn.md）

#### iQIYI 国际版（iQ.com）
- 类别: 大陆平台国际版
- 域名: iq.com | www.iq.com | intl-api.iq.com | pcw-api.iq.com | cache-video.iq.com | intl-help.iq.com | qy.net | msg-intl.qy.net | iqiyipic.com | pic2.iqiyipic.com | pic3.iqiyipic.com | pic4.iqiyipic.com | pic7.iqiyipic.com | pic9.iqiyipic.com | u0.iqiyipic.com | u1.iqiyipic.com | u3.iqiyipic.com | u4.iqiyipic.com | u5.iqiyipic.com | u6.iqiyipic.com | u7.iqiyipic.com | u8.iqiyipic.com | u9.iqiyipic.com | stc.iqiyipic.com | static.iqiyi.com
- 性质: 国际版主站+接口（intl-api/pcw-api）；cache-video.iq.com 视频缓存 CDN；iqiyipic.com 系图片 CDN（与大陆版共用品牌域，u0-u9/pic* 编号子域）；msg-intl.qy.net 为消息服务
- 来源: [www.iq.com 首页 HTML 实测](https://www.iq.com/)（引用 intl-api/pcw-api/cache-video.iq.com、msg-intl.qy.net 及 pic*/u*.iqiyipic.com、static.iqiyi.com）
- 后续更新入口: https://intl-help.iq.com/
- 快测: www.iq.com 200
- 大陆可达性: 直连（依据: GreatFire [not blocked @2026-08-23](https://en.greatfire.org/iq.com)；GFW 名单未收录）
- 备注: 与大陆 iqiyi.com 分域；内容按地区授权（东南亚等）；u0-u9.iqiyipic.com 编号子域见 jp-domains.txt

#### WeTV（腾讯国际版）
- 类别: 大陆平台国际版
- 域名: wetv.vip | www.wetv.vip | wetvinfo.com | static.wetvinfo.com | btrace.wetvinfo.com | videohy.tc.qq.com | vliveachy.tc.qq.com
- 性质: wetvinfo.com 为 WeTV 自有信息/静态域；tc.qq.com 视频主机与大陆腾讯视频共用（tc.qq.com 系共用域，仅收录命中的播放主机）
- 来源: [wetv.vip 首页 HTML 实测](https://wetv.vip/)（引用 static/btrace.wetvinfo.com、videohy.tc.qq.com、vliveachy.tc.qq.com）
- 后续更新入口: 无
- 快测: wetv.vip 200
- 大陆可达性: 直连（依据: GreatFire [not blocked @2026-08-16](https://en.greatfire.org/wetv.vip)；GFW 名单未收录）
- 备注: 与 v.qq.com 内容分区；动画主要面向东南亚

#### 优酷国际版（YOUKU TV）
- 类别: 大陆平台国际版
- 域名: youku.tv | www.youku.tv | m.youku.tv | youku.com | v.youku.com | account.youku.com | so.youku.com
- 性质: 优酷海外版（youku.tv 独立域，实测 title「YOUKU-Drama, Film, Show, Anime」）；账号/接口回落 youku.com 系（与大陆主站共用）
- 来源: [youku.tv 首页 HTML 实测](https://youku.tv/)（title 及 account.youku.com、so.youku.com、v.youku.com 引用）
- 后续更新入口: 无
- 快测: youku.tv 200
- 大陆可达性: 直连（依据: GFW 名单未收录、GreatFire 未测；youku.tv 为海外自有域）→ 低风险
- 备注: 页面大量 alicdn 静态资源（阿里共用 CDN，不收）

#### ABEMA
- 类别: 日本本土
- 域名: abema.tv | www.abema.tv | api.abema.io | license.abema.io | vod-abematv.akamaized.net | linear-abematv.akamaized.net
- 性质: 日本最大免费动画/直播平台（CyberAgent×テレビ朝日）；api.abema.io 接口；license.abema.io 为 DRM；vod-/linear-abematv.akamaized.net 为视频 CDN
- 来源: [yt-dlp abematv.py](https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/extractor/abematv.py)；gfw.txt 收录 abematv/linear-abematv/vod-abematv.akamaized.net 三条
- 后续更新入口: 无
- 快测: abema.tv 200（返回「お住まいの地域からはご利用になれません」页 — 数据中心 IP 被其锁区）
- 大陆可达性: 主域存疑、CDN 需代理（依据: GreatFire [abema.tv not blocked @2026-07-21](https://en.greatfire.org/abema.tv)；但 gfw.txt 收录三个视频 CDN 子域）→ 实际看片需代理
- 备注: 仅日本 IP 可看（实测地域错误页）；免费+Premium 混合

#### dアニメストア（d Anime Store）
- 类别: 日本本土
- 域名: animestore.docomo.ne.jp | cs1.animestore.docomo.ne.jp | id.smt.docomo.ne.jp（d 账号登录，docomo 共用）
- 性质: NTT docomo 系动画流媒体（日本最大动画配信之一）；cs1 为内容服务子域
- 来源: [animestore.docomo.ne.jp/animestore/tp_pc 首页 HTML 实测](https://animestore.docomo.ne.jp/animestore/tp_pc)（引用 cs1.animestore.docomo.ne.jp、id.smt.docomo.ne.jp）
- 后续更新入口: 无
- 快测: 200
- 大陆可达性: 存疑（依据: GreatFire 未测、GFW 名单未收录；docomo 系未见封锁）→ 倾向直连（内容仍需日本 IP）
- 备注: 仅日本区；另有「dアニメストア for Prime Video」支店（走 Amazon，共用域不收）

#### ニコニコ動画（niconico）
- 类别: 日本本土（UGC+官方动画）
- 域名: nicovideo.jp | www.nicovideo.jp | nvapi.nicovideo.jp | account.nicovideo.jp | video.nicovideo.jp | live.nicovideo.jp | anime.nicovideo.jp | seiga.nicovideo.jp | dic.nicovideo.jp | ch.nicovideo.jp | embed.nicovideo.jp | premium.nicovideo.jp | search.nicovideo.jp | news.nicovideo.jp | sp.nicovideo.jp | site.nicovideo.jp | nimg.jp | img.cdn.nimg.jp | cdn.nimg.jp | res.nimg.jp | video.nimg.jp | wktk.nimg.jp | nicoprofile.nimg.jp
- 性质: 弹幕视频站；nimg.jp 系为静态/图片/缩略图 CDN；nvapi 为接口；完整子域清单（40+）见 jp-domains.txt 同节
- 来源: [www.nicovideo.jp 首页 HTML 实测](https://www.nicovideo.jp/)（一次性提取 49 个子域，引用见 jp-domains.txt）
- 后续更新入口: 无
- 快测: 200
- 大陆可达性: 需代理（依据: gfw.txt 收录 +.nicovideo.jp；GreatFire [blocked @2026-09-15](https://en.greatfire.org/nicovideo.jp)）
- 备注: 日本区；官方动画频道与「dアニメストア ニコニコ支店」均在此域体系内

#### U-NEXT
- 类别: 日本本土
- 域名: unext.jp | video.unext.jp | www.video.unext.jp | video-static.unext.jp | static01.ca.unext.jp | account.unext.jp | myaccount.unext.jp | oauth.unext.jp | registration.unext.jp | mobile.unext.jp | help.unext.jp | beacon.unext.jp | lcms-beacon.unext.jp | rconf.unext.jp | sidecar.unext.jp | s-flow.unext.jp | cc.unext.jp | aeoncinema-video.unext.jp | unext.co.jp | unext-info.jp
- 性质: 日本最大级综合配信（动画库极大）；static01.ca.unext.jp 与 video-static.unext.jp 为静态/CDN；beacon*/lcms-beacon 为统计回传；播放主站 video.unext.jp
- 来源: [video.unext.jp 首页 HTML 实测](https://video.unext.jp/)（上述全部子域均在首页引用，另有 coupon/contact/cinemacoupon 等见 jp-domains.txt）
- 后续更新入口: 无
- 快测: 200
- 大陆可达性: 存疑（依据: GreatFire 未测、GFW 名单未收录）→ 倾向直连（内容锁日本区）
- 备注: Paravi 于 2023-06-30 并入（[ja.wikipedia: Paravi](https://ja.wikipedia.org/wiki/Paravi)）；「アニメ放題」为其旗下品牌

#### DMM TV
- 类别: 日本本土
- 域名: tv.dmm.com | awsimgsrc.dmm.com | tag-api.i3.dmm.com | dmm.com | www.dmm.com
- 性质: DMM 系配信（动画独占多）；awsimgsrc.dmm.com 为图片 CDN；dmm.com 为共用大域（成人/PC 游戏区 dmm.co.jp 为另域）
- 来源: [tv.dmm.com/vod/ 首页 HTML 实测](https://tv.dmm.com/vod/)（og:image 于 awsimgsrc.dmm.com、tag-api.i3.dmm.com）
- 后续更新入口: 无
- 快测: 200
- 大陆可达性: 存疑（依据: GreatFire [dmm.com 可达 @2026-04-27](https://en.greatfire.org/dmm.com)、[www.dmm.com 可达 @2026-04-09](https://en.greatfire.org/www.dmm.com)；但 gfw.txt 收录 dmm.co.jp 与 www.dmm.com）→ 建议按需代理
- 备注: 日本区；tv.dmm.com 本身未被 GreatFire 测过

#### FOD（フジテレビ）
- 类别: 日本本土
- 域名: fod.fujitv.co.jp | i.fod.fujitv.co.jp
- 性质: 富士电视台 OTT；i.fod.fujitv.co.jp 为图片 CDN
- 来源: [fod.fujitv.co.jp 首页 HTML 实测](https://fod.fujitv.co.jp/)（引用 i.fod.fujitv.co.jp）
- 后续更新入口: 无
- 快测: 200 / i.fod.fujitv.co.jp 403（存在）
- 大陆可达性: 存疑（依据: GreatFire 未测、GFW 名单未收录）→ 倾向直连（内容锁日本）
- 备注: 日本区；富士系动画

#### Lemino（NTT docomo）
- 类别: 日本本土
- 域名: lemino.docomo.ne.jp | conf.lemino.docomo.ne.jp | if.lemino.docomo.ne.jp
- 性质: docomo 系配信；conf（配置）/if（图片）为服务子域
- 来源: [lemino.docomo.ne.jp 首页 HTML 实测](https://lemino.docomo.ne.jp/)（引用 conf/if.lemino.docomo.ne.jp）
- 后续更新入口: 无
- 快测: 200
- 大陆可达性: 存疑（依据: GreatFire 未测、GFW 名单未收录）→ 倾向直连
- 备注: 日本区；动画/LIVE 含独占

#### TELASA（テレ朝×KDDI）
- 类别: 日本本土
- 域名: telasa.jp | www.telasa.jp | help.telasa.jp | navi.telasa.jp | cdn.videopass.jp | api-videopass.kddi-video.com | api-videopass-sockets.kddi-video.com | image-cf.kddi-video.com
- 性质: 朝日电视台×KDDI 系配信；播放 API/图片走 kddi-video.com 系；cdn.videopass.jp 为 CDN 域
- 来源: [www.telasa.jp 首页 HTML 实测](https://www.telasa.jp/)（引用上述全部子域）
- 后续更新入口: https://help.telasa.jp/
- 快测: 200（跳转 /unlimited）
- 大陆可达性: 存疑（依据: GreatFire 未测、GFW 名单未收录）→ 倾向直连
- 备注: 日本区；动画以朝日系作品为主

#### バンダイチャンネル（Bandai Channel）
- 类别: 日本本土
- 域名: b-ch.com | www.b-ch.com | assets.b-ch.com | image2.b-ch.com | faq.b-ch.com | info.b-ch.com
- 性质: 万代南梦宫系动画配信（运营商 バンダイナムコフィルムワークス www.bnfw.co.jp）；assets/image2 为静态 CDN
- 来源: [www.b-ch.com 首页 HTML 实测](https://www.b-ch.com/)（引用 assets/image2/faq/info.b-ch.com）
- 后续更新入口: https://faq.b-ch.com/
- 快测: www.b-ch.com 200；apex b-ch.com 连接失败（http/https 均 000，实测）
- 大陆可达性: 存疑（依据: GreatFire 未测、GFW 名单未收录）→ 倾向直连（内容锁日本）
- 备注: 日本区；部分作品原版无字幕

#### アニメタイムズ（Anime Times）
- 类别: 日本本土（Amazon Prime Video 频道运营方）
- 域名: animetimes.co.jp | www.animetimes.co.jp | animetimes-store.com | m.imageimg.net（图片 CDN）
- 性质: Prime Video 内动画频道「アニメタイムズ」运营方官网；正片经 amazon.co.jp/primevideo 分发（共用域不收）
- 来源: [www.animetimes.co.jp 首页实测](https://www.animetimes.co.jp/)（title「アニメタイムズ」、链 amazon.co.jp/gp/video/channel/…）
- 后续更新入口: 无
- 快测: www.animetimes.co.jp 200
- 大陆可达性: 存疑（依据: GreatFire 未测、GFW 名单未收录）→ 倾向直连（内容经 Amazon）
- 备注: 注意 anime-times.jp 为 NXDOMAIN（实测），勿写入规则

#### Hulu Japan（HJ ホールディングス，日本テレビ系）
- 类别: 日本本土
- 域名: hulu.jp | www.hulu.jp | id.hulu.jp | help.hulu.jp | news.hulu.jp | hjholdings.tv | images.prod.hjholdings.tv | mapi.prod.hjholdings.tv | papi.prod.hjholdings.tv | playback.prod.hjholdings.tv | token.prod.hjholdings.tv | happyon.jp | streaks.jp | players.streaks.jp | bees.streaks.jp | manifest.streaks.jp
- 性质: 日本 Hulu（与 hulu.com 美国无关）；hjholdings.tv 为其基础设施域（playback/token/mapi 为播放与接口）；streaks.jp 为播放器/CDN 基础设施（players/bees/manifest 子域）；happyon.jp 为旧域族
- 来源: [www.hulu.jp 首页 HTML 实测](https://www.hulu.jp/)（引用上述全部域）
- 后续更新入口: https://help.hulu.jp/
- 快测: www.hulu.jp 200
- 大陆可达性: 存疑偏直连（依据: GreatFire [hulu.jp reachable @2026-02-20](https://en.greatfire.org/hulu.jp)；未入 GFW 名单）
- 备注: 日本区；动画库大、独家作多

### 已确认失效/合并（不建议收录）
- Funimation: funimation.com 实测 302→crunchyroll.com（2026-10-06）；2022-03-01 宣布 Funimation/Wakanim/VRV 服务并入 Crunchyroll（[en.wikipedia: Crunchyroll](https://en.wikipedia.org/wiki/Crunchyroll)）
- Wakanim: wakanim.tv 实测 302→crunchyroll.com（2026-10-06）
- VRV: vrv.co 实测 302→crunchyroll.com；其 *.vrv.co 曾为 Crunchyroll 视频 CDN（multi-downloader-nx #732），2026-10 实测 v.vrv.co 已 NXDOMAIN，勿硬编码
- AnimeLab: animelab.com DNS 尚可解析但连接失败（实测 000）；2021-06-17 品牌并入 Funimation、2021-12-09 关停（[en.wikipedia: AnimeLab](https://en.wikipedia.org/wiki/AnimeLab)）
- GYAO!: gyao.yahoo.co.jp 无 A 记录（实测）；2023-03-31 17:00 服务终了（[ja.wikipedia: GYAO!](https://ja.wikipedia.org/wiki/GYAO!)）
- Paravi: paravi.jp 现为跳转页（Next.js internal-redirect，实测）；2023-06-30 并入 U-NEXT（[ja.wikipedia: Paravi](https://ja.wikipedia.org/wiki/Paravi)）
- アニメ放題: animehodai.jp 无 A 记录（实测）；服务现由 U-NEXT 运营（官网在 unext.jp），旧域不收
- anime-times.jp: NXDOMAIN（实测，2026-10-06）；正确域为 animetimes.co.jp

### 共用域不收（备注）
- Netflix（netflix.com）、Disney+（disneyplus.com）、Prime Video（primevideo.com / amazon.co.jp 的 video 区）、Max（max.com）、YouTube（Muse/Ani-One 官方频道所在）等大平台共用大域不收，其动漫区不单独建条。
- Hulu(US) 与 Disney+/Max 首页互链（Disney 体系），但因动漫区权重大且有独立域，仍单列（见上）。
- 共用 CDN 仅收录与站点强绑定的子域（如 bahamut.akamaized.net、vod-abematv.akamaized.net、upos-bstar-mirrorakam.akamaized.net），不整域收录 akamaized.net/cloudfront.net/alicdn.com 等。

## 3. 海外动漫聚合站

- 调研日期：2026-10-06
- 范围：非官方动漫聚合/在线观看站（英文聚合 + 中文向 + 意/西语），不含成人向、不含日系官方平台（Crunchyroll/巴哈等）、不含 BT/字幕组站（dmhy/mikan/nyaa）
- 快测环境：本机（流量经路由器代理）`curl -A 'Mozilla/5.0'`；**超时 ≠ 死站，403 多为 Cloudflare 盾 = 存活**；必要时用 r.jina.ai 交叉验证
- 可达性判定：本机经代理，无法直接验证"大陆裸连"，故依据 = CF 盾/公告/被墙记录，逐站给出，拿不准标「存疑」

---

### 0. 来源与 aniyomi 生态现状（必读，决定可信度）

- **aniyomi 官方扩展仓库已存档**：`github.com/aniyomiorg/aniyomi-extensions` 页面显示「This repository was archived by the owner on Jul 5, 2025. It is now read-only.」；且存档前已遭 DMCA 清洗，`src/` 只剩 `src/all`（googledrive/jellyfin/torrent 等），**站点类源码（en/zh/it/es）已清空** → 不能再当"当前域名"来源。
- **社区继任（本次实际使用的权威来源）**：
  - `yuzono/anime-extensions`（Anikku/Aniyomi 系，2026 年仍在更新，仓库内 `src/en|zh|it|es` 有 baseUrl/mirrors）→ https://github.com/yuzono/anime-extensions
  - `Kohi-den/extensions-source`（2026 年仍活跃）→ https://github.com/Kohi-den/extensions-source
  - `Sadwhy/aniyomi-extensions`（保留 gogoanime/kaido/nineanime/zoro 等旧源）→ https://github.com/Sadwhy/aniyomi-extensions
  - 聚合索引：almightyhak/aniyomi-anime-repo、`skepsun.github.io/kototoro-repo-hub`（索引型，不含 baseUrl）
- 其他来源：**FMHY** https://fmhy.net/video 与源文件 https://github.com/fmhy/edit/blob/main/docs/video.md ；**EverythingMoe 墓地页** https://everythingmoe.com/graveyard ；各站官方域名发布页。
- 重要结构性发现：EverythingMoe 墓地页给大量站点打 `GOGO`/`HIA`/`MULT` 标记 —— 很多"独立站"只是 Gogoanime / HiAnime 后端的换皮前端，**后端一死就成批阵亡**（2025 Gogo 停更、2026-03 HiAnime 关停 → 连带死站 100+）。

---

#### 一、英文聚合站

#### AnimePahe
- 类别: 英文聚合（硬字幕/生肉风险源）
- 域名: animepahe.pw | animepahe.com | animepahe.org | animepahe.su | pahe.win | kwik.cx
- 性质: 老牌硬字幕聚合，下载/在线双模式，带"Some NSFW"标注
- 来源: [FMHY video.md](https://github.com/fmhy/edit/blob/main/docs/video.md)（第 351 行，列 animepahe.pw）；[yuzono src/en/animepahe](https://github.com/yuzono/anime-extensions/tree/main/src/en/animepahe)（源码内域名单 `animepahe.com/.org/.pw`）
- 后续更新入口: yuzono 与 Kohi-den 的 `src/en/animepahe`（两库都有，更新最勤）
- 快测: animepahe.pw 403（Cloudflare Attention Required，存活）| animepahe.com / .org → 403 且最终跳 .pw | animepahe.ru 200 但最终 URL 变为 animepahe.su | pahe.win 403 | kwik.cx 403
- 大陆可达性: 需代理（CF 全站盾 + 老域名长期被墙；本机经代理访问）
- 备注: **animepahe.ru 已被 .pw 品牌取代**（FMHY 已更新为 .pw）；pahe.win = 下载/播放 CDN，kwik.cx = 视频承载域，规则里建议保留旧域以便接管

#### Anikoto
- 类别: 英文聚合（AniWatch 系别名站群）
- 域名: anikototv.to | anikoto.cz | anikoto.me | anikoto.net | anikototv.se | anikoto.site
- 性质: Sub/Dub/Auto-Next，与 AnimeSuge 同后端、并称双站
- 来源: 官方域名列表页 [anikoto.site](https://anikoto.site/)（正文列出 5 个 official streaming domains）；[yuzono src/en/anikoto](https://github.com/yuzono/anime-extensions/tree/main/src/en/anikoto)（源码 mirrors 名单与此一致）；[FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)（⭐ 条目列 anikototv.to）
- 后续更新入口: 站点官方列表页 anikoto.site；yuzono `src/en/anikoto`
- 快测: anikototv.to 200 | anikoto.cz 200 | anikoto.me 200 | anikoto.net 200 | anikototv.se 200 | anikoto.site 200（旧域 **anikoto.to 000 已失效**）
- 大陆可达性: 需代理（CF 盾、.to/.cz 无国内备案，2026-01 德里高院 Dynamic+ 禁令名单内）
- 备注: 高变动；播放器域 megaplay.buzz（源码内）；域名页自述"仿站多，只认本清单"

#### AnimeSuge
- 类别: 英文聚合（Anikoto 姊妹站）
- 域名: suge.to | animesuge.cz | animesuge.re | anisuge.tv | anisuge.se | animesugez.tv | animesuge.bid
- 性质: Sub/Dub/Auto-Next，与 Anikoto 同源
- 来源: 官方域名列表页 [animesuge.bid](https://animesuge.bid/)（"These are the only official and verified AnimeSuge domains"逐条列出）；[FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)
- 后续更新入口: animesuge.bid（域名清单页）/ 官方 Telegram、Reddit
- 快测: suge.to 200 | animesuge.cz 200 | animesuge.re 200 | anisuge.tv 200 | anisuge.se 200 | animesugez.tv 200 | animesuge.bid 200（旧域 **animesuge.to 000 已失效**）
- 大陆可达性: 需代理（同上，且是德里高院禁令点名对象 animesugez.to）
- 备注: 高变动；与 Anikoto 同 IP 段/同模板，规则里可合组

#### 9anime（现役站）
- 类别: 英文聚合
- 域名: 9animstv.to
- 性质: 借"9anime"品牌续命的 WordPress 型站，Sub/Dub
- 来源: [FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)（第 400 行 [9anime](https://9animstv.to/)）
- 后续更新入口: 无（FMHY 条目）
- 快测: 9animstv.to 200（"9anime - Watch Anime online with DUB and SUB for FREE"，141KB 首页=真站点）
- 大陆可达性: 需代理（品牌名即被墙关键词，CF 盾）
- 备注: **原 9anime.to → aniwave.to 血统已终结**：aniwave.to 302 → ww38.aniwave.to（000，死）；aniwave.live 302 → ww38.aniwave.live（死）。现役 "AniWave" 品牌见下条

#### AniWave 继任品牌（aniwaves.ru 等）+ HiAnime 继任（hianimes.*）
- 类别: 英文聚合（**HiAnime/Aniwatch/Zoro 血统的伪续**，注意风险）
- 域名: aniwaves.ru | hianimes.ru | hianimes.se | animewave.to | aniwave.cz | 123animehub.cc
- 性质: 沿用 Aniwave/HiAnime 品牌的新站群，Sub/Dub/Auto-Next
- 来源: [FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)（第 368 行 "Aniwave "（aniwaves.ru）" + hianimes.ru + 123animehub.cc）；[yuzono src/en/aniwaves](https://github.com/yuzono/anime-extensions/tree/main/src/en/aniwaves)（baseUrl `aniwaves.ru`）；[yuzono src/en/aniwave](https://github.com/yuzono/anime-extensions/tree/main/src/en/aniwave)（baseUrl `animewave.to`，mirror `aniwave.cz`）
- 后续更新入口: yuzono `src/en/aniwave`、`src/en/aniwaves`；FMHY 条目
- 快测: aniwaves.ru 200 | hianimes.ru 200（title 自称 HiAnime）| hianimes.se 200（title 带 "(official)"）| animewave.to 200 | aniwave.cz 200（301→animewave.to）| 123animehub.cc 200
- 大陆可达性: 需代理（俄罗斯/CF 主机 + 品牌被墙）
- 备注: **原 hianime.to 已停运**（hianime.to 本机 000；aniwatch.to 404；zoro.to 000），社区警告 "HiAnime 复活域"有钓鱼风险；FMHY/EverythingMoe 把 aniwaves.ru 当独立条目维护，可作规则兜底

#### Miruro
- 类别: 英文聚合（FMHY ⭐ 首推）
- 域名: miruro.com | miruro.tv | miruro.bz | miruro.cx | miruro.to
- 性质: Hard/Soft Sub + Dub + Auto-Next，多后端聚合（现代 SPA）
- 来源: [FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)（⭐ **Miruro**，列 5 个域 + status 页）；[EverythingMoe](https://everythingmoe.com/s/miruro)
- 后续更新入口: 自带 status.miruro.com；GitHub github.com/Miruro-no-kuon/Miruro；r/miruro
- 快测: www.miruro.com 200（真站首页 107KB）
- 大陆可达性: 需代理（CF + SPA 依赖外部后端域名）
- 备注: 域名多且会轮换，建议 5 域全收；播放需放行其后端/embed 域（未逐一枚举）

#### KickAssAnime
- 类别: 英文聚合
- 域名: kaa.lt | kaa.to | kaa.am | kaas.am
- 性质: Sub/Dub/Auto-Next，老牌站多次迁域
- 来源: [FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)（⭐ KickAssAnime → kaa.lt）；[Kohi-den src/en/kickassanime](https://github.com/Kohi-den/extensions-source/tree/main/src/en/kickassanime)（源码 baseUrl `kaa.to`，mirror `kaa.am`/`kaas.am`）
- 后续更新入口: Kohi-den `src/en/kickassanime`；官方 Telegram/ Discord（FMHY 条目内有）
- 快测: kaa.lt 200（真站 152KB）
- 大陆可达性: 需代理（CF 盾）
- 备注: 源码域(kaa.to)与 FMHY 域(kaa.lt)不同，两套都建议收录

#### AllManga（原 AllAnime）
- 类别: 英文聚合（含生肉/多语字幕）
- 域名: allmanga.to
- 性质: Sub/Dub，后端 API 丰富（allanime.day 系），被大量第三方 App 调用
- 来源: [Kohi-den src/en/allanime](https://github.com/Kohi-den/extensions-source/tree/main/src/en/allanime)（baseUrl `allmanga.to`，旧域 allanime.to）；[FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)（"All Manga allmanga.to"）
- 后续更新入口: Kohi-den `src/en/allanime`
- 快测: allmanga.to 200（真站）；旧域 allanime.to 000（已死）
- 大陆可达性: 需代理（CF；旧域曾长期被墙）
- 备注: 别与 "MKissa"（FMHY 并列条目，mkissa.to，实测 200）混淆

#### KotoTV / AniWatch
- 类别: 英文聚合（AniWatch 品牌残留）
- 域名: kototv.to | aniwatch.rest
- 性质: Sub/Dub/Auto-Next
- 来源: [FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)（第 374 行 KoToTV + Mirrors aniwatch.rest）
- 后续更新入口: 官方 Discord（FMHY 条目）
- 快测: kototv.to 200（真站 116KB）| aniwatch.rest 200（AniWatch 品牌站 29KB）
- 大陆可达性: 需代理
- 备注: aniwatch.rest 是少见的 "AniWatch" 品牌存活域；原 aniwatch.to 已 404

#### AnimeX
- 类别: 英文聚合（新品牌）
- 域名: animex.one
- 性质: Sub/Dub/Auto-Next
- 来源: [FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)（⭐ 条目）
- 后续更新入口: 官方 Discord（FMHY 条目）
- 快测: animex.one 200（真站 71KB）
- 大陆可达性: 需代理
- 备注: 与 Indonesia-only 的 "AnimeX" 云流扩展（HatsuneMikuUwU/AnimeX）无关

#### Ani.pm
- 类别: 英文聚合
- 域名: ani.pm
- 性质: Sub/Dub
- 来源: [FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)（⭐）；[yuzono src/en/anipm](https://github.com/yuzono/anime-extensions/tree/main/src/en/anipm)（扩展存在，源码目录内为 AniList 驱动）
- 后续更新入口: yuzono `src/en/anipm`
- 快测: ani.pm 200
- 大陆可达性: 需代理
- 备注: 无

#### Re:ANIME
- 类别: 英文聚合
- 域名: reanime.to | reanime.cz | reanime.wtf | reindex.to | restatus.me | flixcloud.cc
- 性质: Sub/Dub/Auto-Next + 自有 CDN(flixcloud.cc) + 索引/状态页
- 来源: [FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)（⭐）；[yuzono src/en/reanime](https://github.com/yuzono/anime-extensions/tree/main/src/en/reanime)（源码含 reanime.to/.cz/.wtf、flixcloud.cc、restatus.me、reindex.to）
- 后续更新入口: yuzono `src/en/reanime`；官方 Discord；restatus.me
- 快测: 未逐测（来源为源码+FMHY；FMHY 更新时间新）
- 大陆可达性: 需代理（CF）
- 备注: 带自有视频 CDN 域 flixcloud.cc（fetch*.flixcloud.cc），规则需一并放行

#### Senshi
- 类别: 英文聚合
- 域名: senshi.to | s.vidcloud.se | cdn.vidcloud.se
- 性质: Sub/Dub/Auto-Next，自有 vidcloud.se 播放/CDN
- 来源: [FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)；[yuzono src/en/senshi](https://github.com/yuzono/anime-extensions/tree/main/src/en/senshi)（源码 baseUrl senshi.to + cdn.vidcloud.se）
- 后续更新入口: yuzono `src/en/senshi`
- 快测: senshi.to 200（当前为 "New Website" 施工页，2.3KB）
- 大陆可达性: 需代理
- 备注: 站点改版中，域名存续但首页未就绪

#### AniZone
- 类别: 英文聚合（生肉/英字）
- 域名: anizone.to
- 性质: Sub（无 Dub）
- 来源: [FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)；[yuzono src/all/anizone](https://github.com/yuzono/anime-extensions/tree/main/src/all/anizone)（baseUrl anizone.to）
- 后续更新入口: yuzono `src/all/anizone`
- 快测: 未单测（FMHY+源码）
- 大陆可达性: 需代理
- 备注: 无

#### AniKage
- 类别: 英文聚合
- 域名: anikage.cc | og.bakayaro.live
- 性质: Sub/Dub，播放直链走 og.bakayaro.live
- 来源: [yuzono src/en/anikage](https://github.com/yuzono/anime-extensions/tree/main/src/en/anikage)（baseUrl `anikage.cc` + `og.bakayaro.live`）；[FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)（"Anikage anikage.cc"）
- 后续更新入口: yuzono `src/en/anikage`
- 快测: anikage.cc 200（真站 241KB）
- 大陆可达性: 需代理
- 备注: CDN 域 og.bakayaro.live 必须一并放行

#### Anikuro
- 类别: 英文聚合
- 域名: anikuro.to | anikuro.ru | anikuro.site
- 性质: Sub/Dub
- 来源: [yuzono src/en/anikuro](https://github.com/yuzono/anime-extensions/tree/main/src/en/anikuro)（mirrors `anikuro.to`/`anikuro.ru`）；[FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)（AniKuro to/ru + Status）
- 后续更新入口: yuzono `src/en/anikuro`；anikuro.site 状态页
- 快测: anikuro.to 200（真站 57KB）
- 大陆可达性: 需代理
- 备注: ⚠ 冲突：EverythingMoe 墓地页已把 Anikuro 列死（https://everythingmoe.com/graveyard），但实测 .to 仍返回完整站点 → 按"存续但可能随时死"处理

#### AniNeko
- 类别: 英文聚合
- 域名: anineko.to | otakuhg.site | playmogo.com | vivibebe.site（后三者为其播放/源站域）
- 性质: Sub/Dub
- 来源: [yuzono src/en/anineko](https://github.com/yuzono/anime-extensions/tree/main/src/en/anineko)（baseUrl anineko.to + 三个源域）；EverythingMoe 墓地已列 AniNeko
- 后续更新入口: yuzono `src/en/anineko`（扩展仍在仓库中）
- 快测: anineko.to 200 但返回 PHP 报错页（PDO Connection refused，后端 `nekovault.online` 数据库宕）→ **实质已死**
- 大陆可达性: 需代理（已死，规则可不收）
- 备注: 典型"扩展还在更新、站点已崩"的案例，域名保留但别指望可用

#### Anichi
- 类别: 英文聚合
- 域名: anichi.to
- 性质: Sub/Dub（AniList 元数据）
- 来源: [yuzono src/en/anichi](https://github.com/yuzono/anime-extensions/tree/main/src/en/anichi)（baseUrl anichi.to）
- 后续更新入口: yuzono `src/en/anichi`
- 快测: anichi.to 200（真站 20KB）
- 大陆可达性: 需代理
- 备注: 播放走 megaplay.buzz（与 Anikoto 同播放器域）

#### XAnime
- 类别: 英文聚合
- 域名: xanime.me | xanime.app
- 性质: Sub/Dub，GraphQL 后端
- 来源: [yuzono src/en/xanime](https://github.com/yuzono/anime-extensions/tree/main/src/en/xanime)（mirrors `xanime.me`/`xanime.app`）
- 后续更新入口: yuzono `src/en/xanime`
- 快测: xanime.me 200（483KB 真站）
- 大陆可达性: 需代理
- 备注: 无

#### AnimeGG
- 类别: 英文聚合
- 域名: animegg.org
- 性质: 老牌 Sub/Dub 站
- 来源: [yuzono src/en/animegg](https://github.com/yuzono/anime-extensions/tree/main/src/en/animegg)、[Kohi-den src/en/animegg](https://github.com/Kohi-den/extensions-source/tree/main/src/en/animegg)（baseUrl www.animegg.org）
- 后续更新入口: 两库 `src/en/animegg`
- 快测: 未单测（两库源码均在，视为存续）
- 大陆可达性: 存疑（老站曾可直接访问，后加 CF，本机经代理未单测）
- 备注: 无

#### AnimeParadise
- 类别: 英文聚合（社区向）
- 域名: animeparadise.moe | api.animeparadise.moe | stream.animeparadise.moe
- 性质: Sub/Dub，自有 API + 流媒体子域
- 来源: [yuzono src/en/animeparadise](https://github.com/yuzono/anime-extensions/tree/main/src/en/animeparadise)；[FMHY](https://github.com/fmhy/edit/blob/main/docs/video.md)
- 后续更新入口: yuzono 源；官方 Discord
- 快测: www.animeparadise.moe 200（真站 73KB）
- 大陆可达性: 需代理
- 备注: .moe 三个子域建议全收（API/stream 分离）

#### WCO 系（Watch Cartoons Online / WCO）
- 类别: 英文聚合（动画片+动漫 Sub/Dub）
- 域名: wco.tv | wcoflix.tv | wcostream.tv | wcoanimesub.tv | wcoanimedub.tv | wcoforever.net | wcofun.com | wcostream.com | wcoforever.com
- 性质: 老牌"欧美卡通 + 日番"混合站群，多个品牌域互跳
- 来源: [yuzono src/en/wcofun/wcostream/wcoanimesub/wcoanimedub/wcoforever/wcotv](https://github.com/yuzono/anime-extensions/tree/main/src/en)（6 个独立扩展）；[Kohi-den src/en/wcofun,wcostream](https://github.com/Kohi-den/extensions-source/tree/main/src/en)
- 后续更新入口: 两库 `src/en/wco*`
- 快测: wco.tv 200 | wcoanimesub.tv 200 | wcoanimedub.tv 200 | wcoforever.net 200 | wcofun.com 403→wcoflix.tv（CF 盾，存活）| wcostream.com 403→wcostream.tv（CF 盾）
- 大陆可达性: 需代理（CF 盾；老 .com 域在国内有 DNS 污染记录）
- 备注: 新旧域互跳关系：wcofun.com→wcoflix.tv、wcostream.com→wcostream.tv、wcoforever.com→wcoforever.net

#### FMHY 其余英文新品牌（域名来自 FMHY，未逐一快测，同批收录）
- 域名: mkissa.to | anistream.one | justanime.to | kazora.cc | nekowatch.xyz | anidap.lol | anilight.live | lunarx.to | anidoor.me | anisnatch.top | meguanime.com | anime.nexus | luffytv.live | anichan.to | animedex.fun | enma.lol | anikura.club | 1ani.me | kyren.moe | yenime.net | banime.top | animeonsen.xyz | sakusaku.to | babyanime.top | aniclipse.com | anihq.cc | luna-stream.me | aninami.site | kawaiianime.cc | fireani.me | piratexplay.cc | anify.to | animenosub.to | yomi.to
- 性质: 2025-2026 涌现的大量 Sub/Dub 小站，多数无独立后端
- 来源: [FMHY video.md](https://github.com/fmhy/edit/blob/main/docs/video.md)（Anime Streaming 章）
- 后续更新入口: FMHY 同页（该页更新最勤者即此清单）
- 快测: 抽测 mkissa.to 200 | anistream.one 200 | justanime.to 200 | kazora.cc 200 | nekowatch.xyz 200 | anidap.lol 200 | ani.pm 200 | animex.one 200（抽测均活）
- 大陆可达性: 需代理（清一色 CF）
- 备注: 高变动+仿站多，建议只按 FMHY 原文列表周期性同步，勿扩写

### 小站备注（Kawaiifu / Tokuzilla / BestDubbedAnime / AnimeTake / Kimoitv）
- Kawaiifu: kawaiifu.com，来源 [Kohi-den src/en/kawaiifu](https://github.com/Kohi-den/extensions-source/tree/main/src/en/kawaiifu)；快测 403（CF 盾）；**EverythingMoe 墓地已列死** → 存疑
- Tokuzilla: tokuzilla.net，[Kohi-den src/en/tokuzilla](https://github.com/Kohi-den/extensions-source/tree/main/src/en/tokuzilla)；快测 **000 超时**（本机不可达）
- BestDubbedAnime: bestdubbedanime.com，[Kohi-den 源](https://github.com/Kohi-den/extensions-source/tree/main/src/en/bestdubbedanime)；快测 200 但 301 到 `aestheticode.net`（换皮）；**墓地已列死** → 存疑
- AnimeTake: animetake.tv，[yuzono src/en/animetake](https://github.com/yuzono/anime-extensions/tree/main/src/en/animetake)；快测 **404（站点级 404）** → 疑似已死
- Kimoitv: kimoitv.com，[yuzono/Kohi-den src/en/kimoitv](https://github.com/yuzono/anime-extensions/tree/main/src/en/kimoitv)；快测 403（CF 盾，疑似存活）

---

#### 二、中文向海外聚合站（面向中文用户、服务器多在墙外，高变动）

#### 樱花动漫（YHDM 系 · 现役 App+网页版）
- 类别: 中文向聚合
- 域名: qlyyz.xyz | mub.acgdm001.com(风车CDN,见下条) — 本条仅 qlyyz.xyz
- 性质: 基于 Kazumi 规则格式的跨平台追番应用 + 网页版（聚合多线路，非单一站）
- 来源: [yhdm-rules-skill README](https://github.com/yhdmgf/yhdm-rules-skill)（2026-10-06 push，正文指向 https://qlyyz.xyz/）；[qldwj/Kazumikfc](https://github.com/qldwj/Kazumikfc)（官网 GitHub 按钮指向，即樱花的 Kazumi 分支）；站点实测
- 后续更新入口: qlyyz.xyz（含 /docs 文档 /yhdm 网页版）；Telegram t.me/YHDMLT；QQ 群
- 快测: qlyyz.xyz 200（"樱花动漫 - 跨平台在线弹幕追番应用"）| qlyyz.xyz/yhdm 200（网页版 "好看的二次元番剧都在这里"）
- 大陆可达性: 存疑（页面声明"资源来自网络公开分享"，未声明大陆可用；.xyz + CF 常见封锁）
- 备注: **老"樱花动漫 yhdm"多个发布页已死**（dm519.fans 与 yhdmp.net 均变成 parklogic 停放页，实测 200 但内容为域名出租）；"樱花"品牌仿站极多，只认官方 App 入口

#### 风车动漫（dm530 系 · 现役）
- 类别: 中文向聚合
- 域名: fcbbcc.com | fengchedm.com | fengchedm.cc | acgdm001.com
- 性质: 风车动漫官网（模板互跳），图片 CDN 在 mub.acgdm001.com
- 来源: 站点实测（fengchedm.com 200 → 301 → http://www.fcbbcc.com/，title "风车动漫－专注动漫的门户网站"，ASCII "dm530" 品牌）；搜索侧记录见旧发布页 dmla.fans（已 parklogic）
- 后续更新入口: 无稳定发布页（dmla.fans 已死）
- 快测: www.fcbbcc.com 200（HTTP，70KB 真站）| fengchedm.com 200（301→fcbbcc.com）| fengchedm.cc 000/超时 | dm530.com 200 但为 "This domain is for sale" 停放页 → 死
- 大陆可达性: 存疑（站点为大陆受众镜像、HTTP 明文、无 CF，**部分网络可直连**；但域名轮换频繁）
- 备注: **高变动**：dm530 品牌下 dm530.com/.net/.org 多为停放/仿站，以 fcbbcc.com 为准；CDN mub.acgdm001.com 需一并放行

#### AGE 动漫
- 类别: 中文向聚合
- 域名: agedm.io | age.tv | agedm.com | agefans.com | ageapp.app
- 性质: 老牌中文在线动漫站，官方有 GitHub 发布页
- 来源: 官方发布页 [github.com/agefanscom/website](https://github.com/agefanscom/website)（README「最新域名 https://www.agedm.io」；易记域 age.tv / agedm.com / agefans.com；App ageapp.app；已阵亡 agedm.vip/.live/.me、agefans.la）
- 后续更新入口: github.com/agefanscom/website（**官方发布页，更新于此**）；百度贴吧 AGE动漫吧
- 快测: www.agedm.io 403（CF 盾，存活）| age.tv 000（本机超时，存疑）| agedm.com 000（本机超时）| agefans.com 000（本机超时）| ageapp.app 200（"AGE动漫 - APP下载导航"）
- 大陆可达性: 需代理/**部分可直连**（官方 README 自述"江苏、河南、重庆等地封禁严重，本站 2~3 个月换域名"，并教用户换公共 DNS 防劫持）→ 大陆可达性不稳定，随地区/时间变化
- 备注: **官方自己承认域名 2~3 个月一换**，必须以发布页为准；www.agefans.com 已被"重置"标注不可用

#### Anime1（台湾）
- 类别: 中文向聚合（繁中）
- 域名: anime1.me | v.anime1.me | sta.anicdn.com | d1zquzjgwo9yb.cloudfront.net
- 性质: 台湾老牌在线动漫（繁中字幕），API 与静态资源分域
- 来源: [yuzono src/zh/anime1](https://github.com/yuzono/anime-extensions/tree/main/src/zh/anime1)、[Kohi-den src/zh/anime1](https://github.com/Kohi-den/extensions-source/tree/main/src/zh/anime1)（baseUrl anime1.me，videoApiUrl v.anime1.me，CDN sta.anicdn.com / CloudFront）
- 后续更新入口: 两库 `src/zh/anime1`
- 快测: anime1.me 403（title "注意！"，疑为盾/地区提示页，判存活）
- 大陆可达性: 需代理（V.anime1.me 与 CloudFront 域名在国内不可达记录明确）
- 备注: CDN 域 CloudFront 泛化，Clash 里建议按具体子域 sta.anicdn.com 放行

#### 稀饭动漫 / 小新TV / 泥视频 / 爱壹帆（中文向长视频动漫）
- 类别: 中文向聚合（海外华人向）
- 域名: xifanacg.com（dm.xifanacg.com）| xiaoxintv.cc | nivod.cc（e.kortw.cc）| iyf.tv（m10.iyf.tv / rankv21.iyf.tv）| cycani.org（player.cycanime.com）
- 性质: 面向海外华人的动漫/影视站（iyf=爱壹帆含动漫分区），多为"长视频站+动漫分类"
- 来源: [yuzono](https://github.com/yuzono/anime-extensions/tree/main/src/zh) / [Kohi-den src/zh](https://github.com/Kohi-den/extensions-source/tree/main/src/zh)（xfani/cycity/iyf/nivod/xiaoxintv 五个扩展，baseUrl 即上述域）
- 后续更新入口: 两库 `src/zh/*`
- 快测: nivod.cc 200（"泥视频 - 海外华人在线影院"）| iyf.tv 403（CF "Just a moment"，存活）| cycani.org 403（正文"不提供服务"，站点已关停服务）| xifanacg.com / xiaoxintv.cc 未单测
- 大陆可达性: 需代理（明确面向海外华人，国内多数被墙；cycani 已终止服务）
- 备注: cycani 已声明"不提供服务"→ 死站；xifan/xiaoxintv 保留观察

#### girigiri 爱动漫
- 类别: 中文向聚合（简/繁）
- 域名: girigirilove.com（ani.girigirilove.com / anime.girigirilove.com）| girigirilove.top
- 性质: 中文弹幕追番站（含多语言、1080P）
- 来源: 站点实测（anime.girigirilove.com 200 → 跳 ani.girigirilove.com，title "girigiri愛動漫~just a little love~"）；搜索侧记录 girigiri.cn（2026-08 新注册）
- 后续更新入口: 无固定发布页（站内公告）
- 快测: ani.girigirilove.com 200（真站）| anime.girigirilove.top 000（本机超时）
- 大陆可达性: 存疑（站点提示需"特殊网络方式"访问 = 自认被墙）
- 备注: 高变动；主域是子域名形态，规则里按 `girigirilove.com` 整域放行更省事

#### 妮可动漫（nicotv）
- 类别: 中文向聚合（历史知名）
- 域名: nicotv.me（历史）| nicotv.org / nicotv.biz（均已过期记录）
- 性质: 老牌中文动漫站
- 来源: 域名过期记录（nicotv.org 2024-08-22 过期、nicotv.biz 2024-11-27 过期，搜索侧记录）+ 本机实测
- 后续更新入口: 无
- 快测: nicotv.me 000（r.jina.ai 侧为 ERR_CONNECTION_REFUSED，域名拒连）
- 大陆可达性: —（站点不可达）
- 备注: **判定已失效**；"妮可动漫"现多被仿站占用，勿按老域收录

#### zzzfun
- 类别: 中文向聚合（历史知名）
- 域名: zzzfun.one（2023 起第三方客户端所连域）
- 性质: 中文番剧站（曾有 TV/移动端）
- 来源: [ZzzFunAnimePlugin](https://github.com/feiyeyuanye/ZzzFunAnimePlugin)（README 注明站点 zzzfun.one）
- 后续更新入口: 无
- 快测: zzzfun.one 200 但内容为 **parklogic 停放页**（"Redirecting..." → router.parklogic.com）→ 已死
- 大陆可达性: —（已死）
- 备注: **判定已失效**（域名停放）

---

#### 三、意/西语聚合（扩展源权威、更新勤）

#### AnimeSaturn（意）
- 类别: 意语聚合
- 域名: animesaturn.net | animesaturn.cx | animemars.org | anisaturn.com
- 性质: 意大利最大动漫站，现役 + 一次品牌分裂（anisaturn.com 系列改名 AnimeMars）
- 来源: [Kohi-den src/it/animesaturn](https://github.com/Kohi-den/extensions-source/tree/main/src/it/animesaturn)（baseUrl `animesaturn.cx`、`anisaturn.com`）；站点实测
- 后续更新入口: Kohi-den `src/it/animesaturn`
- 快测: animesaturn.cx 200（301→www.animesaturn.net，真站 548KB）| anisaturn.com 200（301→www.animemars.org，真站 147KB）
- 大陆可达性: 需代理（CF 盾）
- 备注: 源码里还有 anisaturn.com，但该域现已整体跳转 animemars.org（新品牌），规则两套都收

#### AnimeUnity（意）
- 类别: 意语聚合
- 域名: animeunity.so | animeunity.to（跳 .so）
- 性质: 意语 Sub/ITA
- 来源: [Kohi-den src/it/animeunity](https://github.com/Kohi-den/extensions-source/tree/main/src/it/animeunity)（baseUrl https://www.animeunity.so）
- 后续更新入口: Kohi-den `src/it/animeunity`
- 快测: www.animeunity.so 403（CF 盾 17B，存活）| animeunity.to 403→.so
- 大陆可达性: 需代理
- 备注: 任务书里的 animeunity.to 是旧域，现统一 .so

#### AnimeWorld（意）
- 类别: 意语聚合
- 域名: animeworld.ac
- 性质: 意语最大之一（下载+在线）
- 来源: [Kohi-den src/it/animeworld](https://github.com/Kohi-den/extensions-source/tree/main/src/it/animeworld)（baseUrl https://www.animeworld.ac）
- 后续更新入口: Kohi-den `src/it/animeworld`
- 快测: www.animeworld.ac 200（真站 714KB）
- 大陆可达性: 需代理
- 备注: 无

#### AnimeFLV（西/拉美）
- 类别: 西语聚合
- 域名: animeflv.net | www3.animeflv.net
- 性质: 拉美最大西语动漫站
- 来源: [Kohi-den src/es/animeflv](https://github.com/Kohi-den/extensions-source/tree/main/src/es/animeflv)（baseUrl https://www3.animeflv.net）
- 后续更新入口: Kohi-den `src/es/animeflv`
- 快测: animeflv.net / www3.animeflv.net **本机 000 超时**（含 r.jina.ai 亦空响应）→ 站点对数据中心/代理 IP 拦截强
- 大陆可达性: 存疑（本机不可达；站点长期用地域防火墙，国内通常也需代理）
- 备注: 域名本身未变（www3 前缀已沿用多年），只是访问门槛高

#### 其他西语（AnimeAV1 / MonosChinos / JKanime / Latanime / TVAnime / Anime-JL / YTAnime）
- 类别: 西语聚合
- 域名: animeav1.com | monoschinos2.net（vww./wwv.）| jkanime.net | latanime.org | tvanime.tv（原 animefenix2.tv）| anime-jl.net | ytanime.tv | animeid.tv（异常）
- 性质: 拉美/西语各国主力站
- 来源: [Kohi-den src/es/*](https://github.com/Kohi-den/extensions-source/tree/main/src/es)（逐个 baseUrl：animeav1.com、wwv.monoschinos2.net、jkanime.net、latanime.org、animefenix2.tv、anime-jl.net、ytanime.tv、animeid.tv）
- 后续更新入口: Kohi-den `src/es/*`
- 快测: animeav1.com 200 | monoschinos2.net 200（跳 vww.monoschinos2.net）| jkanime.net 403（CF）| latanime.org 200 | animefenix2.tv → **tvanime.tv 200（已改名 TVAnime）** | anime-jl.net 200 | ytanime.tv 403（CF）| animeid.tv **跳 to tiktok.com 直播间 → 域名已被占用/劫持**
- 大陆可达性: 需代理（清一色 CF/西语区）
- 备注: AnimeFenix 改名 TVAnime 是本轮新变化；animeid.tv 已不可信

---

### 四、已确认失效（附证据，勿再收规则）

| 站点 | 旧域 | 证据 |
|---|---|---|
| HiAnime / AniWatch / Zoro（Zoro→Aniwatch→HiAnime 主线） | hianime.to / aniwatch.to / zoro.to | 本机实测：hianime.to 000、zoro.to 000、aniwatch.to **404**；[EverythingMoe 墓地](https://everythingmoe.com/graveyard)列 HiAnime/AniWatch（含 aniwatchtv.to）；社区 2026-03 停运公告、2026-07 越南逮捕运营者报道（搜索侧）；FMHY 已把该品牌条目换成 aniwaves.ru/hianimes.ru |
| AniWave（9anime 后继） | aniwave.to / aniwave.live / ww38.aniwave.to | aniwave.to 302→ww38.aniwave.to（本机 000 死）；aniwave.live 302→ww38.aniwave.live（死）；[EverythingMoe 墓地](https://everythingmoe.com/graveyard)第 1 位 AniWave |
| AnimeKai | animekai.to / anikai.to / animekai.fi / .la | 本机 curl 全部 000；r.jina.ai 报 **Could not resolve hostname（DNS 已消失）**；[EverythingMoe /s/animekai](https://everythingmoe.com/s/animekai)「AnimeKai is moved to Graveyard」；（Kohi-den 源码仍在列这些域，属滞后） |
| Gogoanime 家族 | gogoanime.vc / gogoanime3.co / anitaku.to / anitaku.pe / anitaku.bz / gogocdn.net / gogo-load.com | gogoanime.vc 与 gogoanime3.co 经 r.jina.ai 渲染后为 **"Directory Index" 广告停放页**（本机 429）→ 已非流媒体站；anitaku.to 000、anitaku.pe 为停放页（"Do Not Sell or Share..."）、anitaku.bz "Coming Soon" 停放；gogocdn.net 302→ww38.gogocdn.net（000）；[EverythingMoe 墓地](https://everythingmoe.com/graveyard)第 4 位 Gogoanime（data-link anitaku.bz）；Sadwhy 源码内仍为 anitaku.to + ajax.gogocdn.net（历史） |
| KissAnime | kissanime.co / .sx / kissanime.com.ru / kissanime.org.ru | 本机 kissanime.co/.sx 均 000；[EverythingMoe 墓地](https://everythingmoe.com/graveyard)第 9 位 KissAnime；（Kohi-den 仍有 kissanime 扩展，属给"假活"镜像留口） |
| Anime4Up（阿拉伯语） | anime4up.tv 等 | www1.anime4up.tv → **parklogic 停放页**（本机实测 + r.jina.ai 分离验证） |
| AnimeDao | animedao.to | → parklogic 停放页（本机实测） |
| AnimeKisa | animekisa.tv | 本机 000；[EverythingMoe 墓地](https://everythingmoe.com/graveyard)第 11 位 AnimeKisa |
| AnimeFox | animefox.io | 本机 000（超时/拒连） |
| mikanime | mikanime.tv | 202/301 → **mikanani.me（蜜柑计划 BT 站，另一路负责）** → 原"mikanime"在线站已不存在 |
| Kaido（AniWatch 系） | kaido.to | 本机 000 + r.jina.ai Timeout；2026-09 大量用户报 500/502/CF 登录循环（updownradar 汇总）→ 判失效/不可达 |
| AniNeko | anineko.to | 返回 PHP 数据库错误页（后端 nekovault.online 宕机）；[EverythingMoe 墓地](https://everythingmoe.com/graveyard) |
| 妮可动漫 / zzzfun / 风车旧域（dm530.com）/ 樱花旧发布页（dm519.fans、yhdmp.net） | nicotv.me 等 | 见上文各节实测（拒连 / parklogic 停放 / "domain for sale"） |
| 其他墓地批量（供参考，未逐一实测） | AniMixPlay、4Anime、YugenAnime、Simplyaweeb、AnimeOwl、SlothAnime、Anify、Rive Anime、1Anime、BestDubbedAnime、Kawaiifu、Anikuro 等 | [EverythingMoe Graveyard · Dead Anime Streaming (158)](https://everythingmoe.com/graveyard) |

> 判据说明：parklogic 停放页与 "Directory Index" 广告页是 2026 年域名到期/被抢注的典型信号（本机 200 但无站点内容），本次据此判死 gogoanime.vc/3.co、anime4up、animedao、zzzfun.one、dm519.fans、yhdmp.net、dm530.com。

---

### 五、给分流规则的落地建议（简述）

1. **务必整组收录的域名**：aniyomi/keiyoushi 源内 baseUrl + 官方域名清单页（anikoto.site / animesuge.bid）列出的全部域 —— 它们会被扩展自动换用。
2. **CDN/播放域别漏**：pahe.win、kwik.cx、megaplay.buzz、flixcloud.cc、og.bakayaro.live、vidcloud.se、anicdn.com、mub.acgdm001.com、sub.wyzie.ru、enc-dec.app。
3. **中文向站点高变动**：AGE 官方自述 2~3 个月换域；风车以 fcbbcc.com 为准；樱花只认 qlyyz.xyz；定期（建议双周）按本文件「后续更新入口」重跑一轮。
4. **死后品牌勿留**：hianime/zoro/aniwatch/aniwave.to/anikai/gogo 全系已死，规则里即使有人提交也应剔除（避免误判"翻墙失败"）。
5. **判定口径**：本文"需代理"= CF 盾/被墙可能性高；"存疑"= 本机经代理都无法确认或站点自述被区域封禁。以本机实测为准，超时/403 均不等于死站。

## 4. BT / 字幕组 / 追番社区

> 生成日期：**2026-10-06** ｜ 用途：为 Clash / mihomo（OpenClash）分流规则提供「动漫 BT、字幕组、追番社区」类域名参考
> 全部域名来自当日联网调研（每条附来源 URL）并做了当日实测。

### 阅读说明

覆盖范围：

1. **华语 BT / 资源索引站**（dmhy、蜜柑、萌番组、ACG.RIP、ACGX、U2 等）
2. **字幕组 / 压制组**（只收有独立发布站或主页的）
3. **国际通用 BT 站**（Nyaa 系、TokyoTosho、AniDex）
4. **追番 / 评分 / 情报社区**（Bangumi、AniList、MAL、ANN、弹弹play、trace.moe）
5. **已确认失效 / 陷阱域名**（含证据，**不要**加入规则）

### ⚠️ 快测方法与本机网络的重要说明

- 快测命令：`curl -s -o /dev/null -w '%{http_code}' --connect-timeout 6 -m 10 -A 'Mozilla/5.0' https://域名/`
- **本机（Windows + 路由器 OpenClash）实测出口为日本（AWS Tokyo，实测公网 IP 35.75.235.87）**，**不是大陆出口**。因此：
  - 快测结果 = **海外（日本）视角的快照**，只能证明「站点存活」，**不能证明大陆可达**。
  - 「大陆可达性」一栏依据的是**官方公告、社区实测贴、GFW 封锁记录**等外部证据，不是本机实测。
- 超时 / 000 **≠** 站点已死（可能是本机代理链路抖动、反爬、CF 挑战）。已在条目中区分。

### 可靠性标记

| 标记 | 含义 |
|---|---|
| ✅ | 实测有正常响应（200/30x；403 的 CF 挑战页、404 的 CDN 根路径等已注明属正常） |
| 🟡 | 实测异常（超时 / 连接失败 / 522），多为反爬或链路问题，**不代表不可用** |
| ❌ | 已确认失效 / 停放 / 劫持 / 同音陷阱域名，**不要加入规则** |

### 分流建议

- 优先 `DOMAIN-SUFFIX`（如 `DOMAIN-SUFFIX,dmhy.org`），天然覆盖 `share./bbs./u2.` 等子域。
- **同一站点的「国内入口」与「海外入口」要分开判定**：蜜柑是最典型例子——`mikanime.tv` 是国内专用、`mikanani.me` 已被墙，两条规则可指向不同策略组。
- **图片 CDN 必须单独收**（`lain.bgm.tv`、`s4.anilist.co`、`cdn.myanimelist.net`），漏了会出现「网页能开、封面全挂」。
- **镜像 / 停放域名是主要坑源**：本清单里 `tsdm39.net`、`tsdm.live`、`lightnovel.us` 等已实测为域名停放页，`loli.house` 是同音陷阱（详见 §5）。加规则前建议按 §5 复核一遍。

### 可靠性声明

- 本清单只做域名收集与可达性判断，不构成对站点内容的背书。
- 域名与封锁状态高变动，请以各站**官方公告 / Telegram 频道**为准；建议每季复核一次。

---

### 1. 华语 BT / 资源索引站

- 调研日期: 2026-10-06
- 快测方法: 见上（本机出口 = 日本）

---

#### 動漫花園資源網（DMHY / 花园）
- 类别: BT索引
- 域名: dmhy.org | www.dmhy.org | share.dmhy.org | bbs.dmhy.org | dmhy.anoneko.com | dongmanhuayuan.myheartsite.com | dmhy.xml
- 性质: 华语最大动漫 BT/ED 资源索引站，分动画/漫画/音乐/日剧/RAW/游戏/特摄等板，提供 RSS（`dmhy.xml`）
- 来源: [動漫花園資源網首页](https://dmhy.org/)（实测首页 HTML，站内引用 `bbs.dmhy.org`、`share.dmhy.org`、`dmhy.xml`）；官方 TG [t.me/dmhy_org](https://t.me/dmhy_org)（首页外链）
- 后续更新入口: <https://dmhy.org/> ；TG <https://t.me/dmhy_org>
- 快测: dmhy.org 200｜www.dmhy.org 200｜share.dmhy.org 200（与主站**同内容**）｜bbs.dmhy.org 200（正文 `Forbidden, Please Refresh`，反爬）｜dmhy.anoneko.com 200（同内容镜像）
- 大陆可达性: **需代理**（社区实测大陆存在 DNS 污染 + Cloudflare IP 被运营商无差别阻断，主流绕行方案是改 hosts / 切 IPv6 / 走镜像 / 挂代理）
- 备注: `share.dmhy.org` 现与主站同源（历史上曾是独立 BT 列表页），规则可一并收；`dmhy.gate.flag.moe` 是第三方 DMHY 代理站，目前已挂公告「因大量爬虫流量暂时关闭」，**不建议收**。

#### 蜜柑计划（Mikan Project）
- 类别: BT索引 / 追番订阅
- 域名: mikanime.tv | mikanani.me | mikanani.kas.pub
- 性质: 按番组/字幕组聚合的动漫 BT 索引，主打 RSS 自动追番（Ani-RSS 等工具的默认源）
- 来源: [蜜柑计划首页](https://mikanani.me/)（首页公告原文：「新域名 >>mikanime.tv<< **仅限国内使用**」）；[ani-rss README](https://raw.githubusercontent.com/imlonghao/ani-rss/master/README.md)（原文标注：**已被墙** `https://mikanani.me/`｜**未被墙** `https://mikanime.tv/`）
- 后续更新入口: 首页公告 + 微博（首页 Contact 链接指向 mikanani.me/Home/Contact）
- 快测: mikanani.me 200｜mikanime.tv 200（本机为日本出口，访问 `mikanime.tv/` 会被 **302 跳回 mikanani.me** —— 这正是「国内专用」的 GEO 分流表现）｜mikanani.kas.pub 200（镜像，同页）
- 大陆可达性: **国内入口 `mikanime.tv` 直连；`mikanani.me` 需代理**（依据即 ani-rss README 的「已被墙/未被墙」标注 + 蜜柑自家公告）
- 备注: **两个域名都要收**，且建议分别指向不同策略（`mikanime.tv`→国内直连组，`mikanani.me`→代理组）。`mikanani.tv`（少一个 e）是**错误域名**，社区已有人纠错，勿用。

#### 萌番组（Moe / bangumi.moe）
- 类别: BT索引
- 域名: bangumi.moe | www.bangumi.moe | static.bangumi.moe
- 性质: 中文动漫 BT 索引 + 发布/团队系统，提供 RSS（`/rss/latest`）
- 来源: [bangumi.moe 首页](https://bangumi.moe/)（实测，页脚 `© 2015 Bangumi.moe`，静态资源走 `static.bangumi.moe`）；源码 [GitHub: BangumiMoe](https://github.com/BangumiMoe)（`rin-pr`/`rin-webui`/`wiki` 等，仓库说明含 "Front-end for Bangumi.moe"）
- 后续更新入口: [GitHub BangumiMoe](https://github.com/BangumiMoe)
- 快测: bangumi.moe 200｜www.bangumi.moe 200｜static.bangumi.moe（静态资源域）｜api.bangumi.moe 000（无解析）
- 大陆可达性: **存疑**（有大陆联通用户报告可直连，也有用户反馈 DNS 污染导致连不上、可用阿里 DoH/DoT 解决；另外该站曾出现连续数天的整体宕机）
- 备注: ⚠️ **与 `bgm.tv`「Bangumi 番组计划」是完全无关的两个站**，勿混（`bangumi.moe` 是种子站，`bgm.tv` 是评分社区）。浏览免注册，发布/团队功能需账号。

#### ACG.RIP
- 类别: BT索引
- 域名: acg.rip | www.acg.rip
- 性质: 中文动漫/日剧/综艺/音乐 BT 索引（页面自述 Copyright 2014-2023），含「本站 Tracker」入口
- 来源: [ACG.RIP 首页](https://acg.rip/)（实测；页面公告「Tracker 不再有效。」，联系 `i(at)i.wtf`，发布申请需「邮箱+密码+发布组名」）
- 后续更新入口: 无独立公告频道；首页「本站 Tracker」指向 `https://f86ed7c41c5f.pages.dev`（Cloudflare Pages）
- 快测: acg.rip 200｜www.acg.rip 200
- 大陆可达性: **存疑**（社区反馈大陆访问「不是特别稳定，有些时候可能会登不上，要等它自己好」，成因多为 DNS 污染 / SNI 阻断；也有用户报告联通可直连）
- 备注: 社区提到该站**历史上换过域名**，若长期打不开需留意新域。无需注册即可浏览。

#### 末日動漫資源庫（ACGX / AcgnX）
- 类别: BT索引 / 资源库
- 域名: acgnx.se | www.acgnx.se | share.acgnx.se | share.acgnx.cc | share.acgnx.net
- 性质: 末日动漫资源库，国际主站 + 亚洲站 + 专供大陆的镜像站
- 来源: [AcgnX 主站](https://www.acgnx.se/)（CF 403 实测存活）；官方公告渠道 TG [@acgnxtorrent](https://t.me/acgnxtorrent)（官方公告频道）/ [@acgnxasia](https://t.me/acgnxasia)（中文交流群）（社区整理）
- 后续更新入口: TG <https://t.me/acgnxtorrent> ；<https://t.me/acgnxasia>
- 快测: acgnx.se 301→www.acgnx.se｜www.acgnx.se 403（CF `Just a moment...`，存活）｜share.acgnx.se 403（CF 挑战）｜share.acgnx.cc 302→share.acgnx.se｜share.acgnx.net 301→share.acgnx.cc
- 大陆可达性: **需代理**（官方公告明确：本站域名在大陆已被屏蔽，镜像站也曾被屏蔽，**推荐所有大陆用户使用代理或 VPN 访问**）
- 备注: `.cc` / `.net` 镜像「仅供大陆地区访问」，**非大陆 IP 访问会被强制跳回源站**（本机日本出口实测即被 302 跳回 `share.acgnx.se`，与公告一致）。镜像站限制评论/注册/发布功能，且要求浏览器支持 TLS 1.3。`acgnx.net` / `acgnx.eu` / `acgnx.xyz` / `acgnx.club` / `acgnx.top` / `acgnx.pro` 实测**均无解析**（❌ 见 §5）。

#### Anime 字幕论坛（ACG.RIP 论坛）
- 类别: 社区（字幕/压制交流）
- 域名: bbs.acgrip.com
- 性质: 中文字幕组、压制组、做种/资源讨论最集中的论坛（本清单多个可达性结论的证据源）
- 来源: [bbs.acgrip.com](https://bbs.acgrip.com/)（实测 CF 403 挑战页，站点存活）；讨论帖例：[种子站被墙后如何做种](https://bbs.acgrip.com/forum.php?mod=viewthread&tid=10399)
- 后续更新入口: 无
- 快测: 403（Cloudflare `Attention Required!`，**存活**；浏览器可过）
- 大陆可达性: **存疑**（CF 站点，未见定向封禁公告；论坛本身即大陆用户讨论绕过封锁的主要场所）
- 备注: `acgrip.com` 裸域无解析（❌）。与 §1 的 `acg.rip`（种子站）同一批人运营，但域名独立。

#### U2（動漫花園私人 PT）
- 类别: BT索引（**私人 PT**）
- 域名: u2.dmhy.org
- 性质: 動漫花園旗下私人 PT 站（U2），以动漫 BD/原盘/高清资源为主
- 来源: [u2.dmhy.org](https://u2.dmhy.org/)（实测 `<title>Access Point :: U2</title>`，页面含 `invite` 相关字样）
- 后续更新入口: 无（私人站，靠站内/TG 邀请）
- 快测: 200（未登录时显示 `Access Point :: U2` 引导页）｜302→`/portal.php`（根路径）｜IPv4 实测 104.25.26.31/104.25.27.31（社区 hosts 记录）
- 大陆可达性: **需代理**（同属 `dmhy.org` 域族，社区实测大陆存在 DNS 污染 + CF IP 阻断，hosts 需逐个子域单独写）
- 备注: **私人站，需邀请码**，未登录只能看到 Access Point 页；建议整域 `DOMAIN-SUFFIX,dmhy.org` 一条覆盖 dmhy + share + bbs + u2。

#### 天使动漫（TSDM）
- 类别: 社区 / 网盘资源
- 域名: tsdm39.com | www.tsdm39.com | img.tsdm39.com | img.tsdm39.net | tu.ts-dm.net
- 性质: 天使动漫论坛（Discuz），含 TSDM 字幕组、动漫音乐/网盘资源区
- 来源: [www.tsdm39.com/forum.php](https://www.tsdm39.com/forum.php)（实测页面标题：「天使动漫论坛 - 梦开始的地方 一个能轻松聊天结识同好的温馨小论坛 Angel Beats|TSDM字幕组|天使动漫网 - Powered by Discuz!」）；持续快照 [Wayback 2026-10-04](http://web.archive.org/web/20261004204035/https://www.tsdm39.com/)
- 后续更新入口: 官方微博 <https://weibo.com/acgtsdm>（社区整理）
- 快测: tsdm39.com 301→www.tsdm39.com｜www.tsdm39.com 403（Cloudflare 挑战，**浏览器可正常过**，实测已见真实论坛页）｜img.tsdm39.com 403（**防盗链，存活**）｜img.tsdm39.net 200｜tu.ts-dm.net 200
- 大陆可达性: **存疑**（站点本身对大陆开放且是中文论坛，但套 CF 后部分大陆网络需配合 DoH 才能过挑战；社区也有 DNS 污染报告）
- 备注: ⚠️ **三个旧域名已死，务必别收**：`tsdm39.net` 与 `tsdm.live` 实测均已被 parklogic 域名停放接管（见 §5）；`tsdm.love` 已停止使用；`tsdm39.org` 是**另一家无关机构**（页面出现 `jwc./lib./xsc.` 等教务子域与复旦/北大链接），**不是天使动漫**。

#### 轻之国度（LK）
- 类别: 社区 / 轻小说分享
- 域名: lightnovel.fun | www.lightnovel.fun | api.lightnovel.fun | lightnovel.cn | www.lightnovel.cn
- 性质: 轻之国度 NACG 社群（轻小说/动漫资源分享，网页 + App）
- 来源: [lightnovel.fun 首页](https://www.lightnovel.fun/)（实测 `<title>轻之国度-专注分享的NACG社群</title>`）；[lightnovel.cn](https://www.lightnovel.cn/)（同标题，当前可用域）
- 后续更新入口: 官网/贴吧；未见官方 TG
- 快测: lightnovel.fun 200｜www.lightnovel.fun 200｜lightnovel.cn 200｜www.lightnovel.cn 200；页面内引用 `api.lightnovel.fun`
- 大陆可达性: **存疑**（站点走 Cloudflare，社区历史上反馈部分移动宽带需改 hosts；本次未找到 2026 年的定向封锁证据）
- 备注: ⚠️ **`lknovel.cn` / `www.lknovel.cn` 实测已被劫持**，打开是成人影视站（“小狐阁影院”），**绝对不是轻之国度，不要收**；`lightnovel.us` 已变为域停放页（见 §5）。`api.lightnovel.fun` 是 App 用接口域，建议一并收。

#### 绯月（ScarletMoon / KF）
- 类别: 社区
- 域名: kfmax.com | www.kfmax.com | bbs.kfmax.com
- 性质: 老牌中文 ACG 论坛（动漫/游戏/音乐/绘画），站点自述「绯月是一个以动漫、游戏、音乐、绘画等为主题的论坛」
- 来源: [kfmax.com 首页](https://kfmax.com/)（实测 HTML `<title>绯月ScarletMoon</title>`，GBK 编码，`keywords=苍雪`）
- 后续更新入口: 无
- 快测: kfmax.com 302（存活）｜www.kfmax.com 200｜bbs.kfmax.com 200；解析 IP 173.230.157.235（美国 Linode）
- 大陆可达性: **存疑**（站点本身中文老站，但解析在境外 Linode；本次未找到 2026 年的定向封锁或直连实测证据）
- 备注: 论坛区在 `bbs.kfmax.com`，建议整域 `DOMAIN-SUFFIX,kfmax.com` 一条覆盖。

#### 漫游（POPGO）
- 类别: 社区 / 字幕组
- 域名: popgo.org | www.popgo.org | bbs.popgo.org
- 性质: 漫游（POPGO）老牌字幕组/论坛，现为「慢慢游论坛」导航入口页
- 来源: [popgo.org](https://popgo.org/)（实测落地页：标题「漫游」，正文「请选择目的地:」并链接 `/bbs/` 下的「慢慢游论坛」）
- 后续更新入口: 无
- 快测: popgo.org 200（34 字节级落地页）｜www.popgo.org 200｜bbs.popgo.org 200（`<title>漫游</title>`）
- 大陆可达性: **存疑**（本次未找到定向封锁证据；站点为中文老站但已大幅萎缩）
- 备注: `popgo.net` 实测**无解析**（❌ 旧域已死，见 §5）。漫游字幕组基本停更，仅作为社区入口保留。

#### 澄空学园（SumiSora）
- 类别: 社区 / 字幕组
- 域名: sumisora.net | www.sumisora.net | bbs.sumisora.net
- 性质: 澄空学园字幕组 / 论坛（`bbs.sumisora.net` 为论坛）
- 来源: [sumisora.net](https://sumisora.net/)（实测 `<title>欢迎来到澄空学园 - Welcome to SumiSora</title>`，站内链接指向 `bbs.sumisora.net`）
- 后续更新入口: 无
- 快测: sumisora.net 200｜www.sumisora.net 200｜bbs.sumisora.net 200
- 大陆可达性: **存疑**（本次未找到 2026 年定向封锁或直连实测证据）
- 备注: `sumisora.org` 实测**无解析**（❌ 旧域已死）；`2dgal.com`（原澄空/2DJ 相关）亦无解析。

---

#### 2. 字幕组 / 压制组（有独立站点）

> 说明：大陆字幕组**绝大多数没有独立官网**（靠 mikan / dmhy / fitacg 发布 + GitHub 存字幕 + TG 通知），本清单只收录**确有独立域名站点**的；无独立站的见 §3。

#### VCB-Studio
- 类别: 压制组
- 域名: vcb-s.com | www.vcb-s.com
- 性质: 业界最组织化、流水线化的 BD 压制组（HEVC 10bit + FLAC），官网含编年史/技术教程/招新
- 来源: [vcb-s.com](https://vcb-s.com/)（CF 403 实测存活）；社区佐证 [Anime字幕论坛讨论](https://bbs.acgrip.com/)（VCB 官网留言板回应过「我们是压制组，不是字幕组」）
- 后续更新入口: <https://vcb-s.com/>（官网本身即公告渠道）
- 快测: vcb-s.com 403｜www.vcb-s.com 403（Cloudflare `Just a moment...`，**存活**；Wayback 2026 年快照同样只记录到 CF 403，属反爬特性）
- 大陆可达性: **存疑**（CF 站点，本次未找到定向封禁证据；也未见「大陆专用镜像」公告）
- 备注: 纯官网，无注册/邀请需求。VCB 主做 BD 源，Web 源领域与 LoliHouse 互补。

#### TUcaptions
- 类别: 字幕组
- 域名: tucaptions.org
- 性质: 繁体中文（台湾）字幕组论坛，仍在运作
- 来源: [tucaptions.org](https://tucaptions.org/)（实测 `<title>TUcaptions - Powered by Discuz!</title>`）
- 后续更新入口: 站内论坛
- 快测: 200（Discuz 论坛）
- 大陆可达性: **存疑**（本次未找到定向封锁证据）
- 备注: 本次调研中少见的「仍有独立 Discuz 站点」的字幕组；发布同样会经 dmhy/mikan。

---

### 3. 字幕组（无独立站点 — 仅登记社群入口，域名不收录）

> 这些组**没有独立域名**，规则上无需新增条目；此处登记是为了说明「为什么搜不到官网」，以及给出后续更新入口。

| 字幕组 | 性质 | 发布渠道 | 官方/主入口 | 域名 |
|---|---|---|---|---|
| 桜都字幕组（Sakurato） | 字幕组，2026 年仍活跃 | mikan / dmhy | TG [t.me/sakurato](https://t.me/sakurato) | ❌ `sakurato.net`/`.com`/`.moe`/`saku.rip` 均**无解析**，无官网 |
| 喵萌奶茶屋（Nekomoe kissaten） | 字幕组，常与 LoliHouse 合作 | mikan / fitacg / assrt / subhd | GitHub [Nekomoekissaten-SUB](https://github.com/Nekomoekissaten-SUB/Nekomoekissaten-Subs) | 无独立域名 |
| 北宇治字幕组（KitaujiSub） | 字幕组 | mikan / dmhy / B站 | GitHub [Kitauji-Sub](https://github.com/Kitauji-Sub) ，TG [t.me/KitaUji](https://t.me/KitaUji) | 无独立域名；注意 `kitauji.net` 是无关的 "KITAUJI-NETWORKS" 占位页 |
| LoliHouse（萝莉工房） | 压制组（Web 1080p 新番） | mikan（发布组页）/ dmhy（team 657）/ fitacg | 无官网（曾用 `lolihouse.cafe`，**已关闭且无解析**）；联系邮箱 `LoliHouse@126.com` | ❌ **`loli.house` 不是 LoliHouse**，见 §5 |
| 极影字幕社（JYSub） | 字幕组（已停更） | — | — | ❌ `jysub.net`/`.com`/`.org`/`sub.jysub.net` 均**无解析** |
| 华盟字幕社 | 字幕组（已停更） | — | — | ❌ 未找到任何现存域名（`huameng.net`/`.org` 等无解析） |
| 悠哈C9 / 千夏 / SweetSub / 茉语星梦 等 | 字幕组 | mikan / dmhy / acgrip | GitHub / 微博 / QQ 群 | 均无独立域名（`sweet-sub.com`、`moonsub.org`、`uha-c9.com` 等实测无解析） |

---

#### 4. 国际 / 通用 BT 站

#### Nyaa
- 类别: BT索引（国际通用，动漫为主）
- 域名: nyaa.si | sukebei.nyaa.si（**成人分站**，务必单独区分） | nyaa.tracker.wf | sukebei.tracker.wf | nyaa.xml | sukebei.xml
- 性质: 全球最大动漫 BT 索引（前身 nyaa.eu/nyaa.se），成人内容拆到 Sukebei 分站
- 来源: [nyaa.si](https://nyaa.si/)（实测 `<title>Browse :: Nyaa</title>`；页面链接成人姊妹站 `//sukebei.nyaa.si` 标为 “Fap”，Twitter [@NyaaV2](https://twitter.com/NyaaV2)，tracker `nyaa.tracker.wf`）；[sukebei.nyaa.si](https://sukebei.nyaa.si/)（实测 `<title>Browse :: Sukebei</title>`，分类含 "Art -"、"Real Life"）
- 后续更新入口: Twitter [@NyaaV2](https://twitter.com/NyaaV2)
- 快测: nyaa.si 200｜nyaa.si/?q=test 200｜sukebei.nyaa.si 200｜sukebei.nyaa.si/?q=test 200
- 大陆可达性: **需代理**（境外站，GFW 长期阻断；社区一致以「挂梯子 + 代理 RSS/Tracker」为常规方案）
- 备注: **`sukebei.nyaa.si` 是成人分站，分流时建议与主站分开策略组**。tracker 为 `nyaa.tracker.wf` / `sukebei.tracker.wf`：两者 DoH 均可正常解析（`195.16.73.95` / `195.16.73.66`），但 HTTP GET 返回 000 —— 这是 **BT announce 专用端点的正常表现**（只回 bencode，不服务网页），**不是死域**，做种场景建议收录。⚠️ `nyaa.eu`（自称 "Nyaa.se Torrents Proxy"）与 `nyaa.net`（自称 open torrent index，含 `cn.nyaa.net`）**均非官方**，见 §5。

#### Tokyo Toshokan
- 类别: BT索引
- 域名: tokyotosho.info
- 性质: 老牌英文动漫/亚洲媒体 BT 索引（IRC `#tokyotosho @ irc.rizon.net`）
- 来源: [tokyotosho.info](https://tokyotosho.info/)（实测 `<title>Tokyo Toshokan :: #tokyotosho @ irc.rizon.net :: Torrent Listing</title>`）
- 后续更新入口: 站点 IRC `#tokyotosho @ irc.rizon.net`
- 快测: 首页 200（87KB 真实列表）｜`/search.php?terms=test` 403（反爬，存活）
- 大陆可达性: **需代理**（境外站；本次未找到直连证据）
- 备注: 活跃度已远不如 Nyaa/dmhy，作为兜底源保留。

#### AniDex
- 类别: BT索引
- 域名: anidex.info
- 性质: 面向动漫/东方/音乐的 BT 索引站
- 来源: [anidex.info](https://anidex.info/)（实测 403 `DDoS-Guard` 拦截页，站点存活）
- 后续更新入口: 无
- 快测: anidex.info 403（DDoS-Guard 挑战）｜`/?q=test` 502（DDoS-Guard，存活）｜`api.anidex.info` 000（无解析，❌ 勿收）
- 大陆可达性: **需代理**（境外站 + DDoS-Guard）
- 备注: DDoS-Guard 会拦非浏览器 UA，「403/502」属正常防护表现，不代表死站。

---

#### 5. 追番 / 评分 / 情报社区

#### Bangumi 番组计划
- 类别: 社区 / 评分 / 番组进度
- 域名: bgm.tv | bangumi.tv | chii.in | fast.bgm.tv | doujin.bgm.tv | api.bgm.tv | lain.bgm.tv（图片 CDN）
- 性质: 中文最大 ACG 评分/收藏/进度社区（网页 + App「Bangumi」），提供开放 API
- 来源: [bgm.tv](https://bgm.tv/)（实测 `<title>Bangumi 番组计划</title>`，站内链接含 `doujin.bgm.tv`、`lain.bgm.tv` 图片、`/dev` 开发者入口）；[bangumi.tv](https://bangumi.tv/)（同站，实测标题与资源域一致）；API 实测 `api.bgm.tv/v0/subjects/8` 返回 200 JSON；封面 CDN 实测 `lain.bgm.tv/r/400/pic/cover/...` 返回 200 image/jpeg
- 后续更新入口: <https://bgm.tv/dev>（开发者平台）
- 快测: bgm.tv 200｜bangumi.tv 200｜chii.in 200｜fast.bgm.tv 200｜api.bgm.tv 200｜lain.bgm.tv 200（image/jpeg，根路径 404 属 CDN 正常）
- 大陆可达性: **需代理**（自 **2026-05-27** 起被 GFW 封锁，`bgm.tv`/`bangumi.tv`/`chii.in` 三个主域在大陆均无法直连；`api.bgm.tv` 与 `lain.bgm.tv` 同为海外 Cloudflare，国内直连超时）
- 备注: ⚠️ **`lain.bgm.tv` 漏收会「网页能开、封面全挂」**，必须单独收；`fast.bgm.tv` 会跳回 `bgm.tv`。所有 `*.bgm.tv` / `*.bangumi.tv` 建议整域收进代理组。注意与种子站 `bangumi.moe` 无关。

#### AniList
- 类别: 社区 / 评分 / 进度 + API
- 域名: anilist.co | s4.anilist.co | graphql.anilist.co | img.anili.st
- 性质: 英文为主（含中文）动画/漫画评分与进度追踪站，GraphQL API 被大量第三方客户端（AniHyou 等）使用
- 来源: [anilist.co](https://anilist.co/)（实测 200，`<title>AniList</title>`）；GraphQL 接口 `graphql.anilist.co` 实测可达（根路径 404 为 GraphQL 正常特性）；封面 CDN `s4.anilist.co` 实测取图返回 200 `image/png`
- 后续更新入口: 站内 API 文档
- 快测: anilist.co 200｜s4.anilist.co 200｜graphql.anilist.co 404（正常）｜img.anili.st 404（正常）｜api.anilist.co 000（无解析，正式接口是 `graphql.anilist.co`）
- 大陆可达性: **需代理**（海外站点，国内访问不稳定；国内教程普遍以「加速器/代理」为解法，直连常因国际路由与拦截而失败）
- 备注: **`s4.anilist.co` 是封面/头像 CDN，必须单独收**（实测底图为 Backblaze B2，故根路径会显示 B2 落地页，属正常）。`graphql.anilist.co` 是 App 数据接口，漏收会导致客户端「列表空白」。

#### MyAnimeList（MAL）
- 类别: 社区 / 评分 / 进度 + API
- 域名: myanimelist.net | cdn.myanimelist.net | api.myanimelist.net | api-cdn.myanimelist.net
- 性质: 全球最大英文动画/漫画数据库与进度追踪站（现属 Gaudiy Inc.）
- 来源: [myanimelist.net](https://myanimelist.net/)（实测 200，`<title>MyAnimeList.net - Anime and Manga Database and Community</title>`）
- 后续更新入口: 站内 API 文档
- 快测: myanimelist.net 200｜cdn.myanimelist.net 404（CDN 根路径，正常）｜api.myanimelist.net 404（正常）｜api-cdn.myanimelist.net 404（正常）
- 大陆可达性: **需代理**（海外站，长期不通）
- 备注: `cdn.myanimelist.net` 是图片 CDN，建议一并收；CDN 域根路径 404 属正常，勿误判为死站。

#### Anime News Network（ANN）
- 类别: 情报 / 新闻
- 域名: animenewsnetwork.com | www.animenewsnetwork.com
- 性质: 英文动漫新闻与百科（Encyclopedia）老站
- 来源: [animenewsnetwork.com](https://animenewsnetwork.com/)（实测 301→`www.animenewsnetwork.com`，目标页 200）
- 后续更新入口: 无
- 快测: animenewsnetwork.com 301｜www.animenewsnetwork.com 200
- 大陆可达性: **需代理**（海外站）
- 备注: 裸域 301 到 www，规则按 `DOMAIN-SUFFIX,animenewsnetwork.com` 一条即可覆盖。

#### 弹弹play（dandanplay）
- 类别: 社区 / 弹幕播放器
- 域名: dandanplay.com | www.dandanplay.com | dandanplay.net | api.dandanplay.net | doc.dandanplay.com | assets.anixplayer.net
- 性质: 国产本地视频弹幕播放器（自动匹配番剧弹幕），客户端高频访问其 API
- 来源: [弹弹play 官网](https://www.dandanplay.com/)（实测 `<title>弹弹play - 为本地视频加上弹幕的全功能播放器</title>`）；[dandanplay.net](https://dandanplay.net/)（实测 302→`https://www.dandanplay.com`）
- 后续更新入口: <https://doc.dandanplay.com/>（官方文档）
- 快测: dandanplay.net 302→www.dandanplay.com｜dandanplay.com / www.dandanplay.com 200｜api.dandanplay.net 401（**需鉴权，存活**）｜doc.dandanplay.com 可达
- 大陆可达性: **直连**（国产软件、国内服务，官网与文档均为国内可访问产品）
- 备注: `api.dandanplay.net` 返回 401 属正常（需 AppID/签名），**不是死站**。`assets.anixplayer.net` 是客户端资源域，建议一并收。

#### trace.moe
- 类别: 工具 / 以图搜番
- 域名: trace.moe | api.trace.moe
- 性质: 「截图搜番」动画场景检索引擎（返回剧集与精确时间点），被大量追番工具与 Bot 调用
- 来源: [trace.moe](https://trace.moe/)（实测 `<title>Anime Scene Search Engine - trace.moe</title>`，meta description "Search Anime by ScreenShot"）；接口实测 `api.trace.moe/search?...` 返回 200 JSON
- 后续更新入口: 官方 API 文档（站内）
- 快测: trace.moe 200｜api.trace.moe 200（返回 `application/json`，实测可用）
- 大陆可达性: **需代理**（海外服务；本次未找到直连证据，但作为无国内节点的工具站按需代理更稳）
- 备注: 站点同时提及 `animeoshi.com`（相关/同类项目）。**`api.trace.moe` 是核心接口域，漏收会导致「网页能开、搜图失败」**。

#### Shikimori
- 类别: 社区 / 评分
- 域名: shikimori.one
- 性质: 俄语圈动画/漫画数据库与进度追踪站（前身 shikimori.org）
- 来源: [shikimori.one](https://shikimori.one/)（实测 200，`<title>Шикимори — энциклопедия аниме и манги</title>`）
- 后续更新入口: 无
- 快测: shikimori.one 200｜shikimori.me 522（Cloudflare 超时，❌ 备用域不可靠）
- 大陆可达性: **需代理**（境外俄语站）
- 备注: 主要被 AniList/MAL 之外的俄语用户与部分第三方工具引用；优先级低于前两者。

---

### 6. 已确认失效 / 陷阱域名（❌ 不要加入规则）

> 判定证据以「域名停放页自报域名」为最硬：parklogic 停放页内嵌 base64 JSON，会明文写出 `domainApex`。以下 `domainApex=` 均指该字段解码结果。

| 域名 | 判定 | 证据 |
|---|---|---|
| `tsdm39.net` / `www.tsdm39.net` | ❌ 域名停放 | 实测返回 parklogic 停放页（`<title>Redirecting...</title>` → `router.parklogic.com`），内嵌 JSON 明示 `"domainApex":"tsdm39.net"`；Wayback 2026-05-10 快照亦为同一停放页，说明早在 5 月即已丢失 |
| `tsdm.live` / `www.tsdm.live` | ❌ 域名停放 | 同上停放页，内嵌 JSON `"domainApex":"tsdm.live"`（社区曾称其为「主域名」，实测已被停放接管） |
| `tsdm.love` | ❌ 已停止使用 | 实测 HTTP 429；社区公告原文「tsdm.love（暂停使用）」 |
| `tsdm39.org` / `www.tsdm39.org` | ⚠️ 同音陷阱 | 实测 200，但标题为泛化 SEO 页「天使动漫｜热门动漫推荐与天使动漫资讯」，且站内出现 `jwc.` / `lib.` / `xsc.` / `mail.` 等教务子域及复旦/北大外链，实为**另一家无关机构**，非天使动漫论坛 |
| `lightnovel.us` / `www.lightnovel.us` | ❌ 域名停放 | parklogic 停放页，`"domainApex":"lightnovel.us"`（旧域已死，新域为 `lightnovel.fun`） |
| `lknovel.cn` / `www.lknovel.cn` | ❌ 已被劫持 | 实测打开为成人影视站「小狐阁影院」（内容与其域名毫不相关），**绝不是轻之国度** |
| `loli.house` / `www.loli.house` | ⚠️ **同音陷阱** | 实测 403 CF，但 Wayback 快照标题为「🌸 CarrChen - 萝莉之家 🌸」（个人博客/主页），**并非压缩组 LoliHouse 官网**，勿误收 |
| `lolihouse.cafe` | ❌ 无解析 | LoliHouse 历史域名，实测无解析；社区确认「官网曾有，也没什么内容，之前一起关掉了」 |
| `jysub.net` / `jysub.com` / `jysub.org` / `sub.jysub.net` | ❌ 无解析 | 极影字幕社全部候选域实测连接失败/无解析 |
| `popgo.net` / `www.popgo.net` | ❌ 无解析 | 漫游旧域；现役为 `popgo.org` |
| `sumisora.org` / `www.sumisora.org` | ❌ 无解析 | 澄空学园旧域；现役为 `sumisora.net` |
| `2dgal.com` | ❌ 无解析 | 澄空/2DJ 相关旧域 |
| `sakurato.net` / `sakurato.com` / `sakurato.moe` / `saku.rip` | ❌ 无解析 | 桜都字幕组全部候选域实测无解析；该组只用 TG + mikan/dmhy 发布 |
| `acgnx.net` / `acgnx.eu` / `acgnx.xyz` / `acgnx.club` / `acgnx.top` / `acgnx.pro` | ❌ 无解析 | AcgnX 各历史/猜测后缀均无解析；现役为 `acgnx.se` 与 `share.acgnx.cc`/`.net` |
| `36dm.com` / `www.36dm.com` / `36dm.net` / `36dm.club` | ❌ 停放 / 空响应 | `36dm.com` 实测为 parklogic 停放页；`36dm.net` 空响应（114 字节）；`36dm.club` 无解析。社区曾把它列为 dmhy 镜像，现已失效 |
| `dmhy.b168.net` | ❌ 域名停放 | parklogic 停放页，`"domainApex":"b168.net"`（社区列为 dmhy 镜像，已失效） |
| `dmhy.ye1213.com` | ❌ 域名停放 | parklogic 停放页，`"domainApex":"ye1213.com"`（社区列为 dmhy 镜像，已失效） |
| `sccqygs.com` | ❌ 无解析 | 曾被当作 dmhy/字幕组镜像，实测连接失败 |
| `dmhy.gate.flag.moe` | ⚠️ 已暂停 | 实测页面公告：「DMHY 代理站因大量爬虫流量访问暂时关闭，请合理使用。」 |
| `animeskip.io` | ❌ 无解析 | AnimeSkip（跳过 OP/ED 工具）实测连接失败 |
| `shikimori.me` | ❌ 备用域失效 | 实测 522（Cloudflare 超时）；正常域为 `shikimori.one` |
| `nyaa.eu` | ⚠️ 非官方 | 页面自称 "Nyaa.se Torrents Proxy"，是**第三方代理站**，非官方 Nyaa |
| `nyaa.net` / `cn.nyaa.net` | ⚠️ 非官方 | 页面自称 "open torrent index"，与官方 `nyaa.si` 无关，**品牌同名陷阱** |
| `ayakawa.moe` / `sweet-sub.com` / `moonsub.org` / `uha-c9.com` / `huameng.net` | ❌ 无解析 | 各字幕组猜测/历史域名，实测均无解析 |
| `acgrip.com` | ❌ 无解析 | 论坛裸域；现役为 `bbs.acgrip.com` |
| `kitauji.net` | ⚠️ 无关占位页 | 标题 "KITAUJI-NETWORKS"，正文 "this site is a work in progress"，**与北宇治字幕组无关** |
| `mikanani.tv` | ❌ 错误域名 | 社区已纠错：「蜜柑计划国内直连域名错了，不是 mikanani.tv 是 mikanime.tv」 |

---

### 附录：建议的分流分组（按「大陆可达性」归类）

| 分组 | 域名 |
|---|---|
| **直连（国内入口）** | `mikanime.tv`、`dandanplay.com`、`dandanplay.net`、`api.dandanplay.net`、`doc.dandanplay.com`、`assets.anixplayer.net` |
| **需代理** | `dmhy.org`、`share.dmhy.org`、`bbs.dmhy.org`、`u2.dmhy.org`、`mikanani.me`、`acgnx.se`、`share.acgnx.se`、`nyaa.si`、`sukebei.nyaa.si`、`tokyotosho.info`、`anidex.info`、`bgm.tv`、`bangumi.tv`、`chii.in`、`fast.bgm.tv`、`doujin.bgm.tv`、`api.bgm.tv`、`lain.bgm.tv`、`anilist.co`、`s4.anilist.co`、`graphql.anilist.co`、`img.anili.st`、`myanimelist.net`、`cdn.myanimelist.net`、`api.myanimelist.net`、`api-cdn.myanimelist.net`、`animenewsnetwork.com`、`trace.moe`、`api.trace.moe`、`shikimori.one`、`lightnovel.fun`、`lightnovel.cn` |
| **存疑（建议先按代理放，实测后调整）** | `bangumi.moe`、`static.bangumi.moe`、`acg.rip`、`bbs.acgrip.com`、`tsdm39.com`、`www.tsdm39.com`、`img.tsdm39.com`、`img.tsdm39.net`、`tu.ts-dm.net`、`kfmax.com`、`popgo.org`、`bbs.popgo.org`、`sumisora.net`、`bbs.sumisora.net`、`vcb-s.com`、`tucaptions.org`、`share.acgnx.cc`、`share.acgnx.net` |

> 注：`share.acgnx.cc` / `share.acgnx.net` 官方定位是「仅供大陆地区访问」，但官方同时说明镜像站也曾被屏蔽，故列入「存疑」——若你的线路实测可通，可移入直连组。

## 5. 成人向动漫（里番）

- 调研日期: 2026-10-06
- 方法: WebFetch/WebSearch + curl 实测（本机走路由器代理，超时≠死站）+ 开源客户端源码（Han1meViewer Constants.kt）+ Wayback 快照 + theindex.moe(r/animepiracy wiki) 归档 JSON
- 「大陆可达性」「日本节点可用性」均标注依据；标注 (未实测) 者为推断
- 说明: hentaiplay / bukkake 等未能找到可信的官方域名证据，未列入；低质仿冒站一律不列

---

#### hanime1（Hanime1.me，重点）
- 类别: 成人动漫
- 域名: hanime1.me | hanime1.com | hanimeone.me | javchu.com | vdownload.hembed.com | 1497203185.rsc.cdn77.org
- 性质: 中文里番/H動漫在线观看最大站；视频主站 hanime1.me，漫画分站 hanimeone.me，AV 分站 javchu.com（同一运营方）
- 来源: [Han1meViewer Constants.kt（官方域名数组）](https://cdn.jsdelivr.net/gh/misaka10032w/Han1meViewer@master/app/src/main/java/com/yenaly/han1meviewer/Constants.kt)；[hanime1.me 首页实测 HTML](https://hanime1.me/)（页脚含 hanimeone.me / javchu.com 链接）；[hanime1.me 播放页](https://hanime1.me/watch?v=408545)（视频/图片 CDN 域名 vdownload.hembed.com）
- 后续更新入口: [Han1meViewer 仓库（含域名/网络设置文档）](https://github.com/misaka10032w/Han1meViewer)；官方 Discord discord.gg/hKCdsESSej（站点首页实测）
- 快测: hanime1.me 200；hanime1.com 301→hanime1.me（实测）；hanimeone.me 403（CF 盾，存活）；javchu.com 超时（本机不可达）；vdownload.hembed.com 根路径 403（防盗链，视频带签名参数可 200/206）；cdn77 备用 CDN 根路径 403（存活，需签名）
- 大陆可达性: 需代理（Cloudflare 前置，实测 CF-RAY 香港节点；社区普遍以香港/台湾节点访问，来源：linux.do 讨论）
- 日本节点可用性: **不可用**（hanime1.me 对日本 IP 受限：官方 App FAQ「我只有日本节点怎么办→把域名换成 hanime1.com，该网址部分时段不跳转且支持日本节点」（[v0.12.6+24030714 Release Notes](https://github.com/YenalyLiew/Han1meViewer/releases/tag/v0.12.6%2B24030714)）；linux.do 实测「hanime 日本 ip 会被ban」[linux.do/t/topic/371854/17](https://linux.do/t/topic/371854/17)）
- 备注: 漫画板块已迁 hanimeone.me（首页 "H漫畫" 入口实测指向 hanimeone.me/comics）；CDN 备用域 1497203185.rsc.cdn77.org 见 Constants.kt「部分地區可能無法訪問」注释；页脚友情链接（未验证内容）: moeli-desu.com、sshs.pw、qingse.one、141jj.com、pornbest.org、share.acgnx.net、daradara.me

#### hanime.tv
- 类别: 成人动漫
- 域名: hanime.tv | hanime-cdn.com | auth.hanime.tv | ct.hanime.tv | guest.freeanimehentai.net
- 性质: 英文里番最大流媒站（"The original"，1080p 需会员；theindex.moe 收录语）
- 来源: [Wayback 2026-07-01 hanime.tv 首页快照](https://web.archive.org/web/20260701042555/https://hanime.tv/)（hanime-cdn.com 被引用 103 处：/images/covers/、/js/；另有 auth.hanime.tv、ct.hanime.tv/csrf-token、guest.freeanimehentai.net/api/v11/search_hvs）；[theindex.moe JSON(2026-01)](https://web.archive.org/web/20260113100206/https://theindex.moe/_next/data/00kpxjDzO16k5FGEqAUOp/collection/hentai-streaming.json?id=hentai-streaming)；hanime-cdn.com 实测 302→/index.html 200（Last-Modified: 2025-09-17，即 2025-09 启用的新图片/静态 CDN）
- 后续更新入口: 无官方公告渠道（未发现）
- 快测: hanime.tv 403（CF 人机盾，站点存活）；hanime-cdn.com 200；guest.freeanimehentai.net 403（存活）；freeanimehentai.net 根域无响应
- 大陆可达性: 需代理（Cloudflare 前置 + CF Error 1020 常拦机房/共享 IP；webcompat 报告实例：webcompat/web-bugs#121788）
- 日本节点可用性: **倾向不可用（存疑，未由日本节点复测）**：社区实测日本 IP 被 ban（[linux.do/t/topic/371854/17](https://linux.do/t/topic/371854/17)，2025-01「hanime 日本 ip 会被ban」）；建议与 hanime1 同样走非日本节点
- 备注: 视频流 URL 由官方 API（/api/v8/video）下发，未发现独立视频 CDN 域证据，本条目只列已证实域；hanime-cdn.com 承载图片/封面/静态资源

#### ohentai.org
- 类别: 成人动漫
- 域名: ohentai.org
- 性质: 英文里番在线流媒（轻量纯 HTML 站，视频自托管于站内 video_data/ 目录）
- 来源: [ohentai.org 首页实测 HTML](https://ohentai.org/)（<title>Ohentai.org | HD Hentai Video Streams Online</title>，缩略图路径 video_data/…，无外站 CDN）
- 后续更新入口: 无（页面含 theporndude 等外链）
- 快测: 200（Cloudflare）
- 大陆可达性: 存疑偏需代理（Cloudflare 前置，未做大路直连实测）
- 日本节点可用性: 存疑（无任何站点说明/社区证据表明限制日本 IP；未实测）
- 备注: 未出现在 theindex.moe 收录列表；页内含少量博彩/成人游戏外链，无独立 CDN 域

#### hentaihaven.xxx（HentaiHaven 品牌站群）
- 类别: 成人动漫
- 域名: hentaihaven.xxx | hentaihaven.com | hentaihaven.red | hentaihaven.app | img.hentaihaven.xxx | cms.hentaihaven.xxx | coverlanyvd.org | cdnr-octopus.hhpanel.org | octopusmanifest.org | stream2.defeated.xxx
- 性质: 英文里番流媒，沿用已停运的 hentaihaven.org 品牌；.xxx/.com/.red 共用 img.hentaihaven.xxx 图片域（同一站群）
- 来源: [hentaihaven.xxx 首页实测 HTML](https://hentaihaven.xxx/)（img/cms 子域、coverlanyvd.org 封面 CDN、cdnr-octopus.hhpanel.org 缩略图、octopusmanifest.org/*/playlist.m3u8、stream2.defeated.xxx/2022files/…mp4 旧归档）；[theindex.moe 收录 Hentaihaven.com/.red](https://web.archive.org/web/20260113100206/https://theindex.moe/_next/data/00kpxjDzO16k5FGEqAUOp/collection/hentai-streaming.json?id=hentai-streaming)
- 后续更新入口: 站点自带 "official HentaiHaven Android APK" 页面（实测）；无官方公告渠道
- 快测: hentaihaven.xxx 200；hentaihaven.com 200；hentaihaven.red 200；hentaihaven.app 403；旧文件域 stream2.defeated.xxx 可用（HTML 内实测引用）
- 大陆可达性: 需代理（Cloudflare 前置；此类站大陆直连不稳定）
- 日本节点可用性: 存疑（无站点说明/社区证据；未实测）
- 备注: 官方性存疑——.xxx 自称官方（APK 页），但第三方扫描曾被指为克隆站；.com/.red 与 .xxx 共用资产域，互为镜像/站群的可能性高，勿轻信任一域"官方"

#### AnimeIDHentai
- 类别: 成人动漫
- 域名: animeidhentai.com | nhplayer.com
- 性质: 英文里番在线观看（视频以 iframe 嵌入 NH 播放器）
- 来源: [animeidhentai.com 首页实测 HTML](https://animeidhentai.com/)（视频字段为 nhplayer.com/v/<token>/；<title>Free Hentai Videos Online…</title>）；[theindex.moe 收录](https://web.archive.org/web/20260113100206/https://theindex.moe/_next/data/00kpxjDzO16k5FGEqAUOp/collection/hentai-streaming.json?id=hentai-streaming)
- 后续更新入口: 无
- 快测: 307（需 Cookie 循环后 200 内容正常，站点存活）；nhplayer.com 200
- 大陆可达性: 需代理（Cloudflare 前置）
- 日本节点可用性: 存疑（无证据；未实测）
- 备注: 与 hentai.tv 共用播放器宿主 nhplayer.com；站内 hentaihub.com 外链是 AI 图站（非流媒）

#### Hentaimama
- 类别: 成人动漫
- 域名: hentaimama.io
- 性质: 英文里番（WordPress 站，视频自托管于 hentaimama.io/wp-content/uploads）
- 来源: [hentaimama.io 首页实测](https://hentaimama.io/)；[分集页实测](https://hentaimama.io/episodes/enjo-kouhai-episode-12/)（缩略图/视频路径均在主域）；[theindex.moe 收录](https://web.archive.org/web/20260113100206/https://theindex.moe/_next/data/00kpxjDzO16k5FGEqAUOp/collection/hentai-streaming.json?id=hentai-streaming)
- 后续更新入口: 站点 /devblog/ 页面（实测存在）
- 快测: 200（Cloudflare）
- 大陆可达性: 需代理（Cloudflare 前置）
- 日本节点可用性: 存疑（无证据；未实测）
- 备注: 页面外链 hentaihub.com 是 AI 生成图站（实测 <title>AI Hentai Generator</title>），非流媒

#### Hentai.tv
- 类别: 成人动漫
- 域名: hentai.tv | nhplayer.com
- 性质: 英文里番在线流媒（播放器嵌入 nhplayer.com）
- 来源: [hentai.tv 首页实测 HTML](https://hentai.tv/)（nhplayer.com 引用 36 处）；[theindex.moe 收录](https://web.archive.org/web/20260113100206/https://theindex.moe/_next/data/00kpxjDzO16k5FGEqAUOp/collection/hentai-streaming.json?id=hentai-streaming)
- 后续更新入口: 无
- 快测: 200（Cloudflare）
- 大陆可达性: 需代理（Cloudflare 前置）
- 日本节点可用性: 存疑（无证据；未实测）
- 备注: 与 animeidhentai.com 共用播放器宿主

#### HentaiStream（hstream.moe）
- 类别: 成人动漫
- 域名: hstream.moe（旧域 hentaistream.moe 已弃用）
- 性质: 英文里番，部分片源 4K（theindex 语 "Has some hentai in 4K"）
- 来源: [theindex.moe JSON(2026-01)](https://web.archive.org/web/20260113100206/https://theindex.moe/_next/data/00kpxjDzO16k5FGEqAUOp/collection/hentai-streaming.json?id=hentai-streaming)；[2022 年 piracy.moe 收录旧域 hentaistream.moe](https://web.archive.org/web/20220512074746/https://piracy.moe/_next/data/BAP3p8YY2CZ200Yj7VZE7/collection/hentai-streaming.json)；实测 <title>Watch English Subbed Hentai Online in HD & 4K | hstream.moe</title>
- 后续更新入口: 无
- 快测: 200（Cloudflare）
- 大陆可达性: 需代理（Cloudflare 前置）
- 日本节点可用性: 存疑（无证据；未实测）
- 备注: 换域历史 hentaistream.moe → hstream.moe

#### 999Hentai
- 类别: 成人动漫
- 域名: 999hentai.net（旧域 999hentai.com 已弃用）
- 性质: 英文里番在线观看
- 来源: [theindex.moe JSON(2026-01，域名 .net)](https://web.archive.org/web/20260113100206/https://theindex.moe/_next/data/00kpxjDzO16k5FGEqAUOp/collection/hentai-streaming.json?id=hentai-streaming)；[2022 piracy.moe 收录旧域 .com](https://web.archive.org/web/20220512074746/https://piracy.moe/_next/data/BAP3p8YY2CZ200Yj7VZE7/collection/hentai-streaming.json)
- 后续更新入口: 无
- 快测: 200（Cloudflare）
- 大陆可达性: 需代理（Cloudflare 前置）
- 日本节点可用性: 存疑（无证据；未实测）
- 备注: 换域历史 999hentai.com → 999hentai.net

#### Akuma（akuma.moe）
- 类别: 成人动漫
- 域名: akuma.moe
- 性质: 英文/多语里番流媒（theindex 语：多语言字幕）
- 来源: [theindex.moe JSON(2026-01)](https://web.archive.org/web/20260113100206/https://theindex.moe/_next/data/00kpxjDzO16k5FGEqAUOp/collection/hentai-streaming.json?id=hentai-streaming)
- 后续更新入口: 无
- 快测: 403（CF 盾/区域拦截，站点存活）
- 大陆可达性: 需代理（Cloudflare 前置）
- 日本节点可用性: 存疑（无证据；未实测）
- 备注: 无独立 CDN 域证据；403 时需浏览器环境

#### AnimeFesta（アニメフェスタ，官方）
- 类别: 成人动漫
- 域名: animefesta.iowl.jp | comic.iowl.jp
- 性质: 日本官方 R18 动画订阅平台（僧侶枠/无修正 Premium 版），运营方 WWWave
- 来源: [animefesta.iowl.jp 实测](https://animefesta.iowl.jp/)（Server: AmazonS3 + CloudFront）；[WWWave 官方服务页](https://wwwave.jp/service/animefesta/)
- 后续更新入口: 官方 X @AnimeFesta_info（WWWave 官网标注）
- 快测: animefesta.iowl.jp 200；comic.iowl.jp 200（ComicFesta 姊妹站，漫画清单如已收可忽略）
- 大陆可达性: 存疑偏直连（Amazon CloudFront/S3，非 Cloudflare；未实测，日本站大陆直连一般可通但速度一般）
- 日本节点可用性: 可用（日本本土官方服务；反向提示：海外观看可能受地区/支付限制）
- 备注: animefesta.one、animefesta.com 均 NXDOMAIN（实测），勿用仿冒域；WWWave 海外动画品牌 OceanVeil（oceanveil.com 本机不可达，未验证）

#### DLsite（去重确认）
- 类别: 成人动漫（含动画区）
- 域名: www.dlsite.com | play.dlsite.com
- 性质: 日本官方同人/成人作品交易平台（动画、音声、游戏）；已由漫画清单覆盖，此处仅确认不重复收
- 来源: [www.dlsite.com 实测](https://www.dlsite.com/)；[play.dlsite.com 实测](https://play.dlsite.com/)（官方购买后串流播放器）
- 后续更新入口: 无（与漫画清单同源）
- 快测: www.dlsite.com 200；play.dlsite.com 200
- 大陆可达性: 需代理（DLsite 对大陆访问有地域/风控限制，社区通识）
- 日本节点可用性: 可用（日本本土平台）
- 备注: 唯一新增贡献是 play.dlsite.com（官方流媒体播放域），如漫画清单未收可补

#### 琉璃神社（HACG）
- 类别: 成人动漫
- 域名: www.hacg.me | hacg.la | hacg.casa | hacg.zip | hacg8.com
- 性质: 中文成人ACG资讯/同人资源分享站（含里番介绍与磁力；官方声明不提供直接下载）
- 来源: [www.hacg.me 实测](https://www.hacg.me/)（<title>琉璃神社★分享动漫快乐</title>）；hacg.la 302→hacg.casa（同名站，实测）；hacg.zip 302→ww38.hacg.zip（实测）；[hacg8.com 实测](http://www.hacg8.com/)（<title>琉璃神社导航 | 最新琉璃神社ACG资讯</title>）
- 后续更新入口: 导航站 hacg8.com；社区讨论 liulishe.ooo（域名变动频繁）
- 快测: www.hacg.me 200；hacg.casa 200；hacg.zip 302；hacg8.com 200
- 大陆可达性: 存疑偏需代理（域名极不稳定、常被攻击；未实测大陆直连）
- 日本节点可用性: 存疑（无证据；未实测）
- 备注: 域名更换极频繁（社区多年持续追踪）；官方声明无任何官方群/收款账号，谨防冒充

#### 末日動漫資源庫（share.acgnx.net）
- 类别: 成人动漫（资源库）
- 域名: share.acgnx.net | share.acgnx.se
- 性质: 动漫资源分享站（hanime1.me 页脚友情链接标注「末日動漫資源庫」）
- 来源: [hanime1.me 首页页脚实测](https://hanime1.me/)；share.acgnx.net 302→share.acgnx.se（实测，CF 盾 "Just a moment..."）
- 后续更新入口: 无（需登录，未深入）
- 快测: share.acgnx.se 403（CF 盾，存活）
- 大陆可达性: 需代理（Cloudflare 前置）
- 日本节点可用性: 存疑（无证据；未实测）
- 备注: 非在线观看站，性质为资源库；是否官方无法与 hanime1 关系外核实

---

### 已确认失效 / 仿冒 / 停放域名（证据）
- hentaihaven.org: 原 HentaiHaven 主域，已停运多年；实测连接超时（DNS 仍解析到 Cloudflare IP 104.21.75.6/172.67.166.58 但无响应）；Wayback 无 2024+ 有效快照（archive.org availability API 返回空）
- hentaidude.com: **NXDOMAIN**（Cloudflare DNS/Google DNS 双源验证，2026-10-06）；nslookup 1.1.1.1 同样 NXDOMAIN；2026-01 theindex.moe 仍收录旧域
- hentaidude.to: NXDOMAIN（Google DNS 实测）
- hentaidude.net: 存活但为 JS 反爬壳页（仅 476 字节 "Loading..." + window.location.replace('?ch=1&js=JWT')）；与 hanime1.org 同款壳页模式，非可用站点
- hanime.io: 无响应（000）；2022 piracy.moe 收录时明确标注 "Not affiliated with hanime.tv"
- hanime1.org: **非官方**——不在 Han1meViewer Constants.kt 官方域名数组；实测为 JWT 跳转壳页 + intivesearch 广告停放页（含 intivesearch.com/privacy?dmn=hanime1.org 参数），非 hanime1.me 镜像
- hanime1.pw / www.hanime1.pw: 解析到非 Cloudflare IP（38.190.206.16 等），实测 500/stub 按钮页，非官方、疑似仿冒/停放
- hanime1.one: 解析到 38.49.10.110，实测连接超时，未列入任何官方来源，疑似停放/仿冒
- hentaistream.moe: 旧域，已被 hstream.moe 取代（theindex 2022 vs 2026 对比）
- 999hentai.com: 旧域，已被 999hentai.net 取代（同上）
- freeanimehentai.net: hanime.tv 关联 API 宿主 guest.freeanimehentai.net 存活（403），但根域 freeanimehentai.net 无响应

### 未纳入说明
- hentaiplay / bukkake 系: 未找到可信官方域名证据，不列
- 大量低质仿冒/克隆站（如 hentaihaven 各种变体域）不逐一收录，仅收录有来源支撑者
- 中文"里世界/樱花里番"等: 未能找到可验证的官方当前域名，不凑数
- hanime1.me 页脚友情链接站（moeli-desu.com 夢璃、sshs.pw 紳士會所、qingse.one、141jj.com、pornbest.org、daradara.me）: 内容未验证，不列入正文，仅备注

## 6. 统一实测记录（2026-10-06）

- 实测对象：本文收录的 **736 个唯一域名**，逐个做三项测试：① DoH 双解析（AliDNS `223.5.5.5` + Cloudflare）② HTTPS 连通（curl，超时 12s，失败退 http:// 重试）③ 标题抓取（确认真是目标站点）
- 环境：本机（Windows + 路由器 OpenClash）出网，**出口是日本（AWS Tokyo）**——所以这批结果只能证明「站点存活」，**不能证明大陆可达**；也正因如此才有 §阅读说明 的「存疑」类别
- 结果分布：**可访问 505** ｜ 反爬/受限（403/404/5xx 等，站点存活）**169** ｜ 超时/连接失败（DNS 有解析）**52** ｜ 无解析（NXDOMAIN）**10**
- 判读注意：① CDN 基域 apex 无 A 记录、403/404 属反爬或 API 根路径特性，都不代表不可用；② 两个解析器结果不一致时以站点实测为准

> 完整明细（`DNS` = AliDNS/Cloudflare；`HTTP` 列 `h` 前缀 = https 失败后 http 成功）：

```
### 国内直连（74）
2fp-cdnstatic.svc.litv.tv                   NX/NO_A     000
a1.itc.cn                                   OK/OK       403
account.youku.com                           OK/OK       200
acfun.cn                                    OK/OK       301
acg.youku.com                               OK/OK       403
api.bilibili.com                            OK/OK       301
api.dandanplay.net                          OK/OK       401
assets.anixplayer.net                       OK/OK       404
b23.tv                                      OK/OK       404
bangumi.bilibili.com                        OK/OK       302
bilibili.com                                OK/OK       301
bilivideo.com                               NO_A/NO_A   000
cache-video.iq.com                          OK/OK       200
cache.video.iqiyi.com                       OK/OK       200
cartoon.aplus.pptv.com                      OK/OK       200
css.tv.itc.cn                               OK/OK       403
dandanplay.com                              OK/OK       301
dandanplay.net                              OK/OK       302
display-sc.miguvideo.com                    OK/OK       404
film.qq.com                                 OK/OK       302
fino.svc.litv.tv                            OK/OK       200
honey.mgtv.com                              OK/OK       403
i0.hdslb.com                                OK/OK       200
i1.hdslb.com                                OK/OK       200
i2.hdslb.com                                OK/OK       200
i3.itc.cn                                   OK/OK       403
img.cmvideo.cn                              OK/OK       200
img.mgtv.com                                OK/OK       403
img7.iqiyipic.com                           OK/OK       404
imgs.aixifan.com                            OK/OK       200
intl-api.iq.com                             OK/OK       404
intl-help.iq.com                            OK/OK       200
iq.com                                      OK/OK       302
iqiyi.com                                   OK/OK       301
iqiyipic.com                                OK/OK       h301
itc.cn                                      OK/OK       000
le.com                                      OK/OK       301
letv.com                                    OK/OK       301
liangcang-material.alicdn.com               OK/OK       403
litv.tv                                     OK/OK       301
m.miguvideo.com                             OK/OK       200
m.ykimg.com                                 OK/OK       403
m.youku.tv                                  OK/OK       302
mgtv.com                                    OK/OK       302
migu.cn                                     OK/OK       301
migudm.cn                                   OK/OK       200
miguvideo.com                               OK/OK       302
mikanime.tv                                 OK/OK       302
msg-intl.qy.net                             OK/OK       200
my.tv.sohu.com                              OK/OK       301
pptv.com                                    OK/OK       000
puui.qpic.cn                                OK/OK       400
qy.net                                      OK/OK       302
s1.hdslb.com                                OK/OK       200
so.youku.com                                OK/OK       302
sohu.com                                    OK/OK       302
static.hitv.com                             OK/OK       403
static.wetvinfo.com                         OK/OK       401
t.youku.com                                 OK/OK       302
v.qq.com                                    OK/OK       200
v.youku.com                                 OK/OK       200
vfiles.gtimg.cn                             OK/OK       400
videohy.tc.qq.com                           OK/OK       h302
vliveachy.tc.qq.com                         OK/OK       h302
vm.gtimg.cn                                 OK/OK       200
vv.video.qq.com                             OK/OK       200
wapx.cmvideo.cn                             OK/OK       200
wetv.vip                                    OK/OK       200
wetvinfo.com                                OK/OK       h301
www.youku.com                               OK/OK       302
www.youku.tv                                OK/OK       200
ykimg.alicdn.com                            OK/OK       403
youku.com                                   OK/OK       302
youku.tv                                    OK/OK       200

### 海外代理（362）
123animehub.cc                              OK/OK       200
141jj.com                                   OK/OK       200
1497203185.rsc.cdn77.org                    OK/OK       403
1ani.me                                     OK/OK       200
999hentai.com                               OK/OK       302
999hentai.net                               OK/OK       200
9animstv.to                                 OK/OK       200
abema.tv                                    OK/OK       200
account.nicovideo.jp                        OK/OK       404
account.unext.jp                            OK/OK       302
acg.gamer.com.tw                            OK/OK       302
acg.rip                                     OK/OK       200
acgdm001.com                                OK/OK       000
acgnx.se                                    OK/OK       301
aeoncinema-video.unext.jp                   OK/OK       h301
aestheticode.net                            OK/OK       200
agedm.io                                    OK/OK       301
akuma.moe                                   OK/OK       403
allmanga.to                                 OK/OK       200
ani.baha.tw                                 OK/OK       302
ani.gamer.com.tw                            OK/OK       200
ani.pm                                      OK/OK       200
anichan.to                                  OK/OK       200
anichi.to                                   OK/OK       200
aniclipse.com                               OK/OK       200
anidap.lol                                  OK/OK       200
anidex.info                                 OK/OK       403
anidoor.me                                  OK/OK       200
anify.to                                    OK/OK       404
anihq.cc                                    OK/OK       403
anikage.cc                                  OK/OK       200
anikoto.cz                                  OK/OK       200
anikoto.me                                  OK/OK       200
anikoto.net                                 OK/OK       200
anikoto.site                                OK/OK       200
anikototv.se                                OK/OK       200
anikototv.to                                OK/OK       200
anikura.club                                OK/OK       200
anikuro.ru                                  OK/OK       200
anikuro.site                                OK/OK       200
anikuro.to                                  OK/OK       200
anilight.live                               OK/OK       403
anilist.co                                  OK/OK       200
anime-jl.net                                OK/OK       200
anime.nexus                                 OK/OK       200
anime.nicovideo.jp                          OK/OK       200
anime1.me                                   OK/OK       403
animeav1.com                                OK/OK       200
animedex.fun                                OK/OK       200
animefesta.iowl.jp                          OK/OK       200
animeflv.net                                OK/OK       h301
animegg.org                                 OK/OK       301
animehodai.jp                               NO_A/NO_A   000
animeid.tv                                  OK/OK       301
animeidhentai.com                           OK/OK       307
animemars.org                               OK/OK       301
animenewsnetwork.com                        OK/OK       301
animenosub.to                               OK/OK       200
animeonsen.xyz                              OK/OK       403
animepahe.com                               OK/OK       301
animepahe.org                               OK/OK       301
animepahe.pw                                OK/OK       403
animepahe.su                                OK/OK       200
animeparadise.moe                           OK/OK       308
animesaturn.cx                              OK/OK       301
animesaturn.net                             OK/OK       301
animestore.docomo.ne.jp                     OK/OK       302
animesuge.bid                               OK/OK       200
animesuge.cz                                OK/OK       200
animesuge.re                                OK/OK       200
animesugez.tv                               OK/OK       200
animetimes-store.com                        OK/OK       h301
animetimes.co.jp                            OK/OK       200
animeunity.so                               OK/OK       403
animeunity.to                               OK/OK       302
animewave.to                                OK/OK       200
animeworld.ac                               OK/OK       301
animex.one                                  OK/OK       200
aninami.site                                OK/OK       308
anisaturn.com                               OK/OK       301
anisnatch.top                               OK/OK       200
anistream.one                               OK/OK       200
anisuge.se                                  OK/OK       200
anisuge.tv                                  OK/OK       200
aniwatch.rest                               OK/OK       301
aniwave.cz                                  OK/OK       301
aniwaves.ru                                 OK/OK       200
anizone.to                                  OK/OK       200
api-cdn.myanimelist.net                     OK/OK       404
api-gateway-global.viu.com                  OK/OK       200
api-videopass-sockets.kddi-video.com        OK/OK       404
api-videopass.kddi-video.com                OK/OK       404
api.abema.io                                OK/OK       200
api.bgm.tv                                  OK/OK       200
api.bilibili.tv                             OK/OK       404
api.lightnovel.fun                          OK/OK       200
api.myanimelist.net                         OK/OK       404
api.trace.moe                               OK/OK       200
asiancrush.com                              OK/OK       301
assets.b-ch.com                             OK/OK       403
assets.mytvsuper.com                        OK/OK       200
auth.hanime.tv                              OK/OK       403
auth.hulu.com                               OK/OK       403
avatar2.bahamut.com.tw                      OK/OK       200
awsimgsrc.dmm.com                           OK/OK       200
b-ch.com                                    NO_A/NO_A   000
babyanime.top                               OK/OK       200
bahamut.akamaized.net                       OK/OK       000
bahamut.com.tw                              NO_A/NO_A   000
bangumi.moe                                 OK/OK       200
bangumi.tv                                  OK/OK       200
banime.top                                  OK/OK       200
bbs.acgrip.com                              OK/OK       403
bbs.dmhy.org                                OK/OK       200
beacon.unext.jp                             OK/OK       404
bees.streaks.jp                             OK/OK       403
beta.crunchyroll.com                        OK/OK       302
bgm.tv                                      OK/OK       200
bilibili.tv                                 OK/OK       301
biliintl.com                                OK/OK       404
bstarstatic.com                             NO_A/NO_A   000
buy.gamer.com.tw                            OK/OK       200
cbhtv.top                                   OK/OK       301
cc.unext.jp                                 OK/OK       400
ccytv.cc                                    OK/OK       301
cdn.matchpoint.tv                           OK/OK       401
cdn.myanimelist.net                         OK/OK       404
cdn.nimg.jp                                 NO_A/NO_A   000
cdn.vidcloud.se                             OK/OK       404
cdn.videopass.jp                            OK/OK       200
cdnr-octopus.hhpanel.org                    OK/OK       404
ch.nicovideo.jp                             OK/OK       200
chii.in                                     OK/OK       200
cinemacoupon.unext.jp                       OK/OK       200
cms.hentaihaven.xxx                         OK/OK       410
comic.iowl.jp                               OK/OK       200
conf.lemino.docomo.ne.jp                    OK/OK       403
contact.unext.jp                            OK/OK       307
content-images.onvesper.com                 OK/OK       307
coupon.unext.jp                             OK/OK       404
coverlanyvd.org                             OK/OK       200
cr-play-service.prd.crunchyrollsvc.com      OK/OK       403
crunchyroll.com                             OK/OK       301
crunchyrollexpo.com                         OK/OK       301
crunchyrollsvc.com                          NO_A/NO_A   000
ct.hanime.tv                                OK/OK       200
cyc-anime.net                               OK/OK       302
cycani.org                                  OK/OK       302
d1zquzjgwo9yb.cloudfront.net                NO_A/NO_A   000
d2anahhhmp1ffz.cloudfront.net               OK/OK       403
daradara.me                                 OK/OK       200
dce-frontoffice.imggaming.com               OK/OK       404
dic.nicovideo.jp                            OK/OK       200
dmhy.anoneko.com                            OK/OK       301
dmhy.org                                    OK/OK       200
dmm.com                                     OK/OK       301
dongmanhuayuan.myheartsite.com              OK/OK       200
e-muse.com                                  OK/OK       403
e-muse.com.tw                               NO_A/NO_A   000
e.kortw.cc                                  OK/OK       200
edge-api.hulu.com                           OK/OK       404
embed.nicovideo.jp                          OK/OK       200
enc-dec.app                                 OK/OK       200
enma.lol                                    OK/OK       301
fcbbcc.com                                  OK/OK       h403
fireani.me                                  OK/OK       200
flixcloud.cc                                OK/OK       200
fod.fujitv.co.jp                            OK/OK       200
forum.gamer.com.tw                          OK/OK       200
freeanimehentai.net                         OK/OK       h301
gamer-cds.cdn.hinet.net                     OK/NX       000
gamer.com.tw                                OK/OK       302
gamer2-cds.cdn.hinet.net                    S2/NX       000
hacg.casa                                   OK/OK       200
hacg.la                                     OK/OK       301
hacg.me                                     OK/OK       301
hacg.zip                                    OK/OK       302
hacg8.com                                   OK/OK       301
hanime-cdn.com                              OK/OK       302
hanime.io                                   OK/OK       000
hanime.tv                                   OK/OK       403
hanime1.com                                 OK/OK       301
hanime1.me                                  OK/OK       200
hanimeone.me                                OK/OK       403
happyon.jp                                  OK/OK       301
help.hulu.jp                                OK/OK       302
help.telasa.jp                              OK/OK       200
help.unext.jp                               OK/OK       200
hentai.tv                                   OK/OK       200
hentaihaven.app                             OK/OK       200
hentaihaven.com                             OK/OK       200
hentaihaven.red                             OK/OK       200
hentaihaven.xxx                             OK/OK       200
hentaimama.io                               OK/OK       200
hentaistream.moe                            OK/OK       200
hexa.su                                     OK/OK       200
hianimes.ru                                 OK/OK       200
hianimes.se                                 OK/OK       200
hidive.com                                  OK/OK       301
hjholdings.tv                               NO_A/NO_A   000
hjtv5.cc                                    OK/OK       301
hjwtv.cc                                    OK/OK       301
home.hulu.com                               OK/OK       302
hstream.moe                                 OK/OK       200
hulu.com                                    OK/OK       301
hulu.jp                                     OK/OK       302
huluim.com                                  NO_A/NO_A   000
id.smt.docomo.ne.jp                         OK/OK       301
if.lemino.docomo.ne.jp                      OK/OK       200
image-cf.kddi-video.com                     OK/OK       403
img.anili.st                                OK/OK       404
img.tsdm39.com                              OK/OK       200
img.tsdm39.net                              OK/OK       200
iyf.tv                                      OK/OK       302
javchu.com                                  OK/OK       h200
jkanime.net                                 OK/OK       403
justanime.to                                OK/OK       200
kaa.am                                      S2/NX       000
kaa.lt                                      OK/OK       200
kaa.to                                      OK/OK       301
kaas.am                                     OK/OK       h200
kawaiianime.cc                              OK/OK       200
kazora.cc                                   OK/OK       200
kfmax.com                                   OK/OK       302
kkdm3.com                                   OK/OK       200
kototv.to                                   OK/OK       200
kwik.cx                                     OK/OK       403
kyren.moe                                   OK/OK       200
latanime.org                                OK/OK       200
lcms-beacon.unext.jp                        OK/OK       404
lemino.docomo.ne.jp                         OK/OK       200
lf3-data.volccdn.com                        OK/OK       404
license.abema.io                            OK/OK       200
lightnovel.cn                               OK/OK       301
lightnovel.fun                              OK/OK       302
linear-abematv.akamaized.net                OK/OK       200
live.nicovideo.jp                           OK/OK       200
luffytv.live                                OK/OK       200
luna-stream.me                              OK/OK       200
lunarx.to                                   OK/OK       200
m.imageimg.net                              OK/OK       301
manifest.streaks.jp                         OK/OK       200
matchpoint.tv                               OK/OK       301
medialink.com.hk                            OK/OK       200
meguanime.com                               OK/OK       200
midnightpulp.com                            OK/OK       301
mikanani.kas.pub                            OK/OK       200
mikanani.me                                 OK/OK       200
miruro.bz                                   OK/OK       403
miruro.com                                  OK/OK       302
miruro.cx                                   OK/OK       403
miruro.to                                   OK/OK       403
miruro.tv                                   OK/OK       403
mjtt2.cc                                    OK/OK       301
mkissa.to                                   OK/OK       200
mobile.unext.jp                             OK/OK       200
moeli-desu.com                              OK/OK       403
monoschinos2.net                            OK/OK       301
myaccount.unext.jp                          OK/OK       200
myanimelist.net                             OK/OK       200
mytvsuper.com                               OK/OK       301
navi.telasa.jp                              OK/OK       200
nekowatch.xyz                               OK/OK       200
news.nicovideo.jp                           OK/OK       200
nhplayer.com                                OK/OK       200
nicoprofile.nimg.jp                         NO_A/NO_A   000
nicotv.me                                   OK/OK       h200
nicotv.org                                  OK/OK       h200
nicovideo.jp                                OK/OK       301
nimg.jp                                     NO_A/NO_A   000
nivod.cc                                    OK/OK       301
nyaa.si                                     OK/OK       200
nyaa.tracker.wf                             OK/OK       000
oauth.unext.jp                              OK/OK       404
octopusmanifest.org                         OK/OK       200
og.bakayaro.live                            OK/OK       403
ohentai.org                                 OK/OK       200
otakuhg.site                                OK/OK       200
p-bstarstatic.akamaized.net                 OK/OK       403
pahe.win                                    OK/OK       403
piratexplay.cc                              OK/OK       200
play.dlsite.com                             OK/OK       200
players.streaks.jp                          OK/OK       403
playmogo.com                                OK/OK       302
popgo.org                                   OK/OK       200
pornbest.org                                OK/OK       492
qingse.one                                  OK/OK       403
qlyyz.xyz                                   OK/OK       200
rconf.unext.jp                              OK/OK       403
reanime.cz                                  OK/OK       200
reanime.to                                  OK/OK       200
reanime.wtf                                 OK/OK       200
registration.unext.jp                       OK/OK       307
reindex.to                                  OK/OK       200
restatus.me                                 OK/OK       200
retrocrush.tv                               OK/OK       301
s-flow.unext.jp                             OK/OK       404
s.vidcloud.se                               OK/OK       200
sakusaku.to                                 OK/OK       302
senshi.to                                   OK/OK       200
share.acgnx.cc                              OK/OK       302
share.acgnx.net                             OK/OK       301
shikimori.one                               OK/OK       301
sidecar.unext.jp                            OK/OK       000
sshs.pw                                     OK/OK       301
sta.anicdn.com                              OK/OK       403
static.diceplatform.com                     OK/OK       307
static01.ca.unext.jp                        OK/OK       200
streaks.jp                                  OK/OK       301
stream2.defeated.xxx                        OK/OK       403
sub.wyzie.ru                                OK/OK       301
suge.to                                     OK/OK       200
sukebei.tracker.wf                          OK/OK       000
sumisora.net                                OK/OK       200
support.unext.jp                            OK/OK       308
telasa.jp                                   OK/OK       301
tokyotosho.info                             OK/OK       302
trace.moe                                   OK/OK       200
tsdm39.com                                  OK/OK       301
tu.ts-dm.net                                OK/OK       200
tucaptions.org                              OK/OK       200
tvanime.tv                                  OK/OK       200
tvbanywhere.com                             OK/OK       301
um.viuapi.io                                OK/OK       404
unext-info.jp                               NO_A/NO_A   000
unext.co.jp                                 OK/OK       h301
unext.jp                                    OK/OK       h301
upos-bstar-mirrorakam.akamaized.net         OK/OK       403
upos-bstar1-mirrorakam.akamaized.net        OK/OK       403
vcb-s.com                                   OK/OK       403
vdownload.hembed.com                        OK/OK       403
viu.com                                     OK/OK       301
viu.tv                                      OK/OK       200
viuapi.io                                   NO_A/NO_A   000
vivibebe.site                               OK/OK       000
vod-abematv.akamaized.net                   OK/OK       200
vod-images.onvesper.com                     OK/OK       307
wco.tv                                      OK/OK       301
wcoanimedub.tv                              OK/OK       301
wcoanimesub.tv                              OK/OK       301
wcoflix.tv                                  OK/OK       403
wcoforever.com                              OK/OK       301
wcoforever.net                              OK/OK       301
wcofun.com                                  OK/OK       301
wcostream.com                               OK/OK       301
wcostream.tv                                OK/OK       403
www.dlsite.com                              OK/OK       301
www.xcytv.cc                                OK/OK       200
www.xkytv.cc                                OK/OK       200
www.zbkatv.cc                               OK/OK       200
xanime.app                                  OK/OK       200
xanime.me                                   OK/OK       200
xcytv.cc                                    OK/OK       301
xiaoxintv.cc                                OK/OK       403
xkytv.cc                                    OK/OK       301
yenime.net                                  OK/OK       200
yhdm.la                                     OK/OK       h444
yomi.to                                     OK/OK       200
ytanime.tv                                  OK/OK       403
zbkatv.cc                                   OK/OK       301
zzzfun.com                                  OK/OK       h200
zzzfun.org                                  OK/OK       h301

### 代理·存疑（74）
5dm.dev                                     OK/OK       403
age.tv                                      OK/OK       h302
ageapp.app                                  OK/OK       200
agedm.com                                   OK/OK       h302
agedm.live                                  OK/OK       302
agedm.me                                    OK/OK       h503
agedm.org                                   OK/OK       h301
agedm.vip                                   OK/OK       200
agefans.com                                 OK/OK       h302
agefans.la                                  OK/OK       h301
ani.girigirilove.com                        OK/OK       200
anibk.com                                   OK/OK       301
anifun.cn                                   OK/OK       200
anime.girigirilove.com                      OK/OK       301
animefenix2.tv                              OK/OK       301
animetake.tv                                OK/OK       404
anisnatch.site                              OK/OK       200
app.xifandm.net                             OK/OK       301
apps.fengctv.com.cn                         OK/OK       400
bbs.kfmax.com                               OK/OK       302
bbs.popgo.org                               OK/OK       200
bbs.sumisora.net                            OK/OK       200
bestdubbedanime.com                         OK/OK       307
cn-yinghuadm.com.cn                         OK/OK       200
cn-yinghuadman.com.cn                       OK/OK       200
cycanime.com                                NO_A/NO_A   000
cycdm01.top                                 OK/OK       302
cycity.pro                                  OK/OK       301
dilidili51.com                              OK/OK       200
dlidli.app                                  OK/OK       200
dm.xifanacg.com                             OK/OK       301
dm530.in                                    OK/OK       200
dm530.org                                   OK/OK       200
dm530w6.com                                 OK/OK       000
dmmandao.com.cn                             OK/OK       200
fantuantv.com                               OK/OK       200
fcdm22.com                                  OK/OK       301
fcdmtv.cc                                   OK/OK       301
fengchedm.cc                                OK/OK       000
fengchedm.com                               OK/OK       301
girigiri.cn                                 OK/OK       200
girigirilove.com                            OK/OK       301
gugu3.com                                   OK/OK       301
img.lzipic.com                              OK/OK       200
img.picbf.com                               OK/OK       200
img2.xfmanga.top                            OK/OK       404
imomoe.ai                                   OK/OK       429
kawaiifu.com                                OK/OK       403
kimoitv.com                                 OK/OK       403
kuroiru.co                                  OK/OK       200
luffytv.online                              OK/OK       200
megaplay.buzz                               OK/OK       200
mobile.meinadi.cn                           OK/OK       h200
myani.org                                   OK/OK       200
next.xifanacg.com                           OK/OK       200
nkdm.hkdrj.cn                               NO_A/NO_A   000
omofuns.com                                 OK/OK       301
p.bfvp26.com                                OK/OK       200
piratexplay.com                             OK/OK       200
projectjust.xyz                             OK/OK       200
qudman.com.cn                               OK/OK       200
tokuzilla.net                               NO_A/NO_A   000
ttiandman.com.cn                            OK/OK       200
tvtfun.net                                  OK/OK       200
www.xuandm.com                              OK/OK       301
www.yhdmtv.cc                               OK/OK       200
xifan.moe                                   OK/OK       200
xifanacg.com                                NO_A/NO_A   000
xuandm.com                                  OK/OK       301
yhdm.so                                     OK/OK       h200
yhdmtv.cc                                   OK/OK       301
yhpdm.net                                   OK/OK       200
yinghuacd.com                               NO_A/NO_A   000
yinghuafanju.com.cn                         OK/OK       403

### 已失效（99）
2dgal.com                                   /           000
36dm.club                                   /           000
36dm.com                                    /           000
36dm.net                                    /           000
acgnx.club                                  /           000
acgnx.eu                                    /           000
acgnx.net                                   NO_A/NO_A   000
acgnx.pro                                   /           000
acgnx.top                                   /           000
acgnx.xyz                                   /           000
acgrip.com                                  /           000
agg.md                                      /           000
anime-times.jp                              /           000
anime4up.tv                                 /           000
animedao.to                                 /           000
animefox.io                                 /           000
animekai.to                                 /           000
animekisa.tv                                /           000
animelab.com                                OK/OK       302
animeskip.io                                /           000
anitaku.bz                                  /           000
anitaku.pe                                  /           000
anitaku.to                                  /           000
aniwatch.to                                 /           000
aniwatchtv.to                               /           000
aniwave.live                                /           000
aniwave.to                                  /           000
anix.me                                     /           000
ayakawa.moe                                 /           000
cn.nyaa.net                                 /           000
dm519.fans                                  /           000
dm530.com                                   /           000
dm530w.org                                  /           000
dmhy.b168.net                               /           000
dmhy.gate.flag.moe                          /           000
dmhy.ye1213.com                             /           000
dmla.fans                                   /           000
dmzj.com                                    OK/OK       h302
funimation.com                              OK/OK       301
gogo-load.com                               /           000
gogoanime.vc                                /           000
gogoanime3.co                               /           000
gogocdn.net                                 /           000
gyao.yahoo.co.jp                            NO_A/NO_A   000
hanime1.one                                 OK/OK       h200
hanime1.org                                 S2/OK       302
hanime1.pw                                  OK/OK       301
hentaidude.com                              OK/NX       000
hentaidude.net                              OK/OK       200
hentaidude.to                               NX/NX       000
hentaihaven.org                             OK/OK       h301
hianime.to                                  /           000
huameng.net                                 /           000
jysub.com                                   /           000
jysub.net                                   /           000
jysub.org                                   /           000
kaido.to                                    /           000
kitauji.net                                 /           000
lightnovel.us                               /           000
lknovel.cn                                  /           000
loli.house                                  /           000
lolihouse.cafe                              /           000
mikanani.tv                                 /           000
moonsub.org                                 /           000
nyaa.eu                                     /           000
nyaa.net                                    /           000
nyaa.se                                     /           000
paravi.jp                                   OK/OK       301
popgo.net                                   /           000
saku.rip                                    /           000
sakurato.com                                /           000
sakurato.moe                                /           000
sakurato.net                                /           000
sccqygs.com                                 /           000
shikimori.me                                /           000
sub.jysub.net                               /           000
sumisora.org                                /           000
sweet-sub.com                               /           000
tsdm.live                                   /           000
tsdm.love                                   /           000
tsdm39.net                                  /           000
tsdm39.org                                  /           000
uha-c9.com                                  /           000
v.vrv.co                                    /           000
vrv.co                                      OK/OK       301
wakanim.tv                                  OK/OK       301
ww38.aniwave.to                             /           000
www.36dm.com                                /           000
www.lightnovel.us                           /           000
www.lknovel.cn                              /           000
www.loli.house                              /           000
www.popgo.net                               /           000
www.sumisora.org                            /           000
www.tsdm.live                               /           000
www.tsdm39.net                              /           000
www.tsdm39.org                              /           000
yhdmp.net                                   /           000
zoro.to                                     /           000
zzzfun.one                                  OK/OK       200

### 其他（210）
anineko.to                                  OK/OK          200
api.animeparadise.moe                       OK/OK          404
btrace.wetvinfo.com                         NXDOMAIN/NXDOMAIN    000
cdndm5.com                                  OK/OK          200
cs1.animestore.docomo.ne.jp                 OK/OK          404
css99tel.cdndm5.com                         OK/OK          403
data.bilibili.com                           OK/OK          404
dlsite.com                                  OK/OK          301
dm5.com                                     OK/OK          301
dmhy.xml                                    NXDOMAIN/NXDOMAIN    000
doc.dandanplay.com                          OK/OK          200
doujin.bgm.tv                               OK/OK          200
e.e-muse.com                                OK/OK          403
faq.b-ch.com                                OK/OK          200
fast.bgm.tv                                 OK/OK          301
girigirilove.top                            NXDOMAIN/NXDOMAIN    000
gnn.gamer.com.tw                            OK/OK          200
graphql.anilist.co                          OK/OK          404
guest.freeanimehentai.net                   OK/OK          403
help.crunchyroll.com                        OK/OK          200
home.gamer.com.tw                           OK/OK          000
i.fod.fujitv.co.jp                          OK/OK          403
i2.bahamut.com.tw                           OK/OK          200
id.hulu.jp                                  OK/OK          000
image2.b-ch.com                             OK/OK          200
images.prod.hjholdings.tv                   OK/OK          404
img.alicdn.com                              OK/OK          404
img.cdn.nimg.jp                             OK/OK          404
img.hentaihaven.xxx                         OK/OK          200
img1.hulu.com                               OK/OK          404
img2.hulu.com                               OK/OK          404
img4.hulu.com                               OK/OK          404
imgsrv.crunchyroll.com                      OK/OK          404
info.b-ch.com                               OK/OK          200
js.tv.itc.cn                                OK/OK          403
lain.bgm.tv                                 OK/OK          404
litvfreemobile-hichannel.cdn.hinet.net      S2/NXDOMAIN    000
live.acfun.cn                               OK/OK          200
live.bilibili.com                           OK/OK          200
m.bilibili.com                              OK/OK          302
m.iqiyipic.com                              OK/OK          404
m10.iyf.tv                                  OK/OK          403
mall.e-muse.com.tw                          OK/OK          200
mapi.prod.hjholdings.tv                     OK/OK          403
mesh.if.iqiyi.com                           OK/OK          200
metax.api.matchpoint.tv                     OK/OK          404
mhfm1tel.cdndm5.com                         OK/OK          403
mhfm2tel.cdndm5.com                         OK/OK          403
mhfm3tel.cdndm5.com                         OK/OK          403
mhfm5tel.cdndm5.com                         OK/OK          403
mhfm7tel.cdndm5.com                         OK/OK          403
mhfm9tel.cdndm5.com                         OK/OK          403
mub.acgdm001.com                            OK/OK          403
news.hulu.jp                                OK/OK          200
nikedm.com                                  NXDOMAIN/NXDOMAIN    000
nvapi.nicovideo.jp                          OK/OK          404
nyaa.xml                                    NXDOMAIN/NXDOMAIN    000
p-cdnstatic.svc.litv.tv                     OK/OK          404
p.bstarstatic.com                           OK/OK          403
p1.bstarstatic.com                          OK/OK          403
p2.bahamut.com.tw                           OK/OK          200
papi.prod.hjholdings.tv                     OK/OK          403
passport.bilibili.tv                        OK/OK          404
passport.migu.cn                            OK/OK          200
pcw-api.iq.com                              OK/OK          200
pic.bstarstatic.com                         OK/OK          403
pic0.iqiyipic.com                           OK/OK          404
pic1.bstarstatic.com                        OK/OK          403
pic2.iqiyipic.com                           OK/OK          404
pic3.iqiyipic.com                           OK/OK          404
pic4.iqiyipic.com                           OK/OK          404
pic7.iqiyipic.com                           OK/OK          404
pic9.iqiyipic.com                           OK/OK          403
playback.prod.hjholdings.tv                 OK/OK          404
premium.nicovideo.jp                        OK/OK          403
promo.mytvsuper.com                         OK/OK          301
rankv21.iyf.tv                              OK/OK          403
ref.gamer.com.tw                            OK/OK          302
res.nimg.jp                                 OK/OK          301
s1.bstarstatic.com                          OK/OK          403
s3.happyon.jp                               OK/OK          403
s4.anilist.co                               OK/OK          301
search.gamer.com.tw                         OK/OK          200
search.nicovideo.jp                         OK/NO_A        000
search.video.iqiyi.com                      OK/OK          302
secure.hulu.com                             OK/OK          301
seiga.nicovideo.jp                          OK/OK          301
share.acgnx.se                              OK/OK          403
share.dmhy.org                              OK/OK          200
signup.hulu.com                             OK/OK          200
site.nicovideo.jp                           OK/OK          404
so.iqiyi.com                                OK/OK          200
sp.nicovideo.jp                             OK/OK          302
space.bilibili.com                          OK/OK          302
sso.crunchyroll.com                         OK/OK          308
static.bangumi.moe                          OK/OK          200
static.crunchyroll.com                      OK/OK          502
static.iqiyi.com                            OK/OK          404
static.yximgs.com                           OK/OK          416
stc.iqiyipic.com                            OK/OK          403
stream.animeparadise.moe                    OK/OK          404
sukebei.nyaa.si                             OK/OK          200
sukebei.xml                                 NXDOMAIN/NXDOMAIN    000
tag-api.i3.dmm.com                          OK/OK          404
tb.mgtv.com                                 OK/OK          404
token.prod.hjholdings.tv                    OK/OK          404
truth.bahamut.com.tw                        OK/OK          200
tv.dmm.com                                  OK/OK          301
tv.sohu.com                                 OK/OK          200
tx-free-imgs.acfun.cn                       OK/OK          200
u0.iqiyipic.com                             OK/OK          404
u1.iqiyipic.com                             OK/OK          404
u2.dmhy.org                                 OK/OK          302
u3.iqiyipic.com                             OK/OK          404
u4.iqiyipic.com                             OK/OK          404
u5.iqiyipic.com                             OK/OK          404
u6.iqiyipic.com                             OK/OK          403
u7.iqiyipic.com                             OK/OK          404
u8.iqiyipic.com                             OK/OK          403
u9.iqiyipic.com                             OK/OK          403
upos-sz-mirrorcos.bilivideo.com             OK/OK          403
user.gamer.com.tw                           OK/OK          200
v.anime1.me                                 OK/OK          403
video-static.unext.jp                       OK/OK          404
video.nicovideo.jp                          OK/NO_A        000
video.nimg.jp                               NO_A/NO_A        000
video.unext.jp                              OK/OK          h301
vww.monoschinos2.net                        OK/OK          200
wall.gamer.com.tw                           OK/OK          302
wktk.nimg.jp                                OK/OK          200
wwv.monoschinos2.net                        OK/OK          301
www.5dm.dev                                 OK/OK          403
www.abema.tv                                NXDOMAIN/NXDOMAIN    000
www.acfun.cn                                OK/OK          200
www.acg.rip                                 OK/OK          h404
www.acgnx.se                                OK/OK          403
www.agedm.io                                OK/OK          403
www.anibk.com                               OK/OK          200
www.animegg.org                             OK/OK          200
www.animenewsnetwork.com                    OK/OK          200
www.animetimes.co.jp                        OK/OK          200
www.b-ch.com                                OK/OK          200
www.bangumi.moe                             OK/OK          200
www.bilibili.com                            OK/OK          200
www.bilibili.tv                             OK/OK          200
www.biliintl.com                            OK/OK          301
www.cbhtv.top                               OK/OK          200
www.ccytv.cc                                OK/OK          200
www.crunchyroll.com                         OK/OK          301
www.cycani.org                              OK/OK          403
www.cycanime.com                            OK/OK          302
www.cycdm01.top                             OK/OK          302
www.cycity.pro                              OK/OK          200
www.dandanplay.com                          OK/OK          200
www.dandanplay.net                          OK/OK          302
www.dilidili51.com                          OK/OK          301
www.dlidli.app                              OK/OK          200
www.dm5.com                                 OK/OK          200
www.dm530.org                               OK/OK          301
www.dmhy.org                                OK/OK          200
www.dmm.com                                 OK/OK          200
www.dmmandao.com.cn                         OK/OK          200
www.e-muse.com                              OK/OK          403
www.fantuantv.com                           OK/OK          200
www.fcdmtv.cc                               OK/OK          200
www.gamer.com.tw                            OK/OK          200
www.girigiri.cn                             NXDOMAIN/NXDOMAIN    000
www.girigirilove.com                        OK/OK          301
www.gugu3.com                               OK/OK          200
www.hacg.me                                 OK/OK          200
www.hidive.com                              OK/OK          200
www.hjtv5.cc                                OK/OK          200
www.hjwtv.cc                                OK/OK          200
www.hulu.com                                OK/OK          301
www.hulu.jp                                 OK/OK          200
www.iq.com                                  OK/OK          200
www.iqiyi.com                               OK/OK          200
www.iqiyipic.com                            OK/OK          404
www.iyf.tv                                  OK/OK          403
www.kfmax.com                               OK/OK          302
www.le.com                                  OK/OK          200
www.letv.com                                OK/OK          200
www.lightnovel.cn                           OK/OK          301
www.lightnovel.fun                          OK/OK          200
www.litv.tv                                 OK/OK          200
www.medialink.com.hk                        OK/OK          200
www.mgtv.com                                OK/OK          200
www.midnightpulp.com                        OK/OK          200
www.migu.cn                                 OK/OK          200
www.miguvideo.com                           OK/OK          200
www.mjtt2.cc                                OK/OK          200
www.mytvsuper.com                           OK/OK          308
www.nicovideo.jp                            OK/OK          200
www.omofuns.com                             OK/OK          200
www.popgo.org                               OK/OK          200
www.pptv.com                                OK/OK          200
www.qudman.com.cn                           OK/OK          200
www.retrocrush.tv                           OK/OK          200
www.sumisora.net                            OK/OK          200
www.telasa.jp                               OK/OK          301
www.tsdm39.com                              OK/OK          200
www.ttiandman.com.cn                        OK/OK          200
www.tvtfun.net                              OK/OK          200
www.vcb-s.com                               OK/OK          403
www.video.unext.jp                          OK/OK          307
www.viu.com                                 OK/OK          302
www.viu.tv                                  OK/OK          301
www.wetv.vip                                OK/OK          302
www.xifan.moe                               NXDOMAIN/NXDOMAIN    000
www3.animeflv.net                           OK/OK          h301

```

## 7. 已失效 / 勿收录域名汇总

下表汇总各节的「已失效 / 停放 / 劫持 / 仿冒 / 勿收录」域名（每条都有证据，主要来自 **EverythingMoe 墓地**、站点停放页自报、以及本次 DoH/HTTPS 实测）。**不要写进分流规则**；已收录的要清理。

**2026 年的大变化：英文聚合站成批阵亡** —— HiAnime / AniWatch / Zoro、AniWave（9anime 后继）、AnimeKai、Gogoanime 家族、KissAnime 全部关停或变成停放页；主流名单已换成 `aniwaves.ru` / `hianimes.ru`（FMHY 现役收录）。

| 域名 | 状态与备注 |
|---|---|
| 2dgal.com | 已失效/勿收录（证据见正文表格） |
| 36dm.club | 已失效/勿收录（证据见正文表格） |
| 36dm.com | 已失效/勿收录（证据见正文表格） |
| 36dm.net | 已失效/勿收录（证据见正文表格） |
| acgnx.club | 已失效/勿收录（证据见正文表格） |
| acgnx.eu | 已失效/勿收录（证据见正文表格） |
| acgnx.net | 已失效/勿收录（证据见正文表格） |
| acgnx.pro | 已失效/勿收录（证据见正文表格） |
| acgnx.top | 已失效/勿收录（证据见正文表格） |
| acgnx.xyz | 已失效/勿收录（证据见正文表格） |
| acgrip.com | 已失效/勿收录（证据见正文表格） |
| agg.md | txt 注释标注失效/停放（见正文） |
| anime-times.jp | txt 注释标注失效/停放（见正文） |
| anime4up.tv | txt 注释标注失效/停放（见正文） |
| animedao.to | 已失效/勿收录（证据见正文表格） |
| animefox.io | 已失效/勿收录（证据见正文表格） |
| animekai.to | txt 注释标注失效/停放（见正文） |
| animekisa.tv | 已失效/勿收录（证据见正文表格） |
| animelab.com | 旧平台已停运（2021 并入 Funimation） |
| animeskip.io | 已失效/勿收录（证据见正文表格） |
| anitaku.bz | 已失效/勿收录（证据见正文表格） |
| anitaku.pe | 已失效/勿收录（证据见正文表格） |
| anitaku.to | 已失效/勿收录（证据见正文表格） |
| aniwatch.to | 已失效/勿收录（证据见正文表格） |
| aniwatchtv.to | txt 注释标注失效/停放（见正文） |
| aniwave.live | 已失效/勿收录（证据见正文表格） |
| aniwave.to | 已失效/勿收录（证据见正文表格） |
| anix.me | txt 注释标注失效/停放（见正文） |
| ayakawa.moe | 已失效/勿收录（证据见正文表格） |
| cn.nyaa.net | 已失效/勿收录（证据见正文表格） |
| dm519.fans | txt 注释标注失效/停放（见正文） |
| dm530.com | txt 注释标注失效/停放（见正文） |
| dm530w.org | txt 注释标注失效/停放（见正文） |
| dmhy.b168.net | 已失效/勿收录（证据见正文表格） |
| dmhy.gate.flag.moe | 已失效/勿收录（证据见正文表格） |
| dmhy.ye1213.com | 已失效/勿收录（证据见正文表格） |
| dmla.fans | txt 注释标注失效/停放（见正文） |
| dmzj.com | 动漫之家 2025-09 停运（apex 仅域名保护，无内容） |
| funimation.com | 2024 并入 Crunchyroll，旧域停用 |
| gogo-load.com | 已失效/勿收录（证据见正文表格） |
| gogoanime.vc | 已失效/勿收录（证据见正文表格） |
| gogoanime3.co | 已失效/勿收录（证据见正文表格） |
| gogocdn.net | 已失效/勿收录（证据见正文表格） |
| gyao.yahoo.co.jp | GYAO! 2023-03 停运 |
| hanime1.one | txt 注释标注失效/停放（见正文） |
| hanime1.org | txt 注释标注失效/停放（见正文） |
| hanime1.pw | txt 注释标注失效/停放（见正文） |
| hentaidude.com | txt 注释标注失效/停放（见正文） |
| hentaidude.net | txt 注释标注失效/停放（见正文） |
| hentaidude.to | txt 注释标注失效/停放（见正文）；实测无解析（NXDOMAIN） |
| hentaihaven.org | txt 注释标注失效/停放（见正文） |
| hianime.to | 已失效/勿收录（证据见正文表格） |
| huameng.net | 已失效/勿收录（证据见正文表格） |
| jysub.com | 已失效/勿收录（证据见正文表格） |
| jysub.net | 已失效/勿收录（证据见正文表格） |
| jysub.org | 已失效/勿收录（证据见正文表格） |
| kaido.to | 已失效/勿收录（证据见正文表格） |
| kitauji.net | 已失效/勿收录（证据见正文表格） |
| lightnovel.us | 已失效/勿收录（证据见正文表格） |
| lknovel.cn | 已失效/勿收录（证据见正文表格） |
| loli.house | 已失效/勿收录（证据见正文表格） |
| lolihouse.cafe | 已失效/勿收录（证据见正文表格） |
| mikanani.tv | 已失效/勿收录（证据见正文表格） |
| moonsub.org | 已失效/勿收录（证据见正文表格） |
| nyaa.eu | 已失效/勿收录（证据见正文表格） |
| nyaa.net | 已失效/勿收录（证据见正文表格） |
| nyaa.se | txt 注释标注失效/停放（见正文） |
| paravi.jp | 2023 并入 U-NEXT，旧域停用 |
| popgo.net | 已失效/勿收录（证据见正文表格） |
| saku.rip | 已失效/勿收录（证据见正文表格） |
| sakurato.com | 已失效/勿收录（证据见正文表格） |
| sakurato.moe | 已失效/勿收录（证据见正文表格） |
| sakurato.net | 已失效/勿收录（证据见正文表格） |
| sccqygs.com | 已失效/勿收录（证据见正文表格） |
| shikimori.me | 已失效/勿收录（证据见正文表格） |
| sub.jysub.net | 已失效/勿收录（证据见正文表格） |
| sumisora.org | 已失效/勿收录（证据见正文表格） |
| sweet-sub.com | 已失效/勿收录（证据见正文表格） |
| tsdm.live | 已失效/勿收录（证据见正文表格） |
| tsdm.love | 已失效/勿收录（证据见正文表格） |
| tsdm39.net | 已失效/勿收录（证据见正文表格） |
| tsdm39.org | 已失效/勿收录（证据见正文表格） |
| uha-c9.com | 已失效/勿收录（证据见正文表格） |
| v.vrv.co | txt 注释标注失效/停放（见正文） |
| vrv.co | VRV 2023 停运 |
| wakanim.tv | 并入 Crunchyroll，旧域停用 |
| ww38.aniwave.to | 已失效/勿收录（证据见正文表格） |
| www.36dm.com | 已失效/勿收录（证据见正文表格） |
| www.lightnovel.us | 已失效/勿收录（证据见正文表格） |
| www.lknovel.cn | 已失效/勿收录（证据见正文表格） |
| www.loli.house | 已失效/勿收录（证据见正文表格） |
| www.popgo.net | 已失效/勿收录（证据见正文表格） |
| www.sumisora.org | 已失效/勿收录（证据见正文表格） |
| www.tsdm.live | 已失效/勿收录（证据见正文表格） |
| www.tsdm39.net | 已失效/勿收录（证据见正文表格） |
| www.tsdm39.org | 已失效/勿收录（证据见正文表格） |
| yhdmp.net | txt 注释标注失效/停放（见正文） |
| zoro.to | 已失效/勿收录（证据见正文表格） |
| zzzfun.one | 实测 200 但为 parklogic 停放页（站点已弃用该域） |

另有两个易混域名提醒：`bangumi.moe`（种子站）≠ `bgm.tv`（评分社区，已被墙）；`mikanime.tv`（蜜柑国内入口，有效）≠ `mikanani.tv`（少一个 e，是错域名，见上表）。

**实测双解析器均无解析、已从 §8 清单剔除的域名**（可能是已废弃或仅特定地区解析的主机名，建议不要收）：
- `btrace.wetvinfo.com`
- `girigirilove.top`
- `nikedm.com`
- `www.xifan.moe`

## 8. 附录：国内直连 / 海外代理 域名清单

以下清单由本文全部域名自动生成（已剔除失效域名并做子域合并），按「用国内网络能否直接访问」拆分：

**国内直连 74 条 ｜ 海外代理 436 条（其中 74 条属「代理·存疑」）｜ 其中 9 条需走「非日本节点」**。

### 8.1 国内直连

```yaml
DOMAIN-SUFFIX,2fp-cdnstatic.svc.litv.tv
DOMAIN-SUFFIX,a1.itc.cn
DOMAIN-SUFFIX,account.youku.com
DOMAIN-SUFFIX,acfun.cn
DOMAIN-SUFFIX,acg.youku.com
DOMAIN-SUFFIX,api.bilibili.com
DOMAIN-SUFFIX,api.dandanplay.net
DOMAIN-SUFFIX,assets.anixplayer.net
DOMAIN-SUFFIX,b23.tv
DOMAIN-SUFFIX,bangumi.bilibili.com
DOMAIN-SUFFIX,bilibili.com
DOMAIN-SUFFIX,bilivideo.com
DOMAIN-SUFFIX,cache-video.iq.com
DOMAIN-SUFFIX,cache.video.iqiyi.com
DOMAIN-SUFFIX,cartoon.aplus.pptv.com
DOMAIN-SUFFIX,css.tv.itc.cn
DOMAIN-SUFFIX,dandanplay.com
DOMAIN-SUFFIX,dandanplay.net
DOMAIN-SUFFIX,display-sc.miguvideo.com
DOMAIN-SUFFIX,film.qq.com
DOMAIN-SUFFIX,fino.svc.litv.tv
DOMAIN-SUFFIX,honey.mgtv.com
DOMAIN-SUFFIX,i0.hdslb.com
DOMAIN-SUFFIX,i1.hdslb.com
DOMAIN-SUFFIX,i2.hdslb.com
DOMAIN-SUFFIX,i3.itc.cn
DOMAIN-SUFFIX,img.cmvideo.cn
DOMAIN-SUFFIX,img.mgtv.com
DOMAIN-SUFFIX,img7.iqiyipic.com
DOMAIN-SUFFIX,imgs.aixifan.com
DOMAIN-SUFFIX,intl-api.iq.com
DOMAIN-SUFFIX,intl-help.iq.com
DOMAIN-SUFFIX,iq.com
DOMAIN-SUFFIX,iqiyi.com
DOMAIN-SUFFIX,iqiyipic.com
DOMAIN-SUFFIX,itc.cn
DOMAIN-SUFFIX,le.com
DOMAIN-SUFFIX,letv.com
DOMAIN-SUFFIX,liangcang-material.alicdn.com
DOMAIN-SUFFIX,litv.tv
DOMAIN-SUFFIX,m.miguvideo.com
DOMAIN-SUFFIX,m.ykimg.com
DOMAIN-SUFFIX,m.youku.tv
DOMAIN-SUFFIX,mgtv.com
DOMAIN-SUFFIX,migu.cn
DOMAIN-SUFFIX,migudm.cn
DOMAIN-SUFFIX,miguvideo.com
DOMAIN-SUFFIX,mikanime.tv
DOMAIN-SUFFIX,msg-intl.qy.net
DOMAIN-SUFFIX,my.tv.sohu.com
DOMAIN-SUFFIX,pptv.com
DOMAIN-SUFFIX,puui.qpic.cn
DOMAIN-SUFFIX,qy.net
DOMAIN-SUFFIX,s1.hdslb.com
DOMAIN-SUFFIX,so.youku.com
DOMAIN-SUFFIX,sohu.com
DOMAIN-SUFFIX,static.hitv.com
DOMAIN-SUFFIX,static.wetvinfo.com
DOMAIN-SUFFIX,t.youku.com
DOMAIN-SUFFIX,v.qq.com
DOMAIN-SUFFIX,v.youku.com
DOMAIN-SUFFIX,vfiles.gtimg.cn
DOMAIN-SUFFIX,videohy.tc.qq.com
DOMAIN-SUFFIX,vliveachy.tc.qq.com
DOMAIN-SUFFIX,vm.gtimg.cn
DOMAIN-SUFFIX,vv.video.qq.com
DOMAIN-SUFFIX,wapx.cmvideo.cn
DOMAIN-SUFFIX,wetv.vip
DOMAIN-SUFFIX,wetvinfo.com
DOMAIN-SUFFIX,www.youku.com
DOMAIN-SUFFIX,www.youku.tv
DOMAIN-SUFFIX,ykimg.alicdn.com
DOMAIN-SUFFIX,youku.com
DOMAIN-SUFFIX,youku.tv
```

### 8.2 海外代理

```yaml
DOMAIN-SUFFIX,123animehub.cc
DOMAIN-SUFFIX,141jj.com
DOMAIN-SUFFIX,1497203185.rsc.cdn77.org
DOMAIN-SUFFIX,1ani.me
DOMAIN-SUFFIX,5dm.dev
DOMAIN-SUFFIX,999hentai.com
DOMAIN-SUFFIX,999hentai.net
DOMAIN-SUFFIX,9animstv.to
DOMAIN-SUFFIX,abema.tv
DOMAIN-SUFFIX,account.nicovideo.jp
DOMAIN-SUFFIX,account.unext.jp
DOMAIN-SUFFIX,acg.gamer.com.tw
DOMAIN-SUFFIX,acg.rip
DOMAIN-SUFFIX,acgdm001.com
DOMAIN-SUFFIX,acgnx.se
DOMAIN-SUFFIX,aeoncinema-video.unext.jp
DOMAIN-SUFFIX,aestheticode.net
DOMAIN-SUFFIX,age.tv
DOMAIN-SUFFIX,ageapp.app
DOMAIN-SUFFIX,agedm.com
DOMAIN-SUFFIX,agedm.io
DOMAIN-SUFFIX,agedm.live
DOMAIN-SUFFIX,agedm.me
DOMAIN-SUFFIX,agedm.org
DOMAIN-SUFFIX,agedm.vip
DOMAIN-SUFFIX,agefans.com
DOMAIN-SUFFIX,agefans.la
DOMAIN-SUFFIX,akuma.moe
DOMAIN-SUFFIX,allmanga.to
DOMAIN-SUFFIX,ani.baha.tw
DOMAIN-SUFFIX,ani.gamer.com.tw
DOMAIN-SUFFIX,ani.girigirilove.com
DOMAIN-SUFFIX,ani.pm
DOMAIN-SUFFIX,anibk.com
DOMAIN-SUFFIX,anichan.to
DOMAIN-SUFFIX,anichi.to
DOMAIN-SUFFIX,aniclipse.com
DOMAIN-SUFFIX,anidap.lol
DOMAIN-SUFFIX,anidex.info
DOMAIN-SUFFIX,anidoor.me
DOMAIN-SUFFIX,anifun.cn
DOMAIN-SUFFIX,anify.to
DOMAIN-SUFFIX,anihq.cc
DOMAIN-SUFFIX,anikage.cc
DOMAIN-SUFFIX,anikoto.cz
DOMAIN-SUFFIX,anikoto.me
DOMAIN-SUFFIX,anikoto.net
DOMAIN-SUFFIX,anikoto.site
DOMAIN-SUFFIX,anikototv.se
DOMAIN-SUFFIX,anikototv.to
DOMAIN-SUFFIX,anikura.club
DOMAIN-SUFFIX,anikuro.ru
DOMAIN-SUFFIX,anikuro.site
DOMAIN-SUFFIX,anikuro.to
DOMAIN-SUFFIX,anilight.live
DOMAIN-SUFFIX,anilist.co
DOMAIN-SUFFIX,anime-jl.net
DOMAIN-SUFFIX,anime.girigirilove.com
DOMAIN-SUFFIX,anime.nexus
DOMAIN-SUFFIX,anime.nicovideo.jp
DOMAIN-SUFFIX,anime1.me
DOMAIN-SUFFIX,animeav1.com
DOMAIN-SUFFIX,animedex.fun
DOMAIN-SUFFIX,animefenix2.tv
DOMAIN-SUFFIX,animefesta.iowl.jp
DOMAIN-SUFFIX,animeflv.net
DOMAIN-SUFFIX,animegg.org
DOMAIN-SUFFIX,animehodai.jp
DOMAIN-SUFFIX,animeid.tv
DOMAIN-SUFFIX,animeidhentai.com
DOMAIN-SUFFIX,animemars.org
DOMAIN-SUFFIX,animenewsnetwork.com
DOMAIN-SUFFIX,animenosub.to
DOMAIN-SUFFIX,animeonsen.xyz
DOMAIN-SUFFIX,animepahe.com
DOMAIN-SUFFIX,animepahe.org
DOMAIN-SUFFIX,animepahe.pw
DOMAIN-SUFFIX,animepahe.su
DOMAIN-SUFFIX,animeparadise.moe
DOMAIN-SUFFIX,animesaturn.cx
DOMAIN-SUFFIX,animesaturn.net
DOMAIN-SUFFIX,animestore.docomo.ne.jp
DOMAIN-SUFFIX,animesuge.bid
DOMAIN-SUFFIX,animesuge.cz
DOMAIN-SUFFIX,animesuge.re
DOMAIN-SUFFIX,animesugez.tv
DOMAIN-SUFFIX,animetake.tv
DOMAIN-SUFFIX,animetimes-store.com
DOMAIN-SUFFIX,animetimes.co.jp
DOMAIN-SUFFIX,animeunity.so
DOMAIN-SUFFIX,animeunity.to
DOMAIN-SUFFIX,animewave.to
DOMAIN-SUFFIX,animeworld.ac
DOMAIN-SUFFIX,animex.one
DOMAIN-SUFFIX,aninami.site
DOMAIN-SUFFIX,anisaturn.com
DOMAIN-SUFFIX,anisnatch.site
DOMAIN-SUFFIX,anisnatch.top
DOMAIN-SUFFIX,anistream.one
DOMAIN-SUFFIX,anisuge.se
DOMAIN-SUFFIX,anisuge.tv
DOMAIN-SUFFIX,aniwatch.rest
DOMAIN-SUFFIX,aniwave.cz
DOMAIN-SUFFIX,aniwaves.ru
DOMAIN-SUFFIX,anizone.to
DOMAIN-SUFFIX,api-cdn.myanimelist.net
DOMAIN-SUFFIX,api-gateway-global.viu.com
DOMAIN-SUFFIX,api-videopass-sockets.kddi-video.com
DOMAIN-SUFFIX,api-videopass.kddi-video.com
DOMAIN-SUFFIX,api.abema.io
DOMAIN-SUFFIX,api.bgm.tv
DOMAIN-SUFFIX,api.bilibili.tv
DOMAIN-SUFFIX,api.lightnovel.fun
DOMAIN-SUFFIX,api.myanimelist.net
DOMAIN-SUFFIX,api.trace.moe
DOMAIN-SUFFIX,app.xifandm.net
DOMAIN-SUFFIX,apps.fengctv.com.cn
DOMAIN-SUFFIX,asiancrush.com
DOMAIN-SUFFIX,assets.b-ch.com
DOMAIN-SUFFIX,assets.mytvsuper.com
DOMAIN-SUFFIX,auth.hanime.tv
DOMAIN-SUFFIX,auth.hulu.com
DOMAIN-SUFFIX,avatar2.bahamut.com.tw
DOMAIN-SUFFIX,awsimgsrc.dmm.com
DOMAIN-SUFFIX,b-ch.com
DOMAIN-SUFFIX,babyanime.top
DOMAIN-SUFFIX,bahamut.akamaized.net
DOMAIN-SUFFIX,bahamut.com.tw
DOMAIN-SUFFIX,bangumi.moe
DOMAIN-SUFFIX,bangumi.tv
DOMAIN-SUFFIX,banime.top
DOMAIN-SUFFIX,bbs.acgrip.com
DOMAIN-SUFFIX,bbs.dmhy.org
DOMAIN-SUFFIX,bbs.kfmax.com
DOMAIN-SUFFIX,bbs.popgo.org
DOMAIN-SUFFIX,bbs.sumisora.net
DOMAIN-SUFFIX,beacon.unext.jp
DOMAIN-SUFFIX,bees.streaks.jp
DOMAIN-SUFFIX,bestdubbedanime.com
DOMAIN-SUFFIX,beta.crunchyroll.com
DOMAIN-SUFFIX,bgm.tv
DOMAIN-SUFFIX,bilibili.tv
DOMAIN-SUFFIX,biliintl.com
DOMAIN-SUFFIX,bstarstatic.com
DOMAIN-SUFFIX,buy.gamer.com.tw
DOMAIN-SUFFIX,cbhtv.top
DOMAIN-SUFFIX,cc.unext.jp
DOMAIN-SUFFIX,ccytv.cc
DOMAIN-SUFFIX,cdn.matchpoint.tv
DOMAIN-SUFFIX,cdn.myanimelist.net
DOMAIN-SUFFIX,cdn.nimg.jp
DOMAIN-SUFFIX,cdn.vidcloud.se
DOMAIN-SUFFIX,cdn.videopass.jp
DOMAIN-SUFFIX,cdnr-octopus.hhpanel.org
DOMAIN-SUFFIX,ch.nicovideo.jp
DOMAIN-SUFFIX,chii.in
DOMAIN-SUFFIX,cinemacoupon.unext.jp
DOMAIN-SUFFIX,cms.hentaihaven.xxx
DOMAIN-SUFFIX,cn-yinghuadm.com.cn
DOMAIN-SUFFIX,cn-yinghuadman.com.cn
DOMAIN-SUFFIX,comic.iowl.jp
DOMAIN-SUFFIX,conf.lemino.docomo.ne.jp
DOMAIN-SUFFIX,contact.unext.jp
DOMAIN-SUFFIX,content-images.onvesper.com
DOMAIN-SUFFIX,coupon.unext.jp
DOMAIN-SUFFIX,coverlanyvd.org
DOMAIN-SUFFIX,cr-play-service.prd.crunchyrollsvc.com
DOMAIN-SUFFIX,crunchyroll.com
DOMAIN-SUFFIX,crunchyrollexpo.com
DOMAIN-SUFFIX,crunchyrollsvc.com
DOMAIN-SUFFIX,ct.hanime.tv
DOMAIN-SUFFIX,cyc-anime.net
DOMAIN-SUFFIX,cycani.org
DOMAIN-SUFFIX,cycanime.com
DOMAIN-SUFFIX,cycdm01.top
DOMAIN-SUFFIX,cycity.pro
DOMAIN-SUFFIX,d1zquzjgwo9yb.cloudfront.net
DOMAIN-SUFFIX,d2anahhhmp1ffz.cloudfront.net
DOMAIN-SUFFIX,daradara.me
DOMAIN-SUFFIX,dce-frontoffice.imggaming.com
DOMAIN-SUFFIX,dic.nicovideo.jp
DOMAIN-SUFFIX,dilidili51.com
DOMAIN-SUFFIX,dlidli.app
DOMAIN-SUFFIX,dm.xifanacg.com
DOMAIN-SUFFIX,dm530.in
DOMAIN-SUFFIX,dm530.org
DOMAIN-SUFFIX,dm530w6.com
DOMAIN-SUFFIX,dmhy.anoneko.com
DOMAIN-SUFFIX,dmhy.org
DOMAIN-SUFFIX,dmm.com
DOMAIN-SUFFIX,dmmandao.com.cn
DOMAIN-SUFFIX,dongmanhuayuan.myheartsite.com
DOMAIN-SUFFIX,e-muse.com
DOMAIN-SUFFIX,e-muse.com.tw
DOMAIN-SUFFIX,e.kortw.cc
DOMAIN-SUFFIX,edge-api.hulu.com
DOMAIN-SUFFIX,embed.nicovideo.jp
DOMAIN-SUFFIX,enc-dec.app
DOMAIN-SUFFIX,enma.lol
DOMAIN-SUFFIX,fantuantv.com
DOMAIN-SUFFIX,fcbbcc.com
DOMAIN-SUFFIX,fcdm22.com
DOMAIN-SUFFIX,fcdmtv.cc
DOMAIN-SUFFIX,fengchedm.cc
DOMAIN-SUFFIX,fengchedm.com
DOMAIN-SUFFIX,fireani.me
DOMAIN-SUFFIX,flixcloud.cc
DOMAIN-SUFFIX,fod.fujitv.co.jp
DOMAIN-SUFFIX,forum.gamer.com.tw
DOMAIN-SUFFIX,freeanimehentai.net
DOMAIN-SUFFIX,gamer-cds.cdn.hinet.net
DOMAIN-SUFFIX,gamer.com.tw
DOMAIN-SUFFIX,gamer2-cds.cdn.hinet.net
DOMAIN-SUFFIX,girigiri.cn
DOMAIN-SUFFIX,girigirilove.com
DOMAIN-SUFFIX,gugu3.com
DOMAIN-SUFFIX,hacg.casa
DOMAIN-SUFFIX,hacg.la
DOMAIN-SUFFIX,hacg.me
DOMAIN-SUFFIX,hacg.zip
DOMAIN-SUFFIX,hacg8.com
DOMAIN-SUFFIX,hanime-cdn.com
DOMAIN-SUFFIX,hanime.io
DOMAIN-SUFFIX,hanime.tv
DOMAIN-SUFFIX,hanime1.com
DOMAIN-SUFFIX,hanime1.me
DOMAIN-SUFFIX,hanimeone.me
DOMAIN-SUFFIX,happyon.jp
DOMAIN-SUFFIX,help.hulu.jp
DOMAIN-SUFFIX,help.telasa.jp
DOMAIN-SUFFIX,help.unext.jp
DOMAIN-SUFFIX,hentai.tv
DOMAIN-SUFFIX,hentaihaven.app
DOMAIN-SUFFIX,hentaihaven.com
DOMAIN-SUFFIX,hentaihaven.red
DOMAIN-SUFFIX,hentaihaven.xxx
DOMAIN-SUFFIX,hentaimama.io
DOMAIN-SUFFIX,hentaistream.moe
DOMAIN-SUFFIX,hexa.su
DOMAIN-SUFFIX,hianimes.ru
DOMAIN-SUFFIX,hianimes.se
DOMAIN-SUFFIX,hidive.com
DOMAIN-SUFFIX,hjholdings.tv
DOMAIN-SUFFIX,hjtv5.cc
DOMAIN-SUFFIX,hjwtv.cc
DOMAIN-SUFFIX,home.hulu.com
DOMAIN-SUFFIX,hstream.moe
DOMAIN-SUFFIX,hulu.com
DOMAIN-SUFFIX,hulu.jp
DOMAIN-SUFFIX,huluim.com
DOMAIN-SUFFIX,id.smt.docomo.ne.jp
DOMAIN-SUFFIX,if.lemino.docomo.ne.jp
DOMAIN-SUFFIX,image-cf.kddi-video.com
DOMAIN-SUFFIX,img.anili.st
DOMAIN-SUFFIX,img.lzipic.com
DOMAIN-SUFFIX,img.picbf.com
DOMAIN-SUFFIX,img.tsdm39.com
DOMAIN-SUFFIX,img.tsdm39.net
DOMAIN-SUFFIX,img2.xfmanga.top
DOMAIN-SUFFIX,imomoe.ai
DOMAIN-SUFFIX,iyf.tv
DOMAIN-SUFFIX,javchu.com
DOMAIN-SUFFIX,jkanime.net
DOMAIN-SUFFIX,justanime.to
DOMAIN-SUFFIX,kaa.am
DOMAIN-SUFFIX,kaa.lt
DOMAIN-SUFFIX,kaa.to
DOMAIN-SUFFIX,kaas.am
DOMAIN-SUFFIX,kawaiianime.cc
DOMAIN-SUFFIX,kawaiifu.com
DOMAIN-SUFFIX,kazora.cc
DOMAIN-SUFFIX,kfmax.com
DOMAIN-SUFFIX,kimoitv.com
DOMAIN-SUFFIX,kkdm3.com
DOMAIN-SUFFIX,kototv.to
DOMAIN-SUFFIX,kuroiru.co
DOMAIN-SUFFIX,kwik.cx
DOMAIN-SUFFIX,kyren.moe
DOMAIN-SUFFIX,latanime.org
DOMAIN-SUFFIX,lcms-beacon.unext.jp
DOMAIN-SUFFIX,lemino.docomo.ne.jp
DOMAIN-SUFFIX,lf3-data.volccdn.com
DOMAIN-SUFFIX,license.abema.io
DOMAIN-SUFFIX,lightnovel.cn
DOMAIN-SUFFIX,lightnovel.fun
DOMAIN-SUFFIX,linear-abematv.akamaized.net
DOMAIN-SUFFIX,live.nicovideo.jp
DOMAIN-SUFFIX,luffytv.live
DOMAIN-SUFFIX,luffytv.online
DOMAIN-SUFFIX,luna-stream.me
DOMAIN-SUFFIX,lunarx.to
DOMAIN-SUFFIX,m.imageimg.net
DOMAIN-SUFFIX,manifest.streaks.jp
DOMAIN-SUFFIX,matchpoint.tv
DOMAIN-SUFFIX,medialink.com.hk
DOMAIN-SUFFIX,megaplay.buzz
DOMAIN-SUFFIX,meguanime.com
DOMAIN-SUFFIX,midnightpulp.com
DOMAIN-SUFFIX,mikanani.kas.pub
DOMAIN-SUFFIX,mikanani.me
DOMAIN-SUFFIX,miruro.bz
DOMAIN-SUFFIX,miruro.com
DOMAIN-SUFFIX,miruro.cx
DOMAIN-SUFFIX,miruro.to
DOMAIN-SUFFIX,miruro.tv
DOMAIN-SUFFIX,mjtt2.cc
DOMAIN-SUFFIX,mkissa.to
DOMAIN-SUFFIX,mobile.meinadi.cn
DOMAIN-SUFFIX,mobile.unext.jp
DOMAIN-SUFFIX,moeli-desu.com
DOMAIN-SUFFIX,monoschinos2.net
DOMAIN-SUFFIX,myaccount.unext.jp
DOMAIN-SUFFIX,myani.org
DOMAIN-SUFFIX,myanimelist.net
DOMAIN-SUFFIX,mytvsuper.com
DOMAIN-SUFFIX,navi.telasa.jp
DOMAIN-SUFFIX,nekowatch.xyz
DOMAIN-SUFFIX,news.nicovideo.jp
DOMAIN-SUFFIX,next.xifanacg.com
DOMAIN-SUFFIX,nhplayer.com
DOMAIN-SUFFIX,nicoprofile.nimg.jp
DOMAIN-SUFFIX,nicotv.me
DOMAIN-SUFFIX,nicotv.org
DOMAIN-SUFFIX,nicovideo.jp
DOMAIN-SUFFIX,nimg.jp
DOMAIN-SUFFIX,nivod.cc
DOMAIN-SUFFIX,nkdm.hkdrj.cn
DOMAIN-SUFFIX,nyaa.si
DOMAIN-SUFFIX,nyaa.tracker.wf
DOMAIN-SUFFIX,oauth.unext.jp
DOMAIN-SUFFIX,octopusmanifest.org
DOMAIN-SUFFIX,og.bakayaro.live
DOMAIN-SUFFIX,ohentai.org
DOMAIN-SUFFIX,omofuns.com
DOMAIN-SUFFIX,otakuhg.site
DOMAIN-SUFFIX,p-bstarstatic.akamaized.net
DOMAIN-SUFFIX,p.bfvp26.com
DOMAIN-SUFFIX,pahe.win
DOMAIN-SUFFIX,piratexplay.cc
DOMAIN-SUFFIX,piratexplay.com
DOMAIN-SUFFIX,play.dlsite.com
DOMAIN-SUFFIX,players.streaks.jp
DOMAIN-SUFFIX,playmogo.com
DOMAIN-SUFFIX,popgo.org
DOMAIN-SUFFIX,pornbest.org
DOMAIN-SUFFIX,projectjust.xyz
DOMAIN-SUFFIX,qingse.one
DOMAIN-SUFFIX,qlyyz.xyz
DOMAIN-SUFFIX,qudman.com.cn
DOMAIN-SUFFIX,rconf.unext.jp
DOMAIN-SUFFIX,reanime.cz
DOMAIN-SUFFIX,reanime.to
DOMAIN-SUFFIX,reanime.wtf
DOMAIN-SUFFIX,registration.unext.jp
DOMAIN-SUFFIX,reindex.to
DOMAIN-SUFFIX,restatus.me
DOMAIN-SUFFIX,retrocrush.tv
DOMAIN-SUFFIX,s-flow.unext.jp
DOMAIN-SUFFIX,s.vidcloud.se
DOMAIN-SUFFIX,sakusaku.to
DOMAIN-SUFFIX,senshi.to
DOMAIN-SUFFIX,share.acgnx.cc
DOMAIN-SUFFIX,share.acgnx.net
DOMAIN-SUFFIX,shikimori.one
DOMAIN-SUFFIX,sidecar.unext.jp
DOMAIN-SUFFIX,sshs.pw
DOMAIN-SUFFIX,sta.anicdn.com
DOMAIN-SUFFIX,static.diceplatform.com
DOMAIN-SUFFIX,static01.ca.unext.jp
DOMAIN-SUFFIX,streaks.jp
DOMAIN-SUFFIX,stream2.defeated.xxx
DOMAIN-SUFFIX,sub.wyzie.ru
DOMAIN-SUFFIX,suge.to
DOMAIN-SUFFIX,sukebei.tracker.wf
DOMAIN-SUFFIX,sumisora.net
DOMAIN-SUFFIX,support.unext.jp
DOMAIN-SUFFIX,telasa.jp
DOMAIN-SUFFIX,tokuzilla.net
DOMAIN-SUFFIX,tokyotosho.info
DOMAIN-SUFFIX,trace.moe
DOMAIN-SUFFIX,tsdm39.com
DOMAIN-SUFFIX,ttiandman.com.cn
DOMAIN-SUFFIX,tu.ts-dm.net
DOMAIN-SUFFIX,tucaptions.org
DOMAIN-SUFFIX,tvanime.tv
DOMAIN-SUFFIX,tvbanywhere.com
DOMAIN-SUFFIX,tvtfun.net
DOMAIN-SUFFIX,um.viuapi.io
DOMAIN-SUFFIX,unext-info.jp
DOMAIN-SUFFIX,unext.co.jp
DOMAIN-SUFFIX,unext.jp
DOMAIN-SUFFIX,upos-bstar-mirrorakam.akamaized.net
DOMAIN-SUFFIX,upos-bstar1-mirrorakam.akamaized.net
DOMAIN-SUFFIX,vcb-s.com
DOMAIN-SUFFIX,vdownload.hembed.com
DOMAIN-SUFFIX,viu.com
DOMAIN-SUFFIX,viu.tv
DOMAIN-SUFFIX,viuapi.io
DOMAIN-SUFFIX,vivibebe.site
DOMAIN-SUFFIX,vod-abematv.akamaized.net
DOMAIN-SUFFIX,vod-images.onvesper.com
DOMAIN-SUFFIX,wco.tv
DOMAIN-SUFFIX,wcoanimedub.tv
DOMAIN-SUFFIX,wcoanimesub.tv
DOMAIN-SUFFIX,wcoflix.tv
DOMAIN-SUFFIX,wcoforever.com
DOMAIN-SUFFIX,wcoforever.net
DOMAIN-SUFFIX,wcofun.com
DOMAIN-SUFFIX,wcostream.com
DOMAIN-SUFFIX,wcostream.tv
DOMAIN-SUFFIX,www.dlsite.com
DOMAIN-SUFFIX,www.xcytv.cc
DOMAIN-SUFFIX,www.xkytv.cc
DOMAIN-SUFFIX,www.xuandm.com
DOMAIN-SUFFIX,www.yhdmtv.cc
DOMAIN-SUFFIX,www.zbkatv.cc
DOMAIN-SUFFIX,xanime.app
DOMAIN-SUFFIX,xanime.me
DOMAIN-SUFFIX,xcytv.cc
DOMAIN-SUFFIX,xiaoxintv.cc
DOMAIN-SUFFIX,xifan.moe
DOMAIN-SUFFIX,xifanacg.com
DOMAIN-SUFFIX,xkytv.cc
DOMAIN-SUFFIX,xuandm.com
DOMAIN-SUFFIX,yenime.net
DOMAIN-SUFFIX,yhdm.la
DOMAIN-SUFFIX,yhdm.so
DOMAIN-SUFFIX,yhdmtv.cc
DOMAIN-SUFFIX,yhpdm.net
DOMAIN-SUFFIX,yinghuacd.com
DOMAIN-SUFFIX,yinghuafanju.com.cn
DOMAIN-SUFFIX,yomi.to
DOMAIN-SUFFIX,ytanime.tv
DOMAIN-SUFFIX,zbkatv.cc
DOMAIN-SUFFIX,zzzfun.com
DOMAIN-SUFFIX,zzzfun.org
```

### 8.3 「代理·存疑」子集（默认按代理放；大陆实测直连可用的话挪到 8.1）

```yaml
DOMAIN-SUFFIX,dmmandao.com.cn
DOMAIN-SUFFIX,p.bfvp26.com
DOMAIN-SUFFIX,bbs.popgo.org
DOMAIN-SUFFIX,cn-yinghuadm.com.cn
DOMAIN-SUFFIX,dm530.in
DOMAIN-SUFFIX,anibk.com
DOMAIN-SUFFIX,girigirilove.com
DOMAIN-SUFFIX,luffytv.online
DOMAIN-SUFFIX,agedm.com
DOMAIN-SUFFIX,fcdm22.com
DOMAIN-SUFFIX,nkdm.hkdrj.cn
DOMAIN-SUFFIX,agefans.com
DOMAIN-SUFFIX,cycdm01.top
DOMAIN-SUFFIX,yinghuafanju.com.cn
DOMAIN-SUFFIX,mobile.meinadi.cn
DOMAIN-SUFFIX,xifanacg.com
DOMAIN-SUFFIX,cn-yinghuadman.com.cn
DOMAIN-SUFFIX,bbs.kfmax.com
DOMAIN-SUFFIX,xuandm.com
DOMAIN-SUFFIX,ani.girigirilove.com
DOMAIN-SUFFIX,agedm.org
DOMAIN-SUFFIX,img.picbf.com
DOMAIN-SUFFIX,megaplay.buzz
DOMAIN-SUFFIX,myani.org
DOMAIN-SUFFIX,anifun.cn
DOMAIN-SUFFIX,animefenix2.tv
DOMAIN-SUFFIX,agedm.live
DOMAIN-SUFFIX,bbs.sumisora.net
DOMAIN-SUFFIX,animetake.tv
DOMAIN-SUFFIX,dlidli.app
DOMAIN-SUFFIX,xifan.moe
DOMAIN-SUFFIX,projectjust.xyz
DOMAIN-SUFFIX,dm530w6.com
DOMAIN-SUFFIX,gugu3.com
DOMAIN-SUFFIX,girigiri.cn
DOMAIN-SUFFIX,bestdubbedanime.com
DOMAIN-SUFFIX,yinghuacd.com
DOMAIN-SUFFIX,piratexplay.com
DOMAIN-SUFFIX,apps.fengctv.com.cn
DOMAIN-SUFFIX,img2.xfmanga.top
DOMAIN-SUFFIX,omofuns.com
DOMAIN-SUFFIX,kawaiifu.com
DOMAIN-SUFFIX,www.xuandm.com
DOMAIN-SUFFIX,www.yhdmtv.cc
DOMAIN-SUFFIX,imomoe.ai
DOMAIN-SUFFIX,tvtfun.net
DOMAIN-SUFFIX,ageapp.app
DOMAIN-SUFFIX,agefans.la
DOMAIN-SUFFIX,yhdmtv.cc
DOMAIN-SUFFIX,cycanime.com
DOMAIN-SUFFIX,app.xifandm.net
DOMAIN-SUFFIX,5dm.dev
DOMAIN-SUFFIX,age.tv
DOMAIN-SUFFIX,dilidili51.com
DOMAIN-SUFFIX,img.lzipic.com
DOMAIN-SUFFIX,next.xifanacg.com
DOMAIN-SUFFIX,qudman.com.cn
DOMAIN-SUFFIX,ttiandman.com.cn
DOMAIN-SUFFIX,kimoitv.com
DOMAIN-SUFFIX,kuroiru.co
DOMAIN-SUFFIX,yhdm.so
DOMAIN-SUFFIX,yhpdm.net
DOMAIN-SUFFIX,fcdmtv.cc
DOMAIN-SUFFIX,agedm.vip
DOMAIN-SUFFIX,dm.xifanacg.com
DOMAIN-SUFFIX,fengchedm.com
DOMAIN-SUFFIX,agedm.me
DOMAIN-SUFFIX,dm530.org
DOMAIN-SUFFIX,anime.girigirilove.com
DOMAIN-SUFFIX,fengchedm.cc
DOMAIN-SUFFIX,tokuzilla.net
DOMAIN-SUFFIX,fantuantv.com
DOMAIN-SUFFIX,cycity.pro
DOMAIN-SUFFIX,anisnatch.site
```

### 8.4 ⚠️ 日本节点不可用（要用「非日本节点」组）

```yaml
DOMAIN-SUFFIX,1497203185.rsc.cdn77.org
DOMAIN-SUFFIX,auth.hanime.tv
DOMAIN-SUFFIX,ct.hanime.tv
DOMAIN-SUFFIX,hanime-cdn.com
DOMAIN-SUFFIX,hanime.tv
DOMAIN-SUFFIX,hanime1.me
DOMAIN-SUFFIX,hanimeone.me
DOMAIN-SUFFIX,javchu.com
DOMAIN-SUFFIX,vdownload.hembed.com
```

> **hanime1 家族要点**：`hanime1.me`（主站）、`hanimeone.me`（漫画分站）、`javchu.com`（AV 分站）都**不能走日本节点**；`hanime1.com` 是官方给「只有日本节点」用户的替代域名（走日本节点时改用它，即可正常访问）。
> 你现有的 `NoJP.list` 只有 `DOMAIN-KEYWORD,hanime1`——**`hanimeone.me` 和 `javchu.com` 不含 "hanime1" 字样，命中不到**，建议把上表 8.4 整组收进去（或补关键词 `hanimeone`）。
>
> **（2026-10-06 晚已完成）** 这组域名已收进 `rules/AnimeNoJP.list`（原 `NoJP.list` 改名），
> 并在 `rules/AnimeProxy.list` 尾部留了备用条目；漫画侧同类清单 `rules/MangaNoJP.list` 一并建立。

## 9. 定期复查指南

**复查节奏**：正版平台（国内 / 日系）域名稳定，**每季度抽查**；中文聚合站与海外聚合站高变动，建议**每月**。

| 复查对象 | 看什么 | 入口 |
|---|---|---|
| 海外聚合站（aniwaves/hianimes/animegg 等） | 站点换域、阵亡 | [EverythingMoe 墓地](https://everythingmoe.com/graveyard)（阵亡名单）、[FMHY 视频区](https://fmhy.net/videopiracyguide)、扩展源码（见 §3 各条目） |
| 中文聚合站（樱花 / 风车 / AGE / 稀饭 等） | 当前域名 | 各站发布页 / App 内公告（见 §1 条目） |
| 国内平台（B站 / 爱奇艺 / 腾讯 / 优酷 / 芒果…） | 域名极少变 | 一般不用管；出问题看 §1 的 CDN 清单 |
| BT / 字幕组 | 蜜柑双入口、dmhy 状态 | §4 各条目的官方 TG / 发布渠道 |
| hanime1 家族 | 域名与"日本节点"限制变化 | [Han1meViewer 仓库](https://github.com/misaka10032w/Han1meViewer)（官方域名数组在 Constants.kt） |
| 全局 | 大陆可达性复核 | 上述站点的官方公告 + GreatFire 查询 |
