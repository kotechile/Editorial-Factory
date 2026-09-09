# Signals: gpu_hardware — 2026-09-09
**Window:** 2026-08-10 → 2026-09-09
**Queries run:** 16 (inference economics · supply constraints · open-vs-closed silicon · memory bandwidth ceilings · vendor earnings/changelogs · HN/arxiv/x_ai fan-outs)
**Date-agnostic fallbacks:** used for every angle (backend silently drops `after:`/`since:` filters); each hit timestamp-checked against window start.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | NVIDIA Q2 FY2027: revenue $96.2B (+106% YoY), Data Center $89.0B (+117% YoY) | https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027 | 2026-08-26 | "$96.2 billion, up 106%... Data Center revenue of $89.0 billion, up 117%" | supply constraints / inference economics | 85 |
| 2 | NVIDIA supply/capacity commitments jumped $119B → $279B "primarily related to the procurement of memory" | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/nvda-20260826.htm (CFO Commentary, Ex. 99.2) | 2026-08-26 | "+$160B in one quarter, for memory" | memory bandwidth ceilings | 95 |
| 3 | CFO Colette Kress: "we expect supply to remain a bottleneck, at least through the end of fiscal year 28" + "extreme pricing conditions in memory" | https://www.investopedia.com/nvidia-earnings-live-nvda-stock-ai-trade-12068393 | 2026-08-26 | "bottleneck... through FY28"; memory prices "headed even higher into next year" | supply constraints / memory bandwidth | 92 |
| 4 | CEO Jensen Huang (earnings call): "The buzz is, everything is sold out. H100 sold out, H200s are sold out… AI native startups are really scrambling to get capacity" | https://www.tomshardware.com/pc-components/gpus/nvidia-says-its-h100-h200-gpus-are-not-sold-out-despite-jensen-alluding-otherwise-during-earnings-call-company-clarifies-it-has-plenty-of-gpu-supply | 2026-08-26 | "H100 sold out, H200s are sold out" | supply constraints | 85 |
| 5 | NVIDIA X post denies H100/H200 "sold out": "We have more than enough H100/H200 to satisfy every order without delay" | https://finance.yahoo.com/news/nvidia-denies-h100-h200-shortages-172849421.html | 2026-09-01/02 | "more than enough... to satisfy every order without delay" | supply constraints (contrarian) | 90 |
| 6 | Hyperscaler spot-instance pricing for leading-edge NVIDIA compute up 7.9% QoQ in August (analyst Rolland) | https://www.kiplinger.com/investing/live/nvidia-earnings-live-updates-and-commentary-august-2026 | 2026-08-26 | "up a strong 7.9% QOQ on average in August" | inference economics | 65 |
| 7 | AMD MI355X kernel-level benchmark gap: Oracle OCI $8.60/GPU-hr vs H200 $4.80/hr; no public attention-kernel parity | https://www.spheron.network/blog/mi355x-vs-h200-a-kernel-level-attention-benchmark-2026 | 2026-09-05 | "$8.60/GPU-hr (MI355X) vs $4.80/hr (H200)" | open-vs-closed silicon | 62 |

**Dropped (out of 30-day window, per anchor-freshness rule):** Micron "HBM sold out through calendar 2026" (announced ~April–June 2026 earnings, before 2026-08-10) — retained only as background context, not as a load-bearing signal.
