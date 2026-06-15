#!/usr/bin/env bash
# TEMU Listing Fetcher - extracts listing data from a TEMU product page
# Usage: fetch_listing.sh <temu_product_url>
# Example: fetch_listing.sh "https://www.temu.com/robot-arm-5030175157298-s.html"

set -uo pipefail

URL="${1:?Usage: fetch_listing.sh <temu_product_url>}"

echo "=== TEMU LISTING DATA ==="
echo "URL: $URL"
echo ""

# Fetch the page with browser-like headers (TEMU is JS-rendered, basic fetch is best-effort)
PAGE=$(curl -sL \
  --max-time 20 \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -H "Accept-Language: en-US,en;q=0.9" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Referer: https://www.temu.com/" \
  "$URL" 2>/dev/null)

if [ -z "$PAGE" ]; then
  echo "ERROR: Failed to fetch $URL"
  echo "Note: TEMU pages are JS-rendered. If extraction is incomplete, use tavily_extract instead."
  exit 1
fi

# === Title ===
echo "=== TITLE ==="
# TEMU uses og:title or productTitle in JSON-LD
echo "$PAGE" | grep -oE ''<meta property="og:title" content="[^"]+"|[a-zA-Z]+[[:space:]]*content="[^"]*"'' | head -3
echo "$PAGE" | grep -oE ''<title>[^<]+</title>'' | head -1 | sed ''s/<[^>]*>//g''
echo "$PAGE" | grep -oE ''"title":"[^"]{5,150}"'' | head -3 | sed ''s/"title":"//;s/"$//''
echo ""

# === Price ===
echo "=== PRICE ==="
echo "$PAGE" | grep -oE ''"price":"[^"]+"|"salePrice":"[^"]+"|"marketPrice":"[^"]+"'' | head -5 | sed ''s/"[a-zA-Z]*":"//;s/"$//''
echo "$PAGE" | grep -oE ''US\$[0-9]+\.[0-9]{2}'' | head -3
echo ""

# === Rating + Reviews ===
echo "=== RATING & REVIEWS ==="
echo "$PAGE" | grep -oE ''"ratingValue":"[0-9.]+"|"reviewCount":"[0-9]+"|"commentCount":[0-9]+'' | head -5
echo "$PAGE" | grep -oE ''[0-9]\.[0-9] out of 5 stars'' | head -1
echo ""

# === Sold Count ===
echo "=== SOLD COUNT ==="
echo "$PAGE" | grep -oE ''"soldCount":[0-9]+|"salesVolume":"[0-9]+"|[0-9]+\+ sold|[0-9]+ sold'' | head -5
echo "$PAGE" | grep -oE ''[0-9]+K\? sold|[0-9]+(\.[0-9]+)?K\? bought'' | head -3
echo ""

# === Bullets / Key Selling Points ===
echo "=== KEY SELLING POINTS (BULLETS) ==="
echo "$PAGE" | grep -oE ''"bulletPoint":"[^"]+"|"sellingPoint":"[^"]+"|"highlight":"[^"]{5,100}"'' | head -10 | sed ''s/"[a-zA-Z]*":"//;s/"$//''
echo "$PAGE" | grep -oE ''<li[^>]*>[A-Z][^<]{10,150}</li>'' | head -8 | sed ''s/<[^>]*>//g''
echo ""

# === Rich Description ===
echo "=== RICH DESCRIPTION ==="
echo "$PAGE" | grep -oE ''"description":"[^"]{20,2000}"'' | head -3 | sed ''s/"description":"//;s/"$//'' | head -c 2000
echo ""
echo ""

# === Image Count ===
echo "=== IMAGE COUNT ==="
IMG_COUNT=$(echo "$PAGE" | grep -oE ''"image":"https://[^"]+\.(jpg|jpeg|png|webp)"|"imageUrl":"https://[^"]+"'' | wc -l)
echo "Image references found: $IMG_COUNT"
echo "$PAGE" | grep -oE ''"image":"https://[^"]+\.(jpg|jpeg|png|webp)"'' | head -10 | sed ''s/"image":"//;s/"$//''
echo ""

# === Video Presence ===
echo "=== VIDEO PRESENCE ==="
if echo "$PAGE" | grep -qE ''"videoUrl"|"videoSrc"|\.mp4''; then
  echo "YES - video detected"
  echo "$PAGE" | grep -oE ''"videoUrl":"https://[^"]+\.mp4"|"videoSrc":"https://[^"]+\.mp4"'' | head -3 | sed ''s/"[a-zA-Z]*":"//;s/"$//''
else
  echo "NO - no video found"
fi
echo ""

# === Category Breadcrumb ===
echo "=== CATEGORY BREADCRUMB ==="
echo "$PAGE" | grep -oE ''"categoryName":"[^"]+"|"breadcrumbs":\[[^]]+\]'' | head -5
echo ""

# === JSON-LD Structured Data ===
echo "=== JSON-LD STRUCTURED DATA ==="
echo "$PAGE" | grep -oE ''<script type="application/ld\+json">[^<]+</script>'' | head -1 | sed ''s/<script[^>]*>//;s/<\/script>//'' | python3 -m json.tool 2>/dev/null | head -40
echo ""

# === Attributes (best-effort from JSON-LD) ===
echo "=== ATTRIBUTES (best-effort) ==="
echo "$PAGE" | grep -oE ''"additionalProperty":\[[^]]+\]'' | head -2
echo ""

echo "=== END ==="
echo ""
echo "NEXT STEPS:"
echo "1. If fields are missing, use tavily_extract to render the JS page"
echo "2. For full attribute list, use TEMU Seller Center (this script cannot authenticate)"
echo "3. Compare extracted data against temu-keyword-research candidates"
