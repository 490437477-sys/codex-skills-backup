# 在新电脑同步 Codex Skills 指南

> 私有仓库：<https://github.com/490437477-sys/codex-skills-backup>
>
> 这份文档把整套 skills（5 内置 + 35 用户 + 3 插件）和 MCP 工具配置同步到一台新 Windows 电脑。

---

## 0. 前置软件（一次性安装）

| 软件 | 用途 | 下载 |
|------|------|------|
| Codex 桌面版 | 主体（自带 system skills 与 node_repl） | <https://chat.openai.com/codex> |
| Git for Windows | 拉仓库 | <https://git-scm.com/download/win> |
| GitHub CLI（`gh`） | 私有仓库认证 | <https://cli.github.com> |
| Python 3.10+ | 刷新 `MANIFEST.md`、运行部分 skill 脚本 | <https://www.python.org/downloads/> |
| PowerShell 5.1+ | 执行同步脚本（Windows 自带） | — |

> 可选：`Node.js` 和 `uvx`，仅当你之后要跑 `npx tavily-mcp` / `uvx minimax-mcp` 时需要。

---

## 1. 登录 GitHub（私有仓库要认证）

```powershell
gh auth login
# 选 GitHub.com → HTTPS → Yes (use my GitHub credentials for git) → Login with browser
```

成功后 `gh auth status` 会显示 `Logged in to github.com`。

---

## 2. 克隆仓库

放哪里都行，下面以 `Documents` 为例。

```powershell
cd $env:USERPROFILE\Documents
git clone https://github.com/490437477-sys/codex-skills-backup.git
cd codex-skills-backup
```

---

## 3. 看一眼仓库 vs 本地的差异

```powershell
pwsh ./scripts/diff.ps1
```

- 首次跑全是 `NEW`（仓库里有，本机 Codex 还没有），属于正常。
- 之后再跑就只显示真正的差异。

---

## 4. 一键还原 skills 到 Codex

```powershell
# 用户 skills + 插件 skills 都恢复
pwsh ./scripts/restore.ps1 -IncludePlugins
```

输出大概类似：

```
=== skills/user (from backup) ===
=== plugins/skills (from backup) ===
  - browser      -> ...\browser\26.609.30741\skills
  - chrome       -> ...\chrome\26.609.30741\skills
  - computer-use -> ...\computer-use\26.609.30741\skills
=== summary ===
  user skills : copied=35, removed=0
  plugins     : copied=3, removed=0
```

> **如果 Codex 版本不是 `26.609.30741`**：先看 `~/.codex/plugins/cache/openai-bundled/browser/` 下的版本号，再传：
>
> ```powershell
> pwsh ./scripts/restore.ps1 -IncludePlugins -PluginVersion <你的版本号>
> ```

> **如果想先预演不真改**：加 `-WhatIf`。

---

## 5. 配置 MCP 工具（API Key 不在仓库里，必须手填）

仓库里的 `tools/config.toml.sanitized` 已脱敏成 `***REDACTED***`，把它合并到本机 Codex 配置：

```powershell
notepad tools\config.toml.sanitized
notepad $env:USERPROFILE\.codex\config.toml
```

**操作步骤**

1. 复制 `config.toml.sanitized` 中所有 `[mcp_servers.*]` 段，粘到 `~/.codex/config.toml` 末尾。
2. 把每处 `***REDACTED***` 换成真实 API Key：
   - `TAVILY_API_KEY` → 在 <https://tavily.com> 拿
   - `MINIMAX_API_KEY` → MiniMax Coding Plan 那边拿（多处都要填）
3. `node_repl` 段里的 `CODEX_HOME`、`NODE_REPL_NODE_PATH` 等路径会随 Codex 安装自动生成，不用手动复制。
4. `[plugins."browser@openai-bundled"]`、`chrome@`、`computer-use@` 三个 `enabled = true` 段也加上。

---

## 6. 重启 Codex 并验证

