# Evergreen Brief: gpu_hardware — 2026-10-14
**Archetype:** evergreen
**Vertical:** gpu_hardware
**Persona:** infra_engineer
**Decision the reader is facing:** Whether to keep prefill and decode on the same machines or split them into two pools — and, if they are split, how to size each pool and what the key-value (KV) cache transfer between them costs the fabric that has to carry it.
**Durability:** Prefill is compute-bound and decode is memory-bandwidth-bound, which is a property of transformer inference rather than of this year's parts, so the rule survives the next silicon generation. The cited figures are as of their own publication dates (2023 and 2024 for the two cluster studies, DeepSeek's reported 24-hour production window of 2025-02-27/28 and its 2025-03-18 framework post, 2026-10-13 for the optical fabric simulation), and each is stated with that date so a reader can re-check it.
**De-dup:** `2026-10-07_kv-cache-is-the-concurrency-ceiling` is this vertical's nearest prior evergreen artifact, and it answers a different question: how many users one fixed card serves once the KV cache is paged per token. This brief is about the other axis — which machines the two phases run on, why colocating them makes each phase pay for the other's bottleneck, and what the cache transfer between the pools costs. It is also distinct from the news pieces `2026-10-07_gpu-hour-price-set-by-memory` (memory sets the hourly rate) and `2026-10-14_your-chip-stopped-deciding` (the scheduling and control plane above the part).
**Thesis:** A served token is two different machines — compute-bound prefill and bandwidth-bound decode — so splitting them into pools whose ratio matches the prompt-to-output mix is where the next increment of served requests comes from, and the price of that split is the KV cache the fabric has to carry between them.

**Lead:** The vertical's own `primary_angles` ("inference economics", "memory bandwidth ceilings") and the founder's `gpu_hardware` positions in `context/growth_os/founder-voice.md` §3 ("Memory Bandwidth Is the Real Bottleneck"; "Inference Unit Economics — the metric that matters is tokens generated per dollar per watt"), read against the `infra_engineer` persona's wants in `context/personas.json` ("real numbers, caveats, reproduction details") and the `gpu_hardware` field notes in `context/growth_os/customer-truth.md` §`gpu_hardware` (the serving-stack swap that cut a cloud GPU bill from $28,000 to $9,500 a month). The specific material is the 2026-10-14 signal pool for this vertical — row 5, the optical KV-cache network for disaggregated serving (https://arxiv.org/abs/2610.18444), and row 7, the parallelism-characterization paper that splits its analysis by phase (https://arxiv.org/abs/2610.05305) — plus the two cluster studies and the one production service that publish per-phase throughputs, which that material cites.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | DeepSeek — Open Source Week day 6: DeepSeek-V3/R1 inference system overview (production service statistics, window 2025-02-27 12:00 to 2025-02-28 12:00 UTC+8) | https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md | 2026-10-14 | 73.7k tokens/s input — each H800 node's average throughput while prefilling, against 14.8k tokens/s output while decoding, in a service already running prefill and decode as separate pools with different parallelism per phase, where the average KV-cache length per output token was 4,989 tokens | measured |
| 2 | DistServe (Zhong et al., OSDI 2024) — arXiv full text, evaluation summary | https://arxiv.org/html/2401.09670v3 | 2026-10-14 | 7.4 times more requests — or 12.6 times tighter service-level objective (SLO) — than the colocating systems it was compared against, while staying inside the latency limit for more than 90% of requests | measured |
| 3 | DistServe — same full text, single-A100 goodput experiment (13B model, 512-token input, 64-token output) | https://arxiv.org/html/2401.09670v3 | 2026-10-14 | 1.6 requests per second — the per-GPU goodput of the model served colocated on one A100 at a 90% SLO goal, against 5.6 requests per second for a card serving prefill alone and 10 for a card serving decode alone | measured |
| 4 | DistServe — same full text, section on communication overhead | https://arxiv.org/html/2401.09670v3 | 2026-10-14 | 1.13GB — the KV cache of a single 512-token request on OPT-66B, so an average arrival rate of 10 requests per second needs 90Gbps of bandwidth before the transfer stops being visible | measured |
| 5 | Splitwise (Patel et al., ISCA 2024) — arXiv full text | https://arxiv.org/html/2311.18677v1 | 2026-10-14 | 1.4 times higher throughput at 20% lower cost — the phase-split cluster against the conventional one on the same budgets; the alternative chord is 2.35 times more throughput at the same cost and power | measured |
| 6 | An optical KV-cache network for disaggregated serving — arXiv abstract | https://arxiv.org/abs/2610.18444 | 2026-10-14 | 0.55 to 0.78 times the cost of a 2:1 packet fabric — what a reservation-scheduled optical fabric matched for carrying the KV cache, on simulated clusters built from real serving traces with measured H100 prefill times, tolerating the 50 ms reconfiguration delay of a 384-port mechanical switch | measured |
| 7 | NVIDIA — Introducing NVIDIA Dynamo, a low-latency distributed inference framework (2025-03-18) | https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/ | 2026-10-14 | 30x requests served — the vendor's own claim for its disaggregated prefill/decode framework running DeepSeek-R1 on a GB200 NVL72 rack, against the same models without it | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Two machines, one card: split prefill from decode, and budget the cache transfer between the pools | 9 | 9 | 9 | 9 | **9.0** | **winner** |
| The parallelism ladder by phase: which topology to run on each pool | 8 | 9 | 7 | 7 | 7.9 | dropped — the characterization paper's numbers are modeled latency curves, not a measured deployment, so it can be cited but not anchored |
| Chunked prefill as the cheap first step before a split | 8 | 8 | 6 | 8 | 7.4 | dropped — the primary documentation states the mechanism with no figure of its own, and the only figures are in secondary blogs; carried as context, not as a row |
| Sizing the fabric for the KV transfer alone | 7 | 8 | 8 | 7 | 7.5 | dropped — retreads this vertical's 2026-10-07 KV-capacity evergreen and the fabric row of the 2026-10-14 news piece; the fabric is one row here, not the thesis |
| What a self-hosted GPU-hour costs in electricity | 7 | 8 | 6 | 7 | 7.0 | dropped — settled by spec-sheet arithmetic plus one government price; the 2026-10-13 workstation run scored the same topic 7.6 and dropped it, and nothing has changed since |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=7 fetched=7 sources=5 hosts=3 decision="sha1:e00d2897fa" dedup="matched a prior artifact: 2026-10-07_kv-cache-is-the-concurr" window_days=180 checked_at=2026-10-14T18:35:56+00:00 -->
<!-- evergreen-gate:end -->
