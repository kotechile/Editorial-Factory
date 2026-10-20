---
title: "Enclave overhead: 62.8%, not 4%"
vertical: nhil_infrastructure_ops
persona: it_ops_leader
one_big_thing: "The throughput a confidential GPU enclave costs is set by workload shape, not by the enclave. Vendor posts quote 1.2% to 4.3% on eight tuned B200s. Independent single-GPU studies measure 17.7% to 62.8%. An inference estate sized on the headline number breaks its latency target on the interactive path first."
date: 2026-10-20
slug: enclave-overhead-62-percent-not-4
archetype: evergreen
evergreen: true
---

<!-- lead -->
Enclave overhead is not 4%. On an NVIDIA (the chip maker) H200 inside an Intel TDX (Trusted Domain Extensions) confidential VM, confidential mode cost 35.0% to 62.8% of token throughput. The same GPU ran faster outside that mode [2]. A vendor post tells your platform team a different story. It reports "96.1% to 98.2% of baseline output-token throughput" kept, with 1.2% to 4.3% extra latency per token, measured on eight B200 GPUs [5]. Both numbers are real. They measure different workloads. Your job is to know which one your traffic looks like.

<!-- tension -->

## The big picture:

Data residency stopped being a slide in a policy deck. It is now a hardware constraint. When customer data or model weights cannot leave a trusted boundary, the inference service has to run inside a trusted execution environment (TEE). That means an encrypted central processing unit (CPU) virtual machine, a confidential graphics processing unit (GPU), or both [2]. This is a normal deployment path now.

The cost sits in the data path, not the math. Input and output (IO) moves through an encrypted buffer. Confidential GPU mode "encrypts cGPU IO over bounce buffers between the CVM and the cGPU", so "every IO requires extra copies between trusted and untrusted memory" [2]. The arithmetic inside the GPU is barely touched. The transfers slow it down.

That one fact explains the wide spread in published numbers. The penalty is worst at small batch and short input. There the GPU waits on data. The penalty shrinks as batch and input grow, because compute starts to cover the copies [2][3].

Every measured study says this in its own words. EnclaveX's overheads "tend to decrease with increased batch size" [2]. the Swiss federal technology institute (ETH Zurich) saw "throughput penalties of 4–8% that diminish as batch and input sizes grow" [3]. Mozilla's single-GPU study found its larger model "reaches its saturation knee earlier under confidential mode" [1].

The vendor's 4% is not a lie. It is a measurement of a shape most enterprise traffic never reaches. It used eight GPUs, concurrency of 1 to 16, and a framework tuned for the enclave [5]. That run moved token readback to an asynchronous worker and took pageable memory instead of pinned [5]. Remove the tuning, the eight-GPU run or the concurrency, and the figure moves.

I think this is the most useful thing an ops leader can carry into a capacity review this year. The enclave is not cheap or expensive. It is expensive at one shape. Someone has to know which shape the business runs.

## By the numbers

- **62.8% — Tokens per second, small batch:** On an H200 under Intel TDX, confidential mode cost 35.0% to 62.8% in tokens per second and 35.2% to 73.9% in time between tokens. Both eased as batch size rose [2].
- **17.7% — Global throughput, one H100:** A single H100 80GB in a TDX instance lost 17.7% (Mistral-7B) and 21.1% (Qwen3-30B-A3B) of global token throughput. Average time to first token rose 21.8% and 27.8% [1].
- **4% to 8% — The tuned floor:** ETH Zurich measured 4–8% on H100 confidential GPUs, and under 10% for CPU TEEs, both shrinking with batch and input size [3]. A 2024 H100 study put its average near 6.85% [4].
- **15% to 25% — The planning reserve:** The Mozilla study's first rule is to "reserve 15–25% additional throughput capacity as an initial planning heuristic", then check it against real traces [1].

<!-- tactical-insight -->

## What I'd watch:

The teams that get this right do not argue about the headline figure. They tie the measurement to their own traffic.

- **The saturation knee, not peak throughput:** Mozilla suggests measuring where each model stops scaling under confidential mode. A larger model can lose concurrency headroom before a smaller one does [1]. A cluster sized at peak has nothing left when that knee moves.
- **Time to first token (TTFT) on its own line:** TTFT and throughput fail in different ways. Mozilla splits TTFT into pre-saturation and post-saturation regions. It also warns that TTFT needs throughput and queue state beside it before anyone calls the overhead good or bad [1]. On the H200, the TTFT penalty ran 11.2% to 38.3% [2].
- **The batch size behind any vendor figure:** The concurrency band, the framework version and the data path belong in the quote. A number without those three is not a capacity input [5].
- **Attestation cost, which is not the problem:** Adding an application-level attestation on top of the CPU and GPU chains cost about 1% in the EnclaveX runs [2]. The money goes to data movement. An architect who tunes the attestation flow is tuning the wrong line.
- **Multi-GPU collectives, where the floor drops out:** Confidential GPU instances lack remote direct memory access (RDMA) and GPUDirect. Host data moves through the CPU at 3GB/s against 40GB/s in normal mode [3]. Tensor and pipeline parallelism feel this first.

