# Verified Brief: outdoor_power_equipment (review, comparison) — 2026-11-01

Source of record: `context/recon_proposals/2026-11-01_outdoor_power_equipment_review_brief.md` (review gate PASS,
rows=20 fetched=20 hosts=3 products=3, marker 2026-11-01T14:36:04+00:00). Prices are the manufacturer's own
store prices read on 2026-11-01, mid-markdown.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | 2,300 price | The 2,300 PSI Gen 2 (SKU 5128502 / GPW2303A) sells for $312.99 | VERIFIED | https://www.greenworkstools.com/products/2300-psi-1-2-gpm-cold-water-electric-pressure-washer | "SKU 5128502 \| MODEL# GPW2303A Sale price $ 312 . .99 $ 399 . 99 SAVE $87.00 (21%)" |
| 2 | 2,300 spec | Its peak pressure and peak flow are published at different conditions | VERIFIED | same as 1 | "2300 Max PSI at 1.2 GPM water flow (2.3 GPM flow at 100 PSI)." |
| 3 | 2,700 price | The 2,700 PSI (SKU 5128402 / GPW2702A) sells for $379.99, 15% off | VERIFIED | https://www.greenworkstools.com/products/2700-psi-2-3-gpm-cold-water-electric-pressure-washer | "SKU 5128402 \| MODEL# GPW2702A Sale price $ 379 . .99 $ 449 . 99 SAVE $70.00 (15%)" |
| 4 | 2,700 spec | Same construction at the middle rung | VERIFIED | same as 3 | "2700 Max PSI at 1.2 GPM water flow (2.3 GPM flow at 100 PSI)." |
| 5 | 3,000 price | The 3,000 PSI Gen 2 (SKU 5128802 / GPW3002A) sells for $349.99, 30% off | VERIFIED | https://www.greenworkstools.com/products/3000-psi-2-0-gpm-cold-water-electric-pressure-washer | "SKU 5128802 \| MODEL# GPW3002A Sale price $ 349 . .99 $ 499 . 99 SAVE $150.00 (30%)" |
| 6 | 3,000 spec | The highest-PSI unit carries the lowest flow at pressure | VERIFIED | same as 5 | "3000 Max PSI at 1.1 GPM water flow (2.0 GPM flow at 100 PSI)." |
| 7 | Motor | All three carry the same 14-amp brushless motor | VERIFIED | all three product pages | "Motor 14-Amp" in the specification block of each; "Brushless Motor Yes" on the 3,000 and 2,300 pages |
| 8 | Hose and cord | All three ship a 25-ft hose on a 35-ft GFCI cord with five nozzles | VERIFIED | all three product pages | "25' Kink-Resistant Hose … 35' Power Cord - With inline GFCI … Includes Quick Connect Wand - With 15°, 25°, 40°, soap，and turbo nozzle" |
| 9 | Second SKU | A second 3,000 PSI SKU on the same store costs $424.99 | VERIFIED | same as 5 | "$75.00 OFF Sale SKU: 5113902 3000 PSI 2.0 GPM Cold Water Electric Pressure Washer Earn loyalty points $424.99 $ 424 .99 $499.99 SAVE $75.00 (15%)" |
| 10 | Accessory price | The brand's universal 12-inch rotating surface cleaner costs $39.99 | VERIFIED | https://www.greenworkstools.com/products/12-inch-pressure-washer-surface-cleaner-5207402vt | "Universal 12" Rotating Surface Cleaner … $39.99 View Options" |
| 11 | Accessory rating | That cleaner is rated to a maximum of 2,300 PSI | VERIFIED | same as 10 | "Max PSI 2300 PSI" in its Product Specifications block |
| 12 | Cross-brand | A competitor qualifies its headline the same way | VERIFIED | https://www.dewalt.com/product/dwpw2400/2400-psi-electric-pressure-washer | "2400 MAX PSI and 1.1 gpm" beside the footnote "Maximum psi when used with 15-degree nozzle" and "Maximum GPM when used with soap nozzle" |
| 13 | Publisher price | Popular Mechanics lists the same 2,700 PSI model at $379 | VERIFIED | https://www.popularmechanics.com/home/outdoor-projects/a43931284/best-electric-pressure-washers | "$450 $379 NOW 16% OFF" under "Best Overall Greenworks 2,700-psi Electric Pressure Washer" |
| 14 | Publisher spec | The publisher repeats the 2.3 GPM figure without the 100 PSI condition | VERIFIED | same as 13 | "Motor 14 amp … Weight 47 lb … Cleaning Power 2,700 psi … Max Flow 2.3 gpm" |
| 15 | Publisher observation | Flow, not pressure, sets the pace across a surface | VERIFIED | same as 13 | of the Kärcher K 3000 E at "1-gpm flow rate": "means rinsing large patios or long stretches of siding takes a little longer" |
| 16 | Publisher date | The publisher's price carries its own, older date | FLAGGED | same as 13 | page header "Updated: Aug 18, 2026" — its $379 is nearly three months old and is corroboration of $379.99 only, never a second actionable price |
| 17 | Combo | The 2,700 also sells as a 15" surface cleaner and extension combo at $479.98 | VERIFIED (page fetched; not in the review brief's rows) | https://www.greenworkstools.com/products/2700-psi-pressure-washer-w-15-surface-cleaner | "2700 PSI Pressure Washer, 15" Surface Cleaner and Extension Combo Kit … $479.98" |
| 18 | 100 PSI condition | 100 PSI is the low-pressure/rinse end, not a cleaning pressure | FLAGGED (desk reading, no source row) | — | the vendor prints the flow at 100 PSI without naming which nozzle; DEWALT's parallel footnote names the soap nozzle for its max-GPM figure. The article says "the vendor's own low-pressure condition" and never calls 100 PSI a nozzle by name |

