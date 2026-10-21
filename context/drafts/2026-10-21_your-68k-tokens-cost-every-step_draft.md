---
title: "Your 68K Tokens Cost Every Step"
vertical: gpu_hardware
persona: infra_engineer
one_big_thing: "For an agent, the energy behind each output token is set by the bytes of private key-value history the request reads, so a session's cost per token rises with its own age — and the levers the production data actually measures are a clock on retention, a cheaper format for the retained state, and placement-aware routing, not a bigger card or a bigger batch."
date: 2026-10-21
slug: your-68k-tokens-cost-every-step
synthesis: true
sources:
  - https://arxiv.org/abs/2610.28576
  - https://arxiv.org/abs/2610.22863
meta_title: "Your 68K Tokens Cost Every Step"
meta_description: "Four live traces covering more than 121 million model calls show the median research session growing from about 10K to 68K tokens by the 30th call. A separate energy model says each new token pays for that history."
---

<!-- lead -->
By the 30th call, the median Deep Research session in Microsoft's live traces carries about 68K tokens of history. It started near 10K [2]. Four days later, a second team published an energy model with a blunt claim. The joules behind each new token are set by that same number: the private history a request reads on every step [1]. A prefix cache spares the work of reading the prompt again. It does not spare the read behind each token after that.

<!-- tension -->

## The big picture:

Every cost model for AI serving rests on two numbers. One is a price per token. The other is a price per card-hour. Both are averages. Both assume the work behind a token stays roughly fixed [1][2].

The energy paper breaks the first. It fits board-level energy per output token as a line through two byte counts and one clock: shared weights, private history, and decode time [1]. It covers three small dense models, run at BF16 (16-bit floats) on GH200 and GB300 boards.

All 374 held-out runs land within 3.73% of the energy measured on the board [1].

The residency paper breaks the second. It reads four live Microsoft traces covering more than 121 million model calls. One workload, Deep Research, issues 89% of its calls into a context that keeps growing [2]. About 80% of those context tokens come from the prefix cache [2].

That cache makes an agent cheap to start. It is also the reason the history stays in memory to be read again.

The line I keep coming back to sits in the energy paper's own accounting. Each request reads its own private history. An output that reads L records reads K bytes for each one, plus a write for its own new record [1].

That read is charged per output token, not once per request [1]. A cache hit and a fresh decode are not the same kind of event.

Put the two papers together and the unit every invoice uses stops matching the thing being bought. A session's cost per token is a function of how old the session is.

## By the numbers

- **3.73% — Energy model's worst held-out error:** the fit was checked on 374 held-out runs, across three models, on one card and on two cards in tensor parallel, on GH200 and GB300 boards [1].
- **68K tokens — Median context by call 30:** up from about 10K, in Deep Research, the workload that issues 89% of model calls. About 80% of those tokens are served from the prefix cache [2].
- **501.8 TB — Peak memory estimate:** the memory needed to hold every live session at its peak, with the public Llama-2-70B layout standing in for confidential models. Inference occupies only 5.6% of that retention time [2].
- **3.6x and 13.6% — Two levers, measured:** a one-hour idle cap cuts the memory ceiling 3.6x while the share of calls that recompute context moves from 4.07% to 4.53%. Holding an idle session's state at int4 precision (a format the paper calls multi-resolution retention) keeps recompute at 13.6%, where plain least-recently-used (LRU) eviction hits 63% [2].

<!-- tactical-insight -->

## What I'd watch:

The operators closest to this are not picking between cards. They are picking what to keep, for how long, and in what format. That is a serving-policy call, and the live numbers point to four places it shows up.

- **A clock on retention:** one hour of idle time cut the peak memory ceiling 3.6x. The share of calls forced to recompute moved only from 4.07% to 4.53% [2]. Of the levers measured, this is the cheapest, and it needs no new hardware.
- **A cheaper format for what stays:** at a tenth of the busiest hour's demand, LRU eviction forces 63% of calls to recompute. Even a clairvoyant policy needs 31%. Holding demoted int4 state brings it to 13.6% [2]. The saving is in how the state is stored, not in how much of it there is.
- **Placement as a cache decision:** when the next call lands on a different cluster, reuse falls from 89% to 29%. Treating state as local to one cluster lifts the recompute floor from 5.4% to 20.2% [2]. I'd want to know which routers hold a session in place and which treat it as a fresh request.
- **The chart nobody publishes:** measured energy rose with history in every series the energy team plotted [1]. Agent work also runs at an effective batch of one, where decode latency dominates the task [3]. So the number I watch for is joules per token at a stated history length, not one average.

