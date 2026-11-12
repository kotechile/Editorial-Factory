# Signals: demand_sensing_advanced_sop — 2026-11-12
**Window:** 2026-10-13 → 2026-11-12
**Queries run:** 15 (1 `supply_chain_intel` MCP pull `--recent 30`; 13 date-agnostic web fan-outs across the vertical's configured sources on its four `primary_angles` — demand-sensing ROI, forecast-accuracy amortisation, promo/seasonality shock, ERP-native versus specialised S&OP; plus 7 primary-page reads with an explicit date check, and 2 publisher date probes)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Gartner: access to energy is becoming a major constraint on supply chain growth | https://www.gartner.com/en/newsroom/press-releases/2026-11-05-gartner-says-access-to-energy-is-becoming-a-major-constraint-on-supply-chain-growth | 2026-11-05 | "Gartner predicts that by 2029, most manufacturers without advanced energy management capabilities will experience 20% to 30% higher costs due to price and supply volatility, network congestion, and capacity constraints"; energy constraints "are increasingly shaping network design decisions, capacity planning and facility expansion strategies"; interconnection delays "can delay facility openings, capacity expansions, and other planned investments"; analyst Marta Muñoz: "Many supply chains continue to operate under the assumption that energy is an always-available input" | The constraint that decides whether a plan can execute has become a local power connection | 86 |
| 2 | Manhattan Associates Q3 2026 results: cloud subscriptions overtake services for the first time | https://www.manh.com/about-us/newsroom/press-releases/earnings-2026-q3 | 2026-10-27 | Cloud subscription revenue $134.438M (+28.2% from $104.852M) against services revenue $134.417M (+1.1% from $133.007M) — a $21,000 margin on total revenue of $306.187M (+11.0%); RPO $2.590B, up 24.7% year on year; CEO Eric Clark: "Cloud revenue surpassed services revenue and total quarterly revenue exceeded $300 million" | The software business has crossed from paid implementation work to paid access | 84 |

## Dated background

Carried for the drafter's context and for `synthesize_topics.py --check-briefs`; none of these is an anchor, and none is inside the 30-day window.

- Manhattan Associates, Form 10-K for the year ended 2025-12-31 (filed 2026), "Our services revenue consists of fees generated from implementation, training and application managed services … Implementation services include system planning, design, configuration, testing, and other software implementation support, and are typically optional and distinct from our software" (https://www.sec.gov/Archives/edgar/data/1056696/000119312526037138/manh-20251231.htm). Same filing: services revenue $503.0M in 2025, 47% of total revenue, against $525.5M in 2024 — a $22.5M decline "primarily driven by customer budgetary constraints that shifted services work to future periods"; approximately 75% of professional services revenue relates to cloud subscriptions.
- Manhattan Associates Q3 2026 earnings release, full PDF (https://www.manh.com/siteassets/generic-container-block/about-us/manh-earnings-release---q3-2026.pdf). The source of record for the quarter's line items; the newsroom page above summarises it.
- Gartner, 2026-10-28 — "Gartner Survey Shows 47% of Supply Chains Reduced Headcount by an Average of 10.5% Over the Past Two Years Primarily Due to the Impact of AI" (https://www.gartner.com/en/newsroom/press-releases/2026-10-28-gartner-survey-shows-47-percent-of-supply-chains-reduced-headcount-by-an-average-of-10-5-percent-over-the-past-two-years-primarily-due-to-the-impact-of-ai). This vertical's 2026-11-05 article anchored it; carried here only so the de-dup is explicit, never re-argued.
- Gartner, 2026-09-24 — "Gartner Predicts Only 5% of Organizations Will Make at Least 10% of Supply Chain Planning Decisions Autonomously by 2030" (https://www.gartner.com/en/newsroom/press-releases/2026-09-24-gartner-predicts-only-5-percent-of-organizations-will-make-at-least-10-percent-of-supply-chain-planning-decisions-autonomously-by-2030). Out of window; caps how much autonomy any planning subscription can be paying for.
- Gartner Supply Chain Planning Summit, Denver, 2026-11-02/03, Gartner's own sessions page (https://www.gartner.com/en/conferences/na/supply-chain-planning-us/sessions). The venue at which the 5 November constraint research landed; agenda only, no figures.
- Deconvolute Labs, 2026-10-22 — "Do Forecast Overrides Pay Off? What 147,000 Forecasts and a Marble Funnel Say" (https://deconvolutelabs.com/blog/supply-chain/forecast-overrides). In window as a write-up, but every load-bearing figure belongs to Fildes/Goodwin (2007, 2009) and Fildes/Goodwin/De Baets (2025), so it is a secondary synthesis and not admissible as an anchor; dropped at Stage 3.
- Lawrence Berkeley National Laboratory, "Queued Up: 2026 Edition" (published 2026-06, data through end-2025; https://emp.lbl.gov/queues). Out of window; records the interconnection clock the article may reference qualitatively, never as a dated anchor.
- `supply_chain_intel_client.py --recent 30 --vertical demand_sensing_advanced_sop --format signals`, 2026-11-12: 10 items dated 2026-11-09/11, all Supply Chain Dive/Supply Chain Now newsroom (BMW battery plants, air cargo +6% YoY in October, Honda's $3B Ohio plant, Asics warehouse drones, CarParts.com last-mile, transpacific spot $8,245/FEU, Bed Bath & Beyond DC closure, Kuehne+Nagel cold-chain agents, US–China truce extended to 2027-01-10). None bears on planning method, forecast accuracy or the S&OP budget line; the truce already anchored `supply_chain` on this front today. Recorded as swept and dropped, not softened.

## Dating note

Row 1 is dated by Gartner's own publication date (2026-11-05), six days before the run. Row 2 is dated by Manhattan's release (2026-10-27), sixteen days before the run, and its comparative figures are for the quarter ended 2026-09-30. The 10-K's 2025 figures are background: they establish the definition of services revenue and the prior-year direction of that line, and the article must date them to fiscal 2025 rather than present them as current. No row is outside the window.

## Candidate Synthesis Pairs



<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=2 candidates=0 heuristic=- window=2026-10-13..2026-11-12 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

