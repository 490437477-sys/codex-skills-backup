# scripts/_lib.ps1
# Shared helpers for diff/backup/restore.
# Dot-source this from each script:
#   . (Join-Path $PSScriptRoot '_lib.ps1')

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# --- Paths ---------------------------------------------------------------
function Get-CodexHome          { return $env:USERPROFILE }
function Get-SourceSkills       { return Join-Path (Get-CodexHome) '.codex\skills' }
function Get-SourceAgentsSkills { return Join-Path (Get-CodexHome) '.agents\skills' }
# Returns all plugin-skill source roots under ~/.codex/plugins/cache/<marketplace>/.
# Each marketplace contributes its own subdir; backup layout mirrors that as
#   plugins/skills/<marketplace>/<plugin>/<ver>/skills/
function Get-AllPluginSources {
    $cache = Join-Path (Get-CodexHome) '.codex\plugins\cache'
    if (-not (Test-Path $cache)) { return @() }
    Get-ChildItem -Force -Directory $cache |
        Where-Object { -not ($_.Name -match '^[._]') } |
        ForEach-Object { $_.FullName }
}
function Get-SourcePlugins      { return (Join-Path (Get-CodexHome) '.codex\plugins\cache\openai-bundled') }
function Get-ProjectRoot        { return (Resolve-Path (Join-Path $PSScriptRoot '..')).Path }
function Get-BackupSkills       { return Join-Path (Get-ProjectRoot) 'skills' }
function Get-BackupPlugins      { return Join-Path (Get-ProjectRoot) 'plugins\skills' }

# Returns all user-skill source roots in priority order (r0 first, r1 second).
# r0 (.codex/skills) takes precedence on name conflicts; r1 (.agents/skills) fills in skills not in r0.
function Get-AllUserSkillSources {
    return @(
        (Get-SourceSkills),
        (Get-SourceAgentsSkills)
    )
}

# --- Filtering ------------------------------------------------------------
$Script:JunkRegex = '__pycache__|\.git|\.DS_Store$|Thumbs\.db$'

function Test-IsJunk {
    param([string]$FullPath)
    return ($FullPath -match $Script:JunkRegex)
}

# --- File helpers --------------------------------------------------------
function Get-RelPath {
    param([string]$Full, [string]$Base)
    return $Full.Substring($Base.Length).TrimStart('\','/').Replace('\','/')
}

function Get-DirFingerprint {
    param([string]$Path)
    if ([string]::IsNullOrEmpty($Path) -or -not (Test-Path $Path)) { return $null }
    $files = Get-ChildItem -Force -File -Recurse -Path $Path |
        Where-Object { -not (Test-IsJunk $_.FullName) }
    $entries = New-Object System.Collections.Generic.List[string]
    foreach ($f in $files) {
        $rel = Get-RelPath $f.FullName $Path
        $h = (Get-FileHash -Algorithm SHA256 -Path $f.FullName).Hash
        [void]$entries.Add("$rel=$h")
    }
    $entries = $entries | Sort-Object
    $combined = $entries -join "`n"
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($combined)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        $digest = $sha.ComputeHash($bytes)
        return ([BitConverter]::ToString($digest) -replace '-','')
    } finally { $sha.Dispose() }
}

# --- File-level diff -----------------------------------------------------
function Compare-DirFiles {
    param([string]$Source, [string]$Backup)
    # Normalize both to long-form absolute paths so Substring math works.
    if (Test-Path $Source) { $Source = [System.IO.Path]::GetFullPath($Source) }
    if (Test-Path $Backup) { $Backup = [System.IO.Path]::GetFullPath($Backup) }
    $srcFiles = if (Test-Path $Source) {
        Get-ChildItem -Force -File -Recurse -Path $Source | Where-Object { -not (Test-IsJunk $_.FullName) }
    } else { @() }
    $bakFiles = if (Test-Path $Backup) {
        Get-ChildItem -Force -File -Recurse -Path $Backup | Where-Object { -not (Test-IsJunk $_.FullName) }
    } else { @() }
    $srcMap = @{}
    foreach ($f in $srcFiles) {
        $rel = Get-RelPath $f.FullName $Source
        $srcMap[$rel] = (Get-FileHash -Algorithm SHA256 -Path $f.FullName).Hash
    }
    $bakMap = @{}
    foreach ($f in $bakFiles) {
        $rel = Get-RelPath $f.FullName $Backup
        $bakMap[$rel] = (Get-FileHash -Algorithm SHA256 -Path $f.FullName).Hash
    }
    $keys = @($srcMap.Keys) + @($bakMap.Keys) | Sort-Object -Unique
    foreach ($k in $keys) {
        $inSrc = $srcMap.ContainsKey($k)
        $inBak = $bakMap.ContainsKey($k)
        if ($inSrc -and -not $inBak) {
            [PSCustomObject]@{ RelPath = $k; Status = 'OnlySource' }
        } elseif (-not $inSrc -and $inBak) {
            [PSCustomObject]@{ RelPath = $k; Status = 'OnlyBackup' }
        } elseif ($srcMap[$k] -ne $bakMap[$k]) {
            [PSCustomObject]@{ RelPath = $k; Status = 'Changed' }
        }
    }
}

