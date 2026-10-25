# Review Brief: yard_robotics — 2026-10-25
**Archetype:** review
**Vertical:** yard_robotics
**Persona:** homeowner_pro
**Decision the reader is facing:** Whether to spend $5,599 on a Yarbo Y40 Core with the Snow Blower Module Gen 2 before this winter, or keep a walk-behind blower and hire the rest out — given that the same Core only earns its price back if the mower module is bought on top of it.
**Format:** quick_review
**Price as of:** 2026-10-25
**Verdict:** Buy the Yarbo Y40 Core with Snow Blower Module Gen 2 at $5,599 only if the same Core will also mow your lawn — the Lawn Mower Pro bundle is $7,399, so the second job costs $1,800 and that is where the platform pays. Judged as snow equipment alone, $5,599 buys 6,000 square feet of one-inch clearing per charge, and every storm deeper than that adds a dock return of about 1.5 hours.
**De-dup:** `2026-10-24_your-1-acre-mowers-04-acre-trap` (yard_robotics, published) prices rated versus usable mower acreage — a sizing rule for a machine bought in spring; this brief is a snow purchase priced today, on a different machine and a different unit of capacity. `2026-10-24_your-heated-mat-costs-50-times-the-blower` (outdoor_power_equipment, published) compares a heated mat with a hand-held battery blower on electrical load, and carries none of these prices. A corpus grep for Yarbo / robotic snow blower across `published/`, `context/drafts/` and `context/recon_proposals/` returns no prior artifact that prices a robotic snow unit or its modules.
**Thesis:** The Y40's $5,599 is the entry fee to a modular platform, not the price of a snow blower: as snow equipment it clears 6,000 square feet of one-inch snow per charge and then returns to its dock for about 1.5 hours, so the honest read is that the second module — $1,800 more for the mower — is what makes the number work, and a snow-only buyer is paying platform money for one job.

**Lead:** The vertical's own beats, `context/verticals.json` `primary_angles` #3 ("modular base unit (Yarbo-class) versus dedicated mower plus dedicated snow blower: single point of failure math") and #4 ("robotic snow clearing versus a plow contract versus heated mats in a heavy-snow market"), read at the moment the decision is actually made: the last week of October, with the Y40 snow setup listed at $5,599 against a $6,199 regular price. The reader is `homeowner_pro` in `context/personas.json`, whose wants are "payback math, gotchas, code/incentive reality" — here, the per-charge capacity, the module price list and the replacement part, all of which are published on the vendor's own pages and none of which are in the headline. GSC was checked as the bonus signal only (`context/recon_proposals/2026-10-24_gsc_yard_robotics_opportunities.md` carries 0 candidates; impressions are thin on a young site, which never vetoes a topic).

| Product | Price | Source | Note |
|---|---|---|---|
| Yarbo Y40 Core with Snow Blower Module Gen 2 | $5,599 | https://www.yarbo.com/collections/robotic-snow-blower | $6,199 regular; 2-stage, 24" clearing width, 6,000 ft² per charge measured in 1 inch of snow |

