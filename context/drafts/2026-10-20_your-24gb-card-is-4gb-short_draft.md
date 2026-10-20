---
title: "Your 24GB Card Is 4GB Short: The Label Trap"
vertical: workstation_compute_economics
persona: infra_engineer
one_big_thing: "The model that was meant to make a 24GB card enough ships with a 28GB recipe and was benchmarked on a 128GB laptop, so the unit of local AI is now the memory pool rather than the graphics card."
date: 2026-10-20
slug: your-24gb-card-is-4gb-short
synthesis: true
sources:
  - https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Bolt-24GB/
  - https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models
---

<!-- lead -->
Nvidia calls Nemotron 3.5 Bolt its 24GB build, and on 15 October it shipped the weights. The vendor's own deployment table asks for a 28GB recipe at the small end, so the card the label points at is four gigabytes short of the smallest setup Nvidia lists. The 84 tokens a second on the spec sheet were measured on a laptop holding 128GB of memory, a laptop that went on sale the next day for between $5,109 and $6,999.99.

<!-- tension -->

## The big picture:

The compression work behind this model is real, and it is the most interesting thing in local AI this month. Nvidia took its 120-billion-parameter Super VL model and squeezed it to 74 billion parameters, of which about 9 billion are active for any one token [1]. It trained the experts down to 2.0625 bits per weight, then retrained to recover the accuracy [1]. On Nvidia's own graduate-level science benchmark it scores 86.43, against 83.40 for Qwen3.6-35B-A3B [1].

What did not compress is the deployment envelope. The model card lists discrete cards at 32GB and 48GB and up, with 28GB and 32GB recipes below that line [2]. The research page puts the design target at a footprint below 24GB at batch size 1 and 128K context [1]. Both sentences can be true only if the label means the weights alone at one user. The table means the weights plus the vision encoder, plus the drafter, plus the context. My read is that the label is a floor for a chat window and the table is a floor for an agent.

I keep coming back to what that does at the shelf. The card those recipes actually assume is the 32GB one, and in France it rose another €500 in the week to 16 October, to €6,499.90 [6]. That is up €2,000 since 14 August, on a 16-card tracker where seven cards rose, nine did not move and none fell [6]. The general memory curve bends the other way. TrendForce has conventional memory contracts slowing to 10–15% for the fourth quarter, while graphics memory stays on what it calls an upward trajectory because fast memory output is limited [8].

The other half of the week was the form factor. Nvidia's Spark laptops went on general sale on 16 October with memory options of 24GB, 32GB, 48GB, 64GB and 128GB [4]. The cheap end is an Asus ProArt P14 with 24GB for $2,599. HP (the computer maker) lists a 128GB OmniBook X with 1TB of storage at $5,109, and Asus lists a 128GB ProArt P16 with 2TB at $6,999.99 [4]. Microsoft's Surface Laptop Ultra runs from $2,599.99 for 24GB to $5,899.99 for 128GB [5].

## By the numbers

