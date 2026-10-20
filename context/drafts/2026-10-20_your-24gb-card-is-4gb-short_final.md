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
image_path: "context/assets/illustrations/your-24gb-card-is-4gb-short/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "NVIDIA's 24Gb Label Trap. Massive array of glowing workstation memory modules towering over a single graphics card inside a"
image_caption: "NVIDIA's 24Gb Label Trap: Why a 24GB model needs a 28GB system to actually run."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Nvidia calls Nemotron 3.5 Bolt its 24-gigabyte (GB) build, but the company's own setup guide requires a 28GB system at minimum [2]. The graphics card the label points to is four gigabytes short of Nvidia's smallest listed recipe. The vendor measured its advertised speed of 84 tokens a second on a laptop holding 128GB of memory, which went on sale the next day for up to $6,999.99 [1, 4].

<!-- tension -->

## The big picture:

The compression work behind this model is real. It is the most interesting thing in local artificial intelligence (AI) this month. Nvidia took its massive Super VL model and squeezed it from 120 billion parameters to 74 billion. Only about 9 billion of those are active for any single word or token [1]. 

Nvidia trained the parts down to roughly two bits per weight, then retrained them to win back accuracy [1]. On Nvidia's own graduate-level science test, it scores 86.43, beating the 83.40 score from competing model Qwen3.6-35B-A3B [1]. 

What did not shrink is the hardware limit. The model card lists separate graphics cards at 32GB, 48GB, and higher. It also lists 28GB and 32GB recipes below that line [2]. 

The research page sets a design goal below 24GB for a single user with a large context window [1]. Both claims can be true only if the 24GB label refers to the model weights alone. 

The larger setup table includes those weights plus extra tools [9]. These include the vision encoder that processes images, the smaller drafter model that speeds up text, and the context window itself [9]. My read: the label is a floor for a simple chat window, and the table is a floor for an automated agent. 

I keep coming back to what this does at the retail shelf. The card those agent recipes actually assume is the 32GB one. In France, that card rose another €500 in the week to 16 October, hitting €6,499.90 [6]. 

That price is up €2,000 since 14 August [6]. It sits on a 16-card tracker where seven cards rose, nine did not move, and zero fell [6]. 

The broader memory market bends the other way. TrendForce reports standard memory contracts are slowing down for the fourth quarter [8]. Meanwhile, graphics memory stays on an upward path because fast memory production is limited [8]. 

The other half of the week involved form factors. Nvidia's Spark laptops went on general sale on 16 October with memory options ranging from 24GB to 128GB [4]. The cheap end is an Asus ProArt P14 with 24GB for $2,599 [4]. 

HP (the computer maker) lists a 128GB OmniBook X with 1 terabyte (TB) of storage at $5,109 [4]. Asus lists a 128GB ProArt P16 with 2TB at $6,999.99 [4]. Microsoft's Surface Laptop Ultra runs from $2,599.99 for 24GB to $5,899.99 for 128GB [5].

## By the numbers

- **28GB — Nvidia's smallest recipe:** The setup table requires 28GB at minimum and lists separate cards starting at 32GB, one step above the 24GB product name [2].
- **€6,499.90 — 32GB on a card:** The tracked French price for the 32GB flagship jumped €500 in a week and €2,000 since 14 August [6].
- **$39.90 to $108 — Cost per gigabyte:** The $5,109 laptop from HP delivers 128GB of memory at $39.90 a gigabyte, while Asus's $2,599 laptop delivers 24GB at $108 a gigabyte [4].
- **+47% — Used 24GB premium:** A 2020-era 24GB card sells for $1,361 on the secondary market, climbing from $701 last December to sit 47% above its yearly average [7].

<!-- tactical-insight -->

## What I'd watch:

The bandwidth question is the one I would want answered first. A shared pool of low-power memory is not 128GB of dedicated video memory. Microsoft's own documents say the share available to the graphics processor depends on the setup and the workload [5]. 

