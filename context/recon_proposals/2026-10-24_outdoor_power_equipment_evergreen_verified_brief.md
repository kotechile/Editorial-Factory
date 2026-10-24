# Verified Brief: outdoor_power_equipment — 2026-10-24

**Archetype:** evergreen · **Slug:** your-heated-mat-costs-54-a-square-foot · **Shot:** 2026-10-24
**Brief of record:** `context/recon_proposals/2026-10-24_outdoor_power_equipment_evergreen_brief.md` (evergreen gate PASS, rows=15 fetched=15 sources=15 hosts=5)

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | blower capacity | EGO claims one charge of two 7.5 Ah 56 V packs clears an 18-car driveway at 8 inches, with a 24-inch width and 20-inch intake | VERIFIED | https://www.egopowerplus.com/two-stage-snow-blower-snt2400 | "Peak Power™ technology combines the power of any two EGO POWER+ 56V ARC Lithium™ batteries Throws snow up to 50 feet Clears up to an 18-car driveway with 8 inches of snow on a single charge when used with the two recommended 7.5Ah ARC Lithium™ batteries 24-inch clearing width/20 inch intake height" |
| 2 | blower capacity | The claim names no area, no test method and no snow density — so it cannot be converted into a per-square-foot figure | FLAGGED | https://www.egopowerplus.com/two-stage-snow-blower-snt2400 | The Tech Specs block is the whole evidence: "…Clears up to an 18-car driveway with 8 inches of snow on a single charge…". No square footage, no snow water equivalent, no runtime in minutes appears anywhere on the page. |
| 3 | blower energy | Two 56 V 7.5 Ah packs = 840 Wh per charge (derived: 2 × 56 × 7.5) | VERIFIED (derived) | https://www.egopowerplus.com/two-stage-snow-blower-snt2400 | "combines the power of any two EGO POWER+ 56V ARC Lithium™ batteries" + "two recommended 7.5Ah ARC Lithium™ batteries" |
| 4 | blower energy | 840 Wh at the 2025 U.S. residential average is 14.5¢ (derived: 0.84 kWh × 17.30¢) | VERIFIED (derived) | https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php | "The annual average retail electricity prices by major types of utility customers in 2025 were: residential 17.30¢ per kWh" |
| 5 | mat load | A 24" × 10' 120 V HeatTrak driveway mat draws 5.8 amps | VERIFIED | https://www.heattrak.com/products/heated-snow-ice-melting-driveway-mat | "Sizing and Amps 24\" x 10' (60.96 cm x 3.04 m) \| 120V Mats are 5.8-amps each \| 240V Mats are 2.7-amps each +/- 10%" |
| 6 | mat load | A 24" × 20' 120 V HeatTrak mat draws 11.7 amps (cross-check on the density) | VERIFIED | https://www.heattrak.com/products/heated-snow-ice-melting-driveway-mat | "24\" x 20' (60.96 cm x 6.1 m) \| 120V Mats are 11.7-amps each \| 240V Mats are 5.4-amps each +/- 10%" |
| 7 | mat density | 5.8 A × 120 V over 20 sq ft = 696 W ≈ 34.8 W/sq ft (derived); the 24" × 20' mat gives 35.1 W/sq ft, so the nameplate density holds across sizes | VERIFIED (derived) | https://www.heattrak.com/products/heated-snow-ice-melting-driveway-mat | Row 5 / row 6 amps; 24" x 10' = 20 sq ft, 24" x 20' = 40 sq ft (both from the size table above) |
| 8 | mat price | The 24" × 10' driveway mat lists at $1,075.00 — $53.75 per square foot (derived: $1,075 ÷ 20) | VERIFIED (price) / row cannot carry the gate | https://www.heattrak.com/products/heated-snow-ice-melting-driveway-mat | "Heated Snow & Ice Melting Driveway Mat Sale price $ 1,075.00 USD SKU: HTD24-10 … Includes Power Unit & 26ft Total Cable Length Size: 24\" x 10'" |
| 9 | mat price | The 20" × 60" walkway mat lists at $229.99 — $27.60 per square foot (derived: $229.99 ÷ 8.33) | VERIFIED | https://www.heattrak.com/ | "Heated Snow Melting Walkway Mat - Standard/Long - 20\"x60\" Sale price $ 229.99 USD" |
| 10 | mat performance | HeatTrak states a melt rate of up to 2 inches per hour, operating about 40 degrees above ambient | VERIFIED | https://www.heattrak.com/pages/faqs | "operating at approximately 40 degrees above ambient temperature. This melts existing snow and ice and helps prevent new accumulation at a rate of up to 2 inches per hour." |
| 11 | mat circuit | No more than 13 amps on a single plug; one GFCI power unit connects up to 13 amps | VERIFIED | https://www.heattrak.com/pages/faqs | "Yes, but no more than 13 amps should be on a single plug." / "One Power Unit per set (not per mat). Connects up to 13 amps." |
| 12 | mat lifetime | HeatTrak states a 5–6 year mat lifespan | VERIFIED | https://www.heattrak.com/pages/faqs | "On average, HeatTrak mats have a lifespan of 5–6 years" |
| 13 | mat positioning | HeatTrak sells the driveway mat as a single tire track, not full coverage | VERIFIED | https://www.heattrak.com/pages/faqs | "They lay as a track for one tire, allowing the car to travel in and out of a snowy driveway." |
| 14 | mat running cost | HeatTrak's headline running cost is about $0.18 per hour, $1.80 for ten hours — with no configuration stated | FLAGGED | https://www.heattrak.com/pages/faqs | "The average cost to operate a HeatTrak system is only about $0.18 per hour . Running them for 10 hours during a snowfall costs about $1.80." — at 17.30¢/kWh that $0.18/hour implies 1.04 kWh/hour, i.e. about 30 sq ft of mat at 34.8 W/sq ft, so the figure describes a walkway-scale set rather than a driveway. The page never names the configuration; the article must not scale it to a driveway without recomputing. |
| 15 | embedded design load | Embedded snow-melting design density is 50 W/sq ft, stated with a worked 100 sq ft example | VERIFIED | https://www.warmlyyours.com/en-US/snow-melting | "Example: 100 sq ft at 50 W/sq ft Per Energized Hour $1.00 Six Energized Hours $6.00 This example uses an illustrative electricity rate of $0.20/kWh : 100 sq ft × 50 W/sq ft ÷ 1,000 = 5 kW; 5 kW × $0.20 = $1.00 per energized hour." |
| 16 | embedded design load | A 400 sq ft full-coverage driveway is 20 kW — $4.00 per energized hour, $24.00 for six hours at the vendor's illustrative $0.20/kWh | VERIFIED | https://www.warmlyyours.com/en-US/snow-melting | "For example, a 400 sq ft full-coverage driveway draws 20 kW: $4.00 per energized hour, or $24.00 for six energized hours." |
| 17 | embedded sizing | A typical driveway is 400–800 sq ft | VERIFIED | https://www.warmlyyours.com/en-US/snow-melting | "Typical driveways: 400–800 sq. ft." |
| 18 | embedded capital | Professional installation runs $10–$25 per square foot, materials and labor included | VERIFIED | https://www.warmlyyours.com/en-US/snow-melting | "Professional installation for a heated driveway typically costs between $10 and $25 per square foot, including materials and labor." |
| 19 | embedded performance | WarmlyYours states 1"–3" of snow per hour as the design band, with above 3" treated as blizzard conditions | VERIFIED | https://www.warmlyyours.com/en-US/snow-melting | "these snow melting systems are designed to melt 1\" - 3\" of snow per hour. Anything above 3\" per hour is typically considered blizzard conditions." |
| 20 | corded shovel | The Snow Joe electric snow shovel is 11 inches wide with a 10 amp motor at $124.99 | VERIFIED | https://snowjoe.com/collections/snow-blowers | "Snow Joe Electric Snow Shovel \| 11-Inch \| 10 Amp Motor\| Headlights … Regular price $124.99 Sale price $124.99" |
| 21 | cordless shovel | The 24 V IONMAX 4.0 Ah pack lists at $89.97, and the shovel bundle with that pack at $199.99 | VERIFIED | https://snowjoe.com/collections/snow-blowers | "Snow Joe CERTIFIED AUTHENTIC IONMAX 24-Volt* 4.0-Ah Lithium-ION Battery … Regular price $89.97" / "Snow Joe 24-Volt* IONMAX Cordless Snow Shovel Bundle \| W/ 4.0-Ah Battery, Charger, Cover, Ice Scraper and Extended Warranty … Regular price $199.99 … Regular price $300.00" |

