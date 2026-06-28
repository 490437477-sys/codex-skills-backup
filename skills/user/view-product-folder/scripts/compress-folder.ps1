# Batch-compresses jpg images in a folder to viewable size for Codex view_image.
# Originals are never modified. Output goes to <Folder>\_compressed\.
# Usage:
#   pwsh -ExecutionPolicy Bypass -File compress-folder.ps1 -Folder "C:\path\to\imgs"
#   pwsh -ExecutionPolicy Bypass -File compress-folder.ps1 -Folder "..." -LongEdge 1600 -Quality 85
#   pwsh -ExecutionPolicy Bypass -File compress-folder.ps1 -Folder "..." -Files "a.jpg,b.jpg"
[CmdletBinding()]
param(
  [Parameter(Mandatory)] [string] $Folder,
  [int] $LongEdge = 1200,
  [int] $Quality = 75,
  [string] $Files = ""  # optional comma-separated whitelist of BaseName (no extension)
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

if (-not (Test-Path $Folder)) { Write-Error "[ERROR] folder not found: $Folder"; exit 1 }
$dst = Join-Path $Folder '_compressed'
New-Item -ItemType Directory -Force -Path $dst | Out-Null

$all = Get-ChildItem -LiteralPath $Folder -File -Filter *.jpg | Sort-Object Name
if (-not [string]::IsNullOrWhiteSpace($Files)) {
  $set = New-Object 'System.Collections.Generic.HashSet[string]'(
    [System.StringComparer]::OrdinalIgnoreCase)
  foreach ($n in ($Files -split ',')) {
    $n = $n.Trim()
    if ($n) { [void]$set.Add($n) }
  }
  $all = $all | Where-Object { $set.Contains($_.BaseName) }
}
if ($all.Count -eq 0) { Write-Error "[ERROR] no matching jpg files"; exit 1 }

$encoders = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders()
$jpgEncoder = $encoders | Where-Object { $_.MimeType -eq 'image/jpeg' }
$encParams = New-Object System.Drawing.Imaging.EncoderParameters 1
$qualityParam = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [int64]$Quality)
$encParams.Param[0] = $qualityParam

$ok = 0; $skipped = 0; $failed = 0
foreach ($f in $all) {
  $outPath = Join-Path $dst ($f.BaseName + '.jpg')
  if ((Test-Path $outPath) -and $f.LastWriteTime -le (Get-Item $outPath).LastWriteTime) {
    $skipped++; continue
  }
  try {
    $img = [System.Drawing.Image]::FromFile($f.FullName)
    $ratio = $LongEdge / [math]::Max($img.Width, $img.Height)
    if ($ratio -lt 1) { $w = [int]($img.Width * $ratio); $h = [int]($img.Height * $ratio) }
    else { $w = $img.Width; $h = $img.Height }
    $bmp = New-Object System.Drawing.Bitmap $w, $h
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = 'HighQualityBicubic'
    $g.DrawImage($img, 0, 0, $w, $h)
    $bmp.Save($outPath, $jpgEncoder, $encParams)
    $g.Dispose(); $bmp.Dispose(); $img.Dispose()
    $ok++
  } catch { Write-Warning "skip $($f.Name): $_"; $failed++ }
}
Write-Host "[OK] compressed: $ok, skipped: $skipped, failed: $failed -> $dst"
