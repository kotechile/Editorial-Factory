# Signals: control_tower_exception_orchestration — 2026-10-13
**Window:** 2026-09-13 → 2026-10-13
**Queries run:** 24

Sweep anchor: the measured reliability of the ocean leg and of the port-to-rail handoff, both
reported inside the window. Sources run: Sea-Intelligence GLP / Sunday Spotlight press room, PMSA
data via FreightWaves and Hellenic Shipping News, Kuehne+Nagel myKN port operational updates,
Drewry Cancelled Sailings Tracker, C.H. Robinson ocean freight market update, Alabama Port
Authority / USCG Sector Mobile (Port Condition Zulu), Gartner newsroom. Date-agnostic fallback
phrasing was used on every angle (the backend silently drops `after:`/`since:` filters); every row
below carries a dated figure inside the 30-day window and was timestamp-checked against it.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Sea-Intelligence GLP issue 181: global schedule reliability continues to plummet in August | https://www.sea-intelligence.com/press-room/410-global-schedule-reliability-continues-to-plummet-in-august | 2026-09-28 | Global container schedule reliability fell -5.9 percentage points month-on-month in August 2026 to 49.9%, "the lowest point since September 2022"; average delay for late vessel arrivals rose 0.60 days M/M to 6.81 days, the highest since March 2022 and 1.92 days higher year on year; "No carrier recorded a M/M improvement in reliability in August 2026"; Maersk was most reliable at 67.3%, Wan Hai least at 23.2%; PIL recorded the largest M/M decline at -10.1 pp | Ocean-leg schedule reliability collapse | 95 |
| 2 | Sea-Intelligence Sunday Spotlight 784: August 2026 reliability in Asia at 32.3% | https://www.sea-intelligence.com/press-room/411-august-2026-reliability-in-asia-at-32-3 | 2026-09-29 | Container vessel schedule reliability in Asia dropped to 32.3% in August 2026 with the average delay for late arrivals at 7.28 days; China fell to 23.9%, Shanghai to 12.2% and Ningbo to 16.9%; M/M declines ran from -5.9 pp (Vietnam) to -13.1 pp (South Korea), showing "congestion is not a localised issue but is spread region-wide" | Region-wide Asian port congestion | 92 |
| 3 | PMSA: rail-destined container dwell at LA/Long Beach reaches 2026 high | https://www.hellenicshippingnews.com/rail-destined-container-dwell-times-at-la-lb-ports-reach-2026-high-amid-resilient-demand | 2026-09-21 | Rail-destined container dwell at the ports of Los Angeles and Long Beach climbed to 6.75 days in August, up from 6.34 days in July and "the highest over the past 12 months"; truck-bound dwell eased to 2.95 days from 3.03 days; the Port of Los Angeles handled more than 2.9 million TEU across June, July and August, "the busiest three-month stretch in its history" | Intermodal handoff dwell at a 12-month high | 90 |
| 4 | FreightWaves: container delays by rail increase at busiest US ports | https://www.freightwaves.com/news/container-delays-by-rail-increase-at-busiest-u-s-ports | 2026-09-16 | Same PMSA August reading: "Average local truck dwell was 2.95 days in August, down slightly from 3.03 days in July"; "Rail-destined cargo dwell, however, rose to 6.75 days from 6.34 days in July, extending a period of elevated intermodal dwell at the Los Angeles-Long Beach gateway"; the National Retail Federation says the extended peak season is not over and a final bump could make September the busiest month of the year | Divergence of truck and rail dwell | 86 |
| 5 | Sea-Intelligence Sunday Spotlight 783: Golden Week capacity distortions | https://www.sea-intelligence.com/press-room/409-golden-week-capacity-distortions | 2026-09-21 | For the four-week Golden Week period, Asia-North Europe scheduled weekly capacity is slated at 1.50 million TEU, a 27% year-on-year increase and 60% above the pre-pandemic average, with GW and GW+1 weeks up 63% and 39% Y/Y; severe Asian port congestion has caused a "bunching" effect where delayed vessels depart alongside regular sailings, producing 12 double-sailings over two weeks; Sea-Intelligence tells shippers to treat mid-to-late October schedules as "highly volatile placeholders" | Forward capacity distortion from delayed vessels | 90 |
| 6 | Kuehne+Nagel port operational updates, 30 Sep - 6 Oct 2026 | https://mykn.kuehne-nagel.com/news/article/port-operational-updates-from-06-10-2026 | 2026-10-06 | Seven-day average vessel waiting time: Durban 7.0 days with carriers omitting the port, Tema 5.8 days, Abidjan 4.5 days, Shanghai 3.51 days, Ningbo 2.37 days, Cotonou 2.17 days, Manila 1.61 days; Manila yard utilisation stays high and the port faces work stoppages by truckers and customs brokers over the container backlog; Storm Rachel and low Rhine water levels add to the disruption | Operator-reported vessel waiting times | 82 |
| 7 | Manila container backlog triggers protests as booking suspension extends | https://mykn.kuehne-nagel.com/news/article/manila-container-backlog-triggers-protests-as | 2026-10-05 | A voluntary work stoppage and trucking holiday that started on 5 October left "thousands of empty boxes" across terminals, truck yards and flatbeds while only around 10% of cargo volumes were moving out of the city's ports; the Bureau of Customs commissioner suggested containers waiting more than 10 days be moved offsite; Hapag-Lloyd suspended bookings to Manila, Batangas and Subic Bay across all origins and trade lanes through 31 December unless conditions change | Carrier booking suspension as the exception response | 80 |
| 8 | Port of Mobile closes ahead of Hurricane Isaias under Port Condition Zulu | https://www.waterwaysjournal.net/2026/10/09/isaias-nears-major-hurricane-strength-as-sector-mobile-ports-close | 2026-10-09 | US Coast Guard Sector Mobile set Port Condition Zulu at 2 a.m. on 9 October for Mobile, Pascagoula, Gulfport, Pensacola and Panama City, suspending vessel and cargo operations at Alabama Port Authority public berths while Isaias carried 110 mph winds; the Tennessee-Tombigbee locks at Thad Cochran and Glover Wilkins were already closed for maintenance until 12 and 13 October and Holt Lock until 31 October | Discrete weather exception | 78 |
| 9 | Port of Mobile reopens after Hurricane Isaias | https://www.fox10tv.com/2026/10/11/port-mobile-reopens-after-hurricane-isaias | 2026-10-11 | Terminal gates, vessel and cargo operations at the Port of Mobile resumed by Saturday 11 October, roughly two days after the port shut to vessel traffic early on Friday 9 October | Recovery time of a closed port | 70 |
| 10 | Drewry Cancelled Sailings Tracker, 02 October 2026 | https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/cancelled-sailings-tracker | 2026-10-02 | 39 blank sailings are expected across the major East-West trades from week 41 (5-11 October) to week 45 (2-8 November) out of 710 planned sailings, a 5% cancellation rate; blank sailings are concentrated on the transpacific eastbound trade (49%), followed by Asia-North Europe/Med (33%) and the transatlantic (18%) | Carrier capacity withdrawal after Golden Week | 80 |
| 11 | C.H. Robinson ocean freight market update, October 2026 | https://www.chrobinson.com/en-au/resources/insights-and-advisories/north-america-freight-insights/oct-2026-freight-market-update/ocean | 2026-10-01 | "Ocean capacity remains available, but reliability is uneven": port congestion and the steps carriers are taking to get schedules back on track change where and when capacity is actually available, a different planning problem than a conventional capacity shortage | Capacity availability diverging from reliability | 72 |
| 12 | Gartner: CHROs' top priorities for 2027 | https://www.gartner.com/en/newsroom/press-releases/2026-10-6-gartner-says-chros-top-priorities-for-2027-focus-on-meeting-ceos-expectations-while-minimizing-organizational-risk | 2026-10-06 | Only 24% of leadership teams are aligned on accountability for AI agents, per a July 2026 Gartner survey of 297 CHROs; neglected accountability creates organizational risk as AI agents escalate ambiguity and judgment work to humans | Accountability gap for autonomous decisions | 70 |

## Primary-source notes
- The PMSA August dwell figures (rows 3 and 4) are the same underlying trade-group release read
  through two outlets; the rail figure 6.75 days against 6.34 days in July is quoted identically in
  both. Row 3 is the dated wire copy (2026-09-21), row 4 the FreightWaves original (2026-09-16).
- Corroborating sources I may cite, with their full URLs recorded here so no downstream artifact
  cites a URL absent from this file:
  - Supply Chain Dive, "Port of Mobile shutters operations ahead of Hurricane Isaias",
    2026-10-09 — https://www.supplychaindive.com/news/port-of-mobile-shutters-operations-ahead-hurricane-isaias/832621
  - IndexBox, "Rail Container Dwell at LA/Long Beach Hits 2026 High of 6.75 Days",
    2026-09-21 — https://www.indexbox.io/blog/rail-container-dwell-at-lalong-beach-hits-2026-high-of-675-days
  - The Loadstar, "Capacity conundrum for shippers as carriers unveil post-Golden Week blanks",
    2026-10 — https://theloadstar.com/capacity-conundrum-for-shippers-as-carriers-unveil-post-golden-week-blanks
- Vendor context recorded but NOT used as an anchor leg (undated product page, no primary figure the
  verifier can date): project44 "57 agents and counting" AI Agent Orchestration —
  https://www.project44.com/ai-agent-orchestration
- Dated background, outside the window, not usable as an anchor: Verisk CargoNet Q2 2026
  (677 incidents, losses $304.6 million) and the IC3 public service announcement on cyber-enabled
  strategic cargo theft (2026-04-30) — the previous run for this vertical already carried the
  cargo-theft thread, so it is treated as a retread risk, not a signal.

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=12 candidates=0 heuristic=- window=2026-09-13..2026-10-13 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

