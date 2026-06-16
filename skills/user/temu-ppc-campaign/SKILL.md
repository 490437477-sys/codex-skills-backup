---
name: temu-ppc-campaign
description: "TEMU Ads (商品推广) campaign builder and optimizer for cross-border sellers. Two modes: (A) Build — design a complete ad strategy for new products with ROAS tier selection (快速跑量/效益均衡/稳定增长), budget allocation, and ad-spend math; (B) Optimize — audit existing TEMU ad performance using the three metrics (曝光/点击/转化/ROAS), identify wasted spend, adjust ROAS tier, and generate a week-by-week action plan. Specifically adapted to TEMU's ROAS-based bidding model (not match-type bidding). Integrates with temu-keyword-research for keyword input, temu-listing-optimization for listing quality check, and temu-product-research for margin/break-even ROAS calculation. Use when: (1) launching TEMU ads for a new product, (2) deciding which ROAS tier to use, (3) auditing current TEMU ad spend and ROAS, (4) calculating break-even ROAS from product margin, (5) scaling profitable TEMU ad spend, (6) troubleshooting low CTR/CVR/ROAS on TEMU."
metadata: {"category":"cross-border-ecommerce","platform":"temu"}
---

# TEMU Ads (商品推广) Campaign Builder

Build profitable TEMU ad campaign structures using TEMU''s ROAS-based bidding model. No API key required.

## When to Use This Skill

Use this skill whenever the user:
- Wants to launch TEMU ads for a new product
- Asks which ROAS tier to choose (快速跑量/效益均衡/稳定增长)
- Wants to audit current TEMU ad performance (曝光/点击/ROAS)
- Needs to calculate break-even ROAS from product margin
- Wants to scale profitable TEMU ad spend
- Mentions TEMU推广, TEMU广告, TEMU商品推广, TEMU站内推广, TEMU ROAS

Do NOT use this skill for: Amazon PPC (use `amazon-ppc-campaign`), noon Ads (use `noon-ppc-campaign`), or any non-TEMU platform. For product selection, use `temu-product-research`. For listing quality, use `temu-listing-optimization` BEFORE running ads.

## Critical Differences from Amazon PPC

**Read this first** — TEMU''s ad system is structurally different from Amazon''s. Using Amazon PPC mental models will waste money.

| Dimension | Amazon Sponsored Products | TEMU 商品推广 |
|---|---|---|
| **Launched** | 2012 | 2025-01-20 (random beta) |
| **Pricing model** | CPC (2nd-price auction) | CPC (1st-price, platform-set effective bid) |
| **Bidding control** | Manual CPC + 3 strategies (Dynamic Up-Down, Dynamic Down, Fixed) | **3 preset ROAS tiers** (快速跑量/效益均衡/稳定增长) |
| **Match types** | Broad / Phrase / Exact / Auto | **None** — platform auto-targets via relevance |
| **Keyword targeting** | Manual keyword + ASIN targeting | Sellers select products; platform matches to search/browse |
| **Negative keywords** | 4 match types | **Does not exist** |
| **Ad groups** | Manual structure | **No ad groups** — campaign level only |
| **Primary metric** | ACoS (ad spend / ad sales) | **ROAS** (ad sales / ad spend) |
| **Typical target** | ACoS 15-35% | ROAS 2.0-5.0+ (varies by tier) |
| **Budget source** | Credit card / prepaid | **Frozen from 货款** (order payment) |
| **Audit dimensions** | 14+ (search terms, placements, etc.) | 4 main (曝光, 点击, CTR, CVR, ROAS) |
| **Dayparting** | Yes | No |
| **Placement bidding** | Top of Search +25-50% | No — all placements auto-allocated |
| **Seller pricing control** | Full | **Ad bidding ≠ product pricing** (they are independent) |

**Key tactical implication**: TEMU is closer to **"promote this product, pick a ROAS tier, set budget"** than to a granular campaign manager. Less control, but also less complexity.

## Three ROAS Tiers Explained

TEMU offers three preset bidding strategies. Seller sets the **target ROAS**; platform optimizes bid per impression.

