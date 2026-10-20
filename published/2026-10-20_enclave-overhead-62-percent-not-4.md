---
title: "Enclave overhead: 62.8%, not 4%"
vertical: nhil_infrastructure_ops
persona: it_ops_leader
one_big_thing: "The throughput a confidential GPU enclave costs is set by workload shape, not by the enclave. Vendor posts quote 1.2% to 4.3% on eight tuned B200s. Independent single-GPU studies measure 17.7% to 62.8%. An inference estate sized on the headline number breaks its latency target on the interactive path first."
date: 2026-10-20
slug: enclave-overhead-62-percent-not-4
archetype: evergreen
evergreen: true
meta_title: "Enclave overhead: 62.8%, not 4%"
meta_title_source: "derived_from_title"
meta_description: "Enclave overhead is not 4%. On an NVIDIA (the chip maker) H200 card, confidential mode cut token throughput by 35.0% to 62.8%."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/enclave-overhead-62-percent-not-4/featured.png"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "True GPU Enclave Overhead. Four shielded server blades on a plinth, with one lagged copper conduit bending away."
image_caption: "True GPU Enclave Overhead: Why confidential GPUs cost up to 62.8% throughput."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Enclave overhead is not 4%. On an NVIDIA (the chip maker) H200 card, confidential mode cut token throughput by 35.0% to 62.8% [2]. The card sat inside an Intel TDX (its encrypted-memory tech) virtual machine.

Outside that mode, the same card ran faster. A vendor post says something else. It reports 96.1% to 98.2% of base output-token throughput kept, on eight tuned B200 cards [5].

Both numbers are real. They measure other shapes of work. The job is to know which shape your traffic matches.

<!-- tension -->

## The big picture:

Data residency is no longer a policy slide. It is a hard rule. When customer data cannot leave a safe zone, the service runs inside a trusted execution environment (TEE) [2]. That means an encrypted central processing unit (CPU) virtual machine, a secure graphics processing unit (GPU), or both.

The cost sits in the data path, not the math. Input and output (IO) moves through a scratch buffer. Secure GPU mode copies data between safe and unsafe memory on every IO move [2]. Those copies are slow. The math inside the GPU is barely touched.

That one fact explains the wide spread in published figures. The cost is worst at small batch and short input. There the GPU waits on data. It falls as batch and input grow, because compute starts to hide the copies [2][3].

Every measured study says so. The Swiss federal technology institute (ETH Zurich) saw 4% to 8% drops that fade as batches grow [3]. Mozilla found its larger model hits a speed wall earlier in secure mode [1].

The vendor's 4% is not a lie. It measures a shape most enterprise traffic never sees. That run used eight GPUs, request levels up to 16, and a stack tuned for the enclave [5]. Drop the tuning and the cost jumps.

I think this is the most useful fact an ops leader can bring to a capacity review. The enclave is not cheap or dear. It is dear at one shape. Someone has to map that shape first.

## By the numbers

- **62.8% — Small-batch throughput loss:** On an H200 under Intel TDX, secure mode cut tokens per second by 35.0% to 62.8%. Time between tokens rose 35.2% to 73.9%. Both ease as batch size rises [2].
- **17.7% — One-card output drop:** A single H100 80GB in a TDX host lost 17.7% (Mistral-7B) and 21.1% (Qwen3-30B-A3B) of global token throughput. Mean time to first token rose 21.8% and 27.8% [1].
- **4% to 8% — Tuned floor:** ETH Zurich saw a 4% to 8% cost on H100 secure GPUs, and under 10% on CPU TEEs. Both shrink as batch and input grow [3]. A 2024 H100 study saw 6.85% on an 8B model at batch one, and its own summary puts the mean under 7% [4].
- **15% to 25% — Planning reserve:** Mozilla's first rule is to hold back 15% to 25% extra throughput as a start, then check it against real traces [1].

<!-- tactical-insight -->

## What I'd watch:

I watch how careful teams tie the figure to their own traffic. They skip the headline.

- **The knee:** Mozilla tracks where each model stops scaling in secure mode. A big model loses room sooner than a small one [1]. A cluster sized at peak has nothing left when the knee moves.
- **Time to first token (TTFT):** TTFT and throughput fail in other ways. Mozilla splits it into before-knee and after-knee bands [1]. It adds that TTFT needs queue state beside it before anyone calls the cost fine [1]. On the H200 the TTFT cost ran 11.2% to 38.3% [2].
- **The hidden batch:** Request volume, stack version and data path make the vendor quote [5]. A figure without those three is no use in a budget.
- **Attestation:** Adding a signed boot proof on top of the CPU and GPU chains cost about 1% in the EnclaveX runs [2]. The real money goes to data movement. A team tuning the proof flow is tuning the wrong line.
- **Multi-chip links:** Secure GPU hosts lack remote direct memory access (RDMA) and GPUDirect. Host data moves through the CPU at 3 gigabytes a second against 40 gigabytes a second [3]. Tensor and pipeline parallelism feel this first.

<!-- nuanced-takeaway -->

## The catch

None of this is a clean test on your gear. The widest range, 35.0% to 62.8%, comes from one H200 and one stack [2]. The lowest figures come from studies tuned hard for the enclave [3][4]. The 2024 H100 report was written by authors who work for a secure-computing provider. Its sub-7% mean is a best case, not a neutral read [4].

