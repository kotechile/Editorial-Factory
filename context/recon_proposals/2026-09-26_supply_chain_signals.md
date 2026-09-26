# Signals: supply_chain — 2026-09-26

**Window:** 2026-08-27 → 2026-09-26
**Queries run:** 1 (Supply Chain Intel MCP `--recent 30 --limit 60`; 51 documents, 40 newsroom / 11 podcast) + verification web searches. Load-bearing signals #1/#2 upgraded from their Supply Chain Dive aggregator URLs to primary sources (NBC News; Federal Reserve Bank of Atlanta) during fact-check.
**Source:** Coolify Supply Chain Intelligence server (`intel.giniloh.com`) — healthy (51 docs)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | US, China extend trade-war truce by 2 months to Jan 10 | https://www.nbcnews.com/business/economy/us-china-extend-trade-truce-trump-rcna599525 | 2026-09-23 | Bessent: "Busan Agreement" economic détente extended from Nov 10 → Jan 10, 2027 | Tariff cliff / sourcing risk | 85 |
| 2 | Atlanta Fed: most firms hoarding IEEPA tariff refunds as cash | https://www.atlantafed.org/research-and-data/publications/policy-hub-macroblog/2026/09/21/how-are-firms-using-tariff-refunds | 2026-09-21 | 70% retain at least some refund as cash; ~$100B of ~$170B refunded by late July | Working capital / tariff refund behavior | 80 |
| 3 | Amazon adds AI supply chain agents (inbound planning + aged inventory) | https://www.supplychaindive.com/news/amazon-ai-supply-chain-agents-among-seller-upgrades/831164 | 2026-09-24 | 2 agentic capabilities on Seller Assistant; no benchmarks/ROI disclosed | Agentic exception handling / AI ops | 68 |
| 4 | Lego to spend $400M on Mexico warehouse space | https://www.supplychaindive.com/news/lego-to-spend-400m-to-add-warehouse-space-at-mexico-plant/831302 | 2026-09-25 | $400M capex for warehouse + packing at Mexico plant | Nearshoring / regionalization | 70 |
| 5 | Lowe's debuts drone delivery pilot (Wing + DoorDash) | https://www.supplychaindive.com/news/lowes-debuts-drone-delivery-pilot-with-wing-doordash/831162 | 2026-09-24 | 100+ SKUs, 1 store (NC), 2 delivery partners | Last-mile / micro-fulfillment | 65 |
| 6 | USPS warns Indianapolis, Louisville parcel delays | https://www.supplychaindive.com/news/usps-warns-of-indianapolis-louisville-delays-due-to-facility-upgrades/831390 | 2026-09-25 | 2 facilities; sorting-equipment installs disrupt peak-season flows (no volume disclosed) | Parcel ops / facility upgrades | 62 |
| 7 | Shippers exploring port-to-inland transit to de-risk | https://www.supplychaindive.com/news/shippers-are-exploring-port-to-inland-transit-to-de-risk-supply-chains/831261 | 2026-09-25 | Qualitative route-stability shift (APM Terminals Mobile MD); no benchmark cited | Network resilience / port diversification | 63 |
| 8 | 6 food manufacturers on supply chain tactics (Barclays) | https://www.supplychaindive.com/news/6-food-manufacturers-talk-supply-chain-tactics/831214 | 2026-09-25 | Cost cuts + demand forecasting cited as top levers; no figures | Demand forecasting / freight volatility | 60 |

**Retread flags (per virality_judge §3.5):**
- #2 (Atlanta Fed IEEPA refund usage) shares the IEEPA-refund underlying event with the 2026-09-07 winner `ieepa-refund-wave-hits-earnings`; the Atlanta Fed macroblog (Sept 21) is a NEW primary data point on refund *usage*, but the standalone novelty is capped ≤ 6.0.
- #4 (Lego $400M Mexico warehouse) re-argues the 2026-09-10 winner `reshoring-capacity-gap` (nearshoring/regionalization). Cap Novelty ≤ 6.0.
- #5 (Lowe's drone) is last-mile/micro-fulfillment territory adjacent to the 2026-09-25 `last_mile_routing_fleet_carbon` run — different vertical, but overlapping domain.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=8 candidates=2 heuristic=0.70-0.71 window=2026-08-27..2026-09-26 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #1 ⨂ #4 | freight_chokepoint_x_nearshoring | A: Tariff cliff / sourcing risk | B: Nearshoring / regionalization | https://www.nbcnews.com/business/economy/us-china-extend-trade-truce-trump-rcna599525 https://www.supplychaindive.com/news/lego-to-spend-400m-to-add-warehouse-space-at-mexico-plant/831302 | 0.71 | - |
| 2 | #2 ⨂ #4 | freight_chokepoint_x_nearshoring | A: Working capital / tariff refund behavior | B: Nearshoring / regionalization | https://www.atlantafed.org/research-and-data/publications/policy-hub-macroblog/2026/09/21/how-are-firms-using-tariff-refunds https://www.supplychaindive.com/news/lego-to-spend-400m-to-add-warehouse-space-at-mexico-plant/831302 | 0.7 | - |

**Heuristic terms (advisory):**
- #1: token_coverage=0.75 intensity=0.78 angle_fit=0.25 contrast=1.0 → 0.71 (freight_chokepoint_x_nearshoring)
- #2: token_coverage=0.75 intensity=0.75 angle_fit=0.25 contrast=1.0 → 0.7 (freight_chokepoint_x_nearshoring)
<!-- synthesis-seed:end -->