| Tier (档位) | Target ROAS | Volume | Use When |
|---|---|---|---|
| **快速跑量** (Fast Volume) | **Low ROAS** (e.g. 1.5-2.5) | **Maximum impressions + clicks** | New products needing initial sales velocity, no reviews, no sales history |
| **效益均衡** (Balanced) | **Medium ROAS** (e.g. 2.5-4.0) | **Balanced volume + efficiency** | Products with some sales history, mid-funnel optimization |
| **稳定增长** (Steady Growth) | **High ROAS** (e.g. 4.0+) | **High efficiency, lower volume** | Established products with proven conversion, scaling winners |

**Important**: The "ROAS coefficient" you set is the **minimum ROAS threshold** the platform tries to maintain. Lower coefficient = more volume but lower efficiency. Higher coefficient = less volume but more profitable per click.

## Capabilities

- **ROAS-based financial framework**: Calculate break-even ROAS, target ROAS, max CPC from product margins
- **Tier selection logic**: Pick the right ROAS tier based on listing maturity, sales history, and category competitiveness
- **Budget allocation**: 4-week ramp schedule, daily budget math
- **Performance audit**: 4-dimension diagnosis (曝光不足 / 点击率低 / 转化率低 / ROAS不达标)
- **Listing quality gate**: Pre-flight check — if listing is not ready, ads are wasted money
- **Seasonal alignment**: Tie ad spend to Q4 peak (Black Friday / Christmas) and Q3 back-to-school
- **Multi-product portfolio**: Allocate budget across P0/P1/P2 SKUs
- **Integration chain**: Works with `temu-keyword-research` (keywords), `temu-listing-optimization` (listing check), `temu-product-research` (margins)

## Usage Examples

### Mode A — Build New Campaign

```
I''m launching a 6DOF Aluminum Robotic Arm Kit on TEMU US. 
Price $109.99. Cost $76.50. Daily budget $50. 
Product is new, no reviews yet.
Build me a TEMU ad campaign.
```

```
Use temu-keyword-research to find keywords for "bamboo cutting board",
then build a TEMU ad strategy. Product cost $6, sells for $29.99.
I want to start with 快速跑量 tier and move to 效益均衡 after 7 days.
```

### Mode B — Optimize Existing Campaign

```
My TEMU ad is running 7 days, 快速跑量 tier, daily budget $30.
Stats: 曝光 12,000, 点击 240, CTR 2.0%, 订单 4, ROAS 2.1.
Cost $76.50, sell $109.99. Help me optimize.
```

```
Here''s my TEMU ad report [paste data]. 
Break-even ROAS is 3.2. Current ROAS is 1.8. 
Tell me what to change.
```

### Listing Quality Gate Trigger

```
Should I run ads on my new product? Listing score is 65/100.
Price $89.99. No reviews. Just listed.
```

→ Skill will tell you: **DO NOT run ads yet** — fix listing first (CTR/CVR will be too low to justify spend).

## Workflow (6 Steps)

### Step 1: Verify Listing Readiness (Pre-flight Gate)

**Before spending a single dollar on ads, check listing quality.** This is the #1 reason TEMU ads fail — sellers run ads on a 60-point listing and waste 100% of spend.

Use `temu-listing-optimization` or the bundled listing self-check to score:

| Listing Score | Action |
|---|---|
| **≥ 90/100** | Proceed to ads |
| **75-89/100** | Fix top 2-3 issues first, then run ads at 低预算 |
| **< 75/100** | **DO NOT run ads yet** — fix listing first |

**Critical elements for ad-readiness**:
- 9 images uploaded (1:1, 1000×1000+)
- Video uploaded (15-30 sec)
- Title 60-100 chars with primary keyword in first 30
- All 5 bullet points filled
- Rich description 500-1000 chars
- Price within ±10% of category median
- All category attributes filled
- 14+ age recommendation (for STEM/toys)

### Step 2: Gather Financial Inputs

Need from user (ask if missing):
- **Selling price** (USD)
- **Product cost** (FOB China + freight to US warehouse if semi-managed)
- **Platform commission** (default 5-15% depending on category)
- **Return rate** (default 15% for electronics, 5-8% for hardlines)
- **Daily ad budget** (USD)
- **Current ad stats** (for Mode B)

### Step 3: Calculate Break-Even ROAS

Use `scripts/bid_calculator.py` to compute:
- Break-even ROAS (where ad spend = ad profit)
- Target ROAS (typically break-even × 1.2-1.5 for safety)
- Max CPC (at your assumed CVR)

```bash
python scripts/bid_calculator.py --price 109.99 --cost 76.50 \
  --commission 0.10 --return-rate 0.15 \
  --cvr 0.02 --budget 50
```

Output includes:
- Break-even ROAS
- Recommended target ROAS
- Max CPC (for your CVR)
- Recommended daily clicks at budget
- Expected daily orders at CVR
- **Suggested ROAS tier (3档位) and initial bid coefficient**

### Step 4: Select ROAS Tier

Use the matrix below to pick the starting tier:

| Product Maturity | Reviews | Sales History | Recommended Tier | Why |
|---|---|---|---|---|
| New listing, no reviews | 0 | 0 | **快速跑量** (low ROAS) | Need initial sales velocity + reviews |
| Some reviews, growing | 10-50 | < 100/30d | **效益均衡** (medium ROAS) | Balance traffic + profit |
| Established, BSR stable | 50+ | 100-500/30d | **稳定增长** (high ROAS) | Scale winners efficiently |
| Top seller, BSR top 1% | 200+ | 500+/30d | **稳定增长** (high ROAS) | Maximum efficiency |

**Rule of thumb**: Start at 快速跑量 for the first 7 days to build initial data, then migrate to 效益均衡 based on actual ROAS. Move to 稳定增长 only after you have 30+ days of profitable data.

### Step 5: Build 4-Week Ramp Schedule

Suggested budget pacing:

| Week | Daily Budget | ROAS Tier | Goal |
|---|---|---|---|
| **Week 1** | $20-30 | 快速跑量 (low ROAS) | Generate first sales + reviews |
| **Week 2** | $30-50 | 效益均衡 (medium ROAS) | Optimize based on Week 1 data |
| **Week 3** | $50-80 | 效益均衡 (medium ROAS) | Scale if ROAS ≥ break-even |
| **Week 4** | $80-120 | 稳定增长 (high ROAS) | Lock in profitable keywords |
| **Q4 (Nov-Dec)** | $100-200+ | 效益均衡/稳定增长 | Capture Black Friday / Christmas spike |

**Stop-loss rule**: If Week 1 ROAS < 50% of break-even, pause and re-check listing quality.

### Step 6: Set Up Monitoring

Daily check (5 min):
- 曝光 / 点击 / CTR / 订单 / 花费 / ROAS
- Compare to target

Weekly check (30 min):
- Migrate underperforming products to lower ROAS tier or pause
- Re-allocate budget to winners
- Check listing CTR vs category benchmark

## Output Formats

### Mode A Output — Build New Campaign

```markdown
# ? TEMU Ads Campaign — Ready to Launch

## Listing Quality Gate
**Listing score: [X]/100** → [PROCEED / FIX FIRST]
- [if score < 90, list top 3 issues to fix]

## Financial Framework
- **Selling price**: $XX
- **Product cost**: $XX
- **Platform commission**: XX%
- **Net profit per unit (no ad)**: $XX
- **Break-even ROAS**: X.XX
- **Target ROAS**: X.XX (break-even × 1.3 safety margin)
- **Max CPC** (at 2% CVR): $X.XX

## Recommended ROAS Tier
**[快速跑量 / 效益均衡 / 稳定增长]** — [reasoning based on product maturity]

## 4-Week Budget Ramp
| Week | Daily Budget | Monthly | ROAS Tier | Goal |
|---|---|---|---|---|
| 1 | $XX | $XXX | 快速跑量 | Initial sales |
| 2 | $XX | $XXX | 效益均衡 | Optimize |
| 3 | $XX | $XXX | 效益均衡 | Scale |
| 4 | $XX | $XXX | 稳定增长 | Lock in |

## Targeting (Platform Auto-Handled)
- Keywords from listing title + category attributes
- No manual keyword selection needed
- Platform matches to: search results, category browse, recommendation slots

## Launch Checklist
- [ ] Listing score ≥ 90
- [ ] All images uploaded (9 + 1 video)
- [ ] All attributes filled
- [ ] 14+ age tag (for STEM/toys)
- [ ] Bid budget frozen from 货款
- [ ] Daily check cadence set

## Daily Monitoring Template
| Date | 曝光 | 点击 | CTR | 订单 | 花费 | ROAS | Notes |
|---|---|---|---|---|---|---|---|
| Day 1 | | | | | | | |
| Day 2 | | | | | | | |
...
```

### Mode B Output — Optimize Existing Campaign

