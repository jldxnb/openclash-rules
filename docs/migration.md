# 路径迁移对照表

2026-09 对仓库做了一次结构重构：把散落在根目录的配置按用途分目录，修正了
一批指向已删除/已改名文件的失效引用，并把历史草稿归档。

**如果你是配置的使用者（路由器 / OpenClash / subconverter 里填了本仓库的地址），
只需要照着下面第二张表替换 URL 即可。**

---

## 一、文件位置变化

| 旧路径 | 新路径 | 说明 |
|---|---|---|
| `ACL4SSR_one.ini` | `configs/subconverter/acl4ssr-one.ini` | 当前在用模板 |
| `ACL4SSR_two.ini` | `configs/subconverter/acl4ssr-two.ini` | 多机场/流媒体版 |
| `ACL4SSR_cys.ini` | `configs/subconverter/acl4ssr-cys.ini` | 特定机场前缀版 |
| `qichiyu.ini` | `configs/subconverter/qichiyu.ini` | 基于骑秋雨规则，未改 |
| `qichiyu-edit.ini` | `configs/subconverter/qichiyu-custom.ini` | 改名，表达"本地改版" |
| `one.yaml` | `configs/mihomo/one.yaml` | 单机场完整配置 |
| `three.yaml` | `configs/mihomo/three.yaml` | 多机场完整配置 |
| `rule/<名字>.list` | `rules/<名字>.list` | 目录名由单数改复数 |
| `rule/rule_template.list` | `docs/examples/rule_template.list` | 它是语法示例，不是规则集 |
| `ACL4SSR_Online.ini` | `archive/ACL4SSR_Online.ini` | 已过时，归档 |
| `test.ini` | `archive/test.ini` | 早期草稿，归档 |
| `rule/Twitter.list` | `archive/Twitter.list` | 格式不合法且无人引用，归档 |

## 二、引用地址变化（raw URL）

基址 `https://raw.githubusercontent.com/jldxnb/openclash-rules/main/` 不变，只改后面的路径。

| 旧地址 | 新地址 |
|---|---|
| `.../main/rule/AI.list` | `.../main/rules/AI.list` |
| `.../main/rule/BlueArchive.list` | `.../main/rules/BlueArchive.list` |
| `.../main/rule/DirectOwn.list` | `.../main/rules/DirectOwn.list` |
| `.../main/rule/NoJP.list` | `.../main/rules/NoJP.list` |
| `.../main/rule/ForYiFen.list` | `.../main/rules/ForYiFen.list` |
| `.../main/rule/ProxyLite.list` | `.../main/rules/ProxyLite.list` |
| `.../main/Direct.list` | `.../main/rules/DirectOwn.list`（见下方说明） |
| `.../main/ACL4SSR_one.ini` | `.../main/configs/subconverter/acl4ssr-one.ini` |
| `.../main/ACL4SSR_two.ini` | `.../main/configs/subconverter/acl4ssr-two.ini` |
| `.../main/ACL4SSR_cys.ini` | `.../main/configs/subconverter/acl4ssr-cys.ini` |
| `.../main/qichiyu.ini` | `.../main/configs/subconverter/qichiyu.ini` |
| `.../main/qichiyu-edit.ini` | `.../main/configs/subconverter/qichiyu-custom.ini` |
| `.../main/one.yaml` | `.../main/configs/mihomo/one.yaml` |
| `.../main/three.yaml` | `.../main/configs/mihomo/three.yaml` |

## 三、本次修复的失效引用

重构前，仓库里 8 个配置有 7 个带着 404 的引用（只有 `qichiyu.ini` 是干净的）。
原因都是文件改名/删除后没有回头更新引用。现在全部指向真实存在的文件：

| 失效引用 | 出现位置 | 现在指向 | 依据 |
|---|---|---|---|
| `.../main/rule/Direct.list` | `acl4ssr-cys.ini` | `.../main/rules/DirectOwn.list` | `Direct.list` 在 2024-10-07 被重命名为 `DirectOwn.list`（提交 `37916ab`） |
| `.../main/rule/NoJP.list` | `one.yaml`、`three.yaml`、`acl4ssr-one/two/cys.ini` | `.../main/rules/NoJP.list` | 文件已从历史恢复，见下 |
| `.../main/rule/ForYiFen.list` | `acl4ssr-one/two/cys.ini` | `.../main/rules/ForYiFen.list` | 同上 |
| `.../main/Direct.list`、`.../main/ProxyLite.list`、`.../main/AI.list` | `qichiyu-custom.ini` | `.../main/rules/` 下同名文件 | 旧根路径遗留写法 |
| 根路径 5 处 | `archive/ACL4SSR_Online.ini` | 不修（文件已归档） | 归档文件保持原样 |

## 四、恢复的两个文件：来源考证

两个文件都取自被删除前的最后一次提交，按原始字节恢复，blob 哈希与删除前一致：

