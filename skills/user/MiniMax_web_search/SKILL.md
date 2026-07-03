---
name: MiniMax_web_search
description: Web search backed by the MiniMax (Token Plan) search engine. Use when Codex needs Chinese-language search results, Chinese programming / API docs, Chinese news, Chinese e-commerce platforms (1688, Taobao, JD, Pinduoduo, etc.), or any query where Chinese sources are more useful than Western ones. Works on Windows PowerShell 5+ via the `minimax-coding-plan-mcp` stdio server. Triggers on phrases like '搜索中文', '查一下国内', '搜国内新闻', '查 1688 / 淘宝 / 拼多多 / 京东 规则', 'find on 1688', or any query that is predominantly Chinese characters. Complements the `Tavily_web_search` skill, which is preferred for English / Russian / international content.
metadata:
  short-description: Search the web via MiniMax Chinese-optimized search engine
---

# MiniMax Web Search Skill (uvx + minimax-coding-plan-mcp, PowerShell)

This skill provides a Chinese-first web search by running the official
`minimax-coding-plan-mcp` stdio server through `uvx` and talking to it
via JSON-RPC. It returns the same shape as Tavily (AI answer + organic
results + related searches) so Codex can use both skills interchangeably.

## Prerequisites

- A MiniMax API key set in the **User** environment variable `MINIMAX_API_KEY`,
  and (optionally) `MINIMAX_API_HOST` (defaults to `https://api.minimaxi.com`).
- Windows PowerShell 5.1+ and `uvx` on PATH (installed via `pip install uv`).
- Network access to the MiniMax API host on 443.

## Bundled scripts

| Script | Purpose |
| --- | --- |
| `scripts/search.ps1` | One-shot web search; accepts `-Query` and prints the result |

## Quick usage

```powershell
& "$HOME\.codex\skills\MiniMax_web_search\scripts\search.ps1" -Query "1688跨境宝 最新规则 2025"
```

## When to use this skill (vs Tavily_web_search)

- **Use `MiniMax_web_search`** when:
  - Query is predominantly Chinese (e.g. "查一下速卖通招商政策", "1688 跨境宝费率")
  - Need Chinese news / e-commerce / regulatory content
  - Query is about Chinese programming APIs or Chinese docs
- **Use `Tavily_web_search`** when:
  - Query is English / Russian / Cyrillic
  - Need international / cross-border e-commerce intel (Ozon, Wildberries, Amazon US/EU)
  - Need academic / English-language research

## Operational notes

- One MCP session is spawned per call (the stdio server starts, processes
  the request, then exits). Cold start is ~2-3 s due to `uvx` install-on-demand.
- Quota is governed by the user's MiniMax Token Plan (independent of Tavily).
- If the API call fails (network / quota / auth), the script exits non-zero
  with an error on stderr.

## When NOT to use

- For English / Russian / international search, prefer `Tavily_web_search`.
- For image understanding, use the built-in Codex tool when available
  (`mcp__minimax__understand_image`).
