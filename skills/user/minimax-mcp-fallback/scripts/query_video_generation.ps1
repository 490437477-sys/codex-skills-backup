# minimax-mcp-fallback :: query_video_generation.ps1
[CmdletBinding()]
param([Parameter(Mandatory)][string]$TaskId, [string]$ApiKey, [string]$ApiHost = "https://api.minimaxi.com")
. (Join-Path $PSScriptRoot "_env.ps1") -ApiKey $ApiKey -ApiHost $ApiHost
. (Join-Path $PSScriptRoot "_http.ps1")
Invoke-MiniMaxApi -Path "/v1/query/video_generation?task_id=$TaskId" -Method GET
