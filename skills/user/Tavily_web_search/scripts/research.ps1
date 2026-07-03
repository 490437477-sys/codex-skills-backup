<#
.SYNOPSIS
Tavily deep research (POST /research). Multi-source synthesis. 30-90 s.
.PARAMETER Input
Research task description. Be specific.
.PARAMETER Model
mini | pro | auto. Default auto.
.PARAMETER JsonOnly
Emit raw JSON to stdout, no human summary on stderr.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory, Position=0)] [string] $Input,
    [ValidateSet("mini","pro","auto")] [string] $Model = "auto",
    [switch] $JsonOnly,
    [int] $TimeoutSec = 120
)
. (Join-Path $PSScriptRoot "_lib.ps1")
$body = @{
    input = $Input
    model = $Model
}
$r = Invoke-Tavily -Endpoint "research" -Body $body -TimeoutSec $TimeoutSec
if ($JsonOnly) {
    return ($r | ConvertTo-Json -Depth 10)
}
if ($r.answer) { [Console]::Error.WriteLine("# RESEARCH OUTPUT"); [Console]::Error.WriteLine($r.answer); [Console]::Error.WriteLine("") }
if ($r.sources) {
    [Console]::Error.WriteLine("# SOURCES")
    foreach ($s in $r.sources) { [Console]::Error.WriteLine("- " + $s) }
}
return ($r | ConvertTo-Json -Depth 10)