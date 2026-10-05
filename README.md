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
configs/
  mihomo/          完整的 mihomo 配置，直接给 OpenClash / FlClash / Clash Party 用
    three-v2-redir-host.yaml  主力配置（redir-host）：三机场 + 自建规则做例外分流 + MetaCubeX mrs；
                      规则集走 jsDelivr、控制面板只监听本机、不依赖本机 127.0.0.1:5225。
                      注意：redir-host 下境外域名的解析依赖"代理可用"，代理不通会表现为
                      「国内正常、外站域名解析失败」
    three-v2-fake-ip.yaml     上面那份的 fake-ip 版，**策略组/规则完全一致，只有 DNS 模式不同**
                      （手机 FlClash / TUN 场景用这一份：假 IP 不携带污染信息，连接时用域名出站、
                      由节点解析，既不依赖境外 DoH 也不怕污染）
    两份是孪生配置，改一份要同步另一份；其余历史配置（one / three / three-redir-host / three-v2）
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
  gen_manga_rules.py  漫画规则集同步脚本（每日由 CI 自动运行，见「漫画规则集」节）
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

把 `configs/mihomo/three-v2-redir-host.yaml`（桌面）或 `three-v2-fake-ip.yaml`（手机 / TUN）
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

## 漫画规则集（MangaCN / MangaProxy）

`rules/MangaCN.list`（国内直连）与 `rules/MangaProxy.list`（海外代理）是漫画 / 网漫 / 同人站的
两份域名清单，按「用国内网络能否直接访问」划分——**按域名分，不按站点分**（同一个站的直连域
和需代理域会分别落在两个清单里，典型如拷贝漫画：`copy4000.com` 在国内集、`mangacopy.com`
在代理集）。域名来源与逐条实测记录见根目录 [manga-sites.md](manga-sites.md)。

每份清单分两区：

- **手工维护区**：随手改，脚本永远不动它；想固定某条不被上游增删影响，把它挪到这里。
- **自动同步区**：由 `scripts/gen_manga_rules.py` 从
  [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community/tree/master/data)
  的漫画相关 data 文件合并增量，**每天自动重写**（CI：`.github/workflows/update-manga-rules.yml`，
  北京时间 06:30；有变化才提交，拉上游失败时不写不提交，避免误删条目）。

在配置里引用（沿用「list 与 mrs」的做法：域名部分用 mrs，关键词部分用 rest 文本）：

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
    url: "https://raw.githubusercontent.com/jldxnb/openclash-rules/main/mrs/MangaProxy.mrs"
  manga_proxy_rest:
    type: http
    interval: 86400
    behavior: classical
    format: text
    url: "https://raw.githubusercontent.com/jldxnb/openclash-rules/main/rules/MangaProxy.rest.list"
rules:
  - RULE-SET,manga_cn,🎯 全球直连
  - RULE-SET,manga_cn_rest,🎯 全球直连
  - RULE-SET,manga_proxy,🚀 节点选择
  - RULE-SET,manga_proxy_rest,🚀 节点选择
```

本地手动同步：`python scripts/gen_manga_rules.py`（只报告变化，不写文件）、加 `--apply` 写入；
写入后要再跑 `python scripts/gen_mrs.py` 重建 mrs 与 rest（CI 里这两步是连着做的）。

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
| `rules/NoJP.list` | 只有 1 条 `DOMAIN-KEYWORD,hanime1`——这是**例外清单**，靠顺序提前命中做分流，短是正常的；关键词编不进 mrs，所以它没有 mrs 产物，配置直接引用 `.list`（考证见 [docs/migration.md](docs/migration.md) 第四、五节） |
| `rules/AI.list:26` | `DOMAIN-SUFFIX,claude.ai.com` 应为 `claude.ai`（目前靠 `DOMAIN-KEYWORD,Claude` 兜底） |
| `rules/download.list` | `aria2c`、`uTorrent`、`WebTorrent` 各重复一次 |
| `configs/mihomo/*.yaml` | `dns.fallback` **未废弃**（此前误记为旧写法；官方废弃的是 `fallback-filter.geosite`，文件里没用它）。但它与 `nameserver-policy` 并存会让两套 DNS 并行查询，官方提供 `fallback-lazy-query: true` 可避免 |

重构前后的路径变化见 [docs/migration.md](docs/migration.md)。
