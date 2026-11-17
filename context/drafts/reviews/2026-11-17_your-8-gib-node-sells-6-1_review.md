# Review report — 2026-11-17_your-8-gib-node-sells-6-1_final.md

- verdict: **ACCEPTED**
- draft: `2026-11-17_your-8-gib-node-sells-6-1_draft.md` · attempt kept: 2 of 2
- figures in the ledger: 27 · citations: 4 · quotes: 0 · sources: 4
- reader-side critic: 0 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A node's spec sheet overstates usable memory because the scheduler advertises memory minus a vendor-set reserve, and the gap between Google's 24% and Azure's 8% on an 8 GiB node means capacity plans must be built from allocatable memory, not the advertised figure.
SHAPE: Lead: establish the hidden reserve and the two vendors' different cuts ; At a glance: three-line summary of the shift, the number, and the risk ; The big picture: explain the kubelet floor, then each vendor's formula, then what the ladder does across node sizes ; By the numbers: three figures the prose does not restate ; What I'd watch: the kernel's throttle point and kill order, plus the reserve becoming configurable ; The catch: vendor caveats and what still holds true.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 970 | 954 |
| sentence length mean | 16.5 | 16.4 |
| sentence length spread (sd) | 7.3 | 7.3 |
| rhythm health (0-1) | 0.858 | 0.852 |
| short sentences (<=8 words) | 12.5% | 12.7% |
| filler per 1,000 words | 1.03 | 1.05 |
| hedge per 1,000 words | 1.03 | 1.05 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 58.9 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Attempt trail

```
{"attempt": 1, "ok": true, "hard": 0, "regressions": 1, "rhythm_sd": [7.3, 7.4], "rhythm_health": [0.858, 0.866], "filler": [1.03, 1.05], "words": 951, "flesch": 60.9, "score": [true, 0, -0.77], "critic_fails": 0, "critic_advisories": 0}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 0, "rhythm_sd": [7.3, 7.3], "rhythm_health": [0.858, 0.852], "filler": [1.03, 1.05], "words": 954, "flesch": 58.9, "score": [true, 0, -0.08], "critic_fails": 0, "critic_advisories": 0}
```
