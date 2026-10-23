# Verified Brief: consumer_asset_repair_replace_tco — 2026-10-23 (EVERGREEN)
**Archetype:** evergreen · **Gate:** `scripts/evergreen_gate.py` PASS (6 rows, 4 hosts, marker written 2026-10-23T19:33:52Z)
**Brief of record:** `context/recon_proposals/2026-10-23_consumer_asset_repair_replace_tco_evergreen_brief.md`

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | ES-1 | A certified refrigerator is about 9 percent more efficient than one meeting the federal minimum standard | VERIFIED | https://www.energystar.gov/products/refrigerators | "ENERGY STAR certified refrigerators are about 9 percent more energy efficient than models that meet the federal minimum energy efficiency standard." |
| 2 | ES-2 | Twelve years of that advantage is about $150 | VERIFIED | https://www.energystar.gov/products/refrigerators | "By properly recycling your old refrigerator and replacing it with a new ENERGY STAR certified refrigerator, you can save about $150 over the 12-year lifetime of the product." |
| 3 | ES-3 | A refrigerator older than 15 years costs about $95 a year to run | VERIFIED wording / FLAGGED meaning | https://www.energystar.gov/products/refrigerators | "Refrigerators over 15 years old could be costing you more about $95 per year to run." — the sentence does not say whether $95 is the whole running cost or the premium over a new unit; see FLAG-1 |
| 4 | ES-4 | An old unit draws about a fifth more energy than a certified one | VERIFIED | https://www.energystar.gov/products/refrigerators | "On average, an old refrigerator uses about 20% more energy than a model that has earned the ENERGY STAR." |
| 5 | EIA-1 | Residential electricity averaged 17.30¢ per kWh in 2025 | VERIFIED | https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php | "The annual average retail electricity prices by major types of utility customers in 2025 were: residential 17.30¢ per kWh …" (page also states "In 2025, the U.S. annual average retail price of electricity was about 13.63¢ per kilowatthour (kWh)") |
| 6 | EIA-2 | The same efficiency is worth four times more in the most expensive state than the cheapest | VERIFIED | https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php | "In 2025, the annual average retail electricity price for all types of electric utility customers ranged from 35.72¢ per kWh in Hawaii to 8.20¢ per kWh in North Dakota." |
| 7 | ONET-1 | The median appliance repairer earned $24.51 an hour in 2025 | VERIFIED | https://www.onetonline.org/link/summary/49-9031.00 | "Median wages (2025) $24.51 hourly, $50,990 annual" (occupation 49-9031.00, sample titles include "Appliance Repair Technician (Appliance Repair Tech)") |
| 8 | CFR-1 | The federal ceiling for a top-mount automatic-defrost unit is 8.07 × adjusted volume + 233.7 kWh a year | VERIFIED | https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430/subpart-C/section-430.32 | "3. Refrigerator-freezers—automatic defrost with top-mounted freezer without an automatic icemaker 8.07AV + 233.7" |
| 9 | CFR-2 | Those standards date from 2014, with the next step at 2029/2030 | VERIFIED | https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430/subpart-C/section-430.32 | "The following standards apply to products manufactured on or after September 15, 2014, and before the 2029/2030 compliance dates depending on product class" — page banner: "up to date as of 10/21/2026" |
| 10 | ES-5 | Retailers take the old unit when they deliver | VERIFIED | https://www.energystar.gov/products/refrigerators | "Many appliance retailers will pick up and recycle your old refrigerator when you purchase a new one." |
| 11 | ES-6 | The page's own setting guidance is loosely worded | VERIFIED (used as an aside only) | https://www.energystar.gov/products/refrigerators | "Make sure you keep your fridge in an ambient temperature of 35 to 38 degrees Fahrenheit." — 35–38 °F is the interior setting, not the room |
| 12 | DERIVED-1 | $150 ÷ 12 years = $12.50 a year | VERIFIED (arithmetic) | rows 2 + 3 | 150 / 12 = 12.5 |
| 13 | DERIVED-2 | $12.50 at 17.30¢ buys 72.3 kWh | VERIFIED (arithmetic) | rows 2, 5 | 12.5 / 0.173 = 72.25 |
| 14 | DERIVED-3 | $95 at 17.30¢ is 549 kWh | VERIFIED (arithmetic) | rows 3, 5 | 95 / 0.173 = 549.1 |
| 15 | DERIVED-4 | A certified unit 20 percent leaner draws 457 kWh, so the gap is about 92 kWh and $15.83 a year | VERIFIED (arithmetic) | rows 3, 4, 5 | 549.1 / 1.2 = 457.6; 549.1 − 457.6 = 91.5; 91.5 × 0.173 = 15.83 |
| 16 | DERIVED-5 | $95 is 3.88 technician-hours and $150 is 6.12 | VERIFIED (arithmetic) | rows 3, 2, 7 | 95 / 24.51 = 3.88; 150 / 24.51 = 6.12 |
| 17 | DERIVED-6 | A 24.5 ft³ adjusted-volume top-mount unit is capped at 431 kWh, or $74.63 | VERIFIED (arithmetic) | rows 8, 5 | 8.07 × 24.5 + 233.7 = 431.4; 431.4 × 0.173 = 74.63 |
| 18 | DERIVED-7 | Every 100 kWh a year saved is worth $17.30; every $100 of price needs 5.8 years | VERIFIED (arithmetic) | rows 5 | 100 × 0.173 = 17.3; 100 / 17.3 = 5.78 |
| 19 | DERIVED-8 | The same 72 kWh is worth $25.81 in Hawaii and $5.93 in North Dakota | VERIFIED (arithmetic) | rows 6, 13 | 72.25 × 0.3572 = 25.81; 72.25 × 0.082 = 5.92 |
| 20 | DERIVED-9 | 3.88 hours is 55 percent of a $150 lifetime saving measured in labour | VERIFIED (arithmetic) | rows 12, 16 | (0.78 × 24.51 = $19.1) — used only as the sentence "one $95 call is 3.9 technician-hours, and twelve years of the annuity is 6.1" |

