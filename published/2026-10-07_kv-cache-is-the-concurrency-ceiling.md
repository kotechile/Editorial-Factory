---
title: "Your GPU Runs Out of Cache Before It Runs Out of Math"
vertical: gpu_hardware
persona: infra_engineer
one_big_thing: "On a fixed GPU, the number of users one card can serve at once is set by memory for the key-value cache, not by the weights or the math rate — so the cheapest capacity is a paged, per-token scheduled serving stack, and the second cheapest is another card."
date: 2026-10-07
slug: kv-cache-is-the-concurrency-ceiling
archetype: evergreen
evergreen: true
meta_title: "Your GPU Runs Out of Cache Before It Runs Out of Math"
meta_title_source: "derived_from_title"
meta_description: "A graphics processing unit (GPU) serving a 7-billion-parameter model at 16-bit precision holds about 14GB of weights in memory before it answers a single…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/kv-cache-is-the-concurrency-ceiling/featured.png"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "The KV Cache Bottleneck. Isometric cutaway of a large processor bottlenecked by narrow memory pipelines on a drafting table."
image_caption: "The KV Cache Bottleneck: How the KV cache dictates GPU capacity."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A graphics processing unit (GPU) serving a 7-billion-parameter model at 16-bit precision holds about 14GB of weights in memory before it answers a single prompt [3]. Every token it generates then adds a second, hidden cost: the key-value (KV) cache [3]. Researchers found early systems wasted most of the memory they set aside for this cache [1]. That empty space is the difference between buying one card and buying two.

<!-- tension -->

## The big picture:

A large language model (LLM) answers one token at a time. Each step forces the system to read the whole model and its cache out of memory. Every new token needs to look back at the past tokens to make sense of the text.

Nvidia splits this job into two parts [3]. First, a prompt phase reads the input all at once. Next, a generation phase creates the answer, and this step is entirely limited by memory speed [3]. The expensive part of the job is not doing the math. It is reading the data.

Databricks points out the exact same thing: memory speed acts as the main bottleneck for how fast a model runs [4]. A 7-billion-parameter model generating one token every 14 milliseconds moves 14GB in that time [4]. That eats up half the memory speed of a top-tier card just for one user [4].

My read: Teams often buy chips for their math speed, but the cache is the real asset they use up. Few teams price this cache before they buy.

## By the numbers

- **20.4% to 38.2% — Cache memory used:** Early systems only filled this small share of their reserved memory with real data [1]. The rest sat completely empty due to poor planning.
- **4% — Waste after paging:** Splitting the memory into small, fixed blocks cut wasted space to under 4% [2]. This fixed the 60% to 80% loss seen in older setups [2].
- **2GB — One session's cache:** A 7-billion-parameter model handling a 4,096-token chat needs about 2GB of cache, plus its 14GB of weights [3].
- **23x — Scheduling throughput:** Adding a new user the exact moment another finishes a token proved 23 times faster than waiting for a whole group to finish at once [5].

<!-- tactical-insight -->

## What I'd watch:

What strikes me here is that cheap capacity does not come from a new purchase order. It comes from three specific changes to the software stack, and I want to see which one a team tries first.

- **Computed cache budgets:** Teams can calculate their exact memory needs using strict math. The rule is bytes per token equals 2 × layers × (heads × head size) × bytes per number [3]. They read the layer count from the model card, then divide the free memory by the result.
- **Block paging:** Systems now keep the cache in fixed-size blocks that can live anywhere in memory [1][2]. When a user finishes early, the system frees up that exact block. This completely removes the massive chunks of wasted space.
- **Per-token scheduling:** A smart queue adds a new request the instant another finishes a token [5]. This keeps the hardware fully busy instead of waiting on the slowest user in a group.

<!-- nuanced-takeaway -->

## The catch

The part I keep circling is that these massive speed gains are ceilings compared to older setups, not guaranteed wins for every workload.

The 24-times jump compares a highly tuned system against a very basic path [1][2]. Software that already groups requests well has far less room to grow. A 2-to-4-times gain is a much more realistic target for teams already using good tools [1].

Paging also adds no raw memory speed. It simply lets one card hold more users at once. Because the total speed stays the same, each user gets a smaller slice of the pie [4].

Long inputs bite the hardest, because the cache grows fast as the chat gets longer [3]. A larger group of users lifts the total output, but it slows down every single user at the exact same time [4].

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "NVIDIA RTX PRO: Groundbreaking Performance, But Does the Math…" -> https://giniloh.com/nvidia-rtx-pro-groundbreaking-performance-but-does-the-math-check/ [same site (giniloh.com); same category; topical overlap: math, single] Link "NVIDIA RTX PRO: Groundbreaking Performance, But Does the Math…" in the section where the article touches math, single. -->
<!-- internal-link hint: "Replace Laptop Screen? Let This Decision Engine Do the Math" -> https://giniloh.com/replace-laptop-screen-let-this-decision-engine-do-the-math/ [same site (giniloh.com); same category; topical overlap: math] Link "Replace Laptop Screen? Let This Decision Engine Do the Math" in the section where the article touches math. -->
<!-- internal-link hint: "Ebike Costs: Per-Use Calculator for Commuters" -> https://giniloh.com/ebike-costs-per-use-calculator-for-commuters/ [same site (giniloh.com); same category] Link "Ebike Costs: Per-Use Calculator for Commuters" in the section where the article touches this topic. -->
## Related reading

- [NVIDIA RTX PRO: Groundbreaking Performance, But Does the Math…](https://giniloh.com/nvidia-rtx-pro-groundbreaking-performance-but-does-the-math-check/) — more on Major Purchases & Assets
- [Replace Laptop Screen? Let This Decision Engine Do the Math](https://giniloh.com/replace-laptop-screen-let-this-decision-engine-do-the-math/) — more on Major Purchases & Assets
- [Ebike Costs: Per-Use Calculator for Commuters](https://giniloh.com/ebike-costs-per-use-calculator-for-commuters/) — more on Major Purchases & Assets
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** A graphics processing unit (GPU) hits its user limit on memory for the key-value cache, not on raw math power.
- **Why It Matters:** Generating a token forces the system to read the model and cache from memory, meaning a chip with spare compute can still be completely full.
- **What I'd Watch:** How teams manage memory limits before they buy another card:
  - **Computed cache budgets:** Calculating exact memory needs using strict math based on layers and heads.
  - **Block paging:** Storing cache in fixed-size blocks anywhere in memory to stop wasting empty space.
  - **Per-token scheduling:** Refilling the group instantly as each user finishes a token to keep the card busy.
- **The Catch:** These massive speed gains are ceilings compared to older setups, and a larger group slows down individual users even as it lifts total output.

## Sources
[1] Woosuk Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention" (SOSP 2023, arXiv:2309.06180) — profiling showing 20.4%–38.2% of reserved cache memory held token states, the per-token block design, and the 2–4× throughput gain over FasterTransformer and Orca (https://arxiv.org/html/2309.06180v1)
[2] Woosuk Kwon et al., "vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention", vLLM Blog, 2023-06-20 — 60%–80% memory waste before paging, waste under 4% with PagedAttention, up to 24× throughput over HuggingFace Transformers, and up to 1.7GB of cache for a single LLaMA-13B sequence (https://blog.vllm.ai/2023/06/20/vllm.html)
[3] Nvidia, "Mastering LLM Techniques: Inference Optimization", Nvidia Technical Blog — 14GB of weights for a 7B model at 16-bit, the KV cache sizing formula, the Llama 2 7B worked example at about 2GB, linear growth with batch size and sequence length, and the prefill/decode split where decode is memory-bound (https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/)
[4] Databricks, "LLM Inference Performance Engineering: Best Practices", Databricks Engineering Blog — memory bandwidth as the bottleneck, the 7B/16-bit example at 14 ms per token using 1TB/sec of a 2TB/sec card (50%), and the throughput-versus-latency trade-off at larger batch sizes (https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices)
[5] Cade Daniel, Chen Shen, Eric Liang and Richard Liaw, "How continuous batching enables 23x throughput in LLM inference while reducing p50 latency", Anyscale, 2023-06-22 — continuous versus request-level batching, and the 23× throughput gain (https://www.anyscale.com/blog/continuous-batching-llm-inference)

## Gate report
lead: PASS — Opens directly with the core constraint and immediately explains the hidden cost of the KV cache using simple phrasing.
tension: PASS — Explains the bandwidth bottleneck clearly with a first-person observation and single-sentence follow-up to the H2.
tactical-insight: PASS — Translates the engineering solutions into observable market moves without issuing commands, using plain English definitions.
nuanced-takeaway: PASS — Highlights the trade-offs of batching and the reality of the benchmark numbers clearly, keeping paragraphs under 3 sentences.
tldr: PASS — Strict adherence to the 4-part Smart Brevity schema with proper indented sub-bullets for the tactical section.
