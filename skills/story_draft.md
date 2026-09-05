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
| **TL;DR** | 3 scannable bullets capturing the lead, the insight, and the catch. **Long-form only.** |

The **TOC is render-time only** — the site derives it from the section headings. Never write a
"Table of Contents" into the article body.

## 3. Rules
- Inline citations: every factual sentence carries `[n]` mapping to a source list at the end.
- Two lengths from one skeleton: ~1,200–1,500 word long-form + ~1,300-char LinkedIn post.
- Any claim not in the brief is written as `[NEEDS-SOURCE]` and returned to the verifier —
  never filled with invention.
- Match the target reader's level from `context/personas.json` for the vertical.
- Use the section markers below **verbatim** — the Stylist iterates per section and `verify.sh`
  checks them.

## 4. Output schema
`context/drafts/YYYY-MM-DD_<slug>_draft.md`:
```markdown
---
title: <headline>
vertical: <id>
persona: <id>
date: YYYY-MM-DD
slug: <slug>
# Optional external links:
# article_url: https://pressflow.io/articles/... (or external illustrated post)
# promo_url: https://factory.example.com/tools/... (e.g. software factory tool)
# promo_label: "🛠️ Try the tool:"
---

<!-- lead -->
<concrete incident/stat — 1–3 sentences, hook first, no heading>

<!-- tension -->
<the systemic shift / why now>

<!-- tactical-insight -->
<the doable move>

<!-- nuanced-takeaway -->
<the honest limitation / counter-argument>

<!-- tldr -->
- <bullet 1>
- <bullet 2>
- <bullet 3>

## Sources
[1] ...  [2] ...

<!-- linkedin -->
<~1,300 chars>
```

## 5. Failure handling
Draft thinner than ~800 words despite a full brief → the brief is under-sourced; return to the
verifier, not to padding. Log the gap to `skills/self_improvement_eval.md`.
