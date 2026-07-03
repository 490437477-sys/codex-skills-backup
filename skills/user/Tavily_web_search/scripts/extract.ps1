<#
.SYNOPSIS
Tavily URL extraction (POST /extract). Returns cleaned body of one or more URLs.
.PARAMETER Url
One or more URLs to extract. Comma-separated or pass multiple -Url flags.
.PARAMETER Depth
basic | advanced. Default basic.
.PARAMETER JsonOnly
Emit raw JSON to stdout, no human summary on stderr.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory, Position=0)] [string[]] $Url,
    [ValidateSet("basic","advanced")] [string] $Depth = "basic",
    [switch] $JsonOnly,
    [int] $TimeoutSec = 30
)
. (Join-Path $PSScriptRoot "_lib.ps1")
$body = @{
    urls          = $Url
    extract_depth = $Depth
}
$r = Invoke-Tavily -Endpoint "extract" -Body $body -TimeoutSec $TimeoutSec
if ($JsonOnly) {
    return ($r | ConvertTo-Json -Depth 10)
}
foreach ($it in $r.results) {
    [Console]::Error.WriteLine("===== " + $it.url + " =====")
    if ($it.raw_content) { [Console]::Error.WriteLine($it.raw_content) }
    [Console]::Error.WriteLine("")
}
return ($r | ConvertTo-Json -Depth 10)