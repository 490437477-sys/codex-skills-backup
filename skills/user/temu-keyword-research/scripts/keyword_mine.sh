#!/usr/bin/env bash
# TEMU Keyword Mining Script
# Sources: Amazon autocomplete (proxy for TEMU buyer language) + TEMU site search scraping + alphabet expansion
# Usage: keyword_mine.sh <seed_keyword> [marketplace]
# Marketplace: us (default), uk, de, fr, it, es, jp, kr, mx, br, sa, ae, ph, nl, pl, pt

set -uo pipefail

KEYWORD="${1:?Usage: keyword_mine.sh <seed_keyword> [marketplace]}"
MARKETPLACE="${2:-us}"

# Map marketplace to Amazon domain and market ID (Amazon autocomplete is our best free proxy)
declare -A DOMAINS=(
  [us]="amazon.com" [uk]="amazon.co.uk" [de]="amazon.de"
  [fr]="amazon.fr" [it]="amazon.it" [es]="amazon.es"
  [jp]="amazon.co.jp" [ca]="amazon.ca" [au]="amazon.com.au"
  [in]="amazon.in" [mx]="amazon.com.mx" [br]="amazon.com.br"
  [sa]="amazon.sa" [ae]="amazon.ae" [nl]="amazon.nl"
  [pl]="amazon.pl" [pt]="amazon.pt" [sg]="amazon.sg"
)

declare -A MKTS=(
  [us]="ATVPDKIKX0DER" [uk]="A1F83G8C2ARO7P" [de]="A1PA6795UKMFR9"
  [fr]="A13V1IB3VIYZZH" [it]="APJ6JRA9NG5V4" [es]="A1RKKUPIHCS9HS"
  [jp]="A1VC38T7YXB528" [ca]="A2EUQ1WTGCTBG2" [au]="A39IBJ37TRP1C6"
  [in]="A21TJRUUN4KGV" [mx]="A1AM78C64UM0Y8" [br]="A2Q3Y263D00KWC"
  [sa]="A17E79C6D8DWNP" [ae]="A2VIGQ35RCS4UG" [nl]="A1805IZSGTT6HS"
  [pl]="A1C3SOZRARQ6R3" [pt]="A3Q5ASMUH29YHM" [sg]="A19VAU5S5PQ93B"
)

DOMAIN="${DOMAINS[$MARKETPLACE]:-amazon.com}"
MKT="${MKTS[$MARKETPLACE]:-ATVPDKIKX0DER}"

echo "=== TEMU Keyword Mining ==="
echo "Seed: $KEYWORD"
echo "Marketplace: $MARKETPLACE ($DOMAIN)"
echo ""

# Source 1: Amazon autocomplete with common modifiers
echo "--- Source 1: Amazon autocomplete (modifier expansion) ---"
for prefix in "" "best " "cheap " "top " "mini " "portable " "for " "with "; do
  SEARCH_TERM="${prefix}${KEYWORD}"
  ENCODED=$(python3 -c "import urllib.parse; print(urllib.parse.quote('${SEARCH_TERM}'))")
  RESULT=$(curl -s --max-time 8 "https://completion.${DOMAIN}/api/2017/suggestions?mid=${MKT}&alias=aps&prefix=${ENCODED}" 2>/dev/null)
  if [ -n "$RESULT" ]; then
    echo "$RESULT" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    for s in data.get('suggestions', []):
        v = s.get('value', '').strip()
        if v and len(v) < 80:
            print(v)
except Exception:
    pass
" 2>/dev/null
  fi
  sleep 0.2
done | sort -u

echo ""
echo "--- Source 2: Amazon autocomplete (a-z suffix expansion) ---"
for letter in a b c d e f g h i j k l m n o p q r s t u v w x y z; do
  SEARCH_TERM="${KEYWORD} ${letter}"
  ENCODED=$(python3 -c "import urllib.parse; print(urllib.parse.quote('${SEARCH_TERM}'))")
  RESULT=$(curl -s --max-time 8 "https://completion.${DOMAIN}/api/2017/suggestions?mid=${MKT}&alias=aps&prefix=${ENCODED}" 2>/dev/null)
  if [ -n "$RESULT" ]; then
    echo "$RESULT" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    for s in data.get('suggestions', []):
        v = s.get('value', '').strip()
        if v and len(v) < 80 and v.lower().startswith('${KEYWORD}'.lower()):
            print(v)
except Exception:
    pass
" 2>/dev/null
  fi
  sleep 0.15
done | sort -u

echo ""
echo "--- Source 3: TEMU search suggestion (page title scrape) ---"
# TEMU public search URL: scrape the page title and visible suggestions
ENCODED_TEMU=$(python3 -c "import urllib.parse; print(urllib.parse.quote('${KEYWORD}'))")
TEMU_PAGE=$(curl -sL --max-time 10 \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -H "Accept-Language: en-US,en;q=0.9" \
  "https://www.temu.com/search.html?search_key=${ENCODED_TEMU}" 2>/dev/null)

# Extract product titles (these contain real keywords used by sellers)
echo "$TEMU_PAGE" | grep -oE '"title":"[^"]{5,80}"' | head -40 | sed 's/"title":"//;s/"$//' | sort -u

echo ""
echo "--- Source 4: TEMU search autocomplete (best-effort JSON-LD) ---"
# Some TEMU responses embed suggestion arrays in __NEXT_DATA__ or window.__INITIAL_STATE__
echo "$TEMU_PAGE" | grep -oE '"suggestion":"[^"]{5,80}"' | head -20 | sed 's/"suggestion":"//;s/"$//' | sort -u
echo "$TEMU_PAGE" | grep -oE '"relatedSearch":\[[^]]*\]' | head -5

echo ""
echo "=== Mining complete ==="
echo "Next step: web_search the top 10 candidates to validate competition on TEMU"
