# TEMU Ads (商品推广) — Complete System Reference

> Reference for everything you need to know about TEMU''s advertising platform as of mid-2026. Updated regularly.

## 1. Platform Overview

| Spec | Detail |
|---|---|
| **Official name** | 商品推广 (Product Promotion) / TEMU Ads |
| **Launch date** | 2025-01-20 (random beta) |
| **General availability** | 2025 Q2 (broad rollout) |
| **Entry point** | Seller Center sidebar → 商品推广 |
| **Pricing model** | CPC (按点击付费) |
| **Bid control** | ROAS-based (3 preset tiers) |
| **Auction type** | 1st-price (effective bid set by platform) |
| **Ad positions** | Search results + category pages + recommendation slots (most in-site positions) |
| **Ad label** | "AD" badge on promoted product image |

## 2. ROAS Tier Presets

Sellers pick ONE of three preset tiers. Platform optimizes per-impression bid to maintain target ROAS.

| Tier (中文) | Tier (English) | ROAS Range (typical) | Volume | Use Case |
|---|---|---|---|---|
| **快速跑量** | Fast Volume | 1.5-2.5 | High | New product, no reviews |
| **效益均衡** | Balanced | 2.5-4.0 | Medium | Established, growing |
| **稳定增长** | Steady Growth | 4.0+ | Lower (high efficiency) | Top sellers, scaling |

**Note**: These are typical ranges, not hard limits. Actual platform target depends on category competition and your historical performance.

## 3. Budget Mechanics

| Item | Detail |
|---|---|
| **Budget source** | **Frozen from 货款** (order payments) — NOT separate credit card |
| **Minimum daily budget** | $10 (recommended $30+ for meaningful traffic) |
| **Maximum daily budget** | No hard cap, but practical limit ~$5,000/day |
| **Budget exhaustion** | Ad pauses when daily budget hit, but already-served impressions still billed |
| **Refund policy** | Refunded orders do NOT return ad spend |
| **Auto-pause triggers** | Product sold out, store suspended, listing quality gate failed |

## 4. Ad Serving Logic

TEMU''s algorithm:
1. Receives search/browse query from buyer
2. Ranks all promoted products eligible for that slot
3. Calculates effective bid per product based on:
   - Your ROAS target (lower = higher bid)
   - Historical CTR/CVR of your product
   - Listing quality score
   - Category competition
4. Shows top-N products in ad slots
5. Charges you CPC when clicked

**You cannot control**: specific keywords, specific placements, time of day, audience segments.

**You CAN control**: ROAS target (via tier), daily budget, which products to promote, listing quality (which affects ranking).

## 5. Reporting & Metrics

TEMU Seller Center provides these metrics (downloadable as CSV):

| Metric | 中文 | Calculation | Healthy Range |
|---|---|---|---|
| **曝光** | Impressions | Times ad shown | > 1,000/day |
| **点击** | Clicks | Times ad clicked | > 20/day |
| **CTR** | Click-through rate | Clicks / Impressions | > 2.0% |
| **订单** | Orders | Sales attributed to ad | > 3/day |
| **CVR** | Conversion rate | Orders / Clicks | > 2.0% |
| **花费** | Ad spend | Total CPC charged | Per budget |
| **CPC** | Cost per click | Spend / Clicks | < $0.50 (varies) |
| **ROAS** | Return on ad spend | Ad revenue / Ad spend | > 3.0 (target) |
| **GMV** | Gross merchandise value | Orders × Price | Track growth |

**Note**: TEMU does NOT provide:
- Search term reports (you don''t know which queries triggered your ad)
- Placement-level performance
- Hour-of-day breakdown
- Audience demographics
- Competitor bid data

## 6. Differences from Amazon Ads (Summary)

| Feature | Amazon Ads | TEMU Ads |
|---|---|---|
| Match types | Broad/Phrase/Exact/Auto | None |
| Manual keyword bidding | Yes | No |
| Negative keywords | Yes | No |
| Ad groups | Yes | No |
| Placement bidding | Yes (Top of Search +X%) | No |
| Dayparting | Yes | No |
| ASIN targeting | Yes | No |
| Brand defense | Yes (via own ASIN bidding) | No |
| Sponsored Brands | Yes | No |
| Sponsored Display | Yes | No |
| Off-site (Google/Meta) | Separate programs | N/A |

**Implication**: TEMU Ads is a simpler "promote this product" tool. It will NOT give you the granular control of Amazon. Treat it as complementary to good listing, not as the primary growth lever.

## 7. Listing Quality Gate (Why Most TEMU Ads Fail)

TEMU''s algorithm deprioritizes ads for low-quality listings. Common failure modes:

