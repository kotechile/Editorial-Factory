# Signals: workstation_compute_economics — 2026-10-13
**Window:** 2026-09-13 → 2026-10-13
**Queries run:** 35 web fan-outs across the vertical's seven configured sources/angles (workstation build vs cloud GPU matrix, hardware-debt/compile-hour index, local fine-tuning vs per-token fees, local vs cloud rendering ROI) + 7 primary-source fetches (NVIDIA and PNY product pages, Nebius's own rate card, the Reuters wire, ServeTheHome, getdeploying's dataset page, Tom's Hardware's price tracker), every hit timestamp-checked against the window before it was kept.

Two in-window moves landed on the *same* variable on opposite sides of the build-vs-rent ledger. On the
buy side, the RTX 5090 — the only consumer card with 32 GB, i.e. the one local-AI builders actually buy —
was reported on 2026-10-10 to be out of production, its GB202 die reserved for the professional RTX PRO
line; eleven days earlier NVIDIA's product pages had quietly listed the RTX PRO 5500, the same 21,760 CUDA
cores as the 5090 with 84 GB instead of 32 GB, no price and no ship date. On the rent side, Nebius
notified customers on 2026-09-17 that it would raise pay-as-you-go rates from 2026-10-01 — its second hike
in three months — and its steepest increase (about 41%) is on memory, not on GPU-hours. Neither source
says what the pair says: the thing being rationed is memory content, and it is being rationed by product
mix in silicon and by price in the cloud.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | NVIDIA reportedly halts RTX 5090 production, reserves GB202 for RTX PRO | https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-halts-geforce-rtx-5090-production-in-favor-of-ai-data-center-and-professional-gpus-impending-supply-drought-expected-to-drive-up-prices-rtx-5080-24gb-rumored-as-new-gaming-flagship | 2026-10-10 | A leaked factory notice cited by @hongxing2020: "NVIDIA will no longer sell any RTX 5090 models, including the D variants"; @Zed__Wang confirmed it and added "all future GB202 supplies are RTX Pro exclusive". NVIDIA has not confirmed the plan and has published no end-of-production date; Tom's Hardware notes the economics line up because GB202 "can sell on data center and professional graphics cards that cost substantially more" than the $1,999 card | The only consumer GPU with 32 GB of VRAM — the card this vertical's buyer builds around — is reportedly being withdrawn while its die moves to professional boards | 92 |
| 2 | NVIDIA quietly lists the RTX PRO 5500: 84 GB on the RTX 5090's own die, no price | https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-5500/ | 2026-09-14 (pages read 2026-09-17) | NVIDIA's and PNY's product pages: 84 GB GDDR7 with ECC, 1,398 GB/s, up to 600 W on one 16-pin CEM5 connector, PCIe Gen 5 x16, Multi-Instance GPU as one 84 GB or two 42 GB instances, air- or liquid-cooled, pitched at "rack-mounted workstation deployment"; PNY's page gives 21,760 CUDA cores — exactly the RTX 5090's count — on a 750 mm², 92.2-billion-transistor GB202. No TFLOPS, no AI TOPS, no price, no ship date; NVIDIA footnotes the table "Preliminary product specifications, subject to change" | The same silicon as the $1,999 consumer card, re-cut to carry 2.6x the memory and sold as a rack part with the price withheld | 90 |
| 3 | Nebius raises pay-as-you-go GPU rates again — second hike in three months | https://www.reuters.com/technology/nebius-hikes-ai-cloud-prices-again-demand-computing-power-soars-2026-09-17 | 2026-09-17 | Reuters: Nebius "will raise pay-as-you-go prices for leasing selected Nvidia chips from October 1, marking the company's second price hike in three months"; GPU rates +17% to 21%; some CPU-only instances +25%; "memory offerings by about 41%". Same day, rival CoreWeave "said it is signing contracts at higher prices" | The row that was supposed to be the cheap alternative to buying hardware is the one repricing, and its largest increase is the memory line | 90 |
| 4 | Nebius's own rate card carries the October 1 column | https://nebius.com/prices | 2026-10-01 effective (read 2026-10-13) | Per-GPU-hour on-demand, current vs "Price per hour (Effective October 1, 2026)": HGX H100 $3.85 → $4.50; HGX H200 $4.50 → $5.40; HGX B200 $7.15 → $8.50; HGX B300 $7.85 → $9.50; HGX RTX PRO 6000 unchanged at $1.80; AMD EPYC Genoa vCPU from $0.10 → $0.13 and Intel Ice Lake from $0.05 → $0.06 | The tiers that moved carry less memory per dollar and the 96 GB workstation card did not move — the increase tracks what is scarce, not what is fast | 85 |
| 5 | NVIDIA DGX Spark 64 GB launches at $4,999 while the 128 GB model climbs to $6,950 | https://www.servethehome.com/nvidia-dgx-spark-64gb-launched-and-big-128gb-gb10-price-increases | 2026-10-02 | The DGX Spark 64 GB ships 23 October from Acer, ASUS, Dell, Gigabyte, HP and MSI "starting at $4,999"; the 128 GB / 4 TB model "launched at $3999 about a year ago. The new price is $6950"; ServeTheHome bought 128 GB nodes "for around $3000 each" earlier the same year and calls the eight-node cluster "now a $50K+ option"; NVIDIA's own line is that two 64 GB units cluster to 128 GB "at around $8000" | The desk-side box repriced on the same memory market: half the capacity now costs more than the larger model launched at | 86 |
| 6 | Cloud GPU rental tracker: the cheap row rose and the hyperscaler premium narrowed | https://getdeploying.com/gpu-price-trends | 2026-10-05 | Provider's own dataset (55,249 weekly observations, 88 providers): H100 on-demand median $3.47/GPU/hr across 41 providers, +4.0% over four weeks and +16% over 12 months; all cloud GPU rentals +8% year-over-year, with 14 of 22 models up and 8 down; the hyperscaler premium on H100 narrowed to +75% (GPU-cloud median $4.50 vs $7.89) because the cheaper tier rose; a 1-year reservation runs about 32% below on-demand and a 3-year about 49%; H100 spot 59% of on-demand | The rental side is not a fixed floor either — the floor is the part that moved | 82 |
| 7 | RTX 5090 street price at 3.2x–4.75x MSRP a month before the production report | https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-5090-vanishes-from-online-retail-in-the-us-third-party-sellers-now-demand-as-much-as-usd9-500-for-nvidias-fastest-gpu | 2026-09-14 | First-party US retail stock "almost completely evaporated": third-party listings $6,500–$9,500 against a $1,999 launch MSRP; the cheapest in-stock card at a Micro Center store was $4,299; the tracked early-September low was $5,199 and the June median $4,299 | The card was already three times its list price before its die was reportedly reassigned, so the withdrawal lands on a market with no spare supply | 84 |

