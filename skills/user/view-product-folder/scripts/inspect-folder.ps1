# Read-only inspection of a folder of product images. Prints a structured summary
# so Codex can decide whether to build a contact sheet, compress, or skip entirely.
# Usage:
#   pwsh -ExecutionPolicy Bypass -File inspect-folder.ps1 -Folder "C:\path\to\imgs"
[CmdletBinding()]
param(
  [Parameter(Mandatory)] [string] $Folder
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

if (-not (Test-Path $Folder)) { Write-Error "[ERROR] folder not found: $Folder"; exit 1 }
$imgs = Get-ChildItem -LiteralPath $Folder -File | Where-Object { $_.Extension -in @('.jpg','.jpeg','.png') }
if ($imgs.Count -eq 0) { Write-Host "[WARN] no images in $Folder"; exit 0 }

$totalKB = [math]::Round(($imgs | Measure-Object Length -Sum).Sum / 1KB, 1)
$byExt = $imgs | Group-Object Extension | ForEach-Object { '{0}={1}' -f $_.Name, $_.Count } | Sort-Object

Write-Host "=== Folder Inspection ==="
Write-Host "Path        : $Folder"
Write-Host "Total images: $($imgs.Count)"
Write-Host "Total size  : $totalKB KB"
Write-Host "By format   : $($byExt -join ', ')"
Write-Host ""
Write-Host "Top 5 largest:"
$imgs | Sort-Object Length -Descending | Select-Object -First 5 |
  ForEach-Object { Write-Host ("  {0,-40} {1,8} KB" -f $_.Name, ([math]::Round($_.Length/1KB,1))) }
Write-Host ""

$ratioBuckets = @{ portrait=0; square=0; landscape=0; unknown=0 }
$maxW = 0; $maxH = 0; $minW = [int]::MaxValue; $minH = [int]::MaxValue
foreach ($i in $imgs) {
  try {
    $img = [System.Drawing.Image]::FromFile($i.FullName)
    $r = if ($img.Width -gt $img.Height) { 'landscape' }
         elseif ($img.Width -lt $img.Height) { 'portrait' }
         else { 'square' }
    $ratioBuckets[$r]++
    $maxW = [math]::Max($maxW, $img.Width); $maxH = [math]::Max($maxH, $img.Height)
    $minW = [math]::Min($minW, $img.Width); $minH = [math]::Min($minH, $img.Height)
    $img.Dispose()
  } catch { $ratioBuckets['unknown']++ }
}
Write-Host "Aspect mix  : portrait=$($ratioBuckets['portrait'])  square=$($ratioBuckets['square'])  landscape=$($ratioBuckets['landscape'])  unreadable=$($ratioBuckets['unknown'])"
if ($minW -ne [int]::MaxValue) {
  Write-Host "Dimensions  : min ${minW}x${minH}  max ${maxW}x${maxH}"
}
Write-Host ""
Write-Host "Recommended next step:"
if ($imgs.Count -gt 30) { Write-Host "  -> contact-sheet in batches of 16 (do NOT build one sheet for >30 images)" }
elseif ($imgs.Count -gt 0) { Write-Host "  -> contact-sheet with 4x4 grid (or 2x3 for <=8 images)" }
