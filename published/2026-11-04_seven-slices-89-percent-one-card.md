---
title: "Seven Slices Won't Buy 89%"
vertical: gpu_hardware
kind: evergreen
archetype: evergreen
evergreen: true
persona: infra_engineer
one_big_thing: "A Multi-Instance GPU profile is metered by the memory fraction, not the compute fraction — a 1g slice measured about 13% of a 96 gigabyte card's memory bandwidth against a seventh of its cores — so seven tenants book roughly 89% of one card's bandwidth and 85% of its cores, never seven cards, and the profile has to be sized from the resource a workload saturates."
date: 2026-11-04
slug: seven-slices-89-percent-one-card
meta_title: "Seven Slices Won't Buy 89%"
meta_title_source: "derived_from_title"
meta_description: "Seven slices of one 96 gigabyte card do not buy seven cards. Cut a Hopper card into the smallest Multi-Instance GPU (MIG) profile, and each tenant gets 16…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/seven-slices-89-percent-one-card/featured.jpg"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "A matte clay render of a graphics card on a steel bench, split into seven bays by brass dividers, one bay left open."
image_caption: "Seven slices of one card: multi-instance GPU tenants are metered by memory, not by cores."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Seven slices of one 96 gigabyte card do not buy seven cards. Cut a Hopper card into the smallest Multi-Instance GPU (MIG) profile, and each tenant gets 16 cores and 406 gigabytes a second (GB/s) of memory speed, against 3,175 GB/s for the whole card [1][4]. A tenant sees about 13% of the pipe, not the seventh its core count suggests, because the card divides its memory in eighths and its cores in sevenths. Add the seven tenants up and the split books 112 of 132 cores and about 89% of the memory rate [1].

<!-- tension -->
## A slice is not a seventh

The vendor's own description gives the split away. A memory slice is "roughly one eighth" of the card's memory, "including both capacity and bandwidth", while a compute slice is "roughly one seventh" of the cores [4]. Memory, memory speed and copy engines fall in eighths; cores fall in sevenths. I read the spec twice before I believed that gap, because most sizing advice starts from cores.

Two 24 gigabyte slices, one with 26 cores and one with 32, both run at 812 GB/s. The two 48 gigabyte slices run at 1,611 and 1,635 GB/s, four cores apart [1]. Core count moves around, while the memory slice sets the rate.

Seven of the smallest slices book 112 of 132 cores, so 15% of the card sits idle, and they book 77 of its 96 gigabytes as usable memory [1]. Four larger slices book 104 cores, 92 gigabytes and 3,248 GB/s in total [1]. Fewer tenants, more of the card. Memory turns out to be the scarce half.

The shape is not a Hopper artefact. On a GB200 the card offers seven 23 gigabyte, four 46 gigabyte or two 93 gigabyte slices, sold on its own memory, cache and speed per tenant [3]. Every generation meters tenants in eighths.

## By the numbers

- **39.6 GB/s — copy-path ceiling:** a 1g slice copies host memory through the copy engine at 39.6 GB/s, against 276.3 GB/s with no split, and larger slices ran at the same rate [1].
- **17.5 gibibytes — memory left unbooked:** seven smallest slices leave 17.5 gibibytes unused, because each books 11 usable rather than the 12 printed in its name [1].
- **30% — what isolation is worth:** the co-execution study gives MPS (multi-process service) up to 30% in good conditions, and takes about 30% away under memory clashes, which MIG's hard split removes [2].

<!-- tactical-insight -->
## What operators test instead

Teams close to this stop reading the profile table and change one axis at a time. Grow the slice that adds cores, and a core-bound job goes faster. Grow the memory slice, and a memory-bound job goes faster. The paper's own reward model lands where that test points: for 8-bit Llama3 serving and vector search, the setup built from the smallest slice won when waste dominated, and the full card won when per-request speed dominated [1].

Separation is the other half of the choice. Sharing one memory space pays while jobs do not collide, and costs when they do. Splitting the hardware removes that clash, then charges for it in fixed sizes, because a job whose needs fall between two slices wastes the gap [2]. What I am watching next is the copy-lane anomaly: the paper calls its flat copy rate "likely a bug", so a driver update could retire that row [1].

<!-- nuanced-takeaway -->
## The catch

I may be overstating the memory floor, and the same paper says why. Its language model case scaled almost perfectly with core count, so that test is core-bound, and short prompts on an 8-bit model will see the seventh rather than the eighth [1]. The rule binds on long-context decoding, where each token reads a cache the slice can barely feed — the same ceiling one layer up, where [a card runs out of cache before it runs out of math](/kv-cache-is-the-concurrency-ceiling/) (the running memory a model keeps for each open conversation).

Two limits matter too. The numbers come from one card in one machine: an HBM3 Hopper part inside a Grace Hopper system, so the copy figures describe that machine's chip-to-chip link at 450 GB/s per direction, not a PCIe host [1]. And that one-seventh figure is a rounding, because the measured count is 16 cores of 132 [1][4].

None of this makes the split useless. It makes the count on the box the wrong unit, which is why the floor a memory-bound tenant should expect is 13%. The test for going bigger is which slice change moves tokens a second.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "480GB Won't Skip Your Memory Queue" -> /your-480gb-card-wont-skip-the-memory-queue/ [same site (aichieve.net); same category; topical overlap: card, cards, won't] Link "480GB Won't Skip Your Memory Queue" in the section where the article touches card, cards, won't. -->
<!-- internal-link hint: "2,000 Fine-Tunes Cost You 5.5% Throughput" -> /2000-fine-tunes-one-card-55-throughput/ [same site (aichieve.net); same category; topical overlap: card] Link "2,000 Fine-Tunes Cost You 5.5% Throughput" in the section where the article touches card. -->
<!-- internal-link hint: "Fine-Tune or Rent: The Denominator Decides Your Break-Even" -> /fine-tune-vs-rent-by-token/ [same site (aichieve.net); same category; topical overlap: card] Link "Fine-Tune or Rent: The Denominator Decides Your Break-Even" in the section where the article touches card. -->
## Related reading

- [480GB Won't Skip Your Memory Queue](/your-480gb-card-wont-skip-the-memory-queue/) — more on Major Purchases & Assets
- [2,000 Fine-Tunes Cost You 5.5% Throughput](/2000-fine-tunes-one-card-55-throughput/) — more on Major Purchases & Assets
- [Fine-Tune or Rent: The Denominator Decides Your Break-Even](/fine-tune-vs-rent-by-token/) — more on Major Purchases & Assets
<!-- internal-links:end -->

<!-- tldr -->
## At a glance

**The shift:** One card now splits into seven tenants metered in eighths of memory and speed, but sevenths of cores.
**The number:** 13% of the card's speed per smallest slice.
**The risk:** Core-bound serving scales with cores, so the memory rule binds only long-context decode.

## Sources
[1] G. Schieffer, R. Shi, J. Ren and I. Peng, "Taming GPU Underutilization via Static Partitioning and Fine-grained CPU Offloading", arXiv:2604.08451v1, 9 April 2026 — https://arxiv.org/html/2604.08451v1
[2] J. Villarrubia, L. Costero, F. D. Igual and K. Olcoz, "A comprehensive evaluation of spatial co-execution on GPUs using MPS and MIG technologies", arXiv:2604.22430v2, 29 April 2026 — https://arxiv.org/html/2604.22430v2
[3] NVIDIA, "Multi-Instance GPU" technology page (GB200 partition shapes) — https://www.nvidia.com/en-us/technologies/multi-instance-gpu
[4] NVIDIA, "Multi-Instance GPU User Guide — Concepts" (memory slice and SM slice definitions) — https://docs.nvidia.com/datacenter/tesla/mig-user-guide/concepts.html
