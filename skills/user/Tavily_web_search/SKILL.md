---
name: Tavily_web_search
description: Web search and URL extraction backed by the Tavily API. Use when Codex needs to (1) search the public web for current information, news, market data, or any topic beyond its knowledge cutoff, (2) extract and read the body content of a specific URL, (3) do deep multi-source research on a topic, or (4) crawl a website starting from a URL. Works on Windows PowerShell 5+ via Invoke-RestMethod - no Node, no Python, no MCP server required. Triggers on phrases like 'search the web', 'google this', 'find online', 'look up', 'what is the latest on', 'fetch this URL', 'research this topic', 'crawl this site'.
metadata:
  short-description: Search the web and extract URL content via Tavily HTTP API
---

# Web Search Skill (Tavily HTTP, PowerShell)

This skill replaces the previously-installed Tavily stdio MCP, which Codex desktop app
refuses to load (`Auth = Unsupported`). It provides the same four capabilities through
direct HTTP calls to `https://api.tavily.com`, runnable from any PowerShell session.

## Prerequisites

- A Tavily API key set in the **User** environment variable `TAVILY_API_KEY`.
  Get one at https://tavily.com (free dev tier available).
- Windows PowerShell 5.1+ (works in PowerShell 7 too). No external modules.
- Network access to `api.tavily.com` on 443.

## Bundled scripts

| Script | Endpoint | Purpose |
| --- | --- | --- |
| `scripts/search.ps1` | `POST /search` | Web search with optional answer synthesis |
| `scripts/extract.ps1` | `POST /extract` | Extract body content from one or more URLs |
| `scripts/crawl.ps1` | `POST /crawl` | Crawl a website starting from a URL |
| `scripts/research.ps1` | `POST /research` | Multi-source deep research (sync, up to ~1 min) |

All scripts share the same conventions:

- Read key from `TAVILY_API_KEY` env var (exit with a clear error if missing).
- Accept parameters as named args (`-Query`, `-MaxResults`, etc.). Run with `-?` for full help.
- Write JSON result to stdout, human-readable summary to stderr - or invert with `-JsonOnly` / `-SummaryOnly`.
- Encode JSON safely with `ConvertTo-Json -Depth 10`.
- Set a 30 s default timeout (override with `-TimeoutSec`).

## Quick usage

```powershell
# 1. Web search
& "$HOME\.codex\skills\web-search\scripts\search.ps1" -Query "Russia automotive aftermarket 2025" -MaxResults 8

# 2. Extract a URL
& "$HOME\.codex\skills\web-search\scripts\extract.ps1" -Url "https://www.gmiresearch.com/report/russia-automotive-aftermarket-market"

# 3. Crawl a site
& "$HOME\.codex\skills\web-search\scripts\crawl.ps1" -Url "https://example.com" -MaxDepth 2 -Limit 10

# 4. Deep research
& "$HOME\.codex\skills\web-search\scripts\research.ps1" -Input "Latest trends in Russian auto parts e-commerce 2025"
```

## When to use which script

- `search.ps1` — default for "look this up" / "find X online". Fast (< 5 s).
- `extract.ps1` — when you already have a specific URL in hand (e.g. from a previous search).
- `crawl.ps1` — when you need to map a site or pull a section (e.g. a docs subfolder).
- `research.ps1` — for broad multi-source questions. Slow (30-60 s), returns a long answer + sources.

## Operational notes

- Tavily `search_depth=advanced` is slower but richer; use it for market/competitive research.
- Use `topic=news` for recent news; default is `general`.
- `include_answer=true` (default) returns a synthesized short answer at the top - useful as a TL;DR.
- For Russian-language queries, use Cyrillic directly; Tavily auto-detects language.
- Free tier has a monthly request cap - prefer `search_depth=basic` for routine lookups.

## When NOT to use

- For GitHub-only lookups, prefer the GitHub MCP tools (`mcp__github__*`).
- For content already on the local filesystem, use `rg` / `cat` instead of fetching it.
- For Codex CLI's built-in `web_search` tool, use `--search` flag at the CLI; this skill is for the desktop app context where the flag is unavailable.