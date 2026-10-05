# 漫画站点域名清单（Clash / mihomo 分流用）

> 生成日期：**2026-10-05** ｜ 用途：为 Clash / mihomo（OpenClash）分流规则提供漫画类站点域名参考
> 全部域名来自当日的联网调研（每条附来源 URL），并在当天做过统一实测（方法见 §7）

## 阅读说明

本清单分五节收录：

1. **国内漫画站**（大陆直连为主）
2. **日本漫画站**（基本需代理）
3. **韩国网漫站**（基本需代理）
4. **英文 / 全球漫画站**（基本需代理）
5. **成人 / 本子阅读站**（需代理）

每条包含：**域名**（主域在前，含常用子域与图片 CDN）、**性质**、**来源**（可点击的 URL，方便日后核对与更新）、**后续更新入口**、**快测记录**、**备注**。

### 可靠性标记

| 标记 | 含义 |
|---|---|
| ✅ | 实测可访问（200/30x；403/404/426 等已确认为反爬、需 cookie 或 API 根路径特性的，也归此类但会在条目里注明） |
| 🟡 | 实测异常（超时 / 连接重置 / 需登录），多为反爬或本机网络环境局限，**不代表不可用** |
| ❌ | 已确认失效 / 停用 / 域名停放 / 误导域名，**不要加入规则**（§8 有汇总） |

### 分流建议

- 优先用 `DOMAIN-SUFFIX`（如 `DOMAIN-SUFFIX,manhuagui.com`）：天然覆盖子域与 CDN，图片域、阅读器域一并命中。
- **轮换站**（韩国盗版聚合、拷贝漫画、`mangaraw` 系 raw 站等）域名带数字 / TLD 轮换，后缀匹配挡不住"换号"，建议在 `DOMAIN-SUFFIX` 之外补 `DOMAIN-KEYWORD` 兜底（关键词见 §9 附录）。
- 单独列出的**图片 CDN**（如 `img.dlsite.jp`、`gold-usergeneratedcontent.net`、`i1-i4.nhentai.net`）漏了会出现"网页能开、图挂"，建议一并收录。
- 官方站域名很稳定；聚合 / raw / 盗版站高变动——按每条目的「后续更新入口」定期复核（建议：官方站每季一次，聚合站每月一次）。

### 可靠性声明

- 实测经本机（Windows + 路由器 OpenClash）出网，结果 = 该网络环境的快照；换网络 / 换出口可能不同。
- 域名轮换站的"当前域名"带时间戳，请以各站**官方公告**（多为 Telegram 频道）为准。
- 本清单只做域名收集，不构成对站点内容的背书。

---

## 1. 国内漫画站（大陆直连为主）

- 调研日期: 2026-10-05
- 快测方法: `nslookup 域名` + `curl -s -o /dev/null -w '%{http_code}' --connect-timeout 6 -m 10 -A 'Mozilla/5.0' https://域名/`；本机流量经路由器代理出网，超时/NXDOMAIN 仅作参考，不代表站点死亡。
- CDN 域名来源: 当日抓取站点首页/漫画页 HTML 源码统计，或 DNS 实测子域解析；均已注明。

---

#### 哔哩哔哩漫画（B漫）
- 类别: 国内正版
- 域名: manga.bilibili.com | i0.hdslb.com | s1.hdslb.com | manga.hdslb.com
- 性质: B站旗下正版漫画平台（含收购的有妖气作品迁移入库）
- 来源: [哔哩哔哩漫画首页源码](https://manga.bilibili.com/)（首页 HTML 中图片 1077 次引用 i0.hdslb.com、静态资源 39 次引用 s1.hdslb.com）；漫画图片主机 manga.hdslb.com 实测 403 存活（防盗链，带 Referer 可用）
- 后续更新入口: 无
- 快测: manga.bilibili.com: 200；manga.hdslb.com: 403（存活）
- 备注: API 与网页同域（manga.bilibili.com/twirp/…），无需单独列 API 域名。i0.hdslb.com 是全 B 站通用图片 CDN（与主站共享）。国内直连。

#### 腾讯动漫
- 类别: 国内正版
- 域名: ac.qq.com | m.ac.qq.com | manhua.acimg.cn | gtimgcdn.ac.qq.com
- 性质: 腾讯正版漫画平台
- 来源: [腾讯动漫首页源码](https://ac.qq.com/)（HTML 中图片 130 次引用 manhua.acimg.cn、134 次引用协议相对的 gtimgcdn.ac.qq.com；移动端 m.ac.qq.com）
- 后续更新入口: 无
- 快测: ac.qq.com: 200
- 备注: 解析到腾讯云 ias 节点，国内直连。gtimgcdn.ac.qq.com 与 manhua.acimg.cn 均为图片 CDN，规则建议两条都加。

#### 快看漫画
- 类别: 国内正版
- 域名: kuaikanmanhua.com | www.kuaikanmanhua.com | h5.kuaikanmanhua.com | api.kuaikanmanhua.com | static3w.kuaikanmanhua.com | f2.kkmh.com | houyi.kkmh.com | kkmh.com
- 性质: 国内最大正版条漫平台之一
- 来源: [快看漫画首页源码](https://www.kuaikanmanhua.com/)（57 次引用 f2.kkmh.com、50 次引用 static3w.kuaikanmanhua.com、各 1 次 h5/houyi.kkmh.com）；api.kuaikanmanhua.com 为 DNS 实测独立解析（81.70.60.119，根路径 404 属正常）
- 后续更新入口: 无
- 快测: www.kuaikanmanhua.com: 200；api.kuaikanmanhua.com: 404（存活）
- 备注: kkmh.com 是其图片域 apex（f2./houyi. 子域在用）；App 内 API 常见 api.kuaikanmanhua.com。国内直连。

#### 咚漫（WEBTOON 中国版）
- 类别: 国内正版（NAVER 旗下）
- 域名: dongmanmanhua.cn | www.dongmanmanhua.cn | cdn.dongmanmanhua.cn | cdn-static.dongmanmanhua.cn
- 性质: WEBTOON 简体中文版官方站（页脚链接 www.webtoons.com / m.webtoons.com）
- 来源: [咚漫首页源码](https://www.dongmanmanhua.cn/)（93 次引用 cdn.dongmanmanhua.cn 图片、cdn-static.dongmanmanhua.cn 静态资源）
- 后续更新入口: 无
- 快测: dongmanmanhua.cn: 200
- 备注: 解析 39.106.153.55（阿里云北京），国内直连。api.dongmanmanhua.cn 无解析。

#### 七猫免费漫画 / 番茄漫画（字节）
- 类别: 国内正版（App 内板块，无独立网页漫画站）
- 域名: 无独立漫画域名（七猫主站: qimao.com | xiaoshuo.wtzw.com；番茄主站: fanqienovel.com）
- 性质: 免费阅读平台的漫画板块，内容主要在 App 内提供
- 来源: [七猫中文网](https://www.qimao.com/)；[番茄小说](https://fanqienovel.com/)；本机实测 manga.qimao.com / comic.qimao.com / manhua.qimao.com / fanqiemanga.com 均 NXDOMAIN
- 后续更新入口: 无
- 快测: www.fanqienovel.com: 301（存活）；上述漫画子域: NXDOMAIN
- 备注: 分流规则只需覆盖 fanqienovel.com、qimao.com、wtzw.com 主域，漫画内容随主 App 域名走。

---

#### 漫画柜
- 类别: 汉化站
- 域名: manhuagui.com | www.manhuagui.com | mhgui.com | cf.mhgui.com | i.hamreus.com
- 性质: 繁体汉化漫画站（日漫汉化为主）
- 来源: [漫画柜首页源码](https://www.manhuagui.com/)（首页 201 处资源全部引用 cf.mhgui.com）；[漫画页源码](https://www.manhuagui.com/comic/1/)（同样仅 cf.mhgui.com）；i.hamreus.com 为其历史图片 CDN，实测 200 在线
- 后续更新入口: 无
- 快测: www.manhuagui.com: 200；mhgui.com: 403（存活，防裸访问）；i.hamreus.com: 200
- 备注: 主站与 www 解析境外 VPS（107.189.8.124 / 45.76.100.103），可直连但质量一般；被墙时需代理。i.hamreus.com 保留在规则以防旧缓存页图片。

#### 看漫画（原"漫画台"体系）
- 类别: 国内聚合
- 域名: kanman.com | www.kanman.com | m.kanman.com | resource.mhxk.com | image.yqmh.com | static.321mh.com | activity.321mh.com | cms.samanlehua.com
- 性质: 国内老牌在线漫画站（国漫为主）；原 manhuatai.com 首页已变成"鄂州看漫画动漫有限公司"企业展示页，m.manhuatai.com 301 跳 m.kanman.com，漫画本体已归并到 kanman.com
- 来源: [看漫画首页源码](https://www.kanman.com/)（157 次引用 resource.mhxk.com、81 次 image.yqmh.com、12 次 cms.samanlehua.com）；[漫画台首页实测](https://www.manhuatai.com/)（标题"鄂州看漫画动漫有限公司"）；实测 https://www.manhuatai.com/douluodalu/ 返回 404
- 后续更新入口: 无
- 快测: www.kanman.com: 200；m.manhuatai.com: 301→m.kanman.com；www.manhuatai.com: 404（漫画内容已撤）
- 备注: mhxk.com、yqmh.com、321mh.com、samanlehua.com 均为其关联 CDN/站群域名，规则建议整站群覆盖。国内直连。

#### 包子漫画
- 类别: 汉化站/聚合站
- 域名: baozicomic.cc | baozimh.com | bzmgcn.com | cn.bzmgcn.com | short.tiankongshuyu.cn
- 性质: 国漫条漫类免费在线站（自标"海量正版漫画"），PC/移动端常用聚合源
- 来源: [包子漫画首页实测](https://baozicomic.cc/)（标题"包子漫画 - 海量正版漫画免费阅读"，页面引用 short.tiankongshuyu.cn 短链域）；实测 baozimh.com 302 → cn.bzmgcn.com；第三方源仓库收录列表（yckceo.com）亦登记 https://cn.bzmgcn.com 为当前入口
- 后续更新入口: 无独立发布页（曾用域名 baozimh.com 仍存活做跳转）
- 快测: baozicomic.cc: 200；baozimh.com: 302→cn.bzmgcn.com；cn.bzmgcn.com: 302 回跳（对境外 IP 出现跳转环，疑似按地区分流/盾）
- 备注: 高变动站，历史上用 baozimh.com，现 bzmgcn.com 与 baozicomic.cc 双域名并存。对大陆用户哪个可达需实机再验证；规则里建议把 baozimh.com、bzmgcn.com、baozicomic.cc 都加上。

#### 拷贝漫画（CopyManga）★重点
- 类别: 汉化站/聚合站
- 域名: mangacopy.com | www.mangacopy.com | copymanga.site | www.copymanga.site | copy4000.com | www.copy4000.com | api.mangacopy.com | api.copymanga.site | mangafunb.fun | s3.mangafunb.fun | sa–sz.mangafunb.fun 系列（实测可见: sa sb sc sd se sf sg sh sj sl sm sn sp sq ss st sw sx sy sz + s3）| manga2026.xyz | www.manga2026.xyz
- 性质: 全球华人免费在线漫画站（官方自述"为躲避不可抗力开设"），日漫汉化为主，带官方 App
- 来源: [拷贝漫画首页](https://www.mangacopy.com/)（站内横幅官方公告原文："大陸無障礙訪問地址為https://www.copy4000.com/ ** 更多加速服務正在艱難談判中"）；[百度知道整理](https://zhidao.baidu.com)（网页端为 www.mangacopy.com，copymanga.org 已失效）；[bgm.tv 资源汇总帖](https://bgm.tv)（历史拓展过 .org/.site/.info/.net 后缀）；图片/静态 CDN 域名 mangafunb.fun 全部来自首页源码实测（25 次 s3.mangafunb.fun，封面图使用 sa–sz 系列子域）；manga2026.xyz 为首页 banner 官方关联下载站
- 后续更新入口: 站内首页横幅公告（https://www.mangacopy.com/ 或 copy4000.com 首页）；未发现公开官方 TG 频道链接
- 快测: www.mangacopy.com: 200；www.copymanga.site: 200；www.copy4000.com: 200；api.mangocopy.com(误写)/api.mangacopy.com: 404（存活）；api.copymanga.site: 200；copymanga.org: 连接失败；copymanga.tv: NXDOMAIN；copymanga.com: 连接失败；copymanga.info: 200（停放页）；copymanga.co: 200（停放页）；copymanga.app: 200（welcome 停放页）
- 备注: 域名轮换规律——每遇攻击/封锁即启用新 TLD，官方公告只挂最新可用域名；API 独立于网页（api.mangacopy.com / api.copymanga.site），App 走 API 需单独覆盖；mangafunb.fun 是图片核心域，缺它网页能开但图挂；manga2026.xyz 是关联"新番/里番下载站"，可按需收录。旧域名 .org/.tv/.com 等已失效或停放，不要再加入规则；.info/.co/.app 实测均为停放页（title 即域名本身或 welcome），无内容。

#### 漫画DB
- 类别: 汉化站（单行本扫描聚合）
- 域名: manhuadb.com | www.manhuadb.com | img.manhuadb.com | api.manhuadb.com | images.manhuadb.com
- 性质: 收录经典漫画单行本扫描的免费阅读站
- 来源: 本机 DNS 实测（manhuadb.com 及 img/api/images 子域均解析 182.16.68.115）；https://www.manhuadb.com/ 抓取返回含混淆脚本的跳转页（防盗/防采集）
- 后续更新入口: 无
- 快测: https://www.manhuadb.com/: 000（多次连接失败）；http://www.manhuadb.com/: 200（一次成功）
- 备注: 站点存活但 https 对本机代理出口不可达，疑为限流或盾；大陆直连大概率正常。解析 IP 在境外（182.16.68.x）。

### 中文汉化聚合站（高变动，仅列实测有解析的）
- 说明: 这类站群域名极乱（SEO 站群、无官方公告渠道），页面多为空壳或无法确认官方归属；仅列本机 2026-10-05 实测有 DNS 解析的站，不建议直接写入分流规则，只作参考。
- 漫画堆: manhuadui.com / www.manhuadui.com，DNS 208.115.249.236，首页 200 但 title "Manhuadui"，疑似空壳（来源为本机实测，无官方渠道可引）
- 新新漫画: xindm.cn / www.xindm.cn，DNS 208.98.40.222，首页有返回但无有效标题（疑 JS 渲染或被盾）
- 漫画北: manhuabei.com / www.manhuabei.com，DNS 118.193.202.219，首页 200 但 title "Manhuabei"，疑似空壳（站名未从官方渠道确认）
- 笔趣阁类: 同列表中出现的多为小说站（如 m.ddbiquge.tw），漫画聚合与小说站共用站群模式，无稳定官方域名可确认。

#### 中文站群增量：18comic（JM）/ 海棠 / 漫画人 / boylove（来源 v2fly 上游，2026-10-05 抓取）

- 类别: 汉化站 / 成人向平台（基本需代理）
- 域名: 见下（按站群分组；全部并入 §9 的本站域名总表）
- 性质: 直接摘录 [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community/tree/master/data) 的现成域名表（该仓库官方维护、更新最勤），并做了统一实测（结果见 §7）。
- 18comic / JM 禁漫（成人向汉化，站群轮换，共 51 条）: `18comic.org` | `18comic.vip` | `18comic.cc` | `18comic.company` | `18comic-god.cc` | `18comic-god.club` | `18comic-god.xyz` | `jmcomic.me` | `jmcomic.moe` | `jmcomic.rocks` | `jmcomic.mobi` | `jmcomic.group` | `jmcomic.ltd` | `jmcomic-fb.vip` | `jmcomic-zzz.one` | `jmcomic-zzz.org` | `jmcomic1.city` | `jmcomic1.me` | `jmcomic1.mobi` | `jmcomic1.rocks` | `jmcomic2.moe` | `jm-comic2.cc` | `jm365.work` | `jm365.xyz` | `jmapinode.xyz` | `jmapinode.biz` | `jmapinode.vip` | `jmapinode1.top` | `jmapinode2.top` | `jmapinode3.top` | `jmapinodeudzn.net` | `jmapinodeudzn.xyz` | `jmapiproxy1.cc` | `jmapiproxy2.cc` | `jmapiproxy3.cc` | `jmapiproxy4.cc` | `jmapiproxy1.monster` | `jmapiproxyxxx.vip` | `jmapibranch1.cc` | `jmapibranch2.cc` | `jmapibranch3.cc` | `asjmapihost.cc` | `jm18c-bbm.cc` | `jm18c-bbm.net` | `jm18c-uoi.net` | `cdnblackmyth.club` | `cdnmhws.cc` | `cdnmhwscc.vip` | `cdnuc.vip` | `cdnxxx-proxy.co` | `cdnxxx-proxy.xyz`（上游文件 `data/18comic`）
- copymanga 备用域（v2fly 收录、上文未提）: `2025copy.com` | `copy-manga.com` | `copy20.com` | `copy2000.online` | `mangafuna.xyz`（上游 `data/copymanga`）
- 漫画人 / 动漫屋（瑞安市我喜欢网络有限公司，老牌中文站）: `manhuaren.com` | `dm5.com` | `dm5.cn` | `dm9.com` | `1kkk.com` | `gmanhua.com` | `hkmanga.com` | `manben.com` | `manbenapi.com` | `cdndm5.com`（上游 `data/manhuaren`）
- 海棠文化線上文學城（成人向）: `haitangbook.com` | `haitbook.com` | `longmabook.com` | `longmabookcn.com` | `htlvbooks.com` | `htnewbooks.com` | `htwhbook.com` | `lmbooks.com` | `lmebooks.com` | `lovehtbooks.com` | `lvhtebook.com` | `mybookinlm.com` | `myhtebook.com` | `myhtebooks.com` | `myhtlmebook.com` | `newhtbook.com` | `urhtbooks.com`（上游 `data/haitang`）
- boylove（耽美）: `boylove.cc` | `boylove.live` | `boylove1.cc` | `boyloves.cc` | `fuhouse.club`（上游 `data/boylove`）
- 后续更新入口: https://github.com/v2fly/domain-list-community/tree/master/data （直接跟进上述文件；raw 拉不动时用 jsDelivr：`https://cdn.jsdelivr.net/gh/v2fly/domain-list-community@master/data/18comic`）
- 备注: 这批站点基本都要代理；与本仓库现有 `rules/18comic.list`（关键词 `18-comic`）配合——建议保留关键词兜底，同时把上表作为域名补充。JM 系域名换得很勤，本次实测只有约一半处于在线状态（其余为轮换空档/停放，见 §7），**长期方案是直接引用上游文件**而不是抄本表。

---

### 已确认失效

#### 动漫之家（dmzj.com）★
- 类别: 已倒闭
- 域名: dmzj.com（apex 有解析但无内容）| www.dmzj.com（NXDOMAIN）| idmzj.com（曾用新域名，现连接失败）
- 性质: 2005 年创立的动漫综合平台/漫画站，国内最老牌汉化漫画聚集地之一
- 来源: [萌娘百科·动漫之家](https://zh.moegirl.org.cn/%E5%8A%A8%E6%BC%AB%E4%B9%8B%E5%AE%B6)（"已于2025年09月10日正式停止运营，其网站与APP全面无法访问，用户数据未备份清空"；运营主体尚科齐（北京）网络科技有限公司被列为失信执行人）；多家媒体/社区（QQ频道动漫资讯日报、喜马拉雅新闻等）报 2025-09-10 停运
- 后续更新入口: 无（后续曾流传"再漫画"等转生站，未见官方确认）
- 快测: www.dmzj.com: NXDOMAIN（AliDNS 权威否定）；dmzj.com: 000（apex 尚有解析 180.184.75.122 但无响应）；idmzj.com: 000（解析 101.126.87.151 但无响应）
- 备注: 2025-09-10 正式停运。dmzj.com apex 解析疑为域名保护，www/idmzj 均已不可用。分流规则无需收录。

#### 有妖气（u17.com）
- 类别: 已倒闭（并入 B 漫）
- 域名: u17.com | www.u17.com
- 性质: 原创漫画平台（《十万个冷笑话》《镇魂街》），B站约 6 亿元收购后关停
- 来源: [维基百科·有妖气](https://zh.wikipedia.org/zh-hans/%E6%9C%89%E5%A6%96%E6%B0%94)（2022-12-31 停止服务，并入哔哩哔哩漫画）；[36氪·有妖气漫画正式关停并入B站](https://m.36kr.com/p/2080154894143492)
- 后续更新入口: 无
- 快测: www.u17.com: 000（解析 180.163.28.105 但无响应）
- 备注: 2022-09-01 发公告、2022-12-31 关停，内容迁至 B 漫。

#### 布卡漫画（buka.cn）
- 类别: 已倒闭
- 域名: buka.cn | www.buka.cn | app.buka.cn | www.ibuka.cn（历史域名）
- 性质: 2011 年创立的早期漫画平台，曾拥有 5000 万注册用户
- 来源: [维基百科·布卡漫画](https://zh.wikipedia.org/zh-cn/%E5%B8%83%E5%8D%A1%E6%BC%AB%E7%94%BB)（2023 年 8 月停止营运，事前没有任何通知）
- 后续更新入口: 无
- 快测: buka.cn / www.buka.cn / app.buka.cn: 000（解析 120.92.122.249 但无响应）
- 备注: 2023-08 悄然停运，无官方公告。

#### 嗨皮漫画（happymh.com）
- 类别: 已倒闭（盗版站官方道歉永久关闭）
- 域名: happymh.com | www.happymh.com
- 性质: 运营约 6 年的知名盗版漫画站
- 来源: [NOWnews 报道](https://www.nownews.com) / [Yahoo 奇摩新闻](https://tw.news.yahoo.com)（2026-08-14 报道：无预警永久关闭，首页公告"即日起永久关闭……对相关版权方深表歉意"）
- 后续更新入口: 无
- 快测: happymh.com / www.happymh.com: NXDOMAIN（无 A 记录）
- 备注: 2026 年 8 月关站，域名已无解析。近期新失效站，规则务必移除。

#### 汗汗漫画（hhcomic.com）
- 类别: 已失效（域名已停放）
- 域名: hhcomic.com | www.hhcomic.com
- 性质: 老牌免费漫画站
- 来源: 本机实测：hhcomic.com 首页返回"Redirecting… + router.parklogic.com"（域名停放服务商页面）；老站历史域名多次更换（曾用 hanmanjia、hhimm 等称呼），当前无可靠来源确认其新域名
- 后续更新入口: 无（原站无可靠公告渠道）
- 快测: www.hhcomic.com: 200（但为 parklogic 停放跳转页，非原站）
- 备注: 原站已离开该域名；搜索引擎结果为大量 SEO 仿冒页（如 hhmhua.cn、sdxcby.cn 等，均无法确认真伪），不建议收录。

#### 古风漫画网（gufengmh.com）
- 类别: 已失效/失联
- 域名: gufengmh.com | www.gufengmh.com
- 性质: 古风题材免费漫画站（圣樱漫画管理系统 MHD 模板站群之一）
- 来源: [CeJS 工具站点列表（Gitee）](https://gitee.com)（记录 gufengmh.js 对应站点）；[站点收录页](https://www.yckceo.com)仍登记 https://www.gufengmh.com/
- 后续更新入口: 无
- 快测: gufengmh.com / www.gufengmh.com: NXDOMAIN（无 A 记录）
- 备注: 收录页仍登记但实际已无 DNS 解析，疑关站或换域名；此类站换域名后伴有大量 SEO 仿冒页，无法验证的域名不要收录。

#### 网易漫画（manhua.163.com）
- 类别: 已倒闭
- 域名: manhua.163.com（未实测）
- 性质: 网易旗下漫画平台
- 来源: 媒体与社区报道（网易官方公告：2019-12-31 后永久停止服务，作品大部分转移至哔哩哔哩漫画）
- 后续更新入口: 无
- 快测: 未实测（历史域名）
- 备注: 已并入 B 漫体系。

#### 其他失效/停放域名（勿收录）
- 拷贝漫画旧域名: copymanga.org / copymanga.tv / copymanga.com（失效）；copymanga.info / copymanga.co / copymanga.app（停放页）；copymanga.me（NXDOMAIN）。
- manhuatai.com / www.manhuatai.com / m.manhuatai.com: 漫画站已撤离，域名现为公司官网与跳转（见"看漫画"节）。
- dmzj 体系: www.dmzj.com、idmzj.com、donghua.dmzj.com 等子站随动漫之家主站一并停运。

## 2. 日本漫画站（基本需代理）

- 调研日期：2026-10-05（本机环境，流量走路由器代理）
- 主要信源：keiyoushi/extensions-source 源配置（每站 build.gradle.kts 的 baseUrl + keiyoushi 官方索引 index.json 的 homeUrl）、各站官网实抓、FMHY reading 页、Rawmangaz（FMHY 引用的日本 raw 站清单）
- keiyoushi 索引（全量 homeUrl，最权威的"当前域名"来源）：https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.json
- 说明：超时/403/404 常为反爬或需浏览器，不等于死站；已实测标注。带 "301→" 的老域名不是死站，仍会产生流量（可保留在规则中）。

---

### 一、日本官方平台（出版社 / 杂志社系）

#### 少年ジャンプ＋（Shonen Jump+）
- 类别: 日本官方
- 域名: shonenjumpplus.com
- 性质: 集英社的核心免费/付费 web 漫画平台，Jump 系新作首发。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/shonenjumpplus)；[Keiyoushi 索引 homeUrl](https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.json)
- 后续更新入口: keiyoushi src/ja/shonenjumpplus（baseUrl 变更会体现在该文件/索引）
- 快测: 200（2026-10-05 本机）
- 备注: 无轮换；部分作品海外 IP 限读（需代理）。

#### MANGA Plus by SHUEISHA
- 类别: 日本官方
- 域名: mangaplus.shueisha.co.jp | jumpg-webapi.tokyo-cdn.com（API）
- 性质: 集英社官方多语言版（含中文/英文），与日本同步连载。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/all/mangaplus)（API 域名见 MangaPlus.kt）
- 后续更新入口: keiyoushi src/all/mangaplus
- 快测: mangaplus.shueisha.co.jp 200；jumpg-webapi.tokyo-cdn.com 403@/（API 根路径正常拒绝）
- 备注: API 域名单列，抓取/阅读器需要；地区限制按作品。

#### となりのヤングジャンプ
- 类别: 日本官方
- 域名: tonarinoyj.jp
- 性质: 集英社 YJ 系 web 连载平台（ワンパンマン等）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/tonarinoyoungjump)
- 后续更新入口: keiyoushi src/ja/tonarinoyoungjump
- 快测: 200（2026-10-05 本机）
- 备注: 无。

#### ヤンジャン！（Young Jump+ / ynjn）
- 类别: 日本官方
- 域名: ynjn.jp | webapi.ynjn.jp（API）
- 性质: 集英社 Young Jump 官方 App/Web 平台。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/ynjn)（webapi.$domain 见 Ynjn.kt）
- 后续更新入口: keiyoushi src/ja/ynjn
- 快测: ynjn.jp 200；webapi.ynjn.jp 404@/（API）
- 备注: 无。

#### ジャンプルーキー！（Jump Rookie!）
- 类别: 日本官方
- 域名: rookie.shonenjump.com
- 性质: 集英社新人漫画投稿/阅读平台（shonenjump.com 子域）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/jumprookie)
- 后续更新入口: keiyoushi src/ja/jumprookie
- 快测: 200
- 备注: 注意与主站 shonenjump.com 同 apex。

#### ゼブラック（Zebrack）
- 类别: 日本官方
- 域名: zebrack-comic.shueisha.co.jp | api.zebrack-comic.com（API）
- 性质: 集英社电子书/漫画阅览服务（杂志+YJ/Jump 作品）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/zebrack)
- 后续更新入口: keiyoushi src/ja/zebrack
- 快测: 200；api.zebrack-comic.com 404@/
- 备注: API 域名为复合子域，注意单独覆盖。

#### マガポケ（Magazine Pocket）
- 类别: 日本官方
- 域名: pocket.shonenmagazine.com | api.pocket.shonenmagazine.com（API）
- 性质: 讲谈社《周刊少年Magazine》官方 App/Web。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/magazinepocket)
- 后续更新入口: keiyoushi src/ja/magazinepocket
- 快测: 200；api.pocket.shonenmagazine.com 400@/（API）
- 备注: 无。

#### サンデーうぇぶり
- 类别: 日本官方
- 域名: www.sunday-webry.com | sunday-webry.com
- 性质: 小学馆 Sunday 系官方 web 连载。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/sundaywebevery)
- 后续更新入口: keiyoushi src/ja/sundaywebevery
- 快测: 200
- 备注: 无。

#### マンガワン（MangaONE，旧・裏サンデー）
- 类别: 日本官方
- 域名: manga-one.com | urasunday.com（301→manga-one.com）
- 性质: 小学馆官方 App/Web（マンガワン），裏サンデー已并入。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangaone)；URL 实测 urasunday.com → manga-one.com/?from_redirect=true（标题"マンガワン"）
- 后续更新入口: keiyoushi src/ja/mangaone
- 快测: manga-one.com 200；urasunday.com 301→manga-one.com
- 备注: urasunday.com 仍收流量，建议保留。

#### くらげバンチ
- 类别: 日本官方
- 域名: kuragebunch.com
- 性质: 新潮社 web 漫画站。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/kuragebunch)
- 后续更新入口: keiyoushi src/ja/kuragebunch
- 快测: 200
- 备注: 无。

#### ガンガンONLINE
- 类别: 日本官方
- 域名: www.ganganonline.com
- 性质: 史克威尔艾尼克斯（SQEX）官方 web 漫画。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/ganganonline)
- 后续更新入口: keiyoushi src/ja/ganganonline
- 快测: 200；apex ganganonline.com NXDOMAIN（必须带 www）
- 备注: 只覆盖 www 子域。

#### マンガUP！
- 类别: 日本官方
- 域名: www.manga-up.com
- 性质: SQEX 官方 App 漫画平台；**未停服**（2026-10 实测 200）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangaupjapan)
- 后续更新入口: keiyoushi src/ja/mangaupjapan
- 快测: 200
- 备注: 无。

#### ヤングアニマルWeb / マンガPark（白泉社）
- 类别: 日本官方
- 域名: younganimal.com | manga-park.com
- 性质: 白泉社两个官方 web 平台（YAnimal 系 / 全集合作品）。
- 来源: [keiyoushi 源配置 younganimal](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/younganimal)；[mangaparkpublisher](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangaparkpublisher)
- 后续更新入口: keiyoushi src/ja/younganimal、src/ja/mangaparkpublisher
- 快测: 均 200
- 备注: 无。

#### コミックDAYS
- 类别: 日本官方
- 域名: comic-days.com
- 性质: 讲谈社官方 web/App 漫画（Morning 系等）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/comicdays)
- 后续更新入口: keiyoushi src/ja/comicdays
- 快测: 200
- 备注: 无。

#### コミックアクション（含 web アクション）
- 类别: 日本官方
- 域名: comic-action.com | webaction.jp（301→comic-action.com）
- 性质: 双叶社《漫画アクション》官方 web；webアクション已并入。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/comicaction)；实测 webaction.jp 301→comic-action.com
- 后续更新入口: keiyoushi src/ja/comicaction
- 快测: 均 200（webaction.jp 跳转）
- 备注: webaction.jp 仍收流量，保留。

#### コミックボーダー
- 类别: 日本官方
- 域名: comicborder.com
- 性质: 新潮社 BUNCH 系 web 漫画。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/comicborder)
- 后续更新入口: keiyoushi src/ja/comicborder
- 快测: 200
- 备注: 无。

#### コミックガルド
- 类别: 日本官方
- 域名: comic-gardo.com
- 性质: OVERLAP 官方 web 漫画（なろう系改编多）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/comicgardo)
- 后续更新入口: keiyoushi src/ja/comicgardo
- 快测: 200
- 备注: 无。

#### コミックリュウ
- 类别: 日本官方
- 域名: comic-ryu.jp
- 性质: 德间书店 web 漫画。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/comicryu)
- 后续更新入口: keiyoushi src/ja/comicryu
- 快测: 200
- 备注: 无。

#### コミックグロウル
- 类别: 日本官方
- 域名: comic-growl.com
- 性质: 武士道（Bushiroad）官方 web 漫画。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/all/comicgrowl)
- 后续更新入口: keiyoushi src/all/comicgrowl
- 快测: 200
- 备注: 在 keiyoushi 里属 all 语言目录。

#### コミックブースト
- 类别: 日本官方
- 域名: comic-boost.com
- 性质: 角川系（BOOK☆WALKER 运营）web 漫画。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/comicboost)
- 后续更新入口: keiyoushi src/ja/comicboost
- 快测: 200
- 备注: 无。

#### カドコミ（旧 ComicWalker）
- 类别: 日本官方
- 域名: comic-walker.com
- 性质: KADOKAWA 官方 web 漫画（原 ComicWalker，现品牌"カドコミ"）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/kadocomi)（索引中站点名"カドコミ"）
- 后续更新入口: keiyoushi src/ja/kadocomi
- 快测: 200
- 备注: 域名未变，仅品牌/前端改版；旧文档中的 comic-walker.com/... 路径仍会跳转。

#### ニコニコ漫画
- 类别: 日本官方
- 域名: nicomanga.com | comic.nicovideo.jp | api.nicomanga.jp（API）
- 性质: 多玩国（Dwango）官方漫画平台（原ニコニコ静画/漫画 App）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/nicomanga)；[ニコニコ静画系的 API 佐证](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/nicovideoseiga)
- 后续更新入口: keiyoushi src/ja/nicomanga
- 快测: nicomanga.com 200；api.nicomanga.jp 200；comic.nicovideo.jp 连接被拒（反爬/需浏览器+日本网络）
- 备注: 主域名 comic.nicovideo.jp 在本机被断连，属反爬非死站；APP 走 nicomanga.com。

#### ニコニコ静画（マンガ）
- 类别: 日本官方
- 域名: seiga.nicovideo.jp | sp.manga.nicovideo.jp | drm.cdn.nicomanga.jp（图片 CDN）
- 性质: ニコニコ静态画投稿平台（漫画分区），与ニコニコ漫画共用读者端。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/nicovideoseiga)（图片正则 `drm.cdn.nicomanga.jp/image/...`）
- 后续更新入口: keiyoushi src/ja/nicovideoseiga
- 快测: seiga.nicovideo.jp 403（反爬）；sp.manga.nicovideo.jp 未测（与漫画站共用）；drm.cdn.nicomanga.jp 404@/（CDN 正常拒绝）
- 备注: 图片 CDN 为漫画阅读必需，建议一并覆盖。

#### ガンマ+ / ゼノン編集部（コアミックス）
- 类别: 日本官方
- 域名: ganma.jp | comic-zenon.com
- 性质: コアミックス（Coamix）旗下两个官方 web 漫画平台。
- 来源: [keiyoushi 源配置 ganma](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/ganma)；[zenon](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/zenon)
- 后续更新入口: keiyoushi src/ja/ganma、src/ja/zenon
- 快测: ganma.jp 200（→/web）；comic-zenon.com 200（zenon.jp 403 反爬）
- 备注: 无。

