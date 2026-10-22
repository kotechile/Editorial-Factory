---
title: "One Request, Five Actions: Your 5x Blind Spot"
vertical: enterprise_ai_finops
persona: enterprise_cai
one_big_thing: "The AI bill is metered in actions and the AI budget is written as a share of infrastructure spend, so neither can be lined up with a resolved request until someone counts actions per request — and the vendor's own examples show a 5x spread on the same work."
date: 2026-10-22
slug: one-request-five-actions
synthesis: true
sources:
  - https://www.cloudzero.com/blog/ai-economics-pulse-october-2026
  - https://www.salesforce.com/agentforce/pricing/
---

<!-- lead -->
Salesforce's own pricing page prices one customer request at one action in one worked example. In another, the same kind of request takes five. That is a 5x spread on one list price, or US$0.10 against US$0.50 for the same question [1]. That spread is your blind spot, and it is not a rounding error. A bill metered in actions cannot be lined up with a budget written as a share of infrastructure spend. This month's numbers show how far apart the two have drifted.

<!-- tension -->

## The big picture:

CloudZero's October pulse puts artificial intelligence (AI) at 3.02% of the median cloud bill in September 2026 [2]. That is a rise of 37 basis points in a month, the 14th straight rise and the largest of the 14 [2]. Its survey of 252 finance leaders ran in the same window. It puts AI at 21% to 35% of infrastructure spend [2]. One number is a bill. The other is an estimate.

I'll take CloudZero at its word on the caveat. It says its respondents count AI bundled into software subscriptions. It says the two samples differ. It says 3.02% is a floor and 21% to 35% is a guess [2]. What I keep circling is that neither set counts the unit that moves the invoice: actions per request.

Salesforce's page is the clearest place to watch that meter work. An action is one step an agent takes — change a record, sum up a case, answer a product question [1]. A text action costs 20 credits, or US$0.10 [1]. A voice action costs 30 credits, or US$0.15. A conversation is priced at US$2. A Help Agent resolution is also US$2 [1].

The vendor's five worked examples then price one request at 2, 3, 5, 1 and 4 actions [1]. Same list price. Same kind of task. Five times the money at the top of the range. Salesforce calls the credit "a new unit of payment for Agentforce that align cost to the business value your AI agents create" [1]. My read is that a price per step aligns cost to the number of steps. The step count sits inside the agent's design, not inside the outcome the buyer wanted.

Gartner's survey line sits under all of this. "Unlike traditional technology costs, which are largely predictable, AI costs are probabilistic and determined at run time" [4]. Run time is the agent's loop. That is where the count gets set, request by request, long after the contract is signed.

## By the numbers

- **3.02% — AI's share of the median bill:** September 2026, up 37 basis points from 2.66% in August, the 14th straight monthly rise and the largest of the 14, across 422 firms [2].
- **21% to 35% — Finance's own estimate:** the median of 252 finance leaders put AI at that share of infrastructure spend, 54% said above 20%, and the billed median was 3.02% [2].
- **US$0.10 to US$0.50 — One request, five actions:** text actions on the Agentforce list price, from the one-action example to the five-action example; a voice call ran four actions at US$0.15 each [1].
- **12.55% — Top quartile:** the 75th percentile of AI's share of cloud spend, against 0.27% at the 25th [2].

<!-- tactical-insight -->

## What I'd watch:

Three things, in the order a finance team meets them.

- **Actions per resolution:** nobody prints this. Not the rate card, not the panel data, not the surveys. The first firm to report it holds the only rate that turns steps into outcomes.
- **The step cap in the contract:** the price per action is public and fixed. The count is neither. A cap per request turns a design choice into a budget line a planner can forecast against.
- **The unit on the estimate:** a share of infrastructure spend cannot be checked against an action meter. Cost per resolved request can, because it divides the meter by the work.

The 44% of chief executives who struggle to show AI-driven financial returns are asking for that division [3]. Gartner's own advice to them is to measure outcomes and unit economics rather than AI activity [3]. Unit economics needs a bottom number. Actions per request is the one the bill already holds.

<!-- nuanced-takeaway -->

## The catch

I could be wrong about how typical those examples are. They are pictures a vendor chose, not an audit of live traffic. A five-action request may sit closer to the median than to the edge.

The 21%-against-3.02% gap is also partly a matter of definition. AI bundled inside a software subscription is real spend that no cloud bill will show. The finance leaders may be describing the whole estate. The pulse measures only the part it can see.

What survives both caveats is the mismatch itself. A budget in shares, a bill in actions and a board deck in outcomes are three units. The middle one is now climbing fast: AI's share of the median bill posted its largest monthly gain on record, and the top quartile sits above one dollar in eight [2]. Fast growth in a unit nobody budgets is how a forecast error turns into a governance problem.

<!-- tldr -->

## At a glance

- **The Big Shift:** AI is now billed per action, and the vendor's own worked examples price one customer request at anywhere from one action to five. The budget, meanwhile, is still a share of infrastructure spend, and the two units do not convert.
- **Why It Matters:** AI reached 3.02% of the median cloud bill in September, the largest monthly jump on record, while finance leaders put it at 21% to 35% of infrastructure spend. That spread is why a return is hard to show.
- **What I'd watch:** the numbers that would tie the meter to the work.
  - **Actions per resolution:** the count of agent steps behind one closed ticket, which no vendor and no survey prints.
  - **Step cap per request:** a contract limit on actions, which turns a design choice into a line a planner can forecast.
  - **Cost per resolved request:** the bill divided by finished work, which is the bottom number a unit-economics review needs.
- **The Catch:** the examples are pictures, not live traffic, and part of the estimate-versus-bill gap is definitional, because bundled AI never shows on a cloud bill.

## Sources

[1] Salesforce, "Agentforce Pricing" and the Agentforce rate card (list prices observed 2026-10-22) — https://www.salesforce.com/agentforce/pricing/
[2] CloudZero, "Your AI Economics Pulse for October 2026" (2026-10-13) — https://www.cloudzero.com/blog/ai-economics-pulse-october-2026
[3] Gartner, "Gartner Says 44% of CEOs Struggle to Demonstrate AI Financial Returns as Technology Becomes Central to Growth" (2026-10-20) — https://www.gartner.com/en/newsroom/press-releases/2026-10-20-gartner-says-44-percent-of-ceos-struggle-to-demonstrate-ai-financial-returns-as-technology-becomes-central-to-growth
[4] Gartner, "Gartner Survey Finds Only 13% of CIOs Say Their Enterprise Has Realized Significant or Transformational Value from AI" (2026-10-19) — https://www.gartner.com/en/newsroom/press-releases/2026-10-19-gartner-survey-finds-only-13-percent-of-cios-say-their-enterprise-has-realized-significant-or-transformational-value-from-ai
