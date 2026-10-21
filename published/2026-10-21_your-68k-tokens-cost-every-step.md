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
image_path: "context/assets/illustrations/your-68k-tokens-cost-every-step/featured.jpg"
image_style: "architectural_night"
image_model: "flux"
image_alt: "The Rising Cost Of Tokens. Towering server racks glowing with warm amber light in a dark blue data center hall."
image_caption: "The Rising Cost Of Tokens: Why every new output pays for the history it reads."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
An agent's cost per token rises with its own age. Every new output pays for the private history it reads on every step [1][2]. By the 30th call, the median Deep Research session in Microsoft's live traces grows from about 10K tokens to 68K [2]. A prefix cache spares the work of reading the prompt again, but it does not spare the read behind each token after that.

<!-- tension -->

## The big picture:

Every cost model for artificial intelligence (AI) serving rests on two numbers. One is a price per token. The other is a price per card-hour. Both are averages. Both assume the work behind a token stays roughly fixed [1][2].

The energy paper breaks the first assumption. It fits board-level energy per output token as a line through shared weights, private history, and decode time [1]. It covers three small dense models, run at 16-bit floats (BF16) on GH200 and GB300 boards. All 374 held-out runs land within 3.73% of the energy measured on the board [1].

The residency paper breaks the second assumption. It reads four live Microsoft traces covering more than 121 million model calls. One workload, Deep Research, issues 89% of its calls into a context that keeps growing [2]. About 80% of those context tokens come from the prefix cache [2]. Inference occupies only 5.6% of the time that state is held [2].

The part I keep circling sits in the energy paper's own numbers. Each request reads its own private history [1]. An output that reads L records reads K bytes for each one, plus a write for its own new record [1].

That read is charged per output token, not once per request [1]. Put the two papers together, and the unit every invoice uses stops matching the thing being bought.

## By the numbers

- **3.73% — Energy model error:** The worst held-out error across 374 runs, spanning three models on GH200 and GB300 boards [1].
- **68K tokens — Median context:** The context size by call 30 in Deep Research, the workload that issues 89% of model calls [2].
- **501.8 TB — Peak memory estimate:** The memory to hold every live session at its peak, using a public Llama-2-70B layout instead of the real models. Inference occupies only 5.6% of that retention time [2].
- **3.6x and 13.6% — Two levers:** A one-hour idle cap cuts the peak memory ceiling 3.6x while the share of calls that recompute moves from 4.07% to 4.53%. Holding an idle session's state at 4-bit integer (int4) precision keeps recompute at 13.6%. Plain least-recently-used (LRU) eviction forces 63% of calls to recompute [2].

<!-- tactical-insight -->

## What I'd watch:

Operators are not picking between cards; they are picking what to keep, for how long, and in what format.

- **A clock on retention:** One hour of idle time cut the peak memory ceiling 3.6x [2]. The share of calls forced to recompute moved only from 4.07% to 4.53% [2].
- **A cheaper format:** At a tenth of the busiest hour's demand, LRU eviction forces 63% of calls to recompute. Holding demoted int4 state brings it to 13.6% [2].
- **Placement as a cache decision:** When the next call lands on a different cluster, reuse falls from 89% to 29% [2]. Treating state as local to one cluster lifts the recompute floor from 5.4% to 20.2% [2].
- **Joules per token:** Measured energy rose with history in every series the energy team plotted [1]. Agent work runs at an effective batch of one, where decode latency dominates the task [3]. I'd watch for energy at a stated history length, not one average.

<!-- nuanced-takeaway -->

## The catch

My read is that this pairing works better as a frame than as a forecast. Each half carries a real limit.

The memory numbers are an estimate built on a stand-in. The 501.8 terabytes (TB) figure uses the public Llama-2-70B layout in place of confidential models [2]. The energy fit covers three dense models, 7 to 14 billion parameters each, decoding at 16-bit precision (BF16). It uses full-history attention on Hopper and Blackwell boards. It counts board energy only, and ignores host, network or building power [1].

The link between the two is my inference. Neither paper measures the other's number [1][2]. What both support is narrower: history length drives the private read, and that read lands on every output token.

The cache story also skips a cost. A remote cache tier left median time-to-first-token flat in one cluster [4]. It pushed the tail at 16K tokens from 3.96 seconds to 17.3 seconds [4]. Prompts under about 17K tokens cannot beat a plain recompute [4].

