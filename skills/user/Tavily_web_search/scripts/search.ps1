<#
.SYNOPSIS
Tavily web search (POST /search).
.PARAMETER Query
Search query. Use any language; Cyrillic works directly.
.PARAMETER MaxResults
1-20. Default 8.
.PARAMETER Depth
basic | advanced. Default basic. Advanced is slower but richer.
.PARAMETER Topic
general | news. Default general.
.PARAMETER IncludeAnswer
If set, Tavily synthesizes a short answer at the top. Default $true.
.PARAMETER JsonOnly
Emit raw JSON to stdout, no human summary on stderr.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory, Position=0)] [string] $Query,
    [int] $MaxResults = 8,
    [ValidateSet("basic","advanced")] [string] $Depth = "basic",
    [ValidateSet("general","news")] [string] $Topic = "general",
    [bool] $IncludeAnswer = $true,
    [switch] $JsonOnly,
    [int] $TimeoutSec = 30
)
. (Join-Path $PSScriptRoot "_lib.ps1")
$body = @{
    query           = $Query
    max_results     = $MaxResults
    search_depth    = $Depth
    topic           = $Topic
    include_answer  = $IncludeAnswer
}
$r = Invoke-Tavily -Endpoint "search" -Body $body -TimeoutSec $TimeoutSec
Format-SearchResult -Result $r -JsonOnly:$JsonOnly