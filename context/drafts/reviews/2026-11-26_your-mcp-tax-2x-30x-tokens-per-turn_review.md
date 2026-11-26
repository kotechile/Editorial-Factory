# Review report — 2026-11-26_your-mcp-tax-2x-30x-tokens-per-turn_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-26_your-mcp-tax-2x-30x-tokens-per-turn_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 15 · citations: 4 · quotes: 0 · sources: 4
- reader-side critic: 0 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: Mounting MCP servers the default way re-bills every tool schema on every turn (2x–30x prompt inflation), and retrieval plus sandboxing removes almost all of that cost without losing the right tool.

SHAPE: lead — states the tax and the one measured fix that dissolves it; At a glance — one plain paragraph naming subject, audience, finding; tension — explains the mechanism (stateless chat APIs force full-catalog re-sends) and where it bites hardest; By the numbers — three figures the prose does not restate, placed after the mechanism; tactical — the two production directions (retrieval, sandbox) plus description curation, with measured trade-offs; catch — what each fix gives back, and the pricing discipline that should replace the default.

NOT YET EARNED: the draft's "retrieval's hit rate still falls short of perfect" is vague — it should be tied to the 97.1% figure it already has. The "two paths compound" line arrives before the sandbox is explained; reorder. The internal link to tool-surface practices is kept as context, not evidence. The verified brief attached to this dispatch describes a Türkiye residence-permit story and shares no sources with this draft; I have treated the draft's own DO-NOT-LOSE facts and source list as authoritative and made no claim from the brief.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 644 | 653 |
| sentence length mean | 16.9 | 17.2 |
| sentence length spread (sd) | 6.9 | 7.2 |
| rhythm health (0-1) | 0.8 | 0.885 |
| short sentences (<=8 words) | 8.3% | 8.3% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 57.0 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "Each fix gives something back. Retrieval found the right tool first on 97.1% of test queries, which means roughly one query in thirty starts with the …". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [6.9, 7.2], "rhythm_health": [0.8, 0.885], "filler": [0.0, 0.0], "words": 653, "flesch": 57.0, "score": [false, -1, 0.68], "critic_fails": 0, "critic_advisories": 0}
```
