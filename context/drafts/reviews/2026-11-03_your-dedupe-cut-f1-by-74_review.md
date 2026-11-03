# Review report — 2026-11-03_your-dedupe-cut-f1-by-74_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-03_your-dedupe-cut-f1-by-74_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 20 · citations: 3 · quotes: 1 · sources: 3

## The reviewer's reading

THROUGH-LINE: A synthetic suite's breadth is set by the axes named in the instruction—not by cases per prompt or post-hoc deduping—so a similarity pass that raises every diversity metric can still cut the score a gate runs on, and teams should re-measure the suite's discrimination, not the diversity number.
SHAPE: Lead: sets the 43.8-point gain against the 7.4-point loss and names the root lever; The big picture: explains why the generator collapses onto the same phrasing and why post-generation filtering improves diversity scores while lowering F1; By the numbers: gives the measured anchors for effective case count and prompt axes; What I'd watch: shows how a production-scale corpus varied audience and format inside the instruction instead of asking for more of the same; The catch: states the small-data limits and the reporting rule; At a glance: distills the risk.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 830 | 830 |
| sentence length mean | 22.1 | 23.3 |
| sentence length spread (sd) | 12.0 | 8.1 |
| rhythm health (0-1) | 0.488 | 0.516 |
| short sentences (<=8 words) | 9.4% | 0.0% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 57.8 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- figure lost: 925 — the draft sentence: "Size is settled elsewhere — [a 100-case eval carries 92.5% coverage, not 95%](/100-case-eval-925-coverage/) — but size and spread are two counts, and the gate only runs one."
- figure lost: 30million — the draft sentence: "**Less than 1% — Duplicate text:** the bloom of 30 million prompts reports under 1% duplicates, against a high duplicate rate when only the wording of one prompt changed [2]."

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 12.0 -> 8.1 (kept 68% of the draft's variance)

## Advisories

- figure not in the draft or the brief: 30 — confirm it is the source's own
- rhythm flattened: sentence-length sd 12.0 -> 8.1 (kept 68% of the draft's variance)

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 5, "regressions": 1, "rhythm_sd": [12.0, 8.9], "rhythm_health": [0.488, 0.96], "filler": [0.0, 0.0], "words": 857, "flesch": 48.8, "score": [false, -5, 3.78]}
{"attempt": 2, "ok": false, "hard": 2, "regressions": 1, "rhythm_sd": [12.0, 8.1], "rhythm_health": [0.488, 0.516], "filler": [0.0, 0.0], "words": 830, "flesch": 57.8, "score": [false, -2, 0.22]}
{"attempt": 3, "ok": false, "hard": 5, "regressions": 1, "rhythm_sd": [12.0, 10.9], "rhythm_health": [0.488, 0.611], "filler": [0.0, 0.0], "words": 809, "flesch": 48.9, "score": [false, -5, 0.18]}
```
