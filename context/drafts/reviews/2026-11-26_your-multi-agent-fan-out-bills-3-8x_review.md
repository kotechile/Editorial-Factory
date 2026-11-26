# Review report — 2026-11-26_your-multi-agent-fan-out-bills-3-8x_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-26_your-multi-agent-fan-out-bills-3-8x_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 11 · citations: 6 · quotes: 1 · sources: 6
- reader-side critic: 0 holding defect(s), 2 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: The same week a vendor put a 16-agent tier on sale, the first equal-cost study showed the default fan-out bills 2.6–3.8× a single agent for 1–5 test points — so headcount is the wrong dial; the recoverable margin sits in instructions, fresh context and routing.

SHAPE: lead — the collision in one breath, product launch against measured price; At a glance — one plain paragraph naming subject, audience, finding; tension (chronology) — 17/24/25 November in order, then the study's design, result and mechanism, dates stated once here; By the numbers — three one-metric bullets after the mechanism is explained; tactical — what the people closest to it are doing: the coordination bench, MeterRouter, CypherMAS, with one first-person cue; catch — scope limits (hard tasks, modular code, non-transfer of the probe), the narrow verdict, no new concepts in the closing.

NOT YET EARNED: the draft says "a quality setting just became a price tag" but Perplexity's page carries no cost figure — keep the price claim attributed to the study only. "Partly pays for checking" is the study's mechanism and needs the probe sentence beside it to be earned. The tactical section's "circulated on Hacker News" is not in the brief — drop it. The catch's "more modular code, more files, shorter functions" is fine (row 4 scope) but must stay hedged as the study's finding on parallel runs.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 702 | 759 |
| sentence length mean | 15.2 | 17.6 |
| sentence length spread (sd) | 5.2 | 9.6 |
| rhythm health (0-1) | 0.392 | 0.726 |
| short sentences (<=8 words) | 11.1% | 20.0% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 1.42 | 2.64 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 53.6 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- tension --> carries no first-person sentence — it currently opens "The launch itself is a fan-out by design. One lead agent assigns up to 16 workers on Claude Opus 5.5, GPT (OpenAI's model line) 6.1 Sol and Gemini 4 C…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [5.2, 9.6], "rhythm_health": [0.392, 0.726], "filler": [0.0, 0.0], "words": 759, "flesch": 53.6, "score": [false, -1, 2.67], "critic_fails": 0, "critic_advisories": 2}
```