<!-- nuanced-takeaway -->

## The catch

My read is that this pairing works better as a frame than as a forecast. Each half carries a real limit.

The memory numbers are an estimate built on a stand-in. The 501.8 TB (terabytes) figure uses the public Llama-2-70B layout in place of confidential models. Treat it as a shape, not a purchase order [2]. The energy fit covers three dense models between 7 and 14 billion parameters. It decodes at 16-bit precision, with full-history attention, on Hopper and Blackwell. It counts board energy only, with no host, network or building power [1].

The link between the two is my inference, not either team's finding. Neither paper measures the other's number. The energy work has no retention policy, and the residency work has no energy term [1][2]. What both support is narrower, and still useful. History length drives the private read, and that read lands on every output token.

The cache story also skips a cost. A remote cache tier left median time-to-first-token flat in one deployment. It pushed the tail at 16k tokens from 3.96 s to 17.3 s [4]. A hit only pays above 2.53 gigabytes a second. So prompts under about 17k tokens cannot beat a plain recompute, at any speed [4]. High reuse is not the same as a win.

The power side has a generation gap too. The measured result that a standard test loop is not a ceiling comes from HBM2 chips. The paper validates its model against HBM3E power on three H200 boards, for one power-heavy benchmark, not for a serving workload [5].

<!-- tldr -->

## At a glance

- **The Big Shift:** A trace of more than 121 million Microsoft model calls shows agent context growing from about 10K to a median 68K tokens by the 30th call. A separate energy model prices each new token off the private history bytes a request reads. Neither paper states the other's point. Together they say a session gets dearer per token as it ages.
- **Why It Matters:** A price per token is an average over sessions of very different ages. The fleets with the longest agent sessions carry the worst drift, and no invoice shows it. The reflex that fixes chat serving, a bigger batch, shrinks only the shared-weight term, not the per-request read.
- **What I'd Watch:** whether serving teams treat retention as a policy rather than a capacity problem.
  - **Idle clocks:** a time cap on how long a paused session's state stays in memory. One hour cut the peak ceiling 3.6x.
  - **Demoted state:** keeping idle history at int4 precision instead of evicting it, which held recompute at 13.6% against 63% for plain LRU eviction.
  - **Sticky routing:** sending the next call to the cluster that already holds the state, since reuse falls from 89% to 29% when it lands elsewhere.
- **The Catch:** the memory ceiling is an estimate that borrows another model's layout, the energy fit covers three dense 7 to 14 billion parameter models with full-history attention and counts board power only, and the link between the papers is my reading. A remote cache tier can also make the tail worse before it lifts throughput.

## Sources
[1] Niu, Sencer, Zhang, Chen. "The Token-Energy Law of LLM Decode: Active Bytes and Realized Time Account for Joules per Token." arXiv, submitted 2026-10-20. https://arxiv.org/abs/2610.28576
[2] Arya, Bari, Parayil, Simmhan, St. Amant, Rühle, Rajmohan. "Understanding KV Residency in Production-Scale Agentic LLM Workloads." arXiv, submitted 2026-10-16. https://arxiv.org/abs/2610.22863
[3] "Evaluating Inference Compute for Generative AI: A Framework for Enterprise Workloads." arXiv, submitted 2026-10-05. https://arxiv.org/abs/2610.07094
[4] "When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill." arXiv, submitted 2026-10-15. https://arxiv.org/abs/2610.21500
[5] Olgun, Galanopoulos, Kakolyris, Yüksel, Luo, Bostancı, Mutlu. "Understanding the Power Consumption of Modern High Bandwidth Memory: Experimental Analysis and Modeling Using Real HBM2 DRAM Chips." arXiv, submitted 2026-10-09. https://arxiv.org/abs/2610.14244
