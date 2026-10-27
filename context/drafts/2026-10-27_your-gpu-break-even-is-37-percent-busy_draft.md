---
title: "Your GPU Break-Even Is 37% Busy"
vertical: nhil_infrastructure_ops
persona: it_ops_leader
one_big_thing: "The cost per token of a GPU you own or rent is not set by the price list but by the shape of the work, which moves the output rate 22.8 times on identical hardware — so the buy-versus-rent call turns on the token rate your traffic really holds and the share of the month the box can run at it."
date: 2026-10-27
slug: your-gpu-break-even-is-37-percent-busy
archetype: evergreen
evergreen: true
---

<!-- lead -->
One graphics processing unit (GPU) card, one eight-billion-parameter model, one hourly bill, and an output rate that swung by 22.8 times when only the work changed. On Microsoft's own test, an H100 card running Llama 3.1 8B under vLLM served about 6,067 output tokens a second on a chat-shaped mix and about 266 on a code-shaped one [1]. Rent that card at the listed $3.99 an hour and the hour costs $0.18 per million output tokens in the first case and $4.17 in the second [2]. Claude Haiku 5.5, the tier its maker sells for classification, extraction and routing, asks $0.50 for that million — which puts the chat-shaped box's break-even at 37% of the month held busy at its tested rate [3].

That one division is my argument. The price lists have met in the middle. The workloads have not, and almost no buy-or-rent case I sit in carries the sum.

<!-- tension -->

## The big picture:

The part I keep circling is why the fight moved from price to throughput at all: the two price lists now sit within a few times of each other. The hosted tier is sold for "high-volume, latency-sensitive tasks such as classification, extraction, and routing", which is the work a tuned eight-billion-parameter model does [3]. So the live question is not which side is cheaper per token. It is how many tokens an hour the box turns out, and that number belongs to the work rather than the vendor.

Making tokens is also a memory job before it is a sums job. A language model answers by re-reading the keys and values it has already worked out, and long prompts fill that store until the card spends its time moving data instead of multiplying [1]. That is what splits the two rows of one table: same card, same model, same serving code, and a 22.8 times gap in output.

The other columns of that test show the same thing from the queue. In the code row the card still took in prompts at about 22,269 tokens a second, but gave back only 266 and left 111 requests waiting [1]. Work came in faster than the model could answer, which is the normal state of a busy estate. A reader who plans from the chat row is planning for a quiet one.

## By the numbers

- **$0.18 against $0.50 — the busy case:** a card rented at $3.99 an hour and held at 6,067 output tokens a second yields 21.8 million tokens an hour, so 18 cents per million against the hosted tier's 50 cents [1][2][3].
- **$4.17 — the same card on code-shaped prompts:** at 266 tokens a second the same hour yields 0.96 million tokens, which is 8.3 times the hosted price, and no amount of running time fixes it [1][2][3].
- **37% — the duty the chat box needs:** the share of the month it must hold that rate to beat the hosted tier; a quarter of an administrator's time, $24,782 a year at the 2025 median wage, lifts the bar to 62% [2][3][5].
- **$1,175 — one kilowatt for a year:** the 2025 commercial average of 13.41 cents a kilowatt hour, against $34,952 for a year of the rented card, which says power is not the line that settles this [2][4].

<!-- tactical-insight -->

## What I'd watch:

- **The profile:** the two inputs that decide this are how many requests arrive at the same moment and how long the prompts are against the answers, and both come from a trace rather than a spec sheet. Teams that measure them price the box right; teams that do not end up arguing about list rates.
- **The spare card:** a second card for failover doubles the hourly line, and every break-even duty in this piece roughly doubles with it [2]. The hosted tier folds that spare into its price already.
- **The peak-shaving shape:** the box for the steady base load and the hosted tier for the burst is what keeps a card busy, and busy is the only lever that moves the sum.
- **The repricing:** both sides of the division move. The rental list and the small-tier price list are the two lines to re-read each planning cycle, because either one can put the cross-over somewhere new [2][3].

<!-- nuanced-takeaway -->

## The catch

The test is a vendor lab result. One card, one model, named prompt files and a fixed request rate, run on a dedicated cloud card — a measure of a ceiling, not of a hall a reader owns [1]. My read of the chat row is that it holds the card at high concurrency, so it is not what one user sees, and a team that plans response times from it will be let down. It is a fair input for cost and a poor one for speed.

The quality side is the weaker leg. An eight-billion-parameter open model is not the same tool as a hosted small tier, and the sum above holds only where the open model clears the bar on the reader's own test set [3]. Where it does not, the hosted price is buying skill, not tokens.

Then there is the state of the rate itself. The community-cloud figure carries no service agreement, dedicated or reserved cards cost more, and every break-even duty rises with the rate [2]. Add a quarter of one administrator's time, $24,782 a year [5], and the chat-shaped bar moves to about 62%, which is a box that has to be truly busy rather than nominally on.

Power cuts the other way, which is worth saying in a vertical that spends this much time on it. One kilowatt held for a full year costs about $1,175 at the 2025 commercial average [4], against $34,952 for a year of the same rented card [2]. The meter decides the hall. It does not decide this call, and a business case that leans on power savings to justify an inference box is leaning on the wrong number.

When the work has to sit inside a confidential enclave, the tax lands on top of all of it: [an enclave overhead measured at 62.8%](/enclave-overhead-62-percent-not-4/) is charged against the same token rate, so a break-even worked out on plain hardware understates the duty an enclave needs.

<!-- tldr -->

## At a glance

- **The Big Shift:** A GPU's cost per token stopped being a property of the card or the price list. It is set by the shape of the work, which moves the output rate by more than twentyfold on the same hardware, and by how much of the month the machine is truly working.
- **Why It Matters:** Buy-or-rent calls get made against headline test rates that internal work rarely holds, so a box bought on the vendor's best row can cost several times the hosted price it was meant to beat.
- **What I'd Watch:** the measurements that decide whether a reservation earns its keep, and why none of them come off a price list.
  - **The profile:** requests arriving at the same moment, and prompt length against answer length, which together set the rate a box can hold.
  - **The duty:** the share of the month a box runs at that rate, which is what turns an hourly price into a cost per token.
  - **The spare:** the second card a production estate needs, which doubles the hourly line and the duty needed to justify it.
- **The Catch:** the test is a lab ceiling at high concurrency, the open model may not match the hosted tier on quality, and the rental rate carries no service agreement — so the cross-over is something a team measures on its own traffic, never a number taken from a vendor page.

## Sources
[1] Microsoft Azure High Performance Computing Blog — "Inference performance of Llama 3.1 8B using vLLM across various GPUs and CPUs", Cormac Garvey, updated 26 August 2025. https://techcommunity.microsoft.com/blog/azurehighperformancecomputingblog/inference-performance-of-llama-3-1-8b-using-vllm-across-various-gpus-and-cpus/4448420
[2] Runpod — GPU cloud pricing (community cloud list rates, retrieved 27 October 2026). https://www.runpod.io/pricing
[3] Anthropic — "Pricing" (Claude API model price table, retrieved 27 October 2026). https://docs.claude.com/en/docs/about-claude/pricing
[4] U.S. Energy Information Administration — "Prices and factors affecting prices" (Electricity explained, 2025 annual averages). https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
[5] O*NET OnLine — 15-1244.00 Network and Computer Systems Administrators (2025 wage data). https://www.onetonline.org/link/summary/15-1244.00
