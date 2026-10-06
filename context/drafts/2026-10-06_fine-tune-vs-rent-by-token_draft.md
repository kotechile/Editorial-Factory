---
title: "Fine-Tune or Rent by the Token: The Break-Even Is the Denominator"
vertical: workstation_compute_economics
persona: infra_engineer
one_big_thing: "Whether to fine-tune a model on your own hardware or keep paying per token is settled by which hosted price you put in the denominator, not by the hardware spec sheet."
date: 2026-10-06
slug: fine-tune-vs-rent-by-token
archetype: evergreen
evergreen: true
---

<!-- lead -->
Hugging Face's own quantization guide says a 33-billion-parameter model can be fine-tuned on a single graphics card with 24 gigabytes of video memory [1]. That one line reframes the decision most teams get wrong: whether to fine-tune a model you own or keep paying someone else for every token. The honest comparison is not the two hardware specs. It is the denominator you put on the hosted side.

<!-- tension -->

## The big picture:

A fine-tuned model and a rented one are priced in different units, and the units decide the answer.

Hosted inference is sold by the token. On the same October 2026 afternoon, a cheap hosted model cost 30 cents per million input tokens [3] while the top-tier hosted model cost $10 per million [2]. That is roughly a thirty-times spread for the same unit of work. I keep coming back to how little that spread shows up in the budgets teams build.

On the local side, you buy the card once and then pay for power. A card that draws 575 watts asks for a 1,000-watt system supply [5], and the US average retail price of a kilowatthour was 12.68 cents in the latest annual figures [4]. Run that card flat out for a year and the electricity is about $639, near $53 a month. That is arithmetic on the published power spec and the published price, not a vendor's forecast.

The part teams skip: the fine-tuning memory floor sits above the inference floor. Hugging Face's memory-saving method, called QLoRA (a way to fine-tune while holding the model in a compressed form), fits a 33-billion-parameter model on 24 gigabytes, and a 65-billion-parameter model on 46 gigabytes [1].

## By the numbers

- **33 billion — Fine-tuning on one 24-gigabyte card:** QLoRA fine-tunes a 33-billion-parameter model on a single 24-gigabyte card, and a 65-billion-parameter model on a 46-gigabyte one [1].
- **12.68 cents — Power price:** The US average retail electricity price per kilowatthour [4]. A 575-watt card run all year draws about 5,037 kilowatthours, near $639 of power [5][4].
- **$0.30 vs $10 — Two hosted denominators:** MiniMax M3 hosted at 30 cents per million input tokens [3], against the top-tier hosted model at $10 per million [2].
- **532 million vs 13 million — Output tokens of power:** $639 of electricity buys about 532 million output tokens at $1.20 per million [3], or about 13 million at $50 per million [2] — a 42-fold swing from the denominator alone.

<!-- tactical-insight -->

## What I'd watch:

The teams that get this right price against the cheap hosted model of the same family, not the frontier one.

- **The denominator test:** A payback sheet that drops a $10-per-million rate into the hosted column will always say "build local." The same sheet at 30 cents says "keep renting" [2][3].
- **The token mix:** Cheap hosted output tokens cost four times their input tokens [3]. A workload that writes more than it reads moves the break-even more than any hardware choice.
- **The memory floor:** 24 gigabytes reaches a 33-billion-parameter fine-tune; the 65-billion-parameter floor wants about 46 gigabytes, which most single consumer cards do not offer [1].
- **The power line:** A 575-watt card wants a 1,000-watt system supply [5], so the "free" local compute carries a power-supply constraint before it carries a bill.

What strikes me is that the rig's own electricity turns out to be the smaller number in this comparison. The bigger lever is the hosted price you chose not to beat.

<!-- nuanced-takeaway -->

## The catch

Electricity is the marginal cost, not the full one. The card, the enclosure, and the engineer's time all sit outside it.

My read: 24 gigabytes is a real fine-tuning floor, and it is a floor for the compressed path that keeps most of the quality, not a shortcut around the data problem [1]. A team with no labeled examples has nothing to fine-tune, however cheap the power gets.

The pricing side is just as slippery. The two hosted rates above are the vendors' own numbers as of October 2026, and vendors re-price on their own schedule [2][3]. The power figure is a national average, so an industrial rate or a European one tells a different story [4].

The field note behind this piece is the useful counterweight: a legal-tech team cut roughly $14,200 a month of hosted spend to about $180 a month of power by fine-tuning a small model locally [6]. That result came from a narrow task and a mountain of labeled clauses. It is the shape of the win, not a promise that every workload has one.

<!-- tldr -->

## At a glance

- **The Big Shift:** Fine-tuning a model on your own hardware is usually argued as a hardware question, but the deciding number is the hosted per-token price you compare against — 30 cents or $10 per million tokens, a thirty-times spread on the same day [2][3].
- **Why It Matters:** A local rig's marginal cost is electricity, about $639 a year for a 575-watt card at the national average power price [4][5], so a payback figure swings roughly 42-fold depending on which hosted model sits in the denominator.
- **What I'd Watch:** Whether teams price against the cheap hosted model of the same family instead of the frontier one.
  - **The denominator test:** The hosted rate you put in the comparison. A frontier rate proves build-local; a cheap open-model rate proves keep-renting [2][3].
  - **The token mix:** How much of the workload is output rather than input. Cheap hosted output tokens cost four times input [3], so the mix can outweigh the hardware.
  - **The memory floor:** The video memory a fine-tune needs. About 24 gigabytes for a 33-billion-parameter model and 46 gigabytes for a 65-billion-parameter one [1].
- **The Catch:** Electricity ignores the card's price and the labeled data a fine-tune needs, and both hosted rates are vendor prices that change on the vendor's schedule [1][2][3].

## Sources
[1] Hugging Face, "Making LLMs even more accessible with bitsandbytes, 4-bit quantization and QLoRA" — https://huggingface.co/blog/4bit-transformers-bitsandbytes
[2] Anthropic, "Claude API pricing" (top-tier model rate card, retrieved 2026-10-06) — https://www.anthropic.com/pricing
[3] Together AI, "Pricing" (MiniMax M3 rate card, retrieved 2026-10-06) — https://www.together.ai/pricing
[4] US Energy Information Administration, "Electricity Profile" (state data, 2024) — https://www.eia.gov/electricity/state/
[5] Nvidia, "GeForce 5090" product page (specifications) — https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/
[6] Editorial-factory field notes, workstation_compute_economics Anecdote 3 (internal) — context/growth_os/customer-truth.md

<!-- linkedin -->
Hugging Face's own guide says a 33-billion-parameter model can be fine-tuned on a single 24-gigabyte card. I keep coming back to what that line does to the fine-tune-or-rent question, because the hardware was never the hard part of the comparison.

Hosted inference is priced by the token, and the ladder is wide. On one October 2026 afternoon a cheap hosted model cost 30 cents per million input tokens while the top-tier model cost $10 per million, a thirty-times spread for the same unit of work.

On the local side the recurring cost is power. A card drawing 575 watts wants a 1,000-watt supply, and at the national average of 12.68 cents per kilowatthour the electricity runs about $639 a year, near $53 a month.

My read: that is the smaller number in the whole comparison. Priced against the cheap hosted tier, that $639 of electricity represents roughly 532 million output tokens a year. Priced against the top tier, about 13 million. Same rig, a 42-fold difference, decided entirely by the hosted rate you refused to beat.

I'm curious how others set that denominator. Do teams price against the frontier model, or against the cheapest open model that could do the same job? A payback figure is only as good as the number underneath it.
