---
name: sync-skills-backup-from-remote
description: 当用户要求把远端 GitHub 仓库（默认 https://github.com/490437477-sys/codex-skills-backup.git）的 skills 与插件 skills 拉回本地并装到 Codex 时使用。动作分两步：(1) fetch + fast-forward pull 同步本地仓库 `C:\Users\Administrator\Documents\技能备份`；(2) 调 scripts/restore.ps1 把 `skills/user/*` 镜像到 `~/.codex/skills/`，把 `plugins/skills/*` 镜像到 `~/.codex/plugins/cache/openai-bundled/<plugin>/<detected-version>/skills/`。自动探测当前 Codex 实际安装的插件版本（默认 26.707.72221），处理 working tree 不干净自动 stash、SSH 22 不通时切换 HTTPS。适用场景："从远端拉最新 skills"、"在新机器上恢复"、"重装后批量恢复"。
---

# Sync Skills Backup From GitHub (Remote -> Local)

Pull the latest Codex skills + plugin skills from GitHub into the local mirror
repo, then mirror them back into Codex's live `~/.codex/` trees.

This is the inverse of `backup-and-sync-skills-backup`. Use it on:
- A freshly reinstalled box.
- A new machine that needs the same skill set.
- Any time the user wants the local Codex to match the GitHub snapshot.

## When to use

Trigger when the user says any of:
- "从远端拉回来" / "从仓库更新本地 skills" / "重新装一遍" / "restore from backup"
- "在新机器上恢复" / "重装后批量恢复" / "拉最新版本"
- "把 GitHub 上的 skills 同步到 Codex"

Do **not** trigger for: ad-hoc individual skill installs, edits inside a single
skill, or pushing local changes upstream (use `backup-and-sync-skills-backup`).

## Inputs

| Input            | Default                                                  | Notes                                                          |
| ---------------- | -------------------------------------------------------- | -------------------------------------------------------------- |
| `BackupRoot`     | `C:\Users\Administrator\Documents\技能备份`               | Local mirror repo. Must contain `scripts/{diff,backup,restore}.ps1`. |
| `RemoteHttps`    | `https://github.com/490437477-sys/codex-skills-backup.git` | Read URL; used when SSH is also blocked.                       |
| `RemoteSsh`      | `git@github.com:490437477-sys/codex-skills-backup.git`     | Pinned remote for fetch (HTTPS may be blocked on this host).   |
| `Branch`         | `main`                                                    |                                                                |
| `IncludePlugins` | `true`                                                    | Restore `plugins/skills/*` to `~/.codex/plugins/cache/openai-bundled/`. |
| `PluginVersion`  | auto-detect, fallback `26.707.72221`                       | Plugin cache version dir. Per-plugin override allowed.         |
| `DryRun`         | `false`                                                   | If true, only runs git fetch + read-only diff; never writes.    |

## Workflow

Always run from `BackupRoot`. Follow the steps in order.

### 1. Preflight
- `git -C $BackupRoot rev-parse --is-inside-work-tree` → must succeed.
- `Test-Path $BackupRoot\scripts\restore.ps1` → must succeed.
- `Test-Path $env:USERPROFILE\.codex\skills` → must succeed.
- TCP probe: `github.com:22` and `github.com:443` must respond (we'll prefer
  SSH if both work, matching `scripts/push.ps1`).
- Plugin detection (only if `-IncludePlugins`):
  ```powershell
  pwsh -NoProfile -Command "
      $cache = Join-Path $env:USERPROFILE '.codex\plugins\cache\openai-bundled'
      if (Test-Path $cache) {
          Get-ChildItem -Force $cache -Directory | ForEach-Object {
              $ver = Get-ChildItem -Force $_.FullName -Directory |
                  Where-Object { $_.Name -match '^[0-9]+\.[0-9]+\.[0-9]+$' } |
                  Select-Object -ExpandProperty Name -First 1
              '{0}:{1}' -f $_.Name, ($ver ?? 'unknown')
          }
      }
  "
  ```
  Use the detected version for each plugin's `restore.ps1` call. Fall back to
  `26.707.72221` when detection fails.

### 2. Fetch + pull (update local mirror)
- `git -C $BackupRoot fetch origin`
- If working tree is dirty:
  - Try `git -C $BackupRoot stash push -u -m "sync-from-remote autosave"`.
  - After the restore step, `git stash pop` to restore user edits.
  - If `stash push` reports untracked-only-no-conflict, that is fine; proceed.
- `git -C $BackupRoot pull --ff-only origin main`
  - If `--ff-only` fails (non-fast-forward), do **not** force-push. Surface
    the divergence to the user and stop. Likely cause: someone pushed a
    manual commit to `main`. Suggest `git pull --rebase` only after the user
    confirms.

### 3. Restore Codex skills to live locations
Run `scripts/restore.ps1`:
```powershell
$pluginArgs = @()
foreach ($plugin in @('browser','chrome','computer-use','visualize')) {
    $ver = $detectedVersions[$plugin] ?? $PluginVersion
    # restore.ps1 takes a single PluginVersion; per-plugin override requires
    # running once per (plugin,version) pair.
}
pwsh -NoProfile -File "$BackupRoot\scripts\restore.ps1" -IncludePlugins -PluginVersion $PluginVersion -WhatIf:$DryRun
```
Note: `restore.ps1` accepts a single `PluginVersion`. If the detected versions
diverge (e.g. plugins landed at different releases), restore each plugin
separately using direct `Copy-Item -Recurse -Force` from
`plugins/skills/<plugin>/*` to `~/.codex/plugins/cache/openai-bundled/<plugin>/<ver>/skills/`.

### 4. Verify
- Re-run `scripts/diff.ps1`; expected output "backup is in sync with source"
  for the restored side (the repo now drives the live tree).
- `Test-Path "$env:USERPROFILE\.codex\skills\<each-restored-skill>\SKILL.md"` → True for every restored skill.
- Show the user the final summary: which skills restored, which plugins installed, which file counts changed.

## Edge cases

- **SSH both blocked (22 + 443).** Do not invent a proxy. Ask the user.
- **Working tree dirty + stash conflicts.** Run `git stash list` and surface
  the conflict. Do not silently drop user changes.
- **Plugin versions diverge.** Restore per-plugin so the version dir matches
  what Codex currently has cached. Cross-check by listing
  `~/.codex/plugins/cache/openai-bundled/<plugin>/` before issuing each restore.
- **Plugin not yet cached.** `restore.ps1` will create the `<ver>/skills/`
  dir on demand; Codex picks it up next launch.
- **System skills (`skills/system/`).** NOT restored by this skill. Tell the
  user to use Codex's built-in "Reset bundled skills" action if a system
  marker is missing.
- **MCP keys.** Not handled here. Mention `tools/config.toml.sanitized`
  once at the end with instructions to fill real keys.

## Output contract

After a successful run, do not emit any git directives (this skill pulls,
not pushes). End the run with:
- A list of restored user skills.
- A list of restored plugin skills + the plugin version dir used.
- The new HEAD commit hash on the local mirror.
- A reminder about MCP config if `IncludePlugins` was true and MCP servers
  changed.

## Resource layout

```
sync-skills-backup-from-remote/
├── SKILL.md                              # this file
├── agents/openai.yaml                    # Codex chip metadata
└── scripts/sync-from-remote.ps1          # one-call wrapper: preflight -> pull -> restore -> verify
```

When in doubt, call `scripts/sync-from-remote.ps1 -DryRun` first.