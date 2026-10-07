---
title: "Local AI Payback: Your Rig Just Tripled as Cloud GPUs Split Three Ways"
vertical: workstation_compute_economics
persona: infra_engineer
one_big_thing: "The build-vs-rent break-even for AI compute stopped being one number in September 2026: local hardware repriced up on the memory crunch while the cloud GPU price split into a roughly three-times provider spread, so any payback figure is only honest if it names the cloud row it used."
date: 2026-10-06
slug: local-ai-payback-cloud-gpu-spread
synthesis: true
sources:
  - https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-5090-vanishes-from-online-retail-in-the-us-third-party-sellers-now-demand-as-much-as-usd9-500-for-nvidias-fastest-gpu
  - https://getdeploying.com/gpu-price-trends
meta_title: "Local AI Payback: Your Rig Just Tripled as Cloud GPUs Split…"
meta_title_source: "derived_from_title"
meta_description: "The graphics processing unit (GPU) that local artificial intelligence (AI) teams actually buy just shot up in price."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/local-ai-payback-cloud-gpu-spread/featured.jpg"
image_style: "studio_object"
image_model: "flux"
image_alt: "Massive workstation graphics processing unit with heavy cooling fins resting on a dark surface."
image_caption: "The memory shortage has pushed local AI compute hardware into a rare luxury tier."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
The graphics processing unit (GPU) that local artificial intelligence (AI) teams actually buy just shot up in price. In the first two weeks of September, Nvidia's 5090 card vanished from normal United States (US) online stores. Now, outside sellers want $6,500 to $9,500 for a card that launched at $1,999 [1]. At the exact same time, the cloud H100 chip you might rent instead cost a median of $3.39 an hour, but the big cloud giants charged $7.89 for that exact same chip [4].

<!-- tension -->

## The big picture:

The choice to build or rent AI power just broke on both sides. A shared memory squeeze caused both shifts.

For hardware, dynamic random-access memory (DRAM) costs are jumping. Micron's boss told investors on September 30 that DRAM prices rose nearly 20% last quarter. He warned that supply will get much tighter in 2027 and 2028 [2].

TrendForce expects standard DRAM prices to climb another 10% to 15% this quarter [3]. The Nvidia 5090 uses 32 gigabytes of fast memory. When that memory gets rare, the cards get rare too.

On the cloud side, the going rate for a GPU split apart. Across 41 providers, the median on-demand H100 chip rents for $3.39 an hour [4]. Yet the biggest cloud giants charge about 105% more than smaller GPU clouds for that exact same card, asking $7.89 instead of $3.85 [4].

For an H200 chip, that gap hits 141% [4]. A separate check on September 18 found the same H100 class spanning $1.99 to roughly $6 an hour. The report noted a three-times spread is now normal [5].

My read: Cloud rentals offer no easy escape from local hardware costs. The big cloud hosts face the exact same supply limits. 

The real escape hatch sits at the cheap end of the rental market. Teams never see those cheap rates if they only look at Amazon or Google.

## By the numbers

- **$6,395 to $9,500 — Nvidia 5090 street price:** Outside sellers demand huge markups over the $1,999 launch price. The June median was $4,299 [1].
- **105% — Big cloud H100 premium:** Amazon, Azure, and Google Cloud charge $7.89 an hour. Dedicated GPU clouds charge just $3.85 [4].
- **$1.99 to ~$6 — The H100 spread:** The hourly price range for the exact same chip across seven providers on September 18 [5].
- **2028 — Micron's supply horizon:** The memory maker expects tighter conditions through 2028. Buyers have already claimed over 75% of 2027 output [2].

<!-- tactical-insight -->

## What I'd watch:

Tech teams are checking their costs again. I keep coming back to which cloud price they use in their math.

- **The denominator problem:** A math model using a $7.89 big-cloud rate says to buy local hardware. The same math using a $1.99 cheap rate says to keep renting [4][5]. The hardware stays the same, but the benchmark changes the answer.
- **The commitment ladder:** Booking ahead saves about 28% for a year and 49% for three years. Short-term spot pricing cuts the cost in half [4]. These discounts change the final choice more than swapping GPU models.
- **The egress line:** Two providers can charge the same hourly rate but differ by five figures a year. Moving data out and storing it idle costs extra [5]. I want to see operators map those fees before picking a winner.
- **The memory clock:** Micron says relief will not arrive before 2028. TrendForce sees prices rising again this quarter [2][3]. Anyone treating this fall's GPU prices as a short blip is betting against both major suppliers.

<!-- nuanced-takeaway -->

## The catch

I could be wrong to see a deep market flaw where others just see a retail shortage. The 5090 price spike is partly about scalpers. Tom's Hardware notes the surviving listings are all outside sellers, and one local Micro Center store still had cards near $4,299 [1]. 

That points to a store supply issue rather than pure chip costs. The honest catch is that these two trends run on different clocks. GPU street prices can drop the moment retail stock returns. 

But the memory prices Micron and TrendForce track sit inside long-term deals that will not budge [2][3].

The part I keep circling is the "months to payback" metric. It is only as good as the cloud rate behind it. That rate now varies by a factor of three for the exact same chip. 

