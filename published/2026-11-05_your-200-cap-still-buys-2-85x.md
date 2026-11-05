---
title: "Your $200 Cap Still Buys 2.85x"
vertical: enterprise_ai_finops
kind: news
persona: enterprise_cai
one_big_thing: "A daily dollar budget is written in the one input whose price is falling fastest, so Apple's cut from $300 to $200 still raises the tokens each engineer can buy by about 2.85 times — and the firm that stopped rationing the seat did it by cutting the cost of the supply, not the ceiling."
date: 2026-11-05
slug: your-200-cap-still-buys-2-85x
synthesis: true
sources:
  - https://www.theregister.com/ai-and-ml/2026/11/03/british-fintech-revolut-slashes-ai-coding-costs-10x-by-cutting-out-claude-and-going-self-hosted/5307345
  - https://www.macrumors.com/2026/11/04/apple-reducing-employee-ai-spending/
meta_title: "Your $200 Cap Still Buys 2.85x"
meta_description: "Apple cut its daily AI budget from $300 to $200 while the price of the tokens behind it fell 77%, so the cut bought 2.85 times as many tokens as the old cap did in May."
---

<!-- lead -->
Apple cut the daily budget some of its engineers may spend on artificial intelligence last month [3][4]. The work that budget buys still went up, because the price of what it buys fell more than twice as fast as the cap did [5][18]. The cap fell from $300 a day to $200 a day, according to people Bloomberg spoke to [3][4]. Further cuts toward $100 are planned, and some teams could fall to $25 [4]. The reported price for a million of Anthropic's tokens dropped to $0.62 in October from $2.65 in May, a 77% fall in under five months [5]. Put the two together, and $200 buys about 2.85 times as many tokens as the old $300 cap bought in May [18].

<!-- tension -->
## Why a dollar cap leaks

A cap is a quantity written in money, and money is the one term here that will not hold still. When the unit price falls 77% in five months, the same dollars buy a different number of tokens [5]. Apple cut its budget by a third over the same stretch and still ended with a looser rule than the one it started from. That is a sum, not a policy.

I read the two companies' numbers as one problem, and Revolut's record is the useful half. The bank gave coding tools to about 2,000 engineers under strict budgets, after seeing people spend $1,000 to $10,000 a month with little return, and then watched what a tight cap does to behaviour [1]. Engineers began saving tokens for the hardest task instead of spending them on the work around the code. That surrounding work — inbox, Jira, Confluence — is where the bank's lead-time gain came from [2].

A cap this loose is not a waste, and it is not a saving either. It is a decision about which work gets delegated, taken by committee and reviewed quarterly. That is the part a dollar cap cannot see. It counts the demand it cuts and never the tasks it puts off, so the saving is real and the lost work stays invisible.

## By the numbers

- **2.85x — the budget in tokens:** $300 at May's price bought about 113 million tokens a day, and $200 at October's price buys about 323 million, the desk's own sum on that index [18].
- **4.3x — the unadjusted ceiling:** when the unit price falls 77%, a cap nobody touches lets through about 4.3 times the usage it did in May, the desk's own sum on that price fall [18].
- **$0.30 — blended cost of self-hosting:** Revolut's figure for serving the open-weight Z.ai model on its own chips, about a tenth of what the bank had paid OpenAI and Anthropic [1].

<!-- tactical-insight -->
## What the operators did next

Revolut stopped rationing the seat and cut the cost of supply instead. It says it cut its AI coding inference cost by roughly 90% in under a year by making self-hosted models the default [1]. The model runs on 56 Nvidia B200 chips and serves about 2,000 engineers [2]. The gain that mattered came from tuning, not more chips: 76% more requests a second, and a first token in 1.68 seconds against 14.26 during the move [2]. It also holds the context window at 256,000 tokens and targets a first token in under three seconds [1].

Apple is moving the other way, and it is not alone. Teams are told to use cheaper models or on-device AI, and a larger allowance now needs a senior executive's exemption [3][4]. Uber caps a developer's coding-tool spend at $1,500 a month. Tesla sets a weekly limit, so two engineers at two firms can face the same model at very different prices [6]. I keep landing on the gap between the two controls: one changes the cost of the task, the other only records what was spent. What gets renewed is [the AI coding seat](/ai-coding-seats-measure-or-renew/), not the task.

<!-- nuanced-takeaway -->
## Where this breaks

The honest caveat sits in Apple's own reporting: some people said few of them used the whole old limit, so the saving from the cut may be small [3]. If the cap was never binding, the cut is a signal about spending rather than a change in it. The token sum describes a budget, not a bill.