Capacity is cheap in this shape, but bandwidth is what the buyer gives up. Nvidia measured 83.99 tokens a second on a 128GB Surface [1]. That compares to 96.63 for Qwen3.6-35B-A3B and 100.56 for Gemma 4 26B-A4B on the same test setup [1]. 

That is a 13% to 17% speed deficit. Nobody has published a 32GB-card number to compare it with yet. 

The price spread inside one product line is the other thing I am watching. The same 128GB of the same silicon is $5,109 from HP and $6,999.99 from Asus [4]. That costs 37% more for an extra terabyte and a different brand badge [4]. 

A market with no baseline price for a new unit of capacity produces that spread, and my read is that a gap of that size closes once supply settles rather than because anyone re-thinks the price. 

Then there is the secondhand floor, which is the part that surprises me. A 24GB card launched in 2020 is now $1,361 used [7]. That sits 47% above its yearly average and 9% below its original launch price [7]. 

That older card is not in Nvidia's setup table. The table starts at 32GB for separate cards [2]. The people bidding it up are buying memory rather than official support. I would want to know how many of them have actually run a 28GB recipe on one. 

The last signal is the small model. Nvidia ships a 4GB variant of Bolt on 23 October [3]. If the next tier lands under the 28GB limit instead of above it, the whole ladder drops a rung. 

That shift would make this week's card prices look like a peak rather than a floor.

<!-- nuanced-takeaway -->

## The catch

Every benchmark here is Nvidia's own, running on Nvidia's test setup. No outside lab has reproduced any of it yet [1]. The speed comparison pits a laptop against a laptop, and the vendor picked the laptop. 

The shared memory pool deserves the same suspicion in the other direction. It is capacity, not speed, and the share a graphics processor can use varies by machine [5]. 

Nvidia's own "1 petaflop" line is a theoretical peak using sparsity, a trick that skips zero-value math steps [5]. A laptop running a 74-billion-parameter model at 84 tokens a second is not the same claim as a workstation that trains on it. 

My read, held loosely: one week of tracker data and one model launch is a thin base for a rule about how local AI gets bought. The memory limits could just be a launch-week quirk of a massive 256K context window and an early text drafter. 

What makes me doubt that is the used market. Secondary prices surged 47% before any of this software shipped [7].

<!-- tldr -->

## At a glance

- **The Big Shift:** Nvidia shipped a local agent model labelled 24GB whose own setup table starts at 28GB and requires a 32GB or 48GB card, measuring its speed on a 128GB laptop that went on sale the next day.
- **Why It Matters:** The memory that runs the model is now sold in two shapes at very different prices per gigabyte. The card shape is the expensive one at €6,499.90 for 32GB, while $5,109 buys 128GB in a laptop.
- **What I'd Watch:** Three readings would settle whether capacity or bandwidth ends up setting the price of local agent work.
  - **Tokens a second at long context:** The speed number that decides whether a shared pool is usable for agents, which nobody has published for a 32GB card yet.
  - **The spread across brands:** Identical memory capacity listed at $5,109 and $6,999.99 on launch day, a gap that tends to close as supply settles.
  - **The 4GB variant:** Nvidia's small Bolt ships on 23 October and could move the software floor below the hardware one.
- **The Catch:** The benchmarks are the vendor's own, the shared pool uses slower memory than a dedicated card, and one week of retail tracking is not a trend.

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

## Gate report
lead
PASS — Delivers the core discrepancy immediately in under 28 words for the first sentence, defines GB upfront, and strips out all throat-clearing.
tension
PASS — Breaks monolithic text into tight 1-3 sentence paragraphs, expands HP and TB, translates jargon clearly, and boosts Flesch readability.
tactical-insight
PASS — Uses strict 1-3 sentence paragraphs, maintains observational voice ("What I'd watch"), and cleanly outlines bandwidth trade-offs and price spreads.
nuanced-takeaway
PASS — Defines technical concepts like sparsity simply, keeps paragraphs exceptionally brief, and directly addresses vendor benchmark limitations.
tldr
PASS — Strictly adheres to the 4-part Smart Brevity bulleted schema, distinctively summarizing the big shift, why it matters, what to watch, and the catch.
