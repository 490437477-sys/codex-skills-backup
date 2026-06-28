---
name: view-product-folder
description: |
  Inspect a folder of product images for Amazon/noon/Ozon/TEMU listings when the user asks
  Codex to "看图"、"了解产品"、"浏览图片" or "扫一遍主图". Generates a 4x4 contact
  sheet for fast overview, optionally compresses large images to viewable size, and lets
  Codex call `view_image` on individual images. Use whenever the user references a folder
  of product photos (main images, lifestyle shots, white-background images, scene images)
  and wants Codex to understand the product before writing listing copy. Supports jpg/jpeg/png;
  outputs go to a `_contact.jpg` or `_compressed` subfolder next to the source. Trigger phrases
  include "看产品图"、"了解产品"、"扫一遍主图"、"review product images"、"browse product photos".
---

# View Product Folder

## Overview

One-shot workflow for inspecting a folder of product images. Generates a single contact sheet
for fast overview, then optionally compresses or single-views individual images. Output stays
in a sibling subfolder of the source so the originals are never modified.

## When Codex should trigger this skill

- User references a folder of product images and asks Codex to "看图 / 了解产品 / 扫一遍主图"
- User is about to write listing copy (title / bullets / description) and the product visuals
  are not yet understood
- User pastes image filenames or a folder path and asks "这些图是啥" / "产品长什么样"
- After images have been changed/added and the user wants Codex to re-confirm the product

Do NOT trigger when: user only references a single image (use `view_image` directly), or user
asks for image editing/optimization (use the `imagegen` skill instead).

## Quick Start (4 steps)

```powershell
# 0. Pre-flight: list what is in the folder
Get-ChildItem "<FOLDER>" -File -Filter *.jpg |
  Select-Object Name, @{N='SizeKB';E={[math]::Round($_.Length/1KB,1)}}, LastWriteTime
```

```powershell
# 1. Build a 4x4 contact sheet (auto-skips non-jpg, prints output path + size)
#    This is the most common single command Codex should run.
powershell -ExecutionPolicy Bypass -File "<SKILL>\scripts\contact-sheet.ps1" -Folder "<FOLDER>"
```

```powershell
# 2. After Codex views the contact sheet, ask the user which images need detail.
#    Compress those to long-edge 1600px, quality 85 (preserves detail better than 75).
powershell -ExecutionPolicy Bypass -File "<SKILL>\scripts\compress-folder.ps1" `
  -Folder "<FOLDER>" -LongEdge 1600 -Quality 85
```

```powershell
# 3. Codex calls view_image on a single compressed image, e.g.:
view_image(path="<FOLDER>\_compressed\IMG_0010.jpg")
```

`<SKILL>` in the snippets above is this skill's install path (typically
`C:\Users\Administrator\.codex\skills\view-product-folder`).

## Scripts

| Script | Purpose | Defaults |
| --- | --- | --- |
| `scripts/contact-sheet.ps1` | Generate one 4x4 contact sheet for fast overview | 4 cols, 500px cells, output `_contact.jpg` next to source |
| `scripts/compress-folder.ps1` | Batch-compress all images to viewable size | Long edge 1200px, JPEG q=75, output `_compressed\` subfolder. `-Files "a,b,c"` whitelist (BaseName) |
| `scripts/inspect-folder.ps1` | Print a structured table: count, total size, top 5 largest, format mix | Read-only, no output file |

All scripts:
- Read source images, never modify originals
- Write outputs to a sibling subfolder (`_contact.jpg` or `_compressed\`)
- Use `System.Drawing` only — no third-party installs
- Print final output path + size so Codex can `view_image` it

## Workflow guidance for Codex

1. **Always start with `inspect-folder.ps1`** if the folder has > 30 images or unknown contents.
   Avoid generating a contact sheet over a 200-image folder — chunk into batches of 16.
2. **Default contact sheet** is 4x4 (16 images). For folders of 5-8 images, drop to 2x3.
3. **Compress only when needed.** If the contact sheet is enough, skip compression. If
   individual images still need detail, compress only the requested ones (use `-Files 'a,b,c'`).
4. **Always `view_image` the contact sheet first**, before claiming what the product looks like.
   Do not guess from filenames alone.
5. **After viewing**, summarize: structure, color, materials, key parts, what's visible vs
   what is NOT visible. Flag any discrepancy with the user's stated description.

## Output conventions

- `_contact.jpg` — always the contact sheet, sits in the source folder
- `_compressed\*.jpg` — compressed copies, never overwrite originals
- Filename labels on contact sheet cells: original BaseName, max 28 chars, then `...`

## Failure modes Codex should handle

- Folder contains 0 jpg → contact-sheet script exits with `[ERROR] no jpg files`. Tell the user.
- Any image fails to load → script skips it, prints warning, continues with the rest.
- Contact sheet > 1 MB → reduce cell size to 400px and rebuild.
- Source image already small (< 200 KB) → compress script copies it unchanged (no re-encode).

## Reference: ARM4 case study (worked example)

For `C:\Users\Administrator\Desktop\ARM4\主图\`:

1. Ran `inspect-folder.ps1` → 14 jpg files, 3 with whitespace-cropped aspect ratios
2. Ran `contact-sheet.ps1` → `_contact.jpg` 236.9 KB, 4x4 layout
3. Loaded contact sheet via `view_image` → confirmed: 5-axis blue robotic arm, bionic soft
   gripper (lighter blue, anti-slip texture), 5-servo layout, star-shaped 5-prong base
4. User-prioritized 4 critical images: 1782197733456 (dimensions), 生成使用场景图 (1) and (2),
   替换机械臂颜色 — `view_image` on each via `_compressed\` copies
5. Cross-referenced against user's stated description → flagged 1 ambiguity ("图形可视化控制"
   not actually visible in any image, only Arduino IDE + Python serial are evidenced)


