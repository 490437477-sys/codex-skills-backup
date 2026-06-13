# MCP 工具清单

MCP（Model Context Protocol）服务器通过 `~/.codex/config.toml` 中的 `[mcp_servers.*]` 段配置。
下面的所有工具都来自当前 `config.toml.sanitized` 中启用的 4 个服务器。

## tavily（网页检索）

由 `npx -y tavily-mcp` 启动，需要 `TAVILY_API_KEY`。

| 工具名 | 用途 |
|--------|------|
| `mcp__tavily__tavily_search` | 网页搜索，支持时间范围/域名/主题过滤 |
| `mcp__tavily__tavily_research` | 深度调研，多源汇总 |
| `mcp__tavily__tavily_crawl` | 从入口 URL 递归抓取整站 |
| `mcp__tavily__tavily_extract` | 从指定 URL 列表提取原始内容 |
| `mcp__tavily__tavily_map` | 枚举网站 URL 结构 |

## minimax_coding_plan_mcp（搜索 + 视觉）

由 `npx -y minimax-coding-plan-mcp` 启动。

| 工具名 | 用途 |
|--------|------|
| `mcp__minimax_coding_plan_mcp__web_search` | Google 风格网页搜索 |
| `mcp__minimax_coding_plan_mcp__understand_image` | 用视觉模型分析图片内容 |

## minimax_mcp（媒体生成）

由 `uvx minimax-mcp` 启动。

| 工具名 | 用途 |
|--------|------|
| `mcp__minimax_mcp__text_to_image` | 文生图 |
| `mcp__minimax_mcp__generate_video` | 文生视频 / 图生视频（Director 模式支持镜头指令） |
| `mcp__minimax_mcp__query_video_generation` | 查询异步视频生成任务状态 |
| `mcp__minimax_mcp__text_to_audio` | 文本转语音（TTS） |
| `mcp__minimax_mcp__list_voices` | 列出可用语音 |
| `mcp__minimax_mcp__voice_design` | 根据描述生成新音色 |
| `mcp__minimax_mcp__voice_clone` | 用样本音频克隆音色 |
| `mcp__minimax_mcp__play_audio` | 播放本地音频文件 |
| `mcp__minimax_mcp__music_generation` | 由 prompt + 歌词生成音乐 |

## node_repl（持久 Node.js 内核）

由 Codex 自带的 `node_repl.exe` 启动，运行在用户主目录下的受信 Node 内核。
提供浏览器自动化（playwright/puppeteer）等所需的 ESM 顶层 await 环境。

| 工具名 | 用途 |
|--------|------|
| `mcp__node_repl__js` | 在持久 Node 内核中执行 JS（顶层 await） |
| `mcp__node_repl__js_reset` | 重置内核并清空所有绑定 |
| `mcp__node_repl__js_add_node_module_dir` | 把一个 `node_modules` 目录加入全局搜索路径 |

## 重装提示

1. 重新安装 Codex 应用会自动恢复 `node_repl`。
2. `tavily` / `minimax_*` 依赖 npm/uvx 与对应 API Key，需在新环境补全。
3. 完整可粘贴的配置见同目录 `config.toml.sanitized`，把 `***REDACTED***` 替换成实际密钥即可。
