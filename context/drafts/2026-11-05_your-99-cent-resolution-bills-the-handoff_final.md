---
title: "Your $0.99 Resolution Bills the Handoff"
vertical: enterprise_ai_finops
kind: evergreen
archetype: evergreen
evergreen: true
persona: enterprise_cai
one_big_thing: "AI vendors moved from selling seats to selling units, and each writes the unit's own definition on its pricing page, so one handled customer request is priced from $0.20 to $2.00 and a handoff to a human, a silent customer and a same-day return each bill differently under three major vendors' wording — the definition sentence is the term to negotiate, not the rate."
date: 2026-11-05
slug: your-99-cent-resolution-bills-the-handoff
image_path: "context/assets/illustrations/your-99-cent-resolution-bills-the-handoff/featured.jpg"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "Your $0.99 Resolution Bills The. Three adjacent mechanical tally-register gate modules on a steel baseplate, each with a different handoff"
image_caption: "Your $0.99 Resolution Bills The: Intercom charges $0.99 when its AI agent closes a."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Intercom charges $0.99 when its AI agent closes a question, and it bills that resolution even when the handoff goes to a person [1]. Zendesk sells the same answer for $1.50 with a volume deal, or $2.00 without one, and bills only the requests its AI agent closed without passing them to a person [2]. Salesforce prices by the conversation at $2.00, or by the action credit at $500 for 100,000, which its own example prices at $0.20 a request [3]. Four prices, one request, and the only thing that splits them is what each vendor's page says the unit holds.

<!-- tension -->

## Why the price tells you nothing

What I keep circling is this: the unit belongs to the vendor, while the buyer's cost per resolved task is something else. Buyers spent two years asking for value they could check, which pushed AI vendors from selling seats to selling results. The FinOps Foundation lists per case resolved as a unit a firm can track, right next to cost per token [5]. The buyer picks that measure at the Foundation; the vendor writes it on the pricing page.

The three pricing pages, placed side by side, show the gap. Intercom counts an outcome when a customer confirms the issue is fixed, when the customer simply stops replying, or when "Fin completes a workflow (Procedure), including handoffs" [1]. Zendesk bills only requests "successfully resolved by the AI agent, without any escalation to a human agent" [2]. Salesforce bills a conversation flat, and says that under its credit model "each action is metered individually" [3]. Three firms, three answers to the question a finance chief really asks: who pays when the agent fails?

Three events decide a support bill. If a customer goes quiet without confirming anything, Intercom's wording bills it, Zendesk's wording wants a resolution with no handoff, and Salesforce bills the chat either way.

If the agent then passes the ticket to a person, Intercom keeps that inside the billable workflow, Zendesk leaves it out, and Salesforce bills the chat it happened in. The same customer returns that afternoon with a second issue, so Intercom bills once per chat while Zendesk bills a second time. None of the three is lying; they price different events.

Only one of those versions matches the event the buyer thinks it is buying.

The gap is the whole negotiation.

## By the numbers

- **$21.53 — Wage anchor:** the median hourly wage for customer service representatives in 2025, $44,770 a year, and the only number here that is measured rather than quoted [4].
- **$2.15 — Six minutes of that wage:** at $21.53 an hour, six minutes of human work costs $2.15 in wages alone. The $0.99 unit is 46 percent of that, and the $2.00 unit is 93 percent, before benefits or supervision [1][2][4].
- **5 automated resolutions per agent per month — Included allowance:** Zendesk bundles that much into Suite Team and 10 into Professional. Anything past it bills at the committed or pay-as-you-go rate [2].

<!-- tactical-insight -->

## What buyers are doing now

My sense is that the teams who handle these deals have stopped arguing about the rate and started arguing about the sentence. The pattern holds. It shows up in four moves.

- **They read the definition first.** A cheap unit that bills a handoff is not automatically cheaper than a dearer one that does not. The real ratio turns on how often the agent fails, and no vendor page prints that.
- **They model volume on their own share.** Intercom's page carries a customer reporting a 50 percent resolution rate. Zendesk's page advertises up to 80%+ with no method and no sample [1][2]. Neither is a figure a buyer can plan on, so the share has to come from a pilot.
- **They watch the floors.** Intercom wants a minimum monthly commitment, and its own example is 50 outcomes. Zendesk bundles a few resolutions per agent each month [1][2]. A floor turns a variable unit into a fixed bill, which is the thing the unit was meant to avoid.
- **They keep the bill and the work in one ledger.** A unit price only helps if the bill reaches the unit that caused it. That is the gap that leaves [a chargeback built from tokens alone](/your-chargeback-misses-40-of-the-bill/) short of what a business unit really uses.

<!-- nuanced-takeaway -->

## The catch

My read, held loosely: none of this makes unit pricing a bad deal. It makes it a different deal from the one "pay only for outcomes" suggests. The vendor's own classifier — the model or rule that decides whether an answer counted — sets the count, and a buyer cannot audit it from outside. The unit price is also only part of the bill, since the platform, the seats around it, the setup work and the knowledge base all bill on their own. The fair comparison sets the vendor's unit against the buyer's own loaded cost per contact — wages plus benefits, supervision and tools. That loaded cost includes the review minutes the unit never sees. Cost per resolved task is still the right measure, but it is not one a vendor can sell you because the denominator belongs to the buyer.

<!-- tldr -->

## At a glance

- **The shift:** AI vendors sell units, not seats, and each vendor defines the unit.
- **The number:** $2.15 buys six minutes of a customer-service wage, the floor these units are measured against.
- **The risk:** One vendor's definition bills a handoff, so the cheapest unit is not the cheapest bill.

## Sources

[1] Intercom — Pricing, Fin AI Agent and helpdesk plan cards, list prices and unit definition retrieved 2026-11-05 — https://www.intercom.com/pricing
[2] Zendesk — Pricing, automated-resolution allowances and rates, list prices retrieved 2026-11-05 — https://www.zendesk.com/pricing/
[3] Salesforce — Agentforce pricing, conversation rate, Flex Credit rate and worked example, retrieved 2026-11-05 — https://www.salesforce.com/agentforce/pricing/
[4] O*NET OnLine — Customer Service Representatives (43-4051.00), median wages (2025), retrieved 2026-11-05 — https://www.onetonline.org/link/summary/43-4051.00
[5] FinOps Foundation — "Unit Economics" capability, framework page — https://www.finops.org/framework/capabilities/unit-economics/
[6] Derived arithmetic for this article: $21.53 an hour ÷ 60 = $0.3588 a minute, so six minutes is $2.15; $0.99 ÷ $2.15 = 46 percent and $2.00 ÷ $2.15 = 93 percent.
