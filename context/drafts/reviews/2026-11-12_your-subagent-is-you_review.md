# Review report — 2026-11-12_your-subagent-is-you_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-12_your-subagent-is-you_draft.md` · attempt kept: 2 of 2
- figures in the ledger: 21 · citations: 4 · quotes: 0 · sources: 4
- reader-side critic: 0 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A subagent inherits its parent's full authority because the boundary is a prompt, not a mechanism — so scope must be a grant checked outside the model, never a role the child can write around.
SHAPE: lead: state the two findings and the gap they share ; tldr: three-line box with shift, number, risk ; tension: chronology of the two papers, then the 45-of-45 result, then the arena's pricing of the gap ; tactical-insight: where checks run decides what they catch, and the vendors' own docs confirm the default ; nuanced-takeaway: the honest limits of the evidence and the unresolved tension in the tools field.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 976 | 940 |
| sentence length mean | 17.4 | 17.4 |
| sentence length spread (sd) | 6.1 | 6.5 |
| rhythm health (0-1) | 0.664 | 0.738 |
| short sentences (<=8 words) | 12.5% | 13.0% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 8.2 | 7.45 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 54.9 (PASS) |
| sections restating the through-line | 2 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- tactical-insight --> carries no first-person sentence — it currently opens "The place a check runs decides the result, and this window measured it one level over. On tool calls, prompt-level guards moved obedience from 67% to …". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 3, "regressions": 0, "rhythm_sd": [6.1, 6.2], "rhythm_health": [0.664, 0.667], "filler": [0.0, 0.0], "words": 966, "flesch": 55.8, "score": [false, -3, -0.02], "critic_fails": 2, "critic_advisories": 0}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [6.1, 6.5], "rhythm_health": [0.664, 0.738], "filler": [0.0, 0.0], "words": 940, "flesch": 54.9, "score": [false, -1, 1.04], "critic_fails": 0, "critic_advisories": 0}
```
