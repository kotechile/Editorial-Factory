---
title: Your LLM Judge Silently Votes: 9%–81% Undecided
vertical: ai_observability_qa
meta_title: Your LLM Judge Silently Votes: 9–81% Undecided
meta_description: A new benchmark shows LLM judges that pass every control still pick winners on 9%–81% of conflicts no rubric resolved — the same week vendors made those scores production metrics.
primary_keyword: LLM judge
secondary_keywords: [online evaluation, LLM-as-a-judge, production observability]
kind: news
persona: evals_infra_eng
one_big_finding: "A new benchmark shows LLM judges that pass every control still pick winners on 9%–81% of conflicts no rubric resolved — the same week vendors made those scores standing production metrics."
date: 2026-11-24
slug: your-online-judge-votes-for-itself
synthesis: true
sources:
  - https://arxiv.org/abs/2611.28940v1
  - https://www.snowflake.com/en/blog/ai-agent-observability-monitor-debug-optimize-llm-applications
---

<!-- lead -->
On 13 November, Snowflake said its Observe platform would score live traffic with LLM judges — models that grade other models' answers — and treat those scores like any other monitored metric [2]. Eight days later, a benchmark study called TradeoffBench found that judges passing every stated test still picked winners the tests could not back, on 9%–81% of 1,345 clashes between goals [1]. The quality score you alert on may be carrying a value choice nobody wrote down.

<!-- tldr -->
## At a glance
This article is for evaluation-infrastructure engineers. It joins a 21 November benchmark showing LLM judges silently settle goal conflicts with unstated rules, and this month's vendor ships that turn those judge scores into monitored production metrics.

<!-- tension -->
## The score became a metric before anyone wrote the rule
Three dates set the stage, in order. On 3 November, LangChain moved LangSmith's bring-your-own-cloud (BYOC) offering onto Amazon Web Services (AWS), Azure and Google Cloud, so traces, evals and datasets now live in each customer's own cloud account while LangChain runs the control plane [3]. On 13 November, Snowflake put Agent Observability into private preview, with online judge results that, in its words, "turn into metrics teams can monitor over time," each result linked to the interaction it scored [2]. Then, on 21 November, TradeoffBench read what those scores are made of [1].

The study tested judges that weigh several goals at once — relevance against faithfulness, say — where the rubric does not say which goal wins when they pull apart. Six open-weight judges passed every dominance and equality control the authors set, yet still picked winners those controls could not back, on 9%–81% of 1,345 conflicts between goals [1]. On the 577 choice sets where the winner order stayed stable, every single one followed a majority rule the rubric explicitly banned [1]. The calls look decisive. The rule behind them was never on paper.

That is the friction. Once a judge score becomes a monitored metric, it inherits the whole apparatus: a dashboard, a threshold, a weekly baseline. When the score drops, the alert reads as model drift. It may instead be the judge voting on a trade-off it never disclosed. I keep coming back to how ordinary the failure looks — nothing breaks, the pipeline runs, the number just moves. The team with the best tracing stack in the building is still reading an opinion that was never stated.

## By the numbers
- Six open judges picked unsupported winners on 9%–81% of 1,345 criterion conflicts [1].
- All 577 order-stable choice sets followed a majority rule the rubric explicitly banned [1].

<!-- tactical-insight -->
## Where the hidden vote bites first
The alert path takes the damage first. A closed frontier judge from OpenAI (model 6.1-sol) left its trade-off premise unstated on 29.8% of 400 raw test cases [1]. Even when a rule was spelled out, that judge still gave hard calls on 16 of 45 valid cases [1]. A threshold sitting on a score like that rests on a hidden opinion, and no amount of tracing will surface it.

Model choice is the second exposure. Snowflake's own example prices model choice by failed-evaluation rate, telling buyers to prefer the model with fewer failed checks over the cheaper one [2]. That logic holds only if the judge settles goal clashes the same way every week. If it does not, you swap a good model for a bad one on the judge's silent vote. What I have not yet seen in any vendor prompt template is the one-line fix: state the trade-off rule in the rubric before the score counts. The study names its version of this "identified-first evaluation" — the judge must name its premise before its verdict is accepted [1].

<!-- nuanced-takeaway -->
## The catch
Bigger judges narrow the hole without closing it. In one trial set — cases built to catch judge drift, with the goals hidden — reasoning judges broke the banned rule just twice across 9,720 tries [1]. Yet they still issued strict verdicts on up to 35 of 46 valid cases where a trade-off had been left out [1]. Reasoning shrinks the drift; it does not supply the missing rule. And the Snowflake leg is a private preview with forward-looking disclaimers, not shipped behavior [2], so the production-metric half of this story is still a promise.

So the alert may sit on a hidden opinion either way, and the only fix that costs nothing is a stated trade-off rule in the rubric. My reading, held loosely: the vendors will ship judge-as-metric faster than anyone writes those rules down, because the metric is the product. [Your Judge's 80% Overpays 39 Points](/your-judges-80-overpays-39-points/) made the same shape of argument about how much a judge's agreement is worth.

## Sources
- [1] Chen et al., "When Rubrics Do Not Decide: Silent Value Completion in LLM Evaluation" (TradeoffBench), arXiv 2611.28940, 21 November 2026 — https://arxiv.org/abs/2611.28940v1
- [2] Snowflake, "Improve AI Performance, Quality and Cost with Agent Observability," engineering blog, private preview as of 13 November 2026 — https://www.snowflake.com/en/blog/ai-agent-observability-monitor-debug-optimize-llm-applications
- [3] LangChain, "LangSmith BYOC is now available on AWS, Azure, and Google Cloud," 3 November 2026 — https://www.langchain.com/blog/langsmith-byoc-aws-gc-azure
