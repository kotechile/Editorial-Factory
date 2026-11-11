---
title: 8-Hi HBM Costs More per Gigabit
vertical: gpu_hardware
kind: news
persona: infra_engineer
one_big_thing: "Samsung has already sold its 2027 high bandwidth memory at an agreed price, and the shorter 8-Hi stack costs 10-20% more per gigabit than the one it replaces, so the only lever left on a 2027 budget is to need less memory rather than to buy it cheaper."
date: 2026-11-11
slug: 8-hi-hbm-costs-more-per-gigabit
synthesis: true
sources:
  - https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q3-2026-profit-93CH-4981365
  - https://arxiv.org/abs/2611.11036
---

<!-- lead -->
Samsung has already sold its 2027 high bandwidth memory (HBM) at a price agreed with customers. Because the shorter 8-Hi stack carries fewer memory dies over the same base layer, it costs 10–20% more per gigabit than the 12-Hi stack it replaces. That flips the usual move in a shortage. A smaller stack now buys fewer bits for each dollar, so a 2027 budget has one lever left: need less memory.

<!-- tldr -->

## At a glance

- **The shift:** 2027 HBM is sold at an agreed price, and the shorter stack costs more per bit.
- **The number:** 8-Hi runs 10–20% dearer per gigabit than 12-Hi next year.
- **The risk:** The one cheaper tier only pays on paused traffic.

<!-- tension -->

## Signed Before It Was Measured

I keep coming back to the order these three dates fall in. On 20 October, TrendForce said fourth-quarter conventional dynamic random access memory (DRAM) prices would rise about 20% from the prior quarter. The same note put 8-Hi HBM 10–20% above 12-Hi per gigabit in 2027 [2]. Nine days later, on Samsung's third-quarter call, memory executive Jaejune Kim said the 2027 HBM supply volume was already sold at an agreed target price, with customers still asking for more [1]. A second Korean outlet reported that line the same day, in the same words [4]. On 8 November, a team at the University of California, Merced published the first broad cost test of the tier that would let a buyer need less of it [3].

The 8-Hi premium comes from how the stack is built, not from pricing strategy. Either stack needs one base die, the logic layer that talks to the processor, and 8-Hi carries fewer memory dies above it. Spread that fixed cost over less room and the price per gigabit rises, even though each stack is cheaper. Card makers want the shorter stack because the same bit output then supports more accelerators. Buyers get a smaller bill per socket and a worse price per bit, in the same order.

The substitute has been simulated now, not just asserted. High bandwidth flash (HBF) stacks flash chips so they behave like memory instead of storage. Across 62,279 replays, it cut the minimum card count in 98 of the 224 cases where the standard layout also met the target and needed more than one card [3]. Sixty-three of those 98 stayed cheaper when an HBF stack cost half a card. That half-a-card figure is the authors' test price, not a quote from a supplier [3].

## By the numbers

- **10–20% per gigabit:** The 2027 premium TrendForce expects for 8-Hi over 12-Hi HBM, because both need one base die [2].
- **32 cards:** What Qwen3-235B needed for four short-chat users before cascaded flash cut it to four [3].
- **None of 108:** The tool-session cases where flash saved cards, against 40 of 108 paused-session ones [3].

<!-- tactical-insight -->

## What I'd Watch

The split by workload is the part I keep circling, because it cuts against how fleets are usually sized. Flash saved cards in 40 of 108 paused-session cases and 39 of 108 short-chat cases, 17 of 108 long-retrieval cases and none of 108 tool-session cases [3]. Paused sessions are the shape agent traffic takes: someone stops, comes back, and reuses the same opening. Long retrieval and tool loops, the two patterns that most often force a second card onto one model, get nothing. The memory queue is not one queue, as [480GB won't skip your memory queue](/your-480gb-card-wont-skip-the-memory-queue/) argued last month, and the tier that helps depends on which queue your traffic stands in.

What I'd want to know before a 2027 contract closes is the share of sessions that pause, and the share that run long. An operator serving interactive assistants has a case for tiering cold weights. One running batch retrieval has almost none, and is better served by paying the HBM price and shrinking the model. I'm also watching for any vendor to publish an 8-Hi contract price, because that single number decides whether the premium is a forecast or a bill.

<!-- nuanced-takeaway -->

## The Catch

The flash result is a simulation, and its authors say so: the outputs are projections, not measurements of a working system [3]. Their own sensitivity audit is the honest part. A sensitivity audit ran fourteen reference wins through nine settings in link speed, service time and overhead, and only two survived all nine [3]. That is not a case for buying flash. It is a case for not assuming the cheaper tier arrives in time to matter.

Samsung disclosed almost nothing beyond that one sentence about 2027. It gave no volume, no price level and no customers, so the agreed price for that year is all the public record holds [1]. My reading, held loosely, is that the price is fixed, the short stack is not cheap per bit, and the case for a cheaper tier is real but narrow. Capacity sized on a fleet average will be the wrong size for most of the fleets that buy it.

## Sources

- [1] Samsung Electronics, "3Q 2026 earnings call transcript" (Memory EVP Jaejune Kim, HBM Q&A), 29 October 2026 — https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q3-2026-profit-93CH-4981365
- [2] TrendForce, "DRAM Prices Seen Rising 20% QoQ in 4Q26 Despite Slower Gains; AI Demand, Tight Supply Support Outlook," 20 October 2026 — https://www.trendforce.com/news/2026/10/20/news-dram-prices-seen-rising-20-qoq-in-4q26-despite-slower-gains-ai-demand-tight-supply-support-outlook
- [3] Zhiyu An, Yiping Li and Wan Du, "When Is High-Bandwidth Flash Cost-Effective for LLM Inference?", arXiv:2611.11036, 8 November 2026 — https://arxiv.org/abs/2611.11036
- [4] Chosun Biz, "Samsung Electronics triples 3Q HBM4 sales, locks in 2027 supply," 29 October 2026 — https://biz.chosun.com/en/en-it/2026/10/29/IAJCD425DFFEPB6NZHYAUYGLQY
