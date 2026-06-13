# 工具索引（Tools Index）

本目录汇总本次备份涉及到的全部"工具"——包括内建工具、MCP 工具和子代理能力。

| 文件 | 内容 |
|------|------|
| `built-in.md` | Codex 应用自带工具（shell、apply_patch、update_plan 等） |
| `mcp.md` | 4 个 MCP 服务器提供的全部工具（tavily、minimax_coding_plan_mcp、minimax_mcp、node_repl） |
| `sub-agents.md` | `multi_agent_v1__*` 子代理派发/通信工具 |
| `config.toml.sanitized` | 完整 `~/.codex/config.toml`，密钥已脱敏为 `***REDACTED***` |

## 重装优先级

1. **必须**：重装 Codex 应用 → 自动恢复 `built-in.md`、`sub-agents.md`、`mcp.md` 中的 `node_repl`
2. **可选**：按需补齐 `tavily` / `minimax_*` 三个 MCP 服务器（复制 `config.toml.sanitized` 并填入新密钥）
3. **默认开启**：插件 `browser` / `chrome` / `computer-use`（在 `config.toml.sanitized` 已启用）
