# scripts/backup-and-sync.ps1
# One-call wrapper: diff -> backup -> commit -> push.
#
# Reuses the existing scripts from the backup repo:
#   scripts/diff.ps1       - compare source vs backup
#   scripts/backup.ps1     - mirror source into backup + refresh MANIFEST.md
#   scripts/push.ps1       - git push over SSH (HTTPS is blocked on this host)
#
# Usage:
#   pwsh ./backup-and-sync.ps1                    # full cycle
#   pwsh ./backup-and-sync.ps1 -DryRun            # diff + backup -WhatIf only, no commit/push
#   pwsh ./backup-and-sync.ps1 -SkipPush          # backup + commit, no push
#   pwsh ./backup-and-sync.ps1 -SkipBackup        # diff only
#   pwsh ./backup-and-sync.ps1 -Message 'wip refresh'   # custom commit msg

[CmdletBinding()]
param(
    [switch]$DryRun,
    [switch]$SkipDiff,
    [switch]$SkipBackup,
    [switch]$SkipCommit,
    [switch]$SkipPush,
    [string]$Message,
    [string]$BackupRoot = 'C:\Users\Administrator\Documents\技能备份'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if (-not (Test-Path $BackupRoot)) {
    throw "BackupRoot not found: $BackupRoot"
}

$diff    = Join-Path $BackupRoot 'scripts\diff.ps1'
$backup  = Join-Path $BackupRoot 'scripts\backup.ps1'
$push    = Join-Path $BackupRoot 'scripts\push.ps1'

foreach ($p in @($diff, $backup, $push)) {
    if (-not (Test-Path $p)) { throw "Required script missing: $p" }
}

function Step {
    param([string]$Name, [string]$Cmd)
    Write-Host ''
    Write-Host "=== $Name ===" -ForegroundColor Cyan
    Invoke-Expression $Cmd
    if ($LASTEXITCODE -ne 0) { throw "Step '$Name' failed (exit $LASTEXITCODE)" }
}

# --- 1. diff (preview) --------------------------------------------------
if (-not $SkipDiff) {
    if ($DryRun) {
        Step 'diff (dry-run)' "pwsh -NoProfile -File '$diff'"
    } else {
        Step 'diff' "pwsh -NoProfile -File '$diff'"
    }
}

# --- 2. backup (mirror source -> repo) ----------------------------------
if (-not $SkipBackup) {
    if ($DryRun) {
        Write-Host ''
        Write-Host '=== backup (whatif) ===' -ForegroundColor Yellow
        pwsh -NoProfile -File $backup -WhatIf
    } else {
        Step 'backup' "pwsh -NoProfile -File '$backup'"
    }
}

# --- 3. commit ----------------------------------------------------------
if (-not $SkipCommit -and -not $DryRun) {
    Write-Host ''
    Write-Host '=== stage ===' -ForegroundColor Cyan
    Set-Location $BackupRoot
    git add -A
    $staged = git status --porcelain
    if (-not $staged) {
        Write-Host '  (no changes after backup; nothing to commit)' -ForegroundColor DarkGray
    } else {
        $msg = if ($Message) { $Message } else {
            $today = Get-Date -Format 'yyyy-MM-dd'
            "snapshot: skills + plugin skills backup ($today)"
        }
        Write-Host "=== commit: $msg ===" -ForegroundColor Cyan
        $email = (git config user.email) 2>$null
        $name  = (git config user.name)  2>$null
        $args = @('-c', 'user.email=codex@local', '-c', 'user.name=codex', 'commit', '-m', $msg)
        if ($email -and $name) { $args = @('commit', '-m', $msg) }
        git @args
        if ($LASTEXITCODE -ne 0) { throw 'git commit failed' }
    }
}

# --- 4. push ------------------------------------------------------------
if (-not $SkipPush -and -not $DryRun) {
    Step 'push' "pwsh -NoProfile -File '$push'"
}

Write-Host ''
Write-Host 'Backup cycle complete.' -ForegroundColor Green