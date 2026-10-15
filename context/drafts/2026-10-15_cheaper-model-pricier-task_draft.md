---
title: "Your Cheaper Model: 57% Pricier Tasks"
vertical: enterprise_ai_finops
persona: enterprise_cai
one_big_thing: "Output tokens are billed at a multiple of the input rate and the reasoning half of them is invisible, so a tier priced 50% cheaper per token can cost 57% more per resolved task."
date: 2026-10-15
slug: cheaper-model-pricier-task
archetype: evergreen
evergreen: true
---

<!-- lead -->
A model that looked cheaper on the rate card came out 57% pricier per finished task. OckBench is a token-efficiency benchmark from researchers at Georgia Tech, the Massachusetts Institute of Technology (MIT) and Nvidia [1]. It compared two distilled models from one family. The smaller cost $0.05 per million tokens. The larger cost $0.10 [1]. The smaller then spent 3.13 times more output tokens to reach a worse answer. It used 41,415 output tokens against 13,211. That closed at 14.5 units of cost against 9.2 [1]. Half the sticker price, 57% more per query.

<!-- tension -->

## The big picture:

Output is the dear line on every rate card, and the model decides how much of it a task needs.

Anthropic bills its Opus 5.5 at $4 per million input tokens and $20 per million output tokens [3]. OpenAI bills gpt-6.1-sol at $2.00 and $10.00 [4]. Google prices Gemini 3.7 and 3.8 Flash at $1.50 and $7.50 [5]. Google prints that last number as "output and thinking tokens".

Part of what the buyer pays for never shows up. OpenAI's own docs say reasoning tokens are not visible through its interface. They are still billed as output tokens [6].

That is why the benchmark tables mislead. They rank answers. Here, answers are bought with generated tokens.

The evidence starts with Terminal-Bench 2.0. The top setup resolved 62.9% of its tasks, using 137.5M input tokens. The runner-up resolved 57.8%, using 3.9M [2]. The same suite found output volume weakly and negatively linked to success (r = -0.170, p = 0.515) [2]. The model that produced the most tokens by far, GPT-5-Nano at roughly 60k on average, resolved 8% [2].

What strikes me is how little of this reaches a procurement sheet. Two candidates sit side by side. The per-million-token rate decides. The line that rules the invoice is the one the buyer cannot see.

## By the numbers

- **57% — Pricier at half the token price:** The 7B distilled model cost $0.05 per 1M tokens against $0.10 for its 14B sibling, and still ran to 14.5 units of cost per query against 9.2 [1].
- **3.13× — More output per answer:** It used 41,415 output tokens where the larger model used 13,211, for a worse result. The paper's authors call it the Overthinking Tax [1].
- **5× — Output rate against input rate:** Opus 5.5 sits at $20 against $4 per 1M tokens [3]. gpt-6.1-sol sits at $10.00 against $2.00 [4]. Gemini 3.7 and 3.8 Flash sit at $7.50 against $1.50 [5].
- **137.5M — Top score, top burn:** The best agent on Terminal-Bench 2.0 spent 137.5M input tokens. The runner-up spent 3.9M, so score and burn rank the same field in different orders [2].

<!-- tactical-insight -->

## What I'd watch:

The move I keep coming back to is that buyers rebuild the table on their own traffic, not on the rate card.

- **A price sheet per task.** Candidates get priced on output tokens per resolved task, pulled from production logs and multiplied by each vendor's own output line [3][4][5]. One measured pair of sibling models flipped by 57% on that single change [1].
- **The hidden span, counted.** Google points at the thoughts field in its response data, which reports how many thinking tokens a request used [5]. OpenAI's `max_output_tokens` caps reasoning tokens, visible output and formatting in one number [6]. Its own usage example reports 1024 reasoning tokens inside a 1261-token total [6].
- **The queue as the discount.** The batch lane halves both lines. Anthropic takes 50% off input and output [3]. gpt-6.1-sol drops to $1.00 and $5.00 from $2.00 and $10.00 [4]. It changes the wait, not the model badge.
- **The rate-card calendar.** Google's promotional pricing for Gemini 4 Argon ends November 30, 2026. The introductory rates for Gemini 3.7 and 3.8 Flash end December 31, 2026, with $1.5 and $7.5 per 1M tokens applying from January 1, 2027 [5]. Any per-task model has a shelf life.

<!-- nuanced-takeaway -->

## The catch

My read is that the inversion is real, but narrower than it first looks.

- **The pair is two distilled open models on a third-party gateway, priced as of January 2026** [1]. It shows the mechanic. It does not rank any vendor's tiers for good.
- **Input-heavy work still favours the cheap tier.** Long documents and cached prefixes push the bill toward the input line, where the smaller model is genuinely cheaper. Anthropic's cache reads at 5% of the input price reinforce that [3].
- **The 137.5M figure belongs to a scaffold,** the Codex CLI agent on a benchmark suite, not to a business process [2].
- **No rate card carries a dollar column per resolved task.** The buyer builds that number. Three of the rates quoted here change on published dates in the next ten weeks [5].

<!-- tldr -->

## At a glance

- **The Big Shift:** A model with a lower price per million tokens can cost more per finished task. Output tokens are billed at about five times the input rate, and the reasoning half of them never appears in the response.
- **Why It Matters:** Cost per resolved unit carries the business case. A comparison built on per-million-token rates can pick the dearer option and look like a saving.
- **What I'd watch:** Buyers rebuilding the comparison on their own traffic, plus the dated price changes on the cards themselves.
  - **Per-task pricing:** Counting output tokens per resolved task in production, then pricing them at each candidate's own output line. That is where the 57% inversion showed up [1].
  - **Reasoning audits:** Reading the thinking-token count back from the response data. That spend is billed as output but hidden from the visible answer [5][6].
  - **Queue lanes:** Moving deferrable work into the batch lane, which halves both the input and output lines without changing the model [3][4].
- **The Catch:** The measured inversion is a pair of distilled models priced as of January 2026. Input-heavy workloads still favour the cheaper tier. No vendor publishes a cost per resolved task, so the buyer assembles that number and dates it [1][3][5].

## Sources

[1] Du, Kang, Han & Krishna, "OckBench: Measuring the Efficiency of LLM Reasoning" (arXiv:2511.05722v2, Georgia Tech / MIT / NVIDIA) — https://arxiv.org/html/2511.05722v2 (retrieved 2026-10-15; pricing basis dated January 2026)
[2] Merrill et al., "Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces" (arXiv:2601.11868v1) — https://arxiv.org/html/2601.11868v1 (retrieved 2026-10-15)
[3] Anthropic, "Pricing" — https://docs.claude.com/en/docs/about-claude/pricing (retrieved 2026-10-15; vendor rate card)
[4] OpenAI, "Pricing" — https://platform.openai.com/docs/pricing (retrieved 2026-10-15; vendor rate card)
[5] Google Cloud, "Agent Platform pricing" (Vertex AI) — https://cloud.google.com/vertex-ai/generative-ai/pricing (retrieved 2026-10-15; vendor rate card)
[6] OpenAI, "Reasoning models" — https://platform.openai.com/docs/guides/reasoning (retrieved 2026-10-15; vendor documentation)

<!-- internal-links -->
