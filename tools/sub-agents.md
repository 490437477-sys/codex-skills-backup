# 子代理工具（Sub-agents）

通过 `multi_agent_v1__*` 命名空间调用，用于派发并发任务或长时运行的子代理。

| 工具名 | 用途 |
|--------|------|
| `multi_agent_v1__spawn_agent` | 派生新子代理（agent_type 可选 default / explorer / worker） |
| `multi_agent_v1__send_input` | 向已派生的子代理发送消息（可 interrupt） |
| `multi_agent_v1__wait_agent` | 等待子代理达到终态 |
| `multi_agent_v1__close_agent` | 关闭子代理 |
| `multi_agent_v1__resume_agent` | 重新打开之前关闭的子代理 |

## 子代理类型

- **default**：通用代理，继承父模型
- **explorer**：快速只读代码库问答（适合派多个并行探查）
- **worker**：执行/生产型任务，适合有明确写文件范围的代码改动

## 重装提示

子代理工具是 Codex 桌面版的内建能力，无需额外安装。