| Listing Score | Typical Ad Performance |
|---|---|
| **≥ 90/100** | Strong impressions + 2-4% CTR + 2-4% CVR |
| **75-89/100** | Mediocre impressions + 1-2% CTR + 1-2% CVR |
| **60-74/100** | Low impressions, ad may be auto-suppressed |
| **< 60/100** | Almost no ad serving — platform protects buyer experience |

**The brutal math**: If your listing CTR is 1% and CVR is 1%, even a $0.10 CPC will give you 1 sale per 1,000 clicks = $10 cost per sale. On a $30 product, that''s 33% of revenue gone to ads alone.

## 8. What Sellers Get Wrong

### Mistake 1: Running ads on unready listings
Sellers think ads = sales. They don''t. Ads = **exposure for ready listings**. 80% of TEMU ad waste comes from running ads on 60-70 point listings.

### Mistake 2: Picking 稳定增长 tier from Day 1
High ROAS tier = low volume. New products need volume to build reviews. Start at 快速跑量.

### Mistake 3: Setting budget too low
$10-20/day will get 200-500 impressions — too small for the algorithm to learn. $30-50/day minimum for the first 2 weeks.

### Mistake 4: Never refreshing main image
Ad CTR plateaus after 14-21 days as the same buyers see the same image. Rotate main image weekly.

### Mistake 5: Allocating 100% budget to one product
Spread risk. Even P0 SKUs should have a P1 backup running at 30-50% budget.

### Mistake 6: Ignoring seasonal windows
- **Jan-Feb**: post-Christmas slump — cut budget 50%
- **Aug-Sep**: back-to-school STEM peak — 2x budget
- **Nov 1-Dec 20**: Q4 peak — 3x budget
- **Dec 20-31**: shipping too late — pause

### Mistake 7: Not pausing losers
If a product has 0 orders after 7 days at $30/day spend, it''s a listing problem, not an ad problem. Pause and fix.

## 9. Operational Workflow (Weekly)

### Monday (30 min)
- Download last week''s ad report CSV from Seller Center
- Check ROAS, CTR, CVR trends
- Flag any product with ROAS < 50% of break-even

### Wednesday (15 min)
- Quick check on ad spend pacing
- Adjust daily budget if ahead/behind plan

### Friday (45 min)
- Migrate tier for any product that hit 7+ days of stable ROAS
- A/B test main image for top 3 products
- Plan next week''s budget based on inventory levels

### Monthly (2 hours)
- Full portfolio audit
- Re-calculate break-even ROAS (costs may have changed)
- Review seasonal calendar for next 90 days
- Decision: scale, hold, or kill each product

## 10. Red Flags That Warrant Immediate Pause

| Red Flag | Threshold | Action |
|---|---|---|
| ROAS < 50% of break-even | 3+ consecutive days | Pause ad, fix listing |
| CTR < 0.5% | 7+ days | Main image is broken — change immediately |
| CVR < 0.5% | 7+ days | Listing detail page problem — fix description/price |
| Ad spend > 30% of revenue | Any day | Pause, restructure |
| 0 orders after 1,000 clicks | 7 days | Pause, do not retry without listing overhaul |

## 11. Advanced Tips (Sellers With Experience)

1. **Use ROAS target to test new products**: Set target ROAS = break-even × 1.5. If actual ROAS is 1.0×, listing is good. If < 0.7×, kill it.

2. **Multi-product budget weighting**: 60% to P0, 30% to P1, 10% to P2 (test budget). Re-balance weekly based on ROAS ranking.

3. **Time-of-day insights from CPC fluctuations**: Although you can''t daypart, observe CPC patterns. Low CPC hours = high traffic. If your CVR is consistent, you''re getting cheap clicks.

4. **Use 快速跑量 to harvest reviews**: 30 days at 快速跑量, even at low ROAS, can build 20-50 reviews. After that, migrate to 效益均衡 and ROAS improves naturally.

5. **Inventory-driven ad spend**: Never spend > 30% of available inventory per day. If you have 300 units and want to clear in 60 days, max daily budget should support ~5 sales/day (= $5 × ROAS).

6. **Combine with 平台活动 (Temu platform promotions)**: During 平台大促, the platform itself boosts promoted products. Plan ad spend spikes to align.

## 12. References & Further Reading

- TEMU Seller Center → Help Center → 商品推广 (in-app documentation)
- 雨果跨境 (cifnews) — TEMU 2025 广告投放 articles
- 易仓ERP — TEMU 广告系统 articles
- 叠叠加数据 — TEMU ad analytics platform
- 盖亚跨境助手 — Multi-platform ad management with TEMU support
