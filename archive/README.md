# archive/ — 历史文件，不要使用

这里放的是重构（2026-09）时从根目录移出的历史文件。它们**不再是维护对象**：
内部引用的是重构前的旧路径，直接使用会拉取失败。保留它们只是为了留个念想，
需要参考时看内容即可，不要让它们再回到 configs/ 里。

| 文件 | 原来是什么 | 为什么归档 |
|---|---|---|
| `ACL4SSR_Online.ini` | 最早的在线更新版模板（2024-09） | 引用的还是仓库根目录时期的路径（`main/Direct.list` 等 5 处），自 2024-09 目录迁移后就没再更新过，与 `configs/subconverter/acl4ssr-one.ini` 高度重叠 |
| `test.ini` | 调试用草稿 | 是 `acl4ssr-one.ini` 的早期版本，同样引用旧路径 `rule/Direct.list`、`rule/NoJP.list` |
| `Twitter.list` | 自建 Twitter 规则集 | 每行带 YAML 列表前缀 `- `，不是 classical 文本规则集格式（mihomo 会跳过这些行）；且 `configs/mihomo/*.yaml` 用的是 MetaCubeX 的 twitter.mrs，此文件已无用途 |
| `JapanManga.list` | 手写的成人向漫画/图站清单（10 条域名后缀） | 2026-10-05 退役：内容已由 `rules/MangaProxy.list`（478 条，含每日自动同步；2026-10-06 改名 `MangaProxyNoEH.list`）覆盖，仅 `hentai.cafe` 一个站新清单没有、已迁入其手工区 |
| `JapanAnime.list` | 手写的成人动画站清单（3 条） | 2026-10-05 退役：站点少且问题多——`hanime1` 被 `NoJP.list` 抢先命中（实际走非日本节点）、`animeh.to` / `fast4speed.rsvp` 确认不再需要 |
| `18comic.list` | 18comic 的规则集（1 条 `DOMAIN-KEYWORD,18-comic`） | 2026-10-05 退役：关键字已迁入 `rules/MangaCN.list`（按「国内可直连」归类），不再需要单独文件 |

## 如果确实还要用

1. 移到 `configs/` 下对应的子目录；
2. 把里面的 `raw.githubusercontent.com/jldxnb/openclash-rules/main/...` 引用改成当前路径
   （见 `docs/migration.md` 的对照表）；
3. 跑 `python scripts/validate.py` 确认没有 ERROR 再提交。

历史版本随时可以用 `git log --follow -- <文件>` 找回来。
