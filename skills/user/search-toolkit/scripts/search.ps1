<#
.SYNOPSIS
    search-toolkit skill 的镜像入口。委托给本地项目的 scripts/search.ps1。
.PARAMETER Query
    搜索查询（任意语言）。
.PARAMETER JsonOnly
    只输出原始 JSON 到 stdout。
.PARAMETER TimeoutSec
    子进程超时秒数，默认 60。
.EXAMPLE
    & "$HOME/.codex/skills/search-toolkit/scripts/search.ps1" -Query "MiniMax 大模型"
.NOTES
    真正的实现逻辑在：C:\Users\Administrator\Documents\搜索工具\scripts\search.ps1
    本文件仅作为 ~/.codex/skills 入口，避免 Codex 直接调用本项目路径。
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory, Position=0)] [string] $Query,
    [switch] $JsonOnly,
    [int] $TimeoutSec = 60
)

# 项目根目录（备份位置）
$projectRoot = "C:\Users\Administrator\Documents\搜索工具"
$entry = Join-Path $projectRoot "scripts\search.ps1"

if (-not (Test-Path $entry)) {
    Write-Error "search.ps1 not found at: $entry" -ErrorAction Stop
}

& $entry -Query $Query -JsonOnly:$JsonOnly -TimeoutSec $TimeoutSec
