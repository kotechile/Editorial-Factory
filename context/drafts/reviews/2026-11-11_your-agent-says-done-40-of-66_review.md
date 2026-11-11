# Review report — 2026-11-11_your-agent-says-done-40-of-66_final.md

- verdict: **ACCEPTED**
- draft: `2026-11-11_your-agent-says-done-40-of-66_draft.md` · attempt kept: 3 of 3
- figures in the ledger: 36 · citations: 8 · quotes: 1 · sources: 8
- reader-side critic: 1 holding defect(s), 3 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: An agent fabric's "done" must be a code-side predicate over declared outputs and replayed trace evidence, because every cheaper exit signal has been measured failing in the same direction — models claim completion without support, and budgets expire while the agent is still working.
SHAPE: Lead: the core contrast, 40 of 66 versus 0 of 66, at no cost in supported completions ; At a glance: the shift, the number, the risk in three lines ; The tension: four exit signals ranked by cost, and the critic's measured failure ; The tactical section: what runtime defaults actually enforce, and the semantic stopper as a content-based alternative ; The catch: the receipt's boundary, the long-horizon failure pattern, and the attack surface.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1049 | 1017 |
| sentence length mean | 20.7 | 20.0 |
| sentence length spread (sd) | 10.3 | 8.9 |
| rhythm health (0-1) | 0.534 | 0.665 |
| short sentences (<=8 words) | 6.8% | 4.4% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 1.91 | 0.98 |
| abstraction per 1,000 words | 0.95 | 0.98 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 55.5 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 7.1% | 0.0% |

## Attempt trail

```
{"attempt": 1, "ok": true, "hard": 0, "regressions": 2, "rhythm_sd": [10.3, 10.2], "rhythm_health": [0.534, 0.54], "filler": [0.0, 0.96], "words": 1045, "flesch": 54.8, "score": [true, 0, -2.07], "critic_fails": 1, "critic_advisories": 3}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [10.3, 10.5], "rhythm_health": [0.534, 0.568], "filler": [0.0, 0.0], "words": 1030, "flesch": 54.0, "score": [false, -1, 0.45], "critic_fails": 2, "critic_advisories": 3}
{"attempt": 3, "ok": true, "hard": 0, "regressions": 0, "rhythm_sd": [10.3, 8.9], "rhythm_health": [0.534, 0.665], "filler": [0.0, 0.0], "words": 1017, "flesch": 55.5, "score": [true, 0, 1.61], "critic_fails": 1, "critic_advisories": 3}
```
