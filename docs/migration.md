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

结论：引用已修好（不再 404），但 `rules/NoJP.list` 只有 1 条，**撑不起"非日本节点"这个用途**。
本次没有替你编内容，也没有替你决定 `hanime1` 该走哪边（它同时出现在 `rules/JapanAnime.list`，
那份是走日本节点的，语义相反）。需要按 "已知问题" 里的说明自行取舍。

## 五、重构后如何自查

```bash
python scripts/validate.py     # 0 错误才提交
```

校验脚本会扫描 `configs/` 与 `rules/` 中所有指向本仓库的 URL，任何一处指向不存在的文件
都会直接报 ERROR——也就是说，这次踩过的坑以后会在提交/CI 阶段被拦下。
