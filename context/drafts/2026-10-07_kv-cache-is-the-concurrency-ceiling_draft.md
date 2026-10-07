---
title: "Your GPU Runs Out of Cache Before It Runs Out of Math"
vertical: gpu_hardware
persona: infra_engineer
one_big_thing: "On a fixed GPU, the number of users one card can serve at once is set by memory for the key-value cache, not by the weights or the math rate — so the cheapest capacity is a paged, per-token scheduled serving stack, and the second cheapest is another card."
date: 2026-10-07
slug: kv-cache-is-the-concurrency-ceiling
archetype: evergreen
evergreen: true
---

<!-- lead -->
A graphics processing unit (GPU) serving a 7-billion-parameter model at 16-bit precision holds about 14GB of weights in memory before it answers a single question [3]. Every token of every session it handles at the same time then adds a second bill, and most capacity plans never see it: the key-value (KV) cache [3].

Researchers who profiled real serving systems found they used only 20.4% to 38.2% of the memory they had set aside for that cache [1]. The rest sat idle. That gap is the difference between one card and two.

<!-- tension -->

## The big picture:

A large language model (LLM) answers one token at a time, and each token forces a full read of the model and its cache out of memory. Nvidia splits this into a prefill phase that chews through the prompt in parallel and a decode phase that is memory-bound [3]. The expensive part of the job is not the math. It is the reading.

Databricks says the same thing in one of its own headings: memory bandwidth is the main bottleneck for inference speed [4]. Its worked example makes the point concrete. A 7B model at 16-bit that emits a token every 14 ms is moving 14GB in that time, or about 1TB/sec. On a card that peaks at 2TB/sec, one session spends half the memory speed of the whole card [4].

That is why plans built on math rate keep surprising people. The chip has compute to spare and no room left to hold the sessions. My read: the cache is the asset being bought, and few teams price it before they buy.

## By the numbers

- **20.4% to 38.2% — Cache memory in use:** Profiling of existing serving systems found that only this share of the memory reserved for the key-value cache held real token states; the rest was lost to fragmentation and over-reservation [1].
- **4% — Waste after paging:** Splitting the cache into fixed-size blocks that do not need to sit next to each other cut wasted memory to under 4%, against the 60% to 80% that earlier systems lost [2].
- **2GB — One session's cache:** A Llama 2 7B model at 16-bit, a 4,096-token context, and a batch of one need about 2GB of cache, on top of roughly 14GB of weights [3].
- **23x — Throughput from scheduling:** Continuous batching, which refills the batch as each session finishes a token instead of waiting for the slowest one, measured 23 times the throughput of request-level batching while cutting median latency [5].

<!-- tactical-insight -->

## What I'd watch:

What strikes me here is that the cheap capacity does not come from a purchase order. It comes from three changes to the serving stack, and I'd want to know which one a team reaches for first.

- **A cache budget sized from the model config.** The rule is arithmetic: bytes per token is 2 × layers × (heads × head size) × bytes per number, and the total is batch × sequence × 2 × layers × hidden size × 2 bytes at 16-bit [3]. Teams that do this read the layer count and hidden size off the model card, then divide the card's free memory by the per-session result.
- **A paged cache.** PagedAttention keeps the cache in fixed-size blocks that can live anywhere in memory, so a half-finished session stops holding a whole reserved chunk [1][2]. That is where the 60%-to-80% waste goes.
- **A per-token scheduler.** A queue that admits a new request the moment another finishes a token keeps the card busy without waiting on its slowest session [5].

<!-- nuanced-takeaway -->

## The catch

The part I keep circling is that every multiplier here is a ceiling against a named baseline, not a promise for a given workload. The 2–4× figure compares vLLM with FasterTransformer and Orca at equal latency, and the 24× figure compares it with the plain Hugging Face Transformers path [1][2]. A stack that already batches well has far less room to gain.

Paging also adds no bandwidth. It lets one card hold more sessions at once, and each session gets a smaller slice of the memory speed [4]. A bigger batch lifts total throughput and slows every single user at the same time, which is the trade-off Databricks describes [4].

Two limits deserve a closer look. Long inputs are where the cache bites hardest, because it grows with the batch and the sequence length together [3]. And the figures here are as of the cited sources, published between 2023 and 2024, and they move with model shape, context length, and precision. The shape of the constraint does not move: a session that is still generating still holds its memory.

<!-- tldr -->

## At a glance

- **The Big Shift:** The number of users one GPU can serve at once is set by memory for the key-value cache, not by the weights or the math rate. Profiled systems used as little as a fifth of the cache memory they had reserved.
- **Why It Matters:** Decoding a token re-reads the model and the cache out of memory, so a card with compute to spare can still be full. The same silicon carries more sessions once the cache is paged and scheduled per token.
- **What I'd Watch:** How teams price the cache before they buy another card:
  - **A computed cache budget:** Bytes per token equal 2 × layers × (heads × head size) × bytes per number, scaled by batch and sequence length.
  - **Block paging:** Cache kept in fixed-size blocks anywhere in memory, so unfinished sessions stop holding reserved space.
  - **Per-token scheduling:** Refilling the batch as each session finishes a token, which measured 23 times the throughput of waiting for a whole batch to end.
- **The Catch:** The multipliers are ceilings against named baselines, paging adds no bandwidth, and a larger batch slows each user even as it lifts total throughput.

## Sources
[1] Woosuk Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention" (SOSP 2023, arXiv:2309.06180) — profiling showing 20.4%–38.2% of reserved cache memory held token states, the per-token block design, and the 2–4× throughput gain over FasterTransformer and Orca (https://arxiv.org/html/2309.06180v1)
[2] Woosuk Kwon et al., "vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention", vLLM Blog, 2023-06-20 — 60%–80% memory waste before paging, waste under 4% with PagedAttention, up to 24× throughput over HuggingFace Transformers, and up to 1.7GB of cache for a single LLaMA-13B sequence (https://blog.vllm.ai/2023/06/20/vllm.html)
[3] Nvidia, "Mastering LLM Techniques: Inference Optimization", Nvidia Technical Blog — 14GB of weights for a 7B model at 16-bit, the KV cache sizing formula, the Llama 2 7B worked example at about 2GB, linear growth with batch size and sequence length, and the prefill/decode split where decode is memory-bound (https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/)
[4] Databricks, "LLM Inference Performance Engineering: Best Practices", Databricks Engineering Blog — memory bandwidth as the bottleneck, the 7B/16-bit example at 14 ms per token using 1TB/sec of a 2TB/sec card (50%), and the throughput-versus-latency trade-off at larger batch sizes (https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices)
[5] Cade Daniel, Chen Shen, Eric Liang and Richard Liaw, "How continuous batching enables 23x throughput in LLM inference while reducing p50 latency", Anyscale, 2023-06-22 — continuous versus request-level batching, and the 23× throughput gain (https://www.anyscale.com/blog/continuous-batching-llm-inference)