Revolut's figures carry their own caveats. Its 60% coding-time and 70% lead-time gains are self-reported, and its internal comparison does not separate the model change from the removal of the usage limits [7]. Some of the gain may be the cap coming off rather than the model going in. The $0.30 blended rate describes its own setup and use, not a price another firm can assume [2].

The price index is the weakest link. It is a reported figure whose model mix and list-or-blended status are not disclosed, so I read the 2.85 as a direction, not a number [18]. Cutting the cost of supply is not cheap: it needs chips, serving engineers and rule work that a mid-size firm cannot staff. That is why the cap outlives its usefulness in the org chart.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Half Your Tokens: 5% of Your Bill" -> /half-your-tokens-5-of-bill/ [same site (aichieve.net); same category; topical overlap: artificial, intelligence] Link "Half Your Tokens: 5% of Your Bill" in the section where the article touches artificial, intelligence. -->
<!-- internal-link hint: "One Green Run Is Not Reliability" -> /agent-reliability-pass-k-not-one-green-run/ [same site (aichieve.net); same category; topical overlap: artificial, intelligence] Link "One Green Run Is Not Reliability" in the section where the article touches artificial, intelligence. -->
<!-- internal-link hint: "$2.7 Trillion AI Bill Just Turned Cost Control Into a Buying…" -> /ai-spend-27t-cost-visibility-mandate/ [same site (aichieve.net); same category; topical overlap: artificial, intelligence] Link "$2.7 Trillion AI Bill Just Turned Cost Control Into a Buying…" in the section where the article touches artificial, intelligence. -->
## Related reading

- [Half Your Tokens: 5% of Your Bill](/half-your-tokens-5-of-bill/)
- [One Green Run Is Not Reliability](/agent-reliability-pass-k-not-one-green-run/)
- [$2.7 Trillion AI Bill Just Turned Cost Control Into a Buying…](/ai-spend-27t-cost-visibility-mandate/)
<!-- internal-links:end -->

<!-- tldr -->
## At a glance

**The shift:** Apple cut its daily AI budget while the price of tokens fell 77%, so the new cap admits more work than the old one.
**The number:** $200 buys about 2.85 times the tokens $300 bought in May.
**The risk:** If the cap was never binding, the saving is small and the unmeasured loss is the work engineers stop handing over.

## Sources

[1] The Register, "British fintech Revolut slashes AI coding costs 10x by cutting out Claude and going self-hosted", 2026-11-03 — https://www.theregister.com/ai-and-ml/2026/11/03/british-fintech-revolut-slashes-ai-coding-costs-10x-by-cutting-out-claude-and-going-self-hosted/5307345
[2] AI Engineer NYC 2026, "Shipping like a startup, regulated like a bank" (David Abitbol, Revolut), session transcript, 2026-10-13 — https://ai.engineer/nyc/2026/talks/revolut
[3] MacRumors, "Apple is Putting Employees on an AI Budget", 2026-11-04 — https://www.macrumors.com/2026/11/04/apple-reducing-employee-ai-spending/
[4] Channel NewsAsia / Reuters, "Apple cuts employee AI budgets in cost-control push, Bloomberg News reports", 2026-11-05 — https://www.channelnewsasia.com/business/apple-cuts-employee-ai-budgets-in-cost-control-push-bloomberg-news-reports-6525411
[5] Tom's Hardware, "Firm that lets you rent out your idle Mac for AI inference workloads warns of plummeting token costs", 2026-10-31 — https://www.tomshardware.com/tech-industry/artificial-intelligence/firm-that-lets-you-rent-out-your-idle-mac-for-ai-inference-workloads-warns-of-plummeting-token-costs-darkbloom-network-sees-earnings-drop-to-usd1-23-a-day-as-anthropic-tokens-fall-77-percent
[6] MacDailyNews, "Apple reduces employee AI spending caps in bid to rein in costs", 2026-11-04 — https://macdailynews.com/2026/11/04/apple-reduces-employee-ai-spending-caps-in-bid-to-rein-in-costs
[7] Dealroom, "Revolut moves 2,000 engineers onto self-hosted AI, cutting coding costs 90%", 2026-11-04 — https://dealroom.co/news/169124-revolut-moves-2-000-engineers-onto-self-hosted-ai-cutting-coding-costs-9
[18] Derived arithmetic for this article: $300 ÷ $2.65 per million = about 113 million tokens; $200 ÷ $0.62 per million = about 323 million; 323 ÷ 113 = 2.85.
