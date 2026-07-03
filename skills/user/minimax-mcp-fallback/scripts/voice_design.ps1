# minimax-mcp-fallback :: voice_design.ps1
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$Prompt,
    [Parameter(Mandatory)][string]$PreviewText,
    [string]$VoiceId,
    [string]$ApiKey, [string]$ApiHost = "https://api.minimaxi.com"
)
. (Join-Path $PSScriptRoot "_env.ps1") -ApiKey $ApiKey -ApiHost $ApiHost
. (Join-Path $PSScriptRoot "_http.ps1")
$body = @{ prompt = $Prompt; preview_text = $PreviewText }
if ($VoiceId) { $body.voice_id = $VoiceId }
$j = Invoke-MiniMaxApi -Path "/v1/voice_design" -Body $body
if ($j.demo_audio) { Write-Output $j.demo_audio } else { Write-Output $j }
