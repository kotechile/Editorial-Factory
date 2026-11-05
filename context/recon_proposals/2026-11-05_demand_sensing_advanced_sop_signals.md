# Signals: demand_sensing_advanced_sop — 2026-11-05
**Window:** 2026-10-06 → 2026-11-05
**Queries run:** 14 (supply_chain_intel MCP `--recent 30` pull; 11 date-agnostic web fan-outs across the vertical's configured sources on its four `primary_angles` — demand-sensing ROI, forecast-accuracy amortization, promo/seasonality shock, ERP-native versus specialised S&OP; plus 3 primary fetches with an explicit date check)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Gartner survey: AI is thinning the entry-level supply chain workforce | https://www.gartner.com/en/newsroom/press-releases/2026-10-28-gartner-survey-shows-47-percent-of-supply-chains-reduced-headcount-by-an-average-of-10-5-percent-over-the-past-two-years-primarily-due-to-the-impact-of-ai | 2026-10-28 | "Nearly half of supply chains have reduced headcount by an average of 10.5% over the past two years, primarily due to the impact of AI"; "66% of supply chain leaders report headcount reduction is concentrated at the entry level, more than double the percentage reporting reduction at other levels"; 303 leaders surveyed 2026-05-05 to 2026-06-11, all at organizations already using AI | Labor is the half of planning-software ROI nobody books | 92 |
| 2 | Kinaxis Q3 2026 results (quarter ended 2026-09-30) | https://investors.kinaxis.com/news-releases/news-release-details/2026/Kinaxis-Inc--Reports-Third-Quarter-2026-Financial-Results/default.aspx | 2026-11-04 | SaaS revenue $112.3M, +22% year on year; total revenue $160.3M, +19%; ARR $483.9M, +19%; remaining performance obligations $1,026.9M, +21%; adjusted EBITDA margin 26%; professional services $42.2M, +14% | Subscription commitments are running longer than the planning bench that signs them | 88 |
| 3 | Demand Forecasting Accuracy Report 2026 — 15 live deployments benchmarked against the incumbent forecast | https://demandforecast.ai/resources/forecast-accuracy-report | 2026-10 (edition dated October 2026; the PDF carries a 2026-09 upload path) | Forecast error cut 14% to 56% in every benchmark, 32% on average; "Manual planning effort dropped by 70%, and in one deployment 75% of forecast volume qualified as touchless"; Mars VP of global supply chain: planners "can already 'not touch' ~75% of the volume" | The review load the software genuinely removes is the entry-level load | 70 |
| 4 | Q3 2026 U.S. Bank Freight Payment Index, discussed with its author (index published 2026-10-29) | https://supplychainnow.com/sneak-preview-q3-2026-us-bank-freight-payment-index-1656 | 2026-11-04 | "shipper spending increased by more than 30% despite marginal shipment growth, signaling a market driven by capacity constraints rather than demand"; drawn from "nearly $46 billion in freight transactions" | Cost inflation without volume growth is the pressure that funds a headcount cut | 72 |

## Dated background

Carried for the drafter's context and for `synthesize_topics.py --check-briefs`; none of these is an anchor, and none is inside the 30-day window.

- Gartner, 2026-05-05 — "Gartner Predicts Supply Chain Organizations Pausing Entry-Level Hiring for AI Will Face Higher Costs by 2030" (https://www.gartner.com/en/newsroom/press-releases/2026-05-05-gartner-predicts-supply-chain-organizations-pausing-entry-level-hiring-for-ai-will-face-higher-costs-by-2030). The same firm, five months before its October survey, predicted the cost of the exact cut its respondents then reported making.
- Gartner, 2026-09-24 — "Gartner Predicts Only 5% of Organizations Will Make at Least 10% of Supply Chain Planning Decisions Autonomously by 2030" (https://www.gartner.com/en/newsroom/press-releases/2026-09-24-gartner-predicts-only-5-percent-of-organizations-will-make-at-least-10-percent-of-supply-chain-planning-decisions-autonomously-by-2030). Out of window; it caps how much autonomy a 2.1-year contract can be paying for.
- Gartner, 2026-08-05 — "Gartner Survey Finds Majority of Chief Supply Chain Officers Unclear on AI Investment Returns" (https://www.gartner.com/en/newsroom/press-releases/2026-08-05-gartner-survey-finds-majority-of-chief-supply-chain-officers-unclear-on-ai-investment-returns). Out of window.
- Blue Yonder, 2026 — takeaways from the Gartner Supply Chain Planning Summit (https://blueyonder.com/blog/2026/key-takeaways-from-the-gartner-supply-chain-planning-summit). Vendor blog; names the mechanism the argument needs — planners must "test recommendations, validate the underlying information, and recognize when an issue needs closer review" — and describes Morrisons' forecast-health agent. Corroboration only, never the source of record.
- Kinaxis Inc., 2026-11-04 — Business Wire mirror of the Q3 release (https://www.businesswire.com/news/home/20261104644172/en/Kinaxis-Inc.-Reports-Third-Quarter-2026-Financial-Results). Listed so the citation set is complete; the investor-relations copy is the source of record.
- Supply Chain Dive newsroom feed, 2026-11-03/04 (via `supply_chain_intel_client.py --recent 30`): defence-supply-chain laptop sourcing (90% of prototype procurement from U.S. and allied suppliers), U.S. battery demand 179 GWh → 707 GWh 2025–2035, 3M closing 16 sites, FedEx Network 2.0 at 65% of eligible volume. None bears on planning method, forecast accuracy or the S&OP labour bill — recorded as swept and dropped, not softened.

## Dating note

Rows 1 and 2 are dated by their own publication dates (2026-10-28 and 2026-11-04); row 1's underlying fieldwork ran 2026-05-05 to 2026-06-11 and the article must say so. Row 3 carries only a month of record ("October 2026"); the leading token is the edition month, not a day. Row 4 is dated by the write-up (2026-11-04) and its index was published 2026-10-29; the claim cell keeps both dates. No row is outside the window; the four background items above are, and are labelled as such.

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=4 candidates=0 heuristic=- window=2026-10-06..2026-11-05 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