#### COMIC FUZ（芳文社）
- 类别: 日本官方
- 域名: comic-fuz.com | api.comic-fuz.com | img.comic-fuz.com（图片）
- 性质: 芳文社官方 web 漫画（まんがタイム系/きらら系）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/comicfuz)（api.$domain / img.$domain）
- 后续更新入口: keiyoushi src/ja/comicfuz
- 快测: comic-fuz.com 200、api 200、img 403@/
- 备注: 图片 CDN 为阅读必需。

#### キラポ（旧 コミックメテオ）
- 类别: 日本官方
- 域名: kirapo.jp | comic-meteor.jp（301→kirapo.jp/meteor）
- 性质: 少年画報社系 web 漫画，コミックメテオ已改版并入"キラポ"。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/comicmeteor)；实测 comic-meteor.jp 301→kirapo.jp/meteor
- 后续更新入口: keiyoushi src/ja/comicmeteor（站点名已改 Kiraboshi）
- 快测: 均 200
- 备注: 老域名 comic-meteor.jp 仍收流量；keiyoushi 目录名未改。

#### COMIC FESTA（comic.iowl.jp）
- 类别: 日本官方
- 域名: comic.iowl.jp
- 性质: アイオウル（IOWL）运营的官方电子漫画（TL/女性向为主）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/comicfesta)
- 后续更新入口: keiyoushi src/ja/comicfesta
- 快测: 200
- 备注: 域名不是 apex（iowl.jp 为全站）。

#### ソクヨミ（sokuyomi）
- 类别: 日本官方
- 域名: sokuyomi.jp | api.sokuyomi.jp | cdn.sokuyomi.jp（图片）
- 性质: 广告分成型官方漫画阅读服务（多出版社合作）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/sokuyomi)（api.$domain / cdn.$domain）
- 后续更新入口: keiyoushi src/ja/sokuyomi
- 快测: sokuyomi.jp 200；api 426（协议升级拒绝）；cdn 403@/
- 备注: 图片 CDN 为阅读必需。

#### ヨモンガ（yomonga）
- 类别: 日本官方
- 域名: yomonga.com | www.yomonga.com
- 性质: 官方授权的广告型漫画阅读站（各社作品）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/yomonga)
- 后续更新入口: keiyoushi src/ja/yomonga
- 快测: 200
- 备注: 无。

#### ゼロサムオンライン（一迅社）
- 类别: 日本官方
- 域名: zerosumonline.com | api.zerosumonline.com（API）
- 性质: 一迅社《ZERO-SUM》系官方 web 漫画。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/zerosumonline)
- 后续更新入口: keiyoushi src/ja/zerosumonline
- 快测: 200；api 404@/
- 备注: 无。

#### メチャコミ / mechacomic
- 类别: 日本官方（韩系服务日本版）
- 域名: mechacomi.jp | mechacomic.jp
- 性质: 韩国 Mecha Comic / 漫画 Saison 的日本站（韩漫官方日文版）。
- 来源: [keiyoushi 源配置 mangasaison](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangasaison)；[mechacomic](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mechacomic)
- 后续更新入口: keiyoushi src/ja/mangasaison、src/ja/mechacomic
- 快测: 均 200
- 备注: 两域并存，建议都收。

#### アルファポリス
- 类别: 日本官方
- 域名: www.alphapolis.co.jp
- 性质: 阿尔法波利斯官方投稿/漫画平台（小说改编多）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/alphapolis)
- 后续更新入口: keiyoushi src/ja/alphapolis
- 快测: 未测（本轮未覆盖）
- 备注: 与小说站同域，收 apex 即可。

#### Ameba マンガ（ドクショオジカン）
- 类别: 日本官方
- 域名: dokusho-ojikan.jp | api.dokusho-ojikan.jp（API）
- 性质: CyberAgent 运营的正版电子漫画（Ameba 系）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/amebamanga)（api.$domain/dokusho-server）
- 后续更新入口: keiyoushi src/ja/amebamanga
- 快测: 未测（本轮未覆盖；keiyoushi 索引 homeUrl 为准）
- 备注: 无。

#### comico（コミコ）
- 类别: 日本官方
- 域名: www.comico.jp | api.comico.jp（API）
- 性质: NHN comico 日本站，竖屏彩漫；**未停服**（2026-10 实测在营）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/comico)；实测首页 title「comico (コミコ) | タテカラー漫画が毎日無料」
- 后续更新入口: keiyoushi src/ja/comico
- 快测: www.comico.jp 200；api.comico.jp 200
- 备注: 用户名单中"是否已停服"→ 答案：仍在営業。

#### チャンピオンクロス（秋田书店）
- 类别: 日本官方
- 域名: championcross.jp | mangacross.jp（301→championcross.jp）
- 性质: 秋田书店官方 web 漫画；マンガクロス域名 301 并入本站。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/championcross)；实测 mangacross.jp 301→championcross.jp（首页 title「チャンピオンクロス | 秋田書店の新作マンガが無料で読める！」）
- 后续更新入口: keiyoushi src/ja/championcross
- 快测: 均 200（mangacross.jp 跳转）
- 备注: mangacross.jp 仍收流量，保留。

#### やわらかスピリッツ
- 类别: 日本官方
- 域名: yawaspi.com
- 性质: 小学馆《ビッグコミックスピリッツ》系官方 web。
- 来源: [Rawmangaz 清单（FMHY 引用）](https://clarasguide.valeena.workers.dev/Guides/rawmangaz/)（列出了大量日本官方站点）；实测 200
- 后续更新入口: 官网自身；无 keiyoushi 源（未收录）
- 快测: 200
- 备注: 未进 keiyoushi，靠实测佐证；建议保留复查。

#### ヤンマガWeb / ヤングチャンピオン
- 类别: 日本官方
- 域名: yanmaga.jp | youngchampion.jp
- 性质: 讲谈社《ヤンマガ》与秋田书店《ヤングチャンピオン》官方 web。
- 来源: [keiyoushi 源配置 yanmaga](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/yanmaga)；[youngchampion](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/youngchampion)
- 后续更新入口: keiyoushi src/ja/yanmaga、src/ja/youngchampion
- 快测: 均 200
- 备注: 无。

#### CyComi
- 类别: 日本官方
- 域名: cycomi.com | web.cycomi.com（API）
- 性质: Cygames 官方 web 漫画。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/cycomi)（web.$domain/api）
- 后续更新入口: keiyoushi src/ja/cycomi
- 快测: cycomi.com 200
- 备注: 无。

#### ビッコミ（ビッグコミック）
- 类别: 日本官方
- 域名: bigcomics.jp
- 性质: 小学馆 Big Comic 系官方 web。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/bigcomics)
- 后续更新入口: keiyoushi src/ja/bigcomics
- 快测: 200
- 备注: 无。

#### コロコロオンライン / ちゃおプラス / 花とゆめ+ / フラワーコミックス
- 类别: 日本官方
- 域名: www.corocoro.jp | ciao.shogakukan.co.jp | hanayume.com | flowercomics.jp
- 性质: 小学馆系少儿/少女漫画官方站点（コロコロ、ちゃお、花ゆめ、フラワー）。
- 来源: [keiyoushi corocoroonline](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/corocoroonline)；[ciaoplus](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/ciaoplus)；[hanayume](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/hanayume)；[flowercomics](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/flowercomics)
- 后续更新入口: 对应 keiyoushi 目录
- 快测: 均 200
- 备注: 无。

#### ヒーローズWeb / フィールWeb / ごらくWeb
- 类别: 日本官方
- 域名: heros-web.com | feelweb.jp | gorakuweb.com
- 性质: 小学馆クリエイティブ系三站（ヒーローズ、フィール、ごらく）。
- 来源: [keiyoushi herosweb](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/herosweb)；[feelweb](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/feelweb)；[gorakuweb](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/gorakuweb)
- 后续更新入口: 对应 keiyoushi 目录
- 快测: 均 200
- 备注: 无。

