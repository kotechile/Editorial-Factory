---
title: Your 25-Minute Review Costs $66.67
vertical: enterprise_ai_finops
persona: enterprise_cai
one_big_thing: "A review minute is priced by the reviewer's wage, not the model's rate card: the same 25 minutes of checking costs $12.60 at a paralegal's median wage and $66.67 at a partner's billed rate, so a review ceiling in minutes — not the token price — decides whether the automation beats the manual process."
date: 2026-10-22
slug: review-minute-costs-66-dollars
archetype: evergreen
evergreen: true
---

<!-- lead -->
Eighteen cents of tokens per agreement, then 25 minutes of a senior partner's time at $160 an hour. Your 25-minute review costs $66.67, and against the manual paralegal review it replaced, that put the whole automation at 2.4 times the cost. The model was never the expensive part. The pay grade doing the checking was.

<!-- tension -->

## The big picture:

The token line on an AI bill is falling. The review line on the same bill is not.

Claude Opus 5.5 bills $4 per million input tokens and $20 per million output tokens, with cache hits at 20 cents per million [5]. OpenAI's gpt-6.1-sol sits at $2.00 and $10.00 per million on its standard lane [6]. Those are the numbers quoted in board decks, and they are the only line that keeps shrinking.

Human checking is priced somewhere else: the labour market. O*NET (the US Department of Labor's occupation database) puts the median wage for paralegals and legal assistants at $30.24 an hour, $62,890 a year [1]. That works out at $0.50 a minute.

The same 25 minutes of checking is $12.60 at that wage and $66.67 at the partner's rate, for the same work on the same document. What strikes me is that both numbers are true at once.

The automation did not fail. It was priced at the wrong grade.

The other half of this is that nobody can estimate review time from the inside. A controlled trial by METR (a research nonprofit) had 16 experienced developers finish 246 tasks, some with early-2025 Artificial Intelligence (AI) tools allowed and some without [4]. With the tools, they took 19% longer.

Afterwards those same developers said the tools had made them 20% faster. The people doing the checking were the last to know it was slow, and that is the number I would put next to any pilot's self-reported saving.

## By the numbers

- **$30.24 an hour — Paralegal median wage:** The 2025 median for paralegals and legal assistants, or $0.504 a minute, which makes 25 minutes of checking $12.60 [1]
- **$38.81 an hour — Compliance officer median:** The middle grade a compliance-gated workflow staffs its reviewer at, and $0.65 a minute [2]
- **$21.53 an hour — Service rep median:** The floor grade for an output class a simple check can clear, at $0.36 a minute [3]
- **19% slower — Measured AI slowdown:** 16 developers across 246 tasks took longer with AI tools while believing they had saved 20% [4]

<!-- tactical-insight -->

## What I'd watch:

The number I keep coming back to is a ceiling in minutes, not a rate. Start from the manual cost per unit, take out the token cost, then divide by the price of a review minute. On our field note the manual baseline comes to $27.85 an agreement, with 18 cents of tokens on the other side of the line.

- **$160 an hour:** The ceiling is 10.4 minutes. The pilot spent 25, which is why it lost.
- **$38.81 an hour:** 42.8 minutes, so a compliance officer can spend well over half an hour on the same document and still come in under the manual cost [2].
- **$30.24 an hour:** 54.9 minutes, more than five times the ceiling at the partner's rate [1].
- **$21.53 an hour:** 77.1 minutes, the widest ceiling on the ladder, for output a simple check can genuinely clear [3].

Same agreement, same checking work. Between the partner's desk and the paralegal's, the ceiling moves by a factor of 5.3.

What I am watching next is whether a vendor publishes review minutes per resolved unit beside the token spend. My read is that the first one to do it will be selling against a rival whose per-task cost only looks lower because the customer's own staff absorb the checking.

The second thing is the wage tables. Token prices move in quarters, and median wages are republished once a year. A steep token cut against a flat wage still pushes the review share of the bill up.

<!-- nuanced-takeaway -->

## The catch

The ceiling is not a licence to hand the document to the cheapest person in the building. Our field note's fix was a rule-based check on the clauses that kept getting invented, not a junior reviewer. A badly checked indemnity clause costs more than the review ever would.

The wage comparison is not like for like either. O*NET prints median wages, not loaded cost. Employer taxes, benefits and overhead sit on top of that $30.24, while a $160 billed rate carries the firm's margin as well.

My read is that the real gap is narrower than 5.3 times once both sides are costed the same way, and still wide enough to change which grade sits on the review. The METR result is about software developers on early-2025 tools, not about anyone's contract desk. I would not move that 19% into a legal workflow; I would use it for the one thing it does show, which is that self-reported review time runs optimistic.

<!-- tldr -->

## At a glance

- **The Big Shift:** The token line on an AI budget is falling while the review line is priced by the labour market, so the person who checks the output decides the per-unit cost. The same 25 minutes of review costs $12.60 at a paralegal's median wage and $66.67 at a partner's billed rate.
- **Why It Matters:** Cost per resolved work unit is what a finance team actually approves, and a pilot can look cheap per token while costing 2.4 times the manual process it replaced. The review minute is the line that decides it.
- **What I'd Watch:** I am watching for a review-minute figure published next to token spend, and for the annual wage tables that reset the arithmetic.
  - **Review ceiling:** The most minutes a check can take before the automation costs more than the manual baseline; it moves by a factor of five between a partner and a paralegal.
  - **Measured review time:** Time spent checking, measured rather than estimated, because the trial found developers 19% slower while they believed they were 20% faster.
  - **Reviewer grade:** Which pay grade is qualified to clear which error class, which moves the ceiling more than the model choice does.
- **The Catch:** Cheap reviewers have to be qualified, median wages are not loaded employer costs, and the slowdown evidence comes from software work rather than legal review.

## Sources
[1] O*NET OnLine, "23-2011.00 — Paralegals and Legal Assistants", median wages (2025). https://www.onetonline.org/link/summary/23-2011.00
[2] O*NET OnLine, "13-1041.00 — Compliance Officers", median wages (2025). https://www.onetonline.org/link/summary/13-1041.00
[3] O*NET OnLine, "43-4051.00 — Customer Service Representatives", median wages (2025). https://www.onetonline.org/link/summary/43-4051.00
[4] Becker, Rush, Barnes and Rein, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", arXiv:2507.09089v2. https://arxiv.org/abs/2507.09089
[5] Anthropic, "Pricing", Claude platform documentation. https://docs.claude.com/en/docs/about-claude/pricing
[6] OpenAI, "Pricing", platform documentation. https://platform.openai.com/docs/pricing
