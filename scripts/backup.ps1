# scripts/backup.ps1
<#
.SYNOPSIS
  Refresh the backup of installed Codex skills from your local install.

.DESCRIPTION
  Mirrors:
    $env:USERPROFILE\.codex\skills\.system -> <project>/skills/system
    $env:USERPROFILE\.codex\skills          -> <project>/skills/user
    $env:USERPROFILE\.codex\plugins\cache\openai-bundled\*\skills -> <project>/plugins/skills/

  Then regenerates MANIFEST.md.

.PARAMETER WhatIf
  Show what would change without modifying anything.

.PARAMETER SkipPlugins
  Skip the plugin skills sync.

.PARAMETER SkipManifest
  Skip regenerating MANIFEST.md.

.EXAMPLE
  pwsh ./scripts/backup.ps1 -WhatIf
  pwsh ./scripts/backup.ps1
#>
[CmdletBinding()]
param(
    [switch]$WhatIf,
    [switch]$SkipPlugins,
    [switch]$SkipManifest,
    [string]$SourceSkills = (Join-Path $env:USERPROFILE '.codex\skills'),
    [string]$SourcePlugins = (Join-Path $env:USERPROFILE '.codex\plugins\cache\openai-bundled')
)

. (Join-Path $PSScriptRoot '_lib.ps1')

$BackupSkills = Get-BackupSkills
$BackupPlugins = Get-BackupPlugins

Write-Section 'skills/system'
$r1 = Sync-Directory (Join-Path $SourceSkills '.system') (Join-Path $BackupSkills 'system') -WhatIf:$WhatIf -SkipDirs '^\.system$'

Write-Section 'skills/user'
# Use a staging dir without .system so it cannot leak into user/.
$staging = Join-Path $env:TEMP ("skills-stage-" + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Force -Path $staging | Out-Null
try {
    foreach ($d in (Get-ChildItem -Force -Directory $SourceSkills | Where-Object { -not $_.Name.StartsWith('.') })) {
        Copy-Item -Recurse -Force $d.FullName (Join-Path $staging $d.Name)
    }
    $r2 = Sync-Directory $staging (Join-Path $BackupSkills 'user') -WhatIf:$WhatIf -SkipDirs '^\.system$'
} finally {
    if (Test-Path $staging) { Remove-Item -Recurse -Force $staging }
}

$pluginSummary = @{ Copied = 0; Removed = 0 }
if (-not $SkipPlugins) {
    Write-Section 'plugins/skills'
    if (-not (Test-Path $SourcePlugins)) {
        Write-Host '  (source plugins cache not found; skipping)' -ForegroundColor DarkGray
    } else {
        foreach ($plugin in Get-ChildItem -Force -Directory $SourcePlugins | Sort-Object Name) {
            $ver = Get-ChildItem -Force -Directory $plugin.FullName | Select-Object -First 1
            if (-not $ver) { continue }
            $srcSkillsDir = Join-Path $ver.FullName 'skills'
            if (-not (Test-Path $srcSkillsDir)) { continue }
            Write-Host ('  - ' + $plugin.Name) -ForegroundColor DarkCyan
            $r = Sync-Directory $srcSkillsDir (Join-Path $BackupPlugins $plugin.Name) -WhatIf:$WhatIf -SkipDirs '^\.system$'
            $pluginSummary.Copied += $r.Copied
            $pluginSummary.Removed += $r.Removed
        }
    }
}

if (-not $SkipManifest) {
    Write-Section 'MANIFEST.md'
    Update-Manifest -WhatIf:$WhatIf
}

Write-Section 'summary'
Write-Host ('  skills : copied={0}, removed={1}' -f ($r1.Copied + $r2.Copied), ($r1.Removed + $r2.Removed))
Write-Host ('  plugins: copied={0}, removed={1}' -f $pluginSummary.Copied, $pluginSummary.Removed)
if ($WhatIf) { Write-Host '  (run without -WhatIf to apply)' -ForegroundColor Yellow }
