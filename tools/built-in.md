# 内置工具（Built-in）

这些工具随 Codex 应用内置，无需额外安装或配置。

| 工具名 | 用途 |
|--------|------|
| `shell_command` | 在 PowerShell 中执行命令（带工作目录、超时、沙箱） |
| `apply_patch` | 编辑本地文件（创建/修改/删除），唯一允许的补丁入口 |
| `update_plan` | 创建/更新多步骤任务计划 |
| `view_image` | 查看本地图片文件 |
| `web_search` | 自由格式网页搜索 |
| `request_user_input` | 在 Plan 模式下向用户询问 1-3 个问题 |
| `get_goal` / `create_goal` / `update_goal` | 目标（goal）状态管理 |
| `list_mcp_resources` / `list_mcp_resource_templates` / `read_mcp_resource` | 浏览/读取 MCP 服务器暴露的资源 |
| `codex_app__load_workspace_dependencies` | 加载 sheets/slides/documents 的运行时与依赖 |
| `codex_app__read_thread_terminal` | 读取 Codex 桌面线程的当前终端输出 |

## 重装提示

内置工具不需要备份文件——它们随 Codex 安装包自带。重新安装 Codex 应用即可恢复。
