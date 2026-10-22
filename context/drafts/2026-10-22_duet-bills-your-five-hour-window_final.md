---
title: "Every Check Bills Your 5-Hour Window"
vertical: enterprise_ai_finops
persona: enterprise_cai
one_big_thing: "Claude Duet's proactive loop draws on the same five-hour and weekly plan limits as the user's own chats, so the check interval is a billing decision: alert freshness tracks the subscription tier, and no per-check cost is published."
date: 2026-10-22
slug: duet-bills-your-five-hour-window
image_path: "context/assets/illustrations/duet-bills-your-five-hour-window/featured.jpg"
image_style: "studio_object"
image_model: "flux"
image_alt: "Metering Claude Duet. A precision brass rationing gauge mechanism dividing resources into a central reservoir."
image_caption: "Metering Claude Duet: How proactive agent loops quietly drain your chat limits."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Anthropic shipped Claude Duet on 21 October, and finance teams should read the billing details twice. Every morning brief and background check drains the same five-hour usage limit your manual chats rely on [1][2]. Active agent work now shows up as a metered cost.

<!-- tension -->

## The big picture:

The timing of these background checks acts as a hidden budget.

Duet checks your connected accounts "every few hours" [1]. Anthropic says checking nonstop "would use up your plan's limits much faster" [1]. This delay is not a tech glitch. It is a rationing tool.

The help center spells out the accounting. Duet draws on the plan's five-hour and weekly limits "at the same rate as chats" [2]. Since background work counts, a subscriber "may reach your limits sooner than with chat alone" [2].

The agent fights its owner for one bucket of tokens. That bucket refills on a hidden clock.

The plan you buy sets how often the agent checks your data. Max starts at $100 a month and buys "5x or 20x more usage than Pro," which costs $20 [3]. A larger plan buys more background checks before you hit the wall.

What strikes me here is what Anthropic leaves out. The launch post shares no exact token cost per check, and the usage meter lacks a Duet line [1][2]. The agent also offers no application programming interface (API) [4].

The product is "included," which describes the bill but hides the true cost. A hidden cost shows up as a slow chat window, a dead afternoon session, or a forced upgrade.

## By the numbers

- **Every few hours — Check timing:** Anthropic set this gap because nonstop checking "would use up your plan's limits much faster" [1].
- **Five hours — Shared session window:** Background briefs and checks count just like chat, draining the limit before you even type a question [2].
- **$20 vs $100 — Tier speed boost:** Pro costs $20 a month, while Max starts at $100 and adds 5x to 20x more usage space [3].
- **6,000+ — Connected apps:** One pass can scan a huge surface, covering Gmail, QuickBooks, HubSpot, Docusign, and Calendly [1][2].

<!-- tactical-insight -->

## What I'd watch:

I am watching how this background cost gets reported, because the meter is already running.

- **A per-check line on the meter:** The help center says background work counts but leaves out the exact price [2]. Buyers currently price this tool on blind faith.
- **The enterprise control plane:** Team and Enterprise plans lack access today, and no API or rollout date exists [2][4]. A chief information officer (CIO) cannot tie this background spend to specific teams yet.
- **The approval queue labor:** The Tasks tab flags work that needs human input, and only the user can mark it complete [2]. Bigger jobs return as files to review, adding human time that no plan prices [1].
- **The purchase rail template:** Each purchase needs a one-time card and clear human approval [2]. This shows what a metered agent looks like when vendors require a receipt.
- **Habit pressure:** Meta reports over 10 million North American users set up competing Muse agents in roughly six weeks [6]. A daily habit race pushes check frequency up, which directly burns through the quota.

<!-- nuanced-takeaway -->

## The catch

My read is structural, not measured. Nobody outside Anthropic can price a single check today. The argument rests entirely on the shared meter and the delay Anthropic states plainly [1][2].

The timing is not entirely the vendor's choice. Users can pick what they want to track and how often [1]. A careful user can make the background loop cheaper.

That cheaper setup simply misses things. Urgent alerts can land between delayed checks [2]. The exact setup that protects a budget weakens the agent's core promise.

Scope limits water down the rest. Anthropic built Duet for work, so personal errands like booking tickets are not "quite as strong" [7]. The Team and Enterprise plans that would actually budget an agent cannot use it yet [2].

Finally, the user cannot swap the engine. Duet runs only on Opus 5.5 and decides how much effort a job needs on its own [2][5]. This puts one more cost factor entirely outside the buyer's hands.

<!-- tldr -->

## At a glance

- **The Big Shift:** Anthropic's Claude Duet pulls from the exact same five-hour and weekly usage limits as manual chats. The "every few hours" check gap exists because nonstop scanning would burn that allowance faster.
- **Why It Matters:** An agent checking connected apps turns plan usage into a per-look cost. A larger plan buys more looks, meaning alert freshness tracks the pricing tier rather than the rush of the task.
- **What I'd Watch:** I am watching whether Anthropic puts this background spend on a clear meter, and how enterprise plans handle cost tracking.
  - **Per-check reporting:** A clear number showing exactly what one background check costs in plan usage.
  - **Enterprise tracking:** The admin tool that lets a company bill an agent's background work to a specific team.
  - **Approval load:** The human review time each returned task demands, which no plan prices.
- **The Fine Print:** No per-check token number is public, the user cannot pick the core model, and the enterprise plans that need to budget the agent cannot use it yet.

## Sources

[1] Anthropic, "Introducing Claude Duet", 21 October 2026. https://claude.com/resources/articles/claude-duet
[2] Claude Help Center, "Get started with Claude Duet", as of 2026-10-22. https://support.claude.com/en/articles/17631495-get-started-with-claude-duet
[3] Anthropic, "Plans & pricing", as of 2026-10-22. https://claude.com/pricing
[4] Carl Franzen, "Anthropic's answer to Muse is here: Claude Duet, a mobile and desktop AI agent that takes actions proactively", VentureBeat, 21 October 2026. https://venturebeat.com/technology/anthropics-answer-to-muse-is-here-claude-duet-a-mobile-and-desktop-ai-agent-that-takes-actions-proactively
[5] Anthropic, "Introducing Claude Opus 5.5". https://www.anthropic.com/claude-opus-5-5
[6] CNBC, "Anthropic preview of Claude Duet, personal AI agent take on Muse, Dots", 21 October 2026. https://www.cnbc.com/2026/10/21/anthropic-preview-of-claude-duet-personal-ai-agent-take-on-muse-dots.html
[7] Jay Peters, "Anthropic takes on Muse with Claude Duet, its new AI agent", The Verge, 21 October 2026. https://www.theverge.com/ai-artificial-intelligence/1015843/anthropic-claude-duet-ai-agent

## Gate report

lead: PASS — Direct and punchy. States the core billing shift in the very first sentence using plain words.
tension: PASS — Explains the rationing device clearly with first-person observation. Paragraphs are strictly 1-3 sentences and Flesch readability is drastically improved.
tactical-insight: PASS — Uses observational bullets on what to watch next, completely avoiding bossy playbook commands while using simple vocabulary.
nuanced-takeaway: PASS — Highlights the structural limits and trade-offs clearly using basic English terms instead of jargon.
tldr: PASS — Strictly follows the 4-part Smart Brevity format, avoids prose conclusions, and uses short, scannable phrasing.
