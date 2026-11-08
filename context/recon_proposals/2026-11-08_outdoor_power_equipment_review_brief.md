# Review Brief: outdoor_power_equipment — 2026-11-08

**Vertical:** outdoor_power_equipment
**Persona:** homeowner_pro
**Decision the reader is facing:** whether a paved two-car driveway gets cleared this winter by a $149.99 twelve-inch plug-in power shovel or a $249.99 twenty-two-inch corded thrower, when both plug into the same 120-volt outdoor outlet and both are claimed to suit a multi-car drive.
**Format:** comparison
**Price as of:** 2026-11-08
**Verdict:** Buy the Snow Joe SJ627E at $249.99 for any paved driveway you clear from an outlet: at 840 pounds a minute and a 13-inch intake it takes a 10-inch storm in one pass, where the Toro clears 6 inches at a time and needs two. Buy the Toro Power Shovel 38361 at $149.99 only for a deck, steps or a narrow walk, where its 12-inch cut fits between railings and 20 feet of throw is already more than the space it works in.
**De-dup:** `2026-10-25_your-550-battery-spare-is-wrong` is this vertical's last review and prices a battery two-stage kit's spare pack, not a corded machine; `2026-10-31_why-37667-snow-throwers-failed-winter` is the corded-thrower story already on the front, and it argues a cold rating and a recall of 37,667 Benchmark units with no price anywhere; `2026-11-01_your-3000-psi-washers-11-gpm-trap` is the last review in this vertical and prices pressure washers. A corpus grep for "power shovel", "SJ627E" and "corded snow" across `published/`, `context/drafts/` and `context/recon_proposals/` returns only those files plus two briefs where a snow angle was scored and dropped; no artifact prices a corded snow machine or compares pass counts against intake depth.
**Thesis:** In the corded class the two numbers that decide a driveway are the intake depth and the amp draw, not the clearing width the box leads with: 6 inches of depth doubles the pass count in any storm over 6 inches, and 15 amps is the whole capacity of the outlet the machine hangs off, which is why the maker caps its own extension cord at 100 feet and 12 gauge there. The cheap shovel is the dearer machine per pound of snow.

**Lead:** The vertical's own beats, `context/verticals.json` `primary_angles` #1 ("two-stage battery snow blower versus power shovel versus heated driveway mat: cost per inch cleared"), read at the moment of purchase: the second week of November, with the first plowable storm of the season in the forecast and a homeowner_pro who wants payback math and gotchas rather than a spec-sheet recital. This is the sub-$300 end of the same angle — the two machines a budget buyer actually puts side by side at the store, one of them a shovel on wheels. GSC carried **0 candidates** for this vertical (`context/recon_proposals/2026-11-07_gsc_outdoor_power_equipment_opportunities.md`), a bonus signal only, never a veto on a young site. The subject comes from evidence: the manufacturer pages now publish both machines' per-minute capacity, depth of cut, amp draw and cord limits, and Popular Mechanics' test editor has already stated the class limit in one sentence ("15-amp motors that run on the power an outlet can provide"), so the article can settle what the marketing skirts.

| Product | Price | Source | Note |
|---|---|---|---|
| Snow Joe SJ627E | $249.99 | https://shopjoe.com/products/snow-joe-sj627e-electric-snow-blower-22-inch-15amp-w-dual-led-lights | 22 in wide, 13 in deep, 840 lb/min, 25 ft throw, 15 amp, in stock on the maker's own store |
| Toro Power Shovel 38361 | $149.99 | https://www.toro.com/en/product/38361 | 12 in wide, 6 in deep, 300 lb/min, 20 ft throw, 7.5 amp motor row; the maker lists $149.99 and routes to dealers |