```bash
git rev-parse 8d525b3^:rule/NoJP.list      # e385d8288b200d39ee7bd1a42bf248f1d039908f
git rev-parse refactor/project-structure:rules/NoJP.list   # 同上
```

但**恢复原样不等于恢复用途**，这两个文件的内容一直是残缺的。把它们的全部历史翻出来：

| 文件 | 生命周期 | 每一版的内容 |
|---|---|---|
| `NoJP.list` | 2024-09-17 上传（`5e72993`）→ 09-20 改关键字（`11fe143`）→ 11-07 删除（`8d525b3`） | 三版都只有 1 条，先是 `DOMAIN-SUFFIX,hanime1`，后改为 `DOMAIN-KEYWORD,hanime1` |
| `ForYiFen.list` | 2024-09-13 上传（`aa4e172`）→ 当天自己注释掉（`43a4b86`）→ 11-04 删除（`1932f50`） | 只有 `DOMAIN-SUFFIX,mikanani.me`（蜜柑计划），第二版起被注释，等于空集 |

关键线索：两个文件的第一行注释**完全相同**——`# 内容：默认这些使用一分机场`。
也就是说它们不是公共规则集，而是作者记录"这几个站点默认走便宜机场"的**个人便签**，
所以内容始终只有一两个域名。

另外查证了两点：

1. **它们从来没有指向过别人的仓库。** 最早的模板（`85ce0a9`，2024-09-17）第 15 行就已经是
   `ruleset=非日本代理,https://raw.githubusercontent.com/jldxnb/openclash-rules/main/NoJP.list`，
   指向本仓库；文件是通过 GitHub 网页 "Add files via upload" 从本地上传的。
2. **社区没有现成的同类列表可以替代。** 已检索 GitHub 仓库搜索、ACL4SSR、
   qichiyuhub/rule、Repcz/Tool、DustinWin/ruleset_geodata、Aethersailor/Custom_OpenClash_Rules
   等常见规则仓库，均无"非日本节点"这类清单（ACL4SSR 只有 `HuluJapan.list` 这种服务列表）。
   原因是"哪些站点不能用日本节点"高度个人化，取决于机场和具体服务；社区通行做法是
   按地区建节点组 + 按服务维护域名列表。

结论：引用已修好（不再 404）。`rules/NoJP.list` 只有 1 条**不是残缺，而是设计如此**——
它是一份"例外清单"，靠规则顺序提前命中来做特殊分流，详见下一节。

## 五、NoJP 这类列表是怎么生效的（顺序优先）

`rules/` 下的自建列表在配置里都排在**最前面**，作用是抢在通用规则之前把特定域名捞出来改道：

```
configs/mihomo/one.yaml（three.yaml 同）
  159  RULE-SET,direct1,DIRECT              ← 自建，第 1 条
  160  RULE-SET,ai,🎮 日美等节点             ← 自建
  161  RULE-SET,no_jp,🎞️ 非日本节点          ← 自建，第 3 条
  ...  各种 geosite 服务规则
  175  RULE-SET,geolocation-!cn,🚀 节点选择   ← 通用：几乎所有非中国域名
  181  MATCH,🐟 漏网之鱼                     ← 兜底：默认也是节点选择

configs/subconverter/acl4ssr-one.ini（同理）
  13  ruleset=🎯 全球直连,.../DirectOwn.list
  14  ruleset=🤖 AI,.../AI.list
  15  ruleset=🎞️ 非日本节点,.../NoJP.list     ← 第 3 条
  ...
  38  ruleset=🐟 漏网之鱼,[]FINAL             ← 兜底
```

规则是**顺序匹配、首个命中即生效**，所以前面命中之后，后面的通用规则不会再看到这个域名。
`hanime1` 若不在 `no_jp` 里，就会落到 `geolocation-!cn`（目标"节点选择"）或兜底的
`MATCH`/`FINAL`（目标"漏网之鱼"，默认同样是节点选择），而这两处都可能选到日本节点——
提前捞出来正是为了避开这一点。

因此这类列表**短是正常的**：它记录的是"我特别指定要改道的站点"，不是"所有非日本站点"。
要加新的例外站点，直接追加到对应 `rules/*.list` 即可，位置不需要动（配置里已经排在前面）。

顺带修正一条此前的判断：`hanime1` 虽然同时出现在 `rules/JapanAnime.list`（走日本节点），
但 `JapanAnime.list` 目前没有被任何配置引用（`scripts/validate.py` 会提示），
所以眼下不存在真实冲突，属于备用件；将来真要引用它时再决定 `hanime1` 归属即可。

## 五、重构后如何自查

```bash
python scripts/validate.py     # 0 错误才提交
```

校验脚本会扫描 `configs/` 与 `rules/` 中所有指向本仓库的 URL，任何一处指向不存在的文件
都会直接报 ERROR——也就是说，这次踩过的坑以后会在提交/CI 阶段被拦下。
