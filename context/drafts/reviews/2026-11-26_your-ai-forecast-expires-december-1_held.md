---
title: Your AI Forecast Expires December 1: the Bill Doubles
vertical: enterprise_ai_finops
kind: news
persona: enterprise_cai
one_big_thing: "Google doubles Gemini 4 Carbon's API price on December 1, and its own rate card says so. Most FinOps teams cannot tell which of their workloads are standing on the cliff."
date: 2026-11-26
slug: your-ai-forecast-expires-december-1
synthesis: true
sources:
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://www.finops.org/wg/token-economics-saas
---

<!-- lead -->
Your AI forecast expires on December 1. That is the day Google doubles the prices on the Gemini 4 Carbon API (the pay-per-call interface developers bill tokens through), and Google's own rate card has carried both dates since the model opened to paying developers [1]. Repricing the numbers takes an afternoon. Finding out which of your own workloads run on the model that just doubled is the part most teams cannot do, because the bills for those workloads do not say [2].

<!-- tldr -->
## At a glance
This article covers Google's scheduled December 1 doubling of Gemini 4 Carbon API prices. It is for finance and platform teams who own an AI budget, and it finds that the deadline is public while the list of exposed workloads is invisible on the bill.

<!-- tension -->
## A price on a calendar
The timeline is short and public. Google opened Gemini 4 Carbon to all paying developers on November 10 with a starting rate and a printed expiry [1]. The card states that input runs $2.00 per million tokens through November 30, then $4.00 [1]. Output moves to $20.00 the same day. Cached input moves to $0.20. The family's cheaper sibling, Gemini 4 Hydrogen, costs $1.50 per million input tokens with no end date on its row [1]. One model has a clock on its price; the other does not.

Two years of falling inference prices taught finance teams to wait out any rate and bank the next saving. A scheduled increase breaks that habit, and the FinOps Foundation — the industry body for technology cost management — explains in a working-group paper why the break lands so hard [2]. The paper, dated October 28, states that a model-provider bill shows token use "at most by API key, project, or workspace, with no concept of business unit, cost center, or application" [2]. The budget can be repriced quickly only if the spend can be traced to workloads. The paper's point is that the bill does not carry that grain unless the team built the tracking itself.

I checked the available guidance for a checkpoint that would have caught this, and found none. A November 6 forecasting guide from the vendor Kion tells teams to validate rates "whenever pricing, contracts, or model selection changes" [3]. That is a reactive control. Nothing in its six steps sets a calendar checkpoint for a rate change everyone could see a month out — which is exactly the case December 1 is.

## By the numbers
- Input, output and cached input rates for Gemini 4 Carbon all double on December 1 [1].
- 43% of buyers named proving what the spend returns as their hardest problem, in the September 2026 State of Tokenomics survey [2].
- Gemini 4 Hydrogen input costs $1.50 per million tokens, with no expiry printed on its row [1].

<!-- tactical-insight -->
## Where the exposure hides
The people closest to this are routing, not rebudgeting. The move mid-November write-ups converged on is simple to state: send easy requests to Hydrogen and route the hard ones to Carbon. The widening gap between the two rungs is a routing decision now, and the arithmetic explains why. A workload that draws 500 million input tokens and 100 million output tokens a month bills about $2,000 in November and $4,000 in December on the same usage — my calculation on the card's own rates, not a Google figure. Any client quote built on the November rate is too low by half once the calendar turns.

What I am watching is not the announcement but the December forecast-versus-actuals meeting. Teams that trace token spend to workloads will walk in with a difference they can explain line by line. Teams that cannot will see a variance arrive with no cause attached, and the working-group paper names why they stay stuck. In the September 2026 State of Tokenomics survey, 23 percent of buyers asked providers for more transparency and granular data, while only 4 percent asked for lower prices [2]. Buyers have already decided the rate card is not where their problem lives.

The paper also names another answer. Teams that run open-weight models on rented or owned GPUs pay no per-token charge — just compute, storage, network links and the platform team to run it [2]. That channel has no teaser window because it has no rate card. An earlier piece on [token prices halving while the CFO still can't read the bill](/token-prices-just-halved-the-cfo-still-cant-read-the-bill/) made the same point under falling prices. Here it cuts both ways: when prices can move in either direction, owning the meter helps on both moves.

<!-- nuanced-takeaway -->
## The catch
This should not read as a complaint about Google's pricing. A starting rate that steps up is a normal commercial device, and the change carried a month of public notice. My reading, held loosely: the constraint is not the forecast, it is the plumbing underneath it. The working-group paper states the limit itself — the fix is workload-level cost tracking built before the next card moves, not a sharper spreadsheet after. A published date only helps an organization that has assigned someone to read rate cards on a calendar.

## Sources
- [1] Google, "Gemini Developer API pricing" (rate card, observed 2026-11-26) — https://ai.google.dev/gemini-api/docs/pricing
- [2] FinOps Foundation working group, "Managing AI Token Costs from Direct Model Provider APIs", last updated 2026-10-28 — https://www.finops.org/wg/token-economics-saas
- [3] Kion, "How to Forecast AI Token Spend: A 6-Step Guide", 2026-11-06 — https://kion.io/blog/how-to-forecast-ai-token-spend

<!-- internal-links -->
