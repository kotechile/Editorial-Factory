---
title: "Why Cloud Uptime SLAs Are Not Insurance"
vertical: enterprise_build_vs_buy
persona: eng_leader
one_big_thing: "An uptime promise only pays a credit capped at a slice of the monthly bill — 10% for a month below 99.99% at both Amazon and Google, and the full credit only below 95% — so a fallback is priced against the outage, not the refund."
date: 2026-10-07
slug: sla-credit-is-not-insurance
archetype: evergreen
evergreen: true
meta_title: "Why Cloud Uptime SLAs Are Not Insurance"
meta_title_source: "derived_from_title"
meta_description: "Amazon hands back 10% of the monthly bill when a cloud region drops below 99.99% uptime, but it takes a full month below 95% to see a 100% credit."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/sla-credit-is-not-insurance/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "Darkened, unlit server rack standing out amidst thousands of glowing servers in a cavernous enterprise data hall."
image_caption: "The gap between a vendor's bill credit and a buyer's actual financial exposure turns redundancy into a critical design choice."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Amazon hands back 10% of the monthly bill when a cloud region drops below 99.99% uptime, but it takes a full month below 95% to see a 100% credit [1]. Google's refund ladder lands in almost the exact same place [2]. Both promises look like safety nets, but they are just refund schedules.

<!-- tension -->

## The big picture:

An uptime promise guarantees the vendor's service, but it only pays out a fraction of the invoice.

Amazon commits to 99.99% monthly uptime for a region [1]. Google promises the same for machines across zones [2]. Vercel commits to 99.99% for its content platform [3]. On paper, these Service Level Agreements (SLAs) look identical.

The reality shifts after a bad month. The credit is a percentage of the fee paid, so it scales with the invoice rather than the actual damage. A broken payment service does not cost the buyer an afternoon of subscription fees. It costs whatever the buyer promised its own customers.

The part I keep circling is the gap between those two numbers. A nine-hour break in a mapping service once halted a logistics platform, triggering $85,000 in customer penalties [4]. The queue and local cache that would have absorbed that break cost just $6,500 to build [4]. The vendor's refund never mattered in that math.

## By the numbers

- **10% — First credit tier:** A month below 99.99% but at or above 99.0% earns a 10% bill credit at both Amazon and Google [1][2].
- **30% against 25% — Middle band:** Amazon pays 30% of the month for uptime below 99.0%, while Google pays 25% [1][2].
- **100% — Only at the floor:** Both vendors return a full month's fee only when uptime drops below 95.0% [1][2].
- **12 January 2027 — Free exit:** European Union law bars data processing providers from charging switching fees starting on this date [5].

<!-- tactical-insight -->

## What I'd watch:

The engineering leaders handling this well do not argue about vendor reliability. They read the remedy clause next to their own financial exposure. Here is what I am watching as teams navigate this gap.

- **The credit ladder:** The full refund sits on the bottom rung, below 95% uptime [1][2]. That equals a 36-hour outage in a standard 30-day month.
- **The excluded hours:** Vercel measures uptime in minutes and subtracts "Excused Downtime" before applying any credit [3]. I expect teams to scrutinize how much of a real incident falls into that bucket.
- **The billing carve-out:** Amazon drops charges for a single machine unavailable for more than six minutes of a clock hour [1]. This highlights that the vendor's remedy shapes around its own billing, not the buyer's downtime.
- **The exit date:** Regulation (EU) 2023/2854 removes switching charges from 12 January 2027 [5]. A cheaper exit turns multi-cloud fallbacks into a design choice rather than a sunk cost.
- **The cheap hedge:** Building a queue, a local cache, and a second provider costs roughly $6,500 against an $85,000 penalty [4]. That is the actual trade most teams face.

<!-- nuanced-takeaway -->

## The catch

None of this argues for building everything twice. Redundancy carries its own heavy bill in engineering hours, configuration drift, and the new failure modes of a second system.

The honest limit is that vendors write these credit tiers and can revise them at any time. What lasts is the structure of the remedy. A refund written as a share of the fee cannot cover a loss sized by the buyer's revenue.

