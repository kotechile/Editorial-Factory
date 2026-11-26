---
title: Your Pilot Needs a Scorecard: 95% Fail
vertical: enterprise_ai_finops
kind: evergreen
archetype: evergreen
evergreen: true
persona: enterprise_cai
one_big_thing: "95% of companies get no measurable return from generative AI pilots, and the models are not the problem. The fix is a one-page graduation scorecard with a dated payback threshold that a demo must clear before it earns production compute."
date: 2026-11-26
slug: your-pilot-needs-a-scorecard
---

<!-- lead -->
Your AI pilots are not dying because the model fails the demo: 95% of the companies in MIT's largest generative AI study get no measurable return from it, while the models keep improving [1]. The failure is organizational, and nothing written down decides whether a proof of concept graduates to production compute. So the decision is made on demo excitement and renewed quarter after quarter [1]. A chief information officer (CIO) who runs a dozen pilots a year needs a one-page scorecard, priced in labor hours, to settle the question before renewal season.

<!-- tldr -->
## At a glance
Enterprise teams keep launching GenAI pilots that never earn their keep. MIT found 95% deliver no measurable return. This piece gives budget owners a graduation scorecard: one pain point, a measured wage anchor, and a dated payback threshold that kills weak demos cheaply.

<!-- tension -->
## The demo never got a bill
The sequence is recent. In August 2025, the Massachusetts Institute of Technology (MIT) Media Lab research group behind the "GenAI Divide" study published its findings. Its finding was not a model problem but a "learning gap" in how organizations use the tools [1]. The study's lead author found the exceptions shared one habit: pick one pain point, execute well, and partner with the companies that use the tools [4].

Since then, adoption has only widened. Overall AI use among U.S. businesses sat between 17% and 20% across the December 2025 to May 2026 window [2]. A fifth to a quarter of firms expected to start within six months.

The mechanism underneath is that a pilot's bill is bigger than the tokens. A demo is priced at inference cost, but a finished task in production also carries the human review time behind it. The FinOps desk calls that cost per resolved work-unit (CRW): the total spend — tokens, retrieval, and human minutes — that one completed task consumes. A contract summarizer that costs pennies in tokens can still demand 25 minutes of partner review per document. [One legal team's ledger makes the 25-minute review the bill the token math never shows](/review-minute-costs-66-dollars/), and no demo dashboard counts it. Pilots survive the demo because the dashboard shows the cheap half of the bill. They die in production because the expensive half lands on people, not on the meter.

Nobody wrote a graduation rule, so the expensive half surfaces after the compute budget is spent.

## By the numbers
- **95% of companies:** The share in MIT's dataset whose GenAI work falls short of measurable return [1].
- **$30.24 an hour:** The 2025 median wage for paralegals — the review step most pilots quietly hand to humans [3].

<!-- tactical-insight -->
## What the surviving teams write down
What I find telling in the field is that the teams whose pilots survive all carry the same page, and it is boring. It starts with the work-unit: one task, defined once, with a baseline of what it costs a human today. The MIT research points the same way, because the winners narrow to one pain point rather than piloting five novelties at once [4]. Then the scorecard asks the questions a demo cannot answer, and every question carries a number:

1. What does the resolved work-unit cost with a human doing it, at a measured wage? A review job at the $62,890-a-year median costs about $30 an hour, so ten verification hours a week run roughly $15,700 a year before benefits [3].
2. What does it cost once the agent runs — tokens, retrieval, and the human minutes it still demands? The review tax is real, which is why CRW and token spend are different numbers.
3. What is the payback threshold, in labor hours, and what date is it measured against? The field standard is five times the displaced labor hours over a year; anything under that is a novelty the demo flattered.
4. Is the work deterministic and high-throughput, or open-ended chat? Password resets and invoice triage graduate. Meeting summarizers rarely do, because their output cannot be graded cheaply.
5. Who grades the output, and can that check itself be automated? Until the review step shrinks, the pilot has only moved the labor, not removed it.

The teams that skip the page do not get better pilots. They get the same demo renewed at a higher price. A pilot that clears the five questions moves to production compute with its threshold written on the approval. One that fails is killed cheaply, on paper, in an afternoon.

<!-- nuanced-takeaway -->
## The catch
A hard threshold kills good pilots too. The five-times rule is built for steady work with a countable baseline. It starves the slow pilots whose value shows up after the first year, as reviewers get faster, the same way it kills the novelties. The scorecard is a decision rule, not a verdict: use it to force a price onto every renewal. Where a pilot looks promising but sits under the threshold, fund it on purpose as a measured bet, and never let it drift on demo excitement.

## Sources
- [1] Fortune, "MIT report: 95% of generative AI pilots at companies are failing", 2025-08-18 — https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo
- [2] U.S. Census Bureau, "Large Firms With at Least 20 Employees Biggest AI Users" (BTOS), 2026-05-26 — https://www.census.gov/library/stories/2026/05/ai-use-businesses.html
- [3] O*NET OnLine, "Summary Report for 23-2011.00 — Paralegals and Legal Assistants", 2025 wages — https://www.onetonline.org/link/summary/23-2011.00
- [4] Fortune interview with Aditya Challapally (MIT NANDA lead author), 2025-08-18 — https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo
