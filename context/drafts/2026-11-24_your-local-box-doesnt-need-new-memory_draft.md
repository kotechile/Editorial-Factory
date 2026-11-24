---
title: "Your Local Box Doesn't Need New Memory"
subtitle: "OpenAI's CEO says home machines hoard scarce DRAM. The cheapest rig of the month runs on memory nobody will ever allocate again."
slug: your-local-box-doesnt-need-new-memory
kind: news
synthesis: true
vertical: workstation_compute_economics
persona: infra_engineer
date: 2026-11-24
primary_keyword: local inference DRAM
sources:
  - https://www.techpowerup.com/354346/openai-ceo-argues-home-pcs-waste-the-worlds-limited-dram-supply
  - https://www.tomshardware.com/tech-industry/artificial-intelligence/three-e-waste-nvidia-v100s-hit-100-tokens-per-second-on-qwen-3-6-35b-in-a-usd1-042-homelab-rig-decommissioned-gpus-outpace-a-usd5-399-m5-max-mac-studio-at-long-contexts
---

<!-- lead -->
Your local box doesn't need new memory. OpenAI's Sam Altman told Stripe co-founder John Collison this month that it is "quite terrible" for people to hold "the world's limited supply of DRAM sitting in their own computer" at 5% utilization [1]. Nine days after that episode aired, a hardware writer measured the strongest counter-case on record: three decommissioned Nvidia V100 cards in a $1,042 used-server rig ran Qwen 3.6 35B at 100 tokens per second, out-pacing a $5,399 Mac Studio at long context lengths [2]. Both statements are about the same scarce resource, and they disagree about what counts as using it.

<!-- tldr -->
## At a glance
The fight over local inference is really a fight over DRAM allocation, and both sides price it wrong. This matters to anyone deciding whether the workstation on their desk is waste or capital.

<!-- tension -->
## The argument arrives at the worst moment
Altman's claim came on the Cheeky Pint podcast on October 29 [1]. His arithmetic: a home machine's memory idles most of the day, so in a supply-constrained market that silicon belongs in cloud servers running "maximum utilization" [1]. The same report carries the demand side of that argument — OpenAI's Stargate memory need was projected at up to 900,000 DRAM wafers a month, around 40% of global output, and Dell's chief executive expects the shortage to worsen in 2027 [1]. People who run home AI do it for privacy and for skipping a subscription, the report notes, not for efficiency [1].

What I find hard to square is the hidden denominator. The allocation argument, and the street prices that back it, price local inference in newly manufactured memory. Tom's price index put the cheapest RTX 5090 at $6,919 against a $1,999 launch — about $216 per gigabyte of VRAM versus $62 at launch — and Nvidia pulled the RTX 5080 from its own store, the cheapest in-stock card at 2.2 times its MSRP [3][4]. That is the cost of memory that competes with Stargate for wafers.

The V100 rig's memory does not. Those cards were manufactured years ago, scrapped by the data centers that retired them, and bought secondhand — they draw on no wafer anyone is bidding for [2]. The rig itself cost $1,042, board and CPUs included [2].

## By the numbers
- **100.8 tokens per second:** Qwen 3.6 35B throughput from three used V100s at 4K context, falling to 72.7 at 128K [2].
- **$1,042:** the whole rig — board, two Xeons, three cards — against a $5,399 M5 Max Mac Studio [2].
- **40% of global output:** OpenAI's projected Stargate DRAM demand, up to 900,000 wafers a month [1].

<!-- tactical-insight -->
## Where the measurement bites
The benchmark's own table is more honest than the argument it answers. At 4K context the Mac Studio is effectively tied — 105.5 tokens per second against the rig's 105.4 on the cheaper quantization — and the e-waste rig only pulls ahead as context grows, where the Mac falls to 61.3 and the V100s hold 72.7 to 77.1 [2]. The builder daily-drives Qwen 3.6 35B on the box, across more than 130 llama.cpp test configurations on nine builds, and warns that scaling decommissioned cards "will only get you so far" [2].

Buyers close to this market are already pricing it per gigabyte rather than per generation. A used-workstation reseller's late-October guide put a 48 GB RTX A6000 at about $92 to $94 per gigabyte against $122.50 per gigabyte for a new RTX PRO 4000 Blackwell — old Ampere VRAM now costs less per byte of capacity than the current generation, even after used prices themselves rose 9% to 24% through October [5]. That ratio is the arbitrage the allocation argument never prices: the token-second you buy on scrap silicon competes with the wafer demand of nobody.

A related way to see it is already on this site: [the price of a GPU-hour is now set by memory rather than compute](/gpu-hour-price-set-by-memory/) [6]. Altman's argument extends that logic one step and missteps — it treats every gigabyte as if it were queued behind next month's wafer allocation, when a decommissioned gigabyte is not in that queue at all.

<!-- nuanced-takeaway -->
## The catch
The strongest version of Altman's point survives, and it deserves stating: a home box that idles 95% of the time is genuinely poor utilization, whoever owns the memory [1]. What the argument cannot do is claim that local inference consumes scarce supply — the measured local winner runs on VRAM that had already been written off, and per dollar of throughput it lands near 5 times the flagship Mac's rate [2]. The honest audit is not "home memory versus the cloud" but "new memory versus dead memory," and the second pool has been growing for a decade of datacenter refreshes. It also carries real limits: the builder himself caps how far decommissioned scaling reaches, power draw and platform quirks ride along free of charge, and nobody is manufacturing more V100s. The rig is an inventory play, and inventory runs out.

## Sources
- [1] Ben Lyons, "OpenAI CEO Argues Home PCs Waste the World's Limited DRAM Supply" — https://www.techpowerup.com/354346/openai-ceo-argues-home-pcs-waste-the-worlds-limited-dram-supply
- [2] Shane Downing, "Three 'e-waste' Nvidia V100s hit 100 tokens per second on Qwen 3.6 35B in a $1,042 homelab rig" — https://www.tomshardware.com/tech-industry/artificial-intelligence/three-e-waste-nvidia-v100s-hit-100-tokens-per-second-on-qwen-3-6-35b-in-a-usd1-042-homelab-rig-decommissioned-gpus-outpace-a-usd5-399-m5-max-mac-studio-at-long-contexts
- [3] Avi Pinto, "RTX 5090 for Local LLMs: Speed, Dual Cards, 5090 vs 4090" — https://vdf.ai/blog/rtx-5090-local-llm
- [4] Zhiye Liu, "Nvidia store quietly pulls the RTX 5080 following RTX 5090 removal" — https://www.tomshardware.com/pc-components/gpus/nvidia-store-quietly-pulls-the-rtx-5080-following-rtx-5090-removal-street-prices-climb-to-2-2x-over-msrp
- [5] Konstantin Protasov, "GPU Price Increase 2026: Why, and When Will Prices Drop?" — https://pcserverandparts.com/news/gpu-price-increase-2026
- [6] Editorial desk, "The Price of a GPU-Hour Is Now Set by Memory, Not Compute" — https://aichieve.net/gpu-hour-price-set-by-memory/
