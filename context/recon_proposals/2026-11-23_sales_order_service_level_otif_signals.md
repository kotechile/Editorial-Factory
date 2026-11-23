# Signals: sales_order_service_level_otif — 2026-11-23
**Window:** 2026-10-24 → 2026-11-23
**Queries run:** 9 (supply_chain_intel MCP sweep + web fan-out: Walmart OTIF/SQEP, Target Q3, fill-rate/safety stock, JOC, Reddit r/supplychain)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Walmart's sub-30-minute delivery volume almost tripled in Q3 | https://www.supplychaindive.com/news/walmarts-sub-30-minute-delivery-volume-surges-in-q3/875339/ | 2026-11-20 | Sub-30-minute delivery volume almost tripled YoY in Q3 (US CEO David Guggina, earnings call Thursday); 30-minute delivery now reaches 60% of US households with a 15-minute in-store pick allowance; store-fulfilled deliveries +40%, expedited deliveries +50% in Q3; >80% of US e-commerce orders fulfilled from stores; "if we pick faster, we can either reach further... or deliver more quickly" | Speed as a service-level weapon | 92 |
| 2 | Walmart US online sales +23% on faster fulfillment | https://www.retaildive.com/news/walmart-ecommerce-boom-fulfillment-speed-q3-earnings/875166/ | 2026-11-19 | US e-commerce sales +23% YoY in Q3; CFO John David Rainey: "faster delivery speeds are leading to higher customer and member conversion" | Speed converts: service level as demand driver | 85 |
| 3 | Target lifts on-shelf availability >1 ppt in Q3 | https://www.supplychaindive.com/news/target-boosts-on-shelf-availability-aided-by-stronger-tech/875117/ | 2026-11-20 | On-shelf availability improved more than a full percentage point YoY in Q3, with "meaningful gains on most frequently purchased items" (EVP/COO Lisa Roath); tariff refunds added 1.1 ppt to 2.3 ppt gross-margin growth; supply-chain productivity gains partially offset by elevated freight and fuel costs | Retailer-side availability: the other half of the order book | 90 |
| 4 | Target Q3 earnings: inventory-flow review announced | https://corporate.target.com/news-features/article/2026/11/q3-2026-earnings | 2026-11-18 | On-shelf availability +1 full ppt YoY "including gains on our most frequently purchased items"; AI-powered tools help teams improve availability and keep shelves stocked; "taking a comprehensive look at how inventory moves through our entire network"; store comps +4.6%, digital +9.8%; document dated November 18, 2026 | Inventory network re-plumb, not just more stock | 88 |
| 5 | Target Q3 traffic +5%, comps +5.6% on availability turnaround | https://www.retaildive.com/news/target-traffic-rises-q3-earnings/874959 | 2026-11-18 | Comparable sales +5.6%, net sales +7.1%; traffic +5% "broad based" (CEO Michael Fiddelke); on-shelf availability rose over a full point YoY; net earnings +76% to $1.2B including ~$228M tariff refunds | Availability converts to traffic | 80 |
| 6 | 95% of retail supply chain leaders rate disruption risk critical | https://www.supplychaindive.com/spons/peak-season-optimization-is-out-year-round-optimization-is-in/875297/ | 2026-11-23 | 95% of 100 surveyed retail supply chain leaders rate disruption as extremely or very important (DP World × Supply Chain Dive Studio survey); publisher-sponsored survey, fielding window not disclosed — usable as friction, not as a measured anchor | Peak-season thinking is dead; continuous service pressure | 68 |
| 7 | Chronic expediting = a decision problem, not a forecast problem | https://www.supplychaindive.com/spons/why-more-inventory-wont-fix-your-supply-chains-fill-rate/873053 | 2026-11-23 (observation) | Vendor claim (Huron): fill rates "stuck in the low 90s" despite record inventory; the miss is produced by late, local trade-off decisions (which order to expedite, which plant to pull from), not by the forecast; no audited figures disclosed | The decision layer behind OTIF misses | 64 |

**Dating note:** Rows 1–5 are dated from each publisher's own date field (verified on-page). Row 7 is an undated vendor-sponsored page; the observation date is in the Date cell and it carries no audited figures, so it is corroboration only. Row 6 is a dated sponsored post whose survey fielding window is undisclosed — friction only.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=7 candidates=0 heuristic=- window=2026-10-24..2026-11-23 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

## Dated background
- https://www.supplychaindive.com/spons/why-more-inventory-wont-fix-your-supply-chains-fill-rate/873053 — Huron sponsored thesis page, no publication date shown, no audited figures
- https://www.supplychaindive.com/news/walmart-expands-30-minutes-or-less-delivery-as-speed-woos-shoppers/828404/ — Aug 21, 2026; 30-minute delivery in 38 US markets (out of window; context for row 1)
- https://seekingalpha.com/article/4970165-walmart-inc-wmt-q3-2027-earnings-call-transcript — Walmart earnings call transcript (primary record behind row 1)
- https://www.daserv.com/walmart-vendor-compliance-guide — Walmart OTIF/SQEP mechanics (90% on-time / 95% in-full / 3% chargeback); undated page, evergreen background, not an in-window signal
- https://www.coldstreamlogistics.com/blog/walmart-sqep-explained — SQEP phases; as of October 2026 Phase 4 not launched; undated page, background
- https://www.fool.com/earnings/call-transcripts/2026/11/19/walmart-wmt-q3-2027-earnings-call-transcript — Walmart Q3 FY27 earnings call transcript (primary record, Nov 19, 2026; added as anchor source)
- https://aichieve.net/kroger-direct-buy-retires-its-own-fine/ — own-front back-catalogue article (2026-11-02) carrying the documented 3%-of-goods chargeback structure
