# SKILL: Story Draft (Structural First Pass)

## 1. Objective
Assemble the verified brief into an authoritative structural draft using **only** the VERIFIED
evidence set. No new facts. Provide clear inputs for the Stylist's Smart Brevity rewrite.

## 2. The house structure
| Section | Rule |
|---|---|
| **Title** | Start with a short, punchy initial title (the Stylist will refine for SEO rewording / resonance). For **Synthesis articles**, frame as a high-stakes question or collision thesis (e.g., *"Would Lower LLM Frontier Prices Drive More Reliable In-House Development?"*). When drafting for an SEO keyword (`primary_keyword:` in frontmatter), the title MUST contain the target keyword. |
| **Lead** | A concrete incident or figure from the evidence delivering the core news in sentence 1. For **Synthesis articles**, write a **Collision Lead**: bridge the two underlying developments in the first 1–2 sentences (e.g., *"As frontier model inference prices plunge past 80% cuts, enterprise engineering teams are quietly turning their backs on off-the-shelf SaaS to build bespoke in-house software."*). Not a definition, not a "world is changing" opener. |
| **Tension** | The systemic reason this is happening now — who it hurts, who it helps, what changed (**Why it matters / The big picture**). In a synthesis piece, explain the friction point where Trend A radically alters the economics, reliability, or feasibility of Trend B. |
| **By the numbers** | Mandatory quantitative data section (**By the numbers:**) highlighting 2–4 verified figures, percentages, benchmarks, or cost changes in clean, bolded scannable bullets. In synthesis articles, bullets must represent verifiable data from **both** underlying anchors. |
| **Tactical insight** | The actionable, specific takeaways for the target reader (`persona:` from `context/personas.json`). Sequence 3+ points cleanly for bulletization. |
| **Nuanced takeaway** | The honest limitation or counter-argument (**The catch / Between the lines**). Ends on substance, not a cheerlead. |
| **TL;DR (At a Glance)** | 4-part Smart Brevity breakdown (**The Big Shift / What Happened**, **Why It Matters**, **The Winning Moves**, **The Catch / Fine Print**). Must clearly explain what the article is about in sentence 1, articulate the systemic stakes, break down the tactical moves with plain-English definitions in sub-bullets, and state the trade-offs/caveats. **Long-form only.** |

The **TOC is render-time only** — the site derives it from the section headings. Never write a
"Table of Contents" into the article body.

## 3. Rules
- Inline citations: every factual sentence carries `[n]` mapping to a source list at the end.
- Two lengths from one skeleton: long-form draft + ~1,300-char LinkedIn post.
- Any claim not in the brief is written as `[NEEDS-SOURCE]` and returned to the verifier — never filled with invention.
- Match the target reader's level from `context/personas.json` for the vertical (`persona:` in frontmatter).
- **Mandatory 'By the numbers:' section:** Every story must include a bolded `**By the numbers:**` section containing 2–4 scannable bullets with bold lead-ins (e.g. `- **40% routed:** ...`) that deliver the load-bearing quantitative facts before the tactical moves.
- **Synthesis Frontmatter:** For multi-topic synthesis articles, include `synthesis: true` and list the primary source URLs in `sources: [...]`.
- **At a Glance (TL;DR) Schema:** The `<!-- tldr -->` section must be a complete executive briefing that explains what the article is about in ~30 seconds using this exact 4-part plain-English structure:
  1. `- **The Big Shift:** <1-2 sentences explaining what happened and what the article is about in clear, contextual terms>`
  2. `- **Why It Matters:** <1-2 sentences stating the systemic, financial, or architectural stakes for the reader>`
  3. `- **The Winning Moves:** <Intro line summarizing the tactical playbook>` followed by indented sub-bullets:
     - `  - **<Move Name>:** <1-line plain-English definition explaining what it does and why it works>`
  4. `- **The Catch:** <1-2 sentences detailing the trade-offs, upfront design requirements, security/access controls, and realistic caveats>`
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
- **The Big Shift:** <1-2 sentences explaining what happened and what the article is about in plain English>
- **Why It Matters:** <1-2 sentences articulating the economic/operational impact>
- **The Winning Moves:** <summary of playbook>
  - **<Move 1>:** <plain English definition of what it does and why>
  - **<Move 2>:** <plain English definition of what it does and why>
  - **<Move 3>:** <plain English definition of what it does and why>
- **The Catch:** <practical caveats, access control, and context dependencies>

## Sources
[1] ...  [2] ...

<!-- linkedin -->
<~1,300 chars>
```

## 5. Failure handling
Draft thinner than ~800 words despite a full brief → the brief is under-sourced; return to the
verifier, not to padding. Log the gap to `skills/self_improvement_eval.md`.

