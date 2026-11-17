# Signals: control_tower_exception_orchestration — 2026-11-17
**Window:** 2026-10-18 → 2026-11-17
**Queries run:** 24 (12 date-agnostic web fan-outs across the vertical's four primary angles and its
configured sources — freightwaves, supply_chain_dive, gartner_supply_chain, journal_of_commerce,
logistics_management, iot_world_today — 5 primary-page fetches, 1 `supply_chain_intel` MCP pull
(`--recent 30 --vertical control_tower_exception_orchestration --format signals`: 10 items, all generic
supply-chain news — a Conagra plant closure, FedEx China–US capacity, USPS's 2027 rate increase,
Walmart's drone expansion — none an exception-orchestration signal), 1
`gsc_analyzer.py --vertical control_tower_exception_orchestration --export-md` returning **0**
striking-distance queries (thin impressions; bonus signal only, never a veto), 1 publisher date probe
(`freightwaves.com` WP `date` field on the Descartes OpsForce write-up → **2026-01-30**, dropped), and
3 verification fetches of the rows kept.)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Sea-Intelligence corrects its own alliance schedule-reliability figures, disclosing an 11-year double count | https://www.sea-intelligence.com/press-room/419-glp-correction | 2026-11-07 | A "small subset of vessel arrivals had been double counted in the calculation of aggregated alliance schedule reliability figures"; "dates back to the first alliance section in the April 2015 GLP report and went unnoticed for 11 years, both by our team and by alliance carriers receiving copies of the underlying raw data"; "does not impact any carrier or trade scores, only the aggregated alliance scores"; 461 calls affected = 2.28% of all alliance calls Feb 2025–Sep 2026; affected calls removed and the October 2026 report republished | Benchmark denominator | 92 |
| 2 | The correction flips the August/September 2026 alliance ranking | https://www.sea-intelligence.com/press-room/419-glp-correction | 2026-11-07 | Previously published: "MSC was the most reliable carrier alliance with schedule reliability of 68.9%, followed by Gemini with 68.4%, and Ocean Alliance with 44.8%". Corrected: "Gemini was the most reliable carrier alliance with schedule reliability of 70.4%, followed by MSC with 69.5%, and Ocean Alliance with 44.9%". Gemini +2.0 points, MSC +0.6, Ocean +0.1; the corrected gap (0.9 points) is on the other side of the previously published gap (0.5 points) | Ranking churn | 88 |
| 3 | The mechanism: a call that sits on two trade lanes is counted on both | https://www.sea-intelligence.com/press-room/419-glp-correction | 2026-11-07 | "aggregate East-West alliance scores were calculated as weighted averages of schedule reliability across individual trades, without correcting for a small number of vessel calls in destination regions appearing on two separate trade lanes"; worked example in the release — "on a service calling at Shanghai, Algeciras, and New York, the New York call would appear on both the Asia–North America East Coast and Transatlantic Westbound trade lanes, resulting in double counting" | Counting rule | 86 |
| 4 | Sea-Intelligence's October issue as originally published: 50.6% global reliability, 6.65-day average delay | https://www.sea-intelligence.com/press-room/415-global-schedule-reliability-records-a-marginal-gain-in-september | 2026-10-28 | issue 182 of the Global Liner Performance report, figures up to and including September 2026: reliability "improved by 0.9 percentage points M/M in September 2026 to 50.6%" after "three consecutive M/M drops, with an aggregate drop of -14.8 percentage points, from a peak of 64.5% in May"; average delay of late vessel arrivals "-0.30 days M/M to 6.65 days", "the second-highest figure for the month"; 120-page report covering "34 different trade lanes and 60+ carriers" | Benchmark level | 76 |
| 5 | A live cross-platform FedEx monitor finds 90% of carrier-affecting incidents reported by only one of four platforms | https://shipzil.com/carrier/fedex | 2026-11-15 | "Across 162 carrier-affecting incidents recorded here, 90% were reported by only one company" (four platforms: EasyPost, Shippo, ShipStation, ShipEngine — "four platforms run by three independent companies", ShipStation and ShipEngine both Auctane); of the 162, "47 (29%) had their carriers inferred from the incident title rather than a component the platform tagged" | Incident reporting | 90 |
| 6 | The uptime figure is a function of how much a platform files | https://shipzil.com/carrier/fedex | 2026-11-15 | 90-day reported uptime: EasyPost 99.97% (2 incidents, 1 measured in window), Shippo 95.68% (10 incidents, 6 measured), ShipStation 99.40% (5, 2), ShipEngine 99.24% (1, 1); total incidents recorded per platform Shippo 82, EasyPost 44, ShipEngine 25, ShipStation 11; the page states the figures are "uptime as reported by the platforms, not independently measured: there may be outages nobody reported" and that "a platform that reports less looks better here" and that averaging "improves the number every time a platform is added" | Reporting appetite | 88 |
| 7 | project44 publishes transshipment dwell against a disclosed pre-conflict baseline | https://www.project44.com/supply-chain-insights/hormuz-week-34-impact-on-ocean-freight-eases-but-diversions-and-port-dwell-remain-above-pre-conflict-levels/ | 2026-11-17 | Data window 28 September – 25 October 2026 against a baseline of "Jan 5 to Feb 23": transshipment dwell above baseline at six ports from +12% at Port Said to +59% at Hambantota (17.4 days vs 11.0) and Mundra (10.6 vs 6.7); Colombo 8.6 vs 5.8 (+49%); Singapore 7.6 vs 6.4 (+20%); Jebel Ali export dwell "averages 26.8 days across the conflict versus 8.5 days pre-conflict (+215%)"; weekly diversions averaging "about 2.4 times the pre-conflict level" over 28 Sep–25 Oct, against a 23 March peak of "about 8.4 times" | Baseline choice | 72 |

## Dated background (carried, not anchored)

- Descartes' "Descartes drives the future of visibility with agentic AI" write-up (its own design
  statement that visibility breaks when a single tracking method fails, and that its arrival agent
  "validates times, removes false exceptions") is **2026-01-30** per the publisher's WP `date` field —
  outside the window, so the design claim is not usable as an in-window signal.
  https://www.freightwaves.com/news/descartes-drives-the-future-of-visibility-with-agentic-ai
