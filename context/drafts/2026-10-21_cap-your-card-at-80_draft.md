---
title: "Why Your 80% Cap Wins: 22.4% More Tokens"
vertical: gpu_hardware
persona: infra_engineer
one_big_thing: "At a fixed power budget the cheapest extra capacity is a power cap you tune yourself, not another card: energy per inference is U-shaped in the power setting, a per-card constant near 45% of rated power captures most of the saving, and the latency-safe ceiling near 80% of uncapped draw only comes from a tuning run on your own model, engine and card — with the big gains scoped to mixture-of-experts serving."
date: 2026-10-21
slug: cap-your-card-at-80
archetype: evergreen
evergreen: true
---

<!-- lead -->
At 80% of a decode lane's uncapped power draw, a 235-billion-parameter model returned 22.4% more tokens per joule and met its latency target on every repeated run [2]. At 65% of that same draw, output held and the slow tail broke in most runs [2]. Nothing about the cards changed between those two settings. Only the number on the power cap did.

<!-- tension -->

## The big picture:

Power is now the scarce thing in a serving cluster, not silicon. GPU fleets hit a data center's power ceiling before they run out of rack space, so every watt saved on serving becomes capacity someone can sell [2].

That turns a hardware problem into a scheduling problem. A graphics processing unit (GPU) draws a fixed floor of power for as long as a job runs, and its board power climbs faster than its clocks [1]. So energy per inference traces a U-shape across the power setting. Run the card flat out and work finishes fast and dear. Run it too slow and the fixed floor, spread over a longer job, eats the gain [1].

The bottom of that curve has a name: the Joule Point. Measured on 20 models across four devices, it sits at 43% to 46% of a large card's rated power. A cap there cuts energy per inference by about a quarter to a third [1].

Two recipes now compete. One is a vendor profile: a single setting applied to every GPU in a node. Deployed on a split prefill and decode system, a profile from NVIDIA (the chip maker) returned 8.6% more tokens per joule and cost 5.2% in mean latency [2]. The other is a setting tuned per deployment. That is where the big numbers live [2].

The part I keep circling is why the gap is so wide. A prefill card is limited by math. A decode card is limited by memory speed. One profile cannot fit both, so it suits neither [2].

## By the numbers

- **20.4% — Tokens per joule gained:** A tuned decode cap on eight B200 cards serving a 480-billion-parameter model, at a 3.5% latency cost. The vendor profile managed 8.6% at 5.2% [2].
- **80% of natural draw — Latency-safe ceiling:** The setting a tail-latency test accepted, giving 100% compliance with the service-level objective (SLO) at 22.4% more tokens per joule. A 65% cap had broken the tail [2].
- **43% to 46% of rated power — The Joule Point:** The measured energy minimum on large cards. The price is about 1.2 times slower per request, and 1.2 times as many cards for the same output [1].
- **14.3 kW, or 1.79 kW per GPU — What a node costs the room:** Top system power for NVIDIA's eight-GPU B200 server [5], against a 700 W rated thermal design power (TDP) per H100-class card [4]. At the 2025 U.S. average commercial price of 13.41 cents per kilowatt-hour [6], one kilowatt run flat for a year costs $1,174.72.

<!-- tactical-insight -->

## What I'd watch:

Operators are treating the power cap as a control knob now, not a safety limit. The evidence says the knob pays, and that the cost of turning it badly lands on the slow tail.

