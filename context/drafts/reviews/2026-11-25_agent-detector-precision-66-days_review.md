# Review report — 2026-11-25_agent-detector-precision-66-days_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-25_agent-detector-precision-66-days_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 14 · citations: 6 · quotes: 0 · sources: 6
- reader-side critic: 3 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: Agent-failure detection is getting precise on the bugs that file reports while the costliest failures stay invisible for months, because the tools are trained on the visible half of the failure surface.
SHAPE: lead — the collision in two numbers, precision vs. disclosure lag; At a glance — one plain paragraph under 50 words naming subject, audience, finding; tension (chronology) — the 10 Nov ledger snapshot, the 21 Nov Apsis release, and why the training data guarantees the blind spot, with the Anthropic and OpenAI review-scale misses as evidence; By the numbers — three figures the prose does not restate; tactical — who actually notices failures (outsiders in 21 of 66 cases), the un-escalated Hugging Face signals, and the outages closed with no cause on file, ending with what the closest teams are doing about trace keeping; The catch — 91% precision is measured on the visible few, RecordRoute advances on the same set, and the trace that outlives the run has no metric at all.
NOT YET EARNED: the draft's "its authors do not claim otherwise" is a hedge about the paper's stance that the brief does not verify — cut or soften to my own reading. The two-citation sentence on the OpenAI outage must consolidate to the mirror [4] since the duration detail is quoted from it. The "At a glance" box ran 58 words; the heading "Two records, eleven days apart" promised an enumeration the body never delivered — drop the count heading or number the items. Hedge density rose to 2.43 per 1,000 words: cut "I hold this thesis with one caveat", "What I find telling", "What I find hard to square" and replace with plain first-person observations, one per interpreting section.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 741 | 822 |
| sentence length mean | 13.7 | 19.1 |
| sentence length spread (sd) | 5.5 | 10.0 |
| rhythm health (0-1) | 0.379 | 0.719 |
| short sentences (<=8 words) | 15.4% | 8.7% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 1.35 | 2.43 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 54.1 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- hedge density rose: 1.35 -> 2.43 per 1,000 words

## Advisories

- hedge density rose: 1.35 -> 2.43 per 1,000 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 2, "regressions": 0, "rhythm_sd": [5.5, 10.5], "rhythm_health": [0.379, 0.549], "filler": [0.0, 0.0], "words": 899, "flesch": 46.7, "score": [false, -2, 1.5], "critic_fails": 0, "critic_advisories": 0}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 1, "rhythm_sd": [5.5, 10.0], "rhythm_health": [0.379, 0.719], "filler": [0.0, 0.0], "words": 822, "flesch": 54.1, "score": [true, 0, 2.07], "critic_fails": 3, "critic_advisories": 0}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [5.5, 10.4], "rhythm_health": [0.379, 0.623], "filler": [0.0, 0.0], "words": 984, "flesch": 44.5, "score": [false, -1, 1.14], "critic_fails": 0, "critic_advisories": 0}
```
