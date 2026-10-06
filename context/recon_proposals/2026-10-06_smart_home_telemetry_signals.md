# Signals: smart_home_telemetry — 2026-10-06
**Window:** 2026-09-06 → 2026-10-06
**Vertical:** Local-First Smart Infrastructure & Telemetry
**Queries run:** home_lifestyle_intel MCP (`--recent 30`, Smart Tech & IoT + Residential Energy & Clean Tech categories) plus a web sweep on the vertical's angles (local-first hub hardware / SBC pricing, Home Assistant platform moves, cloud-API subscription changes, panel-level energy telemetry).

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Raspberry Pi raises 2GB board prices by $12.50, effective Oct 1 2026 | https://www.raspberrypi.com/news/price-increases-for-2gb-raspberry-pi-4-and-raspberry-pi-5/ | 2026-10-01 | 2GB Pi 4 rises to $67.50 and 2GB Pi 5 to $77.50; "the cost of memory has risen very steeply over the past two years and continues to increase"; holding the 2GB price "has now become unsustainable" | Local-first hardware cost inflation | 88 |
| 2 | Raspberry Pi's third price hike of 2026 as memory costs climb | https://www.tomshardware.com/raspberry-pi/component-shortages-drive-raspberry-pi-prices-up-by-up-to-23-percent-escalating-lpddr4-lpddr5-costs-trigger-the-third-price-hike-of-the-year | 2026-10-01 | Pi 5 16GB now $220 vs its $120 launch MSRP (up to 83% on high-memory models); "the ongoing shortage of LPDDR4 and LPDDR5 memory is not improving" | Local-first hardware cost inflation | 85 |
| 3 | Micron says the memory shortage runs through 2028 | https://arstechnica.com/information-technology/2026/10/memory-supplies-are-only-getting-tighter-micron-ceo-says/ | 2026-10-01 | Micron CEO Sanjay Mehrotra: "supply-demand environment is only getting tighter"; demand to exceed supply "at least the next couple of years"; 75% of 2027 output already accounted for | AI memory demand crowding out consumer hardware | 86 |
| 4 | HBM set to take ~30% of DRAM wafer capacity in 2027 | https://arstechnica.com/information-technology/2026/10/memory-supplies-are-only-getting-tighter-micron-ceo-says/ | 2026-10-01 | Samsung's Kim Taewoo: HBM will be almost 30% of DRAM makers' wafer capacity in 2027, up from 20% this year — squeezing the consumer DRAM that SBCs and mini PCs use (Reuters, 2026-09-29) | AI memory demand crowding out consumer hardware | 78 |
| 5 | Home Assistant Cloud renamed to "Link" as the platform disowns the word cloud | https://www.home-assistant.io/blog/2026/10/02/big-tech-ruined-the-cloud-so-were-renaming-ours/ | 2026-10-02 | Nabu Casa renames Home Assistant Cloud → Home Assistant Link; "Big Tech has given the cloud a bad name"; cites "ever-increasing subscription prices to outages and data harvesting"; rename official in the 2026.12 release | Cloud subscription creep | 88 |
| 6 | SmartThings API goes paid, $4.99/month, this month | https://blog.smartthings.com/smartthings-updates/a-new-enhanced-smartthings-api-experience/ | 2026-06-23 | Free SmartThings API access is phased out from October 2026; a $4.99/month personal plan applies to non-commercial individual developers, and Home Assistant's SmartThings integration is affected (announced 2026-06-23; effective this window) | Cloud subscription creep / API paywall | 72 |

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=6 candidates=0 heuristic=- window=2026-09-06..2026-10-06 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