| # | Source | URL | Retrieved | Figure | Measured |
|---|---|---|---|---|---|
| 1 | Toro — 38361 product page, price block | https://www.toro.com/en/product/38361 | 2026-11-08 | $149.99 | the manufacturer's listed price, printed as "$149.99 USD" beside "Model: 38361"; the page routes to dealers rather than selling direct |
| 2 | Toro — 38361, key features | https://www.toro.com/en/product/38361 | 2026-11-08 | Up to 4 Car Driveway | the four-car claim qualified in the same bullet by "up to 6-in of snow at a time" |
| 3 | Toro — 38361, specifications: capacity | https://www.toro.com/en/product/38361 | 2026-11-08 | 300 lbs | "Capacity per Minute 300 lbs / 136 kg" — vendor-rated, not measured |
| 4 | Toro — 38361, specifications: motor amps | https://www.toro.com/en/product/38361 | 2026-11-08 | 7.5 Amps | "Motor Amps 7.5 Amps" |
| 5 | Toro — 38361, specifications: motor type | https://www.toro.com/en/product/38361 | 2026-11-08 | 15 Amp Series Wound Electric | the row two below row 4, naming a 15-amp motor type for the same machine — the table contradicts itself and no page resolves it |
| 6 | Toro — 38361, specifications: depth | https://www.toro.com/en/product/38361 | 2026-11-08 | 6 in / 15 cm | both "Ideal Snow Depth" and "Intake Height" read 6 in |
| 7 | Toro — 38361, specifications: throw | https://www.toro.com/en/product/38361 | 2026-11-08 | Up to 20 ft | "Throw Distance Up to 20 ft / 6 m", with the page's own caveat that throw varies with conditions |
| 8 | Snow Joe — SJ627E product page, price | https://shopjoe.com/products/snow-joe-sj627e-electric-snow-blower-22-inch-15amp-w-dual-led-lights | 2026-11-08 | $249.99 | "Regular price $249.99 / Sale price $249.99" — no markdown in effect, so $249.99 is the standing price on 2026-11-08 |
| 9 | Snow Joe — SJ627E, description | https://shopjoe.com/products/snow-joe-sj627e-electric-snow-blower-22-inch-15amp-w-dual-led-lights | 2026-11-08 | 840 lbs | "moves up to 840 lbs of snow per minute" — vendor-rated |
| 10 | Snow Joe — SJ627E, description: path | https://shopjoe.com/products/snow-joe-sj627e-electric-snow-blower-22-inch-15amp-w-dual-led-lights | 2026-11-08 | 22-inches wide by 13-inches deep | "clearing a path up to 22-inches wide by 13-inches deep in a single pass" |
| 11 | Snow Joe — SJ627E, feature bullet: throw | https://shopjoe.com/products/snow-joe-sj627e-electric-snow-blower-22-inch-15amp-w-dual-led-lights | 2026-11-08 | 25 ft | "180° directional chute throws snow up to 25 ft" |
| 12 | Snow Joe — SJ627E, description: motor | https://shopjoe.com/products/snow-joe-sj627e-electric-snow-blower-22-inch-15amp-w-dual-led-lights | 2026-11-08 | 15-amp unit | "This ultra-powerful 15-amp unit with ample 22-inch width" |
| 13 | Snow Joe — SJ623E (18-inch sister model) spec table: cord cap | https://shopjoe.com/products/snow-joe-ultra-18-inch-15-amp-electric-snow-blower-with-light | 2026-11-08 | Maximum Extension Cord Length (ft.) 100 | the maker's own cord limit for a 15-amp machine of the same family; the sister model is listed as sold out, so this is cited as documentation, not as a buy |
| 14 | Snow Joe — SJ623E, spec table: cord gauge | https://shopjoe.com/products/snow-joe-ultra-18-inch-15-amp-electric-snow-blower-with-light | 2026-11-08 | Minimum Extension Gauge (100ft.) 12 | 12 gauge at 100 ft, with 14 gauge at 25 ft in the neighbouring row — the run length, not the machine, sets the copper |
| 15 | Popular Mechanics — best electric snow blowers | https://www.popularmechanics.com/home/lawn-garden/a38146316/best-electric-snow-blowers | 2026-11-08 | 15-amp motors that run on the power an outlet can provide | the publisher's framing of the class limit, attributed to its test editor Brad Ford, beside the same page's note that a power cord "substantially reduces their range" |

## Derived arithmetic (computed from printed endpoints, never estimated)

- **Snow per amp.** 300 lb/min ÷ 7.5 A = **40.0**; 840 ÷ 15 = **56.0**. The wide machine moves **40% more snow per amp** than the shovel, so it is not simply a bigger motor.
- **Watts at the wall.** 7.5 A × 120 V = **900 W**; 15 A × 120 V = **1,800 W**. The two machines draw 2× apart from the same outlet.
- **Dollars per pound of snow a minute.** $149.99 ÷ 300 = **$0.500**; $249.99 ÷ 840 = **$0.298**. The $100-cheaper machine costs **1.68×** as much per unit of rated throughput.
- **Dollars per inch of clearing width.** $149.99 ÷ 12 = **$12.50**; $249.99 ÷ 22 = **$11.36**. The width ladder is nearly flat — the price is buying throughput and depth, not width.
- **Passes for a 24-foot-wide driveway.** 288 in ÷ 12 = **24 passes**; 288 ÷ 22 = 13.1, so **14 passes** with the cut finished at the edge. **1.7×** the passes at equal depth.
- **Passes in a 10-inch storm.** The 13-inch intake takes it in **one pass**; the 6-inch intake needs **two** (6 in + 4 in), so 24 × 2 = **48 passes** against 14 — **3.4×**, and that is the number the two headline capacities never state.
- **The reach the outlet imposes.** A 15-amp machine's own spec table caps the cord at 100 ft and demands 12 gauge there, against 14 gauge at 25 ft: one drive-width of snow is cleared from whatever length of copper the outlet allows.

