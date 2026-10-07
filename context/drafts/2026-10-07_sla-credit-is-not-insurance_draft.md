---
title: "What an Uptime Promise Actually Pays"
vertical: enterprise_build_vs_buy
persona: eng_leader
one_big_thing: "An uptime promise only pays a credit capped at a slice of the monthly bill — 10% for a month below 99.99% at both Amazon and Google, and the full credit only below 95% — so a fallback is priced against the outage, not the refund."
date: 2026-10-07
slug: sla-credit-is-not-insurance
archetype: evergreen
evergreen: true
---

<!-- lead -->
Amazon hands back 10% of the month's bill when one of its cloud regions runs below 99.99% uptime, and it takes a month below 95% before that credit reaches 100% [1].

Google's ladder lands in almost the same place, with a 25% step in the middle band [2]. Both promises read like safety nets. Both are refund schedules.

<!-- tension -->

## The big picture:

An uptime promise is a guarantee about the vendor's own service, and the only thing it pays out is a slice of the invoice.

Amazon commits to 99.99% monthly uptime for a region [1]. Google commits to the same figure for machines spread across zones [2]. Vercel commits to 99.99% for the platform that serves its customers' content [3]. On paper, all three say the same thing.

The picture shifts after a bad month. The credit is written as a percentage of the fee the customer paid, so it grows with the bill and never with the damage. A payment service that stops for an afternoon does not cost the buyer an afternoon of subscription fees. It costs whatever the buyer's own customers were promised.

I keep circling the gap between those two numbers. A nine-hour break in a third-party mapping service once halted route generation for a logistics platform, which then paid $85,000 in customer penalties; the queue and local cache that would have absorbed the break cost $6,500 to build [4]. The vendor's refund never entered that arithmetic.

## By the numbers

- **10% — First credit tier:** A month below 99.99% but at or above 99.0% earns a credit worth 10% of the bill at both Amazon and Google [1][2].
- **30% against 25% — Middle band:** Amazon pays 30% of the month for uptime below 99.0%; Google pays 25% for the same band [1][2].
- **100% — Only at the floor:** Both vendors return a full month's fee only once uptime drops below 95.0%, which is a day and a half of lost service in a 30-day month [1][2].
- **12 January 2027 — Free exit:** From that date, European Union law bars providers of data processing services from charging a customer for the switching process [5].

<!-- tactical-insight -->

## What I'd watch:

The teams that handle this well are not the ones arguing about whether vendors are reliable. They are the ones who read the remedy clause next to their own exposure. Here is where I have seen that show up.

- **The credit ladder:** The full refund sits on the bottom rung, below 95% uptime. That is a 36-hour outage in a 30-day month. Anything short of a lost month pays a thin slice of one invoice [1][2].
- **The excluded hours:** Vercel measures uptime in minutes and subtracts "Excused Downtime" before any credit applies [3]. I would want to know how much of a real incident falls into that bucket.
- **The billing carve-out:** Amazon will not charge for a single machine that is unavailable for more than six minutes of a clock hour [1]. A small courtesy, and a reminder that the vendor's remedy is shaped around its own billing, not the customer's downtime.
- **The exit date:** Regulation (EU) 2023/2854 removes switching charges from 12 January 2027 [5]. The cheaper exit turns a fallback into a design choice rather than a sunk project.
- **The cheap hedge:** The desk's own field note put a queue, a local cache and a second provider at $6,500 against an $85,000 penalty [4]. That is the shape of the trade most teams face, and it is not the credit.

<!-- nuanced-takeaway -->

## The catch

None of this argues for building everything twice. Redundancy carries its own bill in engineers, configuration drift and the new failure modes of any second system.

The honest limit is that the credit tiers I read here are the vendors' own documents, and a vendor can revise the same page. What lasts is the shape of the remedy. A refund written as a share of the fee cannot cover a loss that is sized by the buyer's revenue.

My read: the promise is worth buying for the escalation path and the clock it starts, not for the money. Where I've landed is that the two decisions — buy the promise, build the fallback — get made by different people at different times, which is how a team ends up trusting a refund schedule as if it were insurance.

<!-- tldr -->

## At a glance

- **The Big Shift:** Uptime promises from Amazon, Google and Vercel all cluster around 99.99%, and each one pays a credit capped at a percentage of the monthly bill [1][2][3].
- **Why It Matters:** A refund that scales with the invoice cannot cover an outage sized by the buyer's own revenue, so the call to add a fallback has to be priced against the outage rather than the credit.
- **What I'd Watch:** Whether teams read the remedy clause before they lean on it.
  - **The credit ladder:** The 100% tier needs uptime below 95.0%, a 36-hour outage in a 30-day month [1][2].
  - **The exit date:** European Union rules remove switching charges from 12 January 2027 [5].
  - **The cheap hedge:** A queue, a cache and a second provider cost far less than one large penalty [4].
- **The Catch:** Redundancy adds its own engineering load, and vendors can revise their credit tiers. The durable rule is that a remedy priced as a share of the fee is not insurance.

## Sources
[1] Amazon Web Services, "Amazon Compute Service Level Agreement" (EC2) — https://aws.amazon.com/ec2/sla/
[2] Google Cloud, "Compute Engine Service Level Agreement" — https://cloud.google.com/compute/sla
[3] Vercel, "Service Level Agreement" — https://vercel.com/legal/sla
[4] Editorial-Factory Intelligence Unit, anonymized field note (enterprise_build_vs_buy, Anecdote 3) — context/growth_os/customer-truth.md
[5] European Union, Regulation (EU) 2023/2854 (Data Act), Article 29 — https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng
