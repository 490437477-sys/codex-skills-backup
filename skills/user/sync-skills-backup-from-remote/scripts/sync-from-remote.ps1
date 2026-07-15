# scripts/sync-from-remote.ps1
# Pull codex-skills-backup from GitHub into the local mirror, then restore
# Codex skills + plugin skills to ~/.codex/ live trees.
#
# Usage:
#   pwsh ./sync-from-remote.ps1                       # full cycle
#   pwsh ./sync-from-remote.ps1 -DryRun               # fetch + restore -WhatIf only
#   pwsh ./sync-from-remote.ps1 -NoPull               # local mirror already up to date
#   pwsh ./sync-from-remote.ps1 -NoRestore            # only refresh the mirror repo
#   pwsh ./sync-from-remote.ps1 -SkipPlugins          # user skills only
#   pwsh ./sync-from-remote.ps1 -PluginVersion 26.707.72221

[CmdletBinding()]
param(
    [switch]$DryRun,
    [switch]$NoPull,
    [switch]$NoRestore,
    [switch]$SkipPlugins,
    [string]$PluginVersion = '26.707.72221',
    [string]$BackupRoot = 'C:\Users\Administrator\Documents\技能备份'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if (-not (Test-Path $BackupRoot)) {
    throw "BackupRoot not found: $BackupRoot"
}

$restore = Join-Path $BackupRoot 'scripts\restore.ps1'
if (-not (Test-Path $restore)) { throw "Required script missing: $restore" }

function Step {
    param([string]$Name, [string]$Cmd)
    Write-Host ''
    Write-Host "=== $Name ===" -ForegroundColor Cyan
    Invoke-Expression $Cmd
    if ($LASTEXITCODE -ne 0) { throw "Step '$Name' failed (exit $LASTEXITCODE)" }
}

Set-Location $BackupRoot

# --- 1. preflight ------------------------------------------------------
Write-Host ''
Write-Host '=== preflight ===' -ForegroundColor Cyan

if (-not (git rev-parse --is-inside-work-tree 2>$null)) {
    throw "Not a git repository: $BackupRoot"
}

$skillsLive = Join-Path $env:USERPROFILE '.codex\skills'
if (-not (Test-Path $skillsLive)) {
    throw "Codex skills dir missing: $skillsLive. Is Codex installed?"
}

# Probe SSH first, fall back to HTTPS for fetch.
$t22 = (Test-NetConnection -ComputerName github.com -Port 22 -InformationLevel Quiet -WarningAction SilentlyContinue)
if ($t22) {
    Write-Host '  ssh (22): OK' -ForegroundColor DarkGray
    $useSsh = $true
} else {
    Write-Host '  ssh (22): BLOCKED' -ForegroundColor DarkYellow
    $useSsh = $false
}

# --- 2. fetch + pull ---------------------------------------------------
if (-not $NoPull) {
    $orig = (git remote get-url origin).Trim()
    if ($useSsh -and $orig.StartsWith('https://')) {
        $sshUrl = $orig -replace '^https://github\.com/', 'git@github.com:'
        Write-Host "  remote -> $sshUrl (for fetch)"
        git remote set-url origin $sshUrl
    } elseif (-not $useSsh -and $orig.StartsWith('git@')) {
        $httpsUrl = $orig -replace '^git@github\.com:', 'https://github.com/'
        Write-Host "  remote -> $httpsUrl (for fetch)"
        git remote set-url origin $httpsUrl
    } else {
        Write-Host "  remote : $orig"
    }

    # Stash if dirty
    $dirty = git status --porcelain
    $stashed = $false
    if ($dirty) {
        Write-Host '  working tree dirty; stashing user edits...'
        if ($DryRun) {
            Write-Host '    (dry-run: would stash)' -ForegroundColor Yellow
        } else {
            git stash push -u -m 'sync-from-remote autosave' | Out-Null
            $stashed = $LASTEXITCODE -eq 0
        }
    }

    if ($DryRun) {
        Step 'fetch (dry-run)' 'git fetch --dry-run'
    } else {
        Step 'fetch' 'git fetch origin'
        Step 'pull --ff-only' 'git pull --ff-only origin main'
    }

    # Restore stashed changes if any
    if ($stashed -and -not $DryRun) {
        Write-Host '  restoring stashed changes...'
        git stash pop | Out-Null
    }
}

# --- 3. detect plugin versions ----------------------------------------
if (-not $SkipPlugins) {
    Write-Host ''
    Write-Host '=== detect plugin versions ===' -ForegroundColor Cyan
    $cache = Join-Path $env:USERPROFILE '.codex\plugins\cache\openai-bundled'
    if (Test-Path $cache) {
        $detected = @{}
        Get-ChildItem -Force $cache -Directory | ForEach-Object {
            $ver = Get-ChildItem -Force $_.FullName -Directory |
                Where-Object { $_.Name -match '^[0-9]+\.[0-9]+\.[0-9]+$' } |
                Select-Object -ExpandProperty Name -First 1
            $detected[$_.Name] = ($ver ?? $PluginVersion)
        }
        $detected.GetEnumerator() | Sort-Object Key | ForEach-Object {
            Write-Host ('  {0,-15} -> {1}' -f $_.Key, $_.Value) -ForegroundColor DarkGray
        }

        # If any plugin deviated from the default, restore per-plugin.
        $diverge = $detected.Values | Where-Object { $_ -ne $PluginVersion } | Select-Object -First 1
        if ($diverge) {
            Write-Host '  detected versions diverge from default; restoring per-plugin...' -ForegroundColor DarkYellow
            if ($DryRun) {
                Write-Host "    (dry-run: would iterate per-plugin)" -ForegroundColor Yellow
            } else {
                foreach ($p in $detected.Keys) {
                    $src = Join-Path $BackupRoot ('plugins\skills\' + $p)
                    if (-not (Test-Path $src)) { continue }
                    $dst = Join-Path $cache ('{0}\{1}\skills' -f $p, $detected[$p])
                    Write-Host ('  - {0} -> {1}' -f $p, $dst) -ForegroundColor DarkCyan
                    if (-not (Test-Path $dst)) { New-Item -ItemType Directory -Force -Path $dst | Out-Null }
                    Copy-Item -Recurse -Force (Join-Path $src '*') $dst
                }
            }
        }
    } else {
        Write-Host "  no plugin cache at $cache; skipping plugin restore" -ForegroundColor DarkYellow
    }
}

# --- 4. restore user skills (+ plugins via restore.ps1) --------------
if (-not $NoRestore) {
    $pwshArgs = @('-NoProfile', '-File', $restore)
    if ($DryRun) { $pwshArgs += '-WhatIf' }
    if (-not $SkipPlugins) {
        $pwshArgs += '-IncludePlugins'
        $pwshArgs += @('-PluginVersion', $PluginVersion)
    }
    Step 'restore' "pwsh $($pwshArgs -join ' ')"
}

# --- 5. verify --------------------------------------------------------
Write-Host ''
Write-Host '=== verify ===' -ForegroundColor Cyan
if ($NoPull) {
    Write-Host '  (skipped: pull was skipped)' -ForegroundColor DarkGray
} elseif ($DryRun) {
    Write-Host '  (skipped: dry-run)' -ForegroundColor DarkGray
} else {
    $log = git log --oneline -1 origin/main
    Write-Host "  origin/main HEAD: $log" -ForegroundColor Green
}

Write-Host ''
Write-Host 'Sync from remote complete.' -ForegroundColor Green