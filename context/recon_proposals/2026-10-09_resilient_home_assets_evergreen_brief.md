# Evergreen Brief: resilient_home_assets — 2026-10-09
**Archetype:** evergreen
**Vertical:** resilient_home_assets
**Persona:** pro_homeowner
**Decision the reader is facing:** How many kWh of stationary battery storage to buy and which circuits to put on the backed-up subpanel so a 72-hour grid outage does not take out heat, water and refrigeration — a purchase/retrofit decision the homeowner settles this year, not a policy headline.
**Durability:** The sizing method rests on physical constants and slow-moving consumption baselines, so it stays correct for years; the figures are *as of* the 2022 EIA residential-usage baseline (10,791 kWh/year) and the July 2026 EIA residential price (18.31 ¢/kWh), which are re-published annually and only the price line needs re-indexing each cycle.
**De-dup:** 2026-10-09_your-ev-is-now-a-home-battery-behind-a-paywall published the vehicle-to-home (V2H) leg — an EV feeding the house and the prerequisite Powerwall/Wall-Connector paywall. This differs: it is the stationary LFP bank + critical-loads-subpanel sizing decision (how many kWh, which circuits, how many hours of autonomy), not the EV-as-generator unlock or its hardware cost.
**Thesis:** A home backup battery must be sized against the critical loads it has to carry for the length of the outage — not against the household's annual kWh bill — which is why the same bank that looks oversized next to a monthly utility statement is often barely adequate once you enumerate the circuits that must keep running.

**Lead:** The vertical's own beat — `primary_angles` #2 ("behind-the-meter microgrids solar and LFP storage sizing") in `context/verticals.json`, reinforced by the founder's standing position in `context/growth_os/founder-voice.md` §3 (`resilient_home_assets`: "Avoid undersized consumer battery backups; design dedicated critical-loads subpanels powered by LFP storage") and the field anecdote in `context/growth_os/customer-truth.md` (the 84-hour ice-storm outage where a 5 kWh consumer bank drained in 7 hours while a 20 kWh LFP bank on a critical-loads subpanel ran four days). The measurable anchors are the government consumption baseline, the residential price, FEMA's food-safety hold-times, and the DOE/NREL solar-sizing baseline.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | U.S. Energy Information Administration, "How much electricity does an American home use?" (FAQ) | https://www.eia.gov/tools/faqs/faq.php?id=97&t=3 | 2026-10-09 | 10,791 kWh — 2022 average annual U.S. residential electricity use (about 899 kWh/month), the whole-house number a battery is usually mis-sized against | measured |
| 2 | U.S. Energy Information Administration, Electricity Monthly Update — End-Use | https://www.eia.gov/electricity/monthly/update/end-use.php | 2026-10-09 | 18.31 cents/kWh — U.S. residential retail electricity price, July 2026, up 4.9% from July 2025 | measured |
| 3 | FEMA / Ready.gov, "Power Outages" | https://www.ready.gov/power-outages | 2026-10-09 | 48 hours — a full freezer holds its temperature that long while a refrigerator holds only about 4 hours, and food is unsafe after 2 hours above 40°F: the load envelope the battery actually has to cover | measured |
| 4 | U.S. Department of Energy / NREL, "Homeowner's Guide to Going Solar" | https://www.energy.gov/eere/solar/homeowners-guide-going-solar | 2026-10-09 | 7.15 kW — the average residential solar system size NREL assumes for its analyses (range 3–11 kW), the generation baseline often mistaken for the battery-sizing number | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Size the battery for the outage, not the bill: kWh + critical-loads subpanel for 72-hour autonomy | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| Where the loss actually is: roof-related damage is 70–90% of insured residential catastrophe losses — reorder your hardening spend | 8 | 8 | 9 | 7 | 8.1 | dropped — re-argues the 2026-09-25 insurability/hardening piece (`ca-fair-plan-rate-hike-hardening-exit`); keep as the reserve candidate |
| Ember-resistant vents and a 30-foot non-combustible zone: the wildfire retrofit checklist | 7 | 9 | 6 | 7 | 7.3 | dropped — the ember/vent primer figures (mesh gauge, % of ignitions) do not retrieve through the gate's fetcher; NFPA returns 403 and ibhs.org/wildfire carries no mesh figure |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=3 decision="sha1:6fb024bbf2" dedup="matched a prior artifact: 2026-10-09_your-ev-is-now-a-home-b" window_days=180 checked_at=2026-10-09T18:04:08+00:00 -->
<!-- evergreen-gate:end -->
