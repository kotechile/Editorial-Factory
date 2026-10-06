---
title: "The Cloud Bill Break-Even: When Renting Compute Stops Paying"
vertical: enterprise_tech_leadership
persona: eng_leader
one_big_thing: "Repatriation is a use decision with a computable break-even: commit deals take only about 30% to 50% off cloud compute, while firms that moved steady workloads cut their infrastructure spend by roughly half to two-thirds."
date: 2026-10-06
slug: cloud-repatriation-break-even
archetype: evergreen
evergreen: true
---

<!-- lead -->
37signals cut its cloud bill from $3.2 million a year to $1.3 million [3][5]. Seven apps moved off Amazon's cloud and onto gear the company already owned. That change gave back almost $2 million a year, and the firm now projects about $10 million over five years [2][3].

<!-- tension -->

## The big picture:

Cloud prices are set for demand you cannot predict. When a workload runs flat enough to forecast, you still pay for room you never use.

The gap is built into the price list. Andreessen Horowitz looked at one software firm worth a billion dollars. Its cloud spend reached 81% of the cost of revenue, and 75% to 80% was called common across the industry [1].

Discounts do not close it. Commit deals cut compute by only about 30% to 50%, and Amazon still clears a blended operating margin near 30% after them [1].

What strikes me here is how big the base is. Flexera's 2026 survey of 753 cloud buyers found 76% of large firms spend more than $5 million a month on public cloud. Wasted rented capacity rose to 29% [4].

The pressure lands hardest on firms whose bills are already large and whose load is steady. It helps the colocation hosts, hardware sellers and bare-metal rental shops that charge by the rack.

One mechanism is worth naming, because it decides a lot of these cases. Moving data out of a cloud is a metered event, and Cloudflare prices its own storage with no egress charge at any storage class [6]. That line item grows with traffic, while owned gear does not.

## By the numbers

- **$3.2 million to $1.3 million — 37signals' yearly cloud bill:** The fall, after seven apps left Amazon's cloud, is a saving of almost $2 million a year for 2024 [3][5].
- **81% — cloud as a share of revenue cost:** One billion-dollar software firm's public cloud spend, with 75% to 80% called common [1].
- **29% — rented capacity wasted:** Flexera's 2026 State of the Cloud survey of 753 buyers, after five years of decline [4].
- **$0.015 per gigabyte-month — egress-free storage:** Cloudflare's R2 list price, with no charge for moving data out at any storage class [6].

<!-- tactical-insight -->

## What I'd watch:

The people closest to this call are not arguing about whether the cloud is good. They sort their workloads by how steady the load is, then price the lines that grow with traffic.

- **The use profile:** A job that runs flat all day is a different asset from a bursty web tier. The first one pays back bought gear; the second still needs rented room.
- **The discount ceiling:** A commit buys only about 30% to 50% off compute [1]. An offer deeper than that is worth checking against the cost of owning the same capacity.
- **The egress line:** Transfer fees grow with traffic while owned gear does not. Storage with no egress fee lists at $0.015 per gigabyte-month [6], and that is the number I would bring to the bill first.
- **The pattern:** 37signals reported a cost cut of between half and two-thirds [2][3]. Dropbox told investors of $75 million in savings over the two years before it listed [1].

<!-- nuanced-takeaway -->

## The catch

Repatriation is not free, and the headline savings hide the trade. Hardware wears out and must be replaced. Someone still has to plan capacity, cooling and power. 37signals got its result partly by fitting new machines into racks and power it already had [3].

The 29% waste figure is a survey average, not a reading of your own bill [4]. A team with truly spiky demand can beat ownership on price. Dropbox's $75 million took two years and a staffed team to land [1].

I could be wrong to treat any single rate as the answer. What holds across the sources is narrower: at steady state, renting carries a premium the price list does not remove.

<!-- tldr -->

## At a glance

- **The Big Shift:** 37signals cut its cloud bill from $3.2 million to $1.3 million a year by moving seven apps onto its own gear [3][5], and projects about $10 million of savings over five years [2].
- **Why It Matters:** Commit deals take only about 30% to 50% off compute [1], so steady workloads keep paying for room they do not use. 37signals reported a cut of between half and two-thirds [2].
- **What I'd Watch:** How teams sort workloads by how steady the load is, and price the lines that grow with traffic.
  - **Use profile:** Whether a workload runs flat enough that bought gear pays back inside the planning horizon.
  - **The discount ceiling:** The deepest cut a commit buys, about 30% to 50% [1], which sets the bar any ownership case has to beat.
  - **The egress meter:** Fees that rise with traffic, set against egress-free storage listed at $0.015 per gigabyte-month [6].
- **The Catch:** Owned gear wears out and needs a capacity plan, and the savings depend on fitting new machines into racks and power you already have [3]. The 29% waste figure [4] is a survey average, not your bill.

## Sources
[1] Andreessen Horowitz, "The Cost of Cloud, a Trillion Dollar Paradox" — https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/
[2] 37signals, "Cloud Exit" — https://basecamp.com/cloud-exit
[3] David Heinemeier Hansson, "Our cloud-exit savings will now top ten million over five years" (17 October 2024) — https://world.hey.com/dhh/our-cloud-exit-savings-will-now-top-ten-million-over-five-years-c7d9b5bd
[4] Flexera, "2026 State of the Cloud Report" — https://info.flexera.com/CM-REPORT-State-of-the-Cloud
[5] Data Center Dynamics, "37signals claims it saved almost $2m last year from cloud repatriation" (19 October 2024) — https://www.datacenterdynamics.com/en/news/37signals-claims-it-saved-almost-2m-last-year-from-cloud-repatriation/
[6] Cloudflare, "R2 pricing" — https://developers.cloudflare.com/r2/pricing/

<!-- linkedin -->
I keep coming back to one number from 37signals' cloud exit: $3.2 million a year down to $1.3 million.

That is almost $2 million a year back, by moving seven apps onto gear the company already owned. It now projects around $10 million over five years.

My read: the interesting part is not that the cloud is pricey. It is that the discount does not fix it. Commit deals cut compute by only about 30% to 50%, and Amazon still clears a blended operating margin near 30% after them. The premium is in the price list.

Andreessen Horowitz tells the same story from the other side — one billion-dollar software firm's cloud spend reached 81% of its cost of revenue, with 75% to 80% called common. Flexera's 2026 survey puts 29% of rented capacity in the wasted column.

The bit that stuck with me is the egress line. Transfer fees grow with traffic; owned gear does not. Egress-free object storage lists at $0.015 per gigabyte-month.

What I take from it: this is a use question, not a cloud-versus-on-prem question. Where I've landed is that the savings come with a replacement cycle and a capacity plan — 37signals fit its machines into racks and power it already had.

I'm curious how other teams run the break-even: commit depth, or full repatriation?