<!-- nuanced-takeaway -->

## The catch

None of this is a controlled test on your estate. The widest range here, 35.0% to 62.8%, comes from one H200 pairing with one system stack [2]. The lowest numbers come from studies tuned hard for the enclave [3][4]. One of those, the 2024 H100 report, was written by authors who work for a confidential-computing provider. Its sub-7% average is a best case, not a neutral reading [4].

Read the other way, the spread argues for patience. A service that runs large batches over long inputs may sit near single digits. A residency-bound batch job may never see the batch-one penalty at all. What does not hold is the middle position. That is where one number gets quoted for both shapes, and the gap shows up later as missing headroom.

I would also flag the metric mismatch, because most comparisons here go wrong at that point. The vendor measured output-token throughput across concurrency 1 to 16 [5]. Mozilla measured global token throughput at fixed request rates [1]. The 2024 study measured per-request tokens per second at batch size 1 [4]. Put all three on one slide and the room will think the authors disagree about physics. They do not. They measured three different things.

The durable part is the mechanism. Confidential GPU mode copies through encrypted bounce buffers. The hardware fixes that would remove those copies, Intel TDX-Connect and AMD (the chip maker) Secure Encrypted Virtualization for input and output (SEV-IO), are not yet supported on NVIDIA's confidential GPUs [2]. That is as of June 2026. When it changes, the numbers change with it. Until then the penalty belongs to the data path. It lands on the interactive tail of a workload, which is where a regulated agent or a human-facing assistant lives.

<!-- tldr -->

## At a glance

- **The Big Shift:** Confidential GPU inference is now a mainstream way to keep regulated data inside a trusted boundary. Its cost is quoted anywhere from 1.2% to 62.8%, depending on who measured it. The measured studies agree on the cause. Secret data movement between the CPU and the GPU dominates at small batch and short input, then fades as compute takes over [1][2][3].
- **Why It Matters:** An inference estate sized on a tuned eight-GPU figure will miss its latency target on the batch-one path first. That path is usually the one the business watches. Buying headroom for the wrong shape pays for hardware that does not fix the complaint.
- **What I'd Watch:** The shape of the traffic, not the headline number.
  - **Saturation knee:** The concurrency level where more requests stop adding throughput. It moves earlier under confidential mode [1].
  - **TTFT split:** Time to first token, measured before and after that knee, kept apart from throughput [1].
  - **Batch in the footnote:** The concurrency band, framework version and data path behind any vendor figure [5].
- **The Catch:** The wide end of the range comes from small lab studies and the narrow end from heavily tuned ones. The metrics are not the same thing across sources [4][5]. The mechanism is durable. Every magnitude is dated, and a hardware fix for the copies would move all of them.

## Sources
[1] Wang, Hyee, Waqas and Smith (Mozilla), "Benchmarking Confidential GPU Inference on NVIDIA H100 under Intel TDX", arXiv:2607.19353v1, 20 May 2026 — https://arxiv.org/html/2607.19353v1
[2] Schambach, Le, Arnautov and Fetzer (TU Dresden, STACKIT, Scontain), "EnclaveX: End-to-End Confidential AI with CPU/GPU TEEs", arXiv:2606.31408v1, 30 June 2026 — https://arxiv.org/html/2606.31408v1
[3] Chrapek, Copik, Mettaz and Hoefler (ETH Zurich), "Confidential LLM Inference: Performance and Cost Across CPU and GPU TEEs", arXiv:2509.18886v1, IISWC 2025 — https://arxiv.org/html/2509.18886v1
[4] Zhu, Yin, Deng and Zhou, "Confidential Computing on nVIDIA H100 GPU: A Performance Benchmark Study", arXiv:2409.03992v2, September 2024 — https://arxiv.org/html/2409.03992v2
[5] NVIDIA, "Enabling Private High-Performance Production AI Inference with NVIDIA Confidential Computing", technical blog, 2026 — https://developer.nvidia.com/blog/enabling-private-high-performance-production-ai-inference-with-nvidia-confidential-computing

<!-- internal-links -->
<!-- internal-links:end -->
