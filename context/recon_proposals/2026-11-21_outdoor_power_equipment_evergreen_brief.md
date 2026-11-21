# Evergreen Brief: outdoor_power_equipment — 2026-11-21
**Archetype:** evergreen
**Vertical:** outdoor_power_equipment
**Persona:** homeowner_pro
**Decision the reader is facing:** Whether the gas mower's annual maintenance schedule is worth keeping when a cordless walk-behind can finish the same lawn on one charge — the decision bites every spring, when the gas machine that was stored wrong refuses to start and the oil/plug/filter bill lands at once.
**Durability:** The maintenance-tax arithmetic is set by the engine maker's own service schedule, not by a model year: the oil change is due after the first 5 hours and then every 50 hours of use or annually, whichever comes first, as of the Briggs & Stratton page updated 2026-01-21; stale-fuel limits are physical (fuel in a stored mower must be treated or drained between 30 and 90 days of inactivity, as of the 2026-11-21 retrieval of a Honda dealer's storage guide); cordless run time is a measured class average (45–50 minutes per charge, as of Consumer Reports' current gas-vs-electric guide). All three bounds re-read identically in 12 months.
**De-dup:** `2026-11-07_your-mowers-145-minute-charge-trap` is this vertical's nearest prior evergreen artifact; it argues the *charge/refill clock* (pack rotation misses on a 145-minute charger). This brief argues the *annual maintenance and stale-fuel tax* on the gas side — service intervals, fuel decay windows and storage rules — a different mechanism with different sources. Cross-corpus check: grep of `published/` for maintenance/stale-fuel/ethanol finds no outdoor_power_equipment artifact carrying this mechanism (the 2026-10-25 spare-pack review is battery pricing; the 2026-10-31 evergreen is cold capacity). Dropped as cross-overlapping: the battery-platform five-tool cost candidate re-argues the kit-vs-spare mechanism of `2026-10-25_your-550-battery-spare-is-wrong` (casebook note 2026-10-31), and the buy-window topic is today's news-track artifact `2026-11-21_your-899-blowers-9-day-window` — value expires with the 11/30 offer.
**Thesis:** A cordless walk-behind that finishes the lawn inside its 45–50-minute charge run pays zero annual service bill, while the gas mower it replaces carries a written maintenance schedule — oil after the first 5 hours, then every 50 hours or yearly — plus fuel that decays inside a 30-to-90-day storage window, so for most suburban lawns the "tax" for keeping the gas machine is the entire point of the upgrade.

**Lead:** The vertical's own `primary_angles` entry "cordless versus gas: measured torque and runtime against the carburetor and stale-fuel maintenance tax" (context/verticals.json), targeting the `homeowner_pro` want "payback math, gotchas". Anchors located via the casebook's per-beat probe lists (2026-11-07 entry for the Consumer Reports page; new probes below for Briggs and the fuel-storage guide).

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Briggs & Stratton, How to Change Small Engine Oil (updated 2026-01-21) | https://www.briggsandstratton.com/en-us/support/maintenance-how-to/how-to-change-oil | 2026-11-21 | 50 hours of use or annually, whichever comes first — the standing oil-change interval, after an initial change at 5 hours | vendor claim |
| 2 | Nichols Equipment (Honda OPE dealer), Storing Your Lawn Mower for More Than 30 Days | https://www.nicholsequipment.com/storing-your-lawn-mower-for-more-than-30-days | 2026-11-21 | 90 days is the hard limit — gasoline must not remain in the stored mower past 90 days of inactivity; 30–90 days requires stabilizer and treated fuel | vendor claim |
| 3 | Consumer Reports, Gas vs. Electric Lawn Mower | https://www.consumerreports.org/home-garden/lawn-mowers/gas-vs-electric-lawn-mower-which-is-better-a1057954260 | 2026-11-21 | 45 to 50 minutes per charge — the average battery walk-behind mower's measured run time, enough for a quarter acre | measured |
| 4 | US EIA, How much carbon dioxide is produced per kWh of electricity? | https://www.eia.gov/tools/faqs/faq.php?id=74&t=11 | 2026-11-21 | 0.81 pounds of CO2 per kWh — the U.S. average grid intensity used to price a season of cordless charging | measured |
| 5 | EGO Power+, Battery Info (pack table) | https://www.egopowerplus.com/battery-info | 2026-11-21 | 420 Wh — the energy of the 7.5 Ah pack, the per-charge budget a mower's 45–50-minute run draws down | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Cordless vs gas: the gas mower's 50-hour/annual service schedule and 30–90-day fuel-decay rule against a 45–50-minute charge run | 9 | 9 | 8 | 8 | 8.6 | **winner** |
| The battery-platform trap: true five-tool cost across EGO, Greenworks, DeWalt FlexVolt and Ryobi | 8 | 8 | 6 | 8 | 7.4 | dropped — re-argues the kit-vs-spare mechanism of 2026-10-25 spare-pack artifact |
| Electric zero-turn: acre-per-charge and the pack replacement cliff | 7 | 8 | 6 | 7 | 7.1 | dropped — pack-price anchors are client-rendered on vendor collection pages (casebook 10-24) |
| Buy-window timing: end-of-season markdown vs paying peak | 8 | 4 | 8 | 8 | 7.1 | dropped — expires with the 11/30 offer; already today's news artifact |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=5 hosts=5 decision="sha1:0a79cc3885" dedup="matched a prior artifact: 2026-11-07_your-mowers-145-minute-" window_days=180 checked_at=2026-11-21T19:03:04+00:00 -->
<!-- evergreen-gate:end -->
