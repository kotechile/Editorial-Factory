# Evergreen Brief: consumer_asset_repair_replace_tco — 2026-10-23
**Archetype:** evergreen
**Vertical:** consumer_asset_repair_replace_tco
**Persona:** systems_tinkerer_pro
**Decision the reader is facing:** A 12-to-15-year-old refrigerator still runs but the repair quotes are climbing and the power bill is up. Put another $200–$400 into it, or replace it and bank the efficiency the label promises? The decision bites at the next service call and again at every utility bill until the machine dies.
**Durability:** The rule is arithmetic on dated inputs, so it survives price moves: the federal efficiency ceilings in § 430.32 as of the eCFR edition current on 2026-10-23 (the 2014-era standards, with the next step at the 2029/2030 compliance dates by product class), the EIA 2025 annual average residential rate of 17.30¢ per kWh as of that 2025 edition, O*NET's 2025 median wage for appliance repairers, and ENERGY STAR's own two savings lines as published on 2026-10-23. A reader can re-run the same division with next year's rate and get a correct answer; the annuity stays small because the label's advantage over the legal floor is single-digit percent, not because of any one year's prices.
**De-dup:** `2026-10-23_your-cheap-part-a-599-bill` is this vertical's nearest prior artifact — today's news run, on a manufacturer's fixed service ladder for a wearable and on Right to Repair access, with no appliance, no energy figure and no labour hour in it. This piece moves to the kitchen: the annuity an appliance label actually pays, priced against the repairer's median wage hour. Checked across the desk: `published/2026-10-03_cloud-update-bricked-the-fridge-local-first.md` uses a refrigerator only as an example of cloud dependency, and no artifact in `published/` argues an efficiency payback.
**Thesis:** The efficiency a new refrigerator buys is a small fixed annuity — ENERGY STAR's own lifetime line works out to $12.50 a year, and even a 15-year-old unit only supports about $16 a year — so it can discount a replacement that the failure already justified, but it can never be the reason to buy one; the decision belongs to the repair quote, converted into technician-hours at the $24.51 median wage.

**Lead:** The vertical's own primary angle #2 ("appliance and espresso-machine cost per use against purchase price") plus the founder pillar "The True Unit Economics" (`context/growth_os/founder-voice.md` §3 `personal_microeconomics_tinkering_tax`) — build the cost-per-use audit for the one appliance every household runs 24/7, from the label's own numbers rather than from a vendor pitch. GSC carries 0 query opportunities for this vertical today (young site, thin impressions), recorded as bonus signal only and no veto.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | ENERGY STAR (U.S. EPA/DOE program) — Refrigerators | https://www.energystar.gov/products/refrigerators | 2026-10-23 | $150 over the 12-year lifetime of the product — the certified-vs-federal-minimum saving, i.e. $12.50 a year | program estimate |
| 2 | ENERGY STAR — Refrigerators (old-unit running cost line) | https://www.energystar.gov/products/refrigerators | 2026-10-23 | $95 per year to run — the figure the page attaches to a refrigerator over 15 years old | program estimate |
| 3 | U.S. Energy Information Administration — Prices and factors affecting prices | https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php | 2026-10-23 | 17.30¢ per kWh — the 2025 annual average residential retail price | measured |
| 4 | O*NET OnLine — 49-9031.00 Home Appliance Repairers | https://www.onetonline.org/link/summary/49-9031.00 | 2026-10-23 | $24.51 hourly — median wage, 2025 vintage ($50,990 annual) | measured |
| 5 | eCFR — 10 CFR 430.32, energy conservation standards | https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430/subpart-C/section-430.32 | 2026-10-23 | 233.7 kWh per year — the intercept in the federal ceiling for an automatic-defrost top-mount refrigerator-freezer (8.07 × adjusted volume + 233.7) | regulation |
| 6 | ENERGY STAR — Refrigerators (label delta) | https://www.energystar.gov/products/refrigerators | 2026-10-23 | 9 percent more energy efficient — certified models against the federal minimum standard | program estimate |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The efficiency annuity vs the repair hour: what replacing a working fridge actually pays | 9 | 9 | 9 | 8 | 8.9 | **winner** |
| Espresso machine cost per shot: purchase price, descale cycles, gasket and pump replacement | 7 | 8 | 5 | 7 | 6.6 | dropped — the only anchors are vendor manuals, which fetch as PDFs the verifier cannot read; no measured consumption data |
| Extended warranty math vs self-insuring the failure, deductible and exclusion traps | 8 | 8 | 4 | 7 | 6.7 | dropped — no primary source publishes claim frequency or payout ratios; every anchor would be a plan seller's own marketing |
| Battery or device: replacement economics against trade-in credit and refurbished substitution | 8 | 7 | 7 | 7 | 7.3 | dropped — trade-in values render client-side, and the ground overlaps today's service-ladder piece |

**Arithmetic the brief fixes for the drafter (all derived from the rows above, recompute, never round-trip through the draft):** $150 ÷ 12 years = **$12.50 a year**, which at 17.30¢ is **72 kWh a year**. $95 ÷ 17.30¢ = **549 kWh a year**, and 549 ÷ 1.2 = 457 kWh for a unit using 20 percent less, a **91.5 kWh / $15.83 a year** gap. $95 ÷ $24.51 = **3.88 technician-hours**; $150 ÷ $24.51 = **6.12 technician-hours**. The federal ceiling for a top-mount automatic-defrost unit at 24.5 cubic feet adjusted volume is 8.07 × 24.5 + 233.7 = **431 kWh a year**, or **$74.63 a year** at 17.30¢. Every 100 kWh a year saved is worth **$17.30**, so every $100 of purchase price needs **5.8 years** at that delta.

**Ambiguity to carry as FLAGGED, never resolved silently:** ENERGY STAR's sentence reads "Refrigerators over 15 years old could be costing you more about $95 per year to run." Read as a *total* running cost, the page is self-consistent ($95 ≈ 549 kWh ≈ 20 percent above a 457 kWh certified unit, and the $150 lifetime line ≈ $12.50–16 a year). Read as a *premium over a new unit*, it would imply a 2,745 kWh refrigerator, which no household unit draws. The article uses the total-cost reading, states the 20 percent gap from the same page beside it, and never presents $95 as the saving.

## Gate result

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=6 fetched=6 sources=4 hosts=4 decision="sha1:91d321bfdb" dedup="matched a prior artifact: 2026-10-23_your-cheap-part-a-599-b" window_days=180 checked_at=2026-10-23T19:33:52+00:00 -->
<!-- evergreen-gate:end -->
