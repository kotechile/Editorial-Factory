# Evergreen Brief: outdoor_power_equipment — 2026-11-07
**Archetype:** evergreen
**Vertical:** outdoor_power_equipment
**Persona:** homeowner_pro
**Decision the reader is facing:** Whether to buy a second battery pack with a cordless walk-behind mower — and whether the charger in the box can refill it fast enough for a two-pack rotation to keep cutting, or whether the money is better left in the wallet until a wider deck or a bigger lot justifies it.
**Durability:** The load-bearing numbers are device physics, not prices: a 7.5Ah 56V pack holds 420Wh, a 550W rapid charger refills it in 60 minutes, the standard charger takes 145 minutes, and a 21-inch deck at walking speed covers a quarter acre in 27–64 minutes depending on pace. Nothing here expires except the specific model years, which are named — the spec ladder is as of the 2026 EGO POWER+ line (battery and charger pages read 2026-11-07), and the measured run-time band is as of Consumer Reports' published gas-versus-battery test of the 2025–2026 mower ratings.
**De-dup:** `2026-10-31_your-pack-delivers-half-at-18c` is this vertical's nearest prior evergreen artifact (pack capacity at -18°C); this piece never touches temperature and is about the charge clock and lot arithmetic instead. Also checked against `2026-10-24_your-1-acre-mowers-04-acre-trap` (a robot mower's rated acreage versus usable acreage), `2026-10-25_your-550-battery-spare-is-wrong` (kit configuration versus a spare pack's price) and `2026-10-24_your-heated-mat-costs-50-times-the-blower` (cost per inch cleared). A cross-vertical grep for the duty-cycle mechanic surfaced `2026-10-28_your-charger-gap-buys-16-robots` (warehouse_automation_robotics_capex) — that piece sizes a robot FLEET from loaded runtime against a shift; this one sizes ONE machine against one lot and turns on the charger's wattage, so the mechanic is shared and the decision, unit and evidence are not.
**Thesis:** A cordless walk-behind's 60-minute run is matched to a 60-minute rapid charge, so a second pack only keeps the machine cutting when it refills while the first one mows — on the standard 145-minute charger the rotation misses by an hour, and the second pack buys a wait rather than a cut.

**Lead:** The vertical's own `primary_angles` (entry 3, "cordless versus gas: measured runtime against the maintenance tax") plus the persona's want for payback math and gotchas. The specific material: Consumer Reports' measured run time for battery walk-behinds (45–50 minutes, and two-thirds able to mow a quarter acre per charge), EGO's own published ladder pairing a 60-minute run with a 60-minute rapid charge on the same 7.5Ah pack and 145 minutes on the standard charger, and Battery University's charge-time table, which is what makes the ratio a rule rather than a vendor coincidence.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Consumer Reports — Gas vs. Battery Lawn Mower: Which Is Better? | https://www.consumerreports.org/home-garden/lawn-mowers/gas-vs-electric-lawn-mower-which-is-better-a1057954260 | 2026-11-07 | 45 to 50 minutes — the average battery walk-behind mower's measured run time was 45 to 50 minutes per charge, and on flat ground it might cut half an acre | measured |
| 2 | EGO POWER+ — 21" Select Cut Self-Propelled Mower (LM2135SP) | https://egopowerplus.com/21-inch-self-propelled-mower-select-cut-lm2135sp | 2026-11-07 | 60 minutes of runtime — up to 60 minutes of runtime on a single charge with the recommended 56V 7.5Ah ARC Lithium battery on a 21-inch deck | vendor claim |
| 3 | EGO POWER+ — 21" Select Cut Self-Propelled Mower (LM2135SP) | https://egopowerplus.com/21-inch-self-propelled-mower-select-cut-lm2135sp | 2026-11-07 | .9 MPH – 3.1 MPH — variable speed self-propel, the pace the coverage arithmetic uses | vendor claim |
| 4 | EGO POWER+ — Rapid Charger (CH5500) | https://egopowerplus.com/charger-rapid | 2026-11-07 | 7.5Ah in 60 minutes — from zero the rapid charger fully charges a 7.5Ah battery in 60 minutes (and a 10.0Ah in 70 minutes) | vendor claim |
| 5 | EGO POWER+ — Learn More About EGO Batteries and How to Choose | https://egopowerplus.com/battery-info | 2026-11-07 | 145-Minute charge time w/ Standard charger — the 7.5Ah pack is 420Wh and takes 145 minutes on the standard charger against 60 minutes on the rapid one | vendor claim |
| 6 | Battery University — BU-409: Charging Lithium-ion | https://batteryuniversity.com/article/bu-409-charging-lithium-ion | 2026-11-07 | 99 percent — charge efficiency is about 99 percent at the cell, with 180 min to full saturation at 4.20 volts per cell in its own table | measured |

## Arithmetic the article performs (inputs named, no gate row needed)

- Deck 21 inches = 1.75 feet. Walking speeds 0.9 / 1.3 / 2.0 / 3.1 mph = 79 / 114 / 176 / 273 feet a minute.
- Gross coverage 1.75 × feet-per-minute; apply 15% overlap: 118 / 170 / 262 / 406 square feet a minute.
- Quarter acre = 10,890 sq ft → 92 / 64 / 42 / 27 minutes. Half acre = 21,780 sq ft → 185 / 128 / 83 / 54 minutes.
- Consumer Reports' measured 45–50 minutes therefore lands on an ordinary 1.5–2.0 mph pass over a quarter acre, which is the corroboration the piece rests on.
- Charge arithmetic: 7.5Ah × 56V = 420Wh ÷ 550W = 45.8 minutes at 100% conversion against 60 published (76%); 10Ah (560Wh) ÷ 700W = 48 minutes against 60 (80%). Thus charge minutes ≈ watt-hours ÷ charger watts ÷ 0.78.
- Duty cycle: rapid charger = 60 minutes cut, 60 minutes charge (1:1, a rotation works); standard charger = 60 minutes cut, 145 minutes charge (rotation fails by 85 minutes).

## Candidate topics considered

| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The charge clock: a second pack only pays on a 60-minute charger | 9 | 8 | 8 | 9 | 8.5 | **winner** |
| True five-tool cost across EGO, Greenworks, DeWalt FlexVolt and Ryobi | 8 | 5 | 7 | 7 | 6.8 | dropped — every load-bearing figure is a pack or kit price that expires in weeks; that is the review pipeline's job, not evergreen's |
| Electric zero-turn acres per charge and the pack-replacement cliff | 8 | 6 | 6 | 7 | 6.8 | dropped — the "rated acreage versus usable acreage" trap is already published (`2026-10-24_your-1-acre-mowers-04-acre-trap`) and the cliff itself is a price that moves |
| End-of-season markdown versus peak storm pricing | 7 | 3 | 6 | 6 | 5.5 | dropped — value expires inside 90 days; this is a news-track buy-window story, not a durable one |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=6 fetched=6 sources=5 hosts=3 decision="sha1:6e058eb1a4" dedup="matched a prior artifact: 2026-10-31_your-pack-delivers-half" window_days=180 checked_at=2026-11-07T19:05:23+00:00 -->
<!-- evergreen-gate:end -->
