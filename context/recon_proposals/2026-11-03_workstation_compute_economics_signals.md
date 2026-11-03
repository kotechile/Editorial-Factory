# Signals: workstation_compute_economics — 2026-11-03

**Window:** 2026-10-04 → 2026-11-03
**Queries run:** 12 web fan-outs across the vertical's configured sources and four primary angles (workstation build vs cloud matrix, hardware-debt/compile hours, local fine-tuning vs per-token fees, local vs cloud rendering), plus 8 primary pages fetched and read at source (the NVIDIA newsroom launch release, Tom's Hardware's launch price round-up, the RamRadar index, the getdeploying rental tracker, the American Compute resale index, an ASUS/HP price round-up via trade press, Apple's Mac Studio release, VideoCardz's DGX Spark price note). Every row below carries the publisher's own date.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | NVIDIA puts its Grace-Blackwell superchip into mainstream Windows laptops | https://nvidianews.nvidia.com/news/nvidia-rtx-spark-pcs-available-today-a-new-beginning-for-windows-pcs | 2026-10-16 | "NVIDIA RTX Spark laptops are available today from ASUS, Dell, HP, Lenovo, Microsoft and MSI"; "up to 1 petaflop of AI compute and up to 128GB of unified memory" | Local AI capacity moves from the dev box into the OEM laptop channel | 94 |
| 2 | The launch price ladder, model by model | https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models | 2026-10-16 | "ranging from the Asus ProArt P14 with 24GB of memory for $2,599 up to the Surface Laptop Ultra with 48GB of memory for $3,999"; ProArt P16 "starting at $4,499.99 for the 64GB configuration", "128GB … $6,999.99"; HP OmniBook X 128GB $5,109 | Where the money actually sits on the config ladder | 92 |
| 3 | The cheap rungs carry a cut chip | https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models | 2026-10-16 | "we've only seen the 18-core CPU/5120-core GPU version with laptops that have 24GB or 32GB of Unified Memory. Listings with 48GB or above have the full chip" | The entry rung is a different machine, not a smaller one | 88 |
| 4 | Desktop DDR5 reprices 13.3% in thirty days | https://ramradar.app/ram-price-index | 2026-10-31 | DDR5 median "asking price of $18.12/GB across 211 tracked kits", mean $19.66/GB; "The mean moved +13.3% from October 1, 2026 to October 31, 2026"; DDR4 $7.81 median / $8.40 mean, +11.7% | The one input in a local box that reprices monthly | 96 |
| 5 | Cloud GPU rent is up 8% in four weeks | https://getdeploying.com/gpu-price-trends | 2026-10-26 | H100 median "$3.84 /GPU/hr" across 39 providers, "up 14% over the last 4 weeks and up 29% over the last 12 months"; market "+8% Sep 28 → Oct 26"; a 3-year reservation "about 48% less" than on-demand | The rent side of the same decision, on its own clock | 90 |
| 6 | The launch ships a 74B model in a 24GB build | https://nvidianews.nvidia.com/news/nvidia-rtx-spark-pcs-available-today-a-new-beginning-for-windows-pcs | 2026-10-16 | "Nemotron 3.5 Bolt 74B-A9B 24GB, a 74-billion-parameter model optimized for tool calling and multistep tasks, brings more capable local AI to supported RTX Spark configurations" | The footprint label is the product name on the entry rung | 80 |
| 7 | A laptop becomes the house inference server | https://nvidianews.nvidia.com/news/nvidia-rtx-spark-pcs-available-today-a-new-beginning-for-windows-pcs | 2026-10-16 | PAIR "letting RTX Spark serve AI inference to compatible Windows, Linux and macOS computers on a home network while keeping other PCs free for creating and gaming" | One purchased device amortised across a household's clients | 72 |
| 8 | Discrete workstation cards rent by the hour beside the laptops | https://getdeploying.com/gpu-price-trends | 2026-10-26 | RTX PRO 6000: $2.15/GPU/hr on GPU clouds against $4.50 at hyperscalers, a "+109%" gap; H200 $5.40 against $10.85, "+101%" | The rental alternative priced against the same card class | 70 |

**Dating note.** Every row is dated from the publisher's own page: rows 1, 3, 6 and 7 from NVIDIA's release of 2026-10-16, rows 2 and 3 from Tom's Hardware's launch-day round-up of 2026-10-16, row 4 from the RamRadar index whose latest data point is 2026-10-31 (read 2026-11-03), and rows 5 and 8 from the getdeploying tracker whose latest recorded week closes 2026-10-26. No row is dated from a search-result snippet.

## Dated background

Out-of-window or prior-cycle material that nonetheless belongs in the record — and every URL here that a draft might cite must live in this file for `synthesize_topics.py --check-briefs`:

- https://videocardz.com/newz/nvidia-dgx-spark-drops-to-64gb-memory-but-costs-more-than-the-original-128gb-version — 2026-10-02, the 64GB DGX Spark at $4,999 against the 128GB's original $3,999. Already the anchor of this desk's 2026-10-13 and 2026-10-27 pieces; carried here only so this run does not re-argue it.
- https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra — 2026-08-25, Mac Studio M5 Max/M5 Ultra with up to 512GB unified memory. Out of window; the delivered-versus-announced lag is a standing fact, not this week's signal.
- https://www.amcompute.com/gpu-resale-index — the GPU Resale Index reads 75 for August 2026 (down 12% on July, "the lowest in the 13 months we publish"), published in the October 2026 Rack Report. The reading is outside the window, so it is corroboration for the direction of used-hardware prices, never an anchor.
- https://www.spheron.network/blog/gpu-depreciation-in-2026-how-fast-h100s-and-h200s-lose-value — 2026-10-09, a vendor blog restating resale bands. Secondary; corroboration only.
- https://www.tomshardware.com/pc-components/ram/ram-price-index-2026-lowest-price-on-ddr5-and-ddr4-memory-of-all-capacities — Tom's Hardware's RAM deal tracker: "a conventional 32GB (2x16GB) DDR5 memory kit sold for around $100 to $200 in October 2025, but the same kit now starts at $350, if it's even in stock." Undated on the page, so it corroborates the direction of row 4 and is never dated as a signal.

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=8 candidates=0 heuristic=- window=2026-10-04..2026-11-03 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

