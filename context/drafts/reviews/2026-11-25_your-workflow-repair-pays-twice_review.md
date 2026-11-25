# Review report — 2026-11-25_your-workflow-repair-pays-twice_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-25_your-workflow-repair-pays-twice_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 8 · citations: 8 · quotes: 0 · sources: 8
- reader-side critic: 0 holding defect(s), 1 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A durable engine's replay preserves recorded history, not payload intent, so both natural repairs lose money in a fixed direction — re-paying committed calls or silently serving a replaced artifact — and a call-identity contract (gate, digest, ledger, fail-closed) closes both for milliseconds.

SHAPE: lead — name the trap in one breath, both failure modes and the contract; At a glance — plain box on what the article is and its one finding; tension — explain durable replay's actual bargain via AWS and Temporal docs, then walk both failure modes, then the contract's identity/checks/guarantee; By the numbers — the three measured figures the prose should not restate; tactical — the crash window as the sharpest unresolved piece, then what the field's closest half-measures (Temporal patching, AWS Express) do and don't cover, plus the de-dup link to the error-text piece; catch — one study's scope, the three-assumption guarantee, and the identity floor where a moved call halts the run for a human.

NOT YET EARNED: the draft cites [5] (AWS Step Functions) for the identity-floor claim, which belongs to the study's identity definition — corrected to [2]. The "12 vs 7" figure needs the live-fanout context made explicit once. The title keeps the primary keyword and the measured contrast. The At a glance box is close to schema but tightened. The catch needs its first-person cue and must not introduce the identity floor cold — it is now set up in the tension section.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 895 | 1022 |
| sentence length mean | 16.5 | 20.2 |
| sentence length spread (sd) | 8.9 | 10.9 |
| rhythm health (0-1) | 0.806 | 0.579 |
| short sentences (<=8 words) | 19.6% | 10.4% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 5.59 | 2.94 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 45.0 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: Flesch 45.0 < floor 50.0 — the long words costing the score, each to be replaced or used once: committed, rewrite, identity, contract, runtime, recorded, workflows, repairs, attempt, workflow, durable, history

## Flow regressions against the draft

- rhythm health fell 0.806 -> 0.579 (mean 16.5 -> 20.2 words, sd 8.9 -> 10.9) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm health fell 0.806 -> 0.579 (mean 16.5 -> 20.2 words, sd 8.9 -> 10.9) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [8.9, 10.9], "rhythm_health": [0.806, 0.579], "filler": [0.0, 0.0], "words": 1022, "flesch": 45.0, "score": [false, -1, -0.23], "critic_fails": 0, "critic_advisories": 1}
```
