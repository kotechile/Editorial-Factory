---
title: "Every Check Bills Your 5-Hour Window"
vertical: enterprise_ai_finops
persona: enterprise_cai
one_big_thing: "Claude Duet's proactive loop draws on the same five-hour and weekly plan limits as the user's own chats, so the check interval is a billing decision: alert freshness tracks the subscription tier, and no per-check cost is published."
date: 2026-10-22
slug: duet-bills-your-five-hour-window
---

<!-- lead -->
Anthropic shipped Claude Duet on 21 October, and the part of the launch a finance team should read twice is where the work gets billed: your five-hour window. Every morning brief and every check-in pays out of the same allowance your own questions draw on [1][2]. Proactivity now arrives as a metered line item.

<!-- tension -->

## The big picture:

My read starts with the launch post, which gives the design constraint away. Duet checks your connected accounts "every few hours", and Anthropic names the reason: checking nonstop "would use up your plan's limits much faster" [1]. The interval is not a latency artifact. It is a rationing device, doing the job a budget would do.

The help centre spells out the accounting. Duet draws on the plan's five-hour session and weekly limits "at the same rate as chats", and the background work counts too, so a subscriber "may reach your limits sooner than with chat alone" [2]. Two things follow. The agent competes with its owner for one bucket. And the bucket refills on a clock the subscriber cannot see.

The subscription tier then becomes a cadence multiplier. Max starts at $100 a month and buys "5x or 20x more usage than Pro", which is $20 [3]. Since every check spends usage, a bigger plan does not only buy more chat. It buys more looks at your inbox each day before the wall arrives. How fresh the alerts are tracks the tier, not how urgent the work is.

What Anthropic does not publish matters here. There is no per-check token figure in the launch post, no separate Duet line on the usage meter, and no application programming interface (API) for the agent [1][2][4]. The product is "included", which is accurate about the invoice and silent about the cost. For a business, an unbudgeted variable cost does not disappear. It shows up as a slower chat, a dead window before the day is out, or a tier upgrade nobody planned.

The contrast inside the product is the tell. Money gets metered explicitly: each purchase uses a one-time card that works once, and Duet asks before every one [2]. Token burn behind a background check gets an interval and no receipt.

## By the numbers

- **Every few hours — Check cadence:** Anthropic's own interval, chosen because nonstop checking "would use up your plan's limits much faster" [1].
- **Five-hour — Shared session window:** the brief and the check-ins count at the same rate as chat, so background work reaches the limit before the user's own questions do [2].
- **$20 vs $100 — Tier as a cadence multiplier:** Pro is $20 monthly, or $17 with the $200 annual prepay; Max starts at $100 and adds 5x or 20x Pro's usage [3].
- **6,000+ — Connectors in a check:** the read surface one pass can span, from Gmail and Calendar to QuickBooks, HubSpot, Docusign and Calendly [1][2].

<!-- tactical-insight -->

## What I'd watch:

What I am watching is how this cost gets reported, because the design is already set.

- **A per-check line on the meter:** the help centre says background work counts and does not say how much [2]. Until a per-check figure exists, a buyer prices the agent on faith.
- **The enterprise control plane:** Team and Enterprise plans are excluded, no Duet API was announced, and no enterprise rollout date was given [2][4]. A chief information officer (CIO) cannot attribute this background spend to a team yet, so the first enterprise rollout will be a finance question before it is an IT one.
- **The approval queue as the labour line:** the Tasks tab flags work that needs input, and only the user can mark a task complete [2]. Bigger jobs come back as files to review [1]. Each approval is human time that no plan prices.
- **The purchase rail as the template:** a one-time card per purchase, an approval per purchase [2]. That is what a metered agent looks like once the vendor decides the spend needs a receipt.
- **Habit pressure:** Meta says more than 10 million people in the US and Canada set up Muse agents in about six weeks [6]. A daily-habit race pushes check frequency up, and frequency is the one lever that raises quota burn.

<!-- nuanced-takeaway -->

## The catch

My read is structural, not measured. No per-check token figure is published, so nobody outside Anthropic can put a number on a check today. The argument rests on the interval and the shared meter, both of which Anthropic states plainly [1][2].

The interval is also not the vendor's alone to set. Subscribers can say what they want to hear about and how often [1], so a careful user can make the loop cheaper. That cheaper setting is the one that misses things, since something urgent can arrive between checks [2]. The configuration that protects the budget is the configuration that weakens the promise.

Scope limits water down the rest. Duet is built for work, and personal errands such as booking tickets are not "quite as strong" [7]. The plans that would actually budget an agent, Team and Enterprise, cannot use it yet [2]. And the user cannot choose the model: Duet runs on Opus 5.5 and decides how much effort a job needs [2][5], which puts one more cost variable outside the buyer's hands.

None of that makes the product bad. It makes the pricing question the honest one. A proactive agent is a background process with a subscription attached, and the first question a finance team should ask is how often it runs.

<!-- tldr -->

## At a glance

- **The Big Shift:** Anthropic's Claude Duet works as a proactive agent, and its background loop draws on the same five-hour and weekly limits as the user's own chats. The "every few hours" check interval exists because nonstop checking would burn the allowance faster.
- **Why It Matters:** An agent that checks your accounts every few hours turns plan usage into a per-look cost. A bigger subscription buys more looks, so alert freshness tracks the tier rather than the urgency of the work. None of this shows on an invoice, because the product is bundled into Pro and Max.
- **What I'd Watch:** I am watching whether Anthropic puts the background spend on the meter, and whether enterprise access arrives with cost attribution.
  - **Per-check reporting:** a published or in-product figure for what one background check costs in plan usage.
  - **Enterprise attribution:** the control that lets an organisation bill an agent's background work to a team.
  - **Approval load:** the human review each returned task adds, which no plan prices.
- **The Catch:** No per-check number is published, the user can neither pick the model nor watch the work, and the plans that would budget the agent cannot use it yet.

## Sources

[1] Anthropic, "Introducing Claude Duet", 21 October 2026. https://claude.com/resources/articles/claude-duet
[2] Claude Help Center, "Get started with Claude Duet", as of 2026-10-22. https://support.claude.com/en/articles/17631495-get-started-with-claude-duet
[3] Anthropic, "Plans & pricing", as of 2026-10-22. https://claude.com/pricing
[4] Carl Franzen, "Anthropic's answer to Muse is here: Claude Duet, a mobile and desktop AI agent that takes actions proactively", VentureBeat, 21 October 2026. https://venturebeat.com/technology/anthropics-answer-to-muse-is-here-claude-duet-a-mobile-and-desktop-ai-agent-that-takes-actions-proactively
[5] Anthropic, "Introducing Claude Opus 5.5". https://www.anthropic.com/claude-opus-5-5
[6] CNBC, "Anthropic preview of Claude Duet, personal AI agent take on Muse, Dots", 21 October 2026. https://www.cnbc.com/2026/10/21/anthropic-preview-of-claude-duet-personal-ai-agent-take-on-muse-dots.html
[7] Jay Peters, "Anthropic takes on Muse with Claude Duet, its new AI agent", The Verge, 21 October 2026. https://www.theverge.com/ai-artificial-intelligence/1015843/anthropic-claude-duet-ai-agent
