---
title: Your LLM Judge Silently Votes: 9%–81% Undecided
vertical: ai_observability_qa
meta_title: Your LLM Judge Silently Votes: 9–81% Undecided
meta_description: A new benchmark shows LLM judges that pass every control still pick winners on 9%–81% of conflicts no rubric resolved — the same week vendors made those scores production metrics.
primary_keyword: LLM judge
secondary_keywords: [online evaluation, LLM-as-a-judge, production observability]
kind: news
persona: evals_infra_eng
one_big_thing: "A new benchmark shows LLM judges that pass every control still pick winners on 9%–81% of conflicts no rubric resolved — the same week vendors made those scores standing production metrics."
date: 2026-11-24
slug: your-online-judge-votes-for-itself
synthesis: true
sources:
  - https://arxiv.org/abs/2611.28940v1
  - https://www.snowflake.com/en/blog/ai-agent-observability-monitor-debug-optimize-llm-applications
image_path: "context/assets/illustrations/your-online-judge-votes-for-itself/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "LLM Judges Pick Winners No Rubric Backs. Empty observability control room at night; a wall of live score charts holds flat blue baselines"
image_caption: "LLM Judges Pick Winners No Rubric Backs: The judge scores now watched as production metrics may carry a choice no one declared."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Your LLM judge — a model that scores another model's answers — may be voting on rules nobody wrote. On 13 November, Snowflake said its Observe platform would score live traffic with LLM judges, and those scores would be watched like any other live metric [2]. Eight days later, a benchmark called TradeoffBench found the gap underneath that plan. Its judges passed every stated test, yet still picked winners the tests could not back, on 9%–81% of 1,345 clashes between goals [1]. The quality score you alert on can carry a value choice no one declared.

<!-- tldr -->
## At a glance
This article joins two events from one month: vendors turned live judge scores into watched production metrics, and a new benchmark found those judges invent a rule whenever the rubric leaves two goals in conflict. It explains what that costs the team that alerts on the scores.

<!-- tension -->
## A metric before a rule
The month moved the eval stack twice before the paper landed. Ten days before Snowflake's private preview, LangSmith had moved its customers' traces, evals and datasets into their own cloud accounts on Amazon Web Services (AWS), Azure and Google Cloud [3]. The eval stack now lives inside the buyer's own walls. Then Snowflake's Observe team made online judge results "turn into metrics teams can monitor over time" [2]. TradeoffBench then read what those scores are made of [1].

The study looked at judges that weigh several goals at once, like relevance and faithfulness. Sometimes two goals pull against each other, and the rubric does not say which one wins. Six open judges passed every test the authors set, yet picked winners those tests could not back on 9%–81% of 1,345 clashes [1]. All 577 choice sets with a stable winner order followed a majority rule the rubric in plain words banned [1]. The calls look decisive. The rule behind them was never stated.

That is the friction. Once a judge score becomes a watched metric, it inherits what every metric gets — a dashboard, a threshold, a weekly baseline. A drop in quality then reads as model drift. It may instead be the judge picking a side it never told you about. I read the 577 figure twice before taking it in: every single stable choice broke a rule the rubric had named and forbidden. The team with the best tracing stack can still be reading an opinion that was never on paper.

## By the numbers
- **29.8% of raw test cases:** a closed OpenAI frontier judge (model 6.1-sol) left its trade-off premise unstated across the 400 cases tried [1]
- **16 hard calls:** what that same judge still issued among 45 valid cases even when a rule was spelled out.

<!-- tactical-insight -->
## Where this bites first
The alert path takes the hit first. A closed frontier judge from OpenAI, model 6.1-sol, left its trade-off premise unstated on 29.8% of 400 raw test cases [1]. Even when a rule was spelled out, that judge still gave hard calls on 16 of 45 valid cases [1]. A threshold wired to such a score sits on a hidden opinion. What gives me pause is that the fix costs one line: state the trade-off rule in the rubric. I have yet to see a vendor prompt ask for it. The study calls its own fix "identified-first evaluation" — the judge must name its premise before its call counts [1].

The other thing to watch is model choice by judge. Snowflake's own example tells buyers to prefer the model with fewer failed checks over the cheaper one [2]. That logic only holds if the judge settles clashes the same way every week. If it does not, you may swap a good model for a bad one on the judge's hidden vote.

<!-- nuanced-takeaway -->
## The catch
Bigger judges narrow this hole without ending it. The study hid the goals in one trial set — cases built to catch judge drift — and reasoning judges broke the banned rule just twice across 9,720 tries [1]. Yet the open judges still gave hard calls on up to 35 of 46 valid cases [1], and the reasoning models could not settle cases where a trade-off was left out. My reading, held loosely: scale buys you fewer broken rules, not a rule you can read. The Snowflake leg is a private preview with a legal disclaimer, not shipped behavior [2]. So the alert may sit on a hidden opinion either way, and the one fix that costs nothing is a stated rule. [Your Judge's 80% Overpays 39 Points](/your-judges-80-overpays-39-points/) made the same shape of argument about how much a judge's agreement is worth.

## Sources
- [1] Chen et al., "When Rubrics Do Not Decide: Silent Value Completion in LLM Evaluation" (TradeoffBench), arXiv 2611.28940, 21 November 2026 — https://arxiv.org/abs/2611.28940v1
- [2] Snowflake, "Improve AI Performance, Quality and Cost with Agent Observability," engineering blog, private preview as of 13 November 2026 — https://www.snowflake.com/en/blog/ai-agent-observability-monitor-debug-optimize-llm-applications
- [3] LangChain, "LangSmith BYOC is now available on AWS, Azure, and Google Cloud," 3 November 2026 — https://www.langchain.com/blog/langsmith-byoc-aws-gc-azure
