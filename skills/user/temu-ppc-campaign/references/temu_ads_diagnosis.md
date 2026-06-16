# TEMU Ads 4-Dimension Diagnosis Playbook

> When TEMU ad performance is below target, diagnose by 4 dimensions: 曝光 / 点击率 / 转化率 / ROAS. Each has a specific root cause cluster and fix.

## Diagnostic Decision Tree

```
Ad performance poor → check in this order:
  ↓
1. 曝光 (impressions) is it < 5,000/day?
   ├─ YES → 曝光不足: out of game, no diagnosis possible
   │        Fix: raise ROAS tier / check listing quality / check category
   └─ NO  → continue
  ↓
2. CTR < 2.0%?
   ├─ YES → 点击率低: people see but don''t click
   │        Fix: main image + price + title
   └─ NO  → continue
  ↓
3. CVR < 2.0%?
   ├─ YES → 转化率低: people click but don''t buy
   │        Fix: detail page + price + reviews
   └─ NO  → continue
  ↓
4. ROAS < target?
   ├─ YES → ROAS不达标: clicks convert, but CPC too high
   │        Fix: lower ROAS tier / lower CPC / fix listing
   └─ NO  → all good, scale up
```

## Dimension 1: 曝光不足 (Low Impressions)

### Symptoms
- Daily impressions < 5,000
- Ad may be in "learning phase" with very few impressions
- Seller Center shows "ad delivery limited" warning

### Root Causes (most common first)

| # | Cause | Diagnostic Check | Fix |
|---|---|---|---|
| 1 | **Bid too low** (ROAS target too high) | Compare to category ROAS avg | Lower ROAS target by 0.5-1.0 |
| 2 | **Listing quality score too low** | Check listing score in `temu-listing-optimization` | Fix listing to ≥ 90 score |
| 3 | **Category mismatch** | Verify product in correct leaf category | Move to correct category |
| 4 | **Price not competitive** | Compare to top 10 in category | Adjust price to category median ±10% |
| 5 | **Daily budget too low** | Check actual spend vs budget | Increase budget to $30+ |
| 6 | **New listing, no sales history** | First 7-14 days | Normal — wait, or boost via 快速跑量 |
| 7 | **Inventory zero / low** | Check stock | Restock |
| 8 | **Store has compliance flag** | Check Seller Center alerts | Resolve flag first |

### Fast Fixes
- **Day 1 quick fix**: Drop ROAS target by 0.5 (faster volume)
- **Day 3 quick fix**: Increase budget by 50%
- **Day 7 quick fix**: Verify listing score ≥ 90, fix any <80 dimensions

## Dimension 2: 点击率低 (Low CTR, < 2.0%)

### Symptoms
- Impressions OK (5,000+/day)
- Clicks low (<100/day)
- CTR < 2.0% (industry benchmark for TEMU: 1.5-3%)

### Root Causes

| # | Cause | Diagnostic Check | Fix |
|---|---|---|---|
| 1 | **Main image weak** | Compare to top 3 in category | New main image (white BG, product 80% fill, no text) |
| 2 | **Price not visible in image** | Check if price in image is allowed in TEMU | Test price overlay vs no overlay |
| 3 | **Title weak** | Check first 30 chars in search preview | Rewrite title with hook |
| 4 | **Review count low / rating low** | Check product card display | Boost reviews (post-purchase email) |
| 5 | **Wrong audience** | Check category browse | Verify category is correct |
| 6 | **Ad creative stale** | Same image > 14 days | Rotate image every 14-21 days |

### CTR Benchmark by Category (TEMU)

| Category | Poor CTR | Average CTR | Good CTR |
|---|---|---|---|
| 3C 电子 | < 1.0% | 1.5-2.5% | > 3.0% |
| 家居 | < 0.8% | 1.2-2.0% | > 2.5% |
| 服装 | < 0.5% | 1.0-1.8% | > 2.2% |
| 美妆 | < 1.0% | 1.8-2.8% | > 3.5% |
| 玩具/STEM | < 1.2% | 2.0-3.5% | > 4.0% |
| 宠物 | < 0.8% | 1.5-2.5% | > 3.0% |

**STEM category is high-CTR by nature** — your robotic arm should target CTR > 2.5%.

### A/B Test Main Image
Run two images for 5-7 days each, compare CTR:
- A: original
- B: new (different angle, lifestyle, or with feature callout)
Pick winner, set as default.

## Dimension 3: 转化率低 (Low CVR, < 2.0%)

### Symptoms
- Impressions and clicks OK
- Orders low
- CVR < 2.0% (TEMU benchmark: 1.5-3%)

### Root Causes

