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
meta_title: "Your Pilot Needs a Scorecard: 95% Fail"
meta_title_source: "derived_from_title"
meta_description: "Your AI pilots are not dying because the model fails the demo: 95% of the companies in MIT's GenAI Divide study get no measurable return from it, while the…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-pilot-needs-a-scorecard/featured.jpg"
image_style: "document_flatlay"
image_model: "flux"
image_alt: "AI Pilots Need A Graduation Scorecard. Blank one-page scorecard form on a brushed-steel control room desk, pen resting across it beside a"
image_caption: "AI Pilots Need A Graduation Scorecard: 95% of GenAI pilots earn no measurable return because nobody writes the graduation rule."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Your AI pilots are not dying because the model fails the demo: 95% of the companies in MIT's GenAI Divide study get no measurable return from it, while the models keep improving [1]. The failure is organizational, and nothing written down decides whether a proof of concept graduates to production compute. So the decision gets made on demo excitement and renewed quarter after quarter [1]. A chief information officer (CIO) who runs a dozen pilots a year needs a one-page scorecard, priced in labor hours, to settle the question before renewal season.

<!-- tldr -->
## At a glance
Enterprise teams keep launching generative AI pilots that never earn their keep. MIT found 95% deliver no measurable return. This piece gives budget owners a graduation scorecard: one pain point, a measured wage anchor, and a dated payback threshold that kills weak demos cheaply.

<!-- tension -->
## The demo never got a bill
The sequence starts in August 2025, when the Massachusetts Institute of Technology (MIT) Media Lab research group behind the "GenAI Divide" study published its findings. Its conclusion was not a model problem but a "learning gap" in how organizations use the tools [1]. The study's lead author found the exceptions shared one habit: pick one pain point, execute well, and partner with the companies that use the tools [4].

Since then, adoption has only widened. Overall AI use among U.S. businesses sat between 17% and 20% across the December 2025 to May 2026 window [2].

Underneath sits a simple mechanism: a pilot's bill is bigger than the tokens. A demo is priced at inference cost, but a finished task in production also carries the human review time behind it. This desk calls that number the cost per resolved work-unit (CRW): the total spend — tokens, retrieval, and human minutes — that one completed task consumes. A contract summarizer that costs pennies in tokens can still demand 25 minutes of partner review per document. [One legal team's ledger makes the 25-minute review the bill the token math never shows](/review-minute-costs-66-dollars/), and no demo dashboard counts it. Pilots survive the demo because the dashboard shows the cheap half of the bill. They die in production because the expensive half lands on people, not on the meter. I keep coming back to how ordinary that failure is — nobody wrote a graduation rule, so the expensive half surfaces after the compute budget is spent.

## By the numbers
- **95% of companies:** The share in MIT's dataset whose GenAI work falls short of measurable return [1].
- **$30.24 an hour:** The 2025 median wage for paralegals — the review step most pilots quietly hand to humans [3].

<!-- tactical-insight -->
## What the surviving teams write down
The teams whose pilots survive all carry the same page, and it is boring. It starts with the work-unit: one task, defined once, with a baseline of what it costs a human today. The MIT research points the same way, because the winners narrow to one pain point rather than piloting five novelties at once [4]. Then the scorecard asks the questions a demo cannot answer, and every question carries a number:

1. **The human baseline.** What does the resolved work-unit cost with a person doing it, at a measured wage? A review job at the $62,890-a-year median costs about $30 an hour, so ten verification hours a week run roughly $15,700 a year before benefits [3].
2. **The agent's true cost.** What does the task cost once the agent runs — tokens, retrieval, and the human minutes it still demands? The review tax is real, which is why CRW and token spend are different numbers.
3. **The payback threshold.** What is the threshold, in labor hours, and what date is it measured against? This article's proposed standard is five times the displaced labor hours over a year; anything under that is a novelty the demo flattered.
4. **The shape of the work.** Is the task deterministic and high-throughput, or open-ended chat? Password resets and invoice triage graduate. Meeting summarizers rarely do, because their output cannot be graded cheaply.
5. **The grader.** Who checks the output, and can that check itself be automated? Until the review step shrinks, the pilot has only moved the labor, not removed it.

The teams that skip the page do not get better pilots. They get the same demo renewed at a higher price. A pilot that clears the five questions moves to production compute with its threshold written on the approval. One that fails is killed cheaply, on paper, in an afternoon. What I would ask first, at any renewal meeting, is question two — because it is the one no vendor dashboard will ever volunteer.

<!-- nuanced-takeaway -->
## The catch
A hard threshold kills good pilots too. The five-times rule is built for steady work with a countable baseline. It starves the slow pilots whose value shows up after the first year, as reviewers get faster, in the same way it kills the novelties. My reading, held loosely: the scorecard is a decision rule, not a verdict. Use it to force a price onto every renewal. Where a pilot looks promising but sits under the threshold, fund it on purpose as a measured bet, and never let it drift on demo excitement.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Agentic AI Adoption Soars, But Profits Stall in 2026" -> /agentic-ai-adoption-soars-but-profits-stall-in-2026/ [same site (aichieve.net); same category; topical overlap: companies, measurable, pilot] Link "Agentic AI Adoption Soars, But Profits Stall in 2026" in the section where the article touches companies, measurable, pilot. -->
<!-- internal-link hint: "Half Your Tokens: 5% of Your Bill" -> /half-your-tokens-5-of-bill/ [same site (aichieve.net); same category; topical overlap: models] Link "Half Your Tokens: 5% of Your Bill" in the section where the article touches models. -->
<!-- internal-link hint: "One Green Run Is Not Reliability" -> /agent-reliability-pass-k-not-one-green-run/ [same site (aichieve.net); same category; topical overlap: fail] Link "One Green Run Is Not Reliability" in the section where the article touches fail. -->
## Related reading

- [Agentic AI Adoption Soars, But Profits Stall in 2026](/agentic-ai-adoption-soars-but-profits-stall-in-2026/)
- [Half Your Tokens: 5% of Your Bill](/half-your-tokens-5-of-bill/)
- [One Green Run Is Not Reliability](/agent-reliability-pass-k-not-one-green-run/)
<!-- internal-links:end -->

## Sources
- [1] Fortune, "MIT report: 95% of generative AI pilots at companies are failing", 2025-08-18 — https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo
- [2] U.S. Census Bureau, "Large Firms With at Least 20 Employees Biggest AI Users" (BTOS), 2026-05-26 — https://www.census.gov/library/stories/2026/05/ai-use-businesses.html
- [3] O*NET OnLine, "Summary Report for 23-2011.00 — Paralegals and Legal Assistants", 2025 wages — https://www.onetonline.org/link/summary/23-2011.00
- [4] Fortune interview with Aditya Challapally (MIT NANDA lead author), 2025-08-18 — https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo
