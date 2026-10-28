---
title: "480GB Won't Skip Your Memory Queue"
vertical: gpu_hardware
persona: infra_engineer
one_big_thing: "Intel's capacity-first D270 trades bandwidth for memory capacity and a 350-watt air-cooled slot, but it does not step outside the memory shortage: the low-power memory it substitutes is a high-value line the same suppliers are now contracting, so the card's case rests on prompt-heavy traffic and a tight power budget rather than on cheaper bytes."
date: 2026-10-28
slug: your-480gb-card-wont-skip-the-memory-queue
synthesis: true
sources:
  - https://www.intel.com/content/www/us/en/products/details/discrete-gpus/data-center-gpu/d-series.html
  - https://news.skhynix.com/en/q3-2026-business-results
---

<!-- lead -->
Intel's new inference card is advertised with 480 GB (gigabytes) of memory and no high bandwidth memory (HBM) at all, and it won't skip your memory queue [1]. The D270 was announced in October after Intel decided the limit had moved off bandwidth and onto capacity, for long prompts and many sessions at once [1]. Its headline numbers are memory and watts: 480 GB on partner cards, 350 watts, air cooling, a standard PCIe slot [1][2]. Sixteen days later the memory maker (SK hynix) reported an 80% operating margin, and said more than half of its 2027 and 2028 output is already sold [3].

<!-- tension -->

## The big picture:

I've been reading these two documents side by side all week, because each looks ordinary alone and the pair does not. Intel's page argues the bottleneck has moved: agents read far more than they write, long prompts dominate, and the card keeps more of a model resident, "for richer reasoning with fewer GPUs and no high bandwidth memory (HBM)" [1]. It says nothing about where the memory comes from. The memory maker's quarter says what HBM has become: the main product from this quarter, more than half of the next two years' output signed on deals that run "typically five years", at a margin of 80% [3].

Put the two together and the swap changes shape. The low-power memory Intel's card leans on is not outside the queue, because the same release that lifts HBM4 output also plans to sell more server memory for AI systems, as part of a range built on high-value parts [3]. A buyer is not choosing between a dear memory market and a cheap one. A buyer is choosing which queue to stand in, and the queue this card shortens is the one for HBM stacks, not the one for memory wafers.

Price direction points the same way, though it is not the whole case. TrendForce expects standard dynamic random access memory (DRAM) contract prices to rise 10 to 15% this quarter, with server DRAM still short and graphics DRAM "on an upward trajectory" [4]. Nothing on that list is falling. So the reason to buy capacity in a standard slot is not a lower memory bill. It is what a bigger card does to where models sit, and what it does to the rack.

## By the numbers

- **480 GB — Partner-card ceiling:** Intel's own card carries 160 GB from twenty 8 GB chips; partner cards reach 480 GB using 24 GB chips, on a 1,280-bit path at 1.5 terabytes a second [2].
- **1.5 against 3.6 to 4 terabytes a second — Bandwidth given up:** AMD (the chip designer) runs HBM3E in its MI350P at about 3.6 to 4 terabytes a second, and NVIDIA (the card maker) pairs 96 GB of GDDR7 with 1.6 to 1.8 terabytes a second [2].
- **80% — Memory maker's margin:** on revenue of 104.6155 trillion won and operating profit of 83.3338 trillion won, with HBM4 set to pass HBM3E in volume and revenue this quarter [3].
- **10 to 15% — Memory prices:** the expected rise in standard DRAM contract prices this quarter, with flash memory up 15 to 20% and server DRAM still short [4].

<!-- tactical-insight -->

## What I'd watch:

The first thing I would measure is how much of the work is prompt processing and how much is output. Prompt processing builds the cache and leans on compute, while output leans on memory bandwidth, which is why the two phases fail in different ways. Intel built the card around the first and says so, presenting speculative decoding that retires 2.9 to 4.9 tokens per check [2].

