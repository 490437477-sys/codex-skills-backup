# minimax-mcp-fallback :: voice_clone.ps1
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$VoiceId,
    [Parameter(Mandatory)][string]$File,
    [Parameter(Mandatory)][string]$Text,
    [switch]$IsUrl,
    [string]$ApiKey, [string]$ApiHost = "https://api.minimaxi.com"
)
. (Join-Path $PSScriptRoot "_env.ps1") -ApiKey $ApiKey -ApiHost $ApiHost
. (Join-Path $PSScriptRoot "_http.ps1")
$body = @{ voice_id = $VoiceId; file = $File; text = $Text; is_url = [bool]$IsUrl }
Invoke-MiniMaxApi -Path "/v1/voice_clone" -Body $body
