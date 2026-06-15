---
name: noon-fbn-calculator
version: 1.0.0
description: "noon FBN Calculator - Complete Fulfilled-by-noon fee breakdown and profit analysis for noon.sa (KSA, SAR), noon.ae (UAE, AED), and noon.com (Egypt, EGP). Calculates size tier, FBN fulfillment fee, storage (off-peak / peak / long-term), commission by category, VAT cash-flow line, returns reserve, COD friction, net margin, and ROI. Bilingual output (English / Arabic) via --ar flag. JSON output via --json flag. No API key required. Use when the user asks about noon FBN fees, noon fulfillment costs, noon profit calculator, noon fee estimation, FBN size tier, noon仓储费, or any FBN-related cost question."
metadata: {"category":"noon","locale":"mena"}
---

# noon FBN Calculator (Lite)

Precise FBN fee calculation for the noon marketplace, based on product dimensions, weight, category, and target marketplace.

## Features

- **Size Tier Detection** - Automatic 5-tier classification from dimensions (cm) and weight (kg)
- **Marketplace-Aware Fulfillment Fee** - Separate rate cards for noon.sa / noon.ae / noon.com
- **Storage Fee** - Off-peak / peak / long-term (>180 days) bands
- **Commission** - By category (15 categories + default)
- **Returns Reserve** - By category (fashion / footwear = 12%, beauty = 5%, etc.)
- **COD Friction** - 2% friction when cash-on-delivery is enabled
- **VAT Cash-Flow Line** - 15% KSA / 5% UAE / 14% EGY, kept as cash-flow item
- **Profit Analysis** - Gross / net margin, ROI, monthly net profit projection
- **Optimization Tips** - Tier downgrade, long-term storage warning, COD switch, margin floor
- **Bilingual Output** - English default; `--ar` for Arabic
- **JSON Output** - `--json` for machine-readable
- **Stdin / Argv / key=value** - Three input modes (stdin recommended for JSON)

## Size Tiers (metric: cm / kg)

| Tier | Max Weight | Max Dimensions (L x W x H) |
|------|------------|-----------------------------|
| small_envelope | 0.25 kg | 30 x 20 x 3 cm |
| small_parcel | 1.0 kg | 30 x 22 x 12 cm |
| standard_parcel | 5.0 kg | 45 x 35 x 20 cm |
| large_parcel | 15.0 kg | 60 x 45 x 50 cm |
| oversize | 30+ kg | > 60 cm on any side |

Tiers are checked in order; a product fits the smallest tier that meets all four limits (weight + 3 dimensions, sorted).

## Input Schema

```json
{
  "sku": "DEMO-SKU",
  "name": "Wireless Earbuds",
  "length_cm": 12.0,
  "width_cm": 8.0,
  "height_cm": 4.0,
  "weight_kg": 0.18,
  "selling_price": 199.0,
  "product_cost": 35.0,
  "inbound_shipping_cost": 4.0,
  "category": "electronics",
  "marketplace": "noon-sa",
  "monthly_units_sold": 200,
  "inventory_days": 45,
  "inventory_age_days": 30,
  "returns_rate_override": null,
  "cod_enabled": true,
  "marketing_per_order": 8.0
}
```

### Field reference

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `sku` | string | no | Defaults to `SKU001` |
| `name` | string | no | Display name |
| `length_cm` | float | **yes** | Centimeters |
| `width_cm` | float | **yes** | Centimeters |
| `height_cm` | float | **yes** | Centimeters |
| `weight_kg` | float | **yes** | Kilograms |
| `selling_price` | float | **yes** | Local currency (SAR / AED / EGP) |
| `product_cost` | float | no | Landed cost in cost-base currency |
| `inbound_shipping_cost` | float | no | Per-unit cost to FBN warehouse |
| `category` | string | no | One of the categories below; default = "default" |
| `marketplace` | string | **yes** | `noon-sa` / `noon-ae` / `noon-eg` |
| `monthly_units_sold` | int | no | Defaults to 100 |
| `inventory_days` | int | no | Average days in stock before sell |
| `inventory_age_days` | int | no | 0-90 = off-peak, 91-180 = peak, 180+ = long-term |
| `returns_rate_override` | float | no | 0-1; overrides category default |
| `cod_enabled` | bool | no | Adds 2% friction when true |
| `marketing_per_order` | float | no | PPC / promo per order |

### Categories

`mobiles`, `electronics`, `fashion`, `footwear`, `beauty`, `home`, `kitchen`, `toys`, `baby`, `sports`, `books`, `grocery`, `automotive`, `health`, `default`

## Output

The calculator emits a line-item report (default) or JSON (with `--json`):

```
noon FBN Fee Calculation Report (Lite)

Product:        Wireless Earbuds (DEMO-SKU)
Marketplace:    noon-sa (SAR)
Category:       electronics
Size tier:      small_parcel (cubic: 0.000384 m^3)
  Weight 0.18kg and dimensions 12.0x8.0x4.0cm fit within small_parcel limits.
Selling price:  SAR 199.00

------------------------------------------------------------
Line item                       Amount (SAR)       %
------------------------------------------------------------
Product cost                           35.00   17.6%
Commission (10.0%)                     19.90   10.0%
FBN fulfillment                         8.50    4.3%
Storage (standard)                      0.01    0.0%
Returns reserve (3.0%)                  5.97    3.0%
COD friction                            3.98    2.0%
VAT carry (15.0%)                      29.85   15.0%
Inbound shipping                        4.00    2.0%
Marketing / order                       8.00    4.0%
------------------------------------------------------------
Total fees                             80.21
Total cost                            115.21
------------------------------------------------------------
Gross profit                          160.00   80.4%
Net profit                             83.79   42.1%
ROI                                   239.4%
------------------------------------------------------------
Monthly units (assumed): 200
Monthly net profit:      SAR 16758.04

------------------------------------------------------------
Optimization tips
------------------------------------------------------------
1. [payment] COD enabled on a low-return category adds 2% friction...
2. [cashflow] High-VAT market. Set aside the VAT line in a separate account...
```