#### コミックアーススター / コミックトレイル / コミックRide / COMIC PASH!
- 类别: 日本官方
- 域名: comic-earthstar.com | comic-trail.com | comicride.jp | comicpash.jp
- 性质: 地球星、LEED 系、Ride、PASH!（主妇与生活社）等出版社官方 web 漫画。
- 来源: [keiyoushi 对应目录](https://github.com/keiyoushi/extensions-source/tree/main/src/ja)（comicearthstar / comictrail / comicride / comicpash）
- 后续更新入口: 对应 keiyoushi 目录
- 快测: 均 200
- 备注: 无。

#### コミックグロウル系长尾（其他官方 web 平台速查）
- 类别: 日本官方
- 域名: 见下表（域名 | 快测）
- 性质: 大量中小出版社/平台的官方 web 漫画站点，均为 keiyoushi 在维护的活跃源。
- 来源: [keiyoushi 源目录](https://github.com/keiyoushi/extensions-source/tree/main/src/ja)（逐目录 build.gradle.kts 的 baseUrl，与 index.json 的 homeUrl 一致）
- 后续更新入口: https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.json（全量 homeUrl 快照）
- 快测: 见表列（2026-10-05 本机）
- 备注: 表内站点多为单域名，无轮换；如启用可整表收 apex。

| 站点 | 域名 | 快测 |
| --- | --- | --- |
| Comic Ogyaaa | comic-ogyaaa.com | 200 |
| ビビビ★コミック | bibibi-comic.com | 200 |
| コミレラ | comirela.com | 200 |
| コミックユアーズ | comic-y-ours.com | 200 |
| TakeComic | takecomic.jp | 200 |
| Pash Up! | pash-up.jp | 200 |
| ぴあコミック | piacomic.jp | 200 |
| HAYAコミック | hayacomic.jp | 200 |
| OurFeel | ourfeel.jp | 200 |
| マンガブ | mangabu.jp | 200 |
| momon:GA | momon-ga.com | 200 |
| あさこみ | asacomi.jp | 200 |
| NamiComi（日文版） | namicomic.jp | 200 |
| マンガタイムズスクエア | mangatime-square.com | 200 |
| コミックシーズンズ | comic-seasons.com | 200 |
| マンガゼグラ | manga-zegra.com | 200 |
| ファイヤークロス | firecross.jp | 200 |
| G-Comi | g-comi.jp | 200 |
| マンガバン | comics.manga-bang.com | 200 |
| まんが王国・関西（マグガーデン） | kansai.mag-garden.co.jp | 200 |
| がうがうモンスター＋ | gaugau.futabanet.jp | 200 |
| コロナEX | to-corona-ex.com | 200 |
| リマコミ＋ | rimacomiplus.jp | 200 |
| オオタウェブコミック | webcomic.ohtabooks.com | 200 |
| 日刊ゲンチャン | nikkangecchan.jp | 200 |
| ジャンプTOON | jumptoon.com | 200 |
| コミックルームベース | comic-room-base.com | 200 |
| 一コミ（一迅社） | ichicomi.com | 200 |
| キミコミ（双葉社） | kimicomi.com | 200 |
| KissLove | klz9.com | 200 |
| COMICポラリス（sai-zen-sen） | sai-zen-sen.jp | 200 |
| J-N Books（成人向） | comic.j-nbooks.jp | 200 |
| アイドル・グラビアプリンセス | idol.gravureprincess.date | 200 |
| ドリームコミック | drecomi-plus.jp | 403（反爬，存活） |
| COMIC熱帯 | comicnettai.com | 404@/（路径问题，域名存活） |
| まんが図書館Z（绝版漫画合法公开存档） | www.mangaz.com | 未测（本轮未覆盖） |

---

### 二、商店（电子漫画 / 同人）

#### DLsite
- 类别: 商店（同人/电子）
- 域名: dlsite.com | www.dlsite.com | play.dlsite.com（阅读器） | login.dlsite.com | img.dlsite.jp（图片 CDN） | cs.dlsite.com（客服） | ch.dlsite.com | dlaf.jp（短域，301→www.dlsite.com） | www.dlsitestudio.com（创作端）
- 性质: 日本最大同人数字内容商店（同人志/音声/游戏），分区路径：/maniax/、/girls/、/home/、/pro/、/soft/、/garumani/、/eng/。
- 来源: [官网](https://www.dlsite.com/index.html)（HTML 引用 www/play/login/cs/ch.dlsite.com）；[官方作品页（引用 img.dlsite.jp）](https://www.dlsite.com/maniax/work/=/product_id/RJ01724124.html)；实测 dlaf.jp→www.dlsite.com、img.dlsite.jp 200
- 后续更新入口: 官网；无官方域名清单页
- 快测: dlsite.com/www 200；img.dlsite.jp 200；play.dlsite.com 200；dlaf.jp 301→dlsite.com；download.dlsite.com 404@/（域存在）；dlsite.jp 404@/（来源不足，勿收）
- 备注: 分区是路径不是域名；图片 CDN 单列 img.dlsite.jp（对抓取/阅读器必需）。dlaf.jp 为官方短域（跳官网）可收。

#### FANZA / DMM（DMM 系）
- 类别: 商店（成人/一般电子书）
- 域名: dmm.co.jp | www.dmm.co.jp/dc/doujin/（FANZA 同人区路径） | book.dmm.co.jp（FANZA 电子书） | dmm.com | book.dmm.com（DMM 一般电子书）
- 性质: 成人向 FANZA（dmm.co.jp）与一般向 DMM（dmm.com）分别是两套 apex；电子书在 book.* 子域。
- 来源: [keiyoushi FANZA 源](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/dmm)（baseUrl book.dmm.co.jp）；[keiyoushi DMM 源](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/dmm)（DMM=book.dmm.com）；实测 dmm.co.jp 200（跳 age_check）、book.dmm.co.jp 200（跳登录）、book.dmm.com 200
- 后续更新入口: keiyoushi src/ja/dmm
- 快测: 均 200
- 备注: 用户名单里的 "book.dmm.co.jp + dmm.co.jp" 正确；补充 book.dmm.com / dmm.com 两个一般向域。无泛子域轮换。

#### Renta!（パピレス）
- 类别: 商店（电子漫画租阅）
- 域名: renta.papy.co.jp | papy.co.jp（运营公司）
- 性质: 株式会社パピレス的电子漫画租阅商店（Renta!）。
- 来源: [官网](https://renta.papy.co.jp/)（实测 200，页面内仅引用 papy.co.jp/renta.papy.co.jp）
- 后续更新入口: 官网；无
- 快测: 200
- 备注: **用户名单里的 renta.com ≠ 日本 Renta!**（实测 renta.com 是欧洲建筑设备租赁公司 Renta Group，勿收）。

#### コミックシーモア
- 类别: 商店
- 域名: www.cmoa.jp | cmoa.jp（apex 无 DNS，仅 www）
- 性质: NTT Solmare 运营的日本最大电子漫画商店之一。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/cmoa)（baseUrl https://www.cmoa.jp）；实测 www.cmoa.jp 200
- 后续更新入口: keiyoushi src/ja/cmoa
- 快测: 200；cmoa.jp apex NXDOMAIN
- 备注: **用户名单里的 cmo.jp 是无关的博彩比较站（301→www.cmo.jp），勿收**；正确域是 www.cmoa.jp。

#### まんが王国（ビーグリー）
- 类别: 商店
- 域名: comic.k-manga.jp（另有 k-manga.jp 301→comic.k-manga.jp） | bv.k-manga.jp（浏览器阅读 API）
- 性质: ビーグリー运营的正规电子漫画商店（不是盗版聚合站）。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangakingdom)（baseUrl comic.k-manga.jp）；[阅读器 API 佐证 bv.k-manga.jp](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangakingdom)（bd00.php）
- 后续更新入口: keiyoushi src/ja/mangakingdom
- 快测: comic.k-manga.jp 200；k-manga.jp 301→comic.k-manga.jp；bv.k-manga.jp 200
- 备注: 用户名单把"漫画王国"放在盗版区 → 实为正规商店，建议归入商店/可直连类。

#### BOOK☆WALKER
- 类别: 商店
- 域名: bookwalker.jp | member.bookwalker.jp（API） | viewer.bookwalker.jp | viewer-trial.bookwalker.jp | viewer-df.bookwalker.jp
- 性质: KADOKAWA 系电子书商店（漫画/轻小说），部分书籍仅日本区。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/bookwalkerjp)（member/viewer/viewer-trial/viewer-df 均见源码）
- 后续更新入口: keiyoushi src/ja/bookwalkerjp
- 快测: bookwalker.jp 200；viewer.bookwalker.jp 404@/（正常，路径型）；member 404@/
- 备注: 阅读器/会员/试用/DF 四个子域建议一并覆盖。

#### BookLive / ebookjapan / honto / Reader Store / dブック / music.jp / FOD / U-NEXT
- 类别: 商店
- 域名: booklive.jp | ebookjapan.yahoo.co.jp | honto.jp | ebookstore.sony.jp | dbook.docomo.ne.jp | music-book.jp | manga.fod.fujitv.co.jp | video.unext.jp | prod-contents-br-page.akamaized.net（ebookjapan 图片 CDN，Akamai）
- 性质: 日本各系正规电子书商店（书类电商）。
- 来源: [keiyoushi booklive](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/booklive)、[ebookjapan](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/ebookjapan)（Akamai CDN 见源码）、[honto 无源-官网实测]、[readerstore](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/readerstore)、[docomo](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/docomo)、[musicbookjp](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/musicbookjp)、[fodfuji](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/fodfuji)、[unext](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/unext)
- 后续更新入口: 对应 keiyoushi 目录
- 快测: booklive.jp 200；ebookjapan.yahoo.co.jp 200；honto.jp 200；ebookstore.sony.jp 200；dbook.docomo.ne.jp 200；music-book.jp 200（→/oversea.html）；manga.fod.fujitv.co.jp 403（反爬，存活）；video.unext.jp 200
- 备注: ebookjapan 图片走 Akamai 共用域，若规则收紧可只收主域。

#### Kindle / Rakuten Kobo（日本区）
- 类别: 商店
- 域名: amazon.co.jp（Kindle 共用商城） | www.kobo.com（JP 区路径 /jp/ja）
- 性质: 两大综合电子书渠道的日本区；均与其他业务共用域名。
- 来源: 官网实测（amazon.co.jp 未测本轮；www.kobo.com/jp/ja 403=Cloudflare 反爬 but 存活）；keiyoushi 无对应源
- 后续更新入口: 无
- 快测: www.kobo.com/jp/ja 403（存活）；jp.kobo.com 无响应/不可用
- 备注: amazon.co.jp 会顺带代理商城全部流量，需用户自行取舍；kobo 建议仅收 /jp 路径所在主域。

#### メロンブックス（Melonbooks）
- 类别: 商店（同人通贩）
- 域名: melonbooks.co.jp | www.melonbooks.co.jp
- 性质: 日本最大同人志通贩之一（实体+DL 同人）。
- 来源: 官网实测；[Rawmangaz/FMHY] 未列（属商业同人渠道）
- 后续更新入口: 无
- 快测: 200
- 备注: 无。

#### とらのあな（Toranoana）
- 类别: 商店（同人通贩）
- 域名: toranoana.jp | www.toranoana.jp | ec.toranoana.jp（通贩）
- 性质: 老牌同人商店，实体店收缩后仍在营通贩。
- 来源: 官网实测
- 后续更新入口: 无
- 快测: toranoana.jp 200；ec.toranoana.jp 200
- 备注: 无。

#### BOOTH / Fantia / pixivFANBOX（同人数字贩售）
- 类别: 商店（同人创作平台）
- 域名: booth.pm | fantia.jp | fanbox.cc | www.fanbox.cc
- 性质: pixiv 系 BOOTH、虎穴系 Fantia、pixiv FANBOX——日本同人数字内容/订阅三大平台。
- 来源: 官网实测（booth.pm 403=Cloudflare 反爬 but 存活；fantia.jp 200；fanbox.cc 200）
- 后续更新入口: 无
- 快测: booth.pm 403（curl -L 实测 200）；fantia.jp 200；fanbox.cc 200
- 备注: 常被用作同人志/画集电子版渠道，漫画规则建议纳入。

---

### 三、聚合 / RAW（高变动，务必定期复核）

> 总体规律：日本 raw/聚合站大量使用 Cloudflare 前置 + 频繁换域（换 TLD / 加 wwNN 数字子域 / 跳转新域名）。
> 规则建议：对"轮换型"用 DOMAIN-SUFFIX（覆盖子域轮换），并定期用 keiyoushi 源 + Rawmangaz 复核。

#### 漫画raw 系（mangaraw）
- 类别: 日本聚合（高变动）
- 域名: mangaraw.to | mangaraw.co（含 wwNN.mangaraw.co 随机子域，实测 ww547.mangaraw.co） | mangaraw.xyz（301→mangaraw.best） | mangaraw.best
- 性质: 日本漫画 raw 聚合（本子/tag 检索型）。
- 来源: [Rawmangaz 清单（FMHY 引用）](https://clarasguide.valeena.workers.dev/Guides/rawmangaz/)（mangaraw.to / mangaraw.xyz）；实测 mangaraw.xyz 301→mangaraw.best、mangaraw.co→ww547.mangaraw.co
- 后续更新入口: Rawmangaz 清单（FMHY 会跟更新）；keiyoushi 无对应源
- 快测: mangaraw.to 200；mangaraw.co 200；mangaraw.best 200
- 备注: 典型"数字子域"轮换站，必须后缀匹配；换终端后可能整域迁移。

#### Rawkuma
- 类别: 日本聚合（高变动）
- 域名: rawkuma.net | rawkuma.com
- 性质: 日本 raw 老牌聚合站，双域并存。
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/rawkuma)（baseUrl rawkuma.net）；[Rawmangaz 清单](https://clarasguide.valeena.workers.dev/Guides/rawmangaz/)（rawkuma.com）
- 后续更新入口: keiyoushi src/ja/rawkuma（baseUrl 变即换）
- 快测: 均 200
- 备注: 两域均收。

#### Hachiraw / Manga1000 / Manga1001（同源站群）
- 类别: 日本聚合（高变动）
- 域名: hachiraw.win（Manga1000 现用） | hachiraw.net（Hachiraw） | cdn.hachiraw.net（图片） | raw1001.net（Manga1001/Raw1001）
- 性质: 同一站群：manga1000/manga1001 已迁到 hachiraw 系 + raw1001.net。
- 来源: [keiyoushi Manga1000](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/manga1000)（homeUrl hachiraw.win）；[keiyoushi Hachiraw](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/hachiraw)（homeUrl hachiraw.net，cdn.hachiraw.net）；[keiyoushi Raw1001](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/raw1001)（homeUrl raw1001.net）
- 后续更新入口: keiyoushi 三个目录
- 快测: hachiraw.win 200；hachiraw.net 403（反爬存活）；cdn.hachiraw.net 500@/；raw1001.net 200
- 备注: 用户名单里的 "manga1001" 当前落点是 raw1001.net；"manga1000" 落点 hachiraw.win。

#### Rawdevart / Rawinu / RawBaka / Dokiraw / Raw18（日语 raw）
- 类别: 日本聚合（高变动）
- 域名: rawdevart.art | rawdevart.com（跳转到 .art） | rawinu.com | rawbaka.com（301→rawbaka.site） | dokiraw.click（301→dokiraw.link） | raw18.icu（301→raw18.bar，18+）
- 性质: 日语 raw/同人扫描聚合站群。
- 来源: [keiyoushi rawdevartart](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/rawdevartart)、[rawinu](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/rawinu)、[rawbaka](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/rawbaka)、[dokiraw](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/dokiraw)、[raw18](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/raw18)（baseUrl 见各自 build.gradle.kts）
- 后续更新入口: keiyoushi 对应目录
- 快测: rawdevart.art/rawdevart.com 200；rawinu.com 200；rawbaka.com 301→rawbaka.site；dokiraw.click 301→dokiraw.link；raw18.icu 301→raw18.bar
- 备注: 四个站都在 2026-10 前后换过域，新旧域名都要收。

#### RawOtaku / RawUwU / RawMiu / Kumaraw / Mangamura
- 类别: 日本聚合（高变动）
- 域名: rawotaku.com | rawuwu.net | rawmiu.com | kumaraw.com | cdn.kumaraw.com | mangamura.me
- 性质: 日语 raw 聚合站群（Cloudflare 前置）。
- 来源: [keiyoushi rawotaku](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/rawotaku)、[rawuwu](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/rawuwu)、[rawxz(RawMiu)](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/rawxz)、[kumaraw](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/kumaraw)（cdn.kumaraw.com）、[mangamura](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangamura)
- 后续更新入口: keiyoushi 对应目录
- 快测: rawotaku.com 200；rawuwu.net 200；rawmiu.com 403（反爬存活）；kumaraw.com 403（反爬存活）；cdn.kumaraw.com 403；mangamura.me 523（源站故障/疑似宕机）
- 备注: mangamura.me 523 需复核；403 多为 Cloudflare 盾，非死站。

#### Manga-5 / MangaNo / MangaMeets / Mangalt / MangaKuro / NihonKuni（mangagun）
- 类别: 日本聚合（高变动）
- 域名: manga-5.com | manga-no.com | manga-meets.jp | mangalt.jp | mangakuro.net | nihonkuni.com
- 性质: 同批日语 raw 聚合（keiyoushi 均有维护源）。
- 来源: [keiyoushi manga five](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangafive)、[mangano](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangano)、[mangameets](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangameets)、[mangalt](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangalt)、[mangakuro](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangakuro)、[mangagun=NihonKuni](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangagun)
- 后续更新入口: keiyoushi 对应目录
- 快测: 均 200（mangakuro.net →/home）
- 备注: keiyoushi 目录名与站名可能不一致（mangagun→NihonKuni 等）。

#### WeLoveManga / Love4u / Yomonga（raw 版）/ SenManga / ソクヨミ（raw 版）
- 类别: 日本聚合（高变动）
- 域名: weloma.net | love4u.net | www.yomonga.com | raw.senmanga.com
- 性质: 另有同名/异名 raw 镜像站群（keiyoushi 的 welovemangaone 指向 love4u.net，rawlh 指向 weloma.net）。
- 来源: [keiyoushi rawlh](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/rawlh)（weloma.net）、[welovemangaone](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/welovemangaone)（love4u.net）、[senmanga](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/senmanga)（raw.senmanga.com）；[Rawmangaz](https://clarasguide.valeena.workers.dev/Guides/rawmangaz/)（senmanga）
- 后续更新入口: keiyoushi 对应目录
- 快测: weloma.net 200；love4u.net 200；raw.senmanga.com 200
- 备注: love4u.net/weloma.net 与官方站名相同易混淆，注意区分。

#### Manga-Zip 系 / ZIP 站群（下载型 raw）
- 类别: 日本聚合（高变动，下载型）
- 域名: manga-zip.my（manga-zip.tv 现跳这里） | manga-zip.app（manga-zip.info→ww28.manga-zip.app） | raw-zip.com | dl-zip.com | 13dl.net | x3-dl.net（manga-zip.to→）
- 性质: 打包下载型 raw（ZIP/RAR），换域最频繁的一族。
- 来源: [Rawmangaz 清单（FMHY 引用）](https://clarasguide.valeena.workers.dev/Guides/rawmangaz/)（manga-zip.is/.info/.to/.tv、raw-zip.com、dl-zip.com、13dl.net）；实测各重定向落点
- 后续更新入口: Rawmangaz 清单
- 快测: manga-zip.info 301→ww28.manga-zip.app；manga-zip.to 301→x3-dl.net；manga-zip.tv 301→manga-zip.my；raw-zip.com 200；dl-zip.com 200；13dl.net 404@/（路径问题）
- 备注: 该族每次换域都变 TLD/词根，建议小范围定期刷新而非长期信任。

#### 其他日语 raw（Rawmangaz / keiyoushi 佐证）
- 类别: 日本聚合（高变动）
- 域名: jraws.net | jpddl.com | rawsakura.org | dlraw.tv（dlraw.net→） | a-zmanga.net | 678dl.net | raw77.com | rawhost.net | manga-raw.club | rawmanga.xyz | klto9.com | klraw.info | jmanga.media（jmanga.cyou→） | kmansin09.top
- 性质: 长尾日语 raw/下载站，活跃度不一。
- 来源: [Rawmangaz 清单](https://clarasguide.valeena.workers.dev/Guides/rawmangaz/)；[keiyoushi klraw](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/klraw)、[klto9](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/klto9)、[kmansin09](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/kmansin09)、[jmanga](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/jmanga)
- 后续更新入口: Rawmangaz + keiyoushi
- 快测: jraws.net 200；jpddl.com 200；rawsakura.org 200；dlraw.net 301→dlraw.tv；a-zmanga.net 200；678dl.net 200；raw77.com 403；rawhost.net 200；manga-raw.club 200；rawmanga.xyz 200；klto9.com 200；klraw.info 523；jmanga.cyou 301→jmanga.media；kmansin09.top 200
- 备注: klraw.info 523 疑似停运（keiyoushi 仍列 baseUrl）；raw77.com 403 反爬。

---

### 四、已确认失效 / 停服 / 误导域名（勿加入或需谨慎）

#### mangacross.jp（マンガクロス老域）
- 类别: 失效（301 归并）
- 域名: mangacross.jp
- 性质: 秋田书店旧"マンガクロス"域名，现 301→championcross.jp。
- 来源: 实测 301（2026-10-05）
- 后续更新入口: 无
- 快测: 301→championcross.jp
- 备注: 仍收流量，规则层面可随 championcross.jp 一起覆盖。

#### webaction.jp / urasunday.com / comic-meteor.jp（老域 301）
- 类别: 失效（301 归并）
- 域名: webaction.jp | urasunday.com | comic-meteor.jp
- 性质: webアクション→comic-action.com；裏サンデー→manga-one.com；コミックメテオ→kirapo.jp/meteor。
- 来源: 实测 301（2026-10-05）
- 后续更新入口: 无
- 快测: 全部 301 生效
- 备注: 域名仍活，只是并入新站；保留覆盖避免漏流量。

#### cmo.jp
- 类别: 误导域名（勿收）
- 域名: cmo.jp | www.cmo.jp
- 性质: 实为日本博彩/ブックメーカー比较站，与コミックシーモア无关。
- 来源: 实测首页 title「おすすめ ブックメーカー 比較ガイド【2026 年最新ランキング】」
- 后续更新入口: 无
- 快测: 301→www.cmo.jp，200
- 备注: コミックシーモア = www.cmoa.jp。

#### renta.com
- 类别: 误导域名（勿收）
- 域名: renta.com
- 性质: 欧洲建筑设备租赁公司 Renta Group，与日本 Renta! 无关。
- 来源: 实测首页 title「Renta Group - North-European Construction Equipment Rental」
- 后续更新入口: 无
- 快测: 200
- 备注: 日本 Renta! = renta.papy.co.jp。

#### manga-mee.jp（改正：实为存活） / manga109.com / raw-free.com / rawload.net / comic-clear.jp
- 类别: 失效（NXDOMAIN）+ 一处更正
- 域名: manga-mee.jp | manga109.com | raw-free.com | rawload.net | comic-clear.jp
- 性质: **manga-mee.jp 经统一实测确认存活**（2026-10-05 实测 200、标题「マンガMee…」；此前"已下线"的判断有误，以 §7 实测为准，建议保留收录）。其余 manga109.com / raw-free.com / rawload.net / comic-clear.jp 均已无 DNS。
- 来源: 统一实测（见 §7）；[keiyoushi MangaMee 源](https://github.com/keiyoushi/extensions-source/tree/main/src/ja/mangamee)（baseUrl 仍在，佐证站点在用）
- 后续更新入口: keiyoushi src/ja/mangamee
- 快测: manga-mee.jp 200（存活）；其余 NXDOMAIN
- 备注: raw-free 无可靠现域名来源，建议放弃或后续单独追踪。

#### klraw.info / mangamura.me / jp.kobo.com
- 类别: 失效/异常（复核）
- 域名: klraw.info | mangamura.me | jp.kobo.com
- 性质: klraw.info 523（Cloudflare 源站异常，疑似停运）；mangamura.me 523（疑似宕机，高变动）；jp.kobo.com 无响应（日本 Kobo 走 www.kobo.com/jp/ja）。
- 来源: 实测（2026-10-05）
- 后续更新入口: 无
- 快测: 523 / 523 / 连接失败
- 备注: 523 可能为临时故障，建议列入"观察名单"定期复测。

---

### 附：本轮采用的验证方法
- 域名现值：keiyoushi 官方索引 index.json 的 `sources[].homeUrl`（构建时写入，最接近"当前可用"），并与各扩展 build.gradle.kts 的 `baseUrl`/`source { baseUrl { custom(...) } }` 交叉核对。
- 域名轮换：以实测 301/302 落点为准（rawbaka/dokiraw/raw18/mangaraw/manga-zip 等）。
- 快测：本机 `socket.gethostbyname` + Python urllib（Chrome UA）访问 `https://域名/`，2026-10-05；403/404/426/500 多为反爬或 API 根路径特性，已在各条目注明。

## 3. 韩国网漫站（基本需代理）

- 调研日期: 2026-10-05
- 调研方法: 官网实测（HTTP + HTML 内引用域名）、各站官方 Telegram 公告频道（t.me/s/ 公开预览）、keiyoushi/extensions-source 的 `src/ko/*/build.gradle.kts`（baseUrl 权威源）、FMHY reading 源文件、Google News RSS（韩媒报道）。**namu.wiki 在本机与 WebFetch 均被 Cloudflare 403 拦截，未能直接引用**，凡涉及 namu.wiki 的内容均改用官方 Telegram / keiyoushi 替代。
- 本机 DNS 被路由器代理劫持（`nslookup` 一律返回 `fdfe:dcba:9876::2`），凡标「解析」的结果均来自 Cloudflare DoH（dns-query）实测；HTTP 码为 curl 直连实测。**超时/连接失败 ≠ 死站**（多为代理/地区封锁）。
- 韩国盗版站域名普遍「数字递增轮换」，下列「当前值」有时间戳，请以各站 Telegram 频道为准。

---

#### 네이버 웹툰 (Naver Webtoon)
- 类别: 韩国官方
- 域名: comic.naver.com | m.comic.naver.com | image-comic.pstatic.net | shared-comic.pstatic.net | naverwebtoon-phinf.pstatic.net
- 性质: 韩国最大官方网漫平台（Naver Webtoon 韩国版），图片走 pstatic 系 CDN。
- 来源: [m.comic.naver.com 首页 HTML 实测引用的 pstatic 域名](https://m.comic.naver.com/)；[comic.naver.com](https://comic.naver.com/)
- 后续更新入口: [navercomic 扩展配置](https://github.com/keiyoushi/extensions-source/blob/main/src/ko/navercomic/build.gradle.kts)（baseUrl=comic.naver.com）
- 快测: comic.naver.com 200 / m.comic.naver.com 200 / image-comic.pstatic.net、shared-comic.pstatic.net、naverwebtoon-phinf.pstatic.net 解析正常
- 备注: 与全球版 webtoons.com 图片 CDN 不同：韩国版=image-comic.pstatic.net，全球版=webtoon-phinf.pstatic.net。

#### 네이버 시리즈 (Naver Series) / 네이버 웹소설
- 类别: 韩国官方
- 域名: series.naver.com | m.series.naver.com | comicthumb-phinf.pstatic.net | ac-full.series.naver.com | novel.naver.com
- 性质: Naver 的漫画+网文付费平台（시리즈），含漫画缩略图 CDN；novel.naver.com 为网文站。
- 来源: [series.naver.com 首页 HTML 实测引用域名](https://series.naver.com/)；[novel.naver.com 200](https://novel.naver.com/)
- 后续更新入口: 无（Naver 官方，域名稳定）
- 快测: series.naver.com 200 / m.series.naver.com 302 / novel.naver.com 200 / comicthumb-phinf.pstatic.net、ac-full.series.naver.com 解析正常
- 备注: gak.comic.naver.com 返回 Error 页（无效子域，不要加规则）。

#### Naver Webtoon 全球版 (WEBTOON)
- 类别: 韩国官方（全球）
- 域名: webtoons.com | www.webtoons.com | m.webtoons.com | webtoon-phinf.pstatic.net
- 性质: Naver 全球版，支持 zh-hant / zh-hans 中文页面（中国大陆用户常用）。
- 来源: [FMHY reading 源文件列 Webtoon→webtoons.com](https://raw.githubusercontent.com/fmhy/edit/main/docs/reading.md)；[www.webtoons.com 首页实测引用 webtoon-phinf.pstatic.net](https://www.webtoons.com/en/)
- 后续更新入口: 无
- 快测: www.webtoons.com 301→/en/ / m.webtoons.com 302 / /zh-hant/、/zh-hans/ 均 200 / webtoon-phinf.pstatic.net 解析正常
- 备注: 另一渠道已在收，此处仅确认。

#### 카카오페이지 (KakaoPage)
- 类别: 韩国官方
- 域名: page.kakao.com | page.kakaocdn.net | dn-img-page.kakao.com
- 性质: 韩国最大综合内容商店（网漫/网文/影视），前端页+静态走 page.kakaocdn.net，作品图片走 dn-img-page.kakao.com。
- 来源: [page.kakao.com 首页 HTML 实测引用 page.kakaocdn.net](https://page.kakao.com/)；[dn-img-page.kakao.com 实测 403 + `via: 1.1 google`（GCP CDN 存活）](https://dn-img-page.kakao.com/)；图片 URL 形态 `https://dn-img-page.kakao.com/download/resource?kid=...&filename=o1`（KakaoPage 内容页缩略图/原图，`o1`=原图 `th3`=缩略图）
- 后续更新入口: 无
- 快测: page.kakao.com 200 / page.kakaocdn.net 解析正常 / dn-img-page.kakao.com 403(CDN 正常)
- 备注: dn-img-page.kakao.com 为已知 KakaoPage 图片 CDN，根路径 403 属正常。

#### 카카오웹툰 (Kakao Webtoon)
- 类别: 韩国官方
- 域名: webtoon.kakao.com | kakaowebtoon.com | kr-a.kakaopagecdn.com | contents.kr.kakaowebtoon.com
- 性质: Kakao 的独立网漫平台；kakaowebtoon.com 为其别名域名（302 到主站），图片/内容走 kakaopagecdn 与 kakaowebtoon 子域。
- 来源: [webtoon.kakao.com 首页 HTML 实测引用 kr-a.kakaopagecdn.com、contents.kr.kakaowebtoon.com](https://webtoon.kakao.com/)；[kakaowebtoon.com 实测 302→https://webtoon.kakao.com/](https://kakaowebtoon.com/)
- 后续更新入口: 无
- 快测: webtoon.kakao.com 200 / kakaowebtoon.com 302→webtoon.kakao.com / kr-a.kakaopagecdn.com、contents.kr.kakaowebtoon.com 解析正常
- 备注: webtoon.kakao.com/th、/zh-hant 返回的是韩文首页（SPA 兜底），海外服务不可据此认定存在。

#### 레진코믹스 (Lezhin Comics)
- 类别: 韩国官方
- 域名: lezhin.com | www.lezhin.com | ccdn.lezhin.com | rcdn.lezhin.com | api.lezhin.com | lezhin-web.lezhin.com | panther.lezhin.com | lezhin.jp
- 性质: 付费网漫平台，韩文主站 lezhin.com；英文版为 www.lezhin.com/en；日文版独立站 lezhin.jp。
- 来源: [www.lezhin.com 首页 HTML 实测引用 ccdn/rcdn/api/panther/lezhin-web 子域](https://www.lezhin.com/)；[www.lezhin.com/en 200 = Lezhin Comics（英）](https://www.lezhin.com/en)；[lezhin.jp 200](https://lezhin.jp/)
- 后续更新入口: 无（官网稳定）
- 快测: www.lezhin.com 200 / lezhin.jp 200 / www.lezhin.com/en 200 / ccdn、rcdn、api、panther、lezhin-web 解析正常
- 备注: 西语/中文已无：www.lezhin.com/es 404、/zh-hant 404、es.lezhin.com 失效、lezhin.com/ja 404（日文只能用 lezhin.jp）。

#### 투믹스 (Toomics)
- 类别: 韩国官方
- 域名: toomics.com | global.toomics.com | thumb-g.toomics.com | thumb-g1.toomics.com | thumb-g2.toomics.com
- 性质: 韩文主站 toomics.com；海外版 global.toomics.com 带 12 个语言路径（en/ja/es/fr/de/it/po/sc/tc/th/as/kr）。
- 来源: [global.toomics.com/en 首页 302→/en 且 HTML 实测引用 thumb-g*.toomics.com 与全部语言路径](https://global.toomics.com/en)；[toomics.com 首页 HTML 实测引用 thumb-g*.toomics.com、global.toomics.com](https://toomics.com/)
- 后续更新入口: 无
- 快测: toomics.com 200 / global.toomics.com 302→/en / thumb-g、thumb-g1、thumb-g2 解析正常
- 备注: 各语言不是独立子域，而是 global.toomics.com/<lang> 路径，规则只需收 global.toomics.com。

#### 탑툰 (TOPTOON) / DAYCOMICS / TOPTOON PLUS
- 类别: 韩国官方
- 域名: toptoon.com | global.toptoon.com | toptoon.net | www.toptoon.net | toptoonplus.com | daycomics.com | smurfs.toptoon.com | azrael.toptoon.com | cdn.megadata.co.kr
- 性质: 韩国付费网漫；www.toptoon.net=**繁体中文官方版**（对中文用户最相关）；daycomics.com、toptoonplus.com 均已改为 JS 跳转 global.toptoon.com；图片/静态子域 smurfs、azrael、cdn.megadata.co.kr。
- 来源: [www.toptoon.net 标题「TOPTOON 漫畫 條漫-國際官方中文版」实测 200](https://www.toptoon.net/)；[daycomics.com 与 toptoonplus.com 页面实测 JS 跳转 global.toptoon.com](https://daycomics.com/)；[toptoon.com 首页 HTML 实测引用 azrael/smurfs.toptoon.com、cdn.megadata.co.kr](https://toptoon.com/)
- 后续更新入口: 无
- 快测: toptoon.com 200 / global.toptoon.com 200 / www.toptoon.net 200 / toptoonplus.com 200(跳转) / daycomics.com 200(跳转) / azrael、smurfs、cdn.megadata.co.kr 解析正常
- 备注: toptoon.net 302→www.toptoon.net（中文站）；DAYCOMICS 已被 TOPTOON 收编，不再是独立站。

#### 봄툰 (Bomtoon)
- 类别: 韩国官方
- 域名: bomtoon.com | www.bomtoon.com | image.balcony.studio | bomtoon.tw | www.bomtoon.tw
- 性质: 女性向（纯情/浪漫/BL）付费网漫；图片 CDN 为 image.balcony.studio；繁体中文版为独立域名 bomtoon.tw。
- 来源: [www.bomtoon.com 与 bomtoon.com 首页 HTML 均实测引用 image.balcony.studio（preconnect/图片）](https://www.bomtoon.com/)；[www.bomtoon.tw 200，标题「BOMTOON - 來自韓國的優質女性向網漫平台」](https://www.bomtoon.tw/)
- 后续更新入口: 无
- 快测: www.bomtoon.com 200 / bomtoon.tw 解析正常+200 / image.balcony.studio 解析正常
- 备注: 旧全球站 global.bomtoon.com 已 NXDOMAIN（见失效节）；bomtoon.com/en、/global 均 404，无英文子站。

#### 미스터블루 (MrBlue)
- 类别: 韩国官方
- 域名: mrblue.com | www.mrblue.com | img.mrblue.com | static.mrblue.com
- 性质: 韩国老牌漫画/网漫/网文平台，图片与静态资源自有子域。
- 来源: [www.mrblue.com 首页 HTML 实测引用 img.mrblue.com、static.mrblue.com](https://www.mrblue.com/)
- 后续更新入口: 无
- 快测: www.mrblue.com 200 / img.mrblue.com、static.mrblue.com 解析正常
- 备注: 无

#### 리디 (RIDI / RIDI Books)
- 类别: 韩国官方
- 域名: ridibooks.com | img.ridicdn.net | static.ridicdn.net | select.ridibooks.com | api.ridibooks.com | active.ridibooks.com | cp.ridibooks.com | ridihelp.ridibooks.com
- 性质: 韩国最大电子书/网漫/网文商店，图片 CDN 为 ridicdn.net 系；select 为订阅制 서비스。
- 来源: [ridibooks.com 首页 HTML 实测引用 img/static.ridicdn.net、api/active/cp/select 子域](https://ridibooks.com/)；[ridibooks.com 200，标题「만화 웹툰 웹소설 도서는 리디」](https://ridibooks.com/)
- 后续更新入口: 无
- 快测: ridibooks.com 200 / img.ridicdn.net、static.ridicdn.net、select、api、active 解析正常
- 备注: ridibooks.com/en 404，无英文站；企业站 ridi.com/ridicorp.com 不必收。

#### 애니툰 (AnyToon)
- 类别: 韩国官方（自有原创+免费馆，非聚合盗版）
- 域名: anytoon.co.kr | www.anytoon.co.kr | m.anytoon.co.kr | cdn.anytoon.co.kr
- 性质: (주)애니툰 运营的正版网漫/网文平台，页面含사업자信息与저작권保护声明，含「무료관」免费区。
- 来源: [www.anytoon.co.kr 首页实测（301→/webtoon/main，页脚「(주)애니툰 사업자 정보」「저작권법에 의거 보호」）](https://www.anytoon.co.kr/webtoon/main)
- 后续更新入口: 无
- 快测: www.anytoon.co.kr 200 / m.anytoon.co.kr、cdn.anytoon.co.kr 解析正常
- 备注: anytoon.com 是待售域名（HugeDomains），勿混用。

---

### 韩国盗版聚合站（域名数字轮换，务必带轮换备注）

#### 뉴토끼 (Newtoki) ★高变动
- 类别: 韩国聚合
- 域名: newto31.com | newtoki1.org | sbxh9.com
- 性质: 最大韩漫/韩文盗版漫画聚合之一；2026-04-27 宣布自我关闭，次日经 Telegram 以新域名复出。
- 来源: [뉴토끼 공지방 Telegram（置顶新地址 newto31.com/마나토끼 mato31.com/북토끼 bookto31.com）](https://t.me/s/newtokinews)；[监控频道列出 뉴토끼 고정주소 sbxh9.com、newtoki1.org（两者同 IP 84.17.37.214）](https://t.me/s/NewToki_Official)；[연합뉴스「불법 웹툰 사이트 '뉴토끼' 자진 폐쇄…"운영자 잡을 차례"(종합)」](https://news.google.com/rss/articles/CBMiW0FVX3lxTE53Y1pKbWlWalFiZV9ITXE4YUMwM3YxSEVEUDN5MURnbTRlTVhpaExyTlUtcThDenIwNnptNUd2cTJYcG5aa0pYX2tkbUprQ3g2eDl5T0FRYTM1MW_SAWBBVV95cUxOQWNULXE5aDZ4OTZ1SWRlUi1YQnlBeHJaSkJHS0hidElwZzlmUGV0N2xqSWJaanM3d0VyNnZ6cnRBcWp5eGpGbUQ0RzdEYXRrYk10TTdIN2NlNS1xU0NRUHk?oc=5)；[연합뉴스「네이버웹툰, '뉴토끼' 폐쇄 후 신규 구매 7.9배 증가」](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5pRUhOdUNTcVgwRjV3UUtORmxOUUNQQ0Z4MDJDVjQtYVJFU09CZldMajQyZ0RVNVRDNDlVakxPWHFxNF9iM0pHLTRtZVZwMVN0MnFNMUhCTmlyTlnSAWBBVV95cUxOeVFwaUlTSktSSmZ2RmNpZ1k4YmlmWUducG42OGZUUENRU1lVTUdISFpSalgyZnloN3Vwak0zbXZ0RjRycXhLQVg2QjFad0M5NHhWQlVOZlA5WmFnY3Nway0?oc=5)
- 后续更新入口: https://t.me/s/newtokinews （官方公告房）；入口页 https://최신토끼.net
- 快测: newto31.com 403(Cloudflare 挑战=存活) / sbxh9.com 200（标题「뉴토끼 — 무료 웹툰 미리보기」）/ newtoki1.org 200（同款标题、同 IP）
- 备注: 两套地址并存（newto31.com vs sbxh9.com+newtoki1.org），来源互相矛盾，建议两条都收；旧编号模式 newtoki###.com 已弃用。

#### 마나토끼 (Manatoki) ★高变动
- 类别: 韩国聚合
- 域名: mato31.com | manatoki555.net
- 性质: 韩文日漫/日漫汉化聚合；2026-04 与뉴토끼/북토끼一起宣布关闭后经 Telegram 复出，运营者 2026-06 被韩国警方逮捕并移送检方后站点仍复活。
- 来源: [뉴토끼 공지방置顶：마나토끼 현재 주소 mato31.com](https://t.me/s/newtokinews)；[연합뉴스「국내 최대 불법 웹툰 사이트 '마나토끼' 운영자 구속 송치」](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBCc2hrWVBveWtDR2lmNXB6QUJ4M05jd3FDRzg1bFBnOFU0VWhxV1RFYmkzdHBVSGtQS1VacjBkZm1Qa09wX3BkUmhyMW9RME1RQ3hUZFZnakMwRDDSAWBBVV95cUxNLUUwNW1YTWRqTzd2T2xXLXRJd005TkY1WU9RRXNralJwc1NXX2lKRmFkSDBkbUNHc3hwQi1Kcy0wdHNaMGNfaV92azdVVmY0OGdWcWxCUmRoOFN3ZFhzamc?oc=5)；[인천일보「[단독] 운영자 검찰 송치됐는데도…서비스 재개한 마나토끼」](https://news.google.com/rss/articles/CBMicEFVX3lxTFA1b3gtZDcxU01Zcmhsa0lEbTE2aGlOQ1JkdTVSbks3ZHlJTGN3ME9OdTQtZlE0SVlmcXpGUHk1ak4zNFhncDNTVWVwemNzcE53RHh0NU1ERUlMZVRVMDU2WEJTeVE3ZkVWN2t0QmRrLUo?oc=5)
- 后续更新入口: https://t.me/s/newtokinews
- 快测: mato31.com 403(Cloudflare 挑战=存活) / manatoki555.net 301→linkbbg8.com（跳转到 주소모음 站）
- 备注: 旧编号 manatoki###.net 仍在跳转（555→linkbbg8.com，550 已停放 parklogic）；keiyoushi 旧值 manatoki552.net 已 SERVFAIL。

#### 북토끼 (Booktoki)
- 类别: 韩国聚合
- 域名: bookto31.com
- 性质: 韩文盗版漫画/小说聚合，뉴토끼 同源运营。
- 来源: [뉴토끼 공지방置顶：북토끼 현재 주소 bookto31.com](https://t.me/s/newtokinews)
- 后续更新入口: https://t.me/s/newtokinews
- 快测: bookto31.com 403(Cloudflare 挑战=存活)
- 备注: 旧编号 booktoki###.com 已弃用；与 newto/mato 同步递增（…29→30→31）。

#### 툰코 (Toonkor) ★高变动
- 类别: 韩国聚合
- 域名: toonkor404.com | toonkor405.com | toonkor0.org | tkor146.com
- 性质: 韩文免费网漫聚合，官方 Telegram 每 1-3 天公布新地址（toonkor###.com 递增）。
- 来源: [툰코 공식 Telegram（2026/10/01：현재주소 toonkor404.com、다음주소 toonkor405.com、평생주소 툰코주소보기.com）](https://t.me/s/toonkorinfo)；[keiyoushi toonkor 扩展 baseUrl=toonkor0.org](https://github.com/keiyoushi/extensions-source/blob/main/src/ko/toonkor/build.gradle.kts)
- 后续更新入口: https://t.me/s/toonkorinfo ；평생주소 https://툰코주소보기.com
- 快测: toonkor404.com 200（「툰코 - 웹툰 사이트」）/ toonkor405.com 未解析（预告下一地址）/ toonkor0.org 解析正常 / tkor146.com 超时
- 备注: 另有第二套编号 tkor###.com（tkor140-146，经监控频道转发），当前多不可达；两套编号都在用，规则建议都收。

#### 블랙툰 (BlackToon)
- 类别: 韩国聚合
- 域名: blacktoon423.com | blacktoon.me | blacktoonurl.net
- 性质: 韩文免费网漫聚合，官方 Telegram 滚动公布 blacktoon###.com；blacktoon.me 是「跟随当前域名」的稳定跳转入口。
- 来源: [블랙툰 공식 Telegram（最新 blacktoon423.com；另有图片加载故障公告页 blacktoonurl.net）](https://t.me/s/blacktoonlink)；[keiyoushi blacktoon 扩展 baseUrl=blacktoon.me](https://github.com/keiyoushi/extensions-source/blob/main/src/ko/blacktoon/build.gradle.kts)
- 后续更新入口: https://t.me/s/blacktoonlink ；指南页 https://blacktoonurl.net
- 快测: blacktoon423.com 200（「BlackToon 블랙툰」）/ blacktoon.me 301→blacktoon423.com / blacktoonurl.net 解析正常
- 备注: **blacktoon.me 是唯一稳定入口（301 追踪当前编号域），强烈建议收**；公告建议开 Cloudflare DNS 或 Unicorn HTTPS 绕过图片加载故障。

#### 마루마루 (MaruMaru)
- 类别: 韩国聚合
- 域名: marumaru103.com | marumaru104.com
- 性质: 韩文日漫/日漫汉化聚合，官方 Telegram 公布 marumaru###.com 递增。
- 来源: [마루마루 공식 Telegram（현재주소 marumaru103.com、다음주소 marumaru104.com、평생주소 마루마루최신주소.com）](https://t.me/s/marumaru_ch)
- 后续更新入口: https://t.me/s/marumaru_ch ；평생주소 https://마루마루최신주소.com
- 快测: marumaru103.com 200（「마루마루 | 무료 웹툰 미리보기」）/ marumaru104.com 未解析（预告下一地址）
- 备注: 编号约每 1-2 周 +1；监控频道亦转发同批地址。

#### 늑대닷컴 / 늑대툰 (Wolf.com / wfwf)
- 类别: 韩国聚合
- 域名: wfwf510.com | wfwf507.com
- 性质: 韩文免费网漫（연재/만화책/포토툰/성인 分区），wfwf###.com 递增，旧域变成「新地址公告页」。
- 来源: [wfwf507.com 页面实测公告「새로운 주소 https://wfwf510.com」](https://wfwf507.com/)；[wfwf510.com 200（标题「늑대닷컴 - 연재웹툰」，页内 Telegram @wolftoon999）](https://wfwf510.com/)；[keiyoushi wolfdotcom 扩展 baseUrl=wfwf507.com](https://github.com/keiyoushi/extensions-source/blob/main/src/ko/wolfdotcom/build.gradle.kts)
- 后续更新入口: https://t.me/wolftoon999（客服/联系）；旧域 wfwf### 公告页会指向新域
- 快测: wfwf510.com 200 / wfwf507.com 200（公告页→wfwf510.com）
- 备注: 收域名时「wfwf 旧号 + 新号」都值得收（旧号起到跳板作用）。

#### 일일툰 / 11toon/11툰 系（含 K만화、쿡마나、spotv）
- 类别: 韩国聚合
- 域名: 11toon.com | www.11toon.com | 11toon149.com | www.11toon149.com | 11toon1.com | spotv147.com | www.spotv147.com | kmana10.net | cookmana56.com
- 性质: 韩文日漫聚合网络（일일툰 血统），官方 Telegram 同时公布多条地址（11toon###/spotv###/kmana##/cookmana##），部分服务器同 IP 段（91.192.107.x）。
- 来源: [11toon 官方 Telegram @toonlink11（현재 최신주소 11toon149.com、spotv147.com、kmana10.net、cookmana56.com；安卓 APK 走 toon123dld.spotv24.com）](https://t.me/s/toonlink11)；[www.11toon.com 首页实测（标题「최신애니 최신만화 일일툰…」，页内 Telegram @toonlink11、兄弟域名 11toon1.com）](https://www.11toon.com/)
- 后续更新入口: https://t.me/s/toonlink11
- 快测: www.11toon.com 200 / www.11toon149.com 200 / kmana10.net 200（K만화）/ cookmana56.com 200（쿡마나）/ www.spotv147.com 超时 / 11toon1.com 解析正常
- 备注: keiyoushi 的 `11toon` 扩展 baseUrl 为 www.11toon.com（[配置](https://github.com/keiyoushi/extensions-source/blob/main/src/ko/toon11/build.gradle.kts)）；编号约每天+1，须靠 Telegram 跟进。

#### 엑스툰 (New XTOON)
- 类别: 韩国聚合（19+）
- 域名: newxtoon1.com
- 性质: 成人网漫聚合（뉴엑스툰），被多个 토끼 监控频道同步公布。
- 来源: [뉴토끼监控频道列出 엑스툰(섹툰) newxtoon1.com](https://t.me/s/NewToki_Official)；[newxtoon1.com 200，标题「뉴엑스툰 - New XTOON」](https://newxtoon1.com/)
- 后续更新入口: https://t.me/s/NewToki_Official（监控频道）
- 快测: newxtoon1.com 200
- 备注: 年龄验证/成人内容站点。

#### 조아툰 (JoaToon)
- 类别: 韩国聚合
- 域名: joa-vip.com
- 性质: 韩文免费网漫聚合，2026 年当前域名为 joa-vip.com（非编号模式）。
- 来源: [뉴토끼监控频道「2026년 조아툰 주소 https://joa-vip.com」](https://t.me/s/NewToki_Official)
- 后续更新入口: https://t.me/s/NewToki_Official
- 快测: joa-vip.com DNS SERVFAIL（本机/DoH 均无解析，疑似再次换域）
- 备注: 待确认站点，规则可先收域名。

#### 굿툰 (GoodToon)
- 类别: 韩国聚合
- 域名: www.goodtoon005.com | www.goodtoon006.com
- 性质: 韩文免费网漫聚合，goodtoon###.com 递增，旧号 301 到新号。
- 来源: [keiyoushi goodtoon 扩展（2026-10-02 新增）baseUrl=www.goodtoon005.com](https://github.com/keiyoushi/extensions-source/blob/main/src/ko/goodtoon/build.gradle.kts)；[www.goodtoon005.com 实测 301→www.goodtoon006.com](https://www.goodtoon005.com/)
- 后续更新入口: keiyoushi goodtoon 扩展配置（域名更新最勤）
- 快测: www.goodtoon005.com 301 / www.goodtoon006.com 解析正常
- 备注: 编号小时级/日级变化，建议只收跳转链上的旧号+新号。

#### RawDEX
- 类别: 韩国聚合（生肉/raw 站，英文界面）
- 域名: rawdex.net
- 性质: 漫画/manhwa/webtoon 生肉阅读站（英文 UI），被 keiyoushi 归入 ko 语言组。
- 来源: [rawdex.net 200，标题「Read Manga, Manhwa & Webtoon Raw Online | RawDEX」](https://rawdex.net/)；[keiyoushi rawdex 扩展 baseUrl=rawdex.net](https://github.com/keiyoushi/extensions-source/blob/main/src/ko/rawdex/build.gradle.kts)
- 后续更新入口: keiyoushi rawdex 配置
- 快测: rawdex.net 200
- 备注: 严格说不是韩国站，但对韩漫生肉有用。

---

### 入口 / 地址聚合站（数字轮换站的「稳定入口」）
- 최신토끼 (xn--h10bt26abuh3me.com / .net): 뉴토끼/마나토끼/북토끼 的实时地址公告页，来源 [뉴토끼 공지방](https://t.me/s/newtokinews)；快测 解析正常(Cloudflare)。
- 툰코주소보기.com (xn--ok0b03z1ndutj89hqne.com): 툰코 공식 평생주소，来源 [툰코 공식 Telegram](https://t.me/s/toonkorinfo)；快测 解析正常。
- 마루마루최신주소.com (xn--2s2ba48db550hj3b2ys7xi.com): 마루마루 공식 평생주소，来源 [마루마루 공식 Telegram](https://t.me/s/marumaru_ch)；快测 解析正常。
- blacktoonurl.net: 블랙툰 公告/指南页（见 블랙툰 条目）；快测 解析正常。
- 링크비비기 linkbbg8.com: 韩国「주소모음」目录站（웹툰/만화/소설 分类，实测页面含 뉴토끼/블랙툰/툰코/늑대닷컴/엑스툰/마나토끼/일일툰/북토끼 入口），来源 [linkbbg8.com 实测](https://linkbbg8.com/)。
- 온도툰.com (xn--hq1bt26abyi.com)、온도마나.com (xn--910b43d93g9lo.com)、온도북.com (xn--hq1bs8p27g.com): 上述目录站自营的网关页（Vercel 托管），来源 [linkbbg8.com 实测链接](https://linkbbg8.com/)；快测 解析正常。

---

### 补充（非韩语 / FMHY 收录的 manhwa 聚合，供参考）
- Toonily — https://toonily.com/（Manhwa / Some NSFW），来源 [FMHY reading](https://raw.githubusercontent.com/fmhy/edit/main/docs/reading.md)；快测 解析正常。
- Mgeko — https://www.mgeko.cc/（Manhwa / Manhua），来源同上；快测 解析正常。
- 注: FMHY reading 页中韩国相关仅 Webtoon/Toonily/Mgeko 三条，韩国本土盗版站 FMHY 未收录。

---

### 已失效 / 已改名 / 已停运（单列，勿直接入规则）
| 域名 | 状态 | 说明与来源 |
|---|---|---|
| comico.co.kr | 疑似停运 | HTTPS 证书不匹配（返回 `*.anybuild.com` 证书）→ 站点已非原服务；NHN 已退出网漫平台业务（[연합뉴스「NHN, 웹툰플랫폼 코미코·포켓코믹스 접는다…"日서비스만 지속"」](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1CdEROUXh2ZVQ3eXdWWUdaTmZYX3g5bkhmQzZoU2p2bWllM2hMaWZ1cmtvcGE1dzhUYUZSa0s3NFB0enVnYklQdFU5Q2lTUUVtbWktaUFIMDVEMFHSAWBBVV95cUxOVWF6MTlXWjVuUEZZTFUwVngxcWFKMjJXcnh5VjNQRUpfVDgwQ2d0TmpRQmFpRjRleHZYRXowM3dVV0t2SFU5MFZ5WHZOMnVJWWpZR3JmQlc3S2liazFocnk?oc=5)）|
| battlecomics.com | 停放(dead) | 实测跳 `/lander`（域名停放模板），배틀코믹스 已停运 |
| webtoon.daum.net | 失效 | DoH 无 A 记录，다음웹툰 已并入 KakaoPage |
| justoon.co.kr / justoon.com | 失效 | DoH SERVFAIL（域名已失效）；저스툰 无现存服务 |
| anytoon.com | 待售 | 302→hugedomains.com 域名出售页（真站是 anytoon.co.kr）|
| global.bomtoon.com | NXDOMAIN | 旧봄툰全球站已下线；现行海外版只有 bomtoon.tw |
| manatoki552.net | SERVFAIL | keiyoushi 曾用 baseUrl，现已无解析（被 mato31.com 取代）|
| manatoki550.net | 停放 | 实测 200→router.parklogic.com 停放页 |
| es.lezhin.com | 失效 | 无响应；西语服务已停止（/es 404）|
| manhwakyung.com | 失效 | 无响应（만화경）|
| gak.comic.naver.com | 无效 | 返回「Error」页，勿收 |
| toonkor405.com | 未上线 | 툰코 Telegram 预告的「다음주소」，尚无解析（预计 1-2 天内启用）|
| marumaru104.com | 未上线 | 마루마루 Telegram 预告的下一地址，尚无解析 |
| newtoki###.com | 旧模式 | 뉴토끼 旧编号域，已弃用（现为 newto##/mato##/bookto## 三站同步编号）|
| booktoki###.com | 旧模式 | 북토끼 旧编号域，已弃用 |
| toptoonplus.com / daycomics.com | 已改名 | 仍是 TOPTOON 资产，JS 跳转 global.toptoon.com（如需可收，属跳转域名）|

---

### 轮换规律速查（用于维护）
- 뉴토끼/마나토끼/북토끼: `newto##.com` / `mato##.com` / `bookto##.com` 三站**同步同号递增**（2026-08 观测 28→29→30→31，约数日一档），公告房 https://t.me/s/newtokinews ；旧模式 newtoki###.com、manatoki###.net、booktoki###.com 已弃用。
- 툰코: `toonkor###.com` 递增，约 1-2 天 +1（2026-09-09=401 → 2026-10-01=404），公告 https://t.me/s/toonkorinfo ；另有 tkor###.com 第二套编号。
- 블랙툰: `blacktoon###.com` 递增，约数日 +1（2026 年观测 417→423），公告 https://t.me/s/blacktoonlink ；稳定入口 blacktoon.me。
- 마루마루: `marumaru###.com` 递增（100→104，约 1-2 周/档），公告 https://t.me/s/marumaru_ch 。
- 늑대닷컴: `wfwf###.com` 递增（507→510），旧域自动变成新域公告页，无独立 Telegram 公告房（只有 @wolftoon999 联系号）。
- 11toon 系: `11toon###.com` + `spotv###.com` 每日 +1，另发 kmana##/cookmana## 兄弟站，公告 https://t.me/s/toonlink11 。
- 굿툰: `goodtoon###.com`（005→006），旧号 301 跳新号，keiyoushi 更新最快。

## 4. 英文 / 全球漫画站（基本需代理）

- 调研日期: 2026-10-05（域名变化快，使用前请看各站"后续更新入口"复查）
- 调研范围: 主流平台 / 聚合站 / Webtoon 全球版 / 成人本子阅读站
- 快测说明: 本机 curl（中国大陆、路由器代理）。`000`=连接失败（不一定是死站）；`403`/`Just a moment` 多为 Cloudflare 盾；`301/302` 多为规范化跳转。
- **重大背景**: 全球最大漫画聚合站 Batoto(bato.to) 2025-11-19 站长被中国警方拘留，2026-01 约 60 个关联站被日本 CODA + Kakao P.CoK 联合行动全部关停。`bato.*` 全域域名已被接管，302 跳到 CODA 关闭公告页。原 Batoto 官方镜像域名列表（batotwo/mangatoto/readtoto 等）已全部失效，见文末"已确认失效"节。

### 主要来源与方法

- FMHY Reading 页（实际内容源为 GitHub wiki raw）: https://raw.githubusercontent.com/wiki/fmhy/FMHY/Reading.md （渲染页 https://fmhy.net/reading ）
- keiyoushi/extensions-source（Mihon/Tachiyomi 官方扩展源，聚合站域名最权威的实时索引）: https://github.com/keiyoushi/extensions-source/tree/main/src/en
- EHWiki（e-hentai 域名/IP 权威 wiki）: https://ehwiki.org/wiki/IPs 、 https://ehwiki.org/wiki/Technical_Issues
- EhViewer 源码（域名常量）: https://github.com/FooIbar/EhViewer/blob/main/app/src/main/kotlin/com/hippo/ehviewer/client/EhUrl.kt
- nhentai 官方 API: https://nhentai.net/api/v2/cdn （直接返回图床域名）
- hitomi.la 官方脚本: https://ltn.gold-usergeneratedcontent.net/common.js
- CODA 官方公告: https://coda-cj.jp/en/news/830 ；关闭页: https://coda-cj.jp/closed.html
- Anime News Network（2026-01-31）: https://www.animenewsnetwork.com/news/2026-01-31/major-manga-manhwa-pirate-site-bato.to-shuts-down-chinese-man-suspected-as-operator-detained/.233670
- Reddit r/mangapiracy（社区状态跟踪）: https://www.reddit.com/r/mangapiracy/

---

### 一、主流平台

#### MangaDex
- 类别: 主流平台
- 域名: mangadex.org | api.mangadex.org | auth.mangadex.org | uploads.mangadex.org | forums.mangadex.org | status.mangadex.org
- 性质: 全球最大社区漫画平台（官方授权 + 社区上传混合，社区运营）
- 来源: [MangaDex Status](https://status.mangadex.org/)（官方状态页，组件 Website/API/CDN/MangaDex@Home）；[MangaDex API Docs](https://api.mangadex.org/docs/)（官方确认 api.mangadex.org，含 security.txt）；[gallery-dl mangadex 提取器](https://github.com/mikf/gallery-dl/blob/master/gallery_dl/extractor/mangadex.py)（mangadex.org / api.mangadex.org / auth.mangadex.org）
- 后续更新入口: https://status.mangadex.org/ （官方状态页，支持 RSS/Atom: /history.rss）
- 快测: mangadex.org: 200；api.mangadex.org: 308（→/docs）；uploads.mangadex.org: 200
- 备注: 章节图源经 API `/at-home/server` 动态分配（MD@Home P2P 节点），规则建议整域覆盖 `*.mangadex.org`（含上面未列全的子域）。无 Cloudflare 盾。

#### VIZ (Shonen Jump)
- 类别: 主流平台
- 域名: viz.com | www.viz.com
- 性质: VIZ Media 官方（Shonen Jump 订阅、数字单行本）
- 来源: [VIZ 官网](https://www.viz.com/)；[keiyoushi VIZ 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/vizshonenjump/build.gradle.kts)（baseUrl = https://www.viz.com）
- 后续更新入口: 无
- 快测: viz.com: 301 → www.viz.com
- 备注: 订阅墙。

#### Comikey
- 类别: 主流平台
- 域名: comikey.com | media.comikey.com
- 性质: 正版付费漫画平台（Square Enix 等授权）
- 来源: [Comikey 官网](https://comikey.com/)（本次实测首页 HTML 688 次引用 media.comikey.com）
- 后续更新入口: 无
- 快测: comikey.com: 200
- 备注: media 子域为漫画图源；订阅墙。

#### INKR
- 类别: 主流平台
- 域名: inkr.com | comics.inkr.com
- 性质: 正版漫画订阅平台
- 来源: [keiyoushi INKR 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/inkr/build.gradle.kts)（baseUrl = https://comics.inkr.com）；实测 inkr.com 301 → comics.inkr.com
- 后续更新入口: 无
- 快测: inkr.com: 301 → comics.inkr.com；comics.inkr.com: 200
- 备注: 主站已统一到 comics 子域。

#### Azuki → Omoi（改名，非关站）
- 类别: 主流平台
- 域名: omoi.com | www.omoi.com | azuki.co（旧域过渡）
- 性质: 正版漫画订阅服务；Azuki 于 2025-11 更名 Omoi，内容/价格不变
- 来源: [Omoi 官网](https://www.omoi.com/)（实测标题 "Omoi — Read officially licensed digital manga"）；Good e-Reader 报道更名（2025-11，搜索确认）
- 后续更新入口: 无
- 快测: azuki.co: 301 → www.azuki.co: 302 → www.omoi.com: 200
- 备注: 保留 azuki.co 作旧域兜底。

#### MANGA Plus（确认）
- 类别: 主流平台
- 域名: mangaplus.shueisha.co.jp
- 性质: 集英社官方免费平台（含西语版）
- 来源: [MANGA Plus 官网](https://mangaplus.shueisha.co.jp/)
- 后续更新入口: 无
- 快测: mangaplus.shueisha.co.jp: 200
- 备注: 实测 img.mangaplus.shueisha.co.jp 不存在（NXDOMAIN），无需额外图源子域。

#### BookWalker 全球版
- 类别: 主流平台
- 域名: bookwalker.com | global.bookwalker.jp（旧域，已迁移）
- 性质: Kadokawa 电子漫画商店全球版
- 来源: 实测重定向 global.bookwalker.jp → bookwalker.com/migration/；[keiyoushi BookWalker 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/bookwalker/build.gradle.kts)（baseUrl = https://bookwalker.com）
- 后续更新入口: 无
- 快测: bookwalker.com: 200；global.bookwalker.jp: 301 → bookwalker.com/migration/
- 备注: 日本本土站 bookwalker.jp 不在此清单。

#### Kodansha / K Manga（起步名单外补充）
- 类别: 主流平台
- 域名: kodansha.us | kmanga.kodansha.com
- 性质: 讲谈社英文官方站 / K Manga 官方平台
- 来源: [keiyoushi K Manga 源](https://github.com/keiyoushi/extensions-source/blob/main/src/en/kmanga/build.gradle.kts)；[keiyoushi Kodansha 源](https://github.com/keiyoushi/extensions-source/blob/main/src/en/kodansha/build.gradle.kts)
- 后续更新入口: 无
- 快测: 未单独快测（keiyoushi 活跃维护的官方源）
- 备注: 补充项。

---

### 二、聚合站

#### MangaNato / MangaKakalot 家族
- 类别: 聚合站
- 域名: natomanga.com | manganato.gg | nelomanga.net | mangakakalot.gg | mangakakalove.com
- 性质: 同源聚合站家族（Megane 系）；旧 .com 域已官方关闭（见"已失效"）
- 来源: [keiyoushi Manganato 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/manganelo/build.gradle.kts)（mirrors: natomanga.com / nelomanga.net / manganato.gg）；[keiyoushi Mangakakalot 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangakakalot/build.gradle.kts)（mirrors: mangakakalot.gg / mangakakalove.com）；[MALSync issue #2860](https://github.com/MALSync/MALSync/issues/2860)（迁移记录）；FMHY Reading 页
- 后续更新入口: https://github.com/keiyoushi/extensions-source （issue/commit，无官方公告页）
- 快测: natomanga.com: 301→www(200)；manganato.gg: 301→www(200)；nelomanga.net: 301；mangakakalot.gg: 301→www(200)；mangakakalove.com: 301
- 备注: 仿冒站极多；www.mangakakalot.gg 标题 "MangaKakalot | Read Manga Online Free"，www.natomanga.com 标题 "MangaNato"。

#### MangaHere
- 类别: 聚合站
- 域名: mangahere.cc
- 性质: 老牌聚合站（与 FanFox 同运营谱系）
- 来源: [keiyoushi Mangahere 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangahere/build.gradle.kts)（baseUrl = https://www.mangahere.cc）；FMHY Reading 页
- 后续更新入口: 无
- 快测: mangahere.cc: 301 → www.mangahere.cc（http）
- 备注: 广告多。

#### MangaFox / FanFox
- 类别: 聚合站
- 域名: fanfox.net
- 性质: 老牌聚合站（mangafox.me 的现役域）
- 来源: [keiyoushi MangaFox 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangafox/build.gradle.kts)（baseUrl = https://fanfox.net）；FMHY Reading 页
- 后续更新入口: 无
- 快测: fanfox.net: 200
- 备注: 移动端 m.fanfox.net（未单独验证）。

#### MangaPill
- 类别: 聚合站
- 域名: mangapill.com
- 性质: 简洁型聚合站（无广告，口碑较好）
- 来源: [keiyoushi MangaPill 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangapill/build.gradle.kts)；FMHY Reading 页
- 后续更新入口: 无
- 快测: mangapill.com: 200
- 备注: 图源 CDN 未验证，可先只收主域。

#### Weeb Central
- 类别: 聚合站
- 域名: weebcentral.com
- 性质: MangaSee 风格干净聚合站
- 来源: [keiyoushi Weeb Central 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/weebcentral/build.gradle.kts)；FMHY Reading 页
- 后续更新入口: 无
- 快测: weebcentral.com: 200（实测标题 "Weeb Central"）
- 备注: 图源同域。

#### Comix
- 类别: 聚合站
- 域名: comix.to | comix.ws
- 性质: Batoto 倒下后的新兴聚合站（FMHY + keiyoushi 双双收录）
- 来源: [keiyoushi Comix 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/comix/build.gradle.kts)（mirrors: comix.to / comix.ws）；FMHY Reading 页
- 后续更新入口: FMHY Reading 页 / keiyoushi repo
- 快测: comix.to: 403（Cloudflare "Just a moment..." 人机盾）
- 备注: CF 盾。

#### MangaFire
- 类别: 聚合站
- 域名: mangafire.to
- 性质: 新兴聚合站（界面现代、多语言）
- 来源: FMHY Reading 页
- 后续更新入口: FMHY Reading 页
- 快测: mangafire.to: 200（标题 "MangaFire - Read Manga Online Free"）
- 备注: 广告/弹窗。

#### MangaKatana
- 类别: 聚合站
- 域名: mangakatana.com
- 性质: 中型聚合站
- 来源: [keiyoushi MangaKatana 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangakatana/build.gradle.kts)；FMHY Reading 页
- 后续更新入口: 无
- 快测: mangakatana.com: 200
- 备注: 无盾。

#### MangaHub
- 类别: 聚合站
- 域名: mangahub.io
- 性质: 大型聚合站
- 来源: [keiyoushi MangaHub 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangahubio/build.gradle.kts)；FMHY Reading 页
- 后续更新入口: 无
- 快测: mangahub.io: 403（CF 盾）
- 备注: CF 盾。

#### MangaGo
- 类别: 聚合站
- 域名: mangago.me
- 性质: 老牌聚合站（大量 BL/yaoi）
- 来源: [keiyoushi Mangago 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangago/build.gradle.kts)
- 后续更新入口: 无
- 快测: mangago.me: 403（CF 盾）
- 备注: CF 盾。

#### MangaTown 系列（MangaTown / MangaBat / MangaNel / MangaRead.org / MangaReader.site）
- 类别: 聚合站（合并列出）
- 域名: mangatown.com | mangabats.com | manganel.me | mangaread.org | mangareader.site
- 性质: 各自独立的中小型聚合站（MangaReader.site 与已死的 mangareader.to 无关）
- 来源: [keiyoushi Mangatown](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangatown/build.gradle.kts)、[Mangabat](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangabat/build.gradle.kts)、[MangaNel](https://github.com/keiyoushi/extensions-source/blob/main/src/en/manganel/build.gradle.kts)、[MangaRead.org](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangareadorg/build.gradle.kts)、[MangaReader.site](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangareadersite/build.gradle.kts)；FMHY Reading 页
- 后续更新入口: 无
- 快测: mangatown.com: 301→www；mangabats.com: 301→www；manganel.me: 200；mangaread.org: 301→www(200)；mangareader.site: 200
- 备注: 全部活跃。

#### MangaBuddy → Comizy
- 类别: 聚合站
- 域名: mangabuddy.com | comizy.io
- 性质: MangaBuddy 已改名/迁移为 Comizy（mangabuddy.com 现 301 到 comizy.io，站内品牌已换）
- 来源: 实测 mangabuddy.com 301 → comizy.io；[Reddit r/mangapiracy "Mangabuddy Redirect"](https://www.reddit.com/r/mangapiracy/comments/1tc394b/mangabuddy_redirect)（社区确认改链接/名/logo）
- 后续更新入口: r/mangapiracy
- 快测: mangabuddy.com: 301 → comizy.io；comizy.io: 200
- 备注: 网传 mangabuddy1.com 等疑似仿冒，勿收。

#### MangaK
- 类别: 聚合站
- 域名: mangak.io
- 性质: 现占 keiyoushi "mangabuddy" 源位的独立站
- 来源: [keiyoushi 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangabuddy/build.gradle.kts)（name = "MangaK", baseUrl = mangak.io）；FMHY Reading 页
- 后续更新入口: 无
- 快测: mangak.io: 200
- 备注: 与 MangaBuddy 已无关系。

#### ManhuaUS
- 类别: 聚合站
- 域名: manhuaus.com
- 性质: 国漫/韩漫英文聚合站
- 来源: [keiyoushi ManhuaUS 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/manhuaus/build.gradle.kts)
- 后续更新入口: 无
- 快测: manhuaus.com: 403（CF 盾）
- 备注: CF 盾。

#### Toonily
- 类别: 聚合站
- 域名: toonily.com
- 性质: Manhwa/Webtoon 聚合站（成人向内容多）
- 来源: [keiyoushi Toonily 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/toonily/build.gradle.kts)；FMHY Reading 页
- 后续更新入口: 无
- 快测: toonily.com: 200
- 备注: 无盾。

#### Dynasty Scans
- 类别: 聚合站（百合专门扫描站）
- 域名: dynasty-scans.com
- 性质: Yuri 百合漫画扫描站（半社区性质）
- 来源: [keiyoushi Dynasty 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/dynasty/build.gradle.kts)
- 后续更新入口: 无
- 快测: dynasty-scans.com: 200（标题 "Dynasty Reader"）
- 备注: 长期稳定。

#### MangaUpdates（数据库补充）
- 类别: 数据库（非阅读站）
- 域名: mangaupdates.com | www.mangaupdates.com
- 性质: 漫画元数据库/发布情报（Baka-Updates Manga）
- 来源: FMHY Reading 页
- 后续更新入口: 无
- 快测: www.mangaupdates.com: 200
- 备注: 阅读器 App 高频访问，建议收录。

#### xBato / bato1.com（Batoto 同名新站，非原官方）
- 类别: 聚合站（身份未核实的同名新站）
- 域名: bato1.com
- 性质: 原 Batoto 关停后出现的同名新站（keiyoushi 源名 "Bbato"），**非原官方运营方**
- 来源: [keiyoushi Bbato 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/bbato/build.gradle.kts)（baseUrl = https://bato1.com）；实测标题 "Batoto — Read BL Manga, Manhwa & Yaoi Online Free (2026) | xBato"
- 后续更新入口: 无
- 快测: bato1.com: 200
- 备注: 谨慎对待，来源不明。

---

### 三、Webtoon 全球版（Naver）

#### Webtoon
- 类别: 主流平台（Naver 旗下）
- 域名: webtoons.com | www.webtoons.com | m.webtoons.com | webtoon-phinf.pstatic.net（图源）| webtoons-static.pstatic.net（静态资源）| webtoon.com | shop.webtoon.com | creators.webtoon.com | advertising.webtoon.com | about.webtoon.com
- 性质: Naver Webtoon 英文/全球版
- 来源: [www.webtoons.com/en/ 首页 HTML](https://www.webtoons.com/en/)（本次实测提取：webtoon-phinf.pstatic.net ×87、webtoons-static.pstatic.net、m.webtoons.com、webtoon.zendesk.com、shop/creators/advertising/about.webtoon.com）
- 后续更新入口: 无
- 快测: webtoons.com: 301 → www.webtoons.com: 301 → /en/；m.webtoons.com: 302
- 备注: 图源全部在 pstatic.net（Naver 自有 CDN，与 Naver 其它服务共域，若按 `*.pstatic.net` 收会误伤，建议只收上面两个具体子域）。

---

### 四、成人/本子阅读站

#### E-Hentai / ExHentai 全家桶
- 类别: 成人
- 域名: e-hentai.org | exhentai.org | forums.e-hentai.org | api.e-hentai.org | s.exhentai.org | upload.e-hentai.org | repo.e-hentai.org | xml.e-hentai.org | ehgt.org | ehtracker.org | ehwiki.org | hentaiathome.net | rpc.hentaiathome.net | hath.network | hentaiverse.org | alt.hentaiverse.org
- 性质: 全球最大图库/本子画廊站 + 官方配套（API、图床、论坛、BT tracker、wiki、H@H P2P 网络）
- 来源: [EHWiki IPs 页](https://ehwiki.org/wiki/IPs)（官方 IP 表: e-hentai.org / forums / repo / xml / api.e-hentai.org、ehgt.org、ehtracker.org、hentaiathome.net、rpc.hentaiathome.net、upload.e-hentai.org、ehwiki.org、hentaiverse.org、alt.hentaiverse.org；2025-11-26 更新）；[EHWiki Technical Issues](https://ehwiki.org/wiki/Technical_Issues)（ehgt.org 图片白名单、rpc.hentaiathome.net）；[EhViewer EhUrl.kt](https://github.com/FooIbar/EhViewer/blob/main/app/src/main/kotlin/com/hippo/ehviewer/client/EhUrl.kt)（DOMAIN_E=e-hentai.org；DOMAIN_EX=exhentai.org；API_E=api.e-hentai.org/api.php；API_EX=s.exhentai.org/api.php；上传 upload.e-hentai.org/image_lookup.php）；hath.network 来源: 官方 H@H 下载页 repo.e-hentai.org/hath/ + DNS 记录（CAA mailto:staff@e-hentai.org、SOA support@e-hentai.org）；图片 URL 形如 `https://{subdomain}.hath.network/h/{hash}/...`
- 后续更新入口: https://ehwiki.org/wiki/IPs （官方 IP/域名表，最重要的复查入口）
- 快测: e-hentai.org: 200；exhentai.org: 302（无登录态跳 forums remoteapi，属正常）；api.e-hentai.org: 404（根路径，API 在 /api.php，正常）；ehgt.org: 403（图片域根 403，正常）；hath.network: nslookup 可解析（178.162.151.57，Leaseweb NL）
- 备注: exhentai.org 需要登录态 + 特定 cookie（sadpanda）；s.exhentai.org 为 ex 的 API 端点（唯一来源为 EhViewer 等官方客户端代码）；hath.network 为 H@H 图片分发域，子域动态派生，规则建议整域 `*.hath.network`；ehtracker.org 为 BT tracker。

#### nhentai
- 类别: 成人
- 域名: nhentai.net | i1.nhentai.net | i2.nhentai.net | i3.nhentai.net | i4.nhentai.net | t1.nhentai.net | t2.nhentai.net | t3.nhentai.net | t4.nhentai.net
- 性质: 大型英文同人本子站（官方）
- 来源: [nhentai 官方 API v2 /cdn](https://nhentai.net/api/v2/cdn)（官方端点直接返回 image_servers=[i1-i4.nhentai.net]、thumb_servers=[t1-t4.nhentai.net]，本次实测）；文档 https://nhentai.net/api/v2/docs
- 后续更新入口: https://nhentai.net/api/v2/docs （官方 API 文档）
- 快测: nhentai.net: 403（CF 盾）；i.nhentai.net: NXDOMAIN（不存在，勿收）；/api/v2/cdn: 200 返回上述服务器列表
- 备注: **官方只有 .net 域**；网上 nhentai.xxx/.to/.io 等一律非官方镜像（本次未收录）。

#### hitomi.la
- 类别: 成人
- 域名: hitomi.la | gold-usergeneratedcontent.net（图片/静态 CDN 基域，任意子域如 a.、b.、ltn.）| ltn.gold-usergeneratedcontent.net（静态 JS）
- 性质: 大型在线画廊/本子站（官方）
- 来源: [hitomi.la 首页](https://hitomi.la/)（HTML 引用 ltn.gold-usergeneratedcontent.net 系列 JS）；[官方脚本 common.js](https://ltn.gold-usergeneratedcontent.net/common.js)（定义 `domain2='gold-usergeneratedcontent.net'` 及图片 URL 子域派生逻辑 `url_from_url`；含 dev.hitomi.la / master.hitomi.la 字符串）
- 后续更新入口: 无（可关注其自身脚本变化）
- 快测: hitomi.la: 200；ltn.gold-usergeneratedcontent.net/gg.js: 200（实测抓取成功）；ltn.gold: NXDOMAIN（旧域名方案已废）
- 备注: 图片子域为哈希动态派生（形如 `a{nn}.gold-usergeneratedcontent.net`），规则须用 `gold-usergeneratedcontent.net` 通配整域；旧资料里的 `ltn.gold`、`hitomi.la/gg.js` 均已失效。

#### IMHentai
- 类别: 成人
- 域名: imhentai.xxx | imhentai.to | imhentai.com
- 性质: 大型本子画廊站
- 来源: 实测（.xxx 200；.com 返回 "Redirecting..." 跳转页）；第三方流量统计确认 .xxx 为主域（.to 为活跃镜像，SEMrush 数据，见搜索记录）
- 后续更新入口: 无
- 快测: imhentai.xxx: 200；imhentai.com: 200（重定向页）；imhentai.to: 未单独快测（搜索称活跃）
- 备注: 多域并存，建议全收。

#### HentaiFox
- 类别: 成人
- 域名: hentaifox.com | i1.hentaifox.com | i2.hentaifox.com | i3.hentaifox.com | hentaigold.net | go.hentaigold.net
- 性质: 大型本子画廊站（附姊妹站 HentaiGold）
- 来源: 实测首页 HTML（本次抓取：i3.hentaifox.com ×30、go.hentaigold.net ×4）
- 后续更新入口: 无
- 快测: hentaifox.com: 200
- 备注: 图片域为 i1/i2/i3 编号子域；hentaigold.net 为其姊妹站，是否收看需求。

#### Hentai2Read
- 类别: 成人
- 域名: hentai2read.com | img1.hentaicdn.com | img2.hentaicdn.com | img3.hentaicdn.com | script.hentaicdn.com
- 性质: 大型本子阅读站
- 来源: 实测首页 HTML（img1/2/3.hentaicdn.com、script.hentaicdn.com）
- 后续更新入口: 无
- 快测: hentai2read.com: 200
- 备注: 图源 hentaicdn.com 家族。

#### Simply-Hentai
- 类别: 成人
- 域名: simply-hentai.com | www.simply-hentai.com
- 性质: 英文本子阅读站
- 来源: 实测（simply-hentai.com: 301 → www.simply-hentai.com）
- 后续更新入口: 无
- 快测: simply-hentai.com: 301 → www（308 于 www）
- 备注: -

#### Multporn
- 类别: 成人
- 域名: multporn.net
- 性质: 成人漫画阅读站
- 来源: [keiyoushi Multporn 源配置](https://github.com/keiyoushi/extensions-source/blob/main/src/en/multporn/build.gradle.kts)
- 后续更新入口: 无
- 快测: multporn.net: 200
- 备注: -

#### Luscious
- 类别: 成人
- 域名: luscious.net
- 性质: 成人漫画/图库社区
- 来源: 实测
- 后续更新入口: 无
- 快测: luscious.net: 403（CF 盾）
- 备注: CF 盾，需代理后过验证。

#### HBrowse
- 类别: 成人
- 域名: hbrowse.com
- 性质: 老牌英文本子浏览站
- 来源: 实测
- 后续更新入口: 无
- 快测: hbrowse.com: 200
- 备注: -

#### Fakku
- 类别: 成人（正版）
- 域名: fakku.net | www.fakku.net
- 性质: 正版本子发行/阅读平台（付费）
- 来源: 实测（fakku.net: 301 → www.fakku.net；www: 451 区域限制响应）
- 后续更新入口: 无
- 快测: fakku.net: 301 → www.fakku.net；www.fakku.net: 451（Unavailable For Legal Reasons，疑似区域封锁）
- 备注: 正版付费；451 可能需特定区域节点。

#### Irodori Comics
- 类别: 成人（正版）
- 域名: irodoricomics.com
- 性质: 正版英文成人同人漫画发行商
- 来源: 实测
- 后续更新入口: 无
- 快测: irodoricomics.com: 200（无标题，JS 站）
- 备注: 正版。

#### 成人站补充（keiyoushi 收录，部分未快测）
- 类别: 成人
- 域名: hentainexus.com | hentaihere.com | hentairead.com | doujins.com | comics.8muses.com | allporncomic.com | 18porncomic.com | myhentaigallery.com | xlecx.one
- 性质: keiyoushi 扩展源收录的其它成人漫画源（低优先级备选）
- 来源: 各源 build.gradle.kts，例: [HentaiNexus](https://github.com/keiyoushi/extensions-source/blob/main/src/en/hentainexus/build.gradle.kts)、[HentaiHere](https://github.com/keiyoushi/extensions-source/blob/main/src/en/hentaihere/build.gradle.kts)、[Multporn](https://github.com/keiyoushi/extensions-source/blob/main/src/en/multporn/build.gradle.kts)、[8Muses](https://github.com/keiyoushi/extensions-source/blob/main/src/en/eightmuses/build.gradle.kts)、[AllPornComic](https://github.com/keiyoushi/extensions-source/blob/main/src/en/allporncomic/build.gradle.kts)
- 后续更新入口: https://github.com/keiyoushi/extensions-source/tree/main/src/en
- 快测: hentainexus.com: 200；hentaihere.com: 200；其余未单独快测
- 备注: 数量众多，完整列表见 keiyoushi src/en 目录（含 hentai1io、hentaikun 等更多源）。

---

### 五、已确认失效（附证据，勿再用于分流或直接归档）

#### Batoto 全网络（2026 大案）
- 状态: 2025-11-19 站长在中国被拘留；2026-01 约 60 个关联站全部关停；`bato.*` 域名被反盗版组织接管。
- 证据: [CODA 官方公告](https://coda-cj.jp/en/news/830)（"Operator of the World's Largest Manga Piracy Site BATO."，非法传播日/中/韩漫画、超 50 种语言、约 3.5 亿月访问、约 60 站）；[Anime News Network 2026-01-31](https://www.animenewsnetwork.com/news/2026-01-31/major-manga-manhwa-pirate-site-bato.to-shuts-down-chinese-man-suspected-as-operator-detained/.233670)；[CODA 关闭页](https://coda-cj.jp/closed.html)（实测 bato.to/bato.si/battwo.com 等 302 至此，页面写 "THIS WEBSITE HAS BEEN CLOSED DUE TO COPYRIGHT INFRINGEMENT."）
- 死亡/被接管域名: bato.to | bato.si | bato.ing | battwo.com | batotwo.com（均 302 → coda-cj.jp/closed.html）；mangatoto.net（301 → hqtotobos.com，域名疑似被转售/接管）；readtoto.com（无响应）；comiko.net（历史镜像，随网络关停）
- 注意: bato1.com 是关停后出现的同名新站（见聚合站节 "xBato"），与原官方无关。

#### Manganato / MangaKakalot 旧 .com 域
- 状态: 三站均显示官方关闭页（实测标题 "This site is closed."）
- 域名: manganato.com | mangakakalot.com | manganelo.com
- 证据: 实测（403 + "This site is closed." 标题）；[MALSync issue #2860](https://github.com/MALSync/MALSync/issues/2860)
- 替代: 见聚合站 "MangaNato/MangaKakalot 家族"（natomanga.com / *.gg 等）。

#### MangaReader.to
- 状态: 无响应（DNS 仍有 Cloudflare 地址，但连接失败/超时；社区无官方替代公告）
- 域名: mangareader.to
- 证据: 实测 000 + nslookup（104.21.36.254 / 172.67.201.162 但连不上）
- 注意: 现役 mangareader.site（200）是另一独立站，与 .to 无继承关系。

#### MangaOwl 原站（混乱，不建议收录）
- 状态: 原站已死/身份混乱；官方域不可考。
- 域名: mangaowl.net（302 → router.parklogic.com 域名停放商，彻底死）| mangaowl.to（200 但页面无标题，疑似空壳）| mangaowl.io（200，Cloudflare 拦截页；keiyoushi 源名直接标注 "MangaOwl.io (unoriginal)" 非原站）| mangaowl.one（NXDOMAIN）
- 证据: 实测；[keiyoushi MangaOwl.io 源](https://github.com/keiyoushi/extensions-source/blob/main/src/en/mangaowlio/build.gradle.kts)（name = "MangaOwl.io (unoriginal)"）

#### MangaPark（半死，不建议收录）
- 状态: 老牌聚合站进入 302 相对循环（net→org→me→io），最终页仅 "Redirecting..."，社区报告内容更新已死。
- 域名: mangapark.net | mangapark.org | mangapark.me | mangapark.io（302 循环）| mangapark.one（200，自称 manga hub，疑仿冒）
- 证据: [Reddit r/mangapiracy "Goodbye mangapark"](https://www.reddit.com/r/mangapiracy/comments/1q1jzs9/goodbye_mangapark)（US IP 下镜像可达但最近上传不可用）；实测循环 302

#### vatoto.com（原 Batoto 官方论坛）
- 状态: 403 Cloudflare Challenge，内容无法验证，疑似随主体关停（历史官方声明出处: 该论坛曾置顶 "Our domain is bato.to. Anything else is fake."）
- 域名: vatoto.com
- 证据: 实测 403（"Just a moment..."）；历史声明见搜索记录（vatoto.com 论坛帖）

---

### 备注（给汇总方）

- 域名数量、去重与通配建议: MangaDex 收 `*.mangadex.org`；hitomi 收 `gold-usergeneratedcontent.net` 通配；E-Hentai 收 `*.e-hentai.org` + `*.exhentai.org` + `*.hath.network` + `*.ehgt.org` 等；Webtoon 的 pstatic.net 只收具体子域防误伤。
- 成人站在大陆直连基本不可达，且多带 Cloudflare 盾，走代理是常态。
- 聚合站域名寿命普遍短（Batoto 案、mangabuddy→comizy、mangakakalot 家族换域均在一两年内发生），建议规则做成"整域通配 + 可快速增删的清单文件"。

## 5. 成人 / 本子阅读站（需代理）

> 本节为成人站专项复测记录；与 §4 的「成人/本子阅读站」小节重叠（同一批站点、来源各有侧重），规则清单以 §9 的自动汇总为准。

调研时间：2026-10-05。所有"来源"URL 为当日实际抓取，"快测"为当日 curl/DoH 实测结果（测试点在境外机房，403/000 不代表大陆不可用）。

**两个前置发现（影响来源选择）：**
1. FMHY 已无成人阅读分区：`github.com/fmhy/edit` 的 `docs/reading.md`（2026-10-05 实测，raw 抓取）中没有 hentai/doujin 站点条目，官网 fmhy.net/reading 亦不再收录；NSFW 内容已被导向第三方 rentry 页。故本清单改以 EHWiki、keiyoushi/extensions-source、gallery-dl 源码、站点现场 HTML/JS、DNS 实测为主要来源。
2. gallery-dl 主线已移除一批成人提取器：2026-10-05 实测 mikf/gallery-dl master 的 `gallery_dl/extractor/` 下**已无** exhentai.py / nhentai.py / hitomi.py / hentaifox.py / tsumino.py / pururin.py / fakku.py / hbrowse.py（旧 tag v1.28.5 同样没有）；现存的相关提取器为 imhentai.py（含 hentaifox/hentaiera 等镜像矩阵）、simplyhentai.py、hentai2read.py、hentaihere.py、luscious.py、myhentaigallery.py、tmohentai.py、thehentaiworld.py、hentaicosplays.py。nhentai/hitomi/e-hentai 的域名来源见下文各自条目。

---

#### E-Hentai / ExHentai（e-hentai.org）

- 类别: 成人/本子
- 域名: e-hentai.org | exhentai.org | forums.e-hentai.org | repo.e-hentai.org | xml.e-hentai.org | api.e-hentai.org | upload.e-hentai.org | s.exhentai.org | ehgt.org | ehtracker.org | ehwiki.org | hentaiathome.net | rpc.hentaiathome.net | hath.network | hentaiverse.org | alt.hentaiverse.org
- 性质: 全球最大同人志/本子图库与在线阅读站（ExHentai 为其里站）
- 来源: [EHWiki IPs（官方域名单）](https://ehwiki.org/wiki/IPs)；[FooIbar/EhViewer EhUrl.kt](https://github.com/FooIbar/EhViewer/blob/master/app/src/main/kotlin/com/hippo/ehviewer/client/EhUrl.kt)
- 后续更新入口: https://ehwiki.org/wiki/IPs（官方） ；https://github.com/FooIbar/EhViewer（客户端）
- 快测: e-hentai.org 200 | exhentai.org 302(→?poni=no，Sad Panda) | forums 403(防爬) | repo/xml/upload 200(→e-hentai.org) | api.e-hentai.org 404(裸根；API 为 `/api.php`) | s.exhentai.org 403(需 cookie) | ehgt.org 403 | ehtracker.org 200(→e-hentai.org/torrents.php) | ehwiki.org 200 | hentaiathome.net / rpc.hentaiathome.net / hath.network DNS 有 A 记录但 curl 连接失败(000) | hentaiverse.org / alt.hentaiverse.org 200
- 备注: exhentai 需登录 cookie（sadpanda）；hath.network 为 H@H 图床域名；hentaiverse.org 为游戏（非阅读）；api.e-hentai.org/api.php 与 s.exhentai.org/api.php 是两站 API。

#### NHentai（nhentai.net）

- 类别: 成人/本子
- 域名: nhentai.net | api.nhentai.net | i.nhentai.net | t.nhentai.net | i1.nhentai.net | i2.nhentai.net | i3.nhentai.net | i4.nhentai.net | t1.nhentai.net | t2.nhentai.net | t3.nhentai.net | t4.nhentai.net
- 性质: 最大英文同人志在线读站
- 来源: [nhentai 画廊页实测 HTML](https://nhentai.net/g/1/)（i1-i4/t1-t4 域）；[API 实测](https://nhentai.net/api/v2/galleries/1)（200 JSON）；[keiyoushi 扩展 build.gradle](https://github.com/keiyoushi/extensions-source/tree/main/src/all/nhentaito)
- 后续更新入口: https://github.com/keiyoushi/extensions-source/tree/main/src/all/nhentaito（+nhentaicom / nhentaixxx 分支）
- 快测: nhentai.net 200 | nhentai.net/api/v2/galleries/1 200 | nhentai.net/api/galleries/1 403 | api.nhentai.net / i.nhentai.net DNS 有 A 记录、curl 连接失败(000) | i1-i4/t1-t4 页面引用存在
- 备注: 图片 CDN 为 i1-i4、缩略图 t1-t4；API 走 `/api/v2/`；nhentai.com / nhentai.to / nhentai.xxx 是**第三方冒名镜像**（keiyoushi 标注 "unoriginal"），域名同样常被墙，规则可一并覆盖。

#### Hitomi.la

- 类别: 成人/本子
- 域名: hitomi.la | master.hitomi.la | gold-usergeneratedcontent.net | ltn.gold-usergeneratedcontent.net | a1.gold-usergeneratedcontent.net | a2.gold-usergeneratedcontent.net | w1.gold-usergeneratedcontent.net | w2.gold-usergeneratedcontent.net
- 性质: 同人志/漫画/Artist CG 大站，图床用独立域名
- 来源: [hitomi.la 首页](https://hitomi.la/)（资源全走 ltn.gold-usergeneratedcontent.net）；[hitomi common.js](https://ltn.gold-usergeneratedcontent.net/common.js)（`url_from_url` 把 `//*.hitomi.la/` 图片重写为 `//*.gold-usergeneratedcontent.net/`）；DoH 实测
- 后续更新入口: 无公开仓库；以 hitomi.la 首页 JS（ltn.gold-usergeneratedcontent.net/common.js）为准
- 快测: hitomi.la 200 | ltn.gold-usergeneratedcontent.net 200(根 404，gg.js/common.js 正常) | master.hitomi.la DNS 有记录 | a1./w1. 子域 DNS 有记录 | 旧图床 atn./ltn./tn.hitomi.la 已无 A 记录（NODATA）
- 备注: 规则**必须同时含 hitomi.la 和 gold-usergeneratedcontent.net**（图床易漏，a*=avif、w*=webp 变体）；旧 *.hitomi.la 图床已废弃。另：知名抓取工具 KurtBestor/Hitomi-Downloader 仓库已不可访问（2026-10-05 实测 HTTP 451，疑似 DMCA 下架），域名来源以 hitomi.la 现场 JS 为准。

#### IMHentai 网络（imhentai.xxx / hentaifox.com 等）

- 类别: 成人/本子
- 域名: imhentai.xxx | m11.imhentai.xxx | hentaifox.com | i3.hentaifox.com | hentaifox.tv | hentaiera.com | hentairox.com | hentaienvy.com | hentaizap.com
- 性质: 同一套代码的镜像站矩阵（含 hentaifox / hentaiera 等）
- 来源: [gallery-dl imhentai.py](https://github.com/mikf/gallery-dl/blob/master/gallery_dl/extractor/imhentai.py)（6 域名硬编码）；[keiyoushi hentaifox build.gradle](https://github.com/keiyoushi/extensions-source/blob/main/src/all/hentaifox/build.gradle.kts)；[imhentai 首页](https://imhentai.xxx/)
- 后续更新入口: gallery-dl imhentai.py（域名变更即此文件） | keiyoushi src/all/imhentai
- 快测: imhentai.xxx 200 | hentaifox.com 200 | hentaiera.com 200 | hentairox.com 200 | hentaienvy.com 200 | hentaizap.com 200 | m11.imhentai.xxx 404(根)/CDN 正常 | i3.hentaifox.com 404(根)/CDN 正常
- 备注: hentaifox.tv 为其视频站；imhentai.xxx 图片 CDN 为 m11 等 m 系子域（m11 实测存在），建议 DOMAIN-SUFFIX 整域覆盖。

#### Simply-Hentai / AsmHentai

- 类别: 成人/本子
- 域名: simply-hentai.com | api-v3.simply-hentai.com | images.sh-cdn.com | asmhentai.com | images.asmhentai.com | hentaiyes.com
- 性质: 英文同人志阅读站，两站同源
- 来源: [gallery-dl simplyhentai.py](https://github.com/mikf/gallery-dl/blob/master/gallery_dl/extractor/simplyhentai.py)（root + api-v3）；[keiyoushi asmhentai build.gradle](https://github.com/keiyoushi/extensions-source/blob/main/src/all/asmhentai/build.gradle.kts)；两站首页 HTML 互链
- 后续更新入口: gallery-dl simplyhentai.py / keiyoushi src/all/asmhentai
- 快测: simply-hentai.com 200(→/web3) | api-v3.simply-hentai.com DNS 有记录 | images.sh-cdn.com 404(根)/CDN 正常 | asmhentai.com 200 | images.asmhentai.com 403(根)/CDN 正常 | hentaiyes.com 200
- 备注: simply-hentai 图片 CDN = images.sh-cdn.com；asmhentai CDN = images.asmhentai.com；hentaiyes 为其关联站。

#### Hentai2Read / HentaiHere（共用 CDN）

- 类别: 成人/本子
- 域名: hentai2read.com | img1.hentaicdn.com | img2.hentaicdn.com | img3.hentaicdn.com | script.hentaicdn.com | hentaihere.com | hentai2w.com | hermes.hentai.direct
- 性质: 老牌英文同人志在线阅读（HentaiHere 为其衍生）
- 来源: [gallery-dl hentai2read.py](https://github.com/mikf/gallery-dl/blob/master/gallery_dl/extractor/hentai2read.py)；[gallery-dl hentaihere.py](https://github.com/mikf/gallery-dl/blob/master/gallery_dl/extractor/hentaihere.py)；两站首页 HTML
- 后续更新入口: gallery-dl 上述两提取器（域名硬编码）
- 快测: hentai2read.com 200 | hentaihere.com 200 | hentai2w.com 200 | img1-3/script.hentaicdn.com 引用存在 | hentaicdn.com 200 | hermes.hentai.direct 页面引用存在
- 备注: 图片 CDN 为 *.hentaicdn.com；两站互链，可视为同一运营。

#### Luscious

- 类别: 成人/本子
- 域名: luscious.net | www.luscious.net | members.luscious.net | ah-img.luscious.net | avatars-cdn.luscious.net | static.luscious.net
- 性质: 英文成人漫画/图集社区（含大量 doujin）
- 来源: [gallery-dl luscious.py](https://github.com/mikf/gallery-dl/blob/master/gallery_dl/extractor/luscious.py)（GraphQL on members.）；[keiyoushi luscious build.gradle](https://github.com/keiyoushi/extensions-source/blob/main/src/all/luscious/build.gradle.kts)；首页实测
- 后续更新入口: gallery-dl luscious.py / keiyoushi src/all/luscious
- 快测: luscious.net 200(→www) | www.luscious.net 200 | members.luscious.net 200(→登录) | ah-img./avatars-cdn./static. 子域均被首页引用
- 备注: 站点需登录/人机验证；CDN 子域多，建议 DOMAIN-SUFFIX,luscious.net 一把梭。

#### Multporn

- 类别: 成人/本子
- 域名: multporn.net
- 性质: 欧美成人漫画/同人合集站
- 来源: [keiyoushi multporn build.gradle](https://github.com/keiyoushi/extensions-source/blob/main/src/en/multporn/build.gradle.kts)（baseUrl 明示）；[官网](https://multporn.net/)
- 后续更新入口: keiyoushi src/en/multporn
- 快测: multporn.net 200
- 备注: 站点较单一，无独立图床域名（页面还有第三方广告引擎 engine.sadbaguette.com，属广告不宜并入阅读规则）。

#### MyHentaiGallery 系（MyHentaiComics / MyMangaGallery）

- 类别: 成人/本子
- 域名: myhentaigallery.com | myhentaicomics.com | cdn.myhentaicomics.com | mymangagallery.com
- 性质: 英文成人画廊/漫画阅读
- 来源: [keiyoushi myhentaigallery build.gradle](https://github.com/keiyoushi/extensions-source/blob/main/src/en/myhentaigallery/build.gradle.kts)；[gallery-dl myhentaigallery.py](https://github.com/mikf/gallery-dl/blob/master/gallery_dl/extractor/myhentaigallery.py)；首页 HTML
- 后续更新入口: keiyoushi src/en/myhentaigallery
- 快测: myhentaigallery.com 200 | myhentaicomics.com 200 | cdn.myhentaicomics.com 页面引用 | mymangagallery.com 页面引用
- 备注: 图片 CDN 为 cdn.myhentaicomics.com（易漏）。

#### TMO Hentai

- 类别: 成人/本子
- 域名: tmohentai.app（新） | tmohentai.com（旧，已无解析）
- 性质: 西语成人漫画阅读站，2024 后更换域名
- 来源: [keiyoushi tmohentaiunoriginal build.gradle](https://github.com/keiyoushi/extensions-source/blob/main/src/es/tmohentaiunoriginal/build.gradle.kts)（baseUrl=tmohentai.app）；[gallery-dl tmohentai.py](https://github.com/mikf/gallery-dl/blob/master/gallery_dl/extractor/tmohentai.py)（旧域名）
- 后续更新入口: keiyoushi src/es/tmohentaiunoriginal
- 快测: tmohentai.app 403(Cloudflare 挑战=存活) | tmohentai.com DNS NODATA、连接失败
- 备注: 规则用 tmohentai.app；旧域名可留观察。

#### Tsumino

- 类别: 成人/本子
- 域名: tsumino.com
- 性质: 英文同人志阅读站（老站）
- 来源: [官网实测](https://tsumino.com/)；gallery-dl 当前 master 已无 tsumino 提取器（2026-10-05 实测）
- 后续更新入口: 无（站点自维护）
- 快测: tsumino.com 200
- 备注: 站点存活但社区工具已停更，收录前建议人工抽查内容可用性。

#### TheHentaiWorld

- 类别: 成人/本子
- 域名: thehentaiworld.com
- 性质: 英文成人漫画阅读站
- 来源: [gallery-dl thehentaiworld.py](https://github.com/mikf/gallery-dl/blob/master/gallery_dl/extractor/thehentaiworld.py)
- 后续更新入口: gallery-dl thehentaiworld.py
- 快测: thehentaiworld.com 200
- 备注: 单一域名。

#### Hentai-Cosplay 系（hentai-cosplay-xxx.com）

- 类别: 成人/本子
- 域名: hentai-cosplay-xxx.com | hentai-img-xxx.com | hentai-img.com（新） | porn-image.com
- 性质: Cosplay/图片写成漫画风格的长图阅读站
- 来源: [gallery-dl hentaicosplays.py](https://github.com/mikf/gallery-dl/blob/master/gallery_dl/extractor/hentaicosplays.py)（三域名硬编码）
- 后续更新入口: gallery-dl hentaicosplays.py
- 快测: hentai-cosplay-xxx.com 403(反爬) | hentai-img-xxx.com 200(→hentai-img.com) | porn-image.com 200
- 备注: 注意 hentai-img-xxx.com 已改跳 hentai-img.com（新域名必须收录）；现有规则只有 hentai-cosplay-xxx.com，建议扩充。

#### Fakku（fakku.net，现有规则域名复核）

- 类别: 成人/本子
- 域名: fakku.net | hentalk.pw | fakku.cc | fakkuonion.airdns.org
- 性质: 官方授权的成人漫画发行商（正版站点，机房里站常被 451 地区封锁）
- 来源: [keiyoushi spyfakku build.gradle（镜像列表）](https://github.com/keiyoushi/extensions-source/blob/main/src/en/spyfakku/build.gradle.kts)；fakku.net 实测
- 后续更新入口: keiyoushi src/en/spyfakku（镜像域会在 build.gradle 更新）
- 快测: fakku.net 451(地区法律封锁=存活) | hentalk.pw 200 | fakku.cc 000(连接失败) | fakkuonion.airdns.org 洋葱地址未测
- 备注: SpyFakku 扩展（第三方镜像 hentalk.pw / fakku.cc）为"Fakku 内容"站点，与官网不同源；fakku.net 本身免费内容少。

#### Irodori Comics（irodoricomics.com）

- 类别: 成人/本子
- 域名: irodoricomics.com | sakura-r18.irodoricomics.com | blog.irodoricomics.com | newsletter.irodoricomics.com
- 性质: 官方授权同人英译发行商（正规商店/阅读）
- 来源: [官网](https://irodoricomics.com/)首页实测
- 后续更新入口: 官网（无公开仓库）
- 快测: irodoricomics.com 200；R18 分店子域 sakura-r18.irodoricomics.com 首页引用
- 备注: R18 内容在 sakura-r18 子域，DOMAIN-SUFFIX 覆盖即可。

#### 3hentai.net（现有规则域名复核）

- 类别: 成人/本子
- 域名: 3hentai.net
- 性质: 3D/同人漫画聚合阅读站
- 来源: DoH DNS 实测 + curl；无公开抓取器可佐证
- 后续更新入口: 无
- 快测: DNS 解析正常(15.235.218.75，OVH CA) | curl/WebFetch 均 TLS 复位/超时（000，疑似反爬或封机房 IP）
- 备注: 域名仍存活但无法从机房环境验证内容，建议保留在规则中，用真实浏览器复核一次。

#### Pururin（pururin.io，现有规则域名，实测已死）

- 类别: 成人/本子
- 域名: pururin.io（旧） | pururin.us（停放） | pururin.com（无服务）
- 性质: 老牌英文同人志阅读站 —— 站点已停运
- 来源: Cloudflare + Google DoH 双解析实测（2026-10-05）；站点页面实测
- 后续更新入口: 无
- 快测: pururin.io DNS SERVFAIL（双解析均失败） | pururin.us 200 但内容为 router.parklogic.com 停放页 | pururin.com DNS 无 A 记录
- 备注: **建议从现有规则删除**（已死）。

#### Hentai Cafe（hentai.cafe，现有规则域名，实测已死）

- 类别: 成人/本子
- 域名: hentai.cafe
- 性质: 老牌聚合站 —— 域名已停放（ParkLogic）
- 来源: 站点页面实测（200 但为 JS 跳转 + router.parklogic.com）
- 后续更新入口: 无
- 快测: hentai.cafe 200（停放页）
- 备注: **建议从现有规则删除**。

#### Hentai-En（hentai-en.com，实测已死）

- 类别: 成人/本子
- 域名: 无（原 hentai-en.com）
- 性质: 老牌英文成人漫画站，域名彻底消失
- 来源: DoH 实测（Cloudflare + Google 双解析均为 NXDOMAIN/Status 3）；同族 hentai-en.net / hentai-en.xyz 同为 NXDOMAIN
- 后续更新入口: 无
- 快测: NXDOMAIN（未收录）
- 备注: 不必加入规则；如需兜底可保留 keyword 策略，无实际意义。

#### HBrowse（hbrowse.com，实测已死）

- 类别: 成人/本子
- 域名: hbrowse.com
- 性质: 老牌 doujin 阅读站 —— 域名已停放
- 来源: 站点实测（重定向到 /lander，`LANDER_SYSTEM=CP`、`parking` 标记）
- 后续更新入口: 无
- 快测: hbrowse.com 200（停放 lander）
- 备注: 未在本仓库现有规则中；不建议收录。

#### CosplayTale（cosplaytale.com，现有规则域名，实测已死）

- 类别: 成人/本子
- 域名: cosplaytale.com
- 性质: Cosplay 图站 —— 域名进入 JS 挑战停放循环
- 来源: 站点实测（477 字节 JS 无限跳转，无实际内容）
- 后续更新入口: 无
- 快测: cosplaytale.com 200（停放/挑战页）
- 备注: **建议从现有规则删除或观察**。

#### HentaiVerse（hentaiverse.org）—— 非阅读

- 类别: 成人/本子（游戏，非阅读）
- 域名: hentaiverse.org | alt.hentaiverse.org
- 性质: E-Hentai 官方网页游戏（含成人内容），非阅读站
- 来源: [EHWiki IPs](https://ehwiki.org/wiki/IPs)；实测
- 后续更新入口: https://ehwiki.org/wiki/IPs
- 快测: hentaiverse.org 200 | alt.hentaiverse.org 200
- 备注: 与 e-hentai 同公司，规则可并入 EA 组。

#### Pixiv 系成人向（复核）

- 类别: 成人（含 R18 二创）
- 域名: pixiv.net | pximg.net | fanbox.cc | booth.pm（成人向内容入口）
- 性质: 日本最大插画社区，R18 需登录开关
- 来源: [v2fly data/pixiv](https://raw.githubusercontent.com/v2fly/domain-list-community/master/data/pixiv)；pixiv.net 实测 200
- 后续更新入口: v2fly data/pixiv
- 快测: pixiv.net 200
- 备注: 已有专门渠道覆盖，此处仅确认域名无变动。

---

### 现有规则域名复核结论（本仓库 JapanManga.list / 18comic.list）

| 域名 | 结论 | 动作 |
| --- | --- | --- |
| pixiv.net / comic.pixiv.net | 200，v2fly/blackmatrix7 均覆盖 | 保留 |
| hitomi.la | 200；图床已迁 gold-usergeneratedcontent.net | 保留并补 gold-usergeneratedcontent.net |
| hentai.cafe | 已停放（parklogic） | 删除 |
| fakku.net | 451 地区封锁，站点存活 | 保留（如需镜像可补 hentalk.pw） |
| pururin.io | DNS SERVFAIL，站点停运 | 删除 |
| nhentai.net | 200 | 保留，补 i1-i4/t1-t4.nhentai.net（DOMAIN-SUFFIX 已覆盖） |
| hentai-cosplay-xxx.com | 403 反爬，存活；兄弟域名 hentai-img-xxx.com→hentai-img.com | 保留并补 hentai-img.com / hentai-img-xxx.com / porn-image.com |
| cosplaytale.com | 停车/挑战页，疑似已死 | 删除或观察 |
| 3hentai.net | DNS 存活、机房不可达 | 保留待浏览器复核 |
| 18-comic（keyword） | v2fly 18comic 文件 50 域 + 规则库多来源覆盖 | 保留，可换成 v2fly 域名表 |

## 6. 现成规则上游与更新入口（建议长期跟进）

调研时间：2026-10-05（所有 URL 实测、pushed_at 来自 api.github.com 当日数据）。
用途：作为本仓库规则的上游更新源 + 域名增量。

---

### v2fly/domain-list-community

- URL: 仓库 https://github.com/v2fly/domain-list-community/tree/master/data ；单文件 raw 格式
  `https://raw.githubusercontent.com/v2fly/domain-list-community/master/data/<文件名>`
- 覆盖: 1542 个 data 文件；与漫画/成人相关的 25 个：
  `18comic` `anime` `bilibili` `bilibili-cdn` `bilibili-game` `bilibili2` `copymanga`
  `dlsite` `dmm` `dmm-porn` `ehentai` `hentaichen` `hentaivn` `truyen-hentai`
  `pixiv` `manhuagui` `manhuaren` `haitang` `boylove` `erolabs` `johren` `konachan`
  `naver` `kakao` `category-porn`（无 manga/comic/webtoon/hentai 字样的其它文件）
- 格式: domain-list（v2ray geosite 源格式，支持 `include:` / `full:` / `@ads` 属性；mihomo/Clash 侧一般经 MetaCubeX 转 mrs 使用）
- 活跃度: pushed 2026-10-04T05:31:31Z，9627 stars（maintainer 日常合并 PR，最活跃的上游）
- 摘录的域名（关键文件）:
  - `data/ehentai`（8 域）: e-hentai.org | exhentai.org | ehgt.org | ehtracker.org | ehwiki.org | hath.network | hentaiathome.net | hentaiverse.org
  - `data/18comic`（50 域）: 18comic.org | 18comic.vip | jmcomic.me | jmcomic.moe | jmcomic.rocks | jmcomic.mobi | jm365.work | jmapinode.xyz | jmapinode.biz | jmapinodeudzn.net | jmapiproxy1-4.cc | jmapibranch1-3.cc | cdnblackmyth.club | cdnmhws.cc | cdnuc.vip | cdnxxx-proxy.co | jm18c-bbm.cc | jmcomic-fb.vip | asjmapihost.cc 等（JM 漫画全家，含 API/CDN 节点）
  - `data/copymanga`（7 域）: mangacopy.com | copy-manga.com | 2025copy.com | copy20.com | copy2000.online | mangafuna.xyz | mangafunb.fun（拷贝漫画，含备用域名）
  - `data/hentaichen`（6 域）: hentai-chan.com | hentai-chan.live | hentaichan.live | hentaichan.me | h-chan.me | imgschan.xyz
  - `data/hentaivn`（4 域）: hentaivn.net | hentaivn.de | hentaivn.la | htvncdn.net
  - `data/truyen-hentai`（3 域）: truyen-hentai.com | truyen-hentai.fr | truyen-hentai.ru
  - `data/haitang`（17 域）: haitangbook.com | longmabook.com | longmabookcn.com | htlvbooks.com | htnewbooks.com | htwhbook.com | lmbooks.com | lmeebooks.com | lovehtbooks.com | lvhtebook.com | mybookinlm.com | myhtebook.com | myhtebooks.com | myhtlmebook.com | newhtbook.com | urhtbooks.com | haitbook.com（海棠文化线上文学城）
  - `data/manhuagui`（2 域）: manhuagui.com | mhgui.com
  - `data/manhuaren`（10 域）: manhuaren.com | dm5.com | dm5.cn | dm9.com | 1kkk.com | gmanhua.com | hkmanga.com | manben.com | manbenapi.com | cdndm5.com（漫画人/动漫屋）
  - `data/boylove`（5 域）: boylove.cc | boylove.live | boylove1.cc | boyloves.cc | fuhouse.club
  - `data/erolabs`（12 域）: ero-labs.com/net/io/one/online/site/fun/cloud | erolabs.com/net/online/cloud | erolabsshare.xyz（成人游戏平台，非阅读）
  - `data/johren`（2 域）: johren.net | johren.games（成人漫画/游戏商店）
  - `data/konachan`（2 域）: konachan.com | konachan.net（ACG 图站）
  - `data/pixiv`（11 域）: pixiv.net | pximg.net | pixiv.me | pixiv.org | pixiv.co.jp | pixiv.help | pixivision.net | pixiv-recommend.net | fanbox.cc | booth.pm | ads-pixiv.net(@ads)
  - `data/dlsite`（10 域）: dlsite.com | dlsite.jp | dlsite.com.tw | dlaf.jp | ci-en.jp | ci-en.net | chobit.cc | nijiyome.jp | triokini.com | dlsitestudio.com
  - `data/dmm` + `data/dmm-porn`（共 23 域）: dmm.com | dmm.co.jp | dmmapis.com | dmmrex.com | dmm-extension.com | api-p.videomarket.jp | ad.games.dmm.com(@ads) 等（游戏为主，dmm-porn 为成人商店）
  - `data/anime`（32 域）: 9anime.cz/.id/.to/.ws | gogoanime.vc/.wiki/.gogoanime3.co | gogocdn.net | gogo-load.com | agefans.com | age.tv | agedm.org | animedao-tv.com | crunchyroll.com | funimation.com | hidive.com 等
  - `data/bilibili`（40 行，含 bilicomic.com | bilicomics.com 哔哩哔哩漫画 | maoer.com 猫耳 | acg.tv | b23.tv 等）；`data/bilibili-cdn`（hdslb.com | bilivideo.com/.cn/.net | bilicdn1-5.com | mincdn.com 等）；`data/bilibili2`（注释明确写着这是成人站：bili2.cc | bili888.com | bili999.com | regexp:bilibili30[1-9].xyz）
  - `data/naver`（49 域）: naver.com 全家 + **webtoons.com | webtoonscorp.com | studioncorp.com | studiolico.com | wattpad.com**（Webtoon 官方，含 Canvas）
  - `data/kakao`（83 域）: kakao.com/.co.kr | daum.net | kakaocdn.net | 及 Kakao Entertainment 子公司（melon.com | 1thek.com 等；无 Kakao Webtoon/Page 专域）
  - `data/category-porn`（聚合）: 73 条 include + 6110 条裸域名 + 约 80 条 regexp；include 中与阅读相关：`18comic` `ehentai` `hentaichen` `hentaivn` `truyen-hentai` `haitang` `picacg` `boylove` `dlsite` `dmm-porn` `johren` `erolabs` `konachan` `kemono` `coomer` `pawchive` `tokyo-toshokan` `newgrounds` 等（另含 javbus/javdb/jable/missav 等视频类）
- 评价: 最正统、最全的上游；漫画/成人向细分文件齐全，本仓库的"域名增量"应优先从这里取。

### blackmatrix7/ios_rule_script

- URL: `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/<名称>/<名称>.list`
  国内可用 jsDelivr 镜像：`https://cdn.jsdelivr.net/gh/blackmatrix7/ios_rule_script@master/rule/Clash/<名称>/<名称>.list`
  （同结构另有 QuantumultX / Surge / Loon / Shadowrocket / Rule 等版本）
- 覆盖: rule/Clash 下 669 个子目录，与漫画/动漫/成人相关的目录：
  `EHGallery` `Picacg` `VikACG` `U17` `Pixiv` `DMM` `Naver` `NaverTV` `KakaoTalk` `BiliBili` `BiliBiliIntl` `Anime` `Niconico`
  **没有** MangaDex / Webtoon / Manga / Comic / Hentai 目录。
- 格式: payload（Clash rule-provider list，可直接 RULE-SET 引用）
- 活跃度: 仓库 pushed 2026-10-03T20:34:49Z，28125 stars；但各 list 文件头 UPDATED 偏旧：
  - EHGallery `2025-06-06`（6 DOMAIN-SUFFIX：e-hentai.org | ehgt.org | ehwiki.org | exhentai.org | hath.network | hentaiverse.org；+ IP-CIDR,178.175.128.0/21）
  - Pixiv `2025-06-06`（pixiv.net | pximg.net | fanbox.cc | booth.pm | pixiv.cat | pixiv.co.jp | pixiv.me | pixiv.org）
  - DMM `2025-06-06`（18 域 + 2 IP-CIDR）；Naver/NaverTV/KakaoTalk `2025-06-06`；Niconico `2025-06-06`（含 nicomanga.jp）
  - Picacg 哔咔 `2024-01-08`（bikac.xyz | bikaios.xyz | manhuabika.com | picacgp.com | picacomic.com | picacomic.xyz | picacn.xyz | wikawika.xyz | bikaa.xyz | picacgy.com）
  - VikACG `2025-06-06`（vikacg.com | picjs.xyz）；U17 `2025-06-06`（u17.com | u17i.com | u17t.com）
  - Anime `2024-01-08`（13 域：9anime、crunchyroll 等）
- 摘录的域名: 见上（Picacg/EHGallery 是仅有的两个成人向目录）
- 评价: 国内最流行的规则来源，但成人/漫画覆盖很少（无 MangaDex/Webtoon/NHentai/Hitomi），只能作补充。

### MetaCubeX/meta-rules-dat

- URL:
  - mihomo（mrs）: `https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/<分类>.mrs`
  - sing-box（srs）: `https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/sing/geo/geosite/<分类>.srs`
  - 整包 geosite.db / geosite.dat / geosite-lite.db: `https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/geosite.db`（jsDelivr: `https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geosite.db`）
- 覆盖: 实测存在（HTTP 200）的分类：`ehentai` `pixiv` `bilibili` `dmm` `dmm-porn` `18comic` `copymanga` `hentaivn` `hentaichen` `naver` `kakao` `anime`
  实测不存在（404）：`mangadex` `webtoon` `hitomi` `nhentai` `adult`
  geosite-lite.db 内置常用集含 ehentai / pixiv / bilibili。
- 格式: mrs（mihomo rule-provider format: mrs）；srs（sing-box）
- 活跃度: pushed 2026-10-05T01:09:13Z（每日自动构建），5279 stars
- 摘录的域名: 分类内容 = v2fly data 对应文件（ehentai/18comic/copymanga 等，域名同上表），无额外域名
- 评价: mrs 可直接挂 rule-provider，省流量；但分类是 v2fly 子集，无 MangaDex/Webtoon/Hitomi/NHentai，需要本仓库自建补齐。

### tanmoumou252/NSFWruleset

- URL: `https://raw.githubusercontent.com/tanmoumou252/NSFWruleset/main/NSFW.list`（另有 `NSFW.yaml` / `NSFW_gfwlist.txt` / `geosite-nsfw-singbox.json`）
- 覆盖: 218 行；DOMAIN-KEYWORD（hentai | jav | porn | xvideo | fc2 | mikanani | rarbg | supjav 等）+ 大量成人域，
  阅读/动漫相关摘录：18comic.vip | hitomi.la | hacg.me | cangku.moe | comici.win | acgn.zone | acgnx.se | jmcomic-creed.club | wnacg.com | haho.moe | reimu.net | blog.reimu.net | 2dfan.com | south-plus.net | white-plus.net | snow-plus.net | acgrip.com | imoutolove.me | smallcolor.link | moeli-desu.com | hanime1.me | hanime.tv | ohentai.org | hentaidude.com | rule34.xxx | kemono.su | hentaiera.com | imhentai.xxx | missav.com | supjav.com | nyaa.si | share.dmhy.org | sexinsex.net 等
- 格式: payload（list/yaml）+ gfwlist + sing-box json
- 活跃度: pushed 2026-07-04T08:29:04Z（18 stars；文件头 UPDATED 2025-10-10）
- 评价: 国内用户维护的 NSFW 全向分流，域名量不大但命中率高（含大量本站没有的国内二次元成人站），适合做增量来源。

### SoLfin31/NSFW-Blocking-Rulesets-for-Surge-Singbox

- URL: `https://raw.githubusercontent.com/SoLfin31/NSFW-Blocking-Rulesets-for-Surge-Singbox/main/singbox-nsfw.json`；`.../surge-nsfw.txt`
- 覆盖: 从 Bon-Appetit/porn-domains + scrapeUrls.txt（NSFW 导航站抓取）合成，每日 Actions 更新
- 格式: sing-box json + Surge
- 活跃度: pushed 2026-10-05T04:01:13Z（0 stars，日更）
- 评价: 本意是"屏蔽"，但域名数据可直接复用于分流；作为每日增量抓取源可用。

### Bon-Appetit/porn-domains / blocklistproject/Lists（大而全的成人域名库）

- URL: https://github.com/Bon-Appetit/porn-domains ；https://raw.githubusercontent.com/blocklistproject/Lists/master/porn.txt
- 覆盖: 百万级成人域名自动收集（不细分漫画/本子）
- 格式: payload / hosts
- 活跃度: Bon-Appetit pushed 2026-10-05T07:25:11Z（513 stars）；blocklistproject pushed 2026-10-05T08:54:34Z（5126 stars）
- 评价: 量最大但不适合直接进 Clash 规则（体积过大），可用作域名"命中/校验"参考库。

### powerfullz/override-rules（E-Hentai 专用分流）

- URL: `https://raw.githubusercontent.com/powerfullz/override-rules/main/ruleset/EHentai.list`
- 覆盖: e-hentai.org | ehgt.org | ehwiki.org | exhentai.org | hath.network | hentaiverse.org + IP-CIDR,178.175.128.0/21（与 blackmatrix7 EHGallery 一致）
- 格式: payload（Mihomo/Substore 覆写脚本内嵌 rule-provider）
- 活跃度: pushed 2026-09-16T15:34:46Z（596 stars）
- 评价: "针对 E-Hentai 单独分组"的参考实现，可直接抄其分流组写法。

### ACL4SSR/ACL4SSR

- URL: `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Dmm.list`（另有 `Pixiv.list` `KakaoTalk.list` `Bilibili.list` `BiliBiliHMT.list`）
- 覆盖: 仅 Dmm / Pixiv / Bilibili / KakaoTalk 等，无漫画/成人分类
- 格式: payload
- 活跃度: pushed 2026-10-03T03:17:57Z（6760 stars）
- 评价: 老牌分流项目，但相关覆盖不如 v2fly，价值有限。

### GitHub 搜索记录（2026-10-05 实测）

| 查询 | 结果 |
| --- | --- |
| manga domain list | 0 结果 |
| webtoon domains | 仅无关项目 |
| 漫画 域名 | mihon-ehentai-extension（Tachiyomi/Mihon 的 E-Hentai 源，含域名切换）、jm_comic 下载器等，非清单 |
| clash manga / manga geosite / clash hentai rules | 0 结果或无关小仓库 |
| nhentai domain | xzlrong233x/RoamDoujinshiDomain（桌面/安卓客户端） |
| ehentai domain / hitomi rules / jmcomic rules / mangadex clash | 0 结果 |
| nsfw ruleset | tanmoumou252/NSFWruleset（18★）、SoLfin31/NSFW-Blocking-Rulesets（日更） |

结论：GitHub 上不存在"专注漫画/成人站域名清单且长期维护"的独立仓库；可用域名主要内含在
① v2fly/domain-list-community（最全上游）② blackmatrix7 / MetaCubeX（分发形态）
③ 阅读器扩展源码（github.com/keiyoushi/extensions-source、mihon-ehentai-extension）
④ 社区 NSFW 分流（tanmoumou252、SoLfin31）。
**长期跟进的更新上游 = v2fly data/ 目录 + MetaCubeX 自动构建 + keiyoushi 扩展源码。**

## 7. 统一实测记录（2026-10-05）

- 实测对象：本文收录的 **729 个唯一域名**，逐个做三项测试：
  1. **DoH 解析**：AliDNS（`223.5.5.5`）与 Cloudflare（`cloudflare-dns.com`）双解析器各查一次 A 记录
  2. **HTTPS 连通**：`curl`（Chrome UA，超时 12s）测 HTTP 状态码，失败再退 http:// 重试
  3. **标题抓取**：对返回 2xx/3xx/403 的域名抓 `<title>`，确认真的是目标站点
- 环境：本机（Windows + 路由器 OpenClash）出网；结果为 2026-10-05 快照，换网络/换出口可能不同
- 判读注意：① 部分 CDN 基域（如 `gold-usergeneratedcontent.net`、`pstatic.net` 系）**apex 无 A 记录但子域在用**，`NO_A` 不代表不可用；② `403/404/400/426` 多为反爬、需 cookie 或 API 根路径特性，**站点是活的**；③ 两个解析器结果不一致时（如 `OK/NX`）以站点实测为准
- 结果分布：**可访问 536** ｜ 受限/反爬（403/404/5xx 等，站点存活）**146** ｜ 超时/连接失败（DNS 有解析）**24** ｜ 无解析（NXDOMAIN/SERVFAIL）**23**
- 所有异常项都做过**二次复测**（AliDNS + Cloudflare + Google 三方 DoH、HTTPS 两次重试），下表与正文中的结论以复测为准（`←` 标记处）。

> 下表为完整明细。`DNS` 列 = AliDNS/Cloudflare 的解析结果（OK=有 A 记录、NX=NXDOMAIN、ERR=查询失败）；`HTTP` 列 = HTTPS 状态码（`h` 前缀 = https 失败后 http 成功；`000` = 连接失败）。

```
### 国内（116）
[OK]   321mh.com                                 OK/OK       h200
[OK]   ac.qq.com                                 OK/OK       200   腾讯动漫官网_漫画在线阅读_免费下拉式看漫画平台
[受限] activity.321mh.com                        OK/OK       403   403 Forbidden
[OK]   api.copymanga.site                        OK/OK       200   Redirecting...
[受限] api.kuaikanmanhua.com                     OK/OK       404
[受限] api.mangacopy.com                         OK/OK       404
[OK]   api.manhuadb.com                          OK/OK       h200
[超时] app.buka.cn                               OK/OK       000
[OK]   baozicomic.cc                             OK/OK       200   包子漫画 - 海量正版漫画免费阅读
[OK]   baozimh.com                               OK/OK       302   502 Bad Gateway
[超时] buka.cn                                   OK/OK       000
[OK]   bzmgcn.com                                OK/OK       301   502 Bad Gateway
[受限] cdn-static.dongmanmanhua.cn               OK/OK       403
[受限] cdn.dongmanmanhua.cn                      OK/OK       403
[OK]   cf.mhgui.com                              OK/OK       200   Welcome to nginx!
[OK]   cms.samanlehua.com                        OK/OK       200
[OK]   cn.bzmgcn.com                             OK/OK       302   502 Bad Gateway
[OK]   copy4000.com                              OK/OK       200   拷貝漫畫 - 海賊王 海贼王 哥布林殺手 哥布林杀手 漫畫 漫画 FGO FGO 東方 东方 艦娘 舰娘 同人志 本子 更新 全集 在綫漫畫 在线漫画 - 拷貝漫畫 拷贝漫画
[OK]   copymanga.app                             OK/OK       302   welcome
[OK]   copymanga.co                              OK/OK       200
[超时] copymanga.com                             OK/S2       000
[OK]   copymanga.info                            OK/OK       302   copymanga.info
[无解析]copymanga.me                              NX/NX       000
[OK]   copymanga.org                             OK/OK       h200
[OK]   copymanga.site                            OK/OK       200   Redirecting...
[超时] copymanga.tv                              S2/S2       000
[OK]   dmzj.com                                  OK/OK       h302
[OK]   dongmanmanhua.cn                          OK/OK       200   咚漫漫画官网|咚咚手指 看看漫画
[OK]   f2.kkmh.com                               OK/OK       200
[OK]   fanqienovel.com                           OK/OK       200   小说,番茄小说网_好看的小说尽在番茄小说官网
[受限] gtimgcdn.ac.qq.com                        OK/OK       403   403 Forbidden
[无解析]gufengmh.com                              NX/NX       000
[OK]   h5.kuaikanmanhua.com                      OK/OK       302   快看漫画_官方漫画_漫画大全免费在线观看
[超时] happymh.com                               NO_A/NO_A   000
[OK]   hhcomic.com                               OK/OK       200   Redirecting...
[超时] houyi.kkmh.com                            OK/OK       000
[OK]   i.hamreus.com                             OK/OK       200   Welcome to nginx!
[OK]   i0.hdslb.com                              OK/OK       200
[受限] ibuka.cn                                  OK/OK       h403
[OK]   idmzj.com                                 OK/OK       h302
[OK]   image.yqmh.com                            OK/OK       200
[OK]   images.manhuadb.com                       OK/OK       h200
[OK]   img.manhuadb.com                          OK/OK       h200
[OK]   kanman.com                                OK/OK       301   穿越西元3000后漫画 斗罗大陆漫画 斗破苍穹漫画 漫画大全 看漫网 看漫画
[OK]   kkmh.com                                  OK/OK       301   APP下载_快看
[OK]   kuaikanmanhua.com                         OK/OK       301   快看漫画_官方漫画_漫画大全免费在线观看
[OK]   m.ac.qq.com                               OK/OK       302   腾讯动漫官网_漫画在线阅读_免费下拉式看漫画平台
[OK]   m.kanman.com                              OK/OK       200   穿越西元3000后漫画 斗罗大陆漫画 斗破苍穹漫画 漫画大全 看漫网 看漫画
[OK]   m.manhuatai.com                           OK/OK       h301
[OK]   manga.bilibili.com                        OK/OK       200   哔哩哔哩漫画 - bilibili 正版漫画平台
[受限] manga.hdslb.com                           OK/OK       403   403 Forbidden
[OK]   manga2026.xyz                             OK/OK       200   熱辣漫畫 热辣漫画 - 海賊王 海贼王 哥布林殺手 哥布林杀手 漫畫 漫画 FGO FGO 東方 东方 艦娘 舰娘 同人志 本子 更新 全集 在綫漫畫 在线漫画 - 熱辣漫畫 热辣
[OK]   mangacopy.com                             OK/OK       200   拷貝漫畫 - 海賊王 海贼王 哥布林殺手 哥布林杀手 漫畫 漫画 FGO FGO 東方 东方 艦娘 舰娘 同人志 本子 更新 全集 在綫漫畫 在线漫画 - 拷貝漫畫 拷贝漫画
[OK]   mangafunb.fun                             NO_A/NO_A   000     ← 拷贝漫画图片基域：apex 无 A 记录属正常，子域（s3./sa–sz.）在用，按后缀收录
[OK]   manhua.163.com                            OK/OK       302   LOFTER（乐乎） - 让兴趣，更有趣
[受限] manhua.acimg.cn                           OK/OK       403
[受限] manhuabei.com                             OK/OK       h302    ← 疑似空壳（站名未从官方渠道确认），不入规则
[OK]   manhuadb.com                              OK/OK       h200
[受限] manhuadui.com                             OK/OK       200   Loading...  ← 页面接近空壳（疑似 SEO 站群），归属未确认，不入规则
[OK]   manhuagui.com                             OK/OK       301   在线看漫画_飒漫乐画_妃夕妍雪 - 看漫画
[OK]   manhuatai.com                             OK/OK       h200
[受限] mhgui.com                                 OK/OK       403   403 Forbidden
[OK]   mhxk.com                                  OK/OK       h200
[OK]   qimao.com                                 OK/OK       301   七猫中文网-全本免费小说-免费小说排行榜
[OK]   resource.mhxk.com                         OK/OK       200
[OK]   s1.hdslb.com                              OK/OK       200
[受限] s3.mangafunb.fun                          OK/OK       404
[受限] sa.mangafunb.fun                          OK/OK       404
[OK]   samanlehua.com                            OK/OK       h200
[受限] sb.mangafunb.fun                          OK/OK       404
[受限] sc.mangafunb.fun                          OK/OK       404
[受限] sd.mangafunb.fun                          OK/OK       404
[受限] se.mangafunb.fun                          OK/OK       404
[受限] sf.mangafunb.fun                          OK/OK       404
[受限] sg.mangafunb.fun                          OK/OK       404
[受限] sh.mangafunb.fun                          OK/OK       404
[受限] short.tiankongshuyu.cn                    OK/OK       404
[受限] sj.mangafunb.fun                          OK/OK       404
[受限] sl.mangafunb.fun                          OK/OK       404
[受限] sm.mangafunb.fun                          OK/OK       404
[受限] sn.mangafunb.fun                          OK/OK       404
[受限] sp.mangafunb.fun                          OK/OK       404
[受限] sq.mangafunb.fun                          OK/OK       404
[受限] ss.mangafunb.fun                          OK/OK       404
[受限] st.mangafunb.fun                          OK/OK       404
[受限] static.321mh.com                          OK/OK       403   403 Forbidden
[OK]   static3w.kuaikanmanhua.com                OK/OK       200   快看漫画
[受限] sw.mangafunb.fun                          OK/OK       404
[受限] sx.mangafunb.fun                          OK/OK       404
[受限] sy.mangafunb.fun                          OK/OK       404
[受限] sz.mangafunb.fun                          OK/OK       404
[超时] u17.com                                   NO_A/NO_A   000
[OK]   wtzw.com                                  OK/OK       h301
[超时] www.buka.cn                               OK/OK       000
[OK]   www.copy4000.com                          OK/OK       200   拷貝漫畫 - 海賊王 海贼王 哥布林殺手 哥布林杀手 漫畫 漫画 FGO FGO 東方 东方 艦娘 舰娘 同人志 本子 更新 全集 在綫漫畫 在线漫画 - 拷貝漫畫 拷贝漫画
[OK]   www.copymanga.site                        OK/OK       200   Redirecting...
[无解析]www.dmzj.com                              NX/NX       000
[OK]   www.dongmanmanhua.cn                      OK/OK       200   咚漫漫画官网|咚咚手指 看看漫画
[无解析]www.gufengmh.com                          NX/NX       000
[超时] www.happymh.com                           NO_A/NO_A   000
[OK]   www.hhcomic.com                           OK/OK       200   Redirecting...
[受限] www.ibuka.cn                              OK/OK       h403
[OK]   www.kanman.com                            OK/OK       200   穿越西元3000后漫画 斗罗大陆漫画 斗破苍穹漫画 漫画大全 看漫网 看漫画
[OK]   www.kuaikanmanhua.com                     OK/OK       200   快看漫画_官方漫画_漫画大全免费在线观看
[OK]   www.manga2026.xyz                         OK/OK       200   熱辣漫畫 热辣漫画 - 海賊王 海贼王 哥布林殺手 哥布林杀手 漫畫 漫画 FGO FGO 東方 东方 艦娘 舰娘 同人志 本子 更新 全集 在綫漫畫 在线漫画 - 熱辣漫畫 热辣
[OK]   www.mangacopy.com                         OK/OK       200   拷貝漫畫 - 海賊王 海贼王 哥布林殺手 哥布林杀手 漫畫 漫画 FGO FGO 東方 东方 艦娘 舰娘 同人志 本子 更新 全集 在綫漫畫 在线漫画 - 拷貝漫畫 拷贝漫画
[受限] www.manhuabei.com                         OK/OK       200   Loading...  ← 同上（空壳站群），不入规则
[OK]   www.manhuadb.com                          OK/OK       h200
[受限] www.manhuadui.com                         OK/OK       200   Loading...  ← 同上（空壳站群），不入规则
[OK]   www.manhuagui.com                         OK/OK       200   在线看漫画_飒漫乐画_妃夕妍雪 - 看漫画
[OK]   www.manhuatai.com                         OK/OK       h200
[OK]   www.u17.com                               OK/OK       h301
[受限] www.xindm.cn                              OK/OK       h200    ← 同上（空壳站群），不入规则
[OK]   xiaoshuo.wtzw.com                         OK/OK       200   免费看书100年，七猫免费小说
[受限] xindm.cn                                  OK/OK       h200    ← 无有效页面/标题（疑似 SEO 站群），归属未确认，不入规则
[OK]   yqmh.com                                  OK/OK       h200

### 中文/代理（88）
[OK]   18comic-god.cc                            OK/OK       301
[OK]   18comic-god.club                          OK/OK       302   Loading...
[OK]   18comic-god.xyz                           OK/OK       301
[OK]   18comic.cc                                OK/OK       h301
[无解析]18comic.company                           OK/NX       000     ← 复测：AliDNS 返回疑似污染 IP（108.160 段），CF/Google 均 NXDOMAIN，实测不可达
[OK]   18comic.org                               OK/OK       h301
[受限] 18comic.vip                               OK/OK       403   Just a moment...
[OK]   1kkk.com                                  OK/OK       301   极速漫画_在线漫画_为看漫画的人而生
[OK]   2025copy.com                              OK/OK       200   Redirecting...
[OK]   asjmapihost.cc                            OK/OK       200   Redirecting...
[OK]   boylove.cc                                OK/OK       200   香香腐宅BoyLove│耽美漫畫-最新最全的BL腐漫網
[无解析]boylove.live                              OK/NX       000     ← 复测：AliDNS 返回疑似污染 IP（128.242 段），CF/Google 均 NXDOMAIN，实测不可达
[OK]   boylove1.cc                               OK/OK       h200
[OK]   boyloves.cc                               OK/OK       302   welcome
[OK]   cdnblackmyth.club                         OK/OK       200
[OK]   cdndm5.com                                OK/OK       200   动漫屋_在线漫画_为看漫画的人而生
[受限] cdnmhws.cc                                NO_A/NO_A   000     ← 三方解析均无 A 记录（NOERROR），暂未投入使用；随上游更新
[OK]   cdnmhwscc.vip                             OK/OK       301   Just a moment...
[OK]   cdnuc.vip                                 OK/OK       301   Just a moment...
[无解析]cdnxxx-proxy.co                           NX/NX       000
[无解析]cdnxxx-proxy.xyz                          NX/NX       000
[OK]   copy-manga.com                            OK/OK       200
[OK]   copy20.com                                OK/OK       200   拷貝漫畫 - 海賊王 海贼王 哥布林殺手 哥布林杀手 漫畫 漫画 FGO FGO 東方 东方 艦娘 舰娘 同人志 本子 更新 全集 在綫漫畫 在线漫画 - 拷貝漫畫 拷贝漫画
[OK]   copy2000.online                           OK/OK       200
[OK]   dm5.cn                                    OK/OK       301   动漫屋_在线漫画_为看漫画的人而生
[OK]   dm5.com                                   OK/OK       301   动漫屋_在线漫画_为看漫画的人而生
[OK]   dm9.com                                   OK/OK       301   动漫屋_在线漫画_为看漫画的人而生
[受限] fuhouse.club                              OK/OK       404
[OK]   gmanhua.com                               OK/OK       h301
[OK]   haitangbook.com                           OK/OK       200   海棠文化線上文學城
[OK]   haitbook.com                              OK/OK       200   海棠文化線上文學城
[OK]   hkmanga.com                               OK/OK       301   动漫屋_在线漫画_为看漫画的人而生
[OK]   htlvbooks.com                             OK/OK       200   海棠文化線上文學城
[OK]   htnewbooks.com                            OK/OK       200   海棠文化線上文學城
[OK]   htwhbook.com                              OK/OK       200   海棠文化線上文學城
[OK]   jm-comic2.cc                              OK/OK       200   Redirecting...
[OK]   jm18c-bbm.cc                              OK/OK       301   Just a moment...
[OK]   jm18c-bbm.net                             OK/OK       301   Just a moment...
[OK]   jm18c-uoi.net                             OK/OK       301   Just a moment...
[OK]   jm365.work                                OK/OK       301   Not Found
[OK]   jm365.xyz                                 OK/OK       h200
[OK]   jmapibranch1.cc                           OK/OK       200
[OK]   jmapibranch2.cc                           OK/OK       200   Redirecting...
[OK]   jmapibranch3.cc                           OK/OK       200   Loading...
[OK]   jmapinode.biz                             OK/OK       200   Redirecting...
[受限] jmapinode.vip                             OK/OK       000     ← 复测三方解析均有记录（IP 疑似停放/中转），HTTPS 实测不可达；保留收录以便轮换时命中
[OK]   jmapinode.xyz                             OK/OK       302   welcome
[无解析]jmapinode1.top                            NX/NX       000
[无解析]jmapinode2.top                            NX/NX       000
[无解析]jmapinode3.top                            NX/NX       000
[OK]   jmapinodeudzn.net                         OK/OK       301   Just a moment...
[OK]   jmapinodeudzn.xyz                         OK/OK       301   Just a moment...
[受限] jmapiproxy1.cc                            NO_A/NO_A   000     ← 三方解析均无 A 记录（NOERROR），暂未投入使用；随上游更新
[超时] jmapiproxy1.monster                       S2/NX       000
[OK]   jmapiproxy2.cc                            OK/OK       200   没有找到站点
[受限] jmapiproxy3.cc                            NO_A/NO_A   000     ← 三方解析均无 A 记录（NOERROR），暂未投入使用；随上游更新
[无解析]jmapiproxy4.cc                            NX/NX       000
[无解析]jmapiproxyxxx.vip                         NX/NX       000
[OK]   jmcomic-fb.vip                            OK/OK       301
[受限] jmcomic-zzz.one                           OK/OK       403   Just a moment...
[受限] jmcomic-zzz.org                           OK/OK       403   Just a moment...
[无解析]jmcomic.group                             OK/NX       000     ← 复测：AliDNS 返回疑似污染 IP，CF/Google 均 NXDOMAIN，实测不可达
[OK]   jmcomic.ltd                               OK/OK       200   Redirecting...
[受限] jmcomic.me                                OK/OK       403   Just a moment...
[OK]   jmcomic.mobi                              OK/OK       200   Redirecting...
[OK]   jmcomic.moe                               OK/OK       h200
[受限] jmcomic.rocks                             OK/OK       000     ← 复测三方解析均有记录（IP 疑似停放/中转），HTTPS 实测不可达；保留收录以便轮换时命中
[无解析]jmcomic1.city                             OK/NX       000     ← 复测：AliDNS 返回疑似污染 IP，CF/Google 均 NXDOMAIN，实测不可达
[受限] jmcomic1.me                               OK/OK       403   Just a moment...
[OK]   jmcomic1.mobi                             OK/OK       200   Redirecting...
[超时] jmcomic1.rocks                            OK/OK       000
[受限] jmcomic2.moe                              OK/OK       000     ← 复测三方解析均有记录（IP 疑似停放/中转），HTTPS 实测不可达；保留收录以便轮换时命中
[OK]   lmbooks.com                               OK/OK       200
[OK]   lmebooks.com                              OK/OK       200   海棠文化線上文學城
[受限] longmabook.com                            OK/OK       404
[OK]   longmabookcn.com                          OK/OK       200   海棠文化線上文學城
[OK]   lovehtbooks.com                           OK/OK       200   海棠文化線上文學城
[OK]   lvhtebook.com                             OK/OK       200   海棠文化線上文學城
[OK]   manben.com                                OK/OK       301   漫本_原创漫画发行平台_漫画_在线漫画
[受限] manbenapi.com                             OK/OK       h404
[受限] mangafuna.xyz                             NO_A/NO_A   000     ← 三方解析均无 A 记录（NOERROR），暂不可用；随上游更新
[OK]   manhuaren.com                             OK/OK       200   漫画人 - 为爱漫画的人而生
[OK]   mybookinlm.com                            OK/OK       200   海棠文化線上文學城
[OK]   myhtebook.com                             OK/OK       200   海棠文化線上文學城
[OK]   myhtebooks.com                            OK/OK       200   海棠文化線上文學城
[OK]   myhtlmebook.com                           OK/OK       200   海棠文化線上文學城
[OK]   newhtbook.com                             OK/OK       h200
[OK]   urhtbooks.com                             OK/OK       h200

### 日本（226）
[OK]   13dl.net                                  OK/OK       301   404 Not Found
[OK]   678dl.net                                 OK/OK       200   678 DL.Net - Free Manga DL 無料漫画 ダウンロード
[OK]   a-zmanga.net                              OK/OK       301   A-z manga raw zip rar dl comic daily update | 無料ダウンロード漫画 (まんが)
[OK]   amazon.co.jp                              OK/OK       301   Amazon | 本, ファッション, 家電から食品まで | アマゾン
[OK]   api.comic-fuz.com                         OK/OK       200
[OK]   api.comico.jp                             OK/OK       200
[受限] api.dokusho-ojikan.jp                     OK/OK       403   403 Forbidden
[OK]   api.nicomanga.jp                          OK/OK       200
[超时] api.pocket.shonenmagazine.com             OK/OK       400
[受限] api.sokuyomi.jp                           OK/OK       426
[受限] api.zebrack-comic.com                     OK/OK       404
[受限] api.zerosumonline.com                     OK/OK       404
[OK]   asacomi.jp                                OK/OK       200   アサコミ | 朝日新聞出版の恋愛やホラーマンガが無料で読める！
[OK]   bibibi-comic.com                          OK/OK       200   ビビビコミック | 「ビビッ！ときてるか？」
[OK]   bigcomics.jp                              OK/OK       200   ビッコミ（ビッグコミックス） | いつも、どこでも、漫画と。
[OK]   book.dmm.co.jp                            OK/OK       302   年齢認証 - FANZA
[OK]   book.dmm.com                              OK/OK       200   マンガ・小説・写真集ならDMMブックス！
[OK]   booklive.jp                               OK/OK       200   電子書籍・無料漫画ならブックライブ
[OK]   bookwalker.jp                             OK/OK       200   無料試し読みなら電子書籍ストア - ブックウォーカー ( BOOK WALKER )
[受限] booth.pm                                  OK/OK       403   Just a moment...
[OK]   bv.k-manga.jp                             OK/OK       200
[受限] cdn.hachiraw.net                          OK/OK       500
[受限] cdn.kumaraw.com                           OK/OK       403   Just a moment...
[受限] cdn.sokuyomi.jp                           OK/OK       403   403 Forbidden
[OK]   ch.dlsite.com                             OK/OK       200   DLチャンネル - みんなで作る二次元情報サイト！
[OK]   championcross.jp                          OK/OK       200   チャンピオンクロス | 秋田書店の新作マンガが無料で読める！
[OK]   ciao.shogakukan.co.jp                     OK/OK       200   ちゃおプラス 公式サイト
[受限] cmo.jp                                    OK/OK       403   403 - Forbidden
[OK]   cmoa.jp                                   NO_A/NO_A   000     ← コミックシーモア：apex 无 DNS 属正常，实际用 www.cmoa.jp，按后缀收录
[OK]   comic-action.com                          OK/OK       200   webアクション｜双葉社発のマンガサイト
[OK]   comic-boost.com                           OK/OK       200   comicブースト｜さらに面白く、さらに読みやすく――webマンガサイトを《加速》させるcomicブースト
[超时] comic-clear.jp                            NO_A/NO_A   000
[OK]   comic-days.com                            OK/OK       200   コミックDAYS
[OK]   comic-earthstar.com                       OK/OK       200   コミック アース・スター｜毎週木曜・最新話更新！無料で漫画が読めるWEBコミック誌
[OK]   comic-fuz.com                             OK/OK       200   COMIC FUZ
[OK]   comic-gardo.com                           OK/OK       200   コミックガルド
[OK]   comic-growl.com                           OK/OK       200   コミックグロウル | 毎日更新！無料で読めるWEBマンガサイト
[OK]   comic-meteor.jp                           OK/OK       301   COMICメテオ - きら星ポータル きらポ
[OK]   comic-ogyaaa.com                          OK/OK       200   COMIC OGYAAA!! (コミックオギャー)｜おもしろい、がうまれるところ
[OK]   comic-room-base.com                       OK/OK       200   COMIC ROOM BASE | コミックルームの人気マンガが無料で読めるWebサイト！
[OK]   comic-ryu.jp                              OK/OK       200   COMICリュウライブ | 徳間書店の人気マンガが無料で読める！
[OK]   comic-seasons.com                         OK/OK       200   Seasons｜春夏秋冬、恋をする
[OK]   comic-trail.com                           OK/OK       200   コミックトレイル｜漫画とつながるフェス空間！
[OK]   comic-walker.com                          OK/OK       200   カドコミ (コミックウォーカー)｜KADOKAWAの無料漫画が読める！
[OK]   comic-y-ours.com                          OK/OK       200   COMIC Y-OURS(ユアーズ)｜未だ見ぬ漫画に。
[OK]   comic-zenon.com                           OK/OK       200   ゼノンプラス｜コアミックスの公式WEBマンガサイト
[OK]   comic.iowl.jp                             OK/OK       200   コミックフェスタ | ComicFesta
[OK]   comic.j-nbooks.jp                         OK/OK       200   COMICリュエル&amp;COMICジャルダン | 異世界から日常まで、無料で読めるwebマンガサイト
[OK]   comic.k-manga.jp                          OK/OK       200   まんが王国｜無料漫画・電子コミックが10,000冊以上！お得感No.1
[无解析]comic.nicovideo.jp                        OK/NX       000     ← 域名已停用：复测 CF/Google 均 NXDOMAIN；官方漫画入口现为 nicomanga.com
[OK]   comicborder.com                           OK/OK       200   コミックボーダー
[OK]   comicnettai.com                           OK/OK       h301
[OK]   comicpash.jp                              OK/OK       200   コミックPASH! neo | 人気マンガが毎日無料で読める！
[OK]   comicride.jp                              OK/OK       200   ライコミ（コミックライド） | 異世界・恋愛の&quot;Web漫画&quot;の新しい波はここから!!
[OK]   comics.manga-bang.com                     OK/OK       200   マンガBANGコミックス | 毎日無料で楽しめる！！
[OK]   comirela.com                              OK/OK       200   コミリラ | 無料で人気女性向けマンガが読めるwebサイト！
[OK]   cs.dlsite.com                             OK/OK       302   Just a moment...
[OK]   cycomi.com                                OK/OK       200   サイコミ | オリジナル漫画・人気コミックが毎日無料！
[OK]   dbook.docomo.ne.jp                        OK/OK       200   漫画・無料試し読みならdブック
[OK]   dl-zip.com                                OK/OK       200   Dl-Zip.com | Raw Manga Free Download And Updated Daily
[OK]   dlaf.jp                                   OK/OK       301   DLsite：同人誌、同人ゲームからPCソフト、コミックまで二次元総合ダウンロードショップ | DLsite 総合トップページ
[OK]   dlraw.net                                 OK/OK       301   DLRAW｜Raw Manga ダウンロードサイト
[OK]   dlraw.tv                                  OK/OK       200   DLRAW｜Raw Manga ダウンロードサイト
[OK]   dlsite.com                                OK/OK       301   DLsite：同人誌、同人ゲームからPCソフト、コミックまで二次元総合ダウンロードショップ | DLsite 総合トップページ
[OK]   dmm.co.jp                                 OK/OK       301   年齢認証 - FANZA
[OK]   dmm.com                                   OK/OK       301   DMM.com - DMM TV・ゲーム・動画・電子書籍・英会話・FX等の総合サイト
[OK]   dokiraw.click                             OK/OK       301   Dokiraw - 無料のオンラインマンガ読みサイト!
[OK]   dokiraw.link                              OK/OK       200   Dokiraw - 無料のオンラインマンガ読みサイト!
[OK]   dokusho-ojikan.jp                         OK/OK       200   人気漫画を無料で試し読み・全巻お得に読むならAmebaマンガ
[OK]   drecomi-plus.jp                           OK/OK       200   ドリコミ＋（ドリコミプラス）｜公式WEBマンガサイト
[受限] drm.cdn.nicomanga.jp                      OK/OK       404
[OK]   ebookjapan.yahoo.co.jp                    OK/OK       200   無料漫画・試し読みが豊富！電子書籍をお得に購入 ebookjapan
[OK]   ebookstore.sony.jp                        OK/OK       200   電子書籍・漫画ならソニーのReader Store｜無料でも楽しめる！
[OK]   ec.toranoana.jp                           OK/OK       200   同人誌・同人グッズ通販のとらのあな
[OK]   fanbox.cc                                 OK/OK       302   pixivFANBOX(ファンボックス)
[OK]   fantia.jp                                 OK/OK       200   ファンティア[Fantia]｜クリエイター支援プラットフォーム
[OK]   feelweb.jp                                OK/OK       200   FEEL web｜マンガの数だけ愛がある
[OK]   firecross.jp                              OK/OK       200   ファイアCROSS
[OK]   flowercomics.jp                           OK/OK       200   フラコミlike!
[OK]   g-comi.jp                                 OK/OK       200   Gコミ | あなたの「好き」が見つかる無料コミックサイト
[OK]   ganma.jp                                  OK/OK       301   GANMA!(ガンマ)｜話題のマンガ・ウェブトゥーンが無料で読める！
[OK]   gaugau.futabanet.jp                       OK/OK       200   面白さモンスター級のラノベ漫画・コミック・小説サイト がうがうモンスター＋【毎日無料】
[OK]   gorakuweb.com                             OK/OK       200   ゴラクうぇぶ! | 日本文芸社の公式Webまんがサイト！
[受限] hachiraw.net                              OK/OK       403   Just a moment...
[OK]   hachiraw.win                              OK/OK       200   最新のマンガアップデート &#8211; コミックシーモア
[OK]   hanayume.com                              OK/OK       200   花とゆめ＋ | 無料で人気まんがが読める公式サイト
[OK]   hayacomic.jp                              OK/OK       200   ハヤコミ | SF・ミステリマンガが無料！
[OK]   heros-web.com                             OK/OK       200   HERO&#x27;S Web（ヒーローズウェブ）公式サイト | 毎日更新のマンガサイト！多彩な作品が無料で読める
[OK]   honto.jp                                  OK/OK       200   電子書籍ストア - デジタル漫画・コミック購入ならhonto - 無料・試し読みも
[OK]   ichicomi.com                              OK/OK       200   一迅プラス
[OK]   idol.gravureprincess.date                 OK/OK       200   Idol. gravureprincess .date
[受限] img.comic-fuz.com                         OK/OK       403   403 Forbidden
[OK]   img.dlsite.jp                             OK/OK       200
[OK]   jmanga.cyou                               OK/OK       301   jmanga - Raw Manga, 漫画raw, Manga Raw, 無料で読め, 無料漫画(マンガ)読む, 漫画スキャン王
[OK]   jmanga.media                              OK/OK       200   jmanga - Raw Manga, 漫画raw, Manga Raw, 無料で読め, 無料漫画(マンガ)読む, 漫画スキャン王
[超时] jp.kobo.com                               OK/NX       000
[OK]   jpddl.com                                 OK/OK       200   JPDDL
[OK]   jraws.net                                 OK/OK       200   Download Japanese Manga, Magazines, and Doujins &#x2d; Rapidgator rar zip downloads 漫画 小説
[受限] jumpg-webapi.tokyo-cdn.com                OK/OK       403   403 Forbidden
[OK]   jumptoon.com                              OK/OK       200   ジャンプTOON | オリジナル連載作品が初回全話無料で読める！
[OK]   k-manga.jp                                OK/OK       h301
[OK]   kansai.mag-garden.co.jp                   OK/OK       200   マグカン | 人気マンガが毎日無料で読める
[OK]   kimicomi.com                              OK/OK       200   キミコミ | キミが欲しいコミックがここにある。話題の異世界・恋愛・ファンタジー漫画がまとめて読める！
[OK]   kirapo.jp                                 OK/OK       200   きら星ポータル - メテオ・ポラリス・アンブル・エトワール・アスティル・ズレット！の公式WEBマンガサイト きらポ
[受限] klraw.info                                OK/OK       523
[OK]   klto9.com                                 OK/OK       200   KT9 - Read Manga Raw Online Free
[OK]   klz9.com                                  OK/OK       200   KL - Read Manga Raw Online Free
[OK]   kmansin09.top                             OK/OK       200   Home - K-漫神 - Kmansin09
[受限] kumaraw.com                               OK/OK       403   Just a moment...
[OK]   kuragebunch.com                           OK/OK       200   くらげバンチ
[OK]   login.dlsite.com                          OK/OK       302   viviON ID - はじめての方へ
[OK]   love4u.net                                OK/OK       200   Love4u - Read manga raw high quality
[OK]   manga-5.com                               OK/OK       200   マンガ5(マンガファイブ) presented by レベルファイブ
[OK]   manga-mee.jp                              OK/OK       200   マンガMee(マンガミー)人気のコミックが全話無料で読める漫画サイト！ ｜名作少女漫画・ドラマ アニメ化作品多数  ← 复测存活：2026-10-05 实测 200、标题「マンガMee…」；jp.md 曾据旧信息记为已下线，以本文 §7 实测为准，按存活收录
[OK]   manga-meets.jp                            OK/OK       200   マンガMeets | 集英社の少女・女性向け総合マンガ投稿サイト
[OK]   manga-no.com                              OK/OK       200   マンガノ - 新しいマンガ投稿サイト
[OK]   manga-one.com                             OK/OK       200   マンガワン
[OK]   manga-park.com                            OK/OK       200   マンガPark（マンガパーク） | 人気のマンガが毎日読み放題！
[OK]   manga-raw.club                            OK/OK       200   Redirecting...
[OK]   manga-zegra.com                           OK/OK       200   マンガゼグラ | コミックグラストの人気マンガが無料で読めるWebサイト！
[OK]   manga-zip.app                             OK/OK       301   MANGA ZIP - Download Free Raw Manga
[OK]   manga-zip.is                              OK/OK       200   MANGA ZIP - naruto,one piece,bleach,worst,Yu-Gi-Oh,Hunter X Hunter...
[OK]   manga-zip.my                              OK/OK       200   Manga-Zip.MY - 漫画raw・manga zip無料ダウンロード
[OK]   manga.fod.fujitv.co.jp                    OK/OK       301   FOD | フジテレビ公式、電子書籍も展開中
[无解析]manga109.com                              NX/NX       000
[OK]   mangabu.jp                                OK/OK       200   MANGABU!(マンガ部!) | ファムエンタテイメントのマンガが無料で読めるWEBサイト！
[OK]   mangacross.jp                             OK/OK       301   チャンピオンクロス | 秋田書店の新作マンガが無料で読める！
[OK]   mangakuro.net                             OK/OK       301   無料漫画（漫画）- RawKuro - manga1001 - 漫画ロウ, mangaraw, manga raw, manga1001, manga1000, 漫画raw, 漫画
[OK]   mangalt.jp                                OK/OK       200   マンガルト -Mangalt- | 毎月更新・無料や割引キャンペーンも随時開催！
[受限] mangamura.me                              OK/OK       523
[OK]   mangaplus.shueisha.co.jp                  OK/OK       200   MANGA Plus by SHUEISHA
[OK]   mangaraw.best                             OK/OK       200   漫画 raw - Manga Raw - 漫画 raw
[OK]   mangaraw.co                               OK/OK       302   Loading...
[OK]   mangaraw.to                               OK/OK       200   Redirecting...
[OK]   mangaraw.xyz                              OK/OK       301   漫画 raw - Manga Raw - 漫画 raw
[OK]   mangatime-square.com                      OK/OK       200   まんがタイムSquare｜まんがタイムの「今」が集まる。 読者と作品の広場（スクエア）。
[OK]   mechacomi.jp                              OK/OK       200   まんがセゾン | 無料で試し読みもできる！スキマ時間をスキな時間に
[OK]   mechacomic.jp                             OK/OK       200   漫画なら、めちゃコミック（めちゃコミ）
[OK]   melonbooks.co.jp                          OK/OK       301   メロンブックス 国内最大級の同人・コミック・グッズ メロブの通販サイト - メロンブックス
[受限] member.bookwalker.jp                      OK/OK       404
[OK]   momon-ga.com                              OK/OK       200   エロ漫画 momon:GA（モモンガッ!!）
[OK]   music-book.jp                             OK/OK       302   ログイン｜音楽、コミック・電子書籍、動画ならmusic.jp
[OK]   namicomic.jp                              OK/OK       200   なみコミ | ラブコメ、異世界転生、BL、ファンタジーなどの人気マンガが無料で楽しめる！
[OK]   nicomanga.com                             OK/OK       200   Read Raw Manga Online with Instant Translation - Nicomanga - Raw Manga Translator
[OK]   nihonkuni.com                             OK/OK       200   NihonKuni - Read Manga Raw Scan High Quality The Latest
[OK]   nikkangecchan.jp                          OK/OK       200   日刊月チャン | 秋田書店
[OK]   ourfeel.jp                                OK/OK       200   OUR FEEL（アワフィール）| 女性マンガレーベル、第1・3木曜日更新!!
[OK]   papy.co.jp                                OK/OK       200   株式会社パピレス
[OK]   pash-up.jp                                OK/OK       200   PASH UP!｜無料たっぷり！最速公開！マンガもラノベもアニメ誌も
[OK]   piacomic.jp                               OK/OK       200   ぴあコミック | エンタメを知り尽くしたぴあが贈る、WEBコミック！
[OK]   play.dlsite.com                           OK/OK       200   DLsite Play
[OK]   pocket.shonenmagazine.com                 OK/OK       200   マガポケ | 少年マガジン公式無料漫画アプリ
[受限] prod-contents-br-page.akamaized.net       OK/OK       403
[OK]   r18.mangaz.com                            OK/OK       302   年齢確認 | 全巻無料で漫画読み放題！ - マンガ図書館Z
[无解析]raw-free.com                              NX/NX       000
[OK]   raw-zip.com                               OK/OK       200   Raw-Zip.com | Raw Manga free download - ARTBOOK | MANGA | NOVEL | 雑誌
[OK]   raw.senmanga.com                          OK/OK       200   Sen Manga
[OK]   raw1001.net                               OK/OK       301   無料漫画（漫画）- raw1001 - 漫画ロウ, mangaraw, manga raw, manga1001, manga1000, 漫画raw, 漫画ばんく, 無料 漫画,
[OK]   raw18.bar                                 OK/OK       200   Raw18 - エロ漫画 カラー
[OK]   raw18.icu                                 OK/OK       301   Raw18 - エロ漫画 カラー
[OK]   raw77.com                                 OK/OK       200   Raw 77. com - 無料漫画、コミックのzip
[OK]   rawbaka.com                               OK/OK       301   rawbaka.site -
[OK]   rawbaka.site                              OK/OK       200   rawbaka.site -
[OK]   rawdevart.art                             OK/OK       200   Japanese Manga Raw - Rawdevart
[OK]   rawdevart.com                             OK/OK       200   Redirecting...
[OK]   rawhost.net                               OK/OK       200   RawHost – Bulletproof, Anonymous & Offshore VPS Hosting
[OK]   rawinu.com                                OK/OK       200   RawINU - Read Raw Manga Online New Free
[OK]   rawkuma.com                               OK/OK       200   Rawkuma | Discover Raw Manga &amp; Japanese Manga
[OK]   rawkuma.net                               OK/OK       200   Rawkuma &#8211; Read Raw Manga Online Hiqh Quality
[无解析]rawload.net                               NX/NX       000
[OK]   rawmanga.xyz                              OK/OK       200   赤報漫畫[RawManga.xYz]
[OK]   rawmiu.com                                OK/OK       301   MiuRaw.Com - 生のマンガをオンラインで無料で読む - Read Manga Online Free
[OK]   rawotaku.com                              OK/OK       200   Raw Otaku - Raw Manga, Manga raw, 漫画raw, 無料で読め, 無料漫画(マンガ)読む, 漫画スキャン王
[OK]   rawsakura.org                             OK/OK       200   Manga raw desu!! - RawSakura
[OK]   rawuwu.net                                OK/OK       200   Read Manga Raw Online For Free - RawUwU
[OK]   renta.com                                 OK/OK       200   Renta Group - North-European Construction Equipment Rental
[OK]   renta.papy.co.jp                          OK/OK       200   �ޥ󥬡����硼�ȥɥ�ޡ����˥ᡦ�Υ٥�ʤ�Renta!(���)��̵������ɤߡ�
[OK]   rimacomiplus.jp                           OK/OK       200   リマコミ＋ | 無料で集英社の少女・女性マンガが読める
[OK]   rookie.shonenjump.com                     OK/OK       200   ジャンプルーキー！ | 誰でもジャンプでデビューできる、マンガ投稿サービス
[OK]   sai-zen-sen.jp                            OK/OK       200   最前線 - フィクション・コミック・Webエンターテイメント
[OK]   seiga.nicovideo.jp                        OK/OK       200   ニコニコ静画
[OK]   shonenjumpplus.com                        OK/OK       200   少年ジャンプ＋｜人気オリジナル連載が全話無料！の最強WEBマンガ誌
[OK]   sokuyomi.jp                               OK/OK       200   無料漫画・試し読みが充実！電子書籍を読むなら【ソク読み】
[OK]   sp.manga.nicovideo.jp                     OK/OK       200   ニコニコ漫画 - 雑誌やWebの人気マンガが読める！
[OK]   sunday-webry.com                          OK/OK       h301
[OK]   takecomic.jp                              OK/OK       200   竹コミ！ | 竹書房の新作マンガが毎日更新・無料で読める！
[OK]   to-corona-ex.com                          OK/OK       200   コロナEX｜TOブックスの公式Web漫画サイト
[OK]   tonarinoyj.jp                             OK/OK       200   となりのヤングジャンプ
[OK]   toranoana.jp                              OK/OK       301   �R�~�b�N�Ƃ�̂��ȁF���l�����͂��ߖG����A�C�e�������ł������I
[OK]   urasunday.com                             OK/OK       302   マンガワン
[OK]   video.unext.jp                            OK/OK       200   U-NEXT（ユーネクスト）-映画 / ドラマ / アニメから、マンガや雑誌といった電子書籍まで-│31日間無料トライアル
[受限] viewer-df.bookwalker.jp                   OK/OK       404
[受限] viewer-trial.bookwalker.jp                OK/OK       404
[受限] viewer.bookwalker.jp                      OK/OK       404
[受限] web.cycomi.com                            OK/ERR      403   403 Forbidden
[OK]   webaction.jp                              OK/OK       301   webアクション｜双葉社発のマンガサイト
[受限] webapi.ynjn.jp                            OK/OK       404
[OK]   webcomic.ohtabooks.com                    OK/OK       200   Ohta Web Comic [太田出版のウェブ漫画]
[OK]   weloma.net                                OK/OK       200   WeLoMa - Read Manga Raw Free Online Hight Quality
[OK]   www.alphapolis.co.jp                      OK/OK       200   アルファポリス - 小説・漫画・ビジネス等の総合エンターテインメントサイト
[受限] www.cmo.jp                                OK/OK       403   403 - Forbidden
[OK]   www.cmoa.jp                               OK/OK       200   漫画多すぎ！業界最大級のコミックシーモア｜無料で楽しめる！
[OK]   www.comico.jp                             OK/OK       200   comico (コミコ) | タテカラー漫画が毎日無料、毎日更新！
[OK]   www.corocoro.jp                           OK/OK       200   週刊コロコロコミック
[OK]   www.dlsite.com                            OK/OK       301   DLsite：同人誌、同人ゲームからPCソフト、コミックまで二次元総合ダウンロードショップ | DLsite 総合トップページ
[无解析]www.dlsitestudio.com                      NX/NX       000     ← 复测三方均 NXDOMAIN，域名不存在（DLsite 创作端走 dlsite.com，勿收）
[OK]   www.dmm.co.jp                             OK/OK       302   年齢認証 - FANZA
[OK]   www.dmm.com                               OK/OK       200   DMM.com - DMM TV・ゲーム・動画・電子書籍・英会話・FX等の総合サイト
[OK]   www.fanbox.cc                             OK/OK       200   pixivFANBOX(ファンボックス)
[OK]   www.ganganonline.com                      OK/OK       200   ガンガンONLINE
[受限] www.kobo.com                              OK/OK       403   Challenged | Kobo.com
[OK]   www.manga-up.com                          OK/OK       200   無料漫画・新作コミックを読むならマンガＵＰ！ | SQUARE ENIX
[OK]   www.mangaz.com                            OK/OK       200   全巻無料で漫画読み放題！ - マンガ図書館Z
[OK]   www.melonbooks.co.jp                      OK/OK       200   メロンブックス 国内最大級の同人・コミック・グッズ メロブの通販サイト - メロンブックス
[OK]   www.sunday-webry.com                      OK/OK       200   サンデーうぇぶり
[OK]   www.toranoana.jp                          OK/OK       200   �R�~�b�N�Ƃ�̂��ȁF���l�����͂��ߖG����A�C�e�������ł������I
[OK]   www.yomonga.com                           OK/OK       200   ぶんか社の無料マンガサイト | 復讐サスペンス、話題の実写ドラマ化作品、異世界ファンタジーまで、株式会社ぶんか社＆海王社の幅広いラインナップが読める無料マンガサイト「マンガよもんが
[OK]   x3-dl.net                                 OK/OK       200   X3-DL.net - 漫画 小説 一般書籍 RAW ZIP RAR 無料 ダウンロード
[OK]   yanmaga.jp                                OK/OK       200   ヤンマガWeb - マンガ・グラビアが毎日無料！
[OK]   yawaspi.com                               OK/OK       200   やわらかスピリッツ
[OK]   ynjn.jp                                   OK/OK       200   ヤンジャン＋｜集英社・ジャンプ系青年マンガ公式
[OK]   yomonga.com                               OK/OK       301   ぶんか社の無料マンガサイト | 復讐サスペンス、話題の実写ドラマ化作品、異世界ファンタジーまで、株式会社ぶんか社＆海王社の幅広いラインナップが読める無料マンガサイト「マンガよもんが
[OK]   younganimal.com                           OK/OK       200   ヤングアニマルWeb | 基本無料でマンガもグラビアも楽しめる！
[OK]   youngchampion.jp                          OK/OK       200   ヤンチャンWeb（ヤングチャンピオン） | 人気マンガやグラビアが毎日無料！アナタの日常を満たすオールジャンルエンタメサイト。
[OK]   zebrack-comic.shueisha.co.jp              OK/OK       200   ゼブラック｜総合電子書店
[OK]   zerosumonline.com                         OK/OK       200   ゼロサムオンライン

### 韩国（105）
[OK]   11toon.com                                OK/OK       200   최신애니 최신만화 일일툰 - 일일툰 일본만화 무료만화 무료웹툰 무료애니
[OK]   11toon1.com                               OK/OK       200   일일툰주소
[OK]   11toon149.com                             OK/OK       200   최신애니 최신만화 일일툰 - 일일툰 일본만화 무료만화 무료웹툰 무료애니
[受限] ac-full.series.naver.com                  OK/OK       403   403 Forbidden
[受限] active.ridibooks.com                      OK/OK       404
[OK]   anytoon.co.kr                             OK/OK       301   애니툰 - 웹툰, 웹소설, 무료웹툰
[受限] api.lezhin.com                            OK/OK       401
[受限] api.ridibooks.com                         OK/OK       404
[受限] azrael.toptoon.com                        OK/OK       403   403 Forbidden
[OK]   blacktoon.me                              OK/OK       301   BlackToon 블랙툰 - 무료웹툰 웹툰미리보기
[OK]   blacktoon423.com                          OK/OK       200   BlackToon 블랙툰 - 무료웹툰 웹툰미리보기
[OK]   blacktoonurl.net                          OK/OK       301   블랙툰 링크 BlackToon링크- 최신 접속 주소
[OK]   bomtoon.com                               OK/OK       301   봄툰 - 순정, 로맨스, BL 장르가 가득한 여성 독자를 위한 프리미엄 웹툰
[OK]   bomtoon.tw                                OK/OK       301   BOMTOON - 來自韓國的優質女性向網漫平台。浪漫愛情，耽美BL等內容盡在BOMTOON。
[受限] bookto31.com                              OK/OK       403   Just a moment...
[OK]   ccdn.lezhin.com                           OK/OK       307   레진코믹스 - 솔직한 재미 대폭발
[受限] cdn.anytoon.co.kr                         OK/OK       403   403 Forbidden
[OK]   cdn.megadata.co.kr                        OK/OK       302   404 - ���� �Ǵ� ���͸��� ã�� �� �����ϴ�.
[OK]   comic.naver.com                           OK/OK       302   네이버 웹툰
[受限] comicthumb-phinf.pstatic.net              OK/OK       404
[OK]   contents.kr.kakaowebtoon.com              OK/OK       200
[OK]   cookmana56.com                            OK/OK       200   쿡마나 - 최신만화 일본만화 무료만화 무료웹툰
[OK]   cp.ridibooks.com                          OK/OK       302   리디 Contents Partners
[OK]   daycomics.com                             OK/OK       200
[受限] dn-img-page.kakao.com                     OK/OK       403   403 Forbidden
[OK]   global.toomics.com                        OK/OK       302   Toomics - Read unlimited VIP comics online
[OK]   global.toptoon.com                        OK/OK       200   Toptoon: Stories you never knew you needed.
[超时] image-comic.pstatic.net                   OK/OK       400
[受限] image.balcony.studio                      OK/OK       403
[受限] img.mrblue.com                            OK/OK       403   403 Forbidden
[受限] img.ridicdn.net                           OK/OK       404
[无解析]joa-vip.com                               S2/S2       000     ← 复测三方均 SERVFAIL，疑似再次换域（原公告见 뉴토끼监控频道）
[OK]   kakaowebtoon.com                          OK/OK       302   카카오웹툰 - KAKAO WEBTOON
[OK]   kmana10.net                               OK/OK       200   K만화 - 최신만화 일본만화 무료만화 무료웹툰
[OK]   kr-a.kakaopagecdn.com                     OK/OK       200
[OK]   lezhin-web.lezhin.com                     OK/OK       200   Title
[OK]   lezhin.com                                OK/OK       302   레진코믹스 - 솔직한 재미 대폭발
[OK]   lezhin.jp                                 OK/OK       200   レジンコミックス - オリジナル漫画が毎日更新
[OK]   linkbbg8.com                              OK/OK       200   링크비비기 | 주소모음 주소야 사이트모음 링크모음 가이드
[OK]   m.anytoon.co.kr                           OK/OK       301   애니툰 - 웹툰, 웹소설, 무료웹툰
[OK]   m.comic.naver.com                         OK/OK       302   네이버 웹툰
[OK]   m.series.naver.com                        OK/OK       302   네이버 시리즈
[OK]   m.webtoons.com                            OK/OK       302   WEBTOON - Read Comics, Manga &amp; Manhwa
[OK]   manatoki555.net                           OK/OK       301   링크비비기 | 주소모음 주소야 사이트모음 링크모음 가이드
[OK]   marumaru103.com                           OK/OK       200   마루마루 | 무료 웹툰 미리보기 · 만화·소설 최신 회차
[受限] marumaru104.com                           NO_A/NO_A   000     ← 마루마루 Telegram 预告的下一地址，尚未上线
[受限] mato31.com                                OK/OK       403   Just a moment...
[受限] mgeko.cc                                  OK/OK       403   Attention Required! | Cloudflare
[OK]   mrblue.com                                OK/OK       301   미스터블루 - 웹툰, 만화, 소설
[受限] naverwebtoon-phinf.pstatic.net            OK/OK       404
[受限] newto31.com                               OK/OK       403   Just a moment...
[OK]   newtoki1.org                              OK/OK       200   뉴토끼 - 최신 웹툰 미리보기
[受限] newxtoon1.com                             OK/OK       403   Attention Required! | Cloudflare
[OK]   novel.naver.com                           OK/OK       200   네이버웹소설
[OK]   page.kakao.com                            OK/OK       200   추천 | 카카오페이지
[受限] page.kakaocdn.net                         S2/OK       403
[受限] panther.lezhin.com                        OK/OK       404
[OK]   rawdex.net                                OK/OK       200   Read Manga, Manhwa &amp; Webtoon Raw Online | RawDEX
[受限] rcdn.lezhin.com                           OK/OK       403
[OK]   ridibooks.com                             OK/OK       302   만화 웹툰 웹소설 도서는 리디
[OK]   ridihelp.ridibooks.com                    OK/OK       302   지원 : 고객센터
[OK]   sbxh9.com                                 OK/OK       200   뉴토끼 — 무료 웹툰 미리보기 | 뉴토끼
[OK]   select.ridibooks.com                      OK/OK       200   리디셀렉트 - 신간도 베스트셀러도 무제한으로 즐기는 전자책 구독 서비스
[OK]   series.naver.com                          OK/OK       302   네이버 시리즈
[超时] shared-comic.pstatic.net                  OK/OK       400
[受限] smurfs.toptoon.com                        OK/OK       403   403 Forbidden
[OK]   spotv147.com                              OK/OK       h301
[受限] static.mrblue.com                         OK/OK       403   403 Forbidden
[OK]   static.ridicdn.net                        OK/OK       200   404 Not Found - 리디
[受限] thumb-g.toomics.com                       OK/OK       403   403 Forbidden
[受限] thumb-g1.toomics.com                      OK/OK       404
[受限] thumb-g2.toomics.com                      OK/OK       404
[超时] tkor146.com                               OK/OK       000
[OK]   toomics.com                               OK/OK       302   Toomics - Read unlimited VIP comics online
[OK]   toonily.com                               OK/OK       200   Read Manhwa Online Free - Latest Chapters &amp; Webtoons | Toonily
[OK]   toonkor0.org                              OK/OK       301   툰코(Toonkor) - 웹툰
[OK]   toonkor404.com                            OK/OK       200   툰코 - 웹툰 사이트 | 최신 웹툰·만화·소설 업데이트
[受限] toonkor405.com                            NO_A/NO_A   000     ← 툰코 Telegram 预告的下一地址，尚未上线（三方均无 A 记录）
[OK]   toptoon.com                               OK/OK       200   탑툰
[OK]   toptoon.net                               OK/OK       302   TOPTOON 漫畫 條漫-國際官方中文版-韓國最新漫畫-線上免費看
[OK]   toptoonplus.com                           OK/OK       200
[受限] webtoon-phinf.pstatic.net                 OK/OK       403   Referral Denied
[OK]   webtoon.kakao.com                         OK/OK       200   카카오웹툰 - KAKAO WEBTOON
[OK]   webtoons.com                              OK/OK       301   WEBTOON - Read Comics, Manga &amp; Manhwa
[OK]   wfwf507.com                               OK/OK       200   ������� �ּ� �ȳ�..
[OK]   wfwf510.com                               OK/OK       200   ������� - ��������
[OK]   www.11toon.com                            OK/OK       200   최신애니 최신만화 일일툰 - 일일툰 일본만화 무료만화 무료웹툰 무료애니
[OK]   www.11toon149.com                         OK/OK       200   최신애니 최신만화 일일툰 - 일일툰 일본만화 무료만화 무료웹툰 무료애니
[OK]   www.anytoon.co.kr                         OK/OK       301   애니툰 - 웹툰, 웹소설, 무료웹툰
[OK]   www.bomtoon.com                           OK/OK       200   봄툰 - 순정, 로맨스, BL 장르가 가득한 여성 독자를 위한 프리미엄 웹툰
[OK]   www.bomtoon.tw                            OK/OK       200   BOMTOON - 來自韓國的優質女性向網漫平台。浪漫愛情，耽美BL等內容盡在BOMTOON。
[OK]   www.goodtoon005.com                       OK/OK       301   GoodToon | 무료 웹툰
[OK]   www.goodtoon006.com                       OK/OK       200   GoodToon | 무료 웹툰
[OK]   www.lezhin.com                            OK/OK       307   레진코믹스 - 솔직한 재미 대폭발
[OK]   www.mrblue.com                            OK/OK       200   미스터블루 - 웹툰, 만화, 소설
[OK]   www.spotv147.com                          OK/OK       h301
[OK]   www.toptoon.net                           OK/OK       200   TOPTOON 漫畫 條漫-國際官方中文版-韓國最新漫畫-線上免費看
[OK]   www.webtoons.com                          OK/OK       301   WEBTOON - Read Comics, Manga &amp; Manhwa
[OK]   xn--2s2ba48db550hj3b2ys7xi.com            OK/OK       200   마루마루 - 최신 일본만화·무료만화 번역 공식 최신주소
[OK]   xn--910b43d93g9lo.com                     OK/OK       h308
[受限] xn--h10bt26abuh3me.com                    OK/OK       403   Just a moment...
[受限] xn--h10bt26abuh3me.net                    OK/OK       403   Just a moment...
[OK]   xn--hq1bs8p27g.com                        OK/OK       200   온도북 - 빠른 웹소설 무료 미리보기 다시보기 사이트
[OK]   xn--hq1bt26abyi.com                       OK/OK       200   온도툰 - 최신 웹툰 미리보기 다시보기 추천 사이트
[OK]   xn--ok0b03z1ndutj89hqne.com               OK/OK       200   툰코 - 최신웹툰·인기웹툰·한국웹툰 공식 최신주소 안내 및 한국 웹툰 정보 사이트

### 英文/全球（95）
[OK]   18porncomic.com                           OK/OK       200   18PornComic: Read Hentai - Porncomic online for free
[OK]   about.webtoon.com                         OK/OK       200   WEBTOON Entertainment
[OK]   advertising.webtoon.com                   OK/OK       307   WEBTOON Advertising
[OK]   allporncomic.com                          OK/OK       200   Porn Comics, Hentai Manga, Retro Sex XXX Rule 34 Adult Comics
[OK]   api.mangadex.org                          OK/OK       308   MangaDex API documentation
[OK]   auth.mangadex.org                         OK/OK       200   MangaDex - Authentication Home
[OK]   azuki.co                                  OK/OK       301   Omoi – Read officially licensed digital manga with a monthly subscription app
[OK]   bato.ing                                  OK/OK       302   THIS WEBSITE HAS BEEN CLOSED
[OK]   bato.si                                   OK/OK       302   THIS WEBSITE HAS BEEN CLOSED
[OK]   bato.to                                   OK/OK       302   THIS WEBSITE HAS BEEN CLOSED
[OK]   bato1.com                                 OK/OK       200   Batoto – Read BL Manga, Manhwa & Yaoi Online Free (2026) | xBato
[OK]   batotwo.com                               OK/OK       302   THIS WEBSITE HAS BEEN CLOSED
[OK]   battwo.com                                OK/OK       302   THIS WEBSITE HAS BEEN CLOSED
[OK]   bookwalker.com                            OK/OK       200   BookWalker
[OK]   comics.8muses.com                         OK/OK       301   8muses - Free Sex Comics And Adult Cartoons. Full Porn Comics, 3D Porn and More
[OK]   comics.inkr.com                           OK/OK       200   Read The Latest Manga, Manhua, Webtoon and Comics on INKR!
[OK]   comikey.com                               OK/OK       200   Home - Comikey
[OK]   comiko.net                                OK/OK       200   Xôi Lạc TV – Xem bóng đá trực tuyến full hd, âm thanh sống động
[受限] comix.to                                  OK/OK       403   Just a moment...
[受限] comix.ws                                  OK/OK       403   Just a moment...
[OK]   comizy.io                                 OK/OK       200   COMIZY.io — Read Comics &amp; Manga Online Free, New Chapters Daily
[OK]   creators.webtoon.com                      OK/OK       307   Creators ・ WEBTOON for Creators
[OK]   doujins.com                               OK/OK       200   Doujins.com | English-Translated Hentai, No Ads
[OK]   dynasty-scans.com                         OK/OK       200   Dynasty Reader &raquo; Recently Released Chapters
[OK]   fanfox.net                                OK/OK       200   Manga Fox - Read Manga Online for Free!
[OK]   forums.mangadex.org                       OK/OK       200   MangaDex Forums
[OK]   global.bookwalker.jp                      OK/OK       301   BookWalker
[OK]   go.hentaigold.net                         OK/OK       200
[OK]   hentaigold.net                            OK/OK       200
[OK]   hentainexus.com                           OK/OK       200   Index :: HentaiNexus
[受限] hentairead.com                            OK/OK       403   Just a moment...
[受限] i1.hentaifox.com                          OK/NX       000     ← 图片子域：复测 CF/Google NXDOMAIN，实际在用 i2/i3（主域后缀规则已覆盖）
[OK]   i2.hentaifox.com                          OK/ERR      200
[OK]   imhentai.com                              OK/OK       200   Redirecting...
[OK]   imhentai.to                               OK/OK       200   IMHentai - Hentai Manga, Doujinshi &amp; Porn Comics
[OK]   inkr.com                                  OK/OK       301   Read The Latest Manga, Manhua, Webtoon and Comics on INKR!
[OK]   kmanga.kodansha.com                       OK/OK       200   K MANGA - You can read the latest chapter on the Kodansha official comic site for free!
[OK]   kodansha.us                               OK/OK       200   Kodansha &#8211; Manga &amp; Books &#8211; Discover Kodansha
[OK]   mangabats.com                             OK/OK       301   Mangabat - Read Manga Online Free
[OK]   mangabuddy.com                            OK/OK       301   COMIZY.io — Read Comics &amp; Manga Online Free, New Chapters Daily
[OK]   mangadex.org                              OK/OK       200   MangaDex
[OK]   mangafire.to                              OK/OK       200   MangaFire - Read Manga Online Free
[OK]   mangago.me                                OK/OK       200   Read Manga Online For Free - Mangago
[OK]   mangahere.cc                              OK/OK       301   Manga Here - Read English Manga Free Online. Manga is Here!
[OK]   mangahub.io                               OK/OK       200   MangaHub.io - Read Manga Online for free - MangaHub
[OK]   mangak.io                                 OK/OK       200   MangaK.io — Read Manga Online Free | Manhwa &amp; Manhua
[受限] mangakakalot.com                          OK/OK       403   This site is closed.
[OK]   mangakakalot.gg                           OK/OK       301   MangaKakalot | Mangakakalot.com | Read Manga Online Free Update Daily
[OK]   mangakakalove.com                         OK/OK       301   MangaKakalot.Com - MangaKakalot | Read Manga Online Free Update Daily
[OK]   mangakatana.com                           OK/OK       200   MangaKatana - Read Manga Online
[受限] manganato.com                             OK/OK       403   This site is closed.
[OK]   manganato.gg                              OK/OK       301   MangaNato - MangaNato.Com | Read Free Manga & Manhwa Online
[OK]   manganel.me                               OK/OK       200   MangaNel.me - Read Manga Online for free - MangaNel
[受限] manganelo.com                             OK/OK       403   This site is closed.
[OK]   mangaowl.io                               OK/OK       200   Mangaowl Official Website- #1 Website To Read Manga Free
[OK]   mangaowl.net                              OK/OK       200   Redirecting...
[无解析]mangaowl.one                              NX/NX       000
[OK]   mangaowl.to                               OK/OK       302   mangaowl.to
[OK]   mangapark.io                              OK/OK       200   Redirecting...
[OK]   mangapark.me                              OK/OK       302   Redirecting...
[OK]   mangapark.net                             OK/OK       302   Redirecting...
[OK]   mangapark.one                             OK/OK       200   MangaPark – Manga Websites & Manhwa Comics
[OK]   mangapark.org                             OK/OK       302   Redirecting...
[OK]   mangapill.com                             OK/OK       200   Mangapill - Your Daily Dose of Manga
[OK]   mangaread.org                             OK/OK       301   Read online - manga, manhwa, manhua catalog №1
[OK]   mangareader.site                          OK/OK       200   MangaReader.site - Read Manga Online for free - MangaReader
[OK]   mangareader.to                            OK/OK       h301
[OK]   mangatoto.net                             OK/OK       301   HQTOTO805 | Portal Informasi Slot Online dan Akses Toto Togel Terbaru
[OK]   mangatown.com                             OK/OK       301   Affiliates on MangaTown.com. Read Free Manga Online at MangaTown.com
[OK]   mangaupdates.com                          OK/OK       301   429 Too Many Requests
[受限] manhuaus.com                              OK/OK       403   Just a moment...
[受限] media.comikey.com                         OK/OK       403   403 Forbidden
[OK]   natomanga.com                             OK/OK       301   MangaNato | MangaNato.Com - The Best Manga Free Websites
[OK]   nelomanga.net                             OK/OK       301   MangaNelo | NeloManga - Read Manga Online Free
[OK]   omoi.com                                  OK/OK       301   Omoi – Read officially licensed digital manga with a monthly subscription app
[超时] readtoto.com                              S2/S2       000
[超时] shop.webtoon.com                          OK/OK       429
[OK]   status.mangadex.org                       OK/OK       200   MangaDex Status
[OK]   uploads.mangadex.org                      OK/OK       200   MangaDex
[受限] vatoto.com                                OK/OK       403   Just a moment...
[OK]   viz.com                                   OK/OK       301   VIZ | The Best in Manga, Anime &amp; Global Entertainment
[OK]   webtoon.com                               OK/OK       301   WEBTOON - Read Comics, Manga &amp; Manhwa
[OK]   webtoons-static.pstatic.net               OK/OK       200
[OK]   weebcentral.com                           OK/OK       200   Weeb Central
[OK]   www.azuki.co                              OK/OK       302   Omoi – Read officially licensed digital manga with a monthly subscription app
[受限] www.fakku.net                             OK/OK       451
[OK]   www.mangabats.com                         OK/OK       200   Mangabat - Read Manga Online Free
[OK]   www.mangahere.cc                          OK/OK       200   Manga Here - Read English Manga Free Online. Manga is Here!
[OK]   www.mangaread.org                         OK/OK       200   Read online - manga, manhwa, manhua catalog №1
[OK]   www.mangatown.com                         OK/OK       200   Affiliates on MangaTown.com. Read Free Manga Online at MangaTown.com
[超时] www.mangaupdates.com                      OK/OK       429
[OK]   www.omoi.com                              OK/OK       200   Omoi – Read officially licensed digital manga with a monthly subscription app
[OK]   www.simply-hentai.com                     OK/OK       308   Free Hentai Manga, Doujins, XXX &amp; Anime Porn - Simply Hentai
[OK]   www.viz.com                               OK/OK       200   VIZ | The Best in Manga, Anime &amp; Global Entertainment
[OK]   xlecx.one                                 OK/OK       200   Porn comics free online

### 成人/本子（99）
[超时] 3hentai.net                               OK/OK       000
[受限] a1.gold-usergeneratedcontent.net          OK/OK       404
[受限] a2.gold-usergeneratedcontent.net          OK/OK       404
[受限] ah-img.luscious.net                       OK/OK       401
[OK]   alt.hentaiverse.org                       OK/OK       302   The HentaiVerse
[OK]   api-v3.simply-hentai.com                  OK/OK       308   Free Hentai Manga, Doujins, XXX &amp; Anime Porn - Simply Hentai
[受限] api.e-hentai.org                          OK/OK       404
[无解析]api.nhentai.net                           OK/NX       000     ← 复测 CF/Google 均 NXDOMAIN；nhentai API 实际走 nhentai.net/api/v2，此为非官方域
[OK]   asmhentai.com                             OK/OK       200   AsmHentai - Free Hentai Manga and Doujinshi Reader
[受限] avatars-cdn.luscious.net                  OK/OK       404
[OK]   blog.irodoricomics.com                    OK/OK       200   Home &#187; Irodori Comics
[受限] cdn.myhentaicomics.com                    OK/OK       403   403 Forbidden
[OK]   cosplaytale.com                           OK/OK       302   Loading...
[OK]   e-hentai.org                              OK/OK       200   E-Hentai Galleries - The Free Hentai Doujinshi, Manga and Image Gallery System
[受限] ehgt.org                                  OK/OK       403   403 Forbidden
[OK]   ehtracker.org                             OK/OK       301   EHTracker Torrents - E-Hentai Galleries
[OK]   ehwiki.org                                OK/OK       301   EHWiki
[OK]   exhentai.org                              OK/OK       302
[OK]   fakku.cc                                  OK/OK       h302
[OK]   fakku.net                                 OK/OK       301   FAKKU - Hentai
[受限] fakkuonion.airdns.org                     OK/OK       000     ← Tor 洋葱入口（端口 4096），不适用于 Clash 分流，不入规则
[受限] forums.e-hentai.org                       OK/OK       403   Just a moment...
[OK]   gold-usergeneratedcontent.net             NO_A/NO_A   000     ← hitomi 图床基域：apex 无 A 记录属正常，实际用哈希子域（a1./w1./ltn. 等），按后缀收录
[OK]   hath.network                              OK/OK       h200
[OK]   hbrowse.com                               OK/OK       200
[受限] hentai-cosplay-xxx.com                    OK/OK       403   Just a moment...
[OK]   hentai-img-xxx.com                        OK/OK       301   Just a moment...
[受限] hentai-img.com                            OK/OK       403   Just a moment...
[OK]   hentai.cafe                               OK/OK       200   Redirecting...
[OK]   hentai2read.com                           OK/OK       200   Hentai2Read - Free Online Manga, Hentai, Doujinshi Reader
[OK]   hentai2w.com                              OK/OK       200   Hentai2W - Free Online Hentai Anime, JAV and Adult Porn Streaming
[OK]   hentaiathome.net                          OK/OK       h301
[OK]   hentaicdn.com                             OK/OK       200   HentaiCDN
[OK]   hentaienvy.com                            OK/OK       200   HentaiEnvy - Hentai Manga, Comic Porn &amp; Doujinshi
[OK]   hentaiera.com                             OK/OK       200   HentaiEra - Hentai Manga, Doujinshi & Comic Porn
[OK]   hentaifox.com                             OK/OK       200   HentaiFox - Free Hentai Manga, Doujinshi and Anime Porn
[OK]   hentaifox.tv                              OK/OK       200   Hentai Anime Video Streaming in HD 1080p, 720p | HentaiFox
[OK]   hentaihere.com                            OK/OK       200   HentaiHere - Read Free Hentai Manga and Doujinshi in English
[OK]   hentairox.com                             OK/OK       200   HentaiRox - Free Hentai Manga, Doujinshi and Comic Porn
[OK]   hentaiverse.org                           OK/OK       302   The HentaiVerse
[OK]   hentaiyes.com                             OK/OK       200   Hentai Anime Porn Videos in HD 1080p, 720p | HentaiYes
[OK]   hentaizap.com                             OK/OK       200   HentaiZap - Free Doujin, Hentai Manga &amp; Comic Porn
[OK]   hentalk.pw                                OK/OK       200   ꓘ🧅K
[受限] hermes.hentai.direct                      OK/OK       404
[OK]   hitomi.la                                 OK/OK       200   | Hitomi.la
[OK]   i.nhentai.net                             OK/OK       h301
[OK]   i1.nhentai.net                            OK/OK       h301
[OK]   i2.nhentai.net                            OK/OK       h301
[OK]   i3.hentaifox.com                          OK/OK       200
[OK]   i3.nhentai.net                            OK/OK       h301
[OK]   i4.nhentai.net                            OK/OK       h301
[受限] images.asmhentai.com                      OK/OK       403   403 Forbidden
[受限] images.sh-cdn.com                         OK/OK       404
[OK]   img1.hentaicdn.com                        OK/OK       200   HentaiCDN
[OK]   img2.hentaicdn.com                        OK/OK       200   HentaiCDN
[OK]   img3.hentaicdn.com                        OK/OK       200   HentaiCDN
[OK]   imhentai.xxx                              OK/OK       200   IMHentai - Hentai Manga, Doujinshi & Porn Comics
[OK]   irodoricomics.com                         OK/OK       302   Access Blocked – Irodori Comics
[受限] ltn.gold-usergeneratedcontent.net         OK/OK       404
[受限] luscious.net                              OK/OK       403   Just a moment...
[受限] m11.imhentai.xxx                          OK/OK       404
[受限] master.hitomi.la                          OK/OK       404
[受限] members.luscious.net                      OK/OK       403   Just a moment...
[OK]   multporn.net                              OK/OK       200   Porn Comics, Hentai Manga, Porn Videos - Multporn
[OK]   myhentaicomics.com                        OK/OK       200   MyHentaiComics - Hentai Comics | Porn Comics
[OK]   myhentaigallery.com                       OK/OK       200   MyHentaiGallery - Hentai Comics | Porn Comics Page 1!
[OK]   mymangagallery.com                        OK/OK       200   MyMangaGallery - Hentai Manga | Porn Manga Page 1!
[OK]   newsletter.irodoricomics.com              OK/OK       302   Login - IRODORI, Inc.
[OK]   nhentai.com                               OK/OK       301   nHentai: Free Hentai Manga, Doujinshi and Comics Online!
[OK]   nhentai.net                               OK/OK       200   nhentai: hentai doujinshi and manga
[OK]   nhentai.to                                OK/OK       200   nhentai : Free Hentai Manga, Doujinshi and Comics Online!
[OK]   nhentai.xxx                               OK/OK       200   nhentai - Hentai Manga & Doujinshi
[OK]   pixiv.net                                 OK/OK       301   イラスト・マンガ・小説 作品コミュニケーションサービス [pixiv(ピクシブ)]
[OK]   porn-image.com                            OK/OK       200
[超时] pururin.com                               NO_A/NO_A   000
[超时] pururin.io                                S2/S2       000
[OK]   pururin.us                                OK/OK       200   Redirecting...
[OK]   pximg.net                                 OK/OK       200   pximg.net
[OK]   repo.e-hentai.org                         OK/OK       301   E-Hentai Galleries - The Free Hentai Doujinshi, Manga and Image Gallery System
[OK]   rpc.hentaiathome.net                      OK/OK       h301
[受限] s.exhentai.org                            OK/OK       403   403 Forbidden
[OK]   sakura-r18.irodoricomics.com              OK/OK       301   Access Blocked – Irodori Comics
[OK]   script.hentaicdn.com                      OK/OK       200   HentaiCDN
[OK]   simply-hentai.com                         OK/OK       301   Free Hentai Manga, Doujins, XXX &amp; Anime Porn - Simply Hentai
[受限] static.luscious.net                       OK/OK       h403
[OK]   t.nhentai.net                             OK/OK       h301
[OK]   t1.nhentai.net                            OK/OK       h301
[OK]   t2.nhentai.net                            OK/OK       h301
[OK]   t3.nhentai.net                            OK/OK       h301
[OK]   t4.nhentai.net                            OK/OK       h301
[OK]   thehentaiworld.com                        OK/OK       200   The Hentai World - Huge variety of hentai porn.
[受限] tmohentai.app                             OK/OK       403   Access denied | tmohentai.app used Cloudflare to restrict access | tmohentai.app | Cloudfl
[超时] tmohentai.com                             NO_A/NO_A   000
[OK]   tsumino.com                               OK/OK       200   Tsumino Shutdown
[OK]   upload.e-hentai.org                       OK/OK       301   E-Hentai Galleries - The Free Hentai Doujinshi, Manga and Image Gallery System
[受限] w1.gold-usergeneratedcontent.net          OK/OK       404
[受限] w2.gold-usergeneratedcontent.net          OK/OK       404
[受限] www.luscious.net                          OK/OK       403   Just a moment...
[OK]   xml.e-hentai.org                          OK/OK       301   E-Hentai Galleries - The Free Hentai Doujinshi, Manga and Image Gallery System

```

## 8. 已失效 / 勿收录域名汇总

下表汇总各节标注「已失效 / 停放 / 勿收录」的域名，以及在实测中**双解析器均无解析**的域名。**这些不要写进分流规则**；已收录的要清理。

| 域名 | 状态与备注 |
|---|---|
| 18comic.company | 复测：AliDNS 返回疑似污染 IP（108.160 段），CF/Google 均 NXDOMAIN，实测不可达 |
| api.nhentai.net | 复测 CF/Google 均 NXDOMAIN；nhentai API 实际走 nhentai.net/api/v2，此为非官方域 |
| app.buka.cn | 实测连接失败（域名疑似已废弃） |
| bato.ing | 实测仍可访问（HTTP 302），若为接管/停放页请勿收录 |
| bato.si | 实测仍可访问（HTTP 302），若为接管/停放页请勿收录 |
| bato.to | 实测仍可访问（HTTP 302），若为接管/停放页请勿收录 |
| batotwo.com | 实测仍可访问（HTTP 302），若为接管/停放页请勿收录 |
| battwo.com | 实测仍可访问（HTTP 302），若为接管/停放页请勿收录 |
| boylove.live | 复测：AliDNS 返回疑似污染 IP（128.242 段），CF/Google 均 NXDOMAIN，实测不可达 |
| buka.cn | 实测连接失败（域名疑似已废弃） |
| cdnxxx-proxy.co | 实测无解析（NXDOMAIN） |
| cdnxxx-proxy.xyz | 实测无解析（NXDOMAIN） |
| comic.nicovideo.jp | 域名已停用：复测 CF/Google 均 NXDOMAIN；官方漫画入口现为 nicomanga.com |
| comiko.net | 实测仍可访问（HTTP 200），若为接管/停放页请勿收录 |
| copymanga.app | 实测仍可访问（HTTP 302），若为接管/停放页请勿收录 |
| copymanga.co | 实测仍可访问（HTTP 200），若为接管/停放页请勿收录 |
| copymanga.com | 实测连接失败（域名疑似已废弃） |
| copymanga.info | 实测仍可访问（HTTP 302），若为接管/停放页请勿收录 |
| copymanga.me | 实测无解析（NXDOMAIN） |
| copymanga.org | 实测仍可访问（HTTP h200），若为接管/停放页请勿收录 |
| copymanga.tv | 实测连接失败（域名疑似已废弃） |
| dmzj.com | 实测仍可访问（HTTP h302），若为接管/停放页请勿收录 |
| gufengmh.com | 实测无解析（NXDOMAIN） |
| happymh.com | 实测连接失败（域名疑似已废弃） |
| hhcomic.com | 实测仍可访问（HTTP 200），若为接管/停放页请勿收录 |
| ibuka.cn | 实测 HTTP h403（疑似停放/空壳，需人工复核） |
| idmzj.com | 实测仍可访问（HTTP h302），若为接管/停放页请勿收录 |
| jmapinode1.top | 实测无解析（NXDOMAIN） |
| jmapinode2.top | 实测无解析（NXDOMAIN） |
| jmapinode3.top | 实测无解析（NXDOMAIN） |
| jmapiproxy4.cc | 实测无解析（NXDOMAIN） |
| jmapiproxyxxx.vip | 实测无解析（NXDOMAIN） |
| jmcomic.group | 复测：AliDNS 返回疑似污染 IP，CF/Google 均 NXDOMAIN，实测不可达 |
| jmcomic1.city | 复测：AliDNS 返回疑似污染 IP，CF/Google 均 NXDOMAIN，实测不可达 |
| joa-vip.com | 复测三方均 SERVFAIL，疑似再次换域（原公告见 뉴토끼监控频道） |
| m.manhuatai.com | 实测仍可访问（HTTP h301），若为接管/停放页请勿收录 |
| manga109.com | 实测无解析（NXDOMAIN） |
| mangakakalot.com | 实测 HTTP 403（疑似停放/空壳，需人工复核） |
| manganato.com | 实测 HTTP 403（疑似停放/空壳，需人工复核） |
| manganelo.com | 实测 HTTP 403（疑似停放/空壳，需人工复核） |
| mangaowl.io | 实测仍可访问（HTTP 200），若为接管/停放页请勿收录 |
| mangaowl.net | 实测仍可访问（HTTP 200），若为接管/停放页请勿收录 |
| mangaowl.one | 实测无解析（NXDOMAIN） |
| mangaowl.to | 实测仍可访问（HTTP 302），若为接管/停放页请勿收录 |
| mangapark.io | 实测仍可访问（HTTP 200），若为接管/停放页请勿收录 |
| mangapark.me | 实测仍可访问（HTTP 302），若为接管/停放页请勿收录 |
| mangapark.net | 实测仍可访问（HTTP 302），若为接管/停放页请勿收录 |
| mangapark.one | 实测仍可访问（HTTP 200），若为接管/停放页请勿收录 |
| mangapark.org | 实测仍可访问（HTTP 302），若为接管/停放页请勿收录 |
| mangareader.to | 实测仍可访问（HTTP h301），若为接管/停放页请勿收录 |
| mangatoto.net | 实测仍可访问（HTTP 301），若为接管/停放页请勿收录 |
| manhua.163.com | 实测仍可访问（HTTP 302），若为接管/停放页请勿收录 |
| manhuatai.com | 实测仍可访问（HTTP h200），若为接管/停放页请勿收录 |
| raw-free.com | 实测无解析（NXDOMAIN） |
| rawload.net | 实测无解析（NXDOMAIN） |
| readtoto.com | 实测连接失败（域名疑似已废弃） |
| u17.com | 实测连接失败（域名疑似已废弃） |
| vatoto.com | 实测 HTTP 403（疑似停放/空壳，需人工复核） |
| www.buka.cn | 实测连接失败（域名疑似已废弃） |
| www.dlsitestudio.com | 复测三方均 NXDOMAIN，域名不存在（DLsite 创作端走 dlsite.com，勿收） |
| www.dmzj.com | 实测无解析（NXDOMAIN） |
| www.gufengmh.com | 实测无解析（NXDOMAIN） |
| www.happymh.com | 实测连接失败（域名疑似已废弃） |
| www.hhcomic.com | 实测仍可访问（HTTP 200），若为接管/停放页请勿收录 |
| www.manhuatai.com | 实测仍可访问（HTTP h200），若为接管/停放页请勿收录 |
| www.u17.com | 实测仍可访问（HTTP h301），若为接管/停放页请勿收录 |

另外这些是**误导域名**（真实对应关系见正文）：`cmo.jp`（日本博彩站，非コミックシーモア，正确是 `www.cmoa.jp`）、`renta.com`（欧洲建筑设备租赁公司，非日本 Renta!，正确是 `renta.papy.co.jp`）、`anytoon.com`（域名待售，真站是 `anytoon.co.kr`）。

## 9. 附录：可直接使用的规则清单

以下清单由本文全部域名自动生成（已剔除失效域名，并把能被子域覆盖的条目合并）：**国内直连 31 条、海外代理 429 条**。按需复制到 mihomo 的 `rule-providers`（payload/classical 均适用）。

### 9.1 国内（建议直连）

```yaml
DOMAIN-SUFFIX,321mh.com
DOMAIN-SUFFIX,ac.qq.com
DOMAIN-SUFFIX,baozicomic.cc
DOMAIN-SUFFIX,baozimh.com
DOMAIN-SUFFIX,bzmgcn.com
DOMAIN-SUFFIX,copy4000.com
DOMAIN-SUFFIX,copymanga.site
DOMAIN-SUFFIX,dongmanmanhua.cn
DOMAIN-SUFFIX,fanqienovel.com
DOMAIN-SUFFIX,i.hamreus.com
DOMAIN-SUFFIX,i0.hdslb.com
DOMAIN-SUFFIX,kanman.com
DOMAIN-SUFFIX,kkmh.com
DOMAIN-SUFFIX,kuaikanmanhua.com
DOMAIN-SUFFIX,manga.bilibili.com
DOMAIN-SUFFIX,manga.hdslb.com
DOMAIN-SUFFIX,manga2026.xyz
DOMAIN-SUFFIX,mangacopy.com
DOMAIN-SUFFIX,mangafunb.fun
DOMAIN-SUFFIX,manhua.acimg.cn
DOMAIN-SUFFIX,manhuadb.com
DOMAIN-SUFFIX,manhuagui.com
DOMAIN-SUFFIX,mhgui.com
DOMAIN-SUFFIX,mhxk.com
DOMAIN-SUFFIX,qimao.com
DOMAIN-SUFFIX,s1.hdslb.com
DOMAIN-SUFFIX,samanlehua.com
DOMAIN-SUFFIX,short.tiankongshuyu.cn
DOMAIN-SUFFIX,wtzw.com
DOMAIN-SUFFIX,www.ibuka.cn
DOMAIN-SUFFIX,yqmh.com
```

### 9.2 海外（建议代理）

```yaml
DOMAIN-SUFFIX,11toon.com
DOMAIN-SUFFIX,11toon1.com
DOMAIN-SUFFIX,11toon149.com
DOMAIN-SUFFIX,13dl.net
DOMAIN-SUFFIX,18comic-god.cc
DOMAIN-SUFFIX,18comic-god.club
DOMAIN-SUFFIX,18comic-god.xyz
DOMAIN-SUFFIX,18comic.cc
DOMAIN-SUFFIX,18comic.org
DOMAIN-SUFFIX,18comic.vip
DOMAIN-SUFFIX,18porncomic.com
DOMAIN-SUFFIX,1kkk.com
DOMAIN-SUFFIX,2025copy.com
DOMAIN-SUFFIX,3hentai.net
DOMAIN-SUFFIX,678dl.net
DOMAIN-SUFFIX,a-zmanga.net
DOMAIN-SUFFIX,allporncomic.com
DOMAIN-SUFFIX,amazon.co.jp
DOMAIN-SUFFIX,anytoon.co.kr
DOMAIN-SUFFIX,api.comico.jp
DOMAIN-SUFFIX,api.nicomanga.jp
DOMAIN-SUFFIX,api.zebrack-comic.com
DOMAIN-SUFFIX,asacomi.jp
DOMAIN-SUFFIX,asjmapihost.cc
DOMAIN-SUFFIX,asmhentai.com
DOMAIN-SUFFIX,azuki.co
DOMAIN-SUFFIX,bato1.com
DOMAIN-SUFFIX,bibibi-comic.com
DOMAIN-SUFFIX,bigcomics.jp
DOMAIN-SUFFIX,blacktoon.me
DOMAIN-SUFFIX,blacktoon423.com
DOMAIN-SUFFIX,blacktoonurl.net
DOMAIN-SUFFIX,bomtoon.com
DOMAIN-SUFFIX,bomtoon.tw
DOMAIN-SUFFIX,booklive.jp
DOMAIN-SUFFIX,bookto31.com
DOMAIN-SUFFIX,bookwalker.com
DOMAIN-SUFFIX,bookwalker.jp
DOMAIN-SUFFIX,booth.pm
DOMAIN-SUFFIX,boylove.cc
DOMAIN-SUFFIX,boylove1.cc
DOMAIN-SUFFIX,boyloves.cc
DOMAIN-SUFFIX,cdn.megadata.co.kr
DOMAIN-SUFFIX,cdnblackmyth.club
DOMAIN-SUFFIX,cdndm5.com
DOMAIN-SUFFIX,cdnmhwscc.vip
DOMAIN-SUFFIX,cdnuc.vip
DOMAIN-SUFFIX,championcross.jp
DOMAIN-SUFFIX,ciao.shogakukan.co.jp
DOMAIN-SUFFIX,cmo.jp
DOMAIN-SUFFIX,cmoa.jp
DOMAIN-SUFFIX,comic-action.com
DOMAIN-SUFFIX,comic-boost.com
DOMAIN-SUFFIX,comic-clear.jp
DOMAIN-SUFFIX,comic-days.com
DOMAIN-SUFFIX,comic-earthstar.com
DOMAIN-SUFFIX,comic-fuz.com
DOMAIN-SUFFIX,comic-gardo.com
DOMAIN-SUFFIX,comic-growl.com
DOMAIN-SUFFIX,comic-meteor.jp
DOMAIN-SUFFIX,comic-ogyaaa.com
DOMAIN-SUFFIX,comic-room-base.com
DOMAIN-SUFFIX,comic-ryu.jp
DOMAIN-SUFFIX,comic-seasons.com
DOMAIN-SUFFIX,comic-trail.com
DOMAIN-SUFFIX,comic-walker.com
DOMAIN-SUFFIX,comic-y-ours.com
DOMAIN-SUFFIX,comic-zenon.com
DOMAIN-SUFFIX,comic.iowl.jp
DOMAIN-SUFFIX,comic.j-nbooks.jp
DOMAIN-SUFFIX,comic.naver.com
DOMAIN-SUFFIX,comicborder.com
DOMAIN-SUFFIX,comicnettai.com
DOMAIN-SUFFIX,comicpash.jp
DOMAIN-SUFFIX,comicride.jp
DOMAIN-SUFFIX,comics.8muses.com
DOMAIN-SUFFIX,comics.manga-bang.com
DOMAIN-SUFFIX,comicthumb-phinf.pstatic.net
DOMAIN-SUFFIX,comikey.com
DOMAIN-SUFFIX,comirela.com
DOMAIN-SUFFIX,comix.to
DOMAIN-SUFFIX,comix.ws
DOMAIN-SUFFIX,comizy.io
DOMAIN-SUFFIX,cookmana56.com
DOMAIN-SUFFIX,copy-manga.com
DOMAIN-SUFFIX,copy20.com
DOMAIN-SUFFIX,copy2000.online
DOMAIN-SUFFIX,cosplaytale.com
DOMAIN-SUFFIX,cycomi.com
DOMAIN-SUFFIX,daycomics.com
DOMAIN-SUFFIX,dbook.docomo.ne.jp
DOMAIN-SUFFIX,dl-zip.com
DOMAIN-SUFFIX,dlaf.jp
DOMAIN-SUFFIX,dlraw.net
DOMAIN-SUFFIX,dlraw.tv
DOMAIN-SUFFIX,dlsite.com
DOMAIN-SUFFIX,dm5.cn
DOMAIN-SUFFIX,dm5.com
DOMAIN-SUFFIX,dm9.com
DOMAIN-SUFFIX,dmm.co.jp
DOMAIN-SUFFIX,dmm.com
DOMAIN-SUFFIX,dn-img-page.kakao.com
DOMAIN-SUFFIX,dokiraw.click
DOMAIN-SUFFIX,dokiraw.link
DOMAIN-SUFFIX,dokusho-ojikan.jp
DOMAIN-SUFFIX,doujins.com
DOMAIN-SUFFIX,drecomi-plus.jp
DOMAIN-SUFFIX,drm.cdn.nicomanga.jp
DOMAIN-SUFFIX,dynasty-scans.com
DOMAIN-SUFFIX,e-hentai.org
DOMAIN-SUFFIX,ebookjapan.yahoo.co.jp
DOMAIN-SUFFIX,ebookstore.sony.jp
DOMAIN-SUFFIX,ehgt.org
DOMAIN-SUFFIX,ehtracker.org
DOMAIN-SUFFIX,ehwiki.org
DOMAIN-SUFFIX,exhentai.org
DOMAIN-SUFFIX,fakku.cc
DOMAIN-SUFFIX,fakku.net
DOMAIN-SUFFIX,fanbox.cc
DOMAIN-SUFFIX,fanfox.net
DOMAIN-SUFFIX,fantia.jp
DOMAIN-SUFFIX,feelweb.jp
DOMAIN-SUFFIX,firecross.jp
DOMAIN-SUFFIX,flowercomics.jp
DOMAIN-SUFFIX,fuhouse.club
DOMAIN-SUFFIX,g-comi.jp
DOMAIN-SUFFIX,ganma.jp
DOMAIN-SUFFIX,gaugau.futabanet.jp
DOMAIN-SUFFIX,gmanhua.com
DOMAIN-SUFFIX,gold-usergeneratedcontent.net
DOMAIN-SUFFIX,gorakuweb.com
DOMAIN-SUFFIX,hachiraw.net
DOMAIN-SUFFIX,hachiraw.win
DOMAIN-SUFFIX,haitangbook.com
DOMAIN-SUFFIX,haitbook.com
DOMAIN-SUFFIX,hanayume.com
DOMAIN-SUFFIX,hath.network
DOMAIN-SUFFIX,hayacomic.jp
DOMAIN-SUFFIX,hbrowse.com
DOMAIN-SUFFIX,hentai-cosplay-xxx.com
DOMAIN-SUFFIX,hentai-img-xxx.com
DOMAIN-SUFFIX,hentai-img.com
DOMAIN-SUFFIX,hentai.cafe
DOMAIN-SUFFIX,hentai2read.com
DOMAIN-SUFFIX,hentai2w.com
DOMAIN-SUFFIX,hentaiathome.net
DOMAIN-SUFFIX,hentaicdn.com
DOMAIN-SUFFIX,hentaienvy.com
DOMAIN-SUFFIX,hentaiera.com
DOMAIN-SUFFIX,hentaifox.com
DOMAIN-SUFFIX,hentaifox.tv
DOMAIN-SUFFIX,hentaigold.net
DOMAIN-SUFFIX,hentaihere.com
DOMAIN-SUFFIX,hentainexus.com
DOMAIN-SUFFIX,hentairead.com
DOMAIN-SUFFIX,hentairox.com
DOMAIN-SUFFIX,hentaiverse.org
DOMAIN-SUFFIX,hentaiyes.com
DOMAIN-SUFFIX,hentaizap.com
DOMAIN-SUFFIX,hentalk.pw
DOMAIN-SUFFIX,hermes.hentai.direct
DOMAIN-SUFFIX,heros-web.com
DOMAIN-SUFFIX,hitomi.la
DOMAIN-SUFFIX,hkmanga.com
DOMAIN-SUFFIX,honto.jp
DOMAIN-SUFFIX,htlvbooks.com
DOMAIN-SUFFIX,htnewbooks.com
DOMAIN-SUFFIX,htwhbook.com
DOMAIN-SUFFIX,ichicomi.com
DOMAIN-SUFFIX,idol.gravureprincess.date
DOMAIN-SUFFIX,image-comic.pstatic.net
DOMAIN-SUFFIX,image.balcony.studio
DOMAIN-SUFFIX,images.sh-cdn.com
DOMAIN-SUFFIX,img.dlsite.jp
DOMAIN-SUFFIX,img.ridicdn.net
DOMAIN-SUFFIX,imhentai.com
DOMAIN-SUFFIX,imhentai.to
DOMAIN-SUFFIX,imhentai.xxx
DOMAIN-SUFFIX,inkr.com
DOMAIN-SUFFIX,irodoricomics.com
DOMAIN-SUFFIX,jm-comic2.cc
DOMAIN-SUFFIX,jm18c-bbm.cc
DOMAIN-SUFFIX,jm18c-bbm.net
DOMAIN-SUFFIX,jm18c-uoi.net
DOMAIN-SUFFIX,jm365.work
DOMAIN-SUFFIX,jm365.xyz
DOMAIN-SUFFIX,jmanga.cyou
DOMAIN-SUFFIX,jmanga.media
DOMAIN-SUFFIX,jmapibranch1.cc
DOMAIN-SUFFIX,jmapibranch2.cc
DOMAIN-SUFFIX,jmapibranch3.cc
DOMAIN-SUFFIX,jmapinode.biz
DOMAIN-SUFFIX,jmapinode.vip
DOMAIN-SUFFIX,jmapinode.xyz
DOMAIN-SUFFIX,jmapinodeudzn.net
DOMAIN-SUFFIX,jmapinodeudzn.xyz
DOMAIN-SUFFIX,jmapiproxy1.monster
DOMAIN-SUFFIX,jmapiproxy2.cc
DOMAIN-SUFFIX,jmcomic-fb.vip
DOMAIN-SUFFIX,jmcomic-zzz.one
DOMAIN-SUFFIX,jmcomic-zzz.org
DOMAIN-SUFFIX,jmcomic.ltd
DOMAIN-SUFFIX,jmcomic.me
DOMAIN-SUFFIX,jmcomic.mobi
DOMAIN-SUFFIX,jmcomic.moe
DOMAIN-SUFFIX,jmcomic.rocks
DOMAIN-SUFFIX,jmcomic1.me
DOMAIN-SUFFIX,jmcomic1.mobi
DOMAIN-SUFFIX,jmcomic1.rocks
DOMAIN-SUFFIX,jmcomic2.moe
DOMAIN-SUFFIX,jp.kobo.com
DOMAIN-SUFFIX,jpddl.com
DOMAIN-SUFFIX,jraws.net
DOMAIN-SUFFIX,jumpg-webapi.tokyo-cdn.com
DOMAIN-SUFFIX,jumptoon.com
DOMAIN-SUFFIX,k-manga.jp
DOMAIN-SUFFIX,kakaowebtoon.com
DOMAIN-SUFFIX,kansai.mag-garden.co.jp
DOMAIN-SUFFIX,kimicomi.com
DOMAIN-SUFFIX,kirapo.jp
DOMAIN-SUFFIX,klraw.info
DOMAIN-SUFFIX,klto9.com
DOMAIN-SUFFIX,klz9.com
DOMAIN-SUFFIX,kmana10.net
DOMAIN-SUFFIX,kmanga.kodansha.com
DOMAIN-SUFFIX,kmansin09.top
DOMAIN-SUFFIX,kodansha.us
DOMAIN-SUFFIX,kr-a.kakaopagecdn.com
DOMAIN-SUFFIX,kumaraw.com
DOMAIN-SUFFIX,kuragebunch.com
DOMAIN-SUFFIX,lezhin.com
DOMAIN-SUFFIX,lezhin.jp
DOMAIN-SUFFIX,linkbbg8.com
DOMAIN-SUFFIX,lmbooks.com
DOMAIN-SUFFIX,lmebooks.com
DOMAIN-SUFFIX,longmabook.com
DOMAIN-SUFFIX,longmabookcn.com
DOMAIN-SUFFIX,love4u.net
DOMAIN-SUFFIX,lovehtbooks.com
DOMAIN-SUFFIX,luscious.net
DOMAIN-SUFFIX,lvhtebook.com
DOMAIN-SUFFIX,manatoki555.net
DOMAIN-SUFFIX,manben.com
DOMAIN-SUFFIX,manbenapi.com
DOMAIN-SUFFIX,manga-5.com
DOMAIN-SUFFIX,manga-mee.jp
DOMAIN-SUFFIX,manga-meets.jp
DOMAIN-SUFFIX,manga-no.com
DOMAIN-SUFFIX,manga-one.com
DOMAIN-SUFFIX,manga-park.com
DOMAIN-SUFFIX,manga-raw.club
DOMAIN-SUFFIX,manga-zegra.com
DOMAIN-SUFFIX,manga-zip.app
DOMAIN-SUFFIX,manga-zip.is
DOMAIN-SUFFIX,manga-zip.my
DOMAIN-SUFFIX,manga.fod.fujitv.co.jp
DOMAIN-SUFFIX,mangabats.com
DOMAIN-SUFFIX,mangabu.jp
DOMAIN-SUFFIX,mangabuddy.com
DOMAIN-SUFFIX,mangacross.jp
DOMAIN-SUFFIX,mangadex.org
DOMAIN-SUFFIX,mangafire.to
DOMAIN-SUFFIX,mangago.me
DOMAIN-SUFFIX,mangahere.cc
DOMAIN-SUFFIX,mangahub.io
DOMAIN-SUFFIX,mangak.io
DOMAIN-SUFFIX,mangakakalot.gg
DOMAIN-SUFFIX,mangakakalove.com
DOMAIN-SUFFIX,mangakatana.com
DOMAIN-SUFFIX,mangakuro.net
DOMAIN-SUFFIX,mangalt.jp
DOMAIN-SUFFIX,mangamura.me
DOMAIN-SUFFIX,manganato.gg
DOMAIN-SUFFIX,manganel.me
DOMAIN-SUFFIX,mangapill.com
DOMAIN-SUFFIX,mangaplus.shueisha.co.jp
DOMAIN-SUFFIX,mangaraw.best
DOMAIN-SUFFIX,mangaraw.co
DOMAIN-SUFFIX,mangaraw.to
DOMAIN-SUFFIX,mangaraw.xyz
DOMAIN-SUFFIX,mangaread.org
DOMAIN-SUFFIX,mangareader.site
DOMAIN-SUFFIX,mangatime-square.com
DOMAIN-SUFFIX,mangatown.com
DOMAIN-SUFFIX,mangaupdates.com
DOMAIN-SUFFIX,manhuaren.com
DOMAIN-SUFFIX,manhuaus.com
DOMAIN-SUFFIX,marumaru103.com
DOMAIN-SUFFIX,mato31.com
DOMAIN-SUFFIX,mechacomi.jp
DOMAIN-SUFFIX,mechacomic.jp
DOMAIN-SUFFIX,melonbooks.co.jp
DOMAIN-SUFFIX,mgeko.cc
DOMAIN-SUFFIX,momon-ga.com
DOMAIN-SUFFIX,mrblue.com
DOMAIN-SUFFIX,multporn.net
DOMAIN-SUFFIX,music-book.jp
DOMAIN-SUFFIX,mybookinlm.com
DOMAIN-SUFFIX,myhentaicomics.com
DOMAIN-SUFFIX,myhentaigallery.com
DOMAIN-SUFFIX,myhtebook.com
DOMAIN-SUFFIX,myhtebooks.com
DOMAIN-SUFFIX,myhtlmebook.com
DOMAIN-SUFFIX,mymangagallery.com
DOMAIN-SUFFIX,namicomic.jp
DOMAIN-SUFFIX,natomanga.com
DOMAIN-SUFFIX,naverwebtoon-phinf.pstatic.net
DOMAIN-SUFFIX,nelomanga.net
DOMAIN-SUFFIX,newhtbook.com
DOMAIN-SUFFIX,newto31.com
DOMAIN-SUFFIX,newtoki1.org
DOMAIN-SUFFIX,newxtoon1.com
DOMAIN-SUFFIX,nhentai.com
DOMAIN-SUFFIX,nhentai.net
DOMAIN-SUFFIX,nhentai.to
DOMAIN-SUFFIX,nhentai.xxx
DOMAIN-SUFFIX,nicomanga.com
DOMAIN-SUFFIX,nihonkuni.com
DOMAIN-SUFFIX,nikkangecchan.jp
DOMAIN-SUFFIX,novel.naver.com
DOMAIN-SUFFIX,omoi.com
DOMAIN-SUFFIX,ourfeel.jp
DOMAIN-SUFFIX,page.kakao.com
DOMAIN-SUFFIX,page.kakaocdn.net
DOMAIN-SUFFIX,papy.co.jp
DOMAIN-SUFFIX,pash-up.jp
DOMAIN-SUFFIX,piacomic.jp
DOMAIN-SUFFIX,pixiv.net
DOMAIN-SUFFIX,pocket.shonenmagazine.com
DOMAIN-SUFFIX,porn-image.com
DOMAIN-SUFFIX,prod-contents-br-page.akamaized.net
DOMAIN-SUFFIX,pururin.com
DOMAIN-SUFFIX,pururin.io
DOMAIN-SUFFIX,pururin.us
DOMAIN-SUFFIX,pximg.net
DOMAIN-SUFFIX,r18.mangaz.com
DOMAIN-SUFFIX,raw-zip.com
DOMAIN-SUFFIX,raw.senmanga.com
DOMAIN-SUFFIX,raw1001.net
DOMAIN-SUFFIX,raw18.bar
DOMAIN-SUFFIX,raw18.icu
DOMAIN-SUFFIX,raw77.com
DOMAIN-SUFFIX,rawbaka.com
DOMAIN-SUFFIX,rawbaka.site
DOMAIN-SUFFIX,rawdevart.art
DOMAIN-SUFFIX,rawdevart.com
DOMAIN-SUFFIX,rawdex.net
DOMAIN-SUFFIX,rawhost.net
DOMAIN-SUFFIX,rawinu.com
DOMAIN-SUFFIX,rawkuma.com
DOMAIN-SUFFIX,rawkuma.net
DOMAIN-SUFFIX,rawmanga.xyz
DOMAIN-SUFFIX,rawmiu.com
DOMAIN-SUFFIX,rawotaku.com
DOMAIN-SUFFIX,rawsakura.org
DOMAIN-SUFFIX,rawuwu.net
DOMAIN-SUFFIX,renta.com
DOMAIN-SUFFIX,ridibooks.com
DOMAIN-SUFFIX,rimacomiplus.jp
DOMAIN-SUFFIX,rookie.shonenjump.com
DOMAIN-SUFFIX,sai-zen-sen.jp
DOMAIN-SUFFIX,sbxh9.com
DOMAIN-SUFFIX,seiga.nicovideo.jp
DOMAIN-SUFFIX,series.naver.com
DOMAIN-SUFFIX,shared-comic.pstatic.net
DOMAIN-SUFFIX,shonenjumpplus.com
DOMAIN-SUFFIX,simply-hentai.com
DOMAIN-SUFFIX,sokuyomi.jp
DOMAIN-SUFFIX,sp.manga.nicovideo.jp
DOMAIN-SUFFIX,spotv147.com
DOMAIN-SUFFIX,static.ridicdn.net
DOMAIN-SUFFIX,sunday-webry.com
DOMAIN-SUFFIX,takecomic.jp
DOMAIN-SUFFIX,thehentaiworld.com
DOMAIN-SUFFIX,tkor146.com
DOMAIN-SUFFIX,tmohentai.app
DOMAIN-SUFFIX,tmohentai.com
DOMAIN-SUFFIX,to-corona-ex.com
DOMAIN-SUFFIX,tonarinoyj.jp
DOMAIN-SUFFIX,toomics.com
DOMAIN-SUFFIX,toonily.com
DOMAIN-SUFFIX,toonkor0.org
DOMAIN-SUFFIX,toonkor404.com
DOMAIN-SUFFIX,toptoon.com
DOMAIN-SUFFIX,toptoon.net
DOMAIN-SUFFIX,toptoonplus.com
DOMAIN-SUFFIX,toranoana.jp
DOMAIN-SUFFIX,tsumino.com
DOMAIN-SUFFIX,urasunday.com
DOMAIN-SUFFIX,urhtbooks.com
DOMAIN-SUFFIX,video.unext.jp
DOMAIN-SUFFIX,viz.com
DOMAIN-SUFFIX,webaction.jp
DOMAIN-SUFFIX,webcomic.ohtabooks.com
DOMAIN-SUFFIX,webtoon-phinf.pstatic.net
DOMAIN-SUFFIX,webtoon.com
DOMAIN-SUFFIX,webtoon.kakao.com
DOMAIN-SUFFIX,webtoons-static.pstatic.net
DOMAIN-SUFFIX,webtoons.com
DOMAIN-SUFFIX,weebcentral.com
DOMAIN-SUFFIX,weloma.net
DOMAIN-SUFFIX,wfwf507.com
DOMAIN-SUFFIX,wfwf510.com
DOMAIN-SUFFIX,www.alphapolis.co.jp
DOMAIN-SUFFIX,www.comico.jp
DOMAIN-SUFFIX,www.corocoro.jp
DOMAIN-SUFFIX,www.ganganonline.com
DOMAIN-SUFFIX,www.goodtoon005.com
DOMAIN-SUFFIX,www.goodtoon006.com
DOMAIN-SUFFIX,www.kobo.com
DOMAIN-SUFFIX,www.manga-up.com
DOMAIN-SUFFIX,www.mangaz.com
DOMAIN-SUFFIX,x3-dl.net
DOMAIN-SUFFIX,xlecx.one
DOMAIN-SUFFIX,xn--2s2ba48db550hj3b2ys7xi.com
DOMAIN-SUFFIX,xn--910b43d93g9lo.com
DOMAIN-SUFFIX,xn--h10bt26abuh3me.com
DOMAIN-SUFFIX,xn--h10bt26abuh3me.net
DOMAIN-SUFFIX,xn--hq1bs8p27g.com
DOMAIN-SUFFIX,xn--hq1bt26abyi.com
DOMAIN-SUFFIX,xn--ok0b03z1ndutj89hqne.com
DOMAIN-SUFFIX,yanmaga.jp
DOMAIN-SUFFIX,yawaspi.com
DOMAIN-SUFFIX,ynjn.jp
DOMAIN-SUFFIX,yomonga.com
DOMAIN-SUFFIX,younganimal.com
DOMAIN-SUFFIX,youngchampion.jp
DOMAIN-SUFFIX,zebrack-comic.shueisha.co.jp
DOMAIN-SUFFIX,zerosumonline.com
```

### 9.3 高变动站的 `DOMAIN-KEYWORD` 兜底建议

编号轮换站（`mato31.com`、`newto31.com`、`bookto31.com`、`toonkor###.com`、`wfwf###.com` 等）**换号后关键词也不命中**，只能靠收录「稳定入口域名」+ 定期更新（见 §3 与 §10）。能用关键词兜底的场景：

```yaml
DOMAIN-KEYWORD,copymanga
DOMAIN-KEYWORD,mangacopy
DOMAIN-KEYWORD,copy4000
DOMAIN-KEYWORD,mangafunb
DOMAIN-KEYWORD,18comic
DOMAIN-KEYWORD,jmcomic
DOMAIN-KEYWORD,jmapinode
DOMAIN-KEYWORD,mangaraw
DOMAIN-KEYWORD,rawkuma
DOMAIN-KEYWORD,hachiraw
DOMAIN-KEYWORD,raw1001
DOMAIN-KEYWORD,nhentai
DOMAIN-KEYWORD,hitomi
DOMAIN-KEYWORD,e-hentai
DOMAIN-KEYWORD,exhentai
DOMAIN-KEYWORD,hentaifox
DOMAIN-KEYWORD,imhentai
DOMAIN-KEYWORD,mangadex
DOMAIN-KEYWORD,webtoon
DOMAIN-KEYWORD,manhuagui
DOMAIN-KEYWORD,manhuaren
DOMAIN-KEYWORD,bato
```

> 注意：关键词匹配范围大（如 `webtoon` 会命中 `webtoons.com`、`webtoon.kakao.com` 等，一般是好事；`bato` 要小心误伤无关域名），建议放在规则表靠后位置兜底，别放最前面。

## 10. 定期复查指南

**复查节奏**：官方平台（国内/日/韩正版）域名极少变，**每季度抽查一次**即可；聚合 / raw / 盗版站建议**每月一次**，直接逛一圈下表。

| 复查对象 | 看什么 | 入口 |
|---|---|---|
| 韩国轮换站（newtoki/manatoki/booktoki/toonkor/blacktoon/marumaru/wfwf/11toon…） | 当前编号域 | 各站官方 Telegram（见 §3 各自条目的「后续更新入口」） |
| 日本 raw / 聚合站 | 换域落点（301/302 目标） | keiyoushi 索引 `sources[].homeUrl`：https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.json |
| 拷贝漫画（CopyManga） | 大陆无障碍域名公告 | 站内首页横幅公告（mangacopy.com / copy4000.com） |
| e-hentai 全家 | 官方域名单 | https://ehwiki.org/wiki/IPs |
| hitomi | 图床域名 | https://hitomi.la/ 首页 JS（`ltn.gold-usergeneratedcontent.net/common.js`） |
| 各站域名增量 | 上游域名表 | v2fly：https://github.com/v2fly/domain-list-community/tree/master/data ；MetaCubeX mrs：https://github.com/MetaCubeX/meta-rules-dat |
| 全部站点 | 站点存活 | 重跑 §7 的实测方法（DoH 双解析 + curl 抓标题） |

**发现变化后的动作**：更新对应条目的域名与日期 → 同步更新 §9 的 payload 与规则集 → 在提交信息里写清"哪个站换到什么域名（来源链接）"。
