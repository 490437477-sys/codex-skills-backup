# minimax-mcp-fallback :: music_generation.ps1
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$Prompt,
    [Parameter(Mandatory)][string]$Lyrics,
    [int]$SampleRate = 32000, [int]$Bitrate = 128000,
    [ValidateSet("mp3","wav","pcm")] [string]$Format = "mp3",
    [string]$OutFile = (Join-Path $env:USERPROFILE "Desktop\minimax-fallback" ("music_{0}.mp3" -f (Get-Date -Format "yyyyMMdd_HHmmss"))),
    [string]$ApiKey, [string]$ApiHost = "https://api.minimaxi.com"
)
. (Join-Path $PSScriptRoot "_env.ps1") -ApiKey $ApiKey -ApiHost $ApiHost
. (Join-Path $PSScriptRoot "_http.ps1")
$body = @{ prompt = $Prompt; lyrics = $Lyrics; audio_setting = @{ sample_rate = $SampleRate; bitrate = $Bitrate; format = $Format } }
Invoke-MiniMaxApi -Path "/v1/music_generation" -Body $body
Write-Output $OutFile
