<#
.SYNOPSIS
Shared helpers for the web-search skill scripts.
.NOTES
Dot-source this file:  . "$PSScriptRoot\_lib.ps1"
#>

function Get-TavilyKey {
    $k = [System.Environment]::GetEnvironmentVariable("TAVILY_API_KEY", "User")
    if (-not $k) { $k = [System.Environment]::GetEnvironmentVariable("TAVILY_API_KEY", "Process") }
    if (-not $k) {
        Write-Error "TAVILY_API_KEY is not set. Add it to your User environment variables." -ErrorAction Stop
    }
    return $k
}

function Invoke-Tavily {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)] [string] $Endpoint,
        [Parameter(Mandatory)] [hashtable] $Body,
        [int] $TimeoutSec = 30
    )
    $key = Get-TavilyKey
    $Body.api_key = $key
    $json = $Body | ConvertTo-Json -Depth 10
    $uri = "https://api.tavily.com/$Endpoint"
    try {
        $resp = Invoke-RestMethod -Uri $uri -Method Post -ContentType "application/json" -Body $json -TimeoutSec $TimeoutSec
        return $resp
    } catch {
        $errBody = ""
        if ($_.Exception.Response) {
            $sr = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
            $errBody = $sr.ReadToEnd()
        }
        Write-Error ("Tavily $Endpoint failed: {0} | body={1}" -f $_.Exception.Message, $errBody)
    }
}

function Format-SearchResult {
    param($Result, [switch] $SummaryOnly, [switch] $JsonOnly)
    if ($JsonOnly) { return ($Result | ConvertTo-Json -Depth 10) }
    if ($Result.answer) { [Console]::Error.WriteLine("# ANSWER"); [Console]::Error.WriteLine($Result.answer); [Console]::Error.WriteLine("") }
    if ($Result.results) {
        $i = 0
        foreach ($it in $Result.results) {
            $i++
            [Console]::Error.WriteLine("[" + $i + "] " + $it.title)
            [Console]::Error.WriteLine("  url:   " + $it.url)
            if ($it.content) {
                $snippet = $it.content
                if ($snippet.Length -gt 320) { $snippet = $snippet.Substring(0, 320) + "..." }
                [Console]::Error.WriteLine("  snip:  " + $snippet)
            }
        }
    }
    return ($Result | ConvertTo-Json -Depth 10)
}