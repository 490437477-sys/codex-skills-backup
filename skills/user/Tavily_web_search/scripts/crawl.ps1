<#
.SYNOPSIS
Tavily website crawl (POST /crawl). Walks links from a starting URL.
.PARAMETER Url
Root URL to begin crawling.
.PARAMETER MaxDepth
How far from the base URL to explore. Default 2.
.PARAMETER Limit
Max total pages to process. Default 10.
.PARAMETER JsonOnly
Emit raw JSON to stdout, no human summary on stderr.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory, Position=0)] [string] $Url,
    [int] $MaxDepth = 2,
    [int] $Limit = 10,
    [switch] $JsonOnly,
    [int] $TimeoutSec = 60
)
. (Join-Path $PSScriptRoot "_lib.ps1")
$body = @{
    url       = $Url
    max_depth = $MaxDepth
    limit     = $Limit
}
$r = Invoke-Tavily -Endpoint "crawl" -Body $body -TimeoutSec $TimeoutSec
if ($JsonOnly) {
    return ($r | ConvertTo-Json -Depth 10)
}
if ($r.answer) { [Console]::Error.WriteLine("# ANSWER"); [Console]::Error.WriteLine($r.answer); [Console]::Error.WriteLine("") }
if ($r.results) {
    $i = 0
    foreach ($it in $r.results) {
        $i++
        [Console]::Error.WriteLine("[{0}] {1}" -f $i, $it.title)
        [Console]::Error.WriteLine("  url: " + $it.url)
    }
}
return ($r | ConvertTo-Json -Depth 10)