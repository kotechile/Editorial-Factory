# Signals: workstation_compute_economics — 2026-11-24
**Window:** 2026-10-25 → 2026-11-24
**Queries run:** 11 (web fan-out across tomshardware, lambda pricing, puget systems, hacker news/Algolia, arXiv skipped — no dated in-window paper surfaced for this beat; publisher-date lookups run on every trade-press row before it was written)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Nvidia removes RTX 5080 listing after RTX 5090 removal | https://www.tomshardware.com/pc-components/gpus/nvidia-store-quietly-pulls-the-rtx-5080-following-rtx-5090-removal-street-prices-climb-to-2-2x-over-msrp | 2026-10-30 | Cheapest in-stock RTX 5080 (PNY ARGB Epic-X RGB OC) retails $2,199.99 = 2.2× its $999 MSRP; Nvidia store no longer lists the 5090 or the 5080, fueling rumors production shifted away from consumer Blackwell | local workstation build vs cloud | 88 |
| 2 | Three used V100s outpace a $5,399 M5 Max Mac Studio | https://www.tomshardware.com/tech-industry/artificial-intelligence/three-e-waste-nvidia-v100s-hit-100-tokens-per-second-on-qwen-3-6-35b-in-a-usd1-042-homelab-rig-decommissioned-gpus-outpace-a-usd5-399-m5-max-mac-studio-at-long-contexts | 2026-11-19 | Three decommissioned V100-16GB in a $1,042 Supermicro rig hit 100 tok/s on Qwen 3.6 35B (Q4, 4K context; 77–105 tok/s across 128K→4K) vs DGX Spark's 45.8 tok/s; builder daily-drives the stack; 130+ llama.cpp tests across 9 builds | e-waste build vs new-hardware economics | 85 |
| 3 | RTX 5090 price index: $216 per GB of VRAM | https://vdf.ai/blog/rtx-5090-local-llm | 2026-11-14 | Tom's GPU price index (updated 2026-11-03) lists cheapest US RTX 5090 at $6,919 vs $1,999 launch (also the lowest recorded); ≈$216/GB VRAM vs $62/GB at launch; new RTX 4090 at $4,999 vs $1,599 launch; dual-5090 test platform >$13,000 | developer hardware debt index | 82 |
| 4 | GPU prices jump 11% | https://shattered.io/gpu-prices-jump-11-percent-rtx-5090-1-48-million-yen-2026 | 2026-11-03 | RTX 5090 street ≈$9,400 (observed 2026-11-02, not an official price); cards with the same 16GB GDDR7 sit $361–$1,201 above launch; TrendForce (2026-09-30) says GDDR6 supply is being cut and GDDR7 is tight as capacity redirects to server DRAM | memory shortage → workstation capex | 78 |
| 5 | Sam Altman: home-PC DRAM is "quite terrible" global allocation | https://www.techpowerup.com/354346/openai-ceo-argues-home-pcs-waste-the-worlds-limited-dram-supply | 2026-10-31 | On the Cheeky Pint podcast (episode dated Oct 29, 2026) Altman called it "quite terrible to have everybody have a bunch of the world's limited supply of DRAM sitting in their own computer… used 5% of the time"; article notes OpenAI's Stargate memory demand projected up to 900,000 DRAM wafers/month ≈40% of global output; Dell CEO expects shortage worse in 2027 | local inference legitimacy under attack | 90 |
| 6 | Lambda resets cloud GPU pricing | https://lambda.com/pricing | 2026-11-24 (observed) | Lambda's public pricing page states new prices take effect November 16, 2026 at 00:00 UTC (H100/H200/B200 rental list reset); the event date Nov 16 is inside the window, the page itself is a standing record | rent leg of build-vs-rent matrix | 70 |
| 7 | Used pro-GPU market repriced upward | https://pcserverandparts.com/news/gpu-price-increase-2026 | 2026-10-28 | Reseller price guide checked Oct 28, 2026: RTX A4000 16GB +$889.99 (two in stock), RTX A6000 48GB +$4,499.00 (one), Quadro P5000 +$344.99; guide names a "when not to buy from us" section — even used workstation cards now appreciate | hardware debt index (used market) | 72 |
| 8 | TrnRT: open-source LLM inference on AWS Trainium | https://github.com/RunanywhereAI/trnrt | 2026-11-17 | Show HN (54 points): TrnRT, an open-source LLM inference engine targeting AWS Trainium — a non-Nvidia accelerator getting first-class open tooling this window | non-Nvidia compute escape hatch | 65 |
| 9 | HN: RTX 5090 street prices top $9k | https://news.ycombinator.com/item?id=50363861 | 2026-11-04 | 78-point HN discussion "RTX 5090 Street Prices Top $9k as Nvidia GPU Costs Climb" (via aroundprague.cz story page) — community confirming the retail index at the high end | hardware debt sentiment | 68 |

## Dated background (URLs for --check-briefs, not rows)
- https://www.thundercompute.com/blog/best-gpu-for-ai-guide — cloud-GPU pricing comparison "as of October 2026" but page published 2026-07-08 (out of window; on-demand $/hr ladder quoted with care only).
- https://www.tomshardware.com/tech-industry/this-week-in-toms-hardware-premium-november-14-2026-mac-studio-versus-dgx-spark-amds-mext-cuts-dram-requirements-in-half-and-the-huang-saga-reaches-critical-mass — 2026-11-14 premium roundup: Mac Studio vs DGX Spark benchmark suite; AMD MEXT halves DRAM requirements.
- https://aroundprague.cz/en/news/us/rtx-5090-street-prices-top-9-000-as-nvidia-gpu-costs-climb — the story page behind row 9.
- https://wccftech.com/nvidia-rtx-50-gpus-see-a-massive-price-increase-in-november — Colorful board-partner November price ladder (+$330–550 on 5090D v2, +$380–450 on 5080); page 403s to direct fetch, date unverified → background only.

**Dating note:** every row is a dated publication (or, for row 6, a standing pricing page whose *effective* date 2026-11-16 sits in the window and is stated in the claim cell). Row 5's quote is dated to the podcast episode (Oct 29) by the article itself; the row date is the article's own datePublished (2026-10-31). No event-dated status rows.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=9 candidates=0 heuristic=- window=2026-10-25..2026-11-24 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->