# --- Mirror --------------------------------------------------------------
function Sync-Directory {
    # One-way mirror Source -> Target. Returns @{ Copied; Removed }.
    # Junk files (.git, __pycache__, .DS_Store, Thumbs.db) are skipped.
    # -SkipDirs: a regex; any directory whose relative path matches is skipped.
    param(
        [string]$Source,
        [string]$Target,
        [switch]$WhatIf,
        [string]$SkipDirs
    )
    if ([string]::IsNullOrEmpty($Source) -or -not (Test-Path $Source)) {
        Write-Warning "Source not found: $Source"
        return @{ Copied = 0; Removed = 0 }
    }
    $Source = [System.IO.Path]::GetFullPath($Source)
    if (Test-Path $Target) { $Target = [System.IO.Path]::GetFullPath($Target) }
    if (-not (Test-Path $Target)) {
        if ($WhatIf) { Write-Host "  [would mkdir] $Target" }
        else { New-Item -ItemType Directory -Force -Path $Target | Out-Null }
    }

    $copied = 0; $removed = 0

    $dirFilter = if ($SkipDirs) { [regex]$SkipDirs } else { $null }
    $allFiles = Get-ChildItem -Force -File -Recurse -Path $Source | Where-Object { -not (Test-IsJunk $_.FullName) }
    if ($dirFilter) {
        $allFiles = $allFiles | Where-Object {
            $rel = $_.FullName.Substring($Source.Length).TrimStart([char[]]'\\/')
            $firstSeg = ($rel -split '[\\/]')[0]
            -not $dirFilter.IsMatch($firstSeg)
        }
    }
    $allFiles |
        ForEach-Object {
            $rel = $_.FullName.Substring($Source.Length).TrimStart('\','/')
            $dest = Join-Path $Target $rel
            $destDir = Split-Path -Parent $dest
            if (-not (Test-Path $destDir)) {
                if ($WhatIf) { Write-Host "  [would mkdir] $destDir" }
                else { New-Item -ItemType Directory -Force -Path $destDir | Out-Null }
            }
            $need = $true
            if (Test-Path $dest) {
                $a = (Get-FileHash -Algorithm SHA256 -Path $_.FullName).Hash
                $b = (Get-FileHash -Algorithm SHA256 -Path $dest).Hash
                if ($a -eq $b) { $need = $false }
            }
            if ($need) {
                if ($WhatIf) { Write-Host "  [copy]   $rel" }
                else { Copy-Item -Force $_.FullName $dest }
                $copied++
            }
        }

    if (Test-Path $Target) {
        Get-ChildItem -Force -File -Recurse -Path $Target |
            Where-Object { -not (Test-IsJunk $_.FullName) } |
            ForEach-Object {
                $rel = $_.FullName.Substring($Target.Length).TrimStart('\','/')
                $srcFile = Join-Path $Source $rel
                if (-not (Test-Path $srcFile)) {
                    if ($WhatIf) { Write-Host "  [remove] $rel" }
                    else { Remove-Item -Force $_.FullName }
                    $removed++
                }
            }
    }
    return @{ Copied = $copied; Removed = $removed }
}

# --- Skill enumeration ---------------------------------------------------
function Get-SkillDirs {
    param([string]$Root, [switch]$IncludeHidden)
    if (-not (Test-Path $Root)) { return @() }
    Get-ChildItem -Force -Directory -Path $Root |
        Where-Object { $IncludeHidden -or (-not $_.Name.StartsWith('.')) } |
        ForEach-Object { $_.Name }
}

# --- Pretty printing -----------------------------------------------------
function Write-Section     { param([string]$Title) Write-Host ''; Write-Host "=== $Title ===" -ForegroundColor Cyan }
function Write-SkillChange {
    param([string]$Status, [string]$Path, [string]$Details = '')
    $color = switch ($Status) {
        'NEW'      { 'Green' }
        'REMOVED'  { 'Red' }
        'MODIFIED' { 'Yellow' }
        default    { 'Gray' }
    }
    if ($Details) {
        Write-Host ("[{0,-8}] {1,-50} {2}" -f $Status, $Path, $Details) -ForegroundColor $color
    } else {
        Write-Host ("[{0,-8}] {1}" -f $Status, $Path) -ForegroundColor $color
    }
}

# --- Manifest refresh ----------------------------------------------------
function Update-Manifest {
    param([switch]$WhatIf)
    $py = Get-Command python -ErrorAction SilentlyContinue
    if (-not $py) { $py = Get-Command py -ErrorAction SilentlyContinue }
    if (-not $py) { Write-Warning 'Python not found; MANIFEST.md not regenerated.'; return }
    $script = Join-Path (Get-ProjectRoot) 'tools\_gen_manifest.py'
    if (-not (Test-Path $script)) { Write-Warning "Manifest script missing: $script"; return }
    if ($WhatIf) { Write-Host "  [would run] python $script" }
    else { & $py.Path $script | Out-Null }
}