My read: the uptime promise is worth buying for the escalation path and the clock it starts, not for the cash. The problem happens when the decision to buy the promise and the decision to build the fallback occur in silos, tricking a team into treating a refund schedule like insurance.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "$2.7 Trillion AI Bill Just Turned Cost Control Into a Buying…" -> https://giniloh.com/ai-spend-27t-cost-visibility-mandate/ [same site (giniloh.com); same category; topical overlap: bill] Link "$2.7 Trillion AI Bill Just Turned Cost Control Into a Buying…" in the section where the article touches bill. -->
<!-- internal-link hint: "Token Prices Just Halved. The CFO Still Can’t Read the Bill." -> https://giniloh.com/token-prices-just-halved-the-cfo-still-cant-read-the-bill/ [same site (giniloh.com); same category; topical overlap: bill] Link "Token Prices Just Halved. The CFO Still Can’t Read the Bill." in the section where the article touches bill. -->
<!-- internal-link hint: "Agentic AI Adoption Soars, But Profits Stall in 2026" -> https://giniloh.com/agentic-ai-adoption-soars-but-profits-stall-in-2026/ [same site (giniloh.com); same category] Link "Agentic AI Adoption Soars, But Profits Stall in 2026" in the section where the article touches this topic. -->
## Related reading

- [$2.7 Trillion AI Bill Just Turned Cost Control Into a Buying…](https://giniloh.com/ai-spend-27t-cost-visibility-mandate/)
- [Token Prices Just Halved. The CFO Still Can’t Read the Bill.](https://giniloh.com/token-prices-just-halved-the-cfo-still-cant-read-the-bill/)
- [Agentic AI Adoption Soars, But Profits Stall in 2026](https://giniloh.com/agentic-ai-adoption-soars-but-profits-stall-in-2026/)
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Uptime promises from Amazon, Google, and Vercel all cluster around 99.99%, paying a credit capped strictly at a percentage of the monthly bill [1][2][3].
- **Why It Matters:** A vendor refund scales with the invoice and cannot cover an outage sized by the buyer's own lost revenue. The call to add a fallback has to be priced against the cost of the outage, not the vendor's credit.
- **What I'd Watch:** How engineering teams read the remedy clause before leaning on it.
  - **The credit ladder:** The 100% tier requires uptime below 95.0%, which is a massive 36-hour outage in a 30-day month [1][2].
  - **The exit date:** European Union rules eliminate switching charges starting 12 January 2027 [5].
  - **The cheap hedge:** A queue, a cache, and a second provider cost far less to build than absorbing one large customer penalty [4].
- **The Catch:** Redundancy adds heavy engineering load, and vendors can rewrite their credit tiers at will. The durable rule remains that a remedy priced as a share of the fee is not insurance.

## Sources
[1] Amazon Web Services, "Amazon Compute Service Level Agreement" (EC2) — https://aws.amazon.com/ec2/sla/
[2] Google Cloud, "Compute Engine Service Level Agreement" — https://cloud.google.com/compute/sla
[3] Vercel, "Service Level Agreement" — https://vercel.com/legal/sla
[4] Editorial-Factory Intelligence Unit, anonymized field note (enterprise_build_vs_buy, Anecdote 3) — context/growth_os/customer-truth.md
[5] European Union, Regulation (EU) 2023/2854 (Data Act), Article 29 — https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng

## Gate report
lead: PASS — Delivers the core 10% and 100% refund tiers immediately in sentence 1 with zero throat-clearing.
tension: PASS — Frames the structural gap between vendor refunds and customer damage clearly; includes 4-bullet By the numbers section.
tactical-insight: PASS — Uses first-person observation cues and structures insights as bulleted observations of what teams are doing, not commands.
nuanced-takeaway: PASS — Presents the honest tradeoff of redundancy costs using the mandatory 'The catch' header and a first-person read.
tldr: PASS — Follows the strict 4-part Smart Brevity schema under 'At a glance' header with indented sub-bullets for what to watch.
