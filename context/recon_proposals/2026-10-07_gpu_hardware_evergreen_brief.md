# Evergreen Brief: gpu_hardware — 2026-10-07

**Archetype:** evergreen
**Vertical:** gpu_hardware
**Persona:** infra_engineer
**Decision the reader is facing:** Whether to add another GPU (or rent another instance) to serve more concurrent users, or fix the serving stack first — paged KV cache plus continuous batching — and how to work out the per-session KV-cache footprint so the concurrency ceiling on the card they already own is a number they can compute rather than a guess.
**Durability:** Still true in 12 months because the mechanism is architectural, not a version artefact: decoding reads the whole model plus the whole KV cache from memory once per token, the KV cache grows linearly with batch size and sequence length, and it is managed in fixed-size blocks — so what caps concurrency is memory capacity and bandwidth, not the FLOPS on the box. The measured multipliers are as of the cited publications (the vLLM PagedAttention paper, SOSP 2023; the vLLM launch post, 2023; the NVIDIA and Databricks inference references, 2024; the Anyscale continuous-batching reference, 2024) and the exact gains drift with model shape and sequence length; the constraint and the sizing rule do not expire.
**De-dup:** Nearest prior artifact for this vertical is `2026-10-07_gpu-hour-price-set-by-memory` (`published/2026-10-07_gpu-hour-price-set-by-memory.md`): that piece is about HBM *price* setting what a rented GPU-hour costs — the market rate for someone else's silicon. This one is about *capacity on the GPU you already have*: the KV cache as the concurrency ceiling and the batching stack as the cheap multiplier. It is also distinct from `2026-10-06_local-ai-payback-cloud-gpu-spread` (buy-vs-rent capex payback, workstation_compute_economics) — no re-argument of either thesis.
**Thesis:** On a fixed GPU the number of concurrent sessions you can serve is capped by KV-cache memory, not by model weights — so the first capacity to buy is a paged, continuously-batched serving stack, and the second is another card.

**Lead:** The vertical's own `primary_angles` ("inference economics", "memory bandwidth ceilings"), founder-voice §3 `gpu_hardware` ("Memory Bandwidth Is the Real Bottleneck"; "Inference Unit Economics — tokens generated per dollar per watt"), and real field friction in `context/growth_os/customer-truth.md` §gpu_hardware Anecdote 1 (a production team cut its GPU cloud bill from $28,000 to $9,500/month by moving to vLLM with paged attention and FP8 quantization on the same H100s). The persona's standing question — *how much concurrency does this card hold before I buy another one?* — is the decision. `scripts/gsc_analyzer.py --vertical gpu_hardware` returned 0 high-potential striking-distance queries (impressions are still thin on a young site), so demand is a bonus signal here, not the driver.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (SOSP 2023), arXiv:2309.06180 | https://arxiv.org/html/2309.06180v1 | 2026-10-07 | 20.4% to 38.2% — share of KV cache memory actually holding token states in existing serving systems; the rest is lost to fragmentation and over-reservation, which is what caps the batch size | measured |
| 2 | *vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention* (vLLM Blog, 2023-06-20) | https://blog.vllm.ai/2023/06/20/vllm.html | 2026-10-07 | 4% — KV cache memory wasted under PagedAttention (only the last block of a sequence) against the 60% to 80% that existing systems waste on fragmentation and over-reservation | measured |
| 3 | *Mastering LLM Techniques: Inference Optimization* (NVIDIA Technical Blog, 2024) | https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ | 2026-10-07 | 14 GB — memory held by a 7-billion-parameter model loaded at 16-bit precision before any KV cache is counted; KV caching then grows linearly with batch size and sequence length | vendor claim |
| 4 | *LLM Inference Performance Engineering: Best Practices* (Databricks Engineering Blog) | https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices | 2026-10-07 | 14ms — time per output token for a 7B model at 16-bit, which moves 14GB of parameters in 14ms and needs about 1TB/sec of memory bandwidth against a 2TB/sec machine peak | measured |
| 5 | *Achieve 23x LLM Inference Throughput & Reduce p50 Latency* (Anyscale, continuous batching with Ray Serve) | https://www.anyscale.com/blog/continuous-batching-llm-inference | 2026-10-07 | 23x — throughput gain from continuous batching over naive request-level batching, at the same time-to-first-token budget | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| KV cache, not weights, caps concurrency — page it, batch it, then buy a card | 9 | 9 | 9 | 8 | 8.9 | **winner** |
| Quantization depth: how much VRAM FP8 weights and an FP8 cache actually save | 8 | 8 | 6 | 8 | 7.5 | dropped — the cache-quantization leg rests on a vendor doc page that returned 61 characters, so one anchor is not fetchable and the claim would ship unverifiable |
| Prefill vs decode: two budgets, one card (TTFT and time-per-token) | 8 | 8 | 8 | 6 | 7.7 | dropped — real and well-sourced, but its actionable number is the KV cache already carried by the winner, and its threshold rules are softer |
| Serverless GPU cold starts (15–30 s) as an interactive-session non-starter | 7 | 7 | 6 | 7 | 6.8 | dropped — the figure is a field note in `customer-truth.md`, not a fetchable primary measurement, so it cannot clear the floor |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=5 hosts=5 decision="sha1:ccb44e7f62" dedup="matched a prior artifact: 2026-10-07_gpu-hour-price-set-by-m" window_days=180 checked_at=2026-10-07T18:32:15+00:00 -->
<!-- evergreen-gate:end -->