- **28GB — Nvidia's smallest recipe:** the model card's deployment table starts at 28GB and lists discrete cards at 32GB and 48GB and up, one rung above the 24GB in the product name [2].
- **€6,499.90 — 32GB on a card:** the tracked French price for the 32GB flagship on 16 October, up €500 in a week and €2,000 since 14 August, on a tracker where nothing fell [6].
- **$39.9 to $108 — cost per gigabyte of pool:** $5,109 buys 128GB in HP's laptop and $2,599 buys 24GB in Asus's, which is $39.9 and $108 a gigabyte (the desk's arithmetic on list prices) [4].
- **+47% — the used-24GB premium:** a 2020-era 24GB card sells for $1,361 used, against a twelve-month average of $927, after climbing from $701 in December to $1,344 in September [7].

<!-- tactical-insight -->

## What I'd watch:

The bandwidth question is the one I would want answered first. A shared pool of low-power memory is not 128GB of dedicated video memory, and Microsoft's own documentation says the share available to the graphics processor depends on the configuration and the workload [5]. Capacity is cheap in this shape, and bandwidth is what the buyer gives up. Nvidia measured 83.99 tokens a second on a 128GB Surface, against 96.63 for Qwen3.6-35B-A3B and 100.56 for Gemma 4 26B-A4B on the same harness [1]. That is a 13% to 17% deficit, and nobody has published a 32GB-card number to compare it with.

The price spread inside one product line is the other thing I am watching. The same 128GB of the same silicon is $5,109 from HP and $6,999.99 from Asus, which is 37% more for an extra terabyte and a different badge [4]. A market with no reference price for a new unit of capacity produces that spread, and it usually closes inside two quarters.

Then there is the secondhand floor, which is the part that surprises me. A 24GB card launched in 2020 is now $1,361 used, 47% above its twelve-month average and 9% below its launch price [7]. It is not in Nvidia's deployment table, which starts at 32GB for discrete cards [2]. The people bidding it up are buying memory rather than support, and I would want to know how many of them have run a 28GB recipe on one.

The last signal is the small model. Nvidia ships a 4GB variant of Bolt on 23 October [3]. If the next tier lands under the 28GB envelope instead of above it, the whole ladder drops a rung and this week's card prices look like a peak rather than a floor.

<!-- nuanced-takeaway -->

## The catch

Every benchmark here is Nvidia's own, on Nvidia's harness, and none of it has been reproduced independently yet [1]. The speed comparison is a laptop against a laptop, and the vendor picked the laptop.

The shared pool deserves the same suspicion in the other direction. It is capacity, not bandwidth, and the share a graphics processor can address varies by machine [5]. Nvidia's own "1 petaflop" line is a theoretical peak with sparsity, per Microsoft's documentation [5]. A laptop that runs a 74-billion-parameter mixture-of-experts model at 84 tokens a second is not the same claim as a workstation that trains on it.

My read, held loosely: one week of tracker data and one model launch is a thin base for a rule about how local AI gets bought. The envelope could be a launch-week artifact of a 256K context and an early drafter. What makes me doubt that is the used market, which moved 47% before any of this shipped.

<!-- tldr -->

## At a glance

- **The Big Shift:** Nvidia shipped a local agent model labelled 24GB whose own deployment table starts at 28GB and asks for a 32GB or 48GB card, and measured its speed on a 128GB laptop that went on sale the next day.
- **Why It Matters:** the memory that runs the model is now sold in two shapes at very different prices per gigabyte, and the card shape is the dear one at €6,499.90 for 32GB while $5,109 buys 128GB in a laptop.
- **What I'd Watch:** whether capacity or bandwidth ends up setting the price of local agent work, and how fast the spread across brands closes.
  - **Tokens a second at long context:** the number that decides whether a shared pool is usable for agents, which nobody has published for a 32GB card yet.
  - **The spread across brands:** identical memory capacity listed at $5,109 and $6,999.99 on launch day, a gap that tends to close as supply settles.
  - **The 4GB variant:** Nvidia's small Bolt ships on 23 October and would move the software floor below the hardware one.
- **The Catch:** the benchmarks are the vendor's own, the pool is slower memory than a card's, and one week of retail tracking is not a trend.

## Sources

[1] NVIDIA Nemotron research page, "NVIDIA Nemotron 3.5 Bolt 74B-A9B 24GB" (published 2026-10-15) — 74B total / 9B active, IQ2_XXS at 2.0625 bits per element, the "below 24 GB at batch size 1 and 128K context" design target, the 83.99 / 96.63 / 100.56 TPS table and GPQA Diamond 86.43 / 83.40, measured "with the same RTX Spark hardware (Surface Laptop Ultra, 128GB)" — https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Bolt-24GB/
[2] Hugging Face model card, nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF (release date 10/15/2026) — deployment line "llama.cpp on RTX/DGX Spark (64GB / 128GB) or RTX discrete GPUs (32GB+ / 48GB+); 28GB and 32GB recipes below" — https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF
[3] NVIDIA blog, "Open From Data Center to Desktop: NVIDIA Expands Nemotron Family With Highest Efficiency Super VL and Bolt Models" (2026-10-15) — "Bolt E4B coming Oct. 23", "Built for NVIDIA RTX Spark laptops arriving Oct. 16" — https://blogs.nvidia.com/blog/nemotron-3-5-super-vl
[4] Tom's Hardware, "Nvidia RTX Spark devices are now officially on sale" (2026-10-16) — launch-day listings: ProArt P14 24GB $2,599, Surface Laptop Ultra 48GB $3,999, ProArt P16 64GB from $4,499.99 and 128GB $6,999.99, OmniBook X $5,109 and OmniBook Ultra $5,309 at 128GB/1TB, memory options 24GB–128GB — https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models
[5] MLQ News, "Nvidia's RTX Spark PCs arrive October 16 with up to 128GB of shared memory" (2026-10-16) — Surface Laptop Ultra $2,599.99 (24GB) to $5,899.99 (128GB), full chip from $3,699.99, "total capacity is not equivalent to 128GB of dedicated, high-bandwidth VRAM", "theoretical peak figure using sparsity", 45–80 W — https://mlq.ai/news/nvidias-rtx-spark-pcs-arrive-october-16-with-up-to-128gb-of-shared-memory
[6] Cowcotland weekly graphics-card price tracker, week to 2026-10-16 (published 2026-10-17), as transcribed by Windows Forum — RTX 5090 €5,999.90 to €6,499.90, €4,499.90 on 2026-08-14, "seven climbed in price, nine stood completely still, and zero got cheaper" — https://windowsforum.com/news/rtx-5090-hits-eur6-499-in-france-as-amd-and-nvidia-gpu-prices-surge.448953
[7] bestvaluegpu, "RTX 3090 Price History & Tracker (US)" (prices checked 2026-09-20) — "$1361 used on eBay today. That is 47% above its 12-month average of $927 and 9% below the $1499 launch price"; monthly used averages Dec 2025 $701 to Sep 2026 $1,344 — https://bestvaluegpu.com/history/new-and-used-rtx-3090-price-history-and-specs
[8] TrendForce press release, "AI Server Demand Sustains Memory Contract Price Increases in 4Q26, While Consumer-Side Pressure Persists" (2026-09-30) — conventional DRAM +10–15% QoQ with the pace expected "to moderate"; "These constraints are expected to keep graphics DRAM prices on an upward trajectory" — https://www.trendforce.com/presscenter/news/20260930-13258.html
[9] Bodega One, "How to run NVIDIA Nemotron 3.5 Bolt locally, and whether it really fits in 24 GB" (2026-10-18) — weights 22.02GB, vision encoder 1.73GB, drafter 1.00GB, "All three … 24.75 GB"; "NVIDIA's own recipes start at 28 GB of memory once you add the vision encoder, the speed-up drafter and context" — https://www.bodegaone.ai/blog/run-nemotron-3-5-bolt-locally
