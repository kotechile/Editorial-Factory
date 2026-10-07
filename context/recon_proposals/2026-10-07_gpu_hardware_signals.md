# Signals: gpu_hardware — 2026-10-07
**Window:** 2026-09-07 → 2026-10-07
**Queries run:** 16 (NVIDIA buyback · B200/H100 rental inversion · Nebius rate card · HBM4/HBM 2027 ASP · 4Q26 DRAM contract · TSMC wafer pricing · AMD MI455X/Helios · AMD World Labs · Rubin ramp · cloud GPU pricing October · quantization/distillation economics · HBM supply chain · custom ASIC growth · GPU power constraints)
**Date-agnostic fallbacks:** used throughout (backend silently drops `after:`/`since:` filters); each hit timestamp-checked against the window start. Secondary aggregators (shattered.io, tech-insider, BigGo) were traced back to their cited primary where one exists; where the primary is paywalled the row is marked and the figure carries its attribution.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | TrendForce raises 2027 HBM price outlook — blended ASP to jump 121% YoY | https://www.trendforce.com/presscenter/news/20260929-13255.html | 2026-09-29 | "Blended ASP is now projected to jump 121% YoY" | memory bandwidth ceilings / supply constraints | 90 |
| 2 | TrendForce: HBM supply stays tight through 2027; GPU/ASIC makers weigh cutting HBM density per package (8-Hi vs 12-Hi) | https://www.trendforce.com/presscenter/news/20260929-13255.html | 2026-09-29 | "GPU and ASIC manufacturers are now considering reducing HBM capacity per device… 8-Hi products to carry a roughly 10–20% price premium per Gb over 12-Hi products in 2027" | memory bandwidth ceilings / supply constraints | 74 |
| 3 | TrendForce: 4Q26 conventional DRAM contract prices to rise 10–15% QoQ; server DRAM to stay undersupplied | https://www.trendforce.com/presscenter/news/20260930-13258.html | 2026-09-30 | "Conventional DRAM contract prices are projected to grow 10–15% QoQ in 4Q26" | supply constraints | 82 |
| 4 | Nebius raises on-demand GPU rates effective Oct 1, 2026 — H100 +17%, H200 +20%, B200 +19%, B300 +21% | https://nebius.com/prices | 2026-09-17 | "NVIDIA HGX H100 $3.85 → $4.50; HGX H200 $4.50 → $5.40; HGX B200 $7.15 → $8.50; HGX B300 $7.85 → $9.50 (Effective October 1, 2026)" | inference economics | 92 |
| 5 | Nebius also lifts the memory and CPU tiers — Genoa EPYC +25%, Genoa memory ~+41%, its second hike in three months | https://nebius.com/prices | 2026-10-01 | AMD EPYC Genoa memory "from $0.0032 → $0.0045 per GiB-hour" (~41%); Genoa CPU ~+25% | inference economics | 80 |
| 6 | SemiAnalysis GPU pricing index: B200 rental $8.01/GPU-hour, +79% in three months; B200 now 21% MORE per unit of compute than the older H100 | https://gpu-index.semianalysis.com/ | 2026-09-25 | "B200 cloud-rental rates climbed 79% over three months to reach $8.01 per GPU-hour"; "a B200 now costs 21% more per unit of compute than an H100… a full reversal from June 2026, when a B200 was actually 18% cheaper" | inference economics | 93 |
| 7 | getdeploying.com price dataset: cloud GPU rental prices up 8% over the year; H100 median $3.47/GPU-hour (+16% YoY) across 41 providers; B200 GPU-cloud median $8.55 vs $14.24 at hyperscalers | https://getdeploying.com/gpu-price-trends | 2026-10-05 | "Cloud GPU rental prices are up 8% over the year"; "Nvidia H100… median of $3.47 per GPU per hour… up 16% over the last 12 months" | inference economics | 78 |
| 8 | NVIDIA authorizes a record $150B increase to its share buyback, taking the remaining program to $235B | https://nvidianews.nvidia.com/news/nvidia-announces-a-150-billion-share-repurchase-authorization-increase | 2026-09-28 | "authorized an additional $150 billion under the company's existing share repurchase program, increasing the total remaining amount authorized to $235 billion" | ecosystem moat / unit economics | 80 |
| 9 | AMD agrees to acquire World Labs for $8.2B, all-stock; Fei-Fei Li joins as EVP & Chief Scientist | https://ir.amd.com/news-events/press-releases/detail/1299/amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute | 2026-09-28 | "all-stock transaction… valued at approximately $8.2 billion… expected to close by the end of 2026" | open-source vs closed silicon / hardware-model co-design | 72 |

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=9 candidates=0 heuristic=- window=2026-09-07..2026-10-07 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

