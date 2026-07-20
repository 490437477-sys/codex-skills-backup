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

function Invoke-TavilyTcpFallback { param([System.Net.Http.HttpRequestException]$Ex) Write-Error ("Tavily transport error: {0}" -f $Ex.Message) }

function Invoke-TavilyStreamingCore { param([string]$Uri, [string]$Json, [int]$TimeoutSec, $Key) $client=[System.Net.Http.HttpClient]::new(); $client.Timeout=[TimeSpan]::FromSeconds($TimeoutSec); $req=[System.Net.Http.HttpRequestMessage]::new([System.Net.Http.HttpMethod]::Post,$Uri); $req.Headers.TryAddWithoutValidation("Authorization","Bearer $Key") | Out-Null; $content=[System.Net.Http.StringContent]::new($Json,[System.Text.Encoding]::UTF8,"application/json"); $req.Content=$content; $task=$client.SendAsync($req); $task.Wait(); $resp=$task.Result; $raw=$resp.Content.ReadAsStringAsync().Result; if(-not $resp.IsSuccessStatusCode){ Write-Error ("Tavily request failed: {0} {1}" -f [int]$resp.StatusCode,$raw); return } try { $obj=$raw | ConvertFrom-Json -Depth 10; return $obj } catch { Write-Error ("Tavily response parse error: {0}" -f $_.Exception.Message) } }
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
