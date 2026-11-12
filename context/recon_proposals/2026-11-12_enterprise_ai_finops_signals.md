# Signals: enterprise_ai_finops — 2026-11-12
**Window:** 2026-10-13 → 2026-11-12
**Queries run:** 18 (12 web fan-outs across the vertical's angles — AI token spend survey, FinOps Foundation AI cost work, model price cards, pilot-to-production ROI, AI budget overruns, inference price indices, GPU rental prices, neocloud credit, per-employee AI spend, department-level AI spend, vendor share of token spend, cost-control adoption; 1 Hacker News Algolia `search_by_date` sweep on `created_at_i` ≥ 2026-10-13 with points ≥ 20 across eight query shapes (AI cost, token bill, inference cost, LLM pricing, FinOps, AI budget, GPU cost, AI ROI); plus 7 primary and near-primary page fetches: the Ramp AI Index November edition, the Ramp AI Index dashboard, Cloudera's State of Enterprise AI 2026 release, TechCrunch's read of the Ramp data, Silicon Data's LLM Token Expenditure Index, CoreWeave's Q3 2026 results release, and OpenAI's GPT-6.1 Terra announcement)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Ramp's November AI Index: AI spend rose 1.65% in October to a new peak — the second straight month of near-flat spend — while the average price per million tokens fell 21% and token volume growth outran spend | https://ramp.com/data/ai-index-nov-2026 | 2026-11-11 | "AI spending rose to a new peak in October, rising 1.65% from September"; "The average price per million tokens fell 21% over the last month"; "Token volume growth continues to outpace token spend as AI gets cheaper and cheaper"; "1% of businesses drive 80% of the revenues to OpenAI and Anthropic"; "Growth in the median and top 10% groups is relatively sluggish" | The invoice has stopped tracking consumption, so a budget set on usage no longer describes the bill | 95 |
| 2 | The same Ramp edition: spend per employee is a barbell ($10.2K top 1%, $801 top 10%, $16.32 median), engineering still holds 72% of classified spend while customer success and support rose to 13.3% from 0.8% in June, and frontier models took 69.5% of spend | https://ramp.com/data/ai-index-nov-2026 | 2026-11-11 | "The top 1% of firms now spend a median $10.2K per employee per month on AI, up 9%. Firms in the top 10% spent $801, roughly flat. The median firm spends $16.32, up $0.93"; "In October, Engineering teams drove 72% of all classified spend"; customer success and support "now driving 13.3% of all classified spend, up from 0.8% in June"; frontier models "took 69.5% of spend in October, up from 67.7%" | Per-employee AI benchmarks average two populations that differ by three orders of magnitude | 90 |
| 3 | Cloudera's State of Enterprise AI 2026: 89% of enterprises have already limited or redesigned AI use cases because of rising token consumption, while only 19% continuously monitor token and inference costs | https://www.cloudera.com/about/news-and-blogs/press-releases/2026-10-26-the-ai-scale-trap-why-89-of-enterprises-are-forced-to-redesign-ai-use-cases-amid-rising-costs.html | 2026-10-26 | "Nearly nine in ten (89%) respondents have already limited or redesigned AI use cases because of rising token consumption"; survey commissioned by Cloudera and "fielded by Wakefield Research of 1,500 global IT leaders and decision-makers in September 2026" | Buyers are re-cutting the work itself, not negotiating the rate | 92 |
| 4 | The same Cloudera study, on what the redesign physically is: 45% moved a workload to another cloud, private or on-premises environment; 40% reduced processing frequency, model size, context size or output volume; 24% paused or cancelled a use case; only 19% monitor token and inference costs continuously | https://www.cloudera.com/blog/business/the-state-of-enterprise-ai--what-it-really-takes-to-scale-enterprise-ai.html | 2026-10-26 | "Forty-five percent of respondents have moved a workload to another cloud, private environment or on-premises platform, while 40% have reduced processing frequency, model size, context size, or output volume. Another 24% have paused or canceled an AI use case altogether"; "only 19% continuously monitor token and inference costs" | The savings line is scope reduction — fewer and smaller calls — and four in five firms cannot see it as it happens | 88 |
| 5 | TechCrunch's read of the Ramp series: token spend grew only 1.5% across August and September after 42% growth in July, and Ramp's economist says the top 1% of firms "stuttered slightly" below their summer peak | https://techcrunch.com/2026/11/06/ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo | 2026-11-06 | "token spend only grew 1.5% across August and September. To compare, in July, it grew 42% from the previous month"; Kharazian: "Almost the entire spend on AI is from venture-backed, high-growth tech companies"; "Median firms spend $12-$15 per employee per month, and the top 10% spend $600-$1,000" | The slowdown was visible before October and is concentrated in the cohort that pays | 76 |
| 6 | Silicon Data's LLM Token Expenditure Index, the usage-weighted market price of a million tokens, printed $0.83 on 2026-11-08, down 7.0% on the week and down from $0.89 on 2026-11-01 | https://www.silicondata.com/products/silicon-index/llm-token-expenditure-index | 2026-11-08 | "As of Nov 8, 2026 — 0.83 USD / M tokens — 7.0% (7D)"; daily readings 0.89 (Nov 1), 0.88, 0.87, 0.86, 0.85, 0.85, 0.83 (Nov 7), 0.83 (Nov 8) | The market price of the unit is still falling in the same weeks the bill flattened | 74 |
| 7 | OpenAI's GPT-6.1 Terra: a mid-tier model at $1/$5 per million tokens, half the price of GPT-6.1 Sol, matching GPT-6 Astra's measured capability at one-tenth its price per token | https://openai.com/index/introducing-gpt-6-1-terra | 2026-10-26 | "Standard API pricing is $1 per million input tokens, $0.05 per million cached input tokens, and $5 per million output tokens"; "Its standard API prices are 50% lower than those of GPT-5.6 Terra and GPT-6.1 Sol"; Terra "performs on par with GPT-6 Astra at only one-tenth its price per token" | The vendor's answer to a flat bill is another price cut aimed at high-volume, lower-margin work | 72 |