| # | Cause | Diagnostic Check | Fix |
|---|---|---|---|
| 1 | **Detail page weak** | Check 9 sections filled? | Add lifestyle, scale, exploded view |
| 2 | **Price too high vs category** | Compare to top 10 median | Adjust price to median ±10% |
| 3 | **No reviews / low rating** | Check review count | Drive reviews via post-purchase flow |
| 4 | **Description lacks trust signals** | Check return policy, warranty | Add 30-day return, 1-year warranty |
| 5 | **Wrong product for query** | Check search terms in title | Refine title to match search intent |
| 6 | **Shipping time too long** | Check delivery estimate | Use US warehouse for semi-managed |
| 7 | **Out of stock variant showing** | Check inventory per variant | Hide out-of-stock variants |
| 8 | **Image-quality mismatch** | Product looks different from image | Better photography, multi-angle |

### CVR Benchmark by Price Tier

| Price Range | Poor CVR | Average CVR | Good CVR |
|---|---|---|---|
| < $10 | < 3.0% | 5-8% | > 10% |
| $10-30 | < 2.0% | 3-5% | > 6% |
| $30-80 | < 1.5% | 2-4% | > 5% |
| $80-150 | < 1.0% | 1.5-3% | > 4% |
| > $150 | < 0.5% | 1-2% | > 3% |

**For your $109.99 robotic arm**: target CVR > 1.5% minimum, > 2.5% ideal.

## Dimension 4: ROAS不达标 (ROAS Below Target)

### Symptoms
- All upstream metrics look OK
- ROAS < break-even
- Ad spend > ad profit (losing money)

### Root Causes

| # | Cause | Diagnostic Check | Fix |
|---|---|---|---|
| 1 | **CPC too high** | Compare CPC to category | Lower ROAS tier (more volume, same CPC) |
| 2 | **CVR too low** | Check conversion chain | Fix listing per Dimension 3 |
| 3 | **Wrong tier** | Current vs product maturity | Migrate to appropriate tier |
| 4 | **Price too low** | Net profit per unit | Increase price if competitive |
| 5 | **Cost too high** | Margin eroded | Source alternative supplier |
| 6 | **Return rate too high** | Check return % | Fix quality + description accuracy |
| 7 | **Attribution window issue** | Sales attributed wrong | Wait 7-14 days for stable ROAS |

### ROAS Tier Migration Rules

| Current Performance | Migration Action |
|---|---|
| ROAS > target × 1.5 for 7+ days | **Upgrade tier** (稳定增长) — capture more profit |
| ROAS between target and 1.5× target for 7+ days | **Hold tier** — stable, optimize listing |
| ROAS between target × 0.7 and target for 7+ days | **Downgrade tier** (快速跑量) — trade margin for volume |
| ROAS < target × 0.7 for 3+ days | **Pause ad** — fix listing before retry |

## Common Compound Issues

### Issue: "Impressions OK, CTR OK, CVR low, ROAS low"
This is a **listing quality** problem disguised as an ad problem.
- Ad gets clicks, but listing doesn''t convert
- Fix: enrich detail page, add reviews, adjust price
- Ad spend is wasted until listing is fixed

### Issue: "CTR low, CVR low, ROAS low"
This is a **price + main image** problem.
- People see the ad but aren''t interested at the offered price
- Fix: A/B test new main image + lower price 10-15%
- If still fails: product-market fit is wrong, kill it

### Issue: "Impressions low, ROAS high (when measured)"
This is a **scale** problem, not a problem.
- ROAS is high means the product converts well
- Just needs more impressions
- Fix: lower ROAS tier to scale, OR expand to more products

### Issue: "High spend, zero orders after 1000+ clicks"
This is a **fundamental listing failure**.
- 1000+ clicks and no orders = listing is severely broken
- Either wrong product, wrong price, or listing is misleading
- Pause immediately, do NOT keep spending
- Investigate: title-vs-product match, price reasonableness, image accuracy

## Diagnostic Worksheet

```
Product: _______________
Date: _______

Step 1: 曝光诊断
  Daily impressions: _____
  Target: ≥ 5,000
  Status: ?? / ?? / ??
  Action: _____________

Step 2: CTR诊断
  CTR: _____%
  Target: ≥ 2.0%
  Status: ?? / ?? / ??
  Action: _____________

Step 3: CVR诊断
  CVR: _____%
  Target: ≥ 2.0%
  Status: ?? / ?? / ??
  Action: _____________

Step 4: ROAS诊断
  ROAS: _____
  Break-even: _____
  Target: _____
  Status: ?? / ?? / ??
  Action: _____________

OVERALL: ?? scale / ?? optimize / ?? pause+fix
```
