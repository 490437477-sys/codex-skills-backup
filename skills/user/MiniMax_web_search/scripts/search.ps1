<#
.SYNOPSIS
MiniMax web search (via minimax-coding-plan-mcp / mcp__minimax__web_search).
.PARAMETER Query
Search query. Use any language; Chinese works natively.
.PARAMETER TimeoutSec
Process timeout in seconds. Default 60.
.PARAMETER JsonOnly
Emit raw JSON to stdout, no human summary on stderr.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory, Position=0)] [string] $Query,
    [switch] $JsonOnly,
    [int] $TimeoutSec = 60
)
. (Join-Path $PSScriptRoot "_lib.ps1")

$payload = @(
    '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"MiniMax_web_search_skill","version":"1.0"}}}'
    '{"jsonrpc":"2.0","method":"notifications/initialized"}'
    ("{0}{1}{2}" -f '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"web_search","arguments":{"query":"', ($Query -replace '"','\\"'), '"}}}')
)

$raw = Invoke-MiniMaxMcp -PayloadLines $payload -TimeoutSec $TimeoutSec
Format-MiniMaxSearch -Result $raw -JsonOnly:$JsonOnly
