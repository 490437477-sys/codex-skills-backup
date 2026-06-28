# scripts/push.ps1
# Push the local backup to GitHub over SSH, then restore the HTTPS URL.
#
# Why SSH: this machine can reach github.com:22 but not :443, so HTTPS push
# times out. We temporarily switch the remote to SSH for the push and switch
# it back to HTTPS afterwards so day-to-day URLs stay readable.
#
# Usage:
#   pwsh ./scripts/push.ps1            # push
#   pwsh ./scripts/push.ps1 -DryRun    # check SSH + remote only, don't push

[CmdletBinding()]
param(
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$HttpsUrl = 'https://github.com/490437477-sys/codex-skills-backup.git'
$SshUrl   = 'git@github.com:490437477-sys/codex-skills-backup.git'

Set-Location (Join-Path $PSScriptRoot '..')

# --- Sanity checks -------------------------------------------------------
if (-not (Test-Path '.git')) {
    throw 'Not a git repository. Run this from the project root.'
}

$status = git status --porcelain
if ($status) {
    Write-Warning 'Working tree is not clean. Commit or stash before pushing:'
    Write-Host ($status -join "`n")
    throw 'Uncommitted changes. Run backup.ps1 + git commit first.'
}

$ahead = git rev-list --count '@{u}..HEAD' 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Warning 'No upstream configured. Run `git push -u origin main` once manually first.'
    throw 'No upstream. Aborting.'
}
if ($ahead -eq '0') {
    Write-Host 'Nothing to push (local is in sync with origin/main).' -ForegroundColor DarkGray
    return
}

Write-Host "Local is $ahead commit(s) ahead of origin/main." -ForegroundColor Cyan
git log --oneline '@{u}..HEAD'

# --- Pre-flight: confirm SSH key is present and GitHub is reachable -------
Write-Host ''
Write-Host '[preflight] checking local SSH key...' -ForegroundColor Cyan
$keyPath = Join-Path $env:USERPROFILE '.ssh\id_ed25519.pub'
if (-not (Test-Path $keyPath)) {
    throw "SSH public key not found at $keyPath. Run `ssh-keygen -t ed25519` first."
}
Write-Host ('  key   : {0}' -f $keyPath) -ForegroundColor DarkGray
Write-Host ('  fp    : {0}' -f (Get-Content $keyPath).Substring(0, 30) + '...') -ForegroundColor DarkGray

Write-Host '[preflight] probing GitHub over SSH (10s timeout)...' -ForegroundColor Cyan
$probeFile = [System.IO.Path]::GetTempFileName()
$probe     = & ssh.exe -T -o StrictHostKeyChecking=accept-new -o ConnectTimeout=10 -o BatchMode=yes git@github.com *>$null 2>"$probeFile"
$probeText = (Get-Content -Raw $probeFile) -replace "`r?`n", ' '
Remove-Item -Force $probeFile
if ($probeText -notmatch 'successfully authenticated') {
    Write-Warning 'SSH auth failed or timed out. Make sure id_ed25519 is added at https://github.com/settings/keys'
    Write-Host ('  stderr: {0}' -f $probeText)
    throw 'SSH auth failed.'
}
Write-Host ('  ok    : {0}' -f $probeText.Trim()) -ForegroundColor Green

if ($DryRun) {
    Write-Host ''
    Write-Host '[dry-run] would switch remote to SSH, push, then restore HTTPS.' -ForegroundColor Yellow
    return
}

# --- Push over SSH, then restore HTTPS -----------------------------------
$origUrl = (git remote get-url origin).Trim()
Write-Host ''
Write-Host "[push] switching remote: $origUrl -> $SshUrl" -ForegroundColor Cyan
git remote set-url origin $SshUrl
try {
    git push origin main
    if ($LASTEXITCODE -ne 0) { throw "git push exited with $LASTEXITCODE" }
}
finally {
    Write-Host ''
    Write-Host "[push] restoring remote -> $HttpsUrl" -ForegroundColor Cyan
    git remote set-url origin $HttpsUrl
}

Write-Host ''
Write-Host 'Done. Remote is back to HTTPS.' -ForegroundColor Green
git remote -v


