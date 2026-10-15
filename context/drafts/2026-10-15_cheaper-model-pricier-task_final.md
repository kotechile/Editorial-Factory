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
A language model priced 50% cheaper per token turned out 57% pricier per finished task. OckBench is a token test from researchers at Georgia Tech, the Massachusetts Institute of Technology (MIT) and Nvidia [1]. It compared two distilled models from the same family. 

The smaller model cost $0.05 per million tokens, while the larger cost $0.10 [1]. Yet the smaller model burned 3.13 times more output tokens to get a worse answer. 

It used 41,415 output tokens against 13,211. That closed at 14.5 units of cost against 9.2 [1]. Half the sticker price meant 57% more cost per query.

<!-- tension -->

## The big picture:

Output tokens drive the bill, and the model decides how many it needs.

Anthropic bills its Opus 5.5 at $4 per million input tokens and $20 per million output tokens [3]. OpenAI charges $2.00 and $10.00 for gpt-6.1-sol [4]. Google prices Gemini 3.7 and 3.8 Flash at $1.50 and $7.50 [5].

Google prints that last rate as "output and thinking tokens." Buyers pay for tokens they never see. OpenAI docs say reasoning tokens are hidden from users, but still bill as output [6].

What strikes me here is how benchmark charts hide this. They rank answers, not the tokens spent to buy them. The study that named the Overthinking Tax found the pattern across both frontier and open-source models: efficiency is not a fixed property of model size [1].

The proof starts with Terminal-Bench 2.0. The top setup solved 62.9% of its tasks using 137.5 million input tokens [2]. The runner-up solved 57.8% using just 3.9 million [2].

The model that made the most tokens by far—roughly 60,000 on average—solved only 8% of its tasks [2]. Across that suite, output volume and success moved weakly in opposite directions (r = -0.170, p = 0.515), so extra words bought no extra accuracy [2].

## By the numbers

- **57% — Hidden cost penalty:** The smaller model cost $0.05 per million tokens versus $0.10 for the larger, but finished at 14.5 units of cost per query against 9.2 [1].
- **3.13× — Output token bloat:** The cheap model burned 41,415 output tokens compared to 13,211 for the larger model, giving a worse result [1].
- **5× — Output price markup:** The three models quoted here charge five times more for output tokens than for input: Opus 5.5 at $20 against $4, gpt-6.1-sol at $10.00 against $2.00, Gemini 3.7 and 3.8 Flash at $7.50 against $1.50 [3][4][5].
- **137.5M — Top benchmark burn:** The top agent on Terminal-Bench 2.0 spent 137.5 million input tokens, while the runner-up spent just 3.9 million [2].

<!-- tactical-insight -->

## What I'd watch:

The part I keep circling: the buyers I follow now build their own price tables from real traffic, not vendor rate cards.

- **Task-level pricing:** Operators track output tokens per finished task in their own logs, then multiply by the vendor output rate [3][4][5]. One tested pair flipped by 57% on this single shift [1].
- **Hidden span counts:** Google shows how many thinking tokens a request uses right in its response data [5]. OpenAI caps reasoning tokens, visible output and text formatting under one limit [6]. One OpenAI example shows 1,024 reasoning tokens inside a 1,261-token total [6].
- **Queue-based discounts:** The batch lane cuts both input and output costs in half for Anthropic and OpenAI [3][4]. It changes the wait time, not the model badge.
- **Rate-card expiration:** Google ends cheap rates for Gemini 4 Argon on November 30, 2026. It raises Gemini 3.7 and 3.8 Flash rates on January 1, 2027 [5]. Every per-task model has a shelf life.

<!-- nuanced-takeaway -->

## The catch

My read is that this price flip is real, but narrower than it first looks.

- **Aged pricing data:** The 57% flip relies on two small open models priced on a gateway in January 2026 [1]. It proves the math, but does not rank any vendor's tiers forever.
- **Input-heavy advantage:** Massive text files and cached prompts shift the bill back to the cheaper input line. Anthropic charging just 5% of the input price for cache reads backs this up [3].
- **Lab versus real work:** The 137.5 million token burn belongs to a test tool—the Codex CLI (a command-line coding agent)—not a real business workflow [2].
- **Moving targets:** No rate card lists a dollar cost per finished task. Three of the rates cited here change in the next ten weeks [5].

<!-- tldr -->

## At a glance

- **The Big Shift:** A language model priced lower per million tokens can cost more per finished task. Output tokens cost roughly five times more than input tokens, and the reasoning half stays hidden from the final answer.
- **Why It Matters:** Cost per finished unit drives the artificial intelligence (AI) business case. Buyers who compare models using flat token rates often pick the dearer option while thinking they saved money.
- **What I'd watch:** Operators making new price charts using their own traffic logs and expiring vendor deals.
  - **Task pricing:** Tracking output tokens per finished task in real apps to find the true cost [1].
  - **Reasoning audits:** Pulling the hidden thinking-token count from response data [5][6].
  - **Batch queues:** Sending slow work to batch lanes to cut token costs in half [3][4].
- **The Catch:** Input-heavy work still favors the cheaper tiers. That 57% flip comes from a specific pair of models priced in January 2026 [1].

## Sources

[1] Du, Kang, Han & Krishna, "OckBench: Measuring the Efficiency of LLM Reasoning" (arXiv:2511.05722v2, Georgia Tech / MIT / NVIDIA) — https://arxiv.org/html/2511.05722v2 (retrieved 2026-10-15; pricing basis dated January 2026)
[2] Merrill et al., "Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces" (arXiv:2601.11868v1) — https://arxiv.org/html/2601.11868v1 (retrieved 2026-10-15)
[3] Anthropic, "Pricing" — https://docs.claude.com/en/docs/about-claude/pricing (retrieved 2026-10-15; vendor rate card)
[4] OpenAI, "Pricing" — https://platform.openai.com/docs/pricing (retrieved 2026-10-15; vendor rate card)
[5] Google Cloud, "Agent Platform pricing" (Vertex AI) — https://cloud.google.com/vertex-ai/generative-ai/pricing (retrieved 2026-10-15; vendor rate card)
[6] OpenAI, "Reasoning models" — https://platform.openai.com/docs/guides/reasoning (retrieved 2026-10-15; vendor documentation)

<!-- internal-links -->

## Gate report
lead: PASS — Delivers the core 57% cost inversion stat instantly in the first sentence without filler.
tension: PASS — Frames the structural shift with 'The big picture:' H2, uses short paragraphs, and includes a 4-bullet 'By the numbers' section with bold lead-ins.
tactical-insight: PASS — Uses 'What I'd watch:' H2 and formats 4 actionable observations as clean bullets with bold lead-ins based on real operator actions.
nuanced-takeaway: PASS — Presents honest limitations with 'The catch' H2 and a clear first-person observer cue.
tldr: PASS — Follows the strict 4-part Smart Brevity schema under the 'At a glance' H2, explaining the core shift in plain, simple English.
