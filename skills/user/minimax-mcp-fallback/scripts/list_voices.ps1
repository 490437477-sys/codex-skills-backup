# minimax-mcp-fallback :: list_voices.ps1
[CmdletBinding()]
param([string]$ApiKey, [string]$ApiHost = "https://api.minimaxi.com")
. (Join-Path $PSScriptRoot "_env.ps1") -ApiKey $ApiKey -ApiHost $ApiHost
. (Join-Path $PSScriptRoot "_http.ps1")
$j = Invoke-MiniMaxApi -Path "/v1/voice/list" -Method GET
$j.voice_list | ForEach-Object { "{0,-24}  {1}" -f $_.voice_id, $_.voice_name }
