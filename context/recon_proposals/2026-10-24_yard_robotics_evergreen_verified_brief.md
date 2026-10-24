# Verified Brief: yard_robotics — 2026-10-24 (evergreen)

Topic: a robotic mower's published acreage is a best-case, tolerance-banded number, and the
specification table itself publishes the derating factors a buyer should apply.

All rows fetched 2026-10-24 with the gate's own fetcher
(`citation_hub_dossier.fetch_source`), and every figure cell was run through
`figure_evidence` before it was written.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Sizing column | The 1-acre headline on the Automower 420 iQ is published as three different areas: a ±20% band, a 1-acre systematic figure and a 0.5-acre irregular figure | VERIFIED | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-420-iq/ | "Capacity Lawn Size (±20%) 1 acre Area capacity - irregular 0.5 acre Area capacity - systematic 1 acre" |
| 2 | Slope column | The same machine's maximum slope is 15 % at the boundary and 45 % inside the installation — a third | VERIFIED | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-420-iq/ | "Maximum slope performance at boundary 15 % Maximum slope performance inside installation 45 %" |
| 3 | Slope gloss | The vendor's own FAQ glosses the interior figure only, in degrees | VERIFIED | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-420-iq/ | "It can handle steep slopes of up to 45% (approximately 24 degrees) inside the boundary area." |
| 4 | Duty cycle | 84 minutes of mowing per charge against 54 minutes of charging — the machine cuts 60.9 % of its own clock | VERIFIED | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-420-iq/ | "Typical mow time on one charge 84 min Typical charging time 54 min" |
| 5 | Price | The 420 iQ lists at $3,299.99 | VERIFIED | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-420-iq/ | "Price from $3,299.99" |
| 6 | Second model, same columns | The 435 iQ AWD publishes 1.3 acre (±20 %) against 0.9 acre irregular, and 50 % boundary against 70 % interior | VERIFIED | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-435-iq-awd/ | "Lawn Size (±20%) 1.3 acre Area capacity - irregular 0.9 acre Area capacity - systematic 1.3 acre" · "Maximum slope performance at boundary 50 % Maximum slope performance inside installation 70 %" |
| 7 | Second model, self-contradiction | The 435 iQ AWD's own FAQ answers "maximum lawn size" with the irregular figure, 0.9 acres, not the 1.3-acre spec line | FLAGGED | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-435-iq-awd/ | "The Automower® 435 iQ AWD is designed to manage complex lawns and rough terrain up to 0.9 acres in size." |
| 8 | Second model, duty cycle | 145 minutes mowing per charge against 45 minutes charging | VERIFIED | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-435-iq-awd/ | "Typical mow time on one charge 145 min Typical charging time 45 min" |
| 9 | Second vendor, capacity basis | Navimow publishes mowing area *per charge* well below its recommended lawn size: 265 m² against a recommended 800–2000 m² | VERIFIED | https://navimow.segway.com/ | "Mowing area per charge i208 / i215 / i220 LiDAR: 265 m² / 426 m² / 560 m² Recommended for 800 ㎡ - 2000 ㎡ lawn size." |
| 10 | Second vendor, entry tier | The same split on the AWD (all-wheel drive) tier: 125 m² and 250 m² per charge against a 500–1000 m² recommendation | VERIFIED | https://navimow.segway.com/ | "Mowing area per charge i205 / i208 AWD: 125 m² / 250 m² Recommended for 500 - 1000 m² lawn size." |
| 11 | Second vendor, slope ladder | Navimow's published max slope rises by model: 45 % (24°) on the i2 AWD and i2 LiDAR, 55 % (29°) on the LiDAR Pro, 84 % (40°) on the X4 | VERIFIED | https://navimow.segway.com/ | "i2 AWD Max 45% (24°)" · "i2 LiDAR Pro Max 55% (29°)" · "X4 Series Max 84% (40°)" |
| 12 | Price ladder, low rung | Kress lists the ¼-acre KR161 at $2,799.98 | VERIFIED | https://www.kress.com/en-us/robotic-mowers | "Kress RTKⁿ ¼-acre robotic lawn mower KR161 $ 2,799 .98" |
| 13 | Price ladder, mid rung | The 1¼-acre KR174 lists at $4,199.98 — $1,400 more for five times the rated acreage | VERIFIED | https://www.kress.com/en-us/robotic-mowers | "Kress RTKⁿ 1¼-acre robotic lawn mower with OAS (Obstacle Avoidance System) KR174 $ 4,199 .98" |
| 14 | Price ladder, top rung | The 7-acre KR237 lists at $15,699.98 | VERIFIED | https://www.kress.com/en-us/robotic-mowers | "Kress RTKⁿ 7-acre robotic lawn mower with OAS (Obstacle Avoidance System) KR237 $ 15,699 .98" |
| 15 | Promotional price, caveat | Kress's sale prices carry a dated cutoff, so no sale price may be load-bearing in a durable piece | VERIFIED | https://www.kress.com/en-us/robotic-mowers | "Offer valid through December 31, 2026, or while supplies last." |
| 16 | Consumable interval | Blade sets are rated in mowing hours, not months | VERIFIED | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-420-iq/ | "Calculated based on recommended usage of 500-1000 mowing hours per blade set." |

