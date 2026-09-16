# SKILL: Story Draft (Structural First Pass)

## 1. Objective
Assemble the verified brief into an authoritative structural draft using **only** the VERIFIED
evidence set. No new facts. Provide clear inputs for the Stylist's Smart Brevity rewrite.

## 2. The house structure
| Section | Rule |
|---|---|
| **Title** | Start with a short, punchy initial title (the Stylist will refine for SEO rewording / resonance). |
| **Lead** | A concrete incident or figure from the evidence delivering the core news in sentence 1. Not a definition, not a "world is changing" opener. |
| **Tension** | The systemic reason this is happening now — who it hurts, who it helps, what changed (**Why it matters / The big picture**). |
| **By the numbers** | Mandatory quantitative data section (**By the numbers:**) highlighting 2–4 verified figures, percentages, benchmarks, or cost changes in clean, bolded scannable bullets. |
| **Tactical insight** | The actionable, specific takeaways for the target reader (`persona:` from `context/personas.json`). Sequence 3+ points cleanly for bulletization. |
| **Nuanced takeaway** | The honest limitation or counter-argument (**The catch / Between the lines**). Ends on substance, not a cheerlead. |
| **TL;DR (At a Glance)** | 3-part structured breakdown (**The Reality Check**, **The Winning Moves**, **The Fine Print**). Must clearly explain what happened, break down the moves with plain-English definitions in sub-bullets, and state the trade-offs/caveats. **Long-form only.** |

The **TOC is render-time only** — the site derives it from the section headings. Never write a
"Table of Contents" into the article body.

## 3. Rules
- Inline citations: every factual sentence carries `[n]` mapping to a source list at the end.
- Two lengths from one skeleton: long-form draft + ~1,300-char LinkedIn post.
- Any claim not in the brief is written as `[NEEDS-SOURCE]` and returned to the verifier — never filled with invention.
- Match the target reader's level from `context/personas.json` for the vertical (`persona:` in frontmatter).
- **Mandatory 'By the numbers:' section:** Every story must include a bolded `**By the numbers:**` section containing 2–4 scannable bullets with bold lead-ins (e.g. `- **40% routed:** ...`) that deliver the load-bearing quantitative facts before the tactical moves.
- **At a Glance (TL;DR) Schema:** The `<!-- tldr -->` section must follow this exact 3-part plain-English structure:
  1. `- **The Reality Check:** <1-2 sentences exposing the baseline problem/gap in plain English>`
  2. `- **The Winning Moves:** <Intro line summarizing the playbook>` followed by indented sub-bullets:
     - `  - **<Move Name>:** <1-line plain English definition of what it actually does>`
  3. `- **The Fine Print:** <1-2 sentences explaining the trade-offs, upfront design requirements, security/access controls, and realistic caveats>`
- Use the section markers below **verbatim** — the Stylist iterates per section and `verify.sh` checks them.

## 4. Output schema
`context/drafts/YYYY-MM-DD_<slug>_draft.md`:
```markdown
---
title: <short punchy initial headline>
vertical: <id>
persona: <id from context/personas.json>
one_big_thing: "<single most important takeaway or decision>"
date: YYYY-MM-DD
slug: <slug>
# Optional external links:
# article_url: https://pressflow.io/articles/... (or external illustrated post)
# promo_url: https://factory.example.com/tools/... (e.g. software factory tool)
# promo_label: "🛠️ Try the tool:"
---

<!-- lead -->
<concrete incident/stat — core news delivered immediately in sentence 1, hook first, no heading>

<!-- tension -->
<the systemic shift / why now>

**By the numbers:**
- **<Stat 1>:** <concrete context and citation [1]>
- **<Stat 2>:** <concrete context and citation [2]>
- **<Stat 3>:** <concrete context and citation [3]>

<!-- tactical-insight -->
<the doable moves — structured cleanly for the persona>

<!-- nuanced-takeaway -->
<the honest limitation / counter-argument>

<!-- tldr -->
- **The Reality Check:** <core problem/shift in plain English>
- **The Winning Moves:** <summary of playbook>
  - **<Move 1>:** <plain English definition>
  - **<Move 2>:** <plain English definition>
  - **<Move 3>:** <plain English definition>
- **The Fine Print:** <practical catches, access control, and context dependencies>

## Sources
[1] ...  [2] ...

<!-- linkedin -->
<~1,300 chars>
```

## 5. Failure handling
Draft thinner than ~800 words despite a full brief → the brief is under-sourced; return to the
verifier, not to padding. Log the gap to `skills/self_improvement_eval.md`.

