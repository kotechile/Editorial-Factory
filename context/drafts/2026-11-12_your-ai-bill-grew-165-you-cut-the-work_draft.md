---
title: "Your AI Bill Grew 1.65%: You Cut the Work"
vertical: enterprise_ai_finops
kind: news
persona: enterprise_cai
synthesis: true
sources:
  - https://ramp.com/data/ai-index-nov-2026
  - https://www.cloudera.com/about/news-and-blogs/press-releases/2026-10-26-the-ai-scale-trap-why-89-of-enterprises-are-forced-to-redesign-ai-use-cases-amid-rising-costs.html
one_big_thing: "AI spending across US businesses on Ramp set a record in October but rose only 1.65% while the price of a million tokens fell 21% — and the survey evidence says the flat bill was bought by shrinking the work per task, mostly by teams that cannot see token cost as it happens."
date: 2026-11-12
slug: your-ai-bill-grew-165-you-cut-the-work
meta_description: "AI spending set a record in October and rose 1.65% while a million tokens got 21% cheaper. The flat bill was bought by cutting the size of the work."
---

<!-- lead -->
Your AI bill grew 1.65% in October, a record month for AI spending across United States businesses on Ramp, while the average price of a million tokens — the units a model bills by — fell 21% [1]. A bill that flat, in a month when the unit got a fifth cheaper, has to be explained somewhere other than the price list. Cloudera's survey of 1,500 technology leaders finds the explanation: 89% say they have already limited or redesigned AI use cases because of rising token use, and 40% did it by running the model less often, using a smaller model, feeding it less text or asking for shorter answers [3]. My reading is that the saving came out of the work.

<!-- tldr -->

## At a glance

- **The shift:** AI spending hit a record in October but rose 1.65% as tokens got 21% cheaper [1].
- **The number:** 40% of leaders cut call size or frequency [3].
- **The risk:** only 19% track token cost, so a smaller call hides a worse answer [3].

<!-- tension -->

## When bill and price part ways

The bill climbed through the summer and then stopped. Token spend rose 42% in July, grew 1.5% across August and September together, and added 1.65% in October [1]. The unit price kept falling the whole time. Ramp's blended average dropped 21% in October [1]. A week later, Silicon Data's index, which tracks what buyers actually pay across more than 200 models, printed $0.83 per million tokens, 7% below its reading seven days before [5].

Divide the two readings and the shape appears. 1.0165 divided by 0.79 is about 1.29, so use rose roughly 29% in a month when the bill barely moved. I did that arithmetic myself, and it is not Ramp's figure: the two series sit on different samples: the 1.65% is total AI spending on Ramp's card base, while the 21% is an average price from the smaller token panel [1]. The direction is what matters. Buyers used a quarter more and paid about the same.

Who paid is lopsided. Ramp's customer base is a barbell. Just 1% of businesses account for 80% of the money OpenAI and Anthropic earn there, and Ramp's economist calls that group mostly venture-backed firms in tech, finance and technical services [1]. The median firm spends $16.32 per employee a month on AI. The top 1% spend $10,200, which is 625 times as much by simple division [1]. A market that thin can look flat at the top while the middle never really starts.

Cloudera's numbers say what carried the extra use and what paid for the flat bill. Forty-five percent of respondents moved a workload to another cloud, a private system or their own hardware; 40% ran the model less often, used a smaller one, fed it less text or asked for shorter answers; 24% paused or dropped a use case [3]. That is not purchasing. It is product design under a cost cap.

The same study says why the cap binds. Only 19% watch token and inference cost as it happens [3]. A team that cannot see the meter has one cheap lever: send less. And 58% say the value their AI work creates is roughly equal to its cost, while 23% say it is greater [3]. When most teams only break even, a smaller call is the fastest way to make the ratio look better.

## By the numbers

- **$0.83 a million tokens:** Silicon Data's market index on 8 November, down 7% in a week [5].
- **625x:** The gap between the top 1% of firms' monthly AI spend per employee, $10,200, and the median firm's $16.32 [1].
- **69.5% of spend:** Frontier models' share in October, a share that rose while the total bill flattened [1].

<!-- tactical-insight -->

## Where the next invoice comes from

The people closest to the bill are already pricing the next front. Engineering drove 72% of the spend Ramp can tag to a department in October, and Ramp says that spending stutters along despite rising use [1]. Customer success and support supplied the growth instead: 13.3% of tagged spend in October, against 0.8% in June [1]. Ramp's economist expects that work, which looks like customer-service chatbots, to run on cheaper and faster models rather than the priciest tier [1]. A vendor watching its best customer stall will push volume toward departments that pay less per token.

What I would watch next is the mix, not the total. Frontier models took 69.5% of spend in October, up from 67.7% the month before [1]. The mix moved toward the priciest tier even as the bill flattened, which is the opposite of what a pure cost-cutting story predicts. The firms that can afford the top tier still buy it. The ones cutting context and output do not, and the two groups are close to disjoint.

The meter matters more than the decision. Forty-five percent of the 1,500 leaders moved a workload to a different system to control cost [3]. That is a fair move when quality is measured and a risky one when it is not, and four in five cannot see the cost side as it happens, let alone the quality side. This desk has priced the pure price story before — [token prices hit record lows while enterprise AI bills did not](/token-price-record-low-budget-overrun/) — and the lesson then was that a falling unit price never reaches a bill nobody has attributed.

<!-- nuanced-takeaway -->

## The catch

The two anchors do not measure the same thing, and I have not pretended otherwise. Ramp's 1.65% is a spending total. Its 21% is a price average inside a panel that Ramp itself calls unrepresentative of its whole book, only directionally similar [1]. The 29% is a ratio of those two numbers, and a different mix could produce the same bill with less use and a higher price per call.

The 89% is soft in a second way. It comes from a survey Cloudera paid for, and "limited or redesigned" covers everything from a hard cap on one team to a cancelled programme [3]. Fifty-five percent of the same respondents raised AI spending [3], so the redesign is not a retreat. Cloudera sells a platform for exactly this problem, which makes the 19% the one finding that runs against its own sales pitch.

What keeps me on the thesis is the direction of the three series together: spending flat, price down a fifth, use up by roughly a quarter. A buyer who books that as efficiency has booked a saving he cannot separate from a workload that got worse. Next time a FinOps review reports a flat bill — and FinOps is the team that manages technology spend — the question is not what the price did. It is which calls got smaller, and who checked whether the smaller answer was still good.

## Sources

- [1] Ara Kharazian, "New Fronts in the AI Trade", Ramp AI Index, November 2026 — https://ramp.com/data/ai-index-nov-2026
- [2] Cloudera, "The AI Scale Trap: Why 89% of Enterprises Are Forced to Redesign AI Use Cases Amid Rising Costs", press release, 26 October 2026 — https://www.cloudera.com/about/news-and-blogs/press-releases/2026-10-26-the-ai-scale-trap-why-89-of-enterprises-are-forced-to-redesign-ai-use-cases-amid-rising-costs.html
- [3] Cloudera, "The State of Enterprise AI: What It Really Takes to Scale Enterprise AI", 26 October 2026 — https://www.cloudera.com/blog/business/the-state-of-enterprise-ai--what-it-really-takes-to-scale-enterprise-ai.html
- [4] Rebecca Bellan, "Ramp data shows AI spending stalling just as Anthropic nears its IPO", TechCrunch, 6 November 2026 — https://techcrunch.com/2026/11/06/ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo
- [5] Silicon Data, "LLM Token Expenditure Index (SDLLMTK)", reading dated 8 November 2026 — https://www.silicondata.com/products/silicon-index/llm-token-expenditure-index
