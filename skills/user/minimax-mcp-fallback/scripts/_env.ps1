# minimax-mcp-fallback :: _env.ps1
# Loads MINIMAX_API_KEY / MINIMAX_API_HOST into $env for the current session.
# Source this with `. .\_env.ps1 -ApiKey xxx -ApiHost https://api.minimaxi.com`

[CmdletBinding()]
param(
    [string]$ApiKey,
    [string]$ApiHost = "https://api.minimaxi.com"
)

function Get-MiniMaxKey {
    # 1. explicit -ApiKey
    if ($script:ApiKey) { return $script:ApiKey }
    # 2. $env
    if ($env:MINIMAX_API_KEY) { return $env:MINIMAX_API_KEY }
    # 3. ~/.mmx/config.json (written by `mmx auth login --api-key`)
    $cfg = Join-Path $env:USERPROFILE ".mmx\config.json"
    if (Test-Path $cfg) {
        try {
            $j = Get-Content $cfg -Raw | ConvertFrom-Json
            if ($j.apiKey) { return $j.apiKey }
            if ($j.api_key) { return $j.api_key }
        } catch {}
    }
    throw "MINIMAX_API_KEY not found. Set $env:MINIMAX_API_KEY or pass -ApiKey."
}

$env:MINIMAX_API_KEY  = Get-MiniMaxKey
$env:MINIMAX_API_HOST = $ApiHost

Write-Verbose "[minimax-mcp-fallback] host=$ApiHost key=sk-cp-...$($env:MINIMAX_API_KEY[-4..-1] -join '')"
