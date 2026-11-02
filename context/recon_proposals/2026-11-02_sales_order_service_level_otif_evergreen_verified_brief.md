# Verified Brief: sales_order_service_level_otif — 2026-11-02 (evergreen)

**Archetype:** evergreen · **Companion to:** `context/recon_proposals/2026-11-02_sales_order_service_level_otif_evergreen_brief.md` (evergreen gate: PASS, 5 rows, 5 hosts)

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Critical fractile | The optimal stock level is set by the ratio (p − c)/p inverted through the demand distribution, not by a chosen percentage | VERIFIED | https://en.wikipedia.org/wiki/Newsvendor_model | "q opt = F − 1 ( 7 − 5 7 ) = F − 1 ( 0.285 ) = D min + ( D max − D min ) ⋅ 0.285 = 58.55 ≈ 59" — uniform demand 50–80, price 7, cost 5 |
| 2 | Normal critical values | The service probability converts to a standard-deviation multiple: 1.645 at 95%, 2.326 at 99%, 3.090 at 99.9% | VERIFIED | https://itl.nist.gov/div898/handbook/eda/section3/eda3671.htm | "p 0.999 0.995 0.990 0.975 0.950 0.900 Z p +3.090 +2.576 +2.326 +1.960 +1.645 +1.282 These are critical values for the normal distribution." |
| 3 | Ladder cost | Moving from 95% to 99% service costs roughly 40% more safety stock | VERIFIED | https://metricgate.com/docs/safety-stock-newsvendor | "The service-level sensitivity table shows that the cost of moving from 95% to 99% service is roughly a 40% increase in safety stock." |
| 4 | Carrying rate | A fully loaded carrying rate around a quarter of inventory value, with a worked example | VERIFIED | https://sourceday.com/blog/inventory-holding-costs | "Total inventory value = $1,000,000 Total annual holding costs = $250,000 Holding cost = ($250,000 ÷ $1,000,000) × 100 = 25%" |
| 5 | Model form + worked example | The optimal service level depends on the stock-out cost and the carrying cost over the lead time; a worked example returns ~98.5% | VERIFIED (see FLAG) | https://www.lokad.com/service-level-definition-and-formula | "Let's consider a 1L milk pack at 1.50€ selling price sold with 10% margin (i.e. 0.15€ of gross margin) … The annual carrying cost is 1.50€ … the stock-out cost is 3 time the gross margin, that is to say 0.45€ … we obtain p ≈ 98.5%" |
| 6 | Lead-time scoping | The carrying cost in the model is the annual rate prorated to the lead time | VERIFIED | https://www.lokad.com/service-level-definition-and-formula | "instead of considering the more usual annual carrying cost Hy, we are considering H = d/365 Hy assuming that d is the lead time expressed in days" |
| 7 | Reasonable miss-cost reading | Where goodwill cannot be priced, the stock-out cost may be taken as a multiple of the margin (the page's own example uses 3×) | VERIFIED | https://www.lokad.com/service-level-definition-and-formula | "(2) The stock-out cost includes a minima the gross margin" plus the example's "3 time the gross margin … 0.45€" |

## FLAG — Lokad's 98.5% is not the simple critical ratio

For the same inputs the marginal single-period form returns **96.48%** (0.45 ÷ (0.45 + 4/365 × 1.50)). Lokad's page runs a fuller optimisation in which the stocked quantity moves with the target. The article must quote 98.5% as *Lokad's* result and keep its own worked examples in the marginal form sourced to rows 1–3; it must never restate 98.5% as the output of Cu/(Cu+Co).

## Derived figures the article owns (recompute in the final, do not trust the draft)

| Figure | Derivation | Result |
|---|---|---|
| Cover cost, $200 unit, 45 days, 25% a year | 200 × 0.25 × 45 ÷ 365 | $6.16 |
| 12%-margin item's ratio | 24 ÷ (24 + 6.16) | 79.6% → z 0.83 |
| 30%-margin item's ratio | 60 ÷ (60 + 6.16) | 90.7% → z 1.32 |
| 50%-margin $20 item, 45 days | 10 ÷ (10 + 0.62) | 94.2% → z 1.57 |
| 12%-margin item + $10 late-line charge | 34 ÷ (34 + 6.16) | 84.7% → z 1.02 |
| $0.60 part, 7-day cover, $30 allocated stop cost | 30 ÷ (30 + 0.003) | 99.99% → z 3.73 |
| Blanket 98% multiple | Φ⁻¹(0.98) | 2.05 |
| Over-funding at 98% (12%-margin item) | 2.05 ÷ 0.83 | 2.5× |
| Share of the four-sigma buffer a 98% target holds | 2.05 ÷ 3.73 | 0.55 |
| 95 → 99 ladder | 2.326 ÷ 1.645 | +41.4% (the "roughly 40%" of row 3) |

## Boundaries for the drafter

- **Cycle service level is not fill rate.** The ratio returns the probability an item is in stock at the end of its lead time. The customer-facing fill rate is a different, generally higher number on multi-unit orders. The article says so in The catch and never equates them.
- **No retailer, programme or fine percentage is asserted.** The 5%-of-invoice charge in the sensitivity is a labelled hypothetical the reader replaces with their own contract term; no named retailer's threshold is cited anywhere in the piece.
- **Do not import the order-fill exponent** (line fill raised to the lines on the order) from `2026-10-26_your-98-fill-rate-18-dont-ship`; that mechanism is published and the two pieces must not be merged.
- **No instruction to the reader.** The tactical section reports what operators are doing, in the observer voice the voice gate matches.
- Row 5 is a supplier's own model and is labelled a vendor claim in the brief; it supplies the mechanism and the 3× rule, never a measured benchmark.
