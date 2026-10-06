# openclash-rules

个人的 Clash / mihomo（OpenClash）分流规则与配置模板集合，不是面向公众的通用规则库。

内容分三层：**自建规则**（`rules/`）、**完整配置**（`configs/mihomo/`）、
**订阅转换模板**（`configs/subconverter/`）。外部规则集来自
[ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)、
[blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)、
[MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat)，本仓库只维护自己的部分。

## 目录结构

```
manga-sites.md      漫画站点域名清单（2026-10-05，729 个域名逐条实测+来源，供自建分流规则参考）
anime-sites.md      动漫站点域名清单（2026-10-06，736 个域名调研+实测）：国内直连 / 海外代理拆分、
                    代理·存疑清单、hanime1 家族的「非日本节点」说明、2026 年聚合站阵亡名单
configs/
  mihomo/          完整的 mihomo 配置，直接给 OpenClash / FlClash / Clash Party 用
    three-redir-host.yaml  主力配置（redir-host）：三机场 + 自建规则做例外分流 + MetaCubeX 上游（GEOSITE/GEOIP 内联）；
                      规则集走 jsDelivr、控制面板只监听本机、不依赖本机 127.0.0.1:5225。
                      注意：redir-host 下境外域名的解析依赖"代理可用"，代理不通会表现为
                      「国内正常、外站域名解析失败」
    three-fake-ip.yaml     上面那份的 fake-ip 版，**策略组/规则完全一致，只有 DNS 模式不同**
                      （手机 FlClash / TUN 场景用这一份：假 IP 不携带污染信息，连接时用域名出站、
                      由节点解析，既不依赖境外 DoH 也不怕污染）
    两份是孪生配置，改一份要同步另一份；其余历史配置（one / three / three-v2 等）
    已于 2026-10-06 删除，需要时从 git 历史取回
  subconverter/    subconverter 转换模板（ACL4SSR 语法）
    acl4ssr-one.ini  主力模板
    acl4ssr-two.ini  多机场 + 流媒体走便宜节点
    acl4ssr-cys.ini  带特定机场前缀的版本
    qichiyu.ini      基于骑秋雨的上游模板，未做本地改动
    qichiyu-custom.ini  上面的本地改版
rules/              自建规则集**手工源**（classical 文本，见「list 与 mrs」节）
  *.list              手工维护的清单；配置不直接用它，而是用下面两个生成物
  *.rest.list         生成物：清单里 mrs 表达不了的部分（DOMAIN-KEYWORD / IP-CIDR 等）
mrs/                生成物：清单的域名部分（mihomo 二进制规则集，索引查找，见「list 与 mrs」节）
docs/
  migration.md      路径迁移对照表（重构前后的位置与 URL 变化）
  examples/         规则语法示例
scripts/
  validate.py       仓库自检脚本，见下文
  gen_manga_rules.py  漫画清单同步（每日由 CI 运行，见「漫画 / 动漫规则集」节）
  gen_anime_rules.py  动漫清单同步（同上；自动上游 = FMHY）
  rules_sync.py     上面两个脚本共用的实现（清单格式、上游解析、突变保护）
  gen_mrs.py        由 rules/*.list 生成 mrs/ 与 rules/*.rest.list（见「list 与 mrs」节）
archive/            历史文件，不要使用
```

## list 与 mrs

`rules/*.list` 是**唯一手工维护的地方**（classical 文本，`类型,内容` 一行一条）；配置里引用的
却是两个自动生成物，各自放一个文件夹：

| 位置 | 内容 | 谁生成 |
|---|---|---|
| `mrs/<同名>.mrs` | 清单的域名部分（`DOMAIN` / `DOMAIN-SUFFIX`） | `python scripts/gen_mrs.py` |
| `rules/<同名>.rest.list` | mrs 表达不了的部分（`DOMAIN-KEYWORD` / `IP-CIDR` / `PROCESS-NAME` 等） | 同上 |

为什么不直接引用 `.list`：classical 文本规则集是**逐条线性扫描**，清单越大每个连接越慢；
`mrs` 走索引查找，代价与条目数基本无关。为什么还要留 `rest.list`：mrs 是域名前缀树，
只能表达"精确域名 / 后缀"，**表达不了 `DOMAIN-KEYWORD`**（关键词是"包含即可"），
把关键词硬塞进去只会变成永远匹配不到的死条目，所以清单必须拆成两半，
配置里用相邻的两条 `RULE-SET` 引用（指向同一个策略组，顺序不影响结果）。

