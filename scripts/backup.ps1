# scripts/backup.ps1
<#
.SYNOPSIS
  Refresh the backup of installed Codex skills from your local install.

.DESCRIPTION
  Mirrors:
    $env:USERPROFILE\.codex\skills\.system        -> <project>/skills/system
    $env:USERPROFILE\.codex\skills               -> <project>/skills/user  (priority)
    $env:USERPROFILE\.agents\skills              -> <project>/skills/user  (fills skills not in r0)
    $env:USERPROFILE\.codex\plugins\cache\openai-bundled\*\skills -> <project>/plugins/skills/

  Then regenerates MANIFEST.md.

  r0 (.codex\skills) takes precedence on name conflicts; r1 (.agents\skills) adds the rest.

  Local-only skills (in backup but NOT in r0 or r1) are PRESERVED by default.
  This protects skills you author or extend locally; they are not removed by sync.
  Use -PruneLocal to remove them (the old mirror-everything behavior).

.PARAMETER WhatIf
  Show what would change without modifying anything.

.PARAMETER SkipPlugins
  Skip the plugin skills sync.

.PARAMETER SkipManifest
  Skip regenerating MANIFEST.md.

.PARAMETER PruneLocal
  Remove local-only skills (skills present in backup but absent from both r0 and r1).

.EXAMPLE
  pwsh ./scripts/backup.ps1 -WhatIf
  pwsh ./scripts/backup.ps1
  pwsh ./scripts/backup.ps1 -PruneLocal
#>
[CmdletBinding()]
param(
    [switch]$WhatIf,
    [switch]$SkipPlugins,
    [switch]$SkipManifest,
    [switch]$PruneLocal,
    [string]$SourceSkills = (Join-Path $env:USERPROFILE '.codex\skills'),
    [string]$SourceAgents = (Join-Path $env:USERPROFILE '.agents\skills'),
    [string]$SourcePlugins = (Join-Path $env:USERPROFILE '.codex\plugins\cache\openai-bundled')
)

. (Join-Path $PSScriptRoot '_lib.ps1')

$BackupSkills = Get-BackupSkills
$BackupPlugins = Get-BackupPlugins

Write-Section 'skills/system'
$r1 = Sync-Directory (Join-Path $SourceSkills '.system') (Join-Path $BackupSkills 'system') -WhatIf:$WhatIf -SkipDirs '^\.system$'

# Compute the union of source skill names (r0 + r1) so we can identify local-only skills.
function Get-UnionSourceSkillNames {
    $names = New-Object System.Collections.Generic.HashSet[string]
    foreach ($src in @($SourceSkills, $SourceAgents)) {
        if (Test-Path $src) {
            Get-ChildItem -Force -Directory $src | Where-Object { -not $_.Name.StartsWith('.') } |
                ForEach-Object { [void]$names.Add($_.Name) }
        }
    }
    return $names
}
$sourceSkillNames = Get-UnionSourceSkillNames

# Identify local-only skills: present in backup but absent from r0 + r1.
$localOnlyCount = 0
$backupUserDir = Join-Path $BackupSkills 'user'
if (Test-Path $backupUserDir) {
    foreach ($d in (Get-ChildItem -Force -Directory $backupUserDir | Where-Object { -not $_.Name.StartsWith('.') })) {
        if (-not $sourceSkillNames.Contains($d.Name)) { $localOnlyCount++ }
    }
}

Write-Section 'skills/user (r0 + r1)'
$staging = Join-Path $env:TEMP ("skills-stage-" + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Force -Path $staging | Out-Null
try {
    if (Test-Path $SourceSkills) {
        foreach ($d in (Get-ChildItem -Force -Directory $SourceSkills | Where-Object { -not $_.Name.StartsWith('.') })) {
            Copy-Item -Recurse -Force $d.FullName (Join-Path $staging $d.Name)
        }
    } else {
        Write-Warning "  r0 source not found: $SourceSkills"
    }

    $r1Added = 0
    $r1Skipped = 0
    if (Test-Path $SourceAgents) {
        foreach ($d in (Get-ChildItem -Force -Directory $SourceAgents | Where-Object { -not $_.Name.StartsWith('.') })) {
            $dest = Join-Path $staging $d.Name
            if (Test-Path $dest) {
                $r1Skipped++
                continue
            }
            Copy-Item -Recurse -Force $d.FullName $dest
            $r1Added++
        }
        if ($r1Added -gt 0) {
            Write-Host ("  - added {0} r1-only skill(s) from {1}" -f $r1Added, $SourceAgents) -ForegroundColor DarkCyan
        }
        if ($r1Skipped -gt 0) {
            Write-Host ("  - skipped {0} r1 skill(s) that already exist in r0" -f $r1Skipped) -ForegroundColor DarkGray
        }
    }

    if ($localOnlyCount -gt 0 -and -not $PruneLocal) {
        # Pull local-only skills into staging so Sync-Directory does not remove them.
        $localOnlyRestored = 0
        foreach ($d in (Get-ChildItem -Force -Directory $backupUserDir | Where-Object { -not $_.Name.StartsWith('.') })) {
            if (-not $sourceSkillNames.Contains($d.Name)) {
                $dest = Join-Path $staging $d.Name
                if (-not (Test-Path $dest)) {
                    Copy-Item -Recurse -Force $d.FullName $dest
                    $localOnlyRestored++
                }
            }
        }
        Write-Host ("  - preserving {0} local-only skill(s) (in backup, not in r0/r1)" -f $localOnlyCount) -ForegroundColor Yellow
    } elseif ($localOnlyCount -gt 0 -and $PruneLocal) {
        Write-Host ("  - PruneLocal: {0} local-only skill(s) WILL be removed" -f $localOnlyCount) -ForegroundColor Yellow
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
Write-Host ('  skills : copied={0}, removed={1}, local-only-preserved={2}' -f ($r1.Copied + $r2.Copied), ($r1.Removed + $r2.Removed), $localOnlyCount)
Write-Host ('  plugins: copied={0}, removed={1}' -f $pluginSummary.Copied, $pluginSummary.Removed)
if ($WhatIf) { Write-Host '  (run without -WhatIf to apply)' -ForegroundColor Yellow }
