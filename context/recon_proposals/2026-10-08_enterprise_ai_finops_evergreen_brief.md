# Evergreen Brief: enterprise_ai_finops — 2026-10-08
**Archetype:** evergreen
**Vertical:** enterprise_ai_finops
**Persona:** enterprise_cai
**Decision the reader is facing:** Whether to re-architect how the prompt is assembled — a frozen static prefix, volatile content pinned to the tail — so prefix caching actually discounts the bill, and where to draw that cache boundary given each provider's own write/read multipliers and time-to-live window.
**Durability:** The rule is structural, not a news fact: a prefix cache can only reuse a *stable* head, so where the cache boundary is drawn decides the discount, and that holds for as long as providers price reused input below fresh input. The multipliers are stated **as of October 2026** (Anthropic: 5-minute write 1.25×, read 0.1× base input; OpenAI: write 1.25×, read 0.1×, 0.05× on GPT-6.1 Sol; Google: a 90% cached-token discount, 75% on Gemini 2.0) and must be re-read when a vendor changes its rate card — the method does not expire, only the price sheet does.
**De-dup:** Nearest prior artifact is 2026-09-28_gpt6-cache-is-agent-architecture (an unpublished agentic_ai draft) — a single-vendor news piece that framed OpenAI's Sept-22 caching feature as an *interface-design* rule for agent builders; this brief is a cross-provider *FinOps cost model* (write/read multipliers, TTL, break-even reuses, cache-boundary placement) written for the enterprise cost owner, grounded in three vendors' own rate cards plus a measured benchmark that draft never cited. Also distinct from the published 2026-10-07_kv-cache-is-the-concurrency-ceiling (GPU key-value-cache *capacity* on a card, gpu_hardware vertical) and from the 2026-10-01_token-prices-halved-cfo-cant-read-bill news piece (frontier price cuts → attribution), neither of which prices the cache boundary.
**Thesis:** The cache boundary, not the model choice, sets most of an agent's input bill — static context belongs in the cached prefix and volatile content belongs last, because a cached read costs a small fraction of fresh input while a write costs a premium, so a single dynamic token placed ahead of the prefix turns a 90% discount into full price.

**Lead:** The vertical's own beat — `primary_angles` §"prompt prefix caching economics and layout stability" — reinforced by the founder's standing position (`context/growth_os/founder-voice.md` §3, enterprise_ai_finops: naive prefix construction "penalizing inference costs by 5× to 10×"), and grounded in a measured cross-provider benchmark plus the three vendors' own published cache rate cards.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Lumer et al., "Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks" (arXiv:2601.06007, Jan 2026) | https://arxiv.org/abs/2601.06007 | 2026-10-08 | 41-80% — prompt caching cut API costs by 41% to 80% and time-to-first-token by 13% to 31% across OpenAI, Anthropic and Google, over 500+ agent sessions with 10,000-token system prompts | measured |
| 2 | Anthropic, "Prompt caching" documentation (Claude docs) | https://docs.claude.com/en/docs/build-with-claude/prompt-caching | 2026-10-08 | 1.25 times — a 5-minute cache write costs 1.25 times the base input price and cache reads cost 0.1 times the base input price | vendor claim |
| 3 | OpenAI, "Prompt caching" documentation (platform docs) | https://platform.openai.com/docs/guides/prompt-caching | 2026-10-08 | 0.1× — GPT-5.6 and later cache writes cost 1.25× the uncached input rate and reads cost 0.1× that rate (0.05× on GPT-6.1 Sol), cached input discounted up to 95% | vendor claim |
| 4 | Google Cloud, "Context caching overview" (Vertex AI / Gemini Enterprise) | https://cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview | 2026-10-08 | 90% — implicit caching provides a 90% discount on cached tokens versus standard input tokens (75% on Gemini 2.0 models) | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Cache-boundary economics: where the static prefix ends decides the input bill | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| Cost Per Resolved Work-Unit (CRW) with amortized human-in-the-loop review labour | 9 | 8 | 5 | 9 | 7.8 | dropped — no fetchable primary carries the review-labour figures (they live only in `customer-truth.md`), and CRW/attribution was the load-bearing thesis of the 09-24, 10-01 and 10-08 news runs → retread risk |
| Pilot-to-production PoC audit scorecard (graduation scorecard) | 8 | 8 | 6 | 7 | 7.4 | dropped — failure-rate figures are dated vendor surveys that do not retrieve under the gate's fixed user-agent, and the piece degenerates into a statistics listicle (refused by `skills/evergreen_topics.md` §3) |
| Token cost attribution by business unit | 8 | 7 | 6 | 7 | 7.1 | dropped — the 2026-10-08 news run (overrun is funded, not cut) already argued the attribution/ownership thesis |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=4 decision="sha1:145703acc3" dedup="matched a prior artifact: 2026-09-28_gpt6-cache-is-agent-arc" window_days=180 checked_at=2026-10-08T18:02:42+00:00 -->
<!-- evergreen-gate:end -->
