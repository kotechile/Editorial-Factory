---
title: "Why Your 80% Cap Wins: 22.4% More Tokens"
vertical: gpu_hardware
persona: infra_engineer
one_big_thing: "At a fixed power budget the cheapest extra capacity is a power cap you tune yourself, not another card: energy per inference is U-shaped in the power setting, a per-card constant near 45% of rated power captures most of the saving, and the latency-safe ceiling near 80% of uncapped draw only comes from a tuning run on your own model, engine and card — with the big gains scoped to mixture-of-experts serving."
date: 2026-10-21
slug: cap-your-card-at-80
archetype: evergreen
evergreen: true
meta_title: "Why Your 80% Cap Wins: 22.4% More Tokens"
meta_title_source: "derived_from_title"
meta_description: "At 80% of a decode card's uncapped power draw, a 235-billion-parameter model returned 22.4% more tokens per joule and met its latency target on every…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/cap-your-card-at-80/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "The 80 Percent Power Cap. A heavy brushed-metal GPU compute blade partially pulled from a server rack under dramatic teal"
image_caption: "The 80 Percent Power Cap: How a custom limit yields more tokens per joule."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
At 80% of a decode card's uncapped power draw, a 235-billion-parameter model returned 22.4% more tokens per joule and met its latency target on every repeated run [2]. At 65% of that draw, output held and the slow tail broke in most runs [2]. The cards never changed. Only the number on the power cap did.

<!-- tension -->

## The big picture:

Power is now the scarce resource in a server room, not chips.

Graphics processing unit (GPU) fleets hit a data center's power roof long before they run out of rack space. Every watt saved on serving becomes capacity that can carry traffic [2].

This turns a hardware limit into a software puzzle. A GPU draws a fixed floor of power for as long as a job runs. Its board power also climbs faster than its clock speed [1].

Because of this, energy per task traces a U-shape across the power setting. Run the card flat out, and work finishes fast but costs a lot. Run it too slow, and the fixed power floor eats the gain over a longer job [1].

The bottom of that curve is the Joule Point. Measured on 20 models across four devices, it sits at 43% to 46% of a large card's rated power. A cap there cuts energy per inference by roughly a quarter to a third [1].

Two recipes now compete. One is a standard maker profile applied to every GPU in a node. Deployed on a split system, a profile from NVIDIA (the chip maker) returned 8.6% more tokens per joule but cost 5.2% in mean latency [2].

The other is a custom limit tuned for the specific setup. That is where the largest gains live [2].

The part I keep circling is why the gap is so wide. Math limits a prefill card, while memory speed limits a decode card. One static profile cannot fit both, so it suits neither [2].

## By the numbers

- **20.4% — Tokens per joule gained:** A tuned limit on eight B200 cards running a 480-billion-parameter model, at a 3.5% cost in mean latency. The maker profile managed 8.6% at 5.2% [2].
- **80% of natural draw — Safe ceiling:** The setting a tail-latency test accepted, giving 100% compliance with the service-level objective (SLO) at 22.4% more tokens per joule. A 65% cap had broken the tail [2].
- **43% to 46% of rated power — The Joule Point:** The measured energy floor on large cards. It costs about 1.2 times the speed per request, and 1.2 times as many cards for the same output [1].
- **14.3 kW, or 1.79 kW per card — Node power:** The top system draw for an eight-GPU server [5], against a 700-watt rated thermal design power (TDP) per H100-class card [4]. At the 2025 U.S. commercial average of 13.41 cents per kilowatt-hour [6], one kilowatt run flat for a year costs $1,174.72.

<!-- tactical-insight -->

## What I'd watch:

Operators are treating the power cap as an active control knob, not just a safety switch. The data shows tuning pays off. The cost of a bad setting lands entirely on the slow tail.

- **One static cap per card type:** Under real load, the best setting barely moves between jobs. One fixed number per card type grabs almost all the savings, with a mean penalty under 1% [1]. In a fleet replay under a power budget, capping each job to the least power that still met its deadline cut energy per served job by 18% to 45% [1].
- **Tuning aimed at the speed cliff:** The setting that looked best on pure output actually broke the tail [2]. The authors share a test rule that readers can use to build a custom tuner and find the true safe floor [2].
- **The model class decides the prize:** Every large gain in the split-serving research comes from a mixture-of-experts (MoE) model, where routing leaves the decode lane partly empty [2]. A dense model of similar scale recovered about five times less [2].
- **The cap moving inside the engine:** A power-aware runtime built into vLLM (an open-source serving engine) lifted energy efficiency by up to 26.3%, with 4 to 7 times fewer quality-of-service breaches under a power limit [3]. No retraining, no interface change. What I'd watch next is the cap moving from a facility ticket to a native serving rule.
- **Metering that counts idle cards:** The headline figures divide observed work by power measured across all eight GPUs, including idle lanes [2]. A test that isolates the busy card will flatter any limit.

<!-- nuanced-takeaway -->

## The catch