## Derived figures (arithmetic, not sourced — recompute in the final before the push)

| Figure | Formula | Endpoints (both above) |
|---|---|---|
| 0.4 acre usable | 1 acre × 0.8 (bottom of the ±20 % band) × 0.5 (irregular ÷ systematic column) = 0.40 | row 1 |
| 0.72 acre usable on the 435 | 1.3 × 0.8 × (0.9 ÷ 1.3) = 0.72 | row 6 |
| $8,249.97 per usable acre | $3,299.99 ÷ 0.4 | rows 1, 5 |
| $3,300 per systematic acre | $3,299.99 ÷ 1 | rows 1, 5 |
| Kress $/rated acre | 2,799.98 ÷ 0.25 = 11,199.92 · 3,199.98 ÷ 0.5 = 6,399.96 · 3,699.98 ÷ 0.75 = 4,933.31 · 4,199.98 ÷ 1.25 = 3,359.98 · 9,199.98 ÷ 3 = 3,066.66 · 14,499.98 ÷ 6 = 2,416.66 · 15,699.98 ÷ 7 = 2,242.85 | rows 12–14 |
| 4.99× spread, quarter-acre vs seven-acre | 11,199.92 ÷ 2,242.85 = 4.99 | rows 12, 14 |
| 60.9 % cutting duty, 420 iQ | 84 ÷ (84 + 54) = 0.6087 | row 4 |
| 76.3 % cutting duty, 435 iQ AWD | 145 ÷ (145 + 45) = 0.7632 | row 8 |
| 3.0× Navimow per-charge gap | 800 ÷ 265 = 3.02; at the top of its band 2,000 ÷ 265 = 7.55 | row 9 |
| m² to sq ft | 265 m² ≈ 2,852 sq ft; 800 m² ≈ 8,611 sq ft; 2,000 m² ≈ 21,528 sq ft (× 10.7639) | row 9 |

## Drafter constraints

- **Every row is a vendor claim, not a field measurement.** No page reached by the gate publishes a
  measured coverage test. The article says so plainly; the derating is arithmetic performed on the
  vendor's own published columns, and must never be written as "we tested" or as a measured result.
- **Do not use Kress sale prices.** They expire on a printed date (row 15). Only the list prices.
- **The 435's 0.9-versus-1.3 contradiction (row 7) is a FLAGGED reading**: the spec line says 1.3 acre
  and the page's own FAQ answer says 0.9 acres. Write it as the page disagreeing with itself; do not
  pick one and call the other an error.
- **"Boundary" is the spec table's own word.** Do not invent a mechanism for why the boundary figure is
  lower (wire burial, dock approach, guide wire). State that the table publishes two slope figures and
  that the boundary one is the smaller.
- Percent slope is not degrees: the 420's 45 % is glossed by the vendor as "approximately 24 degrees"
  (row 3). Keep the two units attached to their own numbers.
- No claim about contract mowing prices, break-even months, battery replacement costs or snow clearing
  — none of those cleared a fetchable primary anchor in this run.
