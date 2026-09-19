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

## 四、恢复的两个文件

都取自被删除前的最后一次提交，内容按原始字节恢复（可以用 `git hash-object` 验证）：

| 文件 | 来源提交 | 内容 |
|---|---|---|
| `rules/NoJP.list` | `8d525b3^`（2024-11-07 删除） | 只有 1 条：`DOMAIN-KEYWORD,hanime1` |
| `rules/ForYiFen.list` | `1932f50^`（2024-11-04 删除） | 只有 1 行被注释的 `;DOMAIN-SUFFIX,mikanani.me`，等于空规则集 |

注意 `NoJP.list` 恢复后内容极简，而 `hanime1` 同时也出现在 `rules/JapanAnime.list` 里
（那条走日本节点，与"非日本节点"组语义相反）。这是作者后来新建列表时留下的重复，
本次**没有替你决定该保留哪一边**，请在 "已知问题" 里看到后自行取舍。

## 五、重构后如何自查

```bash
python scripts/validate.py     # 0 错误才提交
```

校验脚本会扫描 `configs/` 与 `rules/` 中所有指向本仓库的 URL，任何一处指向不存在的文件
都会直接报 ERROR——也就是说，这次踩过的坑以后会在提交/CI 阶段被拦下。
