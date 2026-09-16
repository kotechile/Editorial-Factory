# Signals: gpu_hardware — 2026-09-16
**Window:** 2026-08-17 → 2026-09-16
**Queries run:** 12 (inference economics · supply constraints · open-vs-closed silicon · memory bandwidth ceilings · vendor changelogs · HN/arxiv/x_ai fan-outs + custom-silicon + Rubin/HBM4 + B300 pricing)
**Date-agnostic fallbacks:** used throughout (backend silently drops `after:`/`since:` filters); each hit timestamp-checked against window start.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | OpenAI's first custom chip (Jalapeño, w/ Broadcom) posts first measured benchmark: 1.5–1.9× more AI work per watt, 1.7–3.6× lower latency vs NVIDIA GB300/GB200 | https://openai.com/index/jalapeno-first-results/ | 2026-08-25 | "1.5 to 1.9 times more AI work per watt at peak throughput and 1.7 to 3.6 times lower end-to-end latency than the comparison systems" | inference economics / closed silicon | 95 |
| 2 | Jalapeño rated 700 W (sustained ≤550 W) vs GB300 1,400 W; Kimi K2.5 1T: ~1.5× perf/watt, 3.4× lower latency (1.56 s vs 5.31 s) | https://openai.com/index/jalapeno-first-results/ | 2026-08-25 | "rated at 700 watts… at or below 550 watts"; "18,195 vs. 11,862 mixed / kW"; "1.56 s vs. 5.31 s" | inference economics | 92 |
| 3 | OpenAI full-stack compute strategy: "first-party path alongside the accelerators we use from other partners" (NVIDIA, AMD, Broadcom, Cerebras, CoreWeave…) | https://openai.com/index/the-full-stack-behind-abundant-intelligence/ | 2026-08-25 | "credible first-party path alongside the accelerators we use from other partners" | open-vs-closed silicon | 78 |
| 4 | AMD Instinct MI455X (CDNA 5) at Hot Chips 2026: 432 GB HBM4, 23.3 TB/s bandwidth, 40.26 PFLOPS MXFP4 — open ROCm counter to closed ASICs | https://www.servethehome.com/amd-mi400-gpu-at-hot-chips-2026 | 2026-08 (STH coverage 09-15) | "432GB at 23.3 TB/s"; "40.26 petaflops" MXFP4 | open-vs-closed silicon | 72 |
| 5 | Meta's Iris (MTIA) chip enters production Sept 2026; targets 14 GW compute by 2027 | https://www.reuters.com/world/asia-pacific/meta-put-ai-chip-into-production-september-it-looks-double-computing-capacity-2026-07-09 (broke 07-09; production-start is in-window) | 2026-09 (production) | "start manufacturing… from September"; "14 gigawatts next year" | closed silicon | 68 |
| 6 | NVIDIA B300 cloud pricing firms: $8.44/hr on-demand (Spheron 08 Sep) — demand outpacing 288 GB tier supply | https://www.spheron.network/blog/nvidia-b300-blackwell-ultra-guide | 2026-09-08 | "$8.44/hr on-demand and $5.85/hr spot… as of 08 Sep 2026" | supply constraints | 60 |

**Dropped (out of 30-day window, anchor-freshness rule):**
- OpenAI-Broadcom Jalapeño *announcement* (June 24, 2026) — pre-window; retained only as the primary source for the chip's provenance, not as a fresh signal. The fresh event is the Aug 25 benchmark.
- Micron HBM4 "high-volume production" (Mar 16, 2026) / SK Hynix & Samsung HBM4 CES 2026 (Jan) — pre-window.
- AMD MLPerf Inference 6.0 (Apr 2026) — pre-window.
- TrendForce custom-ASIC +44.6% YoY (May 2026) — pre-window; background context only.
