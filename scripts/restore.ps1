# scripts/restore.ps1
<#
.SYNOPSIS
  Reinstall Codex skills from this project's backup.

.DESCRIPTION
  Mirrors:
    <project>/skills/user      -> $env:USERPROFILE\.codex\skills
    <project>/plugins/skills/  -> $env:USERPROFILE\.codex\plugins\cache\openai-bundled\<plugin>\<ver>\skills

  System skills (skills/system/) are owned by Codex and are NOT copied here.
  Use Codex's built-in "Reset bundled skills" action if a system skill is missing.

.PARAMETER WhatIf
  Show what would change without modifying anything.

.PARAMETER IncludePlugins
  Also restore the openai-bundled plugin skills.

.PARAMETER PluginVersion
  Target plugin cache version directory (default: 26.609.30741 - matches current Codex).

.PARAMETER SkipMcpConfig
  Suppress the MCP config reminder at the end.

.EXAMPLE
  pwsh ./scripts/restore.ps1 -WhatIf
  pwsh ./scripts/restore.ps1 -IncludePlugins
#>
[CmdletBinding()]
param(
    [switch]$WhatIf,
    [switch]$IncludePlugins,
    [string]$PluginVersion = '26.609.30741',
    [switch]$SkipMcpConfig,
    [string]$TargetSkills = (Join-Path $env:USERPROFILE '.codex\skills'),
    [string]$TargetPlugins = (Join-Path $env:USERPROFILE '.codex\plugins\cache\openai-bundled')
)

. (Join-Path $PSScriptRoot '_lib.ps1')

$BackupSkills = Get-BackupSkills
$BackupPlugins = Get-BackupPlugins


Write-Section 'skills/user (from backup)'
# Skip any .system subtree inside backup/user (shouldn't exist, defensive)
$r1 = Sync-Directory (Join-Path $BackupSkills 'user') $TargetSkills -WhatIf:$WhatIf -SkipDirs '^\.system$'

$pluginSummary = @{ Copied = 0; Removed = 0 }
if ($IncludePlugins) {
    Write-Section 'plugins/skills (from backup)'
    if (-not (Test-Path $BackupPlugins)) {
        Write-Host '  (no plugin skills in backup)' -ForegroundColor DarkGray
    } else {
        # Backup layout: plugins/skills/<marketplace>/<plugin>/
        # Target layout: ~/.codex/plugins/cache/<marketplace>/<plugin>/<ver>/skills/
        foreach ($market in (Get-ChildItem -Force -Directory $BackupPlugins | Sort-Object Name)) {
            $marketName = $market.Name
            $targetMarket = Join-Path $TargetPlugins $marketName
            foreach ($plugin in (Get-ChildItem -Force -Directory $market.FullName | Sort-Object Name)) {
                # Detect the version Codex currently has for this plugin; fall back to -PluginVersion.
                $ver = $PluginVersion
                $cached = Join-Path $targetMarket $plugin.Name
                if (Test-Path $cached) {
                    $detected = Get-ChildItem -Force -Directory $cached |
                        Where-Object { $_.Name -match '^[0-9]+\.[0-9]+\.[0-9]+' } |
                        Select-Object -ExpandProperty Name -First 1
                    if ($detected) { $ver = $detected }
                }
                $targetPluginDir = Join-Path $targetMarket ('{0}\{1}\skills' -f $plugin.Name, $ver)
                Write-Host ('  - {0}/{1} (v{2}) -> {3}' -f $marketName, $plugin.Name, $ver, $targetPluginDir) -ForegroundColor DarkCyan
                $r = Sync-Directory $plugin.FullName $targetPluginDir -WhatIf:$WhatIf -SkipDirs '^\.system$'
                $pluginSummary.Copied += $r.Copied
                $pluginSummary.Removed += $r.Removed
            }
        }
    }
} else {
    Write-Section 'plugins/skills'
    Write-Host '  (skipped; pass -IncludePlugins to restore them)' -ForegroundColor DarkGray
}

if (-not $SkipMcpConfig) {
    Write-Section 'MCP config reminder'
    $cfg = Join-Path (Get-ProjectRoot) 'tools\config.toml.sanitized'
    if (Test-Path $cfg) {
        Write-Host ('  See ' + $cfg + ' for the MCP server definitions.') -ForegroundColor DarkGray
        Write-Host ('  Manually merge [mcp_servers.*] into ' + (Join-Path $env:USERPROFILE '.codex\config.toml')) -ForegroundColor DarkGray
        Write-Host '  and replace ***REDACTED*** with your real API keys.' -ForegroundColor DarkGray
    }
}

Write-Section 'summary'
Write-Host ('  user skills : copied={0}, removed={1}' -f $r1.Copied, $r1.Removed)
Write-Host ('  plugins     : copied={0}, removed={1}' -f $pluginSummary.Copied, $pluginSummary.Removed)
if ($WhatIf) { Write-Host '  (run without -WhatIf to apply)' -ForegroundColor Yellow }
Write-Host ''
Write-Host '  Note: skills/system/ is NOT restored by this script.' -ForegroundColor DarkGray
Write-Host "  Use Codex's built-in 'Reset bundled skills' if a system skill is missing." -ForegroundColor DarkGray