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
Your AI forecast expires on December 1. That is the day Google doubles the prices on the Gemini 4 Carbon API (the interface teams bill tokens through), and Google's own rate card has shown both dates since the model opened to paying customers [1]. Anyone can reprice the numbers in an afternoon. What most teams cannot do in an afternoon is find which of their own workloads run on the model that just doubled, because the bills for those workloads do not say [2].

<!-- tldr -->
## At a glance
This piece is for the finance and platform teams who own an AI budget: a public price deadline meets a gap in cost tracking, so a team can know the date the bill rises and still not know which of its workloads the rise lands on.

<!-- tension -->
## A price on a calendar
The timeline is short and public. Google opened Gemini 4 Carbon to all paying customers on November 10 with a starting rate and a printed expiry [1]. The card states that input runs $2.00 per million tokens through November 30, then $4.00 [1]. Output moves to $20.00 the same day. Cached input moves to $0.20. The family's cheaper sibling, Gemini 4 Hydrogen, costs $1.50 per million input tokens with no end date on its row [1]. One model has a clock on its price; the other does not.

Two years of falling inference prices taught finance teams to wait. The usual move is to revalidate rates at the next refresh and bank another saving. A scheduled increase breaks that habit, and the FinOps Foundation — the industry body for technology cost management — explains why the break lands so hard [2]. Its paper on token costs, dated October 28, states that a model-provider bill shows token use "at most by API key, project, or workspace, with no concept of business unit, cost center, or application" [2]. The budget can be repriced quickly only if the spend can be traced to workloads. The paper's point is that the bill does not carry that grain unless the team built the tracking itself.

The available guidance does not close this gap. A November 6 forecasting guide from the vendor Kion tells teams to validate rates "whenever pricing, contracts, or model selection changes" [3]. That is a reactive control. Nothing in its six steps sets a date to check a rate change everyone could see a month out — which is exactly the case December 1 is.

## By the numbers
- **2× on three lines:** Input, output and cached input rates for Gemini 4 Carbon all double on December 1 [1].
- **43% of buyers:** The share whose hardest problem is proving what the spend returns, in the September 2026 State of Tokenomics survey [2].
- **$1.50 per million:** The input price of Gemini 4 Hydrogen, the sibling with no expiry on its row [1].

<!-- tactical-insight -->
## Where the exposure hides
The routing answer is the one the card itself sets up. Easy requests can go to Hydrogen at its steady rate while the hard ones stay on Carbon [1]. The arithmetic shows what that choice is worth. Take a workload that draws 500 million input tokens and 100 million output tokens each month. In November it bills about $2,000. In December, with nothing changed, it bills about $4,000 — my calculation on the card's own rates, not a Google figure. Any client quote priced off the November rate will come in half too low.

What I would watch is not the announcement but the December review of forecast against actuals. Teams that trace token spend to workloads will walk in with a difference they can explain line by line. Teams that cannot will see a variance arrive with no cause attached. The FinOps paper names why they stay stuck. In the September survey it cites, buyers were asked what they want most from model providers, and 23% asked for more transparency while only 4% asked for lower prices [2]. Buyers, in other words, have already priced in that the rate card is not where their problem lives.

The paper also names another answer. Teams that run open-weight models on rented or owned GPUs pay no per-token charge — just compute, storage, network links and the platform team to run it [2]. That channel has no teaser window because it has no rate card. An earlier aichieve.net piece on [token prices halving while the CFO still can't read the bill](/token-prices-just-halved-the-cfo-still-cant-read-the-bill/) made the same point under falling prices. Here it cuts both ways: when prices can move in either direction, owning the meter helps on both moves.

<!-- nuanced-takeaway -->
## The catch
This should not read as a complaint about Google's pricing. A starting rate that steps up is a normal commercial device, and the change carried a month of public notice. The real limit is the one the FinOps paper states itself: the fix is not a sharper forecast, it is cost tracking at the workload level, built before the next card moves. A published date only helps a company that has assigned someone to read rate cards on a set schedule.

## Sources
- [1] Google, "Gemini Developer API pricing" (rate card, observed 2026-11-26) — https://ai.google.dev/gemini-api/docs/pricing
- [2] FinOps Foundation working group, "Managing AI Token Costs from Direct Model Provider APIs", last updated 2026-10-28 — https://www.finops.org/wg/token-economics-saas
- [3] Kion, "How to Forecast AI Token Spend: A 6-Step Guide", 2026-11-06 — https://kion.io/blog/how-to-forecast-ai-token-spend

<!-- internal-links -->