## Primary-source ledger (corroboration and dated background)

In-window corroboration of the 2026-10-10 production report (all secondary, attributed; NVIDIA has issued
no statement and has privately disputed the claim to at least one outlet, per the analysis below):
- https://www.techpowerup.com/353578/nvidia-reportedly-ending-the-rtx-5090-reserves-gb202-silicon-for-workstation-gpus (TechPowerUp, 2026-10-10 — "No more GB202 for 5090, confirmed")
- https://videocardz.com/newz/nvidia-reportedly-discontinuing-rtx-5090-gb202-gpus-to-be-reserved-for-rtx-pro-series (VideoCardz, 2026-10-10)
- https://shattered.io/nvidia-gb202-shifts-rtx-pro-5090-supply-2026 (records that NVIDIA has not confirmed and "has privately disputed the discontinuation claim to at least one outlet")

Primary vendor records behind the RTX PRO 5500 row:
- https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-5500/ (NVIDIA product page, "Coming Soon")
- https://www.pny.com/nvidia-rtx-pro-5500-blackwell (PNY: 21,760 CUDA cores, 750 mm², 92.2 bn transistors)
- https://www.techpowerup.com/gpu-specs/rtx-pro-5500-blackwell-workstation.c4449 (GPU database, launch dated September 14th, 2026)
- https://flopper.io/docs/nvidia-rtx-pro-5500-blackwell (spec table cross-check, 2026-09-17)

DGX Spark price record:
- https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark (NVIDIA's own store listing the 128 GB model at $6,950, out of stock)

**Dated background — OUTSIDE the 30-day window (not an anchor; carried for the memory-supply context only):**
- https://www.trendforce.com/presscenter/news/20260825-13198.html (TrendForce, 2026-08-25: DRAM + NAND to reach 68% of major cloud providers' capex in 2027, from 47% in 2026; server DRAM +270% cumulative in 2026; HBM contract prices could rise another 70–140% in 2027)

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=7 candidates=0 heuristic=- window=2026-09-13..2026-10-13 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