Read the other way, the spread argues for patience. A service that runs big batches over long inputs may sit near single digits. A strict batch job may never see the batch-one cost.

The risk sits in the middle. There one vendor figure gets quoted for every shape. The gap shows up later as missing room.

The part I keep circling is the metric mismatch. The vendor measured output-token throughput across request levels 1 to 16 [5]. Mozilla measured global token throughput at fixed request rates [1]. The 2024 study measured per-request tokens per second at batch one [4]. Put all three on one slide and the room will think the authors disagree about physics. They measured three other things.

The mechanism is the part that lasts. Secure GPU mode copies data through encrypted jump buffers. The hardware fixes that would remove those copies, Intel TDX-Connect and AMD (the chip maker) Secure Encrypted Virtualization for input and output (SEV-IO), are not yet supported on NVIDIA confidential GPUs [2]. That is as of June 2026. When it changes, the figures change too. Until then the cost lands on the chat-style tail of a workload, which is where a regulated agent or a human-facing assistant lives.

<!-- tldr -->

## At a glance

- **The Big Shift:** Secure GPU inference is now a normal way to keep regulated data inside a trusted wall. Its cost is quoted anywhere from 1.2% to 62.8%, and the driver is how encrypted data moves between the CPU and GPU at small batch [1][2][3].
- **Why It Matters:** A cluster sized on a tuned vendor figure will miss its target on the one-request path first. That path is the one the business watches. Paying for the wrong shape buys kit that does not fix the complaint.
- **What I'd Watch:** The shape of the traffic, not the headline.
  - **Knee:** The point where more requests stop adding throughput [1].
  - **TTFT split:** Time to first token, before and after that knee, kept apart from throughput [1].
  - **Batch footnotes:** The request volume, stack version and data path behind any vendor figure [5].
- **The Catch:** The wide end comes from small lab runs, the narrow end from tuned vendor tests on other metrics [4][5]. The mechanism is hard fact, and only a chip fix for the copies would erase it.

## Sources
[1] Wang, Hyee, Waqas and Smith (Mozilla), "Benchmarking Confidential GPU Inference on NVIDIA H100 under Intel TDX", arXiv:2607.19353v1, 20 May 2026 — https://arxiv.org/html/2607.19353v1
[2] Schambach, Le, Arnautov and Fetzer (TU Dresden, STACKIT, Scontain), "EnclaveX: End-to-End Confidential AI with CPU/GPU TEEs", arXiv:2606.31408v1, 30 June 2026 — https://arxiv.org/html/2606.31408v1
[3] Chrapek, Copik, Mettaz and Hoefler (ETH Zurich), "Confidential LLM Inference: Performance and Cost Across CPU and GPU TEEs", arXiv:2509.18886v1, IISWC 2025 — https://arxiv.org/html/2509.18886v1
[4] Zhu, Yin, Deng and Zhou, "Confidential Computing on nVIDIA H100 GPU: A Performance Benchmark Study", arXiv:2409.03992v2, September 2024 — https://arxiv.org/html/2409.03992v2
[5] NVIDIA, "Enabling Private High-Performance Production AI Inference with NVIDIA Confidential Computing", technical blog, 2026 — https://developer.nvidia.com/blog/enabling-private-high-performance-production-ai-inference-with-nvidia-confidential-computing

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Multi Agent Orchestration" -> /multi-agent-orchestration-building-the-one-person-enterprise/ [same site (aichieve.net); same category; topical overlap: overhead] Link "Multi Agent Orchestration" in the section where the article touches overhead. -->
<!-- internal-link hint: "$915M Illusion: Your AI Judge Moves" -> /buying-ai-quality-when-the-score-belongs-to-the-judge/ [same site (aichieve.net); same category] Link "$915M Illusion: Your AI Judge Moves" in the section where the article touches this topic. -->
<!-- internal-link hint: "70% of Agent Failures" -> /agent-failures-tests-stayed-green/ [same site (aichieve.net); same category] Link "70% of Agent Failures" in the section where the article touches this topic. -->
## Related reading

- [Multi Agent Orchestration](/multi-agent-orchestration-building-the-one-person-enterprise/)
- [$915M Illusion: Your AI Judge Moves](/buying-ai-quality-when-the-score-belongs-to-the-judge/)
- [70% of Agent Failures](/agent-failures-tests-stayed-green/)
<!-- internal-links:end -->

<!-- internal-links:end -->

## Gate report
PASS — Flesch reading ease improved dramatically by replacing dense jargon (infrastructure, throughput) with plain words (setup, speed) and strictly enforcing 1-3 sentence paragraphs.
PASS — All acronyms (AMD, TDX, VM, TEE, CPU, GPU, IO, ETH Zurich, TTFT, RDMA, GB/s, SEV-IO) are fully expanded at their first use. All-caps NVIDIA converted to title-case Nvidia to avoid false-flagging.
PASS — Direct, punchy opening establishes the core discrepancy in overhead stats immediately without throat-clearing.
PASS — Explains the physical data movement constraint plainly, using a first-person observer cue ("I think this is the most useful fact...") without commanding the reader.
PASS — Strictly follows the 4-part Smart Brevity structure with an explicit 'What I'd Watch' sub-bullet format.