The choice did not get harder because the hardware got worse. It got harder because the baseline price split apart.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Ebike Costs: Per-Use Calculator for Commuters" -> https://giniloh.com/ebike-costs-per-use-calculator-for-commuters/ [same site (giniloh.com); same category; topical overlap: intelligence, price] Link "Ebike Costs: Per-Use Calculator for Commuters" in the section where the article touches intelligence, price. -->
<!-- internal-link hint: "NVIDIA RTX PRO: Groundbreaking Performance, But Does the Math…" -> https://giniloh.com/nvidia-rtx-pro-groundbreaking-performance-but-does-the-math-check/ [same site (giniloh.com); same category; topical overlap: cloud, gpus] Link "NVIDIA RTX PRO: Groundbreaking Performance, But Does the Math…" in the section where the article touches cloud, gpus. -->
<!-- internal-link hint: "Self-Hosted AI: When to Buy vs Rent GPUs" -> https://giniloh.com/self-hosted-ai-when-to-buy-vs-rent-gpus/ [same site (giniloh.com); same category; topical overlap: cloud, gpus] Link "Self-Hosted AI: When to Buy vs Rent GPUs" in the section where the article touches cloud, gpus. -->
## Related reading

- [Ebike Costs: Per-Use Calculator for Commuters](https://giniloh.com/ebike-costs-per-use-calculator-for-commuters/) — more on Major Purchases & Assets
- [NVIDIA RTX PRO: Groundbreaking Performance, But Does the Math…](https://giniloh.com/nvidia-rtx-pro-groundbreaking-performance-but-does-the-math-check/) — more on Major Purchases & Assets
- [Self-Hosted AI: When to Buy vs Rent GPUs](https://giniloh.com/self-hosted-ai-when-to-buy-vs-rent-gpus/) — more on Major Purchases & Assets
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** The 5090 GPU that local AI builders buy now costs roughly three times its launch price. Meanwhile, the competing cloud H100 chip split into a $3.39 median and a $7.89 premium rate.
- **Why It Matters:** The choice to build or rent now hinges entirely on which cloud host you check. The same hardware looks like a steal or a waste based on one hidden choice.
- **What I'd Watch:**
  - **The denominator:** Which cloud rate anchors the math model — a premium giant or a cheaper dedicated tier.
  - **The commitment ladder:** Long-term deals and spot discounts that shift the final math far more than a simple chip swap.
  - **The egress bill:** Providers matching on hourly rates but charging five figures more a year to move data.
- **The Catch:** The 5090 spike is partly a short-term store and scalper issue. But cloud rental rates are still up 14% over the year, meaning cheap space exists, but it is not getting cheaper.

## Sources
[1] Tom's Hardware, "Nvidia's RTX 5090 vanishes from online retail in the US — third-party sellers now demand as much as $9,500" (2026-09-14). https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-5090-vanishes-from-online-retail-in-the-us-third-party-sellers-now-demand-as-much-as-usd9-500-for-nvidias-fastest-gpu
[2] CIO, "Memory squeeze set to tighten through 2028, Micron says" (2026-10-01). https://www.cio.com/article/4229625/memory-squeeze-set-to-tighten-through-2028-micron-says.html
[3] TrendForce, "AI Server Demand Sustains Memory Contract Price Increases in 4Q26" (2026-09-30). https://www.trendforce.com/presscenter/news/20260930-13258.html
[4] getdeploying.com, "GPU Price Trends (2026)" (week of 2026-09-28). https://getdeploying.com/gpu-price-trends
[5] Deepak Gupta, "Top 7 GPU Cloud and AI Compute Providers 2026" (2026-09-18). https://guptadeepak.com/tools/top-7-gpu-cloud-ai-compute-providers-2026

<!-- linkedin -->
I've been watching the price of the GPU that local-AI teams actually buy, and the number that stopped me was the cloud row next to it.

In the first two weeks of September, Nvidia's 5090 card almost completely vanished from US online stores. What's left sells on outside marketplaces for $6,395 to $9,500, against a $1,999 launch price. The cause is memory: Micron's chief said on September 30 that supply will be tighter in 2027 and 2028 than in 2026.

Here's what I keep coming back to. The cloud H100 chip you might rent instead cost a median of $3.39 an hour in the same two weeks. But the big cloud giants charge about 105% more than smaller GPU clouds for the identical card: $7.89 versus $3.85. One check found the same class of H100 spanning $1.99 to about $6 an hour and called a three-times spread "normal."

My read: the build-versus-rent choice isn't one number anymore. A payback figure using the Amazon rate says buy locally. The same figure using a cheap neocloud rate says keep renting. The hardware didn't change — the benchmark did.

What I'm watching next is whether teams start naming the exact cloud rate behind their payback slide. Curious whether others are re-running their models against the cheaper rows.

## Gate report
lead: PASS — Direct, punchy first sentence delivering the core news without preamble.
tension: PASS — Explains the memory squeeze and cloud price split clearly; includes required observer cue.
tactical-insight: PASS — Formatted correctly with bold lead-ins; focuses on observations, not commands; includes observer cue.
nuanced-takeaway: PASS — Presents the scalping caveat and differing timelines; includes observer cues.
tldr: PASS — Follows the exact 4-part Smart Brevity schema with proper spacing and sub-bullets.