改完清单后跑一次生成（有变化才会写文件）：

```bash
python scripts/gen_mrs.py            # 生成/更新 mrs/ 与 rules/*.rest.list
python scripts/gen_mrs.py --check    # 只校验产物与源清单是否一致（CI 用）
```

生成时会用 `mihomo convert-ruleset` 转出 mrs，再**转回文本逐条比对**，
任何条目对不上都会报错退出——防止"静默丢弃"这类看不见的行为变化。
CI（`.github/workflows/build-mrs.yml`）会在 `rules/**` 变更后自动重跑并提交产物；
漫画清单则由每日同步任务（见下）连带生成。mihomo 二进制会自动下载到 `.cache/`（已 gitignore）。

## 怎么用

### 1. 单独引用某个规则集

在任意 mihomo 配置里加 rule-provider（域名清单用 mrs；含关键词/IP 类的用 classical 文本）：

```yaml
rule-providers:
  ai:
    type: http
    interval: 86400
    behavior: domain
    format: mrs
    url: "https://raw.githubusercontent.com/jldxnb/openclash-rules/main/mrs/AI.mrs"
  ai_rest:            # 同一清单里 mrs 编不进去的关键词部分
    type: http
    interval: 86400
    behavior: classical
    format: text
    url: "https://raw.githubusercontent.com/jldxnb/openclash-rules/main/rules/AI.rest.list"
```

### 2. 直接使用完整配置

把 `configs/mihomo/three-redir-host.yaml`（桌面）或 `three-fake-ip.yaml`（手机 / TUN）
的内容喂给客户端。**必须先替换占位符**（见下一节），否则订阅拉不下来。

配置里几个可以随时切换的分流开关（在面板里改即可，不用编辑文件）：

| 组 | 作用 |
|---|---|
| `🛑 广告拦截` | 默认 `REJECT`（拦截广告域名）；切到 `DIRECT` 即全部放行 |
| `🔯 自动兜底` | 跨机场故障转移：`stable` 整体不可用时自动切到 `stable1`，再不行才用 `cheap` |
| `🔯 主备切换*`、`♻️ 便宜主备` | 都是 `fallback` 类型：默认用列表里第一个健康的节点，**也可以在面板里点选一个首选节点**（选择会持久化），该节点失效时自动切到下一个健康的 |
| `🎯 全球直连` | 切到 `🚀 节点选择` 可让所有国内直连流量也走代理 |
| `🐟 漏网之鱼` | 兜底流量，默认走节点选择，可切成直连 |

### 3. 用 subconverter 模板转换

在 subconverter / OpenClash 的"订阅转换"里把 `configs/subconverter/acl4ssr-*.ini`
填为外部配置（`&config=` 参数指向该文件的 raw 地址）。

## 漫画 / 动漫规则集（MangaCN、MangaProxyNoEH、AnimeCN、AnimeProxy）

四份域名清单，各按「用国内网络能否直接访问」划分——**按域名分，不按站点分**。同一个站可能出现
在两边：漫画的典型是拷贝漫画（`copy4000.com` 在国内集、`mangacopy.com` 在代理集），动漫的典型是
蜜柑计划（`mikanime.tv` 直连、`mikanani.me` 已被墙）。

| 清单 | 内容 | 自动上游 |
|---|---|---|
| `rules/MangaCN.list` | 漫画 / 网漫 / 同人 · 国内直连 | v2fly 的 manhuagui / manhuaren / copymanga 等 data 文件 |
| `rules/MangaProxyNoEH.list`（原 `MangaProxy.list`，2026-10-06 改名） | 漫画 / 网漫 / 同人 · 海外代理（**不含 e-hentai 家族**） | 同上（18comic / haitang / boylove / pixiv / dlsite / dmm-porn；e-hentai 家族已拆出，见下一节） |
| `rules/AnimeCN.list` | 动漫 · 国内直连（国内平台动漫区 + CDN、国际版未被墙域） | 无（国内平台域名稳定，纯手工维护） |
| `rules/AnimeProxy.list` | 动漫 · 海外代理（日系 / 海外聚合 / BT·字幕组 / 成人向） | FMHY 的 Anime Streaming / Downloading / Torrenting / Tracking 小节 |

