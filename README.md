# openclash-rules

个人的 Clash / mihomo（OpenClash）分流规则与配置模板集合，不是面向公众的通用规则库。

内容分三层：**自建规则**（`rules/`）、**完整配置**（`configs/mihomo/`）、
**订阅转换模板**（`configs/subconverter/`）。外部规则集来自
[ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)、
[blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)、
[MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat)，本仓库只维护自己的部分。

## 目录结构

```
configs/
  mihomo/          完整的 mihomo 配置，直接给 OpenClash 用
    one.yaml         单机场版（一个 proxy-provider，靠 include-all + filter 分日/非日）
    three.yaml       多机场版（stable / stable1 / cheap 三个订阅，便宜节点分流）
  subconverter/    subconverter 转换模板（ACL4SSR 语法）
    acl4ssr-one.ini  主力模板
    acl4ssr-two.ini  多机场 + 流媒体走便宜节点
    acl4ssr-cys.ini  带特定机场前缀的版本
    qichiyu.ini      基于骑秋雨的上游模板，未做本地改动
    qichiyu-custom.ini  上面的本地改版
rules/              自建规则集（classical 文本格式，被上面两类配置通过 raw URL 引用）
docs/
  migration.md      路径迁移对照表（重构前后的位置与 URL 变化）
  examples/         规则语法示例
scripts/
  validate.py       仓库自检脚本，见下文
archive/            历史文件，不要使用
```

## 怎么用

### 1. 单独引用某个规则集

在任意 mihomo 配置里加 rule-provider：

```yaml
rule-providers:
  ai:
    type: http
    interval: 86400
    behavior: classical
    format: text
    url: "https://raw.githubusercontent.com/jldxnb/openclash-rules/main/rules/AI.list"
```

### 2. 直接使用完整配置

把 `configs/mihomo/one.yaml`（或 `three.yaml`）的内容喂给 OpenClash。
**必须先替换占位符**（见下一节），否则订阅拉不下来。

### 3. 用 subconverter 模板转换

在 subconverter / OpenClash 的"订阅转换"里把 `configs/subconverter/acl4ssr-*.ini`
填为外部配置（`&config=` 参数指向该文件的 raw 地址）。

## 使用前必须替换的占位符

| 位置 | 当前值 | 要改成 |
|---|---|---|
| `configs/mihomo/one.yaml` | `url: "订阅"` | 真实机场订阅链接 |
| `configs/mihomo/three.yaml` | `url: "订阅"` ×3（stable / stable1 / cheap） | 三个订阅链接，或删掉不用的 provider 及其策略组 |
| `configs/mihomo/*.yaml` | `authentication: - name:passwd` | 真实 `用户名:密码`；同时建议 `allow-lan: false` |
| `configs/mihomo/*.yaml` | `external-controller: 0.0.0.0:9090` + `secret: ""` | 改为 `127.0.0.1:9090` 并设置非空 `secret`（当前等于把控制面板无密码开放给整个局域网） |
| `configs/mihomo/*.yaml` | DNS `127.0.0.1:5225` | 设备上确有本地 DNS 服务时保留，否则改公共 DNS |
| `configs/mihomo/*.yaml` | `mirror.ghproxy.com` | 该第三方镜像不稳定，建议换官方地址 |

## 日常维护

改完规则后跑一次自检，**0 错误再提交**：

```bash
python scripts/validate.py            # 离线检查（CI 每次提交都会跑）
python scripts/validate.py --online   # 额外探测外部 URL（每周定时跑，抓上游失效）
```

CI 配置在 `.github/workflows/validate.yml`，提交和 PR 会自动执行同样的检查。

`validate.py` 查这些：

- **引用完整性**：`configs/` 里所有指向本仓库的 raw URL 是否都能在仓库里找到对应文件
  （历史上这里翻过车：文件改名/删除后引用没跟着改，导致规则集全部 404）
- **规则集格式**：未知规则类型、缺失匹配内容、YAML 列表前缀 `- `、重复行、空规则集、UTF-8 BOM
- **mihomo 配置**：YAML 语法、rule-provider 必填字段、`RULE-SET` 是否指向已定义的 provider、
  策略组 `use` 是否指向已定义的订阅、未替换的占位符、控制面板与局域网的暴露风险
- **subconverter 模板**：`ruleset=` 指向的策略组是否在 `custom_proxy_group=` 中有定义
- **未引用文件**：`rules/` 下有哪些规则集没被任何配置使用（提示，不算错误）

## 约定

- `rules/*.list`：classical 文本格式，每行 `类型,内容[,参数]`，`#` 或 `;` 开头是注释；
  不要写 YAML 的 `- ` 前缀，不要放 `MATCH` / `RULE-SET` 这类规则（classical 规则集不允许）
- 新增规则集后，记得在 `configs/` 里引用它，否则 `validate.py` 会提示未被引用
- 文件编码 UTF-8（无 BOM），换行沿用 CRLF（见 `.editorconfig`）
- 命名：自建规则集用能一眼看懂的名字；外部上游规则集不要复制进本仓库，直接引用上游 URL

## 已知问题（未擅自修改，待决定）

| 位置 | 问题 |
|---|---|
| `rules/NoJP.list` 与 `rules/JapanAnime.list` | 都含 `DOMAIN-KEYWORD,hanime1`，但一个走"非日本节点"、一个走日本，语义相反，需要二选一 |
| `rules/ForYiFen.list` | 只有被注释的一行，等于空规则集；引用它的 `🍀 流媒体`、`🌍 默认用一分` 组目前不会命中任何流量 |
| `rules/AI.list:26` | `DOMAIN-SUFFIX,claude.ai.com` 应为 `claude.ai`（目前靠 `DOMAIN-KEYWORD,Claude` 兜底） |
| `rules/download.list` | `aria2c`、`uTorrent`、`WebTorrent` 各重复一次 |
| `configs/mihomo/*.yaml` | `dns.fallback` 是旧写法，新版 mihomo 更推荐 `nameserver-policy`（文件里两套都写了） |

重构前后的路径变化见 [docs/migration.md](docs/migration.md)。
