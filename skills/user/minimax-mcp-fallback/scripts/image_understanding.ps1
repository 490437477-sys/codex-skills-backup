# minimax-mcp-fallback :: image_understanding.ps1
# Analyzes an image (URL, local file, or data: URL) and returns a text description.
# Endpoint: POST {host}/v1/coding_plan/vlm  body: { image_url, prompt }
# Auto-converts http(s) URLs and local file paths to data: URLs because the endpoint
# rejects plain http(s) image URLs with status_code 2013 (invalid image URL).
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$Prompt,
    [Parameter(Mandatory)][string]$ImageUrl,
    [string]$ApiKey,
    [string]$ApiHost = "https://api.minimaxi.com",
    [string]$OutFile
)
. (Join-Path $PSScriptRoot "_env.ps1") -ApiKey $ApiKey -ApiHost $ApiHost
. (Join-Path $PSScriptRoot "_http.ps1")

function ConvertTo-DataUrl {
    param([string]$Source)
    if ($Source -match "^data:") { return $Source }
    if ($Source -match "^https?:") {
        try {
            $resp = Invoke-WebRequest -Uri $Source -TimeoutSec 30 -ErrorAction Stop
        } catch {
            Write-Error "Failed to download image from URL: $($_.Exception.Message)"
            return $null
        }
        $ct = ($resp.Headers."Content-Type" | Select-Object -First 1)
        if (-not $ct) { $ct = "image/png" }
        $ct = ($ct -split ";")[0].Trim()
        if (-not $resp.Content -or $resp.Content.Length -eq 0) {
            Write-Error "Downloaded image is empty (URL: $Source)"
            return $null
        }
        $b64 = [Convert]::ToBase64String($resp.Content)
        return "data:$ct;base64,$b64"
    }
    if (Test-Path -LiteralPath $Source) {
        $bytes = [System.IO.File]::ReadAllBytes($Source)
        if ($bytes.Length -eq 0) {
            Write-Error "Local image file is empty: $Source"
            return $null
        }
        $ext = ([System.IO.Path]::GetExtension($Source)).TrimStart(".").ToLower()
        $mime = "application/octet-stream"
        switch ($ext) {
            "jpg"  { $mime = "image/jpeg" }
            "jpeg" { $mime = "image/jpeg" }
            "png"  { $mime = "image/png" }
            "gif"  { $mime = "image/gif" }
            "webp" { $mime = "image/webp" }
        }
        $b64 = [Convert]::ToBase64String($bytes)
        return "data:$mime;base64,$b64"
    }
    Write-Error "Image source not found or unsupported: $Source (expected http(s) URL, local file path, or data: URL)"
    return $null
}

$dataUrl = ConvertTo-DataUrl -Source $ImageUrl
if (-not $dataUrl) { exit 1 }

$body = @{ prompt = $Prompt; image_url = $dataUrl }
$resp = Invoke-MiniMaxApi -Path "/v1/coding_plan/vlm" -Body $body
$text = $resp.content
if (-not $text -and $resp.choices) { $text = $resp.choices[0].message.content }
if (-not $text) { $text = ($resp | ConvertTo-Json -Depth 6 -Compress) }
if ($OutFile) {
    $dir = Split-Path $OutFile -Parent
    if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    [System.IO.File]::WriteAllText($OutFile, $text, [System.Text.UTF8Encoding]::new($false))
    $resolved = Resolve-Path $OutFile
    Write-Output $resolved.Path
} else {
    Write-Output $text
}