```markdown
# ? TEMU Ads Optimization Plan

## Current Performance
| Metric | Current | Target | Status |
|---|---|---|---|
| 曝光 | X,XXX | >X,XXX | ??/??/?? |
| 点击 | XX | >XX | ??/??/?? |
| CTR | X.X% | >2.0% | ??/??/?? |
| CVR | X.X% | >2.0% | ??/??/?? |
| ROAS | X.XX | >X.XX | ??/??/?? |

## 4-Dimension Diagnosis
### 1. 曝光不足 (Impressions low)
**Likely cause**: [bid too low / listing score low / category mismatch]
**Fix**: [raise ROAS tier / improve listing / verify category]

### 2. 点击率低 (CTR low, < 1.5%)
**Likely cause**: [main image weak / price not competitive / title not attractive]
**Fix**: [swap main image / adjust price / test new title]

### 3. 转化率低 (CVR low, < 1.5%)
**Likely cause**: [description weak / price too high / review count low]
**Fix**: [enrich description / adjust price / get more reviews]

### 4. ROAS不达标 (ROAS < target)
**Likely cause**: [CPC too high / CVR too low / wrong tier]
**Fix**: [lower ROAS tier to gain volume / fix listing / pause product]

## Priority Actions (This Week)
1. [Action 1 - specific, measurable]
2. [Action 2 - specific, measurable]
3. [Action 3 - specific, measurable]

## Tier Migration Plan
- Current: [快速跑量/效益均衡/稳定增长]
- Day X: migrate to [next tier] if ROAS > X.XX
- Day Y: pause if ROAS < X.XX for 3 consecutive days

## Expected Results After 4 Weeks
- ROAS: X.XX → X.XX
- Daily spend: $XX → $XX
- Daily orders: X → X
- Monthly ad profit: $XXX
```

## Seasonal Overlay (Critical for TEMU)

TEMU''s discount-driven model amplifies seasonal demand. Plan ad spend around these peaks:

| Period | Event | Ad Spend Strategy |
|---|---|---|
| **Jan-Feb** | Post-Christmas, Chinese New Year | **Reduce 50%** — low demand, high return rate |
| **Mar-May** | Spring, Mother''s Day | **Maintain baseline** |
| **Jun-Aug** | Father''s Day, Back-to-school | **Increase 30-50%** — back-to-school STEM peak |
| **Sep-Oct** | Pre-Q4 ramp | **Test new SKUs at low budget** |
| **Nov 1-30** | Black Friday + Cyber Monday | **3x budget** — biggest volume window |
| **Dec 1-20** | Christmas | **3x budget** — gift buying peak |
| **Dec 20-31** | Late Christmas | **Pause** — shipping too late |

For STEM/educational products specifically:
- **Back-to-school (Aug-Sep)** is the #1 peak — STEM purchases for students
- **Christmas (Dec 1-20)** is the #2 peak — gift purchases
- **Q1 is the lowest** — plan inventory and ad cuts accordingly

## Limitations

- Cannot access TEMU Seller Center directly (no public API for ad data)
- No granular keyword-level performance data (TEMU does not expose)
- No dayparting or placement control
- ROAS is the only bid lever — no manual CPC override
- Estimates of CTR/CVR are based on category benchmarks; actual values vary

For deeper analytics, recommend:
- TEMU Seller Center ad reports (download weekly)
- Third-party tools (盖亚跨境助手, 叠叠加数据)
- Manual tracking in spreadsheet (recommended)

## Integration with Other TEMU Skills

- **`temu-listing-optimization`**: ALWAYS run this BEFORE ads. Listing quality gate is non-negotiable.
- **`temu-keyword-research`**: Use to verify your title keywords are optimized; no manual keyword selection in TEMU Ads, but title keywords drive auto-targeting.
- **`temu-product-research`**: Use to validate break-even ROAS from product margin.
- **`temu-product-research` + `temu-keyword-research` + `temu-listing-optimization` + `temu-ppc-campaign`**: The complete pre-launch sequence.

## Resources

- `scripts/bid_calculator.py`: ROAS / max CPC / break-even calculator
- `references/temu_ads_specs.md`: Complete TEMU ad system reference
- `references/temu_ads_diagnosis.md`: 4-dimension diagnosis playbook
- `assets/campaign_template.md`: Fill-in template for tracking
