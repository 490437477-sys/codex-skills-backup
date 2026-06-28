---
name: search-routing
description: 工具路由手册。在 Codex 会话中需要执行网络搜索、抓取网页、深度研究、读取图片这四类任务时自动调用本 skill：按"国内/国外"语境和"普通/深度"层级，在 mmx (MiniMax CLI) 与 Tavily MCP 之间选择首选与备选工具，并附调用示例。Use this skill whenever a task involves web search, URL content extraction, deep multi-source research, or local image understanding, so the right tool is picked first time.
---

# Search & Fetch Routing

本 skill 是一张**工具选路表**。当任务落到「搜索 / 抓取 / 深度研究 / 看图」四类时，按下表选**首选**；首选失败、超时或结果不达标时再切**备选**。

> 「国内 / 国外」指**搜索意图的目标市场与资料语种**，不是工具的部署地。

## 路由表

| 任务 | 首选 | 备选 |
| --- | --- | --- |
| 国内普通搜索 | `mmx search query --q "..."` | `mcp__tavily__tavily_search` |
| 国外搜索 | `mcp__tavily__tavily_search` | `mmx search query --q "..." --region global` |
| 国内深度汇总 | `mcp__tavily__tavily_research` | `mmx search query`（多跑几次人工合并） |
| 抓 URL 内容 | `mcp__tavily__tavily_extract` | `Invoke-WebRequest` |
| 图片理解 | `mmx vision describe --image <path>` | `mcp__minimax_coding_plan_mcp__understand_image` |

## 选路逻辑（速记）

- **语种 + 目标市场 = 关键词**：中文 + 国内资料 → 首选 mmx；英文 / 跨语种 + 海外资料 → 首选 Tavily。
- **普通 vs 深度**：单点问题 → 单次 search；需要多源汇总、报告式输出 → research。
- **抓取 vs 渲染**：拿到 URL 后想读内容 → extract；想拿原始 HTML 自行解析 → `Invoke-WebRequest`。
- **看图 = 本地优先**：本地路径直接喂 `mmx vision describe`；远端 URL 或 mmx 不可用时切 `understand_image`。

## 调用示例

**国内普通搜索**
```bash
mmx search query --q "2026 年新能源汽车补贴政策"
```

**国外搜索**
```python
mcp__tavily__tavily_search(
    query="latest EU AI Act enforcement guidelines 2026",
    max_results=10,
    search_depth="advanced"
)
```

**国内深度汇总**
```python
mcp__tavily__tavily_research(
    input="2026 年中国跨境电商政策变化与平台合规要点",
    model="pro"
)
```

**抓 URL 内容**
```python
mcp__tavily__tavily_extract(
    urls=["https://example.com/article"],
    format="markdown"
)
```

**图片理解（本地）**
```bash
mmx vision describe --image "C:\path\to\image.png"
```

**图片理解（远端 / 备选）**
```python
mcp__minimax_coding_plan_mcp__understand_image(
    image_source="https://example.com/photo.jpg",
    prompt="描述这张图片中的产品外观与材质"
)
```

## 失败回退顺序

1. 首选工具报错 / 超时 / 返回空结果。
2. 切到本行「备选」。
3. 备选仍失败：把 URL 或关键词交给用户确认，再决定人工补查或换路径。
4. 不在表内的工具（`web_search`、浏览器自动化等）仅在表内两条全失败时临时使用，并在最终回复中说明原因。

## 注意事项

- 不要在「国内」语境下硬走 Tavily 默认通道——会拉到海外索引。带 `--region global` 的 mmx 也只用于备用兜底。
- 深度汇总 `tavily_research` 是「单次出报告」的省事选择，但走全球检索；对强国内语境的主题，可能不如「多次 mmx search + 人工合并」覆盖好。
- 抓 URL 时若目标是动态渲染页（JS 重度），`tavily_extract` 仍优于 `Invoke-WebRequest`；后者留给「我要原始 HTML 自己解析」的场景。
