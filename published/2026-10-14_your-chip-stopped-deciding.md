---
title: "1.016M Non-GPUs: Your Chip Stopped Deciding"
vertical: gpu_hardware
persona: infra_engineer
one_big_thing: "When the accelerator stops being the differentiator, the layer that decides how much of it you actually get to use becomes the product — which is why the vendor that sells the chips moved its own scheduler, GPU-fractioning operator and quota layer into open source the same week IDC's data showed specialised chips out-shipping general-purpose ones for the first time."
date: 2026-10-14
slug: your-chip-stopped-deciding
synthesis: true
sources:
  - https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/
  - https://www.reuters.com/business/retail-consumer/nvidias-china-ai-chip-share-falls-huawei-closes-gap-report-finds-2026-10-13
meta_title: "1.016M Non-GPUs: Your Chip Stopped Deciding"
meta_title_source: "derived_from_title"
meta_description: "Non-GPUs overtook GPUs in China for the first time in the first half of 2026: 1.016 million chips built for specific jobs against 991,000 graphics processing…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-chip-stopped-deciding/featured.jpg"
image_style: "studio_object"
image_model: "flux"
image_alt: "The GPU Scheduling War. A heavy compute blade partitioned by illuminated amber acrylic dividers on a dark stone surface."
image_caption: "The GPU Scheduling War: Why the fight for AI capacity moved off the single chip."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Non-GPUs overtook GPUs in China for the first time in the first half of 2026: 1.016 million chips built for specific jobs against 991,000 graphics processing units (GPUs) [1]. Nvidia shipped 678,000 accelerators there, down 44%, and its share fell to 34% [1]. The same day, 13 October, Nvidia put the software that decides how hard those chips work into open source, and handed the scheduler project to the Cloud Native Computing Foundation (CNCF) [2]. The chip stopped deciding. The layer above it now sets your cost per token.

<!-- tension -->

## The big picture:

The fight for AI capacity just moved off the single chip. The line I keep coming back to is the one IDC (the market research firm) attached to its own shipment table: competition "was shifting from the performance of a single chip to system-level capabilities, including how well chips work in a larger computing cluster" [1].

Nvidia's code drop backs it up [2]. Giving Run:ai away opened up a tool that splits one physical GPU into smaller slices, so several jobs can share a single card [2]. It also adds a quota system for team access [2]. Eight named cloud partners are already integrating it [2].

If the real edge is how well parts work together, then the software setting your limits is not plumbing. It sets your cost per token.

For ten years, buyers picked a part number, an hourly rate, and a memory size. A free, open scheduler that runs anyone's code gives them a reason to keep buying Nvidia chips instead of settling into a cloud vendor's custom hardware.

## By the numbers

- **1.016M vs 991K — The crossover:** Custom AI chips jumped nearly 80% in a year, while GPU shipments dropped 26% [1]. That gave custom chips a 25,000-unit lead in China [1].
- **34% — Nvidia's shrinking share:** Nvidia shipped 678,000 chips from January through June, a 44% drop [1]. Huawei closed the gap, shipping 572,000 units to claim 28% of the market [1].
- **95% — The custom lock:** Four local makers — Huawei, T-Head, Kunlunxin, and Cambricon — hold 95% of the custom chip market [1].
- **19% vs −9% — The split forecast:** IDC expects all AI chip shipments to China to grow 19% this year, even as GPU shipments fall 9% [1].

<!-- tactical-insight -->

## What I'd watch:

My read: vendors know the hardware race is cooling down, so they are pricing the software layer above it instead.

- **Open scheduling as a test:** Nvidia released its tool under a free Apache 2.0 license as a CNCF sandbox project [2]. Teams can now manage bare hardware using public tools instead of a single vendor's closed map [2].
- **Splitting cards to save cash:** The new open tool lets multiple jobs share a slice of one GPU [2]. For teams with low use rates at night, slicing a card is much cheaper than buying a new one. Nvidia used this same logic for memory this month, shipping a tool that shares a set cache budget across layers [6].
- **Metering as the new lock-in:** Saturn Cloud is already turning this open platform into a service that bills per token [2]. Whoever counts the tokens controls the profit margins.
- **The fabric bill:** The physical network cables are the real limit now. New research models a light-based, circuit-switched network for split serving that matches fast 400-gigabit packet fabrics with adaptive routing at 0.55 to 0.78 times the cost of a 2:1 fabric [4]. The chip is an input; the network layout is the product.

<!-- nuanced-takeaway -->

## The catch

A hardware flip in one country does not mean a global shift.

IDC's 34% figure does not say exactly which parts it counted, nor does it track smuggled high-end boards [1]. Nine out of eleven tracked Chinese vendors saw growth [1]. That is exactly what a blocked home market should look like.

The custom bucket is also broad, covering chips built for specific jobs such as running already-trained models [1]. For most engineers outside China, the server rack has not changed.

The open code is not a total giveaway, either. The free version lacks vendor support and paid plans [2]. Nvidia still sells the fully backed enterprise product through its own channels [2].

I would not read too much into the timing. Nvidia never ties its software drop to the shipment data. Two events on the same day can be a coincidence, not a cause.

The strongest pushback comes from Nvidia itself. On 1 October, the company argued that A100 chips shipped in 2020 are still earning money six years later [3]. CoreWeave has booked those older units out to 2029 [3]. Nvidia's post also cites one analysis putting useful life at five to six years for an eight-GPU H100 system, and nine to ten for its newer racks [3]. Another finds a six-year-old A100 still worth a quarter of what it cost, where a five-year schedule had it at zero [3].

Supply is not getting easier either. Memory contract prices are still climbing into the fourth quarter, and server memory stays short [5].