- Descartes MacroPoint OpsForce was announced **2026-03-04** — outside the window.
  https://www.descartes.com/resources/news/descartes-expands-ai-innovation-global-logistics-network-ai-agents-freight-visibility
- FourKites withdrew from Gartner's RTTVP Magic Quadrant on **2025-02-24** — outside the window.
  https://www.fourkites.ai/press/fourkites-withdraws-from-gartner-rttvp-magic-quadrant
- Samsara's Agent Studio launch (7x agent-adoption growth since June) is **2026-10-13**, five days
  before the window opened — outside. https://www.samsara.com/company/news/press-releases/agent-studio
- project44's Q3 FY27 shipper ARR release is **2026-11-03** and is inside the window, but it reports
  commercial performance (new ARR +49% YoY) rather than a measurement, so it is not an anchor here.
  https://www.project44.com/press-releases/project44-recognized-by-four-market-insight-firms-in-three-months
- The D.C. Circuit's Evergreen Shipping Agency decision upholding the FMC's detention-fee reasoning
  (174 F.4th 169) carries no publication date on the Commission's page; the FMC's demurrage and
  detention billing rule's own history is 2024–2025 material. Background only.
  https://www.fmc.gov/articles/u-s-court-of-appeals-upholds-fmc-decision-that-detention-fees-must-promote-freight-fluidity
- Tive's "State of Visibility" figure that 37% of companies lose track of shipments in transit is
  from the **2025** edition — outside the window. https://www.agistix.com/resources/blog/what-is-real-time-visibility

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=7 candidates=0 heuristic=- window=2026-10-18..2026-11-17 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

## Dating note

Rows 1–4 carry the publisher's own dates: the correction press release's own download filenames are
`20261107_…`, and issue 182's release names itself "Oct 28th, 2026". Rows 5 and 6 are a **live status
page read at 2026-11-15, 21:35 UTC** — the page's own snapshot line — and the figures quoted are that
snapshot's, not today's; the page refreshes continuously, so the article cites the snapshot rather
than "current" uptime. Row 7 is a **dataset publication observed on 2026-11-17**: project44's page
carries no visible publication date, its own data window ends 25 October, and the release is dated by
observation with the data window stated in the claim cell (the same convention used for standing
records). No row rests on a search-snippet date, and no row's anchor sits outside the window.