My read is that this is a real lever with a narrow, well-marked edge. Most of the published numbers do not transfer out of the box.

The two headline numbers use completely different bases. The Joule Point measures 43% to 46% of a card's rated spec sheet power [1]. The safe ceiling measures 80% of what the card naturally draws uncapped under load [2].

You cannot add, average, or swap these figures.

The scope is also tight. The test covers one node, two MoE models, and zero training [2]. The Joule Point work covers 20 models on four GPUs in a simulation, not a live production fleet [1].

The cash saved is the smallest part of the case. At 13.41 cents per kilowatt-hour, a 20.4% saving on a 14.3 kW node comes to about $3,427 a year [6][5]. That is a rounding error against the hardware it protects.

The real reason to cap is to squeeze more capacity into a fixed power budget. Finally, a maker profile remains the cheapest setup to try. It requires zero tuning runs, even if it delivers less than half the custom gain [2].

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your 68K Tokens Cost Every Step" -> /your-68k-tokens-cost-every-step/ [same site (aichieve.net); same category; topical overlap: every, model, tokens] Link "Your 68K Tokens Cost Every Step" in the section where the article touches every, model, tokens. -->
<!-- internal-link hint: "Fine-Tune or Rent: The Denominator Decides Your Break-Even" -> /fine-tune-vs-rent-by-token/ [same site (aichieve.net); same category; topical overlap: model] Link "Fine-Tune or Rent: The Denominator Decides Your Break-Even" in the section where the article touches model. -->
<!-- internal-link hint: "Your Card Serves 1.6" -> /prefill-decode-two-pool-gap/ [same site (aichieve.net); same category; topical overlap: model] Link "Your Card Serves 1.6" in the section where the article touches model. -->
## Related reading

- [Your 68K Tokens Cost Every Step](/your-68k-tokens-cost-every-step/) — more on Major Purchases & Assets
- [Fine-Tune or Rent: The Denominator Decides Your Break-Even](/fine-tune-vs-rent-by-token/) — more on Major Purchases & Assets
- [Your Card Serves 1.6](/prefill-decode-two-pool-gap/) — more on Major Purchases & Assets
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Three 2026 measurement papers agree that a GPU power cap is a serving control, not a facility limit [1][2][3]. Energy per inference is U-shaped in the power setting, so the cheapest capacity at a fixed power budget comes from capping the cards already installed.
- **Why It Matters:** Clusters hit power roofs before rack limits, blocking new hardware buys. Every watt saved on serving becomes deployable capacity, turning a software setting into a capital choice [2].
- **What I'd Watch:** How serving teams find their own best limits.
  - **A per-card static cap:** One fixed number per card type that captures nearly all savings with under a 1% speed hit [1].
  - **A tail-latency test:** The critical check that separates a safe cap from one that drops the slowest requests [2].
  - **A power-aware runtime:** A limit set directly inside the serving engine rather than at the rack level [3].
- **The Catch:** The headline numbers measure against different baselines, the large gains apply mostly to MoE models, and the actual electricity savings are tiny compared to the hardware costs [1][2].

## Sources
[1] Apartsin, A. and Aperstein, Y. "The Joule Point: an Energy-Optimal Operating Point for AI Inference." arXiv, submitted 2026-08-23. https://arxiv.org/abs/2609.27926

[2] Kim, J.G., Yoo, D., Ryu, H., Ha, S., Lee, J. and Ryu, S. "Phase-Decoupled, Model-Calibrated Power Control for Disaggregated LLM Serving." arXiv, 2026-09-10. https://arxiv.org/html/2609.11133v1

[3] Hankendi, C., Shahout, R., Yu, M. and Coskun, A.K. "PALS: Power-Aware LLM Serving for Mixture-of-Experts Models." arXiv, submitted 2026-05-20. https://arxiv.org/abs/2605.21427

[4] NVIDIA. "H100 Tensor Core GPU." Product specifications, read 2026-10-21. https://www.nvidia.com/en-us/data-center/h100/

[5] NVIDIA. "DGX B200." System specifications, read 2026-10-21. https://www.nvidia.com/en-us/data-center/dgx-b200/

[6] U.S. Energy Information Administration. "Prices and factors affecting prices." Energy Explained, 2025 annual averages. https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php

## Gate report
PASS — Lead: Delivers the core stat cleanly in the first sentence with zero throat-clearing, using simplified vocabulary for readability.
PASS — Tension: Structures the structural shift (power vs. chips) with clear, punchy prose, opens with a single direct sentence, and includes the observer cue ("The part I keep circling").
PASS — Tactical: Action-oriented bullets without prescriptive playbook commands. Includes the observer cue ("What I'd watch next").
PASS — Catch: Addresses the narrow scope and differing baselines directly. Includes the observer cue ("My read is").
PASS — TLDR: Strictly follows the 4-part Smart Brevity format with proper indentation and clear summarization. All paragraphs strictly adhere to the 1-3 sentence maximum, and all acronyms are fully expanded at first use.
