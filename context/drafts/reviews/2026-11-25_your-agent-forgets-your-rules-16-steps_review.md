# Review report — 2026-11-25_your-agent-forgets-your-rules-16-steps_final.md

- verdict: **ACCEPTED**
- draft: `2026-11-25_your-agent-forgets-your-rules-16-steps_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 10 · citations: 4 · quotes: 0 · sources: 4
- reader-side critic: 0 holding defect(s), 1 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A long agent run stops obeying the procedure it was given once because decay is driven by step count, not context length — so the procedure has to live outside the context, in an enforced state machine.

SHAPE: lead — states the refutation (step count, not window) and its consequence in four sentences; At a glance — one plain paragraph naming subject, audience, finding; tension — the chronology in strict order (METR horizon trend → 39% multi-turn study → the 10,664-trajectory mechanism study), then the counterintuitive window-trimming result; By the numbers — three one-metric bullets, placed after the mechanism; tactical — what the FSM study did, what it cost, and what to watch (horizon arithmetic); catch — the FSM evidence is young and wide-intervaled, and the refutation matters more than the remedy.

NOT YET EARNED: nothing new needed — all claims trace to the brief. Watch: the draft's "16 a shape marker, not a universal tripwire" is interpretation but supported by "the direction held across every model tested"; keep it labelled as reading. The "part of the decay evidence sits on an abstract" caveat must survive. Fix: the draft opens tactical and catch sections without first-person cues in tension; add one per interpreting section in fresh words. Avoid re-explaining dates after the chronology.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 761 | 859 |
| sentence length mean | 14.0 | 15.6 |
| sentence length spread (sd) | 6.0 | 7.2 |
| rhythm health (0-1) | 0.482 | 0.782 |
| short sentences (<=8 words) | 19.6% | 15.4% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 51.6 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Attempt trail

```
{"attempt": 1, "ok": true, "hard": 0, "regressions": 0, "rhythm_sd": [6.0, 7.2], "rhythm_health": [0.482, 0.782], "filler": [0.0, 0.0], "words": 859, "flesch": 51.6, "score": [true, 0, 2.4], "critic_fails": 0, "critic_advisories": 1}
```
