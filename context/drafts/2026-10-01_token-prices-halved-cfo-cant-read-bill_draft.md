---
title: Token Prices Just Halved. The CFO Still Can't Read the Bill.
vertical: enterprise_ai_finops
persona: enterprise_cai
one_big_thing: "Cheaper tokens don't fix an unexplainable bill — the unit of account must move from cost-per-token to cost-per-resolved-work-unit."
date: 2026-10-01
slug: token-prices-halved-cfo-cant-read-bill
synthesis: true
sources:
  - https://openai.com/index/introducing-gpt-6-sol-and-luna/
  - https://www.anthropic.com/news/claude-opus-5-5
  - https://www.finops.org/insights/state-of-tokenomics-september-2026/
---

<!-- lead -->
OpenAI and Anthropic both cut frontier token prices on September 22 — OpenAI halved GPT-6 Sol and Luna, and Anthropic shipped Claude Opus 5.5 at 40% less to run than Opus 5 [1][2]. One day later, 472 enterprises told the Tokenomics Foundation what they actually wanted, and it was not a discount: only 4% asked providers for cheaper prices, while 23% asked for a bill they could explain to a CFO [3].

<!-- tension -->
I've been watching this all week, and the 4% figure is the part I keep circling. The two biggest labs raced the rate card toward zero on the same day, and the buyers shrugged. That is not a signal about price. It is a signal about what "cost" now means in enterprise AI.

**Why it matters:** the price card has stopped predicting the actual bill. A token rate no longer captures what enterprises actually spend on AI — the agent loops, cache-miss penalties, retries, tool calls, and human review that sit between a model call and a finished piece of work. OpenAI itself says the cut was paid for by "improvements in caching and inference" [1]; Anthropic is discounting cache reads specifically because they "make up the majority of agentic and coding work costs" [2]. In other words, the cost has already migrated to the infrastructure around the model. The token price is the one line item that is shrinking, and it was never the expensive part.

**The big picture:** the Tokenomics Foundation — a Linux Foundation project — reports that three in four enterprises cannot confidently prove AI business outcomes to the CFO, with 39% saying they can't connect AI spend to any measurable outcome their CFO would accept [3]. The bottleneck is not the numerator of the price. It is the absence of a denominator: what did we get for it?

**By the numbers:**
- **50%:** OpenAI cut GPT-6 Sol to $2/$10 and GPT-6 Luna to $0.10/$0.50 per million tokens, down from $4/$20 and $0.20/$1.20 [1].
- **40%:** Anthropic says Opus 5.5 costs 40% less to run than Opus 5 while matching its pricier Fable 5.1 on most work; cache reads fell 60% to $0.20 per million [2].
- **4% vs 23%:** the share of enterprises asking providers for cheaper prices versus the share asking for more granular, explainable data [3].
- **3 in 4:** enterprises that cannot confidently prove AI business outcomes to the CFO [3].

<!-- tactical-insight -->
Where this bites is in how the people closest to the story are reorganizing the accounting. The Tokenomics Foundation found that 88% of enterprises now have a named owner for AI economics, and that having one makes them 3.7× more likely to show the CFO real value [3]. I'd read that as the first structural fix landing: attribution before optimization.

- **Model routing is the fast lane.** 86% of enterprises are evaluating or already using a model router, and router users are 4× more likely to show CFO value [3]. The logic is simple: when you can send each task to the cheapest model that clears its bar, the price cut actually reaches the P&L instead of vanishing into a bigger token bill.
- **The ask is standardization, not price.** Only 4% asked for discounts. Seven percent wrote FOCUS — the open billing standard now used across cloud providers — into a free-text answer without being prompted [3]. A bill in one shared schema is worth more to a CFO than another 50% off.
- **The real metric is cost-per-resolved-work-unit.** What I'd watch next: whether vendors start publishing that denominator — cost per resolved ticket, per merged change, per accepted claim — the way they now publish cost per token. That is the number that turns "we cut prices" into "we can prove it."

<!-- nuanced-takeaway -->
**The catch:** none of this means the price cuts are irrelevant. A 50% cut on the token bill is real money for anyone already running a disciplined, attributed stack. My read is that the gap is widening in both directions at once: the leaders with model routing and a named cost owner capture every cent of the deflation, while the three-quarters of enterprises that can't prove AI outcomes to the CFO see the price drop and get no closer to a defensible ROI story [3]. I could be wrong that this forces a re-platforming, but the survey's own closing line is hard to argue with — enterprises are not asking providers to charge less; they are asking for a bill they can explain to a CFO [3].

<!-- tldr -->
- **The Big Shift:** OpenAI and Anthropic cut frontier token prices on the same day — September 22 — and buyers responded that price was never the problem. Only 4% asked for cheaper prices; 23% asked for a bill they can explain to a CFO.
- **Why It Matters:** Enterprise AI cost has already migrated past the token into agent loops, cache misses, and human review. The token price is shrinking while the real bill stays opaque, so cost-per-token has become a worse predictor of value, not a better one.
- **What I'd Watch:**
  - **Cost-per-resolved-work-unit:** whether vendors start reporting cost per completed task rather than cost per token, which is the denominator a CFO can actually hold someone to.
  - **FOCUS billing standardization:** the open schema 7% of enterprises name-checked unprompted — a shared bill is the precondition for cross-provider attribution.
  - **Model routing adoption:** 86% are already in it; router users are 4× more likely to show CFO value, so routing may be where the price cuts finally reach the P&L.
- **The Catch:** The deflation is real, but it only helps teams that already attribute spend to business units. For the three in four enterprises that can't prove AI outcomes to the CFO, a 50% token cut changes the price and nothing about the story.

## Sources
[1] OpenAI — "Introducing GPT-6 Sol and Luna" (September 22, 2026) — https://openai.com/index/introducing-gpt-6-sol-and-luna/
[2] Anthropic — "Introducing Claude Opus 5.5" (September 22, 2026) — https://www.anthropic.com/news/claude-opus-5-5
[3] Tokenomics Foundation — "State of Tokenomics, September 2026" (September 23, 2026) — https://www.finops.org/insights/state-of-tokenomics-september-2026/

<!-- linkedin -->
I've been following the September 22 model launches all week, and one number from the next day's survey stopped me.

OpenAI cut GPT-6 Sol and Luna in half on the same day Anthropic shipped Claude Opus 5.5 at 40% less to run than Opus 5. Big, real price deflation.

Then 472 enterprises told the Tokenomics Foundation what they actually wanted. Only 4% asked for cheaper prices. 23% asked for a bill they could explain to a CFO. Three in four can't prove AI business outcomes to the CFO at all.

My read: the price card has stopped predicting the bill. Cost has already moved into agent loops, cache misses, and human review — OpenAI says caching paid for the cut, Anthropic is discounting cache reads because they're "the majority of agentic and coding work costs."

What I take from it: the unit of account has to move from cost-per-token to cost-per-resolved-work-unit. Router users are 4× more likely to show CFO value; enterprises with a named AI-cost owner are 3.7× more likely.

I could be wrong that this forces re-platforming, but "we're not asking you to charge less — we want a bill we can explain" is hard to argue with.
