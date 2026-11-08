# Verified Brief: outdoor_power_equipment — 2026-11-08

Review run (`skills/review_comparison.md`), format `comparison`, two corded plug-in snow machines.
Claim extraction from `context/recon_proposals/2026-11-08_outdoor_power_equipment_review_brief.md`
(15 evidence rows, all fetched by `scripts/review_gate.py` on 2026-11-08 — gate PASS, 3 hosts).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Toro 38361 | The Power Shovel 38361 is listed at $149.99 by the manufacturer | VERIFIED | https://www.toro.com/en/product/38361 | "Model: 38361 · UPC/EAN: 21038383613 $149.99 USD" |
| 2 | Toro 38361 | Rated capacity is 300 pounds of snow a minute | VERIFIED | https://www.toro.com/en/product/38361 | "Capacity per Minute 300 lbs / 136 kg" |
| 3 | Toro 38361 | The motor is rated 7.5 amps | VERIFIED | https://www.toro.com/en/product/38361 | "Motor Amps 7.5 Amps" |
| 4 | Toro 38361 | The same spec table names a 15-amp motor type for the same machine | FLAGGED — contradicts row 3 two rows above it on one page; no page on either host resolves it. The drafter must report the contradiction and use row 3 for arithmetic, never the flattering number | https://www.toro.com/en/product/38361 | "Motor Type 15 Amp Series Wound Electric" |
| 5 | Toro 38361 | Intake height and ideal snow depth are both 6 inches | VERIFIED | https://www.toro.com/en/product/38361 | "Ideal Snow Depth 6 in / 15 cm" · "Intake Height 6 in / 15 cm" |
| 6 | Toro 38361 | Rated throw is up to 20 feet | VERIFIED | https://www.toro.com/en/product/38361 | "Throw Distance Up to 20 ft / 6 m" |
| 7 | Toro 38361 | The four-car driveway claim is qualified by a 6-inch snow depth in the same bullet | VERIFIED | https://www.toro.com/en/product/38361 | "Ideal for decks, patios and small driveways that can hold up to 4 cars and up to 6-in of snow at a time" |
| 8 | Snow Joe SJ627E | The machine lists at $249.99, regular and sale price identical | VERIFIED | https://shopjoe.com/products/snow-joe-sj627e-electric-snow-blower-22-inch-15amp-w-dual-led-lights | "Regular price $249.99 Sale price $249.99" |
| 9 | Snow Joe SJ627E | Rated capacity is 840 pounds a minute | VERIFIED | https://shopjoe.com/products/snow-joe-sj627e-electric-snow-blower-22-inch-15amp-w-dual-led-lights | "Snow Joe moves up to 840 lbs of snow per minute" |
| 10 | Snow Joe SJ627E | It clears 22 inches wide by 13 inches deep in one pass | VERIFIED | https://shopjoe.com/products/snow-joe-sj627e-electric-snow-blower-22-inch-15amp-w-dual-led-lights | "clearing a path up to 22-inches wide by 13-inches deep in a single pass" |
| 11 | Snow Joe SJ627E | Rated throw is up to 25 feet | VERIFIED | https://shopjoe.com/products/snow-joe-sj627e-electric-snow-blower-22-inch-15amp-w-dual-led-lights | "180° directional chute throws snow up to 25 ft" |
| 12 | Snow Joe SJ627E | The motor is rated 15 amps | VERIFIED | https://shopjoe.com/products/snow-joe-sj627e-electric-snow-blower-22-inch-15amp-w-dual-led-lights | "This ultra-powerful 15-amp unit with ample 22-inch width" |
| 13 | Snow Joe, 18-inch sister model | The maker caps the extension cord at 100 feet for a 15-amp machine of this family | VERIFIED — documentation only; that model is listed sold out and is not a purchase option | https://shopjoe.com/products/snow-joe-ultra-18-inch-15-amp-electric-snow-blower-with-light | "Maximum Extension Cord Length (ft.) 100" |
| 14 | Snow Joe, 18-inch sister model | 12-gauge wire is the minimum at 100 feet, 14-gauge at 25 feet | VERIFIED | https://shopjoe.com/products/snow-joe-ultra-18-inch-15-amp-electric-snow-blower-with-light | "Minimum Extension Gauge (100ft.) 12" · "Minimum Extension Gauge (25ft.) 14" |
| 15 | Popular Mechanics | The class is limited to 15-amp motors because that is what an outlet supplies | VERIFIED — publisher's framing, not a test of either machine | https://www.popularmechanics.com/home/lawn-garden/a38146316/best-electric-snow-blowers | "They're also limited to smaller, 15-amp motors that run on the power an outlet can provide." |
| 16 | Popular Mechanics | A cord substantially reduces reach | VERIFIED | https://www.popularmechanics.com/home/lawn-garden/a38146316/best-electric-snow-blowers | "power cord substantially reduces their range" |
| 17 | Popular Mechanics | Its test editor dismisses the corded class on convenience grounds | VERIFIED — attribution must stay with the publisher | https://www.popularmechanics.com/home/lawn-garden/a38146316/best-electric-snow-blowers | "Corded is old, out-of-date tech in most cases." — Test Editor Brad Ford |
| 18 | Derived | 900 watts vs 1,800 watts at 120 volts | DERIVED — rows 3, 12 × the 120 V both pages print | rows 3, 12 | arithmetic only; attribute as this desk's arithmetic, never to a source |
| 19 | Derived | $0.500 vs $0.298 per rated pound a minute | DERIVED — rows 1, 9 | rows 1, 2, 9 | 149.99 ÷ 300 and 249.99 ÷ 840 |
| 20 | Derived | 48 passes against 14 for a 10-inch storm on a 24-foot-wide drive | DERIVED — rows 5, 10; assumes straight full-width passes | rows 5, 7, 10 | 288 ÷ 12 × 2 and 288 ÷ 22 |
| 21 | Derived | 40.0 vs 56.0 pounds a minute per amp | DERIVED — rows 2, 3, 9, 12 | rows 2, 3, 9, 12 | 300 ÷ 7.5 and 840 ÷ 15 |
| 22 | Absence | Neither maker publishes a measured capacity, a tested throw distance or a break-in-period figure; no independent test of either machine was retrievable | FLAGGED — a negative claim established by reading the pages; the honesty paragraph must say so | rows 1–17 | no such figure appears on any cited page |

## Rulings carried into drafting

1. Rows 1–17 are the only admissible facts. Every capacity number is a vendor rating, labelled as one in prose.
2. Row 4 is a real defect on the manufacturer's page and is part of the story; the article reports both rows and uses 7.5 amps only for arithmetic it labels as arithmetic.
3. Row 13–14 belong to a sold-out sister model. Name it as such; never present it as a buy.
4. Row 18–21 are this desk's arithmetic on printed endpoints. Say "on the printed figures" in the sentence; do not attribute them to a source.
5. No Review or AggregateRating schema: `Product` + `Offer` with `priceValidUntil`, or a plain `ItemList`.
6. No first-person claim of use; row 22 goes into `## What we did not test` verbatim in substance.
7. Prices carry the date 2026-11-08 in the table and the first mention in prose.
8. The Toro page routes the buyer to a dealer, so the article says a dealer may price it differently and quotes no retailer price (none was fetched).