关闭 Codex 应用 → 重新打开 → 在对话框输入：

```
列出你的技能
```

应当能看到完整的 system / user / plugin 三类、共 27 个左右 skills。

---

## 日常同步节奏

### 拉取仓库最新版到本机

```powershell
cd $env:USERPROFILE\Documents\codex-skills-backup
git pull origin main
pwsh ./scripts/diff.ps1                      # 看仓库改了啥
pwsh ./scripts/restore.ps1 -IncludePlugins  # 应用到本机
```

### 把本机新增/修改的 skill 推回仓库

```powershell
pwsh ./scripts/diff.ps1                      # 显示 NEW / MODIFIED
pwsh ./scripts/backup.ps1                    # 镜像到仓库 + 刷新 MANIFEST.md
git add -A
git commit -m "snapshot: add <skill-name>"
git push origin main
```

### 模拟丢失 → 一键恢复

```powershell
# 假装某个 skill 被误删
Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\skills\baiditu"
pwsh ./scripts/diff.ps1                      # → REMOVED: 1
pwsh ./scripts/restore.ps1                   # → copied=1
pwsh ./scripts/diff.ps1                      # → backup is in sync
```

---

## 文件结构速查

```
codex-skills-backup/
├── INSTALL.md                ← 本文件
├── README.md                 仓库总览（含还原指南细节）
├── MANIFEST.md               全部 skills 的 description（自动生成）
├── .gitignore
├── skills/
│   ├── system/   (5)         5 个内置 skill（仅作为参考；不要手工还原）
│   └── user/     (35)        市场/手写 skill，restore.ps1 会同步它们
├── plugins/skills/ (3)       browser / chrome / computer-use 插件 skills
├── tools/
│   ├── INDEX.md              工具索引
│   ├── built-in.md           内置工具清单
│   ├── mcp.md                MCP 工具清单（4 个 server，17 个工具）
│   ├── sub-agents.md         子代理工具
│   ├── config.toml.sanitized config.toml 备份（密钥脱敏）
│   └── _gen_manifest.py      重生成 MANIFEST.md 的脚本
└── scripts/
    ├── _lib.ps1              共享函数库
    ├── diff.ps1              对比 source vs 备份
    ├── backup.ps1            源 → 备份镜像
    └── restore.ps1           备份 → 源同步
```

---

## FAQ

**Q1：`skills/system/` 的 5 个内置 skill 怎么还原？**
重装/升级 Codex 时自动到位，**不要**手动复制。`restore.ps1` 也不会动这一类。

**Q2：插件版本号怎么查？**

```powershell
Get-ChildItem $env:USERPROFILE\.codex\plugins\cache\openai-bundled\browser
```

**Q3：脚本提示 `cannot be loaded because running scripts is disabled`？**

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

**Q4：每次推送都要输密码？**
说明凭证助手没生效，跑：

```powershell
git config --global credential.helper manager
gh auth setup-git
```

**Q5：仓库太大克隆慢？**
所有 skill 都是文本，整库 < 25 MB。如果真慢，可以先 `git clone --depth 1` 浅克隆，再 `git fetch --unshallow` 补全历史。

---

## 故障排查

| 现象 | 处理 |
|------|------|
| `restore.ps1` 报 `Source not found` | 确认在仓库根目录运行（含 `skills/` `scripts/` 同级） |
| Codex 启动后看不到新 skill | 完全退出 Codex（任务栏图标也右键退出）后重启 |
| 插件 skill 不生效 | 确认 `~/.codex/config.toml` 里 `[plugins."browser@openai-bundled"] enabled = true` 三段都有 |
| MCP 工具无响应 | 检查 `config.toml` 里 API Key 是否填对；`gh auth status` / `npx --version` / `uvx --version` 能否运行 |

---

> 维护：日常用 `scripts/backup.ps1` + `git push` 同步；**API Key 永远不要提交到仓库**（`config.toml.sanitized` 已经做过脱敏，请保持这个习惯）。