| # | Source | URL | Retrieved | Figure | Measured |
|---|---|---|---|---|---|
| 1 | Yarbo — Robotic Snow Blower collection (price block) | https://www.yarbo.com/collections/robotic-snow-blower | 2026-10-25 | $5,599 | vendor list price, sale, regular $6,199 |
| 2 | Yarbo — Robotic Snow Blower collection (Core comparison table) | https://www.yarbo.com/collections/robotic-snow-blower | 2026-10-25 | 6,000 ft² | vendor claim, coverage per charge, "measured in 1 inch of snow" |
| 3 | Yarbo — Robotic Snow Blower collection (Core comparison table) | https://www.yarbo.com/collections/robotic-snow-blower | 2026-10-25 | 7,000 ft² | vendor claim, Y40P coverage per charge |
| 4 | Yarbo — Robotic Snow Blower collection (recharge note) | https://www.yarbo.com/collections/robotic-snow-blower | 2026-10-25 | roughly 1.5 hours | vendor claim, dock recharge 20% to 80% |
| 5 | Yarbo — Robotic Snow Blower collection (Core comparison table) | https://www.yarbo.com/collections/robotic-snow-blower | 2026-10-25 | 36% (20°) | vendor claim, slope rating |
| 6 | Yarbo — Robotic Snow Blower collection (Core comparison table) | https://www.yarbo.com/collections/robotic-snow-blower | 2026-10-25 | Up to 40 ft | vendor claim, throw distance |
| 7 | Yarbo — Robotic Snow Blower collection (bundle price block) | https://www.yarbo.com/collections/robotic-snow-blower | 2026-10-25 | $7,399 | vendor list price, Y40 Core + Snow Blower Gen 2 + Lawn Mower Pro |
| 8 | Yarbo — Modules collection (product price block) | https://www.yarbo.com/collections/modules | 2026-10-25 | $2,000 | vendor list price, Snow Blower Module Gen 2 sold alone |
| 9 | Yarbo — Accessories collection (product price block) | https://www.yarbo.com/collections/accessories | 2026-10-25 | $159 | vendor list price, Snow Plow Blade |
| 10 | Yarbo — Y Series 38.4Ah Battery product page | https://www.yarbo.com/products/yarbo-battery | 2026-10-25 | $1,199 | vendor list price, replacement battery |
| 11 | PCWorld — Yarbo robotic snow blower review (specification table) | https://www.pcworld.com/article/2937640/yarbo-robotic-snow-blower-review.html | 2026-10-25 | 134 pounds | independent reviewer's spec table, Core less snow blower |
| 12 | PCWorld — Yarbo robotic snow blower review (measured throw) | https://www.pcworld.com/article/2937640/yarbo-robotic-snow-blower-review.html | 2026-10-25 | 7- to 8 meters | independent observation on the module reviewed in October 2025 |
| 13 | PCWorld — Yarbo robotic snow blower review (specification table) | https://www.pcworld.com/article/2937640/yarbo-robotic-snow-blower-review.html | 2026-10-25 | IPX4 | independent spec table, against the vendor's IPX5 |
| 14 | Consumer Reports — Yarbo modular yard robot preview | https://www.consumerreports.org/home-garden/yarbo-modular-robot-review-a1192484202 | 2026-10-25 | 6,000 square feet | CR restating the claim and stating it has not lab-tested the product |
| 15 | EGO — POWER+ 24 in. two-stage snow blower (SNT2400) tech specs | https://egopowerplus.com/two-stage-snow-blower-snt2400 | 2026-10-25 | 18-car driveway | competitor capacity claim, 8 inches of snow, no published area |

## What the article must carry

- **Storm arithmetic, derived, never estimated.** 6,000 ft² at 1 inch = 6,000 square-foot-inches per charge. A 500 ft² driveway (the reader's own number, stated as an assumption): 2 in = 1,000 (17% of a charge), 4 in = 2,000 (33%), 8 in = 4,000 (67%), 12 in = 6,000 (100%). A 1,000 ft² driveway: 6 in = 6,000 (100%), 10 in = 10,000 (167%, i.e. one dock return). Show the method, not just the totals.
- **The step-up is a worse deal per unit of capacity.** $7,299 for the Y40P (row 3's 7,000 ft²) works out to $1.70 per extra square foot of per-charge capacity against the Y40 — the premium buys brushless hub motors and faster mapping, not a different class of machine.
- **The priced wear part is the module itself.** No auger, scraper or shear-pin price list exists on the storefront; the snow module is sold as a unit at $2,000 (row 8), with a refurbished one listed at $1,299. Owner reports on Yarbo's own forum describe a module swapped for a wiring fault and clogging in wet heavy snow — vendor-hosted community, not an independent test, and no figure from it is load-bearing.
- **Two published specs disagree.** The vendor page says IPX5; PCWorld's spec table says IPX4 (row 13). Neither is a lab test this desk ran; write the disagreement, not a winner.
- **Measured throw is shorter than the claim.** Up to 40 ft on the page (row 6); 7- to 8 meters (23-26 ft) observed by PCWorld on the module it reviewed in October 2025 (row 12), which is the earlier generation than the Gen 2 sold today. Both facts, in the same sentence, labelled.
- **Mandatory honesty paragraph:** built from manufacturer spec pages, one independent measured review of the earlier generation, Consumer Reports' untested preview and owner reports; the unit was not handled here.
- **No Review or AggregateRating schema.** `Product` + `Offer` with price and `priceValidUntil`, or a plain `ItemList`.
- **Verdict block links:** the vertical hub https://wellroost.com/categories/yard-robotics/ and the live ownership calculator https://wellroost.com/calculators/true-cost-of-ownership/ (both probed HTTP 200 on 2026-10-25). There is no yard-robotics-specific calculator on the front — do not invent `/yard-robotics/calculators/`, which a prior frontier pass did and which serves nothing.

## Gate result

## Gate result

<!-- review-gate:start -->
<!-- review-gate: helper=review_gate.py format=quick_review rows=15 products=1 fetched=15 hosts=4 price_as_of=2026-10-25 checked_at=2026-10-25T14:04:42+00:00 -->
<!-- review-gate:end -->