## What the article must carry

- **Depth, not width, is the axis.** Rows 6 and 10: 6 in against 13 in. Any storm deeper than 6 in doubles the shovel's pass count, and rows 2 and 10 show the two makers describe their driveways in the same words ("Up to 4 Car Driveway" against "large driveways") while publishing a 2.17× depth difference. That is the piece's finding.
- **The amp draw is the class ceiling, and the vendor documentation admits it.** Rows 12–15: 15 amp is the largest motor in this class because that is what an outlet gives (Popular Mechanics says it in one sentence), and the maker's own spec table then caps the cord at 100 ft with 12 gauge. Present the cord as part of the purchase, priced by gauge and length, and do not invent a price for one.
- **Toro's own spec table contradicts itself on amps** (rows 4 and 5: "Motor Amps 7.5 Amps" beside "15 Amp Series Wound Electric"). Say that plainly and say what it means: the 7.5-amp row is the one that governs the arithmetic above, and no page on either host resolves the contradiction. Do not pick the number that flatters the article.
- **Every capacity figure is a vendor rating.** Rows 3, 7, 9, 11: pounds per minute and throw distance are the makers', not measurements by this desk or by any source in the table. The only independent voice here is Popular Mechanics, and it is a framing of the class limit, not a test of either machine.
- **The trap is the outlet, and it has two halves.** The cord (rows 13, 14) and the circuit behind it: 1,800 W is the full rating of a 15-amp household branch circuit, so the wide machine wants an outlet with nothing else drawing on it, and a long thin cord is the usual reason a 15-amp thrower trips a breaker mid-drive. Present the circuit as arithmetic on the printed figures (row 12 × 120 V), attributed as such, and keep the buying advice to the cord the maker specifies.
- **The four-car claim is conditional, and the condition is the depth** (row 2). The shovel is not oversold on width; it is oversold on what a four-car driveway looks like in February.
- **Verdict by situation**, not a single ranking: a deck, steps or a walk narrower than 4 ft; a two-car drive with an outlet within reach; a drive longer than 100 ft from the outlet (no corded machine of either size reaches it, and the article must say so rather than imply a longer cord fixes it).
- **Mandatory honesty paragraph:** this review is built from two manufacturer product pages, one sister-model spec table and one publisher's roundup; neither machine was handled, run or measured, and no capacity figure here is a test result. No Review or AggregateRating schema — `Product` + `Offer` with the price and `priceValidUntil`, or a plain `ItemList`.
- **Verdict block links:** the vertical hub https://wellroost.com/categories/outdoor-power-equipment/ and the live ownership calculator https://wellroost.com/calculators/true-cost-of-ownership/ (both probed HTTP 200 on 2026-11-08). There is no snow-specific calculator on either front; do not invent one.
- **One earned inline internal link** in the body, site-relative, from the live corpus; the vertical hub or `/why-37667-snow-throwers-failed-winter/` are the justified targets, and the sentence must read as an observation rather than a nudge.

## Drafter rulings (labels the article must keep)

1. Prices are the manufacturers' own listed prices on 2026-11-08. Snow Joe's page shows regular and sale price at the same $249.99, so call it the standing price, not a markdown. Toro lists $149.99 and routes the buyer to a dealer, so say the dealer may price it differently; do not quote a retailer price that was not fetched.
2. "Pounds per minute", "throw distance" and "driveway size" are vendor claims under vendor conditions. They are not measurements by this desk.
3. Do not rank the two machines on a single "clearing power" number. The capacities are published by two different makers with no shared test, which is why the article compares pass counts instead.
4. The sister model in rows 13 and 14 is listed as sold out and exists here only as the maker's published cord requirement. Name it as the 18-inch model in the same family, never as an alternative purchase.
5. The article must not imply use: no first-person claim that a machine was run, measured, tried or owned, and no claim of time spent with one. It says what the two pages publish, what the publisher observed, and that nothing was handled.
6. The 1,800 W figure is the article's arithmetic on the printed 15 amp and 120 V, attributed as arithmetic in the sentence. Do not attribute it to any source in the table.

## Gate result

<!-- review-gate:start -->
<!-- review-gate: helper=review_gate.py format=comparison rows=15 products=2 fetched=15 hosts=3 price_as_of=2026-11-08 checked_at=2026-11-08T14:36:29+00:00 -->
<!-- review-gate:end -->
