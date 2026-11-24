# Signals: enterprise_tech_leadership — 2026-11-24
**Window:** 2026-10-25 → 2026-11-24
**Queries run:** 12 (HN Algolia x10 date-filtered; publisher date checks x4; arXiv n/a this window)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Build vs Buy October 2026 report (first edition, final update) | https://hissingkitty.com/research/build-vs-buy-october-2026 | 2026-10-31 | 26 documented in-house builds this month, 23 of 26 state no saving at all; 177 yearly bills across 68 tools total $6,860,836; ServiceTitan highest median bill ~$120,000 (n=3); report cites external McKinsey State of AI survey (n=1,719): 32% of respondents at AI-using organizations skipped buying at least one product or feature to build it with AI coding tools. Data window Oct 17–31, 2026; self-selected, self-reported; 0 verified replacement reports. | build vs buy | 88 |
| 2 | Indie SaaS founder replaced bought services with AI-built in-house features | https://blog.emailengine.app/how-ai-changed-the-build-vs-buy-equation-in-saas/ | 2026-10-26 | One builder reports replacing landing page, testimonials and docs chatbot with AI-added features to an existing backoffice; ~€300/month SaaS subscriptions dropped, cost was "a few days" of AI coding plans — a single self-reported counter-case to the aggregate build-savings picture. | build vs buy | 70 |
| 3 | AI inference costs: five decisions for engineering leaders | https://one2n.io/blog/ai-inference-costs | 2026-11-08 | Committed-spend discount is "the biggest cut most teams get today" and lowers price, not volume; prompt caching cuts the input side ~85% (total-bill saving scales with input:output ratio — 24% at 2:1 up to 77% at 50:1 on Claude Sonnet 5.5); batch API is half price on Anthropic/Bedrock/OpenAI; Claude Haiku ≈ 1/40 of Opus per token; self-hosting pays off only at high, steady volume. | AI ROI | 82 |
| 4 | 27-year self-hosted Exchange finally retired for Microsoft 365 | https://www.tomshardware.com/software/enthusiast-abandons-self-hosted-microsoft-exchange-after-27-years-moving-mailboxes-to-microsoft-365-replaces-final-on-premises-relay-with-postfix-starttls-and-lets-encrypt-certificates | 2026-11-07 | r/homelab user (Nov 5 post) abandons Exchange kept since 1999: mailboxes already on Microsoft 365; last on-prem role (alert relay) moved to Postfix on Ubuntu LTS; Exchange 2019 end of support and Exchange Server SE subscription licensing were reasons — though existing 2019 licenses could run on SE, so the exit was a choice, not forced. Repatriation runs the other way here: 27 years on-prem → cloud, with a bare-bones open-source relay kept. | cloud repatriation | 65 |

**Dating note:** Row 1's report was first published 2026-10-19 (before the window opened) and its final edition 2026-10-31 carries the complete October figures used here; the row is dated to the final edition. Row 3's date is the page's own `datePublished` (2026-11-08). Rows 2 and 4 carry the publisher's own publication date.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=4 candidates=3 heuristic=0.60-0.73 window=2026-10-25..2026-11-24 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #3 ⨂ #4 | economics_x_architecture | A: AI ROI | B: cloud repatriation | https://one2n.io/blog/ai-inference-costs https://www.tomshardware.com/software/enthusiast-abandons-self-hosted-microsoft-exchange-after-27-years-moving-mailboxes-to-microsoft-365-replaces-final-on-premises-relay-with-postfix-starttls-and-lets-encrypt-certificates | 0.73 | - |
| 2 | #1 ⨂ #3 | economics_x_architecture | A: build vs buy | B: AI ROI | https://hissingkitty.com/research/build-vs-buy-october-2026 https://one2n.io/blog/ai-inference-costs | 0.62 | - |
| 3 | #2 ⨂ #3 | economics_x_architecture | A: build vs buy | B: AI ROI | https://blog.emailengine.app/how-ai-changed-the-build-vs-buy-equation-in-saas/ https://one2n.io/blog/ai-inference-costs | 0.6 | - |

**Heuristic terms (advisory):**
- #1: token_coverage=1.0 intensity=0.73 angle_fit=0.5 contrast=0.5 → 0.73 (economics_x_architecture)
- #2: token_coverage=0.75 intensity=0.85 angle_fit=0.25 contrast=0.5 → 0.62 (economics_x_architecture)
- #3: token_coverage=0.75 intensity=0.76 angle_fit=0.25 contrast=0.5 → 0.6 (economics_x_architecture)
<!-- synthesis-seed:end -->

## Dated background
- McKinsey Global Survey on the State of AI, 2026 (n=1,719; cited by row 1; survey fielded earlier in 2026, outside window): https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- ETR/techstrong.ai open-weight enterprise token share (Sept 2026 survey, published 2026-09-22 — out of window): https://techstrong.ai/articles/open-weight-ai-models-expected-to-capture-41-of-enterprise-token-usage/
- Dubach, "Don't Go Monolithic; the Agent Stack Is Stratifying" (published 2026-02-10 — out of window; HN resubmission 2026-11-13): https://philippdubach.com/posts/dont-go-monolithic-the-agent-stack-is-stratifying/
- beforeyouship.dev batch/caching arithmetic (published 2026-08-31, catalog verified 2026-10-09 — out of window): https://beforeyouship.dev/blog/llm-batch-api-pricing
- Scalar Engineering, "Start with a Monolith Was Good Advice. AI Is Changing That" (2026-11-04; medium.com fetch returned 403, page undatable from the body): https://medium.com/scalar-engineering/architecture-in-the-ai-era-part-1-summary-start-with-a-monolith-was-good-advice-7df0597d0e37
