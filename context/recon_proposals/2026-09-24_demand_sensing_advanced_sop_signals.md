# Signals: demand_sensing_advanced_sop — 2026-09-24

**Window:** 2026-08-25 → 2026-09-24 (30 calendar days)
**Queries run:** 12 (web + supply_chain_intel MCP `--recent 30` + `--search` for demand sensing / forecast / S&OP / IBP)
**Sources swept:** supply_chain_intel (healthy; 40 docs: 27 newsroom + 13 podcast), gartner_supply_chain, supply_chain_brain, supply_chain_dive, harvard_business_review, journal_of_business_forecasting, x_ai (+ web fallback: ToolsGroup, Arkieva, RELEX, Horizon, Lokad, SCMR, Viewpoint Analysis, BCG)

## Raw candidate table

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | BCG "Supply Chain Planning 2026: Why AI Alone Isn't Enough" | https://www.bcg.com/publications/2026/supply-chain-planning-why-ai-alone-isnt-enough | Feb 2026 | 181 global leaders surveyed; **78% cite forecast inaccuracy as #1 challenge** despite >70% APS investment; few translate AI/APS spend into performance gains | forecast accuracy amortization / AI ROI | 88 (primary) — **OUT of window** |
| 2 | First-ever Gartner Magic Quadrant for Supply Chain Planning Solutions (Discrete + Process industries) | https://www.toolsgroup.com/news/toolsgroup-recognized-in-the-first-ever-2026-gartner-magic-quadrant-for-supply-chain-planning-solutions-discrete-industries | Mar 18, 2026 | MQ split into Discrete/Process; Kinaxis highest Ability-to-Execute + furthest Completeness-of-Vision (Discrete); Oracle Leader in both; OMP highest in Process | ERP-native vs specialized S&OP point solutions | 86 (primary) — **OUT of window** |
| 3 | RELEX "5 forecasting accuracy questions for planning leaders" | https://www.relexsolutions.com/resources/diagnostic-forecasting-accuracy-questions | Mar 26, 2026 | **$1B safety stock → 10% forecast-error reduction frees ~$100M working capital**; Europris −17% DC inventory in 18 wks while availability 91%→97% | forecast accuracy amortization / MAPE→safety stock | 84 (vendor) — **OUT of window** |
| 4 | ToolsGroup "Forecast Accuracy in Decision-Centric Supply Chain Planning" | https://www.toolsgroup.com/blog/forecast-accuracy-decision-planning | Aug 27, 2026 | "Forecast accuracy alone rarely moves supply chain outcomes; shift focus to decision quality" (no independent primary figures) | forecast accuracy → decision quality | 65 (vendor blog) |
| 5 | Arkieva "How Late Is Your Forecast to the Party? Measuring Trend-Detection Latency" | https://arkieva.com/blog/demand-sensing | Aug 26, 2026 | Trend-detection latency as the overlooked accuracy metric (no independent primary figures) | demand sensing / forecast latency | 63 (vendor blog) |
| 6 | ToolsGroup "Discrete Manufacturing Supply Chains: Planning Challenges" | https://www.toolsgroup.com/blog/discrete-manufacturing-supply-chains-planning/ | Sep 3, 2026 | Integrated planning for demand variability / BOM complexity (no independent primary figures) | S&OP / planning | 62 (vendor blog) |
| 7 | ToolsGroup "Demand Sensing: Turning Short-Term Signals Into Better Decisions" | https://www.toolsgroup.com/blog/demand-sensing-better-decisions | Sep 10, 2026 | Sensing as overlay on baseline forecast; product-page claims 15–40% accuracy lift, 3× faster response (self-reported marketing) | spreadsheet → real-time ML demand sensing | 62 (vendor blog) |
| 8 | Arkieva "Is Your Forecast Biased, Or Just Slow?" | https://arkieva.com/blog/demand-sensing | Sep 10, 2026 | Bias vs latency framing (no independent primary figures) | forecast accuracy | 60 (vendor blog) |
| 9 | Supply Chain Now podcast "The Buzz: AI at Scale, Panama Canal Risk, and the Future of IBP" | https://supplychainnow.com/buzz-ai-scale-panama-canal-risk-future-IBP-1636 | Sep 18, 2026 | "Thousands of operational micro-decisions" leak value under human capacity (no concrete primary figure) | S&OP/IBP AI execution | 58 (podcast — below floor) |
| 10 | Supply Chain Dive sponsor "When demand won't sit still" | https://www.supplychaindive.com/spons/when-demand-wont-sit-still-building-a-more-flexible-warehouse-network/830243/ | Sep 21, 2026 | 15–30% fixed-overhead reduction via on-demand 3PL capacity (sponsored vendor content, warehouse-network angle not demand sensing) | network flexibility | 55 (sponsored — below floor) |

## Sweep verdict

- **In-window survivors ≥60** are all **tertiary vendor marketing blogs** (ToolsGroup, Arkieva) — on-topic and fresh, but carry **no independently verifiable primary figure**; their quantitative claims are self-reported product marketing.
- **Every genuinely primary signal is out of window**: BCG (Feb 2026), Gartner MQ (Mar 18, 2026), RELEX case math (Mar 2026). The 30-day window (Aug 25 → Sep 24) contains no fresh primary spike for this anchor-driven vertical.
- `supply_chain_intel` MCP holds **no demand-sensing/S&OP-specific content** across its 40 documents — the recent corpus is freight/logistics news (GRI rate hikes, executive appointments, truck electrification, tariffs) and leadership podcasts.
