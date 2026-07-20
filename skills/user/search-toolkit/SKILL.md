---
name: search-toolkit
description: 三引擎自动分流搜索工具（Tavily + MiniMax + Exa）。当用户提出需要联网搜索的请求时使用此 skill——根据查询语言自动选择主引擎，失败时降级到下一引擎。中文查询走 MiniMax，英文/俄文走 uvx Tavily，编程/API 查询走 Exa。统一入口：& "$HOME/.codex/skills/search-toolkit/scripts/search.ps1" -Query "..."。
---

# Search Toolkit（三引擎自动分流）

本 skill 是 `~/.codex/AGENTS.md` 2026-07-19 三引擎自动分流逻辑的**镜像入口**。所有 Codex session 都可以从这里调用同一套逻辑。

## 何时使用

- 用户需要联网搜索资料、查 API 文档、查商品信息、查新闻
- 用户给出查询关键词，要求多语言 / 跨境电商 / 国际查询
- 用户要求"调用搜索工具"或类似的联网动作

## 调用方式

直接调用统一入口：

```powershell
& "$HOME/.codex/skills/search-toolkit/scripts/search.ps1" -Query "你的查询"

# 仅输出原始 JSON：
& "$HOME/.codex/skills/search-toolkit/scripts/search.ps1" -Query "你的查询" -JsonOnly
```

可选参数：
- `-JsonOnly`：只输出原始 JSON 到 stdout
- `-TimeoutSec 60`：子进程超时秒数（默认 60）

## 三个引擎的角色

| 引擎 | 何时作为主引擎 | 何时作为兜底 |
| --- | --- | --- |
| MiniMax | 中文 / 编程 API / 国内 | 英文查询的第三兜底 |
| uvx Tavily | 英文 / 俄文 / 国际 | 中文查询的第三兜底 |
| Exa | 编程 / API / 代码示例 | 任何场景的兜底补足 |

Tavily 套餐用完时不要手动切到 PS Tavily——`search.ps1` 会自动从 Exa 兜底。

## 源码位置

`C:\Users\Administrator\Documents\搜索工具\` 下完整备份：
- `scripts/search.ps1` —— 统一入口（本 skill 调它）
- `scripts/switch-engine.ps1` —— 环境检查器
- `scripts/MiniMax_web_search/`、`Tavily_web_search/`、`Exa_web_search/` —— 各引擎底层
- `README.md`、`UPSTREAM_SYNC.md` —— 文档

需要修改逻辑时改上面那个目录，本目录的 `scripts/search.ps1` 是 thin wrapper。

## 注意事项

- Codex 桌面端 stdio MCP 频繁返回 `unsupported call`，**不要依赖 `mcp__tavily__*` / `mcp__minimax__*`**，一律走本 skill 的 PowerShell 入口
- KEY 配置：`TAVILY_API_KEY` / `MINIMAX_API_KEY` / `EXA_API_KEY` 都从环境变量读，缺哪个引擎就跳过哪个
- 配额独立：Tavily 看月度免费额度，MiniMax 看 Token Plan 积分，Exa 看其自家套餐