## Derived arithmetic (authorised — printed endpoints only)

- Flow at working pressure: 1.2 → 1.2 → 1.1 GPM. **1.1 ÷ 1.2 = 0.917**, i.e. the 3,000 moves 8.3% less water at its peak pressure than the two below it.
- PSI ladder: **3,000 ÷ 2,300 = 1.304** (30.4% taller) against that −8.3%.
- Price order: **$349.99 − $312.99 = $37.00**; **$379.99 − $349.99 = $30.00**.
- **$312.99 ÷ 2,300 = $0.136** per rated PSI; **$379.99 ÷ 2,700 = $0.141**; **$349.99 ÷ 3,000 = $0.117**.
- **$312.99 ÷ 1.2 = $260.83** per GPM at pressure; **$379.99 ÷ 1.2 = $316.66**; **$349.99 ÷ 1.1 = $318.17**.
- Accessory ceiling: **3,000 − 2,300 = 700 PSI** (30.4% above the cleaner's rating).
- Second SKU: **$424.99 − $349.99 = $75.00** for the same headline.

## Drafter rulings

1. Prices are sale prices on 2026-11-01 from the maker's own store; never call them list prices and never promise they hold.
2. "Max PSI" and "Max GPM" are vendor claims under vendor-specified conditions. Neither this desk nor any source here measured them.
3. Do not multiply PSI by GPM into a "cleaning power" figure: rows 2, 4, 6 and 12 show the two numbers are published at different conditions, so the product would describe a state neither machine reaches.
4. Popular Mechanics' $379 (row 13) is three months old (row 16): use it as agreement with $379.99, never as a price to buy at.
5. The 100 PSI condition is the vendor's low-pressure figure (row 18 is FLAGGED): describe it as the pressure the vendor states, and do not name a nozzle the vendor does not name.
6. No first-person claim of use anywhere: no running, measuring, owning or time-with-unit. The "what we did not test" paragraph is mandatory and names the three evidence classes.
7. No Review or AggregateRating schema. `Product` + `Offer` with `priceValidUntil`, or a plain `ItemList`, if any structured data is emitted at all.
8. The verdict block carries the vertical hub and the ownership calculator; the body carries exactly one earned inline internal link, site-relative, verified HTTP 200 before the push.