A firmware unlock published this month shows the same split from the other end. Doubling the half-precision math issue rate on consumer cards lifted prompt processing by 14 to 36% and left output, "which is limited by memory bandwidth", about the same [5]. More compute does not fix a bandwidth wall. Neither does more memory.

- **Prompt share:** if most of the clock goes on prompts and cache building, capacity is the lever, and a 1.5-terabyte card can be the cheaper way to hold a large model [2].
- **Placement:** a 480 GB partner card holds weights that would otherwise be split across several cards, which cuts traffic between them [2].
- **Watts and air:** 350 watts with passive cooling fits racks that cannot take a liquid retrofit, and that decides more rollouts than a bandwidth table does [1][2]; the cap-tuning arithmetic in [Why Your 80% Cap Wins](/cap-your-card-at-80/) is the other half of that budget.
- **The next supply deal:** whether low-power server memory joins HBM in the sold-ahead category, which its maker now lists among its high-value lines [3].

<!-- nuanced-takeaway -->

## The catch

The card is not on sale. Intel is sampling it, with no price and no ship date, and the analyst house that tore it down expects volume early in 2027 [2]. Its costs are also openly tied to the memory market, because the same analysis says low-power memory prices have been unstable and that "the economics of the 480GB configuration depend heavily on DRAM pricing" [2]. Intel's record in this market is a further reason to wait, since two earlier programmes were cancelled or pulled [2].

My read, held loosely, is that the honest claim is narrower than the launch. The D270 does not cut the memory bill, because no price has been published for the card or its memory, and every memory type TrendForce tracks is rising [2][4]. It turns a bandwidth budget into a capacity and power budget, which suits long-prompt agent work on air-cooled racks and fits badly anything whose users sit waiting on output tokens.

<!-- tldr -->

## At a glance

- **The Big Shift:** Intel's D270 sells memory capacity instead of bandwidth, up to 480 GB of low-power memory on partner cards in a 350-watt slot, and markets the result as inference without HBM [1][2].
- **Why It Matters:** The HBM it avoids is now a sold-ahead product, with more than half of the supplier's 2027 and 2028 output signed and an 80% margin on the quarter, so the swap changes which queue a buyer joins rather than what memory costs [3].
- **What I'd Watch:** How much of the workload is prompt processing, and whether the rack can take the power.
  - **Prompt share:** the time spent reading prompts and building the cache, where extra compute and extra capacity both help [2][5].
  - **Output speed:** the time spent producing tokens, set by memory bandwidth, where this card trails HBM parts by well over half [2].
  - **Supply terms:** whether low-power server memory gets contracted the way HBM now is, which decides whether the cheaper option stays available [3].
- **The Catch:** No price, no ship date, sampling only, a cost case the analyst says depends heavily on DRAM pricing, and software coverage in vLLM and SGLang that still trails the incumbent stack [2].

## Sources

[1] Intel, "Intel GPU D270 — Inference-Optimized Data Center GPU," product page, D-Series announced at the Open Compute Project summit, 12 October 2026. https://www.intel.com/content/www/us/en/products/details/discrete-gpus/data-center-gpu/d-series.html
[2] Steve McDowell, "Intel GPU D270: An Inference-First GPU for the Data Center," NAND Research, 15 October 2026. https://nand-research.com/intel-gpu-d270-an-inference-first-gpu-for-the-data-center
[3] SK hynix, "SK hynix Announces 3Q26 Financial Results," press release, 28 October 2026. https://news.skhynix.com/en/q3-2026-business-results
[4] TrendForce, "AI Server Demand Sustains Memory Contract Price Increases in 4Q26, While Consumer-Side Pressure Persists," press release, 30 September 2026. https://www.trendforce.com/presscenter/news/20260930-13258.html
[5] Zagitta, "GPU unlock 1.0.0 — unlock FP/BF16 instruction issue rate on NVIDIA 3000-series cards," GitHub repository, read 24 October 2026. https://github.com/Zagitta/gpu-unlock