## Dating note

Every row above is event-dated inside the window. Rows 1–2 are the November edition of Ramp's monthly AI Index,
published 2026-11-11 and covering October 2026; both rows are read from the same first-party letter. Rows 3–4 are one
study: row 3 is Cloudera's press release dated 2026-10-26 announcing the report and naming the fielding instrument
(Wakefield Research, 1,500 IT leaders and decision-makers, September 2026); row 4 is Cloudera's own summary page for
the same study, published the same day, and is used only for the breakdown of *what* the redesign was. Row 5 is
TechCrunch's 2026-11-06 write-up of the prior (October) Ramp edition and is corroboration, never the source of record
for a Ramp figure — where the two disagree, the Ramp letter wins. Row 6 is a daily index reading dated 2026-11-08.
Row 7 is OpenAI's announcement post dated 2026-10-26. No row rests on an undated status page.

## Dated background

- The prior Ramp edition, covering September and the first weeks of October, and the origin of the "Cracks in the AI
  Thesis" framing: https://ramp.com/data/ai-index-oct-2026
- Ramp's dashboard carrying the weekly token-spend, volume and blended-price series: https://ramp.com/data/ai-index
- FinOps Foundation / Tokenomics Foundation, *State of Tokenomics, September 2026* — 43% named proving value or ROI
  as the top challenge and 23% asked providers for more transparency, not lower prices. September fielding, outside
  this window; context only, and already anchored by this vertical's 2026-10-01 and 2026-11-05 runs:
  https://www.finops.org/topic/ai-tokenomics
- Harness, *2026 State of AI in FinOps* — 26% of AI spend estimated wasted, 52% report no clear AI cost owner, 57%
  say their organization encourages "tokenmaxxing". The survey was fielded May–June 2026, so the report cannot anchor
  a 30-day signal; carried as background for the ownership split only:
  https://www.harness.io/state-of-ai-in-finops-2026
- CoreWeave's Q3 2026 results (revenue $3.661B, interest expense $846M, debt $46.9B, capex guidance $37–39B,
  published 2026-11-10) are in-window but are not used here: this desk priced the buyer's exposure to a GPU
  landlord's balance sheet on 2026-10-20 (`your-gpu-landlord-80-wont-survive`), and re-pairing the same rule would
  be a retread. Recorded so the next run does not re-discover it:
  https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=7 candidates=0 heuristic=- window=2026-10-13..2026-11-12 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

