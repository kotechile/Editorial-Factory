---
title: "Your 44x Saving Breaks When Idle"
vertical: enterprise_build_vs_buy
kind: news
persona: eng_leader
one_big_thing: "Amazon's engineers cut a ticket-classification bill from $22,200 to about $500 per million tickets by swapping a frontier API model for a self-hosted decision model — but the cheap side is a rented GPU-hour, so the saving is a utilisation bet that breaks even at about 63 tickets an hour and only reproduces the published figure at roughly half the box's capacity."
date: 2026-11-11
slug: your-44x-ticket-saving-needs-a-busy-box
---

<!-- lead -->
Two Amazon engineers moved the ticket classifier — the program that assigns each ticket one of 20 fixed labels — off Claude Sonnet 4.6 and onto a four-billion-parameter decision model they serve themselves, then published both bills: about $22,200 per million tickets before, about $500 after [1]. That is a 44x saving on the same traffic. It is also not a price. The cheap side is a rented graphics card at $1.408 an hour, so the saving breaks whenever the box sits idle, and the numbers on the page imply it runs at about half its ceiling [1].

<!-- tldr -->

## At a glance

- **The shift:** Amazon's ticketing team swapped a frontier model for a small decision model it hosts itself [1].
- **The number:** $500 per million tickets, against $22,200 before [1].
- **The risk:** the cheap side rents by the hour, so the saving shrinks as the box idles [1].

<!-- tension -->

## The bill changed meters, not size

Sonnet 4.6 spent about nine months labelling tickets before the swap [1]. Its bill was a token bill, and a token bill moves with demand. Every extra ticket, every longer comment thread, every retry costs again. Nobody had to forecast that bill, because it simply followed the work.

The replacement is priced the other way round. One rented instance at $1.408 an hour serves the model at about 640 milliseconds a request, which caps it near 5,600 tickets an hour, and it costs the same whether that hour holds 5,600 tickets or forty [1]. A token price tells you what one decision costs. An instance-hour tells you what a month of decisions costs if you sized the box right, and it charges you the same for a quiet Sunday.

I read the second bill as a demand forecast, not a price. Run the page's own numbers and it implies roughly 2,800 tickets an instance-hour, about half of what the hardware can do, because the team keeps headroom for bursts [1]. Break-even against Sonnet sits near 63 tickets an hour on the same box, a low bar for a system that takes company-wide alarms. The risk is not the bar. It is the nights and weekends when the bar is not cleared. The same arithmetic decides a rented graphics card for model inference, which this desk has priced in [Self-hosted AI: when to buy vs rent GPUs](/self-hosted-ai-when-to-buy-vs-rent-gpus/).

The model itself is not a smaller Sonnet. It cannot write text at all: it takes a state and a question with a list of options, then returns a probability and a confidence for each [1]. Getting there cost work, because the production label descriptions were longer than the model's 4,096-token window. All 20 were rewritten as one- or two-sentence criteria, plus a none option. Long tickets now drop their oldest comments to fit [1]. Fitting a catalog to a model that small is the part of a build nobody puts in a slide.

## By the numbers

- **$1.408 an instance-hour:** The published us-east-1 rate for the one graphics card that serves the whole classifier [1].
- **640 milliseconds a request:** The speed that sets one instance's ceiling at about 5,600 tickets an hour [1].
- **2,010 tokens a ticket:** Down from 6,724, because the answer is a label and not a written explanation [1].

<!-- tactical-insight -->

## What the team is watching now

I keep circling the three-way switch. Before the cut-over, one setting sent every ticket to the cloud model, one sent every ticket to the local model, and the third ran both and compared the answers on live traffic [1]. Going back was a 45-second configuration change, and the authors call the trial the part worth copying rather than the model [1]. That is a cheaper way to buy evidence than any offline evaluation, and a platform team can lift it without changing vendors.

The second finding is a reminder that serving code decides answers as much as weights do. Reordering the fields in a request moved the output probabilities by up to 0.19, so requests now go out with sorted keys [1]. I would want that measured before anyone reads a difference between two runs as a difference in quality.

The size choice is still open, and the team's own release notes price it in accuracy. On a 231-task public benchmark the four sizes score 77.9%, 81.0%, 86.6% and 89.6%, with median latencies of 102, 139, 136 and 245 milliseconds on a single Nvidia data-centre card [2]. The build in production is the second smallest of the four [2]. That leaves the largest about three points ahead of it at a higher latency, which is a trade a leader can argue with a table instead of a demo.

<!-- nuanced-takeaway -->

## The catch

The saving is real and narrow. It rests on a closed choice from a catalog of 20 labels, at high volume, where the old path's latency was hurting, and the authors say so [1]. They add that labels needing explanation, a catalog that changes weekly, or context that will not fit a few thousand tokens breaks the substitution [1]. Their page reports list prices, leaves out the Lambda (the small function that passes each ticket to the model), and never prices the engineering weeks behind the endpoint, the deployment stack and the label rewrite [1].

I cannot check the quality claim the way I would like. The page says the small model beat production Sonnet on a separate set of their tickets, and publishes no accuracy figure for either side [1]. The benchmark scores the decision models alone, so it compares sizes rather than vendors [3]. A vendor's own table about its own product is evidence of what that product costs, not of what it can do.

What I keep returning to is the floor under the saving. One box at that hourly rate is about $12,300 a year whether it labels anything or not, by arithmetic on the published rate [1]. Below about 63 decisions an hour the frontier model is cheaper. The hours when nobody files a ticket are the hours that decide whether the saving survives the quarter.

## Sources

- [1] Carr Onstott, Mehul Jaiswal and the Strands Agents team, "Amazon saves millions by replacing Sonnet 4.6 with Strands Decider" — https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider/
- [2] Tim Moreton and the Strands Agents team, "Strands Decider adds four Gemma 4 models" — https://strandsagents.com/blog/strands-decider-gemma-4-models/
- [3] Benchmark Heaven, "JevBench v1" — https://benchmarkheaven.com/jev-models