域名来源与逐条实测记录：漫画见 [manga-sites.md](manga-sites.md)，动漫见 [anime-sites.md](anime-sites.md)。
「屏蔽 / 限制日本 IP」的站单独成两份清单：`rules/AnimeNoJP.list`（hanime1 家族、hanime.tv 系；
原 `NoJP.list` 于 2026-10-06 改名）与 `rules/MangaNoJP.list`（18comic / 3hentai / irodoricomics /
exhentai / manhuagui，证据分档见文件头注释）。配置里 `no_jp` 指向 AnimeNoJP.list，必须排在
`anime_proxy` / `manga_proxy_no_eh` 之前命中；`AnimeProxy.list` 尾部另留了一份同内容的备用条目，
没接 NoJP 时也能走同样路线。

每份清单分两区：

- **手工维护区**：随手改，脚本永远不动它；想固定某条不被上游增删影响，把它挪到这里。
- **自动同步区**：由 `scripts/gen_manga_rules.py` / `scripts/gen_anime_rules.py` 合并上游增量，
  **每天自动重写**（CI：`.github/workflows/update-rules.yml`，北京时间 06:30）。安全设计：只重写
  自动区；任何上游拉取失败都不写不提交；自动区条目数骤降（疑似上游改版 / 解析失效）时拒绝写入。
  `AnimeProxy.list` 的「代理·存疑」区是手工条目——面向大陆但托管墙外的中文聚合站（樱花 / 风车 /
  AGE / 稀饭等），默认按代理放，实测直连可用再挪到 AnimeCN。

在配置里引用（沿用「list 与 mrs」的做法：域名部分用 mrs，关键词部分用 rest 文本；
AnimeCN / AnimeProxy 没有关键词条目，所以不需要 rest provider）：

```yaml
rule-providers:
  manga_cn:
    type: http
    interval: 86400
    behavior: domain
    format: mrs
    url: "https://raw.githubusercontent.com/jldxnb/openclash-rules/main/mrs/MangaCN.mrs"
  manga_cn_rest:
    type: http
    interval: 86400
    behavior: classical
    format: text
    url: "https://raw.githubusercontent.com/jldxnb/openclash-rules/main/rules/MangaCN.rest.list"
  manga_proxy:
    type: http
    interval: 86400
    behavior: domain
    format: mrs
    url: "https://raw.githubusercontent.com/jldxnb/openclash-rules/main/mrs/MangaProxyNoEH.mrs"
  manga_proxy_rest:
    type: http
    interval: 86400
    behavior: classical
    format: text
    url: "https://raw.githubusercontent.com/jldxnb/openclash-rules/main/rules/MangaProxyNoEH.rest.list"
  anime_cn:
    type: http
    interval: 86400
    behavior: domain
    format: mrs
    url: "https://raw.githubusercontent.com/jldxnb/openclash-rules/main/mrs/AnimeCN.mrs"
  anime_proxy:
    type: http
    interval: 86400
    behavior: domain
    format: mrs
    url: "https://raw.githubusercontent.com/jldxnb/openclash-rules/main/mrs/AnimeProxy.mrs"
rules:
  - RULE-SET,manga_cn,🎯 全球直连
  - RULE-SET,manga_cn_rest,🎯 全球直连
  - RULE-SET,manga_proxy,🚀 节点选择      # 本仓库当前配置里指向 🎌 漫画动漫 组
  - RULE-SET,manga_proxy_rest,🚀 节点选择
  - RULE-SET,anime_cn,🎯 全球直连
  - RULE-SET,anime_proxy,🚀 节点选择      # 同上，可自行接到 🎌 漫画动漫 组
```

本地手动同步：`python scripts/gen_manga_rules.py` / `python scripts/gen_anime_rules.py`
（只报告变化，不写文件）、加 `--apply` 写入；写入后要再跑 `python scripts/gen_mrs.py`
重建 mrs 与 rest（CI 里这两步是连着做的）。

> 这四份清单现已全部接进 `configs/`（`manga_cn` → 🎯 全球直连、`manga_proxy_no_eh` → 🎌 漫画动漫、
> `anime_cn` → 🎯 全球直连、`anime_proxy`(+rest) → 🎌 漫画动漫）；`validate.py` 对仍未引用的清单
> （如 `rules/MangaNoJP.list`）给出的「未被引用」提示属正常（不是错误）。

## B站番剧 / e-hentai 专用组（`rules/BiliBiliHMT.list`、`rules/MangaEHentai.list`）

两份清单各对应一个可切换的策略组（2026-10-06 增加）：