## Rulings for the drafter (all from this run)

**FLAG-1 — the $95 line's basis is unstated, and the article must not read it as the saving.** Read as a total running cost it is coherent with the page's other numbers ($95 ≈ 549 kWh; a unit 20 percent leaner ≈ 457 kWh; the $150 lifetime line ≈ $12.50 a year). Read as a premium over a new unit it would require a 2,745 kWh refrigerator, which no household unit draws. Use the total-cost reading, put the 20 percent gap beside it, and never write "$95 a year saving".

**FLAG-2 — the $150 is certified-vs-federal-minimum, not old-vs-new.** Row 1 fixes the 9 percent comparison; the $150 line is that comparison monetised. A 15-year-old machine is two standard revisions behind, so its gap is the 20 percent in row 4, not the 9 percent in row 1.

**FLAG-3 — no repair price exists in any primary source; do not invent one.** The article prices the *annuity* against the technician's wage hour, and leaves the reader's own quote as the variable. Any sentence containing a dollar repair cost (`$250`, `$400`) is unsourced and barred.

**FLAG-4 — no purchase price exists in any primary source.** Express payback per $100 of price (row 18), never a sticker price for a machine.

**FLAG-5 — the annuity is worth four times more in Hawaii than North Dakota** (row 19). The article's worked figures use the national residential average (17.30¢) and say so.

**Numbers section (2–4 bullets only):** $12.50 a year (§ row 12), 72 kWh (§ row 13), $24.51 an hour (§ row 7), 3.9 technician-hours (§ row 16). The $150 and $95 rows belong in the lead and the tension, not in the bullets.

**Unusable rows:** none REMOVED. Row 11 is an aside, never a section.
