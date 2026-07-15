---
name: backup-and-sync-skills-backup
description: 当用户要求把本地 Codex 的全部 skills、插件 skills 备份并同步推送到 GitHub 远端仓库（默认 https://github.com/490437477-sys/codex-skills-backup.git）时使用。涵盖三个动作：(1) diff — 对比 ~/.codex/skills、~/.agents/skills、~/.codex/plugins/cache/openai-bundled 与本地仓库，列出 NEW/REMOVED/MODIFIED；(2) backup — 把本地镜像到仓库并重生成 MANIFEST.md；(3) push — 提交并推送到 GitHub；本机到 443 直连 GitHub 不通，会自动切到 SSH 推送（git@github.com:22）后再切回 HTTPS URL。可处理新增的 visualize 等插件 skill、自动处理 working tree 不干净、自动 preflight 检查 SSH key。
---

# Backup and Sync Codex Skills to GitHub

Back up the local Codex skills + plugin skills, generate a manifest, commit, and
push to `https://github.com/490437477-sys/codex-skills-backup.git`.


This machine can reach `github.com:22` (SSH) but not `:443` (HTTPS) reliably, so
this skill always switches the remote URL to SSH for the push, then restores the
HTTPS URL afterwards.

## When to use

Trigger when the user says any of:
- "备份到远端" / "把本地技能备份上去" / "push the skills backup"
- "刷新备份并推 GitHub" / "snapshot and push"
- "diff 一下当前 skills 状态" / "看看本地和仓库差异"

Do **not** trigger for: ad-hoc individual skill installs, `skill-installer`-style
plugin adds, or repo edits unrelated to the backup snapshot.

## Inputs

| Input          | Default                                     | Notes                                                          |
| -------------- | ------------------------------------------- | -------------------------------------------------------------- |
| `BackupRoot`   | `C:\Users\Administrator\Documents\技能备份`  | The local mirror repo. Override only if the repo moved.        |
| `RemoteHttps`  | `https://github.com/490437477-sys/codex-skills-backup.git` | Pinned remote (we switch to SSH on push). |
| `RemoteSsh`    | `git@github.com:490437477-sys/codex-skills-backup.git`     | URL used for the actual push (HTTPS is blocked on this host). |
| `Branch`       | `main`                                       | Target branch.                                                 |
| `Message`      | `snapshot: skills + plugin skills backup (UTC yyyy-MM-dd)` | Commit message template.                          |
| `DryRun`       | `false`                                      | If true, only runs preflight + diff; no copy/commit/push.      |

## Workflow

Always run from `BackupRoot`. Follow the steps in order; do not skip preflight.

### 1. Preflight
- `git -C $BackupRoot rev-parse --is-inside-work-tree` → must succeed.
- `Test-Path $BackupRoot\scripts\backup.ps1` and `…\push.ps1` → must succeed.
- `Test-Path $env:USERPROFILE\.ssh\id_ed25519.pub` → must succeed (GitHub auth via SSH).
- TCP probe `github.com:22` with `Test-NetConnection -Port 22` → must succeed.
  - If 22 is also blocked, stop and ask the user to provide an SSH-over-443 or
    HTTPS proxy.

### 2. Diff (preview)
Run:
```powershell
pwsh $BackupRoot\scripts\diff.ps1
```
Parse the `[MODIFIED]` / `[NEW]` / `[REMOVED]` blocks. If everything is `0`,
print "backup is in sync with source" and stop (no-op).

### 3. Backup (mirror local → repo)
Run:
```powershell
pwsh $BackupRoot\scripts\backup.ps1
```
This:
- Copies `~/.codex/skills/*` → `skills/system/` and `skills/user/r0/`
- Copies `~/.agents/skills/*` → `skills/user/r1/` (deduped against r0 by name)
- Copies `~/.codex/plugins/cache/openai-bundled/<plugin>/<ver>/skills/*`
  → `plugins/skills/<plugin>/`
- Regenerates `MANIFEST.md` from `tools/_gen_manifest.py`.

### 4. Commit
- Read the diff. Aggregate into one commit per push cycle (do not split by skill).
- Stage everything: `git -C $BackupRoot add -A`
- Commit message template:
  ```
  snapshot: skills + plugin skills backup (yyyy-MM-dd)

  - <bullet summarizing new skills, if any>
  - <bullet summarizing refreshed plugin skills, if any>
  - regenerate MANIFEST.md
  ```
  Use `git -C $BackupRoot -c user.email='codex@local' -c user.name='codex' commit`
  if no global git identity is configured.

### 5. Push over SSH, then restore HTTPS URL
Run:
```powershell
pwsh $BackupRoot\scripts\push.ps1
```
The script:
1. Switches `origin` → SSH URL.
2. Pushes to `main`.
3. Restores `origin` → HTTPS URL in a `finally` block.

### 6. Verify
Run:
```powershell
git -C $BackupRoot ls-remote --heads origin
git -C $BackupRoot log --oneline -1 origin/main
```
The `log` output must show the new commit hash on `origin/main`. If it does
not, fail loudly — do not assume success.

## Edge cases

- **Working tree dirty before backup.** Run backup first to surface new files,
  then stage+commit. Never `git stash` and lose user work.
- **No upstream.** Tell the user to run `git push -u origin main` manually once.
- **New plugin added.** `backup.ps1` auto-discovers `openai-bundled/<plugin>/<ver>/skills/`.
  Highlight the new plugin in the commit message bullet.
- **`__pycache__` / `.DS_Store` drift.** `_lib.ps1` already filters these — trust it.
- **Port 22 also blocked.** Do not fall back to a different host. Ask for proxy.

## Output contract

After a successful run, emit exactly these git directives on their own lines:

```
::git-stage{cwd="<BackupRoot>"}
::git-commit{cwd="<BackupRoot>"}
::git-push{cwd="<BackupRoot>" branch="<Branch>"}
```

## Resource layout

```
backup-and-sync-skills-backup/
├── SKILL.md                  # this file
├── agents/openai.yaml        # Codex chip metadata (display label + summary)
└── scripts/
    └── backup-and-sync.ps1   # one-call wrapper: preflight → diff → backup → commit → push
```

The wrapper script `scripts/backup-and-sync.ps1` is the canonical entry point.
When in doubt, call it with `-DryRun` first.


