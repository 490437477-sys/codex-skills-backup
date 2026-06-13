# Codex 技能与工具备份

把当前 Codex 环境里所有可重装的 **skills**、**plugin skills** 与 **工具配置** 备份到本目录，便于在新机器/重装后一键还原。

> 备份时间：' + ([DateTime]::Now.ToString('yyyy-MM-dd HH:mm:ss')) + '（Asia/Shanghai）
> 备份源：`$env:USERPROFILE\.codex\skills`、`$env:USERPROFILE\.codex\plugins\cache\openai-bundled\*\skills`、`$env:USERPROFILE\.codex\config.toml`

## 目录结构

```
技能备份/
├── README.md                       # 本文件
├── MANIFEST.md                     # 全部 skills 清单（含 description）
├── skills/
│   ├── system/                     # 5 个 Codex 内置 skills
│   └── user/                       # 19 个用户/市场安装的 skills
├── plugins/
│   └── skills/                     # 3 个插件贡献的 skills（browser/chrome/computer-use）
└── tools/
    ├── INDEX.md                    # 工具索引
    ├── built-in.md                 # 内置工具清单
    ├── mcp.md                      # MCP 工具清单
    ├── sub-agents.md               # 子代理工具清单
    ├── config.toml.sanitized       # config.toml 备份（密钥已脱敏）
    ├── _gen_manifest.py            # 重新生成 MANIFEST.md 的脚本
    └── _gen_manifest.ps1           # 同上 PowerShell 版本（已废弃）
```

## 数量统计

| 类别 | 数量 |
|------|------|
| 内置 skills（`skills/system/`） | 5 |
| 用户 skills（`skills/user/`） | 19 |
| 插件 skills（`plugins/skills/`） | 3 |
| **合计** | **27** |
| 内置工具 | 10+ |
| MCP 工具 | 17（4 个 server） |
| 子代理工具 | 5 |

详细列表见 `MANIFEST.md` 与 `tools/INDEX.md`。

## 一键重装指南

### 1) 还原内置工具与子代理能力

无需任何操作——重装 Codex 应用后自动恢复。

### 2) 还原用户 skills

把 `skills/user/` 下的每个 skill 目录整体复制到新机器的 `$env:USERPROFILE\.codex\skills\<skill-name>\`：

```powershell
Copy-Item -Recurse -Force .\skills\user\* "$env:USERPROFILE\.codex\skills\"
```

> 注意：原环境下 `doubao-shengtu/` 是空目录，重装后保留即可，不影响其他 skills。

### 3) 还原内置 skills（`skills/system/`）

`system/` 下的 5 个 skills 是 Codex 内置组件，**不要手动覆盖**。如果重装后缺失，可执行：

```powershell
# 让 Codex 在启动时自动恢复系统 skills 标记
# 通常在 Codex 桌面端 "Settings → Reset bundled skills" 一键完成
```

### 4) 还原插件 skills

把 `plugins/skills/` 下的三个插件目录放回 `~/.codex/plugins/cache/<marketplace>/<plugin>/<version>/skills/`：

```powershell
$ver = "26.609.30741"   # 与当前 Codex 版本对齐
$dst = "$env:USERPROFILE\.codex\plugins\cache\openai-bundled"
Copy-Item -Recurse -Force .\plugins\skills\browser        "$dst\browser\$ver\skills\"
Copy-Item -Recurse -Force .\plugins\skills\chrome         "$dst\chrome\$ver\skills\"
Copy-Item -Recurse -Force .\plugins\skills\computer-use   "$dst\computer-use\$ver\skills\"
```

同时确保 `config.toml` 中启用了这三个插件：

```toml
[plugins."browser@openai-bundled"]
enabled = true

[plugins."chrome@openai-bundled"]
enabled = true

[plugins."computer-use@openai-bundled"]
enabled = true
```

### 5) 还原 MCP 工具

把 `tools/config.toml.sanitized` 中的 `[mcp_servers.*]` 段合并到新机器的 `$env:USERPROFILE\.codex\config.toml`，然后**手动填入真实 API Key**：

- `TAVILY_API_KEY` —— 注册 https://tavily.com 获取
- `MINIMAX_API_KEY` / `MINIMAX_API_HOST` —— 由 MiniMax Coding Plan 提供
- `node_repl` 段（CODEX_HOME、NODE_REPL_NODE_PATH 等）应保持与本机 Codex 安装路径一致

### 6) 验证

启动 Codex 后运行：

```text
列出你的技能
```

应能完整看到 24 个 skills + 3 个插件 skills。

## 维护

- 修改 skills 后，用 `python tools/_gen_manifest.py` 重新生成 `MANIFEST.md`
- 新增 MCP server 后，把脱敏后的 `[mcp_servers.*]` 段补到 `tools/config.toml.sanitized`

---

## 日常维护（`scripts/` 工作流）

项目根目录的 `scripts/` 下有三个 PowerShell 脚本，可重复执行以保持备份与安装同步：

| 脚本 | 作用 |
|------|------|
| `scripts/diff.ps1` | 对比 `~/.codex/skills/` 与本仓库，列出 `NEW` / `REMOVED` / `MODIFIED` |
| `scripts/backup.ps1` | 把 `~/.codex/skills/` 镜像到本仓库，并刷新 `MANIFEST.md` |
| `scripts/restore.ps1` | 把本仓库镜像回 `~/.codex/skills/`，可选 `-IncludePlugins` |

三个脚本支持 `-WhatIf` 预览；都自动跳过 `__pycache__`、`.DS_Store`、`Thumbs.db`、`.system` 这类杂物。

### 推荐工作流

```powershell
# 1. 查看本地与备份差异
pwsh ./scripts/diff.ps1

# 2. 把本地新增/修改的 skills 同步进仓库
pwsh ./scripts/backup.ps1                  # 直接生效
pwsh ./scripts/backup.ps1 -WhatIf         # 仅预览

# 3. 仓库里改了 skill 文件 → 推回本地
pwsh ./scripts/restore.ps1                # 用户 skill
pwsh ./scripts/restore.ps1 -IncludePlugins # 用户 + 插件 skill

# 4. 新机器 / 重装后一键还原
pwsh ./scripts/restore.ps1 -IncludePlugins
# 然后按提示把 tools/config.toml.sanitized 合并到 ~/.codex/config.toml
```

### 端到端验证（已实测通过）

```powershell
# 模拟丢一个 skill
Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\skills\amazon-a-plus-content"
pwsh ./scripts/diff.ps1                   # → REMOVED: 1
pwsh ./scripts/restore.ps1                # → copied=1, removed=0
Test-Path "$env:USERPROFILE\.codex\skills\amazon-a-plus-content\SKILL.md"  # True
pwsh ./scripts/diff.ps1                   # → backup is in sync with source
```

### 写入 git 的建议

```powershell
git add scripts/ tools/ skills/ plugins/ MANIFEST.md README.md
git commit -m "snapshot: skills + plugin skills backup"
```

> `scripts/_lib.ps1` 是其他三个脚本的共享函数库（含指纹计算、对比、镜像），单独修改即可影响全部脚本。