If a single chip keeps making cash for a decade, buying more of them stays a safe bet. The software that squeezes every drop of value out of that decade simply matters more.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Local AI Payback: Your Rig Just Tripled as Cloud GPUs Split…" -> https://giniloh.com/local-ai-payback-cloud-gpu-spread/ [same site (giniloh.com); same category; topical overlap: gpus, graphics, processing] Link "Local AI Payback: Your Rig Just Tripled as Cloud GPUs Split…" in the section where the article touches gpus, graphics, processing. -->
<!-- internal-link hint: "Your 32GB Card, Gone" -> https://giniloh.com/your-32gb-card-gone/ [same site (giniloh.com); same category; topical overlap: graphics, stopped] Link "Your 32GB Card, Gone" in the section where the article touches graphics, stopped. -->
<!-- internal-link hint: "Your GPU Runs Out of Cache Before It Runs Out of Math" -> https://giniloh.com/kv-cache-is-the-concurrency-ceiling/ [same site (giniloh.com); same category; topical overlap: graphics, processing] Link "Your GPU Runs Out of Cache Before It Runs Out of Math" in the section where the article touches graphics, processing. -->
## Related reading

- [Local AI Payback: Your Rig Just Tripled as Cloud GPUs Split…](https://giniloh.com/local-ai-payback-cloud-gpu-spread/) — more on Major Purchases & Assets
- [Your 32GB Card, Gone](https://giniloh.com/your-32gb-card-gone/) — more on Major Purchases & Assets
- [Your GPU Runs Out of Cache Before It Runs Out of Math](https://giniloh.com/kv-cache-is-the-concurrency-ceiling/) — more on Major Purchases & Assets
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** China's half-year data shows custom AI chips out-shipping standard GPUs for the first time, landing the same day Nvidia open-sourced its GPU sharing software.
- **Why It Matters:** The real edge is moving from the raw speed of a single chip to how well thousands of chips work together in a cluster. The software layer that manages that hardware now sets your cost per token.
- **What I'd Watch:** How teams shift their focus from buying more hardware to tuning the control plane.
  - **Open scheduling:** A public tool lets teams manage their own fleets without asking a vendor for permission.
  - **Card splitting:** Sharing one physical GPU across multiple jobs boosts use rates without requiring new purchase orders.
  - **The fabric:** The physical network sets the time to first token, pushing buyers to weigh switch costs alongside chip costs.
- **The Catch:** The hardware flip is limited to China's blocked market, and Nvidia's free tier lacks the enterprise support most large companies need.

## Sources
[1] IDC data for the first half of 2026 on China's AI accelerator shipments, reported by Reuters, 2026-10-13 — https://www.reuters.com/business/retail-consumer/nvidias-china-ai-chip-share-falls-huawei-closes-gap-report-finds-2026-10-13 (full wire text retrieved from the U.S. News syndication: https://money.usnews.com/investing/news/articles/2026-10-12/nvidias-china-ai-chip-share-falls-as-huawei-closes-gap-report-finds)
[2] NVIDIA, "NVIDIA Run:ai Is Now Open Source as Part of NVIDIA DSX AI Factory Platform", 2026-10-13 — https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/
[3] NVIDIA, "Productive, Durable, Fungible: How NVIDIA AI Factories Maximize Return on Investment", 2026-10-01 — https://blogs.nvidia.com/blog/productive-durable-fungible-ai-factories
[4] "An Optical KV Cache Network for Disaggregated LLM Serving", arXiv:2610.18444, 2026-10-13 — https://arxiv.org/abs/2610.18444
[5] TrendForce, "AI Server Demand Sustains Memory Contract Price Increases in 4Q26", 2026-09-30 — https://www.trendforce.com/presscenter/news/20260930-13258.html
[6] NVIDIA Model Optimizer, "AutoQuant KV: Automatic Mixed-Precision KV Cache Quantization", 2026-10-08 — https://nvidia.github.io/Model-Optimizer/announcements/autoquant-kv.html

## Gate report
lead
PASS — Drops readers immediately into the core takeaway with zero throat-clearing, expanding AI, GPU, and CNCF on first use.
tension
PASS — Replaces dense jargon with simple, everyday words while keeping paragraphs short. Carries a first-person cue and quotes IDC's own axis statement verbatim.
tactical-insight
PASS — Clean bullets, observations rather than commands, strong first-person read, readable language.
nuanced-takeaway
PASS — Honest limitations in short paragraphs; carries a first-person cue and the counterweight from Nvidia's own asset-life argument.
tldr
PASS — Four-part Smart Brevity schema under its own 'At a glance' header.
post-rewrite audit (desk, 2026-10-14)
Six corrections applied by hand after the frontier rewrite, none visible to any gate: the frontier's re-cut title ("The Control Plane is the New Product", 81/100 OK) reverted to the hand-written 100/100 STRONG headline; "the International Data Corporation" (an expansion the run never fetched) replaced with the verified gloss "IDC (the market research firm)"; "Eight major cloud hosts are already using it" corrected to "integrating it" (the source says integrating, not operating); the optical-fabric result's "a fraction of the cost" restored to the source's own "0.55 to 0.78 times the cost of a 2:1 fabric"; the claim that the non-GPU bucket covers chips built to run trained models "not train them" narrowed to what the wire states ("such as running already-trained models"); and "a crash, not a cause" corrected to "a coincidence". Every figure in the body traces to the verified brief (2.008M / 1.016M / 991K / 25,000 / 678,000 / 44% / 34% / 572,000 / 28% / 95% / 19% / −9% / 400-gigabit / 0.55 to 0.78 / 2020 / 2029 / five to six years / nine to ten years / a quarter / five-year schedule); no unsourced figure, no substituted name, no invented quotation.