| 清单 | 内容 | 指向的策略组 |
|---|---|---|
| `rules/BiliBiliHMT.list`（自建） | B站港澳台限定番剧的「地区判定 + 播放入口」（`api.` / `bangumi.` / `www.`）+ 国际版（`bilibili.tv` / `biliintl.com` / `p.bstarstatic.com`） | `📺 B站番剧` |
| `rules/MangaEHentai.list`（自建，从 MangaProxyNoEH 拆出） | e-hentai / ExHentai 家族 8 个域名（= geosite:ehentai 全集）+ 2 条关键词（拆进 `MangaEHentai.rest.list`） | `🔞 e-hentai` |
| 上游 blackmatrix7 的 `BiliBili.list`（**直接引用 URL，不复制进仓库**） | B站系其余域名：全部 CDN / PCDN 主机、四个 akamai 镜像（含港澳台番剧的海外 UPOS `upos-hz-mirrorakam`）、`biliplus` / `hdslb` / App 包名等 | `🎯 全球直连` |

- **📺 B站番剧**：默认 `DIRECT`——与不加这份清单时行为完全一致。要看港澳台限定番剧时，把这一组
  切到「🔯 主备切换|港澳台」或「…|港澳台1」（各机场一条；过滤器 `hktw` 只收香港 / 台湾节点）。
  港澳台限制是在**接口层**判定的，所以只有判定 / 取址域名进这个组；视频 CDN（`upos-*` / `mcdn`、
  四个 akamai 镜像）由 `bilibili_cn` 保持直连——播放地址是签名直链，CDN 不做地区判定，走代理只会更慢。
  规则顺序上 `bilibili_hmt` **必须排在 `bilibili_cn` 之前**：上游清单里的 `+.bilibili.com` 会把判定域名
  先接走，顺序反了 📺 组就切不动。
  代价：切到港澳台之后，内地版权内容也会变成"港澳台视角"（两者共用同一批域名，无法自动区分，
  只能手动切组）。
- **🔞 e-hentai**：图站的下载额度按 IP 记，独立成组方便换机场 / 换节点。候选与「🎌 漫画动漫」
  同源（非日本链 + 全机场非日本节点，`no_jp` 过滤——exhentai 对日本 IP 有限制，证据见
  `rules/MangaNoJP.list` 文件头）。
- 动漫两份清单也一并接进来了：`anime_cn` → `🎯 全球直连`（国内平台动漫区，按清单定位直连）、
  `anime_proxy`(+`anime_proxy_rest`) → `🎌 漫画动漫`（海外动漫站；其中「不能用日本节点」的
  hanime1 家族由更靠前的 `no_jp` 规则先命中，同样落这一组）。
- 两个组用的 `hktw` / `no_hktw` 筛选词都定义在 `x-node-filters`，改词只改那一处。
- e-hentai 家族原来在漫画代理清单里；现已迁出成独立的 `MangaEHentai.list`，原清单同时改名
  `MangaProxy.list` → `MangaProxyNoEH.list`（文件名直接写明「不含 e-hentai」）
  （文件名保留了 Manga 前缀，一眼能看出它是从漫画清单拆出来的），`gen_manga_rules.py` 也不再同步
  v2fly 的 `data/ehentai`（否则 CI 会把条目写回 MangaProxyNoEH）。

## 使用前必须替换的占位符

| 位置 | 当前值 | 要改成 |
|---|---|---|
| `configs/mihomo/*.yaml` | `url: "订阅"` ×3（stable / stable1 / cheap） | 三个订阅链接，或删掉不用的 provider 及其策略组 |
| `configs/mihomo/*.yaml` | `authentication: - name:passwd` | 真实 `用户名:密码`；同时建议 `allow-lan: false` |
| `configs/mihomo/*.yaml` | `external-controller: 0.0.0.0:9090` + `secret: ""` | 改为 `127.0.0.1:9090` 并设置非空 `secret`（当前等于把控制面板无密码开放给整个局域网） |
| `configs/mihomo/*.yaml` | DNS `127.0.0.1:5225` | 设备上确有本地 DNS 服务时保留，否则改公共 DNS |

## 日常维护

改完规则后跑一次自检，**0 错误再提交**：

```bash
python scripts/validate.py            # 离线检查（CI 每次提交都会跑）
python scripts/validate.py --online   # 额外探测外部 URL（每周定时跑，抓上游失效）
```

CI 配置在 `.github/workflows/validate.yml`，提交和 PR 会自动执行同样的检查。

`validate.py` 查这些：

- **引用完整性**：`configs/` 里所有指向本仓库的 URL（raw 与 jsDelivr 两种写法都认）是否都能
  在仓库里找到对应文件（历史上这里翻过车：文件改名/删除后引用没跟着改，导致规则集全部 404）
