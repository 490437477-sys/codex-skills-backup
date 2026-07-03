# minimax-mcp-fallback :: play_audio.ps1
[CmdletBinding()]
param([Parameter(Mandatory)][string]$InputFilePath)
Add-Type -AssemblyName System.Media
$full = (Resolve-Path $InputFilePath).Path
$sp = New-Object System.Media.SoundPlayer
$sp.SoundLocation = $full
$sp.PlaySync()
"played: $full"
