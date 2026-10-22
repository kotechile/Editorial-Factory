# Verified Brief: enterprise_ai_finops — 2026-10-22 (evergreen)

Topic: the review minute. The decision is which pay grade checks an AI output, because the review
line — not the token line — decides the per-unit cost. Archetype: evergreen (no news window, no
virality Judge; this topic's value does not expire inside 90 days).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | Wage anchor — reviewer floor | Paralegals and legal assistants (SOC 23-2011.00) have a median wage of $30.24 an hour, $62,890 a year, on the 2025 wage vintage | VERIFIED | https://www.onetonline.org/link/summary/23-2011.00 | "Median wages (2025) $30.24 hourly, $62,890 annual" |
| 2 | Wage anchor — middle grade | Compliance officers (13-1041.00) have a median wage of $38.81 an hour, $80,730 a year | VERIFIED | https://www.onetonline.org/link/summary/13-1041.00 | "Median wages (2025) $38.81 hourly, $80,730 annual" |
| 3 | Wage anchor — triage grade | Customer service representatives (43-4051.00) have a median wage of $21.53 an hour, $44,770 a year | VERIFIED | https://www.onetonline.org/link/summary/43-4051.00 | "Median wages (2025) $21.53 hourly, $44,770 annual" |
| 4 | Measured review-time reality check | In a randomised controlled trial, 16 experienced developers completing 246 tasks took 19% longer when early-2025 AI tools were allowed, while estimating afterwards that the tools had cut their completion time by 20%; they had forecast a 24% cut before starting | VERIFIED | https://arxiv.org/abs/2507.09089 | "we find that allowing AI actually increases completion time by 19%--AI tooling slowed developers down" / "developers estimate that allowing AI reduced completion time by 20%" / "16 developers with moderate AI experience complete 246 tasks" |
| 5 | Token side — vendor A | Claude Opus 5.5 is billed $4 per million input tokens and $20 per million output tokens, with cache hits at $0.20 per million, on the October 2026 rate card | VERIFIED (vendor claim, labelled as such) | https://docs.claude.com/en/docs/about-claude/pricing | "Claude Opus 5.5 For long-running agentic coding and knowledge work $4 / MTok $20 / MTok $5 / MTok $8 / MTok $0.20 / MTok" / "All prices are in USD." |
| 6 | Token side — vendor B | gpt-6.1-sol is billed $2.00 per million input tokens and $10.00 per million output tokens on the standard lane, $1.00 / $5.00 on batch and $4.00 / $20.00 on fast | VERIFIED (vendor claim, labelled as such) | https://platform.openai.com/docs/pricing | "gpt-6.1-sol $2.00 $10.00 $0.10 $2.50 $5.00" (standard) / "$1.00 $5.00" (batch) / "$4.00 $20.00" (fast) |
| 7 | Desk field note (internal, not a published source) | The vertical's own field note: a legal department's contract-summarising agent cost $0.18 of tokens per agreement; a senior partner spent 25 minutes checking it at a $160-an-hour billed rate ($66.67); cost per resolved work unit came out 2.4× the manual paralegal baseline | INTERNAL FIELD DATA — carried as the desk's own observation, attributed in the article as "our field notes", never as a published statistic | context/growth_os/customer-truth.md (no public URL — must not be cited as a source row) | "costing only $0.18 in raw tokens per agreement … senior partners spent 25 minutes ($160/hour billed rate = $66.67 labor) … the automation was 2.4× more expensive than the legacy manual paralegal review until strict deterministic regex validation was inserted" |

**Arithmetic check (every derived figure, recomputed).**
- $30.24 ÷ 60 = $0.504 a minute → 25 minutes = $12.60. Recompute before publishing: 25 × 0.504 = 12.60. OK.
- $38.81 ÷ 60 = $0.6468 → 25 minutes = $16.17. OK. $21.53 ÷ 60 = $0.3588 → 25 minutes = $8.97. OK.
- $160 ÷ 60 = $2.6667 a minute → 25 minutes = $66.67. OK (and this is the field note's own figure, not a derivation).
- $160 ÷ $30.24 = 5.29 → "5.3 times the median paralegal wage". OK.
- Manual baseline: ($66.67 + $0.18) ÷ 2.4 = $27.85. This is derived from the field note's 2.4× and must be labelled as derived in the article's own sentence, not stated as a measured figure.
- Review ceiling in minutes = ($27.85 − $0.18) ÷ minute rate: at $2.6667 → 10.4 min; at $0.6468 → 42.8 min; at $0.504 → 54.9 min; at $0.3588 → 77.1 min. The ceiling at the partner's rate vs the paralegal's (54.9 ÷ 10.4 = 5.3) is the same 5.3× ratio, not a second finding.
- Annual cross-check: $30.24 × 2,080 = $62,899 against O*NET's $62,890 (rounding in the source). Do not "correct" the source figure.

**Gate rulings for the drafter.**
- Row 7 is NOT citable as a source. The article may say "our field notes" / "one legal department we have seen" and must not attach a `[n]` to it or imply a published URL. The $0.18 / $66.67 / 2.4× figures come from it and are the only internal numbers in the piece.
- Rows 5 and 6 are vendor rate cards: every sentence carrying them attributes the price to the vendor, and no sentence claims a *task* cost the rate card does not print.
- Row 4 is a study of software developers, not of contract review. Any sentence using it states the population (experienced open-source developers, early-2025 tools) and does not generalise the 19% to other work.
- O*NET figures are **median wages**, not loaded employer costs and not billed rates. The article must say so where it compares $30.24 with $160, or the comparison overstates the gap.
- No new figures. The article's numbers are: $0.18, 25 minutes, $160, $66.67, 2.4×, $27.85 (derived), $30.24, $62,890, $38.81, $80,730, $21.53, $44,770, 19%, 20%, 246 tasks, 16 developers, $4/$20/$0.20, $2.00/$10.00, 10.4/42.8/54.9/77.1 minutes, 5.3×.
- Expand every acronym at first use, including Artificial Intelligence (AI). Do not invent an expansion for O*NET or METR — gloss them instead ("O*NET, the US Department of Labor's occupation database"; "METR, a research nonprofit").
