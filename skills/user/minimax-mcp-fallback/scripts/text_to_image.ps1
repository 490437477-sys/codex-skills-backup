# minimax-mcp-fallback :: text_to_image.ps1
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$Prompt,
    [string]$Model = "image-01",
    [ValidateSet("1:1","16:9","4:3","3:2","2:3","3:4","9:16","21:9")] [string]$AspectRatio = "1:1",
    [int]$N = 1,
    [string]$ApiKey,
    [string]$ApiHost = "https://api.minimaxi.com",
    [string]$OutDir = (Join-Path $env:USERPROFILE "Desktop\minimax-fallback")
)
. (Join-Path $PSScriptRoot "_env.ps1") -ApiKey $ApiKey -ApiHost $ApiHost
. (Join-Path $PSScriptRoot "_http.ps1")

$body = @{ model = $Model; prompt = $Prompt; aspect_ratio = $AspectRatio; n = $N; prompt_optimizer = $true }
$bytes = Invoke-MiniMaxApi -Path "/v1/image_generation" -Body $body -ReturnBytes
$ext = "png"
$name = "img_{0}_{1}.{2}" -f (Get-Date -Format "yyyyMMdd_HHmmss"), ([guid]::NewGuid().Guid.Substring(0,8)), $ext
$out  = Join-Path $OutDir $name
$path = Save-MiniMaxMedia -Bytes $bytes -OutFile $out
Write-Output $path
