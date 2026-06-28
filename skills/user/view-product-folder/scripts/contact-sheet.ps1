# Generates a contact sheet (4x4 grid) of jpg images in a folder.
# Usage:
#   pwsh -ExecutionPolicy Bypass -File contact-sheet.ps1 -Folder "C:\path\to\imgs"
#   pwsh -ExecutionPolicy Bypass -File contact-sheet.ps1 -Folder "..." -Cols 3 -Cell 400
[CmdletBinding()]
param(
  [Parameter(Mandatory)] [string] $Folder,
  [int] $Cols = 4,
  [int] $Cell = 500,
  [int] $MaxImages = ($Cols * 4)
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

if (-not (Test-Path $Folder)) { Write-Error "[ERROR] folder not found: $Folder"; exit 1 }
$files = Get-ChildItem -LiteralPath $Folder -File -Filter *.jpg | Sort-Object Name | Select-Object -First $MaxImages
if ($files.Count -eq 0) { Write-Error "[ERROR] no jpg files in $Folder"; exit 1 }

$rows = [math]::Ceiling($files.Count / $Cols)
$w = $Cols * $Cell; $h = $rows * $Cell
$bmp = New-Object System.Drawing.Bitmap $w, $h
$g   = [System.Drawing.Graphics]::FromImage($bmp)
$g.Clear([System.Drawing.Color]::White)
$g.TextRenderingHint = 'AntiAliasGridFit'
try { $font = New-Object System.Drawing.Font('Segoe UI', 14) } catch { $font = [System.Drawing.SystemFonts]::DefaultFont }

$loaded = 0
for ($i = 0; $i -lt $files.Count; $i++) {
  try {
    $img = [System.Drawing.Image]::FromFile($files[$i].FullName)
    $ratio = [math]::Min($Cell / $img.Width, $Cell / $img.Height)
    $ww = [int]($img.Width * $ratio); $hh = [int]($img.Height * $ratio)
    $x = ($i % $Cols) * $Cell + [int](($Cell - $ww) / 2)
    $y = [int]($i / $Cols) * $Cell + [int](($Cell - $hh) / 2)
    $g.DrawImage($img, $x, $y, $ww, $hh)
    $img.Dispose()
    $loaded++
  } catch { Write-Warning "skip $($files[$i].Name): $_" }
}

for ($i = 0; $i -lt $files.Count; $i++) {
  $label = $files[$i].BaseName
  if ($label.Length -gt 28) { $label = $label.Substring(0, 28) + '...' }
  $x = ($i % $Cols) * $Cell + 6
  $y = [int]($i / $Cols) * $Cell + $Cell - 22
  $g.DrawString($label, $font, [System.Drawing.Brushes]::Black, $x, $y)
}

$out = Join-Path $Folder '_contact.jpg'
$bmp.Save($out, [System.Drawing.Imaging.ImageFormat]::Jpeg)
$g.Dispose(); $bmp.Dispose()
$sizeKB = [math]::Round((Get-Item $out).Length / 1KB, 1)
Write-Host "[OK] contact sheet: $out ($sizeKB KB) — $loaded/$($files.Count) images, ${Cols}x$rows"
