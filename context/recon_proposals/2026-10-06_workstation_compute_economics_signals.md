# Signals: workstation_compute_economics — 2026-10-06
**Window:** 2026-09-06 → 2026-10-06
**Queries run:** 16 (GPU/workstation price trackers, memory-supply primaries, cloud-GPU rental price trackers, HN/community, vendor pricing pages)

Two in-window cost shocks landed on the same decision this cycle: the memory crunch repriced the
*local* rig upward (a GPU at ~3x its launch MSRP, memory contracts rising through 2028), and the
*cloud* side stopped being one number (the same H100 rents at a ~3.2x spread, $2.46 vs $7.89/hr,
depending only on the provider). Neither source states the collision; the build-vs-rent matrix now
has a provider column nobody models.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | RTX 5090 vanishes from first-party US retail | https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-5090-vanishes-from-online-retail-in-the-us-third-party-sellers-now-demand-as-much-as-usd9-500-for-nvidias-fastest-gpu | 2026-09-14 | First-party stock "almost completely evaporated"; third-party listings $6,500–$9,500 (cheapest $6,395 Amazon / $6,449 Newegg; Newegg first result $8,699) against a $1,999 launch MSRP; June median was $4,299, early-September low $5,199; the card holds 32GB GDDR7 that "starts to look attractive for building an AI server" | Local workstation capital cost is repricing up: the exact GPU local-AI builders buy is ~3.2x MSRP | 88 |
| 2 | Micron FQ4 2026 earnings call | https://www.cio.com/article/4229625/memory-squeeze-set-to-tighten-through-2028-micron-says.html | 2026-10-01 | Micron DRAM prices +"high teens" % and NAND +~30% in the fiscal Q4; CEO Sanjay Mehrotra: supply-demand "much tighter in calendar 2027 and 2028 than they were in 2026" and "no line of sight to when supply and demand will return to balance"; >75% of 2027 output already committed; IDC: PC ASPs +17% in 2026 | The memory supply is the binding constraint and the suppliers say relief is years away | 90 |
| 3 | TrendForce Q4 2026 contract-price forecast | https://www.trendforce.com/presscenter/news/20260930-13258.html | 2026-09-30 | Conventional DRAM contract prices forecast to rise another 10%–15% in Q4 2026 from Q3; NAND flash +15%–20%; "increases are slowing but the market remains undersupplied" | Prices keep climbing into the quarter the reader is buying in | 80 |
| 4 | Cloud GPU rental price index | https://getdeploying.com/gpu-price-trends | 2026-09-28 | H100 on-demand median $3.39/GPU/hr across 41 providers (own dataset, 53,914 weekly observations); +2.0% over 4 weeks (Aug 31 → Sep 28), +14% over 12 months; cloud GPU rental +10% year-over-year; hyperscalers charge ~105% more than dedicated clouds (H100 $7.89 vs $3.85; H200 $10.85 vs $4.50 = +141%); spot ≈53% of on-demand; 1-yr reserved −28%, 3-yr −49% | Cloud compute is no longer one price: it is a spread, and the hyperscaler row is the expensive one | 86 |
| 5 | Provider-vs-provider GPU price comparison | https://computeprices.com/compare/coreweave-vs-lambda | 2026-09-29 | Same H100 SXM 80GB: CoreWeave $2.46/hr vs Lambda $3.99/hr (−38.3%); A100 SXM CoreWeave $1.21 vs Lambda $1.99 (−39.4%); B200 CoreWeave $4.26 vs Lambda $6.69 (−36.3%); GH200 flips the other way — Lambda $2.29 vs CoreWeave $6.50 (+183.8%) | Identical silicon, up to ~3.2x spread; the provider you pick sets the price, not the chip | 82 |
| 6 | GPU-cloud rate card audit (verified from provider pages) | https://guptadeepak.com/tools/top-7-gpu-cloud-ai-compute-providers-2026 | 2026-09-18 | Seven providers verified from their own pricing pages on 18 Sep 2026: $1.99/GPU-hr floor (Together preemptible, RunPod Community PCIe) to CoreWeave ~$6.16; Crusoe $3.90, Modal $3.95 effective, Lambda/Together on-demand $3.99; reserved H100 $3.19–$3.69, preemptible H100 $1.99 | The floor and the ceiling for the same class of card sit in a ~3x band the buyer never sees on AWS | 78 |

## Candidate Synthesis Pairs
<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=6 candidates=0 heuristic=- window=2026-09-06..2026-10-06 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->
| Pair | Signals | Collision Vector / Emergent Inquiry | Estimated Emergence (1-10) |
|---|---|---|---|
| (seeded by `synthesize_topics.py --seed`) | | | |
