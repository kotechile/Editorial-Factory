# Verified Brief: yard_robotics (review) — 2026-10-25

Source of record: `context/recon_proposals/2026-10-25_yard_robotics_review_brief.md` (review gate PASS,
15/15 rows fetched, 4 hosts, marker written 2026-10-25T14:04:42+00:00). Every row below was re-fetched
during verification; verbatim is quoted from the page, not paraphrased.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | price | Y40 Core with Snow Blower Module Gen 2 lists at $5,599, regular $6,199 | VERIFIED | https://www.yarbo.com/collections/robotic-snow-blower | "Yarbo Y40 Core with Snow Blower Module Gen 2 … Regular price $5,599.00 USD Sale price $5,599.00 USD Regular price $6,199.00 USD" |
| 2 | capacity | Vendor publishes coverage per charge as 6,000 ft² for the Y40, and the note says the basis is one inch of snow | VERIFIED (vendor claim) | https://www.yarbo.com/collections/robotic-snow-blower | "Coverage per charge Up to 6,000 ft² … Coverage per charge is measured in 1 inch of snow." |
| 3 | capacity | Y40P Core with the same module lists at $7,299 (regular $7,799) and publishes 7,000 ft² per charge | VERIFIED (vendor claim) | https://www.yarbo.com/collections/robotic-snow-blower | "Yarbo Y40P Core with Snow Blower Module Gen 2 … $7,299.00 USD … $7,799.00 USD"; "Up to 6,000 ft² Up to 7,000 ft²" |
| 4 | recharge | At about 20% the unit docks, recharges to about 80% in roughly 1.5 hours, and resumes | VERIFIED (vendor claim) | https://www.yarbo.com/collections/robotic-snow-blower | "At about 20% battery, Yarbo docks, recharges to about 80% in roughly 1.5 hours, and picks up where it left off." |
| 5 | limits | Slope rating 36% (20°); operating range -13°F to 113°F; 2-stage, 12" intake, 24" clearing width, throw up to 40 ft | VERIFIED (vendor claim) | https://www.yarbo.com/collections/robotic-snow-blower | "Slope rating Up to 36% (20°) … Operating temperature -13°F to 113°F (-25°C to 45°C)"; "2-stage, 12\" intake height, 24\" clearing width"; "Up to 40 ft" |
| 6 | bundle | The Y40 with Snow Blower Gen 2 and Lawn Mower Pro lists at $7,399 (regular $8,199), i.e. $1,800 over the snow-only setup | VERIFIED + DERIVED | https://www.yarbo.com/collections/robotic-snow-blower | "Yarbo Y40 Core with Snow Blower Gen 2 and Lawn Mower Pro Modules … $7,399.00 USD … $8,199.00 USD" (7,399 − 5,599 = 1,800) |
| 7 | wear part | The Snow Blower Module Gen 2 (Y Series) is sold alone at $2,000; a refurbished one is listed at $1,299 "Pre-order" | VERIFIED | https://www.yarbo.com/collections/modules | "Snow Blower Module Gen 2 (Y Series) … 2,000.00"; "Pre-order Refurbished Snow Blower Module … Regular price $1,299.00 USD" |
| 8 | accessory | Snow Plow Blade (Y Series) lists at $159; Track Grease (200 ml) at $49 | VERIFIED | https://www.yarbo.com/collections/accessories | "Snow Plow Blade (Y Series) … 159.00"; "Yarbo Track Grease (200 ml) … 49.00" |
| 9 | battery | The Y Series 38.4Ah battery lists at $1,199 | VERIFIED | https://www.yarbo.com/products/yarbo-battery | "Y Series 38.4Ah Battery (Y Series) … Regular price $1,199.00 USD" |
| 10 | weight | The Core weighs 134 pounds (61 kg), less snow blower, per the reviewer's spec table | VERIFIED (independent) | https://www.pcworld.com/article/2937640/yarbo-robotic-snow-blower-review.html | "Weight : 134 pounds (61kg) (Yarbo Core, less snow blower)" |
| 11 | throw | Measured throw was 7- to 8 meters (23-26 ft) on the module reviewed in October 2025, against a "Up to 40 ft" page claim today | VERIFIED (independent measurement, prior generation) | https://www.pcworld.com/article/2937640/yarbo-robotic-snow-blower-review.html | "it has no problem tossing snow (and ice chunks) 7- to 8 meters (7.6- to 8.7 yards)" |
| 12 | weatherization | The vendor page says IPX5; the reviewer's spec table says IPX4 | FLAGGED — two published specs disagree; neither is a lab test this desk ran | https://www.pcworld.com/article/2937640/yarbo-robotic-snow-blower-review.html | "Weatherization : IPX4 (i.e., not tested for dust ingress, protected from water sprayed from any direction)" |
| 13 | cold charging | In cold weather the battery needs 20-30 minutes of warm-up before charging starts | VERIFIED (independent observation, prior generation) | https://www.pcworld.com/article/2937640/yarbo-robotic-snow-blower-review.html | "when its cold outside, it needs to warm up for 20- to 30 minutes before you can start charging its battery" |
| 14 | third-party testing | Consumer Reports restates the 6,000 sq ft claim on a "3-hour charge" and states it has not lab-tested the product | VERIFIED (CR's own words) | https://www.consumerreports.org/home-garden/yarbo-modular-robot-review-a1192484202 | "cover 6,000 square feet of land on a single 3-hour charge"; "CR hasn't tested the nearly $10,000 product" |
| 15 | competitor claim | A 24-inch two-stage walk-behind claims an 18-car driveway at 8 inches of snow on one charge, with no published area | VERIFIED (competitor claim; must not be converted to square feet) | https://egopowerplus.com/two-stage-snow-blower-snt2400 | "Clears up to an 18-car driveway with 8 inches of snow on a single charge when used with the two recommended 7.5Ah ARC Lithium™ batteries" |
| 16 | owner reports | Owners report 9 inches cleared without issue, clogging in wet heavy snow (worked around with the plow blade), and one module replaced for a wiring fault | VERIFIED as owner report (vendor-hosted forum; no figure is load-bearing) | https://forum.yarbo.com/t/still-worth-buying-in-2026/5429 | "We officially got 9" during the storm and I didn't have any issues removing the bulk"; "the snow blower was not good … I abandoned the S1 then used the plow"; "I did end up needing to have the snowblower module replaced due to a wiring issue" |

## Derived arithmetic (computed from printed endpoints, never estimated)

- 6,000 ft² × 1 in = **6,000 square-foot-inches of clearing per charge** (row 2).
- A **500 ft² driveway** (the reader's own figure, stated as an assumption): 2 in = 1,000 (17% of a charge); 4 in = 2,000 (33%); 8 in = 4,000 (67%); 12 in = 6,000 (100%).
- A **1,000 ft² driveway**: 6 in = 6,000 (100%); 10 in = 10,000 (167%, i.e. one dock return at 1.5 hours).
- **$1,800** = $7,399 − $5,599 (row 6).
- **$1.70 per extra ft² per charge** = $1,700 premium (7,299 − 5,599) ÷ 1,000 ft² (7,000 − 6,000), row 3.
- **23–26 ft** = 7–8 m × 3.28084, i.e. the measured throw is 58–66% of the 40 ft claim (row 11 vs row 5).
- **21% of the purchase** = $1,199 battery ÷ $5,599 (row 9 vs row 1).

## Drafter rulings

1. **Evidence classes must be labelled in the sentence.** Rows 2-9 are vendor claims from Yarbo's own
   storefront; rows 10, 11, 13 are an independent reviewer's observations on the module it reviewed in
   October 2025 — the earlier generation than the Gen 2 sold today — and row 14 is a testing
   organisation stating it has not tested the product. Never merge the classes.
2. **Row 12 is a disagreement, not an error.** Write both published figures, name who publishes each,
   and do not pick a winner: neither is a test this desk ran.
3. **Row 15 may not be converted into square feet.** "18-car driveway" has no published area, so it
   stays a claim in its own words and is explicitly not comparable to Yarbo's ft² figure.
4. **Row 16 is a vendor-hosted owner forum.** Attribute it as owner reports, keep no number from it
   load-bearing, and do not present it as a test.
5. **No price may be restated without its date.** "$5,599 as of 2026-10-25" in the table and in prose.
6. **No Review / AggregateRating schema.** `Product` + `Offer` with `priceValidUntil`, or `ItemList`.
7. **Say what was not done.** One sentence near the verdict: manufacturer spec pages, one independent
   measured review of the earlier generation, Consumer Reports' untested preview and owner reports; the
   unit was not handled here.
