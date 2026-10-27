# Evergreen Brief: workstation_compute_economics — 2026-10-27

**Archetype:** evergreen
**Vertical:** workstation_compute_economics
**Persona:** infra_engineer
**Decision the reader is facing:** How many cards to buy — or how many GPU-hours to rent — to serve a growing set of task-specific fine-tunes, a decision that bites the week the fourth customer-specific or task-specific model arrives and the team starts pricing a fourth GPU on the assumption that one fine-tune needs one whole model's worth of memory.
**Durability:** The ratio and the mechanism do not expire: a LoRA adapter is a pair of low-rank matrices per module, so its bytes scale with rank times width and not with the base model, which is why the base can be loaded once and selected per request. The figures are dateable and stay quotable: the adapter-vs-base size ratio and the 30-adapter/3% VRAM line are **as of** the TGI multi-LoRA engineering post of 18 July 2024; the 2,000-adapter throughput and the baseline out-of-memory point are **as of** the S-LoRA paper's published benchmarks (arXiv 2311.03285v1, MLSys 2024) on A100 40 GB and 80 GB cards; the rank-to-parameter-share arithmetic and the low-rank quality finding are **as of** the LoRA Learns Less and Forgets Less study (arXiv 2405.09673v2, 2024); the 80 GB capacity anchor is **as of** NVIDIA's current A100 product page. What a reader re-checks each cycle is the serving stack's adapter limit and the card they are pricing, never the ratio itself.
**De-dup:** `2026-10-06_fine-tune-vs-rent-by-token` is this vertical's nearest prior artifact on the fine-tuning beat, and it settles whether to fine-tune at all by pricing one tuned model against a per-token API bill; this piece starts after that decision is made and prices the *fleet* — how many models one card serves — which that artifact never asks. Also checked and dropped by hand: `2026-10-07_kv-cache-is-the-concurrency-ceiling` (gpu_hardware) already owns the KV-cache-meets-concurrency thesis, `2026-10-27_your-gpu-break-even-is-37-percent-busy` (nhil_infrastructure_ops) already owns the utilisation-break-even thesis, and `2026-10-20_your-render-bill-multiplies-by-22-97` is this vertical's rendering-ROI piece — so none of those three mechanisms is re-argued here.
**Thesis:** A shelf of fine-tunes is not a shelf of models: an adapter is roughly a thousandth of its base model's bytes, so one card serves thousands of task-specific models at almost the throughput of one — which means the next purchase for a multi-model local deployment is host memory and a serving stack that packs adapters, not another GPU, and the limit that actually bites first is the naive serving path that runs out of memory at a hundred adapters.

**Lead:** The vertical's own third beat (`primary_angles`: "local llm fine-tuning hardware requirements vs commercial api per-token fees") plus the founder's standing position that fine-tuning open weights removes a recurring token bill (`context/growth_os/founder-voice.md` §"Local LLM Fine-Tuning & Open-Weights Economics"), narrowed to the half the corpus has not priced: the 2026-10-06 evergreen settled one fine-tune against an API bill, and the field anecdotes in `context/growth_os/customer-truth.md` (a 4×RTX 4090 rig for one tuned 14B model) describe rig-per-model builds, so the unasked question is what the *second through twentieth* model costs. GSC opportunity export for this vertical returned 0 candidate queries on 2026-10-20, so demand data adds nothing either way — the topic stands on the beats and the evidence. The specific material: the S-LoRA benchmark table (2,000 adapters on one A100 80 GB), the TGI multi-LoRA post's adapter-size arithmetic, and the measured finding that low-rank adapters underperform full fine-tuning on code and math.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Sheng et al., "S-LoRA: Serving Thousands of Concurrent LoRA Adapters" (arXiv 2311.03285v1), Table 3 | https://arxiv.org/html/2311.03285v1 | 2026-10-27 | 7.61 requests a second — with 2,000 adapters loaded on a single A100 (80GB), S-LoRA sustained 7.61 requests a second against 8.05 with five adapters | measured (authors' benchmark, one A100 80GB) |
| 2 | Same paper, Table 3 baseline columns | https://arxiv.org/html/2311.03285v1 | 2026-10-27 | 2.04 requests a second — the naive packed baseline (vLLM-packed) held 2.04 requests a second with five adapters and ran out of memory at 100 adapters | measured (same benchmark, baseline system) |
| 3 | Hugging Face, "TGI Multi-LoRA: Deploy Once, Serve 30 Models" (18 July 2024) | https://huggingface.co/blog/multi-lora-serving | 2026-10-27 | 13.6 MB — a Predibase Magicoder adapter is 13.6 MB against a 14.48 GB base model, under a thousandth of its size | vendor claim (platform operator's own post; artifact sizes as listed on the Hub) |
| 4 | Same post, VRAM arithmetic | https://huggingface.co/blog/multi-lora-serving | 2026-10-27 | 3% — loading 30 adapters into VRAM is only a 3% increase | vendor claim (platform operator's own worked example) |
| 5 | NVIDIA, A100 Tensor Core GPU product page | https://www.nvidia.com/en-us/data-center/a100/ | 2026-10-27 | 80 GB — the A100 80GB carries 80 GB of memory and the PCIe and SXM variants are the card the study benchmarks on | vendor claim (specification table) |
| 6 | Biderman et al., "LoRA Learns Less and Forgets Less" (arXiv 2405.09673v2), §2 and §4.1 | https://arxiv.org/html/2405.09673v2 | 2026-10-27 | 4096 — a rank-16 adapter on a 4096-wide 7B weight matrix trains under 1% of the original parameters, and the study's own result section is titled "LoRA at low ranks underperforms full finetuning" on code and math | measured (preprint; continued-pretraining and instruction-tuning experiments) |

## Candidate topics considered

| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| One card serves thousands of task fine-tunes; buy host memory and a packing serving stack, not the next GPU | 9 | 8 | 9 | 9 | 8.8 | **winner** |
| The KV cache, not the weights, sets what context length and concurrency a card carries | 9 | 9 | 9 | 8 | 8.9 | dropped by hand — cross-vertical duplicate: `2026-10-07_kv-cache-is-the-concurrency-ceiling` already owns this mechanism |
| The quantisation tier (4-bit vs 8-bit) decides which card class buys which model | 8 | 8 | 8 | 8 | 8.0 | dropped — the load-bearing decision is model quality rather than a purchase, and the non-arXiv anchors are thinner than the winning row set |
| Cloud egress and storage gravity as the hidden recurring cost of a remote media pipeline | 8 | 7 | 6 | 7 | 7.1 | dropped — the cloud egress price pages render client-side and no fetchable primary states the per-gigabyte rate |

## Gate result

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=6 fetched=6 sources=4 hosts=3 decision="sha1:a0d4546fb6" dedup="matched a prior artifact: 2026-10-06_fine-tune-vs-rent-by-to" window_days=180 checked_at=2026-10-27T19:34:31+00:00 -->
<!-- evergreen-gate:end -->