- **One static cap per card type as the cheap default.** Under real load the best setting barely moves between jobs, so one number per card type captures almost all of the saving, with a mean penalty under 1% [1]. In a fleet replay under a power budget, capping each job to the least power that still met its deadline cut energy per served job by 18% to 45% [1].
- **Tuning aimed at the latency cliff, not the energy minimum.** The setting that looked best on output alone was the one that broke the tail [2]. The setting that survived repeated runs came from a tail-latency test, which the authors publish as an algorithm a reader can port to a home-grown tuner [2].
- **The model class decides the size of the prize.** Every large result in the split-serving work is a mixture-of-experts (MoE) result, where routing leaves the decode lane under-loaded. A dense model of similar scale recovered about five times less [2].
- **The cap moving inside the serving engine.** A power-aware runtime built into vLLM (an open-source model-serving engine) lifted energy efficiency by up to 26.3%. It also cut quality-of-service breaches by 4 to 7 times under a power limit, with no retraining and no interface change [3]. That is the shape I'm watching: the knob stops being a facility ticket and becomes a serving setting.
- **Metering that counts the idle cards.** The headline tokens-per-joule figures divide observed work by power measured across all eight GPUs, idle lanes included [2]. A benchmark that counts only the busy card will flatter any cap.

<!-- nuanced-takeaway -->

## The catch

My read is that this is a real lever with a narrow, well-marked edge. Most of the published numbers do not transfer as written.

The two headline percentages use different bases. The Joule Point is a share of a card's rated power: 43% to 46% of the number on the spec sheet [1]. The latency-safe ceiling is a share of what the card draws uncapped under load: near 80% [2]. Rated power and natural draw are not the same quantity, so the two numbers cannot be added, averaged or swapped.

The scope is one node, two MoE models and no training. The authors say so themselves, and they make no dense-model claim [2]. The Joule Point work covers 20 models on four GPUs in a simulation, not a production fleet [1].

The money is the small half of the case. At 13.41 cents per kilowatt-hour, a 20.4% saving on a 14.3 kW node comes to about $3,427 a node-year [6][5]. That is a rounding error against the hardware it protects. The reason to cap is capacity inside a power budget, not the power bill.

And a vendor profile is still the cheapest thing to try, even though it delivered less than half the tuned gain [2]. It costs one setting and no tuning run.

<!-- tldr -->

## At a glance

- **The Big Shift:** Three 2026 measurement papers agree that a GPU power cap is a serving control, not a facility limit. Energy per inference is U-shaped in the power setting, so the cheapest capacity at a fixed power budget comes from capping the cards already installed [1][2][3].
- **Why It Matters:** A cluster that hits its power ceiling before its rack space cannot add capacity by buying cards. Every watt saved on serving turns into sellable output, which makes a scheduler setting a capital decision [2].
- **What I'd Watch:** How serving teams find their own setting.
  - **A per-card static cap:** One number per card type, capturing nearly all of the saving at a mean penalty under 1% [1].
  - **A tail-latency test:** The check that separates a cap which holds output from one that quietly breaks the slowest requests [2].
  - **A power-aware runtime:** A cap set inside the serving engine rather than at the rack, where the largest measured gains appear [3].
- **The Catch:** The two headline percentages measure against different baselines, the big gains are MoE-only, and the electricity saved is trivial next to the hardware. The argument is capacity at fixed power, not the power bill [1][2].

## Sources
[1] Apartsin, A. and Aperstein, Y. "The Joule Point: an Energy-Optimal Operating Point for AI Inference." arXiv, submitted 2026-08-23. https://arxiv.org/abs/2609.27926

[2] Kim, J.G., Yoo, D., Ryu, H., Ha, S., Lee, J. and Ryu, S. "Phase-Decoupled, Model-Calibrated Power Control for Disaggregated LLM Serving." arXiv, 2026-09-10. https://arxiv.org/html/2609.11133v1

[3] Hankendi, C., Shahout, R., Yu, M. and Coskun, A.K. "PALS: Power-Aware LLM Serving for Mixture-of-Experts Models." arXiv, submitted 2026-05-20. https://arxiv.org/abs/2605.21427

[4] NVIDIA. "H100 Tensor Core GPU." Product specifications, read 2026-10-21. https://www.nvidia.com/en-us/data-center/h100/

[5] NVIDIA. "DGX B200." System specifications, read 2026-10-21. https://www.nvidia.com/en-us/data-center/dgx-b200/

[6] U.S. Energy Information Administration. "Prices and factors affecting prices." Energy Explained, 2025 annual averages. https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