The JSON output has the same data, structured for machine consumption:

```json
{
  "sku": "DEMO-SKU",
  "name": "Wireless Earbuds",
  "marketplace": "noon-sa",
  "currency": "SAR",
  "category": "electronics",
  "size_tier": "small_parcel",
  "tier_reason": "...",
  "cubic_meters": 0.000384,
  "selling_price": 199.0,
  "fees": { ... },
  "total_fees": 80.21,
  "total_cost": 115.21,
  "net_profit": 83.79,
  "net_margin_pct": 42.11,
  "gross_profit": 160.0,
  "gross_margin_pct": 80.4,
  "roi_pct": 239.4,
  "commission_rate_pct": 10.0,
  "returns_rate_pct": 3.0,
  "vat_rate_pct": 15.0,
  "monthly_units_sold": 200,
  "monthly_net_profit": 16758.04,
  "optimization_tips": [ ... ]
}
```

## Usage

### Default (sample product, English)

```bash
python scripts/calculator.py
```

### Custom product via key=value flags (most shell-friendly)

```bash
python scripts/calculator.py \
  name=My-SKU \
  length_cm=25 width_cm=18 height_cm=10 weight_kg=0.8 \
  selling_price=159 product_cost=40 inbound_shipping_cost=5 \
  category=fashion marketplace=noon-ae \
  monthly_units_sold=150 inventory_days=50 inventory_age_days=40 \
  cod_enabled=false marketing_per_order=6
```

### Custom product via JSON (positional)

```bash
python scripts/calculator.py '{"name":"UAE Test","length_cm":25,"width_cm":18,"height_cm":10,"weight_kg":0.8,"selling_price":159,"product_cost":40,"inbound_shipping_cost":5,"category":"fashion","marketplace":"noon-ae","monthly_units_sold":150,"inventory_days":50,"inventory_age_days":40,"cod_enabled":false,"marketing_per_order":6}'
```

### Custom product via JSON (stdin, recommended on PowerShell)

```bash
Get-Content product.json -Raw | python scripts/calculator.py --json
```

### Arabic output

```bash
python scripts/calculator.py --ar
```

### JSON output for piping to other tools

```bash
python scripts/calculator.py --json | jq .net_profit
```

## Multi-Marketplace Behavior

| Marketplace | Currency | VAT | Default commission spread |
|-------------|----------|-----|---------------------------|
| `noon-sa` | SAR | 15% | 6% (mobiles) - 16% (beauty) |
| `noon-ae` | AED | 5% | Same spread |
| `noon-eg` | EGP | 14% | Same spread |

Storage rates differ between KSA/UAE (similar) and EGY (much higher in nominal EGP).

## Optimization Tips Generated

The calculator emits 0-5 tips depending on input:

| Trigger | Tip |
|---------|-----|
| `large_parcel` + longest side > 45 cm | Reduce longest side to drop to `standard_parcel` |
| `standard_parcel` + weight > 1 kg | Reduce weight to drop to `small_parcel` |
| `inventory_age_days` > 180 | Long-term storage band; move deadstock |
| `inventory_age_days` > 90 | Peak storage band; promo slow SKUs |
| `cod_enabled` + low-return category | Switch to prepaid-only to save 2% |
| `net_margin_pct` < 8% | Below safety floor; renegotiate cost or pick new SKU |
| KSA or EGY marketplace | High-VAT cash-flow warning |

Each tip includes a per-unit potential savings estimate (where computable).

## Known Limitations

- **Rate cards are approximate** (mid-points from public noon rate sheets ~2024-2025). Verify against noon Seller Central before committing P&L.
- **Egypt EGP rates** are inflation-adjusted approximations; refresh quarterly.
- **No inbound duty / customs** calculation — wrap the `product_cost` to include HS-code-based duty for accurate KSA / EGY P&L.
- **No advertising ACOS** — pass marketing as a flat per-order line in `marketing_per_order`.
- **No currency conversion** — pass `product_cost` already converted to the revenue currency, or use a separate sheet for FX exposure.
- **Stdout encoding** — the script forces UTF-8; on Windows, redirect to a file (`> out.txt`) if your terminal mis-renders Arabic.

## Best Practices

- **Always pass `inventory_age_days`** to surface long-term-storage risk early.
- **Set `cod_enabled: false`** for low-return categories (electronics, home) unless conversion data shows lift.
- **Use `--json`** when chaining into another tool (Excel, Power BI, custom dashboards).
- **Test tier downgrade** by adjusting dimensions: a 1-2 cm trim can save SAR 10.5 per unit (large → standard).
- **Refresh rates** from noon Seller Central at least once per quarter; paste the updated numbers into the rate tables at the top of `scripts/calculator.py`.

## Related Skills

- `noon-product-research` — for product-level opportunity analysis (uses this calculator as Step 4)
- `noon-listing-optimization` — for Arabic-first listing copy once you've picked the SKU
- `noon-keyword-research` — for the keyword + competitor analysis upstream of listing

---

_Version 1.0.0 | Platform: noon | Variant: Lite | Locale: MENA (KSA default)_