## Derived figures — every one recomputed here, and the article must show its inputs

| Figure | Inputs (all cited above) | Result |
|---|---|---|
| Energy in one blower charge | rows 3 | 840 Wh = 0.84 kWh |
| Cost of one blower charge | rows 3 + 4 | 0.84 × 0.1730 = **14.5¢** |
| Driveway-mat density | rows 5, 7 | 696 W ÷ 20 sq ft = **34.8 W/sq ft** |
| Cost per sq ft per inch of melt | rows 7, 10, 4 | 34.8 W × 0.5 h = 17.4 Wh/sq ft-in → **$0.0030/sq ft-in** |
| One blower charge expressed as melt | rows 3 + above | 840 ÷ 17.4 = **≈48 sq ft of 1-inch snow** (≈6 sq ft at 8 inches) |
| Mat area per 120 V plug | rows 11, 7 | 13 A × 120 V ÷ 34.8 = 1,560 W → **≈45 sq ft** |
| 200 sq ft of mat, six energized hours | rows 7, 4 | 200 × 34.8 W × 6 h = 41.8 kWh → **≈$7.23** |
| Mat storm vs blower charge | above | $7.23 ÷ $0.145 = **≈50×** |
| 400 sq ft of portable mat | rows 8 | 400 ÷ 20 = 20 mats → **$21,500** at list |
| 400 sq ft embedded, installed | rows 17, 18 | 400 × $10–$25 = **$4,000–$10,000** |
| Embedded 400 sq ft draw in amps | rows 16 | 20 kW ÷ 240 V = **≈83 A** |
| HeatTrak's $0.18/hour implied area | rows 14, 4 | 1.04 kW ÷ 34.8 W/sq ft = **≈30 sq ft** |
| Corded shovel running cost | row 20 + 4 | 10 A × 120 V = 1.2 kW → **20.8¢/hour** |
| Cross-check: melt physics | row 7, 10 | 17.4 Wh/sq ft-in is the same order as the latent heat of the water in an inch of snow (~0.5 lb/sq ft at 10% density × 144 Btu/lb ≈ 21 Wh) — the vendor's wattage and melt rate are mutually consistent, so the arithmetic is safe to print |

