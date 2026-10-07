# Evergreen Brief: smart_home_telemetry — 2026-10-06

**Archetype:** evergreen
**Vertical:** smart_home_telemetry
**Persona:** pro_homeowner
**Decision the reader is facing:** Whether to buy a residential water-leak monitor / automatic shutoff this year, and what flow rate to set its alarm to — the decision bites the moment a pinhole supply-line or slab leak runs silently at under a tenth of a gallon a minute, because the repair-versus-deductible arithmetic, not the device feature list, is what settles it.
**Durability:** The physics do not expire: a leak is a continuous flow rate and a monitor classifies that flow against a baseline. Figures are as of 2026-10-06 — EPA WaterSense's household leak volumes (retrieved 2026-10-06; the agency re-issues them, the order of magnitude holds), Triple-I/ISO homeowners loss data for accident year 2023 (published 2025), and USGS domestic water-use context (2015 estimates, the most recent national compilation). Re-check the EPA page and the ISO loss table annually; the decision rule this article carries — size the alarm to your night-flow baseline and your deductible, not to the vendor's alert presets — is true for years, not weeks.
**De-dup:** Nearest prior artifacts for this vertical in the last 180 days: the news brief 2026-10-06_smart_home_telemetry_verified_brief.md and its published output local-first-smart-home-cost-squeeze (2026-10-06, a cost-of-ownership thesis: AI memory pricing repricing local-first hardware), plus 2026-10-03 cloud-update-bricked-the-fridge-local-first (a reliability thesis: a vendor cloud update bricked an appliance). Neither is about water telemetry, leak rates, or insurance math; none of this piece's anchors (EPA leak volumes, Triple-I loss share, USGS public-supply share) appears in either.
**Thesis:** A residential water-leak monitor is not a leak detector — it is a flow-rate classifier scored against a baseline the owner has to establish, so the buy decision is settled by the night-flow threshold and the insurance deductible, not by the device's alert list.

**Lead:** `founder-voice.md` §3 `smart_home_telemetry` bullet 2 — *Industrial Telemetry for Residential Real Estate* ("Inline ultrasonic water meters … isolate micro-leaks before pipe bursts occur") — restated as a buy/set decision at the vertical's own `primary_angles` line *"ultrasonic inline flow meters and early leak telemetry"* (`context/verticals.json`), grounded in the field note in `customer-truth.md` §smart_home_telemetry anecdote 2 (a monitor flagged 0.08 gpm at 3:15 a.m. and a pinhole slab leak was caught before it surfaced, ~$34,000 of tear-out avoided). Demand corroboration only: persona `pro_homeowner` wants "payback math, gotchas, code/incentive reality", and `gsc_analyzer.py --vertical smart_home_telemetry` returned 0 striking-distance queries (impressions too thin on a young site to be a signal, and per the skill that never vetoes a lead).

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | US EPA WaterSense — Statistics and Facts | https://www.epa.gov/watersense/statistics-and-facts | 2026-10-06 | 9,400 gallons — the water an average family wastes every year on household leaks, 180 gallons a week, against more than $1,000 a year in water costs | measured |
| 2 | US EPA WaterSense — Fix a Leak Week | https://www.epa.gov/watersense/fix-leak-week | 2026-10-06 | nine percent — the share of US homes whose leaks waste 50 gallons or more a day; the page's own manual red flag is a family of four exceeding 12,000 gallons a month | measured |
| 3 | Insurance Information Institute (Triple-I) — Facts + Statistics: Homeowners and renters insurance (ISO/Verisk loss data) | https://www.iii.org/fact-statistic/facts-statistics-homeowners-and-renters-insurance | 2026-10-06 | 22.6 percent — water damage and freezing's share of US homeowners property-damage losses in 2023 (2023 average severity $20,062 per claim) | measured |
| 4 | US Geological Survey — Domestic Water Use (Water Science School) | https://www.usgs.gov/special-topics/water-science-school/science/domestic-water-use | 2026-10-06 | 87 percent — the share of Americans whose water arrives through a public-supply system rather than a self-supplied well, which is the premise that a metered, readable flow signal exists at all | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| What an inline water monitor actually catches, and the rate threshold that pays for it | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| The 200A service ceiling: dynamic load shedding vs a $10k+ utility upgrade | 9 | 9 | 5 | 8 | 7.9 | dropped — the load-calculation anchors (NEC 220.82/625.42) are paywalled or PDF-only, so fewer than three fetchable HTML primaries exist and the gate cannot stand on them |
| Panel-level CT clamps for compressor and motor health | 8 | 8 | 6 | 7 | 7.4 | dropped — every concrete detection figure on offer is a vendor claim; no measured anchor for "weeks before failure" |
| Isolated IoT VLANs and zero-cloud camera privacy | 8 | 8 | 6 | 6 | 7.2 | dropped — the load-bearing claim is reliability-of-cloud, the same thesis the 2026-10-03 published piece already ran |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=3 decision="sha1:c1abed1378" dedup="matched a prior artifact: 2026-10-06_smart_home_telemetry_ve" window_days=180 checked_at=2026-10-06T19:05:20+00:00 -->
<!-- evergreen-gate:end -->