- **规则集格式**：未知规则类型、缺失匹配内容、YAML 列表前缀 `- `、重复行、空规则集、UTF-8 BOM
- **mrs 与源清单的对应**：纯域名清单有没有 mrs 产物、有没有孤儿 mrs、配置引用了 mrs 却漏引
  对应的 `*.rest.list`（内容层面的"是否同步"由 `gen_mrs.py --check` 负责）
- **孪生配置同步**：`three-redir-host.yaml` 与 `three-fake-ip.yaml` 除「文件头 / dns 段 / store-fake-ip」
  外必须逐字节相同——只改一份会被直接报错
- **mihomo 配置**：YAML 语法、rule-provider 必填字段（`format: mrs` 必须是 `domain`/`ipcidr`）、
  `RULE-SET` 是否指向已定义的 provider、策略组 `use` 是否指向已定义的订阅、未替换的占位符、
  控制面板与局域网的暴露风险
- **subconverter 模板**：`ruleset=` 指向的策略组是否在 `custom_proxy_group=` 中有定义
- **未引用文件**：`rules/` 下有哪些规则集没被任何配置使用（提示，不算错误）

## 约定

- `rules/*.list`：classical 文本格式，每行 `类型,内容[,参数]`，`#` 或 `;` 开头是注释；
  不要写 YAML 的 `- ` 前缀，不要放 `MATCH` / `RULE-SET` 这类规则（classical 规则集不允许）
- **只改 `rules/*.list`，别改 `mrs/` 与 `rules/*.rest.list`**：后两者是生成物（文件头也写了），
  改完 list 跑 `python scripts/gen_mrs.py` 重新生成；配置引用生成物，不引用 `.list`
- **自建列表排在前面 = 优先级更高**：`configs/` 里的自建 rule-provider / ruleset 都排在通用规则
  （`geolocation-!cn`、`MATCH` / `FINAL`）之前，顺序匹配、首个命中即生效。要给某些站点做特殊分流
  （比如"这个站不能走日本节点"），直接往对应 `rules/*.list` 里追加即可——这类列表是**例外清单**，
  只有一两条是正常的，不需要凑成完整清单
- 新增规则集后，记得在 `configs/` 里引用它（并跑一次 `gen_mrs.py`），否则 `validate.py` 会报错/提示
- 新增规则集时，若清单里既有域名条目又有 `DOMAIN-KEYWORD` 之类，配置里要引用成对的
  `mrs/<名>.mrs` + `rules/<名>.rest.list` 两条 `RULE-SET`，指向同一个策略组、紧挨着写
- 文件编码 UTF-8（无 BOM），换行沿用 CRLF（见 `.editorconfig`）；`mrs/` 是二进制（`.gitattributes` 已标 binary）
- 命名：自建规则集用能一眼看懂的名字；外部上游规则集不要复制进本仓库，直接引用上游 URL

## 已知问题（未擅自修改，待决定）

| 位置 | 问题 |
|---|---|
| `rules/AnimeNoJP.list`（原 `NoJP.list`，2026-10-06 改名） | 动漫侧"非日本"清单：1 条关键词（hanime1 家族轮换兜底）+ 9 个域名（hanime1 家族与 hanime.tv 系，日本 IP 受限；证据见 anime-sites.md §5/§8.4）。漫画侧同类清单是 `rules/MangaNoJP.list`（18comic / 3hentai / irodoricomics / exhentai / manhuagui，证据与"已排查但不需要"的名单都写在文件头注释里，暂未被 configs 引用）。两份清单都有 mrs 产物，但配置仍直接引用 `.list`（10 条量级用文本足够）；顺序上 `no_jp` 必须排在 `anime_proxy` / `manga_proxy` 之前（考证见 [docs/migration.md](docs/migration.md) 第四、五节） |
| `rules/AI.list:26` | `DOMAIN-SUFFIX,claude.ai.com` 应为 `claude.ai`（目前靠 `DOMAIN-KEYWORD,Claude` 兜底） |
| `rules/download.list` | `aria2c`、`uTorrent`、`WebTorrent` 各重复一次 |
| `configs/mihomo/*.yaml` | `dns.fallback` **未废弃**（此前误记为旧写法；官方废弃的是 `fallback-filter.geosite`，文件里没用它）。但它与 `nameserver-policy` 并存会让两套 DNS 并行查询，官方提供 `fallback-lazy-query: true` 可避免 |

重构前后的路径变化见 [docs/migration.md](docs/migration.md)。
