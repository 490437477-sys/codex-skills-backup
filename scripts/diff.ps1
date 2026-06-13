# scripts/diff.ps1
<#
.SYNOPSIS
  Compare installed Codex skills with this project's backup.

.DESCRIPTION
  Walks both $env:USERPROFILE\.codex\skills and <project>/skills, and reports:
    NEW       - present in source but missing from backup
    REMOVED   - present in backup but missing from source
    MODIFIED  - present in both but file contents differ

  Also compares openai-bundled plugin skills under .codex/plugins\cache.

.PARAMETER Detailed
  For modified skills, also list which files changed (OnlySource / OnlyBackup / Changed).

.PARAMETER SourceSkills
  Override the source Codex skills root. Default: $env:USERPROFILE\.codex\skills.

.PARAMETER SourcePlugins
  Override the source plugins cache root. Default: $env:USERPROFILE\.codex\plugins\cache\openai-bundled.

.EXAMPLE
  pwsh ./scripts/diff.ps1
  pwsh ./scripts/diff.ps1 -Detailed
#>
[CmdletBinding()]
param(
    [switch]$Detailed,
    [string]$SourceSkills = (Join-Path $env:USERPROFILE '.codex\skills'),
    [string]$SourcePlugins = (Join-Path $env:USERPROFILE '.codex\plugins\cache\openai-bundled')
)

. (Join-Path $PSScriptRoot '_lib.ps1')

$BackupSkills = Get-BackupSkills
$BackupPlugins = Get-BackupPlugins
$Total = @{ NEW=0; REMOVED=0; MODIFIED=0 }

function Compare-SkillCategory {
    param([string]$Category, [string]$SourceBase, [string]$BackupBase)
    $src = @(Get-SkillDirs $SourceBase -IncludeHidden:$false)
    $bak = @(Get-SkillDirs $BackupBase -IncludeHidden:$false)
    $srcSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$src)
    $bakSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$bak)

    foreach ($n in ($srcSet | Where-Object { -not $bakSet.Contains($_) } | Sort-Object)) {
        Write-SkillChange 'NEW' "$Category/$n"
        $script:Total.NEW++
    }
    foreach ($n in ($bakSet | Where-Object { -not $srcSet.Contains($_) } | Sort-Object)) {
        Write-SkillChange 'REMOVED' "$Category/$n"
        $script:Total.REMOVED++
    }
    foreach ($n in ($srcSet | Where-Object { $bakSet.Contains($_) } | Sort-Object)) {
        $sp = Join-Path $SourceBase $n
        $bp = Join-Path $BackupBase $n
        $sh = Get-DirFingerprint $sp
        $bh = Get-DirFingerprint $bp
        if ($sh -ne $bh) {
            Write-SkillChange 'MODIFIED' "$Category/$n"
            $script:Total.MODIFIED++
            if ($Detailed) {
                $diff = Compare-DirFiles $sp $bp
                if (-not $diff) { Write-Host "           (no file-level differences detected)" -ForegroundColor DarkGray }
                foreach ($d in $diff) {
                    $tag = switch ($d.Status) {
                        'OnlySource' { '+ src' }
                        'OnlyBackup' { '- bak' }
                        'Changed'    { '~ diff' }
                    }
                    Write-Host ("             {0,-7} {1}" -f $tag, $d.RelPath) -ForegroundColor DarkYellow
                }
            }
        }
    }
}

Write-Host ""
Write-Host "Codex skills diff" -ForegroundColor Cyan
Write-Host ("  source : {0}" -f $SourceSkills)
Write-Host ("  backup : {0}" -f $BackupSkills)
Write-Host ("  plugins: {0}" -f $SourcePlugins)

Write-Section 'skills/system'
Compare-SkillCategory 'system' (Join-Path $SourceSkills '.system') (Join-Path $BackupSkills 'system')

Write-Section 'skills/user'
Compare-SkillCategory 'user' $SourceSkills (Join-Path $BackupSkills 'user')

Write-Section 'plugins/skills'
if (-not (Test-Path $SourcePlugins)) {
    Write-Host "  (source plugins cache not found; skipping)" -ForegroundColor DarkGray
} else {
    foreach ($plugin in Get-ChildItem -Force -Directory $SourcePlugins | Sort-Object Name) {
        $ver = Get-ChildItem -Force -Directory $plugin.FullName | Select-Object -First 1
        if (-not $ver) { continue }
        $srcSkillsDir = Join-Path $ver.FullName 'skills'
        if (-not (Test-Path $srcSkillsDir)) { continue }
        $bakPlugin = Join-Path $BackupPlugins $plugin.Name
        $srcNames = @(Get-SkillDirs $srcSkillsDir)
        $bakNames = @()
        if (Test-Path $bakPlugin) { $bakNames = @(Get-SkillDirs $bakPlugin) }
        $srcSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$srcNames)
        $bakSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$bakNames)
        foreach ($n in ($srcSet | Where-Object { -not $bakSet.Contains($_) } | Sort-Object)) {
            Write-SkillChange 'NEW' "plugin/$($plugin.Name)/$n"; $script:Total.NEW++
        }
        foreach ($n in ($bakSet | Where-Object { -not $srcSet.Contains($_) } | Sort-Object)) {
            Write-SkillChange 'REMOVED' "plugin/$($plugin.Name)/$n"; $script:Total.REMOVED++
        }
        foreach ($n in ($srcSet | Where-Object { $bakSet.Contains($_) } | Sort-Object)) {
            $sh = Get-DirFingerprint (Join-Path $srcSkillsDir $n)
            $bh = Get-DirFingerprint (Join-Path $bakPlugin $n)
            if ($sh -ne $bh) {
                Write-SkillChange 'MODIFIED' "plugin/$($plugin.Name)/$n"; $script:Total.MODIFIED++
                if ($Detailed) {
                    foreach ($d in (Compare-DirFiles (Join-Path $srcSkillsDir $n) (Join-Path $bakPlugin $n))) {
                        $tag = switch ($d.Status) { 'OnlySource'{'+ src'}; 'OnlyBackup'{'- bak'}; 'Changed'{'~ diff'} }
                        Write-Host ("             {0,-7} {1}" -f $tag, $d.RelPath) -ForegroundColor DarkYellow
                    }
                }
            }
        }
    }
}

Write-Section 'summary'
Write-Host ("  NEW      : {0}" -f $Total.NEW)
Write-Host ("  REMOVED  : {0}" -f $Total.REMOVED)
Write-Host ("  MODIFIED : {0}" -f $Total.MODIFIED)
if (($Total.NEW + $Total.REMOVED + $Total.MODIFIED) -eq 0) {
    Write-Host "  backup is in sync with source" -ForegroundColor Green
}
