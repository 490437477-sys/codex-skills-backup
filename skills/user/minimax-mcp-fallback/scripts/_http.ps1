# minimax-mcp-fallback :: _http.ps1
# Shared MiniMax HTTP helper. Sources _env.ps1 automatically.

. (Join-Path $PSScriptRoot "_env.ps1") -ApiHost $env:MINIMAX_API_HOST

function Invoke-MiniMaxApi {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][string]$Path,
        $Body,
        [string]$Method = "POST",
        [switch]$ReturnBytes
    )
    $uri = "$($env:MINIMAX_API_HOST)$Path"
    $headers = @{
        "Authorization" = "Bearer $env:MINIMAX_API_KEY"
        "Content-Type"  = "application/json"
    }
    $jsonBody = if ($Body) { $Body | ConvertTo-Json -Depth 12 } else { $null }
    $params = @{
        Uri         = $uri
        Method      = $Method
        Headers     = $headers
        TimeoutSec  = 180
        ErrorAction  = "Stop"
    }
    if ($jsonBody) { $params.Body = $jsonBody }
    $resp = Invoke-WebRequest @params
    $contentType = ($resp.Headers["Content-Type"] -join ",")
    if ($ReturnBytes -or $contentType -match "audio|octet|video|image|stream") {
        return ,$resp.RawContentStream.ToArray()
    }
    return $resp.Content | ConvertFrom-Json
}

function Save-MiniMaxMedia {
    param([byte[]]$Bytes, [string]$OutFile)
    $dir = Split-Path $OutFile -Parent
    if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    [System.IO.File]::WriteAllBytes($OutFile, $Bytes)
    return (Resolve-Path $OutFile).Path
}
