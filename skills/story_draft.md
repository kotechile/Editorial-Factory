# SKILL: Story Draft (Structural First Pass)

## 1. Objective
Assemble the verified brief into an authoritative structural draft using **only** the VERIFIED
evidence set. No new facts.

## 2. The house structure
| Section | Rule |
|---|---|
| **Lead** | A concrete incident or figure from the evidence. Not a definition, not a "world is changing" opener. |
| **Tension** | The systemic reason this is happening now — who it hurts, who it helps, what changed. |
| **Tactical insight** | The actionable, specific takeaway for the target reader (persona from `context/personas.json`). |
| **Nuanced takeaway** | The honest limitation or counter-argument. Ends on substance, not a cheerlead. |

## 3. Rules
- Inline citations: every factual sentence carries `[n]` mapping to a source list at the end.
- Two lengths from one skeleton: ~1,200–1,500 word long-form + ~1,300-char LinkedIn post.
- Any claim not in the brief is written as `[NEEDS-SOURCE]` and returned to the verifier —
  never filled with invention.
- Match the target reader's level from `context/personas.json` for the vertical.

## 4. Output
`context/drafts/YYYY-MM-DD_<slug>_draft.md`:
```markdown
# <Headline>
**Vertical:** <id>  **Persona:** <id>  **Date:** YYYY-MM-DD
<lead / tension / tactical insight / nuanced takeaway>
## Sources
[1] ...  [2] ...
---
## LinkedIn variant
<~1,300 chars>
```

## 5. Failure handling
Draft thinner than ~800 words despite a full brief → the brief is under-sourced; return to the
verifier, not to padding. Log the gap to `skills/self_improvement_eval.md`.