## Drafter's rulings

- **Never convert the EGO "18-car driveway" claim into square feet.** Row 2 is the ruling: the area is unpublished. The article states the vendor claim as a capacity claim and then uses the pack energy (rows 3–4), which is arithmetic on printed nameplate values, for every comparison.
- **Never blend 34.8 W/sq ft (portable mat) with 50 W/sq ft (embedded design).** They are different products from different vendors; each dollar figure is recomputed at its own density and at the EIA rate, and the vendor's illustrative $0.20/kWh is quoted only when reproducing the vendor's own worked example.
- **Never scale HeatTrak's "$0.18/hour" to a driveway.** Row 14: the basis is unstated and the arithmetic puts it at walkway scale. Print the vendor's number as the vendor's number, then show the recomputed 200 sq ft figure as *our* arithmetic.
- **Never merge the two melt rates into one spec.** Row 10 is a portable mat's "up to 2 inches per hour"; row 19 is an embedded system's 1"–3" design band with a 3"-per-hour blizzard threshold. Attribute each to its own page.
- **Never present $21,500 as HeatTrak's recommendation.** Row 13: the mat is sold as one tire track. The figure is list-price arithmetic for 400 sq ft of track, labelled as arithmetic, and the article says plainly that the vendor positions the mat for a track.
- **Prices are as of 2026-10-24 and the rate is EIA's 2025 annual average** — both stated in the body, not only in the footer.
- **No hands-on claim.** This desk has no hardware. Nothing in the article was tested, and the article must not say "we tried", "in our test" or "after a season with".
- **The article's job is a decision rule**, not a product ranking: pay for melting only where bare pavement over a small area is the requirement, and count square feet and amps before dollars of electricity.