The power side has a generation gap too. The measured result that a standard test loop is not a ceiling comes from HBM2 chips. The paper then validates its model against High Bandwidth Memory 3E (HBM3E) power on three H200 boards [5]. That check is one power-heavy benchmark, not a serving workload.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Self-Hosted AI: When to Buy vs Rent GPUs" -> /self-hosted-ai-when-to-buy-vs-rent-gpus/ [same site (aichieve.net); same category; topical overlap: cost] Link "Self-Hosted AI: When to Buy vs Rent GPUs" in the section where the article touches cost. -->
<!-- internal-link hint: "CaseProof: Stop Signing $3M Warehouse Automation Deals on a…" -> /caseproof-stop-signing-3m-warehouse-automation-deals-on-a-vendors/ [same site (aichieve.net); topical overlap: cost, every] Link "CaseProof: Stop Signing $3M Warehouse Automation Deals on a…" in the section where the article touches cost, every. -->
<!-- internal-link hint: "Token Prices Hit Record Lows. Enterprise AI Bills Didn't." -> /token-price-record-low-budget-overrun/ [same site (aichieve.net); topical overlap: token, tokens] Link "Token Prices Hit Record Lows. Enterprise AI Bills Didn't." in the section where the article touches token, tokens. -->
## Related reading

- [Self-Hosted AI: When to Buy vs Rent GPUs](/self-hosted-ai-when-to-buy-vs-rent-gpus/) — more on Major Purchases & Assets
- [CaseProof: Stop Signing $3M Warehouse Automation Deals on a…](/caseproof-stop-signing-3m-warehouse-automation-deals-on-a-vendors/) — more on Business Automation & Operations
- [Token Prices Hit Record Lows. Enterprise AI Bills Didn't.](/token-price-record-low-budget-overrun/)
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** A trace of more than 121 million Microsoft model calls shows agent context growing from about 10K to a median 68K tokens by the 30th call [2]. A separate energy model prices each new token off the private history bytes a request reads [1]. Neither paper states the other's point; together they say a session gets dearer per token as it ages.
- **Why It Matters:** A price per token is an average over sessions of very different ages. The fleets with the longest agent sessions carry the worst drift. The reflex that fixes chat serving, a bigger batch, shrinks only the shared-weight term. It does not shrink the per-request read.
- **What I'd Watch:** How serving teams treat retention as a policy rather than a capacity problem.
  - **Idle clocks:** A time cap on how long a paused session's state stays in memory.
  - **Demoted state:** Keeping idle history at int4 precision instead of evicting it.
  - **Sticky routing:** Sending the next call to the cluster that already holds the state.
- **The Catch:** The memory ceiling is an estimate that borrows another model's layout, and the energy fit counts board power only [1][2]. A remote cache tier can also make the tail worse before it lifts throughput [4].

## Sources
[1] Niu, Sencer, Zhang, Chen. "The Token-Energy Law of LLM Decode: Active Bytes and Realized Time Account for Joules per Token." arXiv, submitted 2026-10-20. https://arxiv.org/abs/2610.28576
[2] Arya, Bari, Parayil, Simmhan, St. Amant, Rühle, Rajmohan. "Understanding KV Residency in Production-Scale Agentic LLM Workloads." arXiv, submitted 2026-10-16. https://arxiv.org/abs/2610.22863
[3] "Evaluating Inference Compute for Generative AI: A Framework for Enterprise Workloads." arXiv, submitted 2026-10-05. https://arxiv.org/abs/2610.07094
[4] "When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill." arXiv, submitted 2026-10-15. https://arxiv.org/abs/2610.21500
[5] Olgun, Galanopoulos, Kakolyris, Yüksel, Luo, Bostancı, Mutlu. "Understanding the Power Consumption of Modern High Bandwidth Memory: Experimental Analysis and Modeling Using Real HBM2 DRAM Chips." arXiv, submitted 2026-10-09. https://arxiv.org/abs/2610.14244

## Gate report
lead
PASS — Delivers the core takeaway immediately in the first sentence without filler, establishing the link between session age and token cost.
tension
PASS — Clearly contrasts the assumptions of standard cost models with the findings of the two papers using short paragraphs and plain language.
tactical-insight
PASS — Uses clear, bolded bullets to highlight the exact levers operators are pulling, framed as observations rather than commands.
nuanced-takeaway
PASS — Honestly presents the limitations of the data (estimates, board power only) and clearly labels the synthesis as the author's own read.
tldr
PASS — Strictly follows the 4-part Smart Brevity schema, cleanly summarizing the shift, impact, watch areas, and tradeoffs in scannable bullets.
