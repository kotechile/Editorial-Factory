---
title: Token Prices Hit a Record Low. The AI Budget Didn't.
vertical: enterprise_ai_finops
persona: enterprise_cai
one_big_thing: "As token prices fall to a record low, vendors reprice on speed, allowance and volume — so the enterprise AI bill keeps climbing, and the only lever that changes it is a ceiling tied to a resolved work-unit."
date: 2026-10-08
slug: 2026-10-08_token-price-record-low-budget-overrun
synthesis: true
sources:
  - https://www.silicondata.com/products/silicon-index/llm-token-expenditure-index
  - https://futurumgroup.com/insights/enterprise-ai-overruns-hit-46-9-is-the-reckoning-in-fy2027
---

<!-- lead -->
Silicon Data's token-price index printed $0.96 per million tokens on Oct. 4 — the first reading under a dollar, and the cheapest a token has been tracked [1]. Five days earlier, OpenAI put a $500-a-month price on its fastest ChatGPT seat [3]. I think both moves are the same repricing, and neither one shows up in the per-token budget a chief financial officer (CFO) signed off.

<!-- tension -->
## The big picture:

The index is the cleanest single number for what the market pays for a token, and by that measure intelligence is close to free. It crossed below a dollar this month and sits more than half below its summer high [1][2]. The easy reading is that Artificial Intelligence (AI) is getting cheaper to run.

The bills say otherwise. In Futurum's second-half survey of technology buyers, 46.9% of enterprises ran over budget on AI, and only 5.6% came in under plan [4]. CloudZero's panel tells the same story from a different angle: the top quarter of companies now spend more than a tenth of their cloud bill on AI, a line that moved in a single month [5].

What strikes me is that the price of the input and the size of the bill are not moving together. They are moving apart. The reason shows up on the pricing page: the bill was never metered in the one number the buyer watches.

OpenAI makes the split concrete. Its seats cost $100, $200 and $500 a month, and the fastest mode — the one called Ultrafast — is sold only with the $500 plan [3]. The same week, the $200 plan lost included usage for new customers, at the same price [3]. So the vendor stopped competing on the cost of a token and started charging for speed and allowance. A token meter cannot see either one.

## By the numbers

- **$0.96 — Token price at a record low:** Silicon Data's index fell under a dollar for the first time on Oct. 4 and sits more than half below its summer peak [1][2].
- **46.9% — Enterprises over budget on AI:** Only 5.6% came in under plan, and 10% had no formal AI budget to measure against [4].
- **47.6% — Overruns that got more money:** The most common response to an overrun was to ask for supplemental funding, not to slow the work [4].
- **11.12% — AI's share of the cloud bill, top quartile:** The 75th percentile crossed a tenth of cloud spending, up from 9.63% a month earlier [5].

<!-- tactical-insight -->
## What I'd watch:

The part I keep circling is what companies do once the overrun lands. Futurum found that 47.6% went back for more money and 43.3% pushed the gap into the next planning cycle; only about one in six cut or paused the work [4]. Nearly four in ten moved money from elsewhere in the tech budget, and almost a quarter parked the spend on a unit that was not the tech department [4].

That is funding the growth and hiding the size of the gap, not controlling the cost. It also shifts who owns the decision, because the business unit that pays part of the bill tends to shape the next renewal.

Three signals I have been watching from here:

- **The meter over the price:** vendors bill on speed tiers, usage allowances and volume. I want to know which enterprises renegotiate those lines instead of chasing a cheaper token.
- **The ceiling:** a fixed cap per team, per agent or per finished task is the one lever that moves the total. The number I want is how many firms have one, and how they set it.
- **The work-unit:** cost per finished job — a ticket closed, an invoice processed — is the figure a finance team can act on. Token totals are not.

<!-- nuanced-takeaway -->
## The catch

I could be wrong that price and bill are decoupled everywhere. A team running short, simple prompts really does save money when the rate falls, and some of the 46.9% overruns are just healthy new adoption rather than waste.

The catch is the direction of the incentive. When a unit gets cheaper, people buy more of it, and an agent re-sends its whole context on every step, so one job can burn many times the tokens of a single question. A lower rate makes more of those jobs look affordable, and each new job is a line finance never modeled. Cheaper tokens can lower the unit cost and still raise the bill; only a ceiling tied to finished work tells you which one is happening.

<!-- tldr -->
## At a glance

- **The Big Shift:** Token prices hit a record low this month while enterprise AI budgets overran — 46.9% of firms went over in the latest survey. The two are the same story, because vendors now charge for speed and usage, not just tokens.
- **Why It Matters:** If the rate card is falling but the bill is climbing, a budget built on cheaper tokens is a forecast built on the wrong number. The gap lands first on the tech budget, then on the business units.
- **What I'd Watch:** I am watching how companies change the meter, not the price.
  - **The ceiling:** a hard cap per team or per agent — the one lever that changes the total.
  - **The work-unit:** cost per finished job, such as a ticket closed, which a finance team can act on.
  - **The allowance line:** what vendors charge for speed and volume once the token gets cheap.
- **The Catch:** The decoupling is not uniform. Short, simple workloads still get cheaper as the rate falls, and some overruns are healthy adoption. The risk is that a falling rate quietly funds the experiments nobody budgeted for.

## Sources
[1] Silicon Data — "LLM Token Expenditure Index" (reading as of October 4, 2026) — https://www.silicondata.com/products/silicon-index/llm-token-expenditure-index
[2] CNBC — "Artificial intelligence token prices are hitting new record lows" (September 1, 2026) — https://www.cnbc.com/2026/09/01/ai-token-prices-lows.html
[3] OpenAI — "About ChatGPT Pro tiers" (DevDay, September 29, 2026) — https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers
[4] Futurum Research — "Enterprise AI Overruns Hit 46.9%: Is the Reckoning in FY2027?" (September 14, 2026) — https://futurumgroup.com/insights/enterprise-ai-overruns-hit-46-9-is-the-reckoning-in-fy2027
[5] CloudZero — "Your AI Economics Pulse for September 2026" (September 8, 2026) — https://www.cloudzero.com/blog/ai-economics-pulse-september-2026
