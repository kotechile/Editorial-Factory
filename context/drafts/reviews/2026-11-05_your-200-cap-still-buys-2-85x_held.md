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
Apple cut the daily budget that some of its engineers may spend on artificial intelligence last month, and the amount of work that budget buys still went up. The cap fell from $300 a day to $200 a day, with further cuts toward $100 planned and some teams facing a $25 limit, according to people Bloomberg spoke to [3][4]. The price of what the budget buys fell harder: the listed price for a million Anthropic tokens dropped 77% in under five months [5]. Put the two together and the new $200 cap buys about 2.85 times as many tokens as the old $300 cap did in May [18]. The result is a cut in the budget that behaves like a raise in the work.

<!-- tension -->

## Why a dollar cap leaks

Dollar caps are written in the one input whose price will not hold still. When a token's unit price falls 77% in five months [5], a ceiling nobody touches admits about 4.3 times the usage it did in spring, because the same dollars now buy a different number of tokens. Apple cut its budget by a third over the same stretch and still ended with a looser rule than it started from, which is arithmetic rather than policy.

I keep coming back to the price changing under both firms, and Revolut's record is the useful half. The bank gave coding tools to about 2,000 engineers under strict budgets, after seeing people spend $1,000 to $10,000 a month with little return [1]. Then it watched what a tight cap does to behaviour [2]. Engineers began saving tokens for the hardest task instead of spending them on the work around the code. That surrounding work is where the bank's lead-time gain came from: debugging, and the Jira and Confluence tickets that sit between a merged change and a live one [2].

## By the numbers

- **$2.65 → $0.62 — token price index:** the listed price for a million Anthropic tokens from May to October 2026, a 77% fall that no per-seat budget was reset against [5].
- **2.85x — the budget in tokens:** $300 at May's price bought about 113 million tokens a day, and $200 at October's price buys about 323 million, the desk's own sum on that index [18].
- **$0.30 — blended cost of self-hosting:** Revolut's figure for serving an open-weight Z.ai model on its own chips, about a tenth of what the bank had paid OpenAI and Anthropic [1].

<!-- tactical-insight -->

## What the operators did next

Revolut stopped rationing the seat and cut the cost of supply instead. It serves the model on 56 Nvidia B200 chips for about 2,000 engineers. The gain that mattered came from tuning rather than more hardware: 76% more requests per second, and a first token in 1.68 seconds against 14.26 during the move [2]. It also holds the context window at 256,000 tokens, on the view that a longer one costs more memory than it returns [1].

Apple is moving the other way, and it is not alone. Teams are being asked to use cheaper models or to move work onto the device, and a bigger budget now needs a senior executive's approval [3][4]. Uber caps a developer's spend on coding tools at $1,500 a month, and Tesla sets a weekly limit. Two engineers at two firms can face the same model at very different prices [6].

What I would watch next is whether the seat budget changes the choice of work rather than just recording the spend. A seat budget tells finance what was spent; it never says what a finished task costs. The unit a finance team is being asked to approve is the [AI coding seat measured against the renewal decision](/ai-coding-seats-measure-or-renew/).

<!-- nuanced-takeaway -->

## Where this breaks

The Apple side carries its own caveat: some people told Bloomberg that few employees used the whole old limit, so the saving from the cut may be small [3]. If the cap was never binding, the cut is a signal about spending rather than a change in it, and the token sum above describes a budget, not a bill.

Revolut's figures carry their own caveats: its 60% coding-time and 70% lead-time gains are self-reported, and its internal comparison does not separate the model change from the removal of the usage limits. Part of the gain may be the cap coming off rather than the model going in [7]. The $0.30 blended rate describes its own setup and use, and is not a price another firm can assume [2].

The price index is the weakest link, because its model mix and list-or-blended status are not disclosed. So I read the 2.85 as a direction rather than a number [5]. Cutting the cost of supply is not cheap: it needs chips, serving engineers, and rule work that a mid-size firm cannot staff. That is why the cap outlives its usefulness in the org chart.

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
