# minimax-mcp-fallback :: generate_video.ps1
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$Prompt,
    [ValidateSet("T2V-01","T2V-01-Director","I2V-01","I2V-01-Director","I2V-01-live","MiniMax-Hailuo-02")] [string]$Model = "MiniMax-Hailuo-02",
    [int]$Duration = 6,
    [ValidateSet("768P","1080P")] [string]$Resolution = "768P",
    [string]$FirstFrameImage,
    [string]$ApiKey, [string]$ApiHost = "https://api.minimaxi.com",
    [switch]$Async
)
. (Join-Path $PSScriptRoot "_env.ps1") -ApiKey $ApiKey -ApiHost $ApiHost
. (Join-Path $PSScriptRoot "_http.ps1")
$body = @{ model = $Model; prompt = $Prompt }
if ($Model -eq "MiniMax-Hailuo-02") { $body.duration = $Duration; $body.resolution = $Resolution }
if ($FirstFrameImage -and $Model -like "I2V*") { $body.first_frame_image = $FirstFrameImage }
$j = Invoke-MiniMaxApi -Path "/v1/video_generation" -Body $body
if ($Async) { Write-Output $j.task_id; return }
Write-Output $j
