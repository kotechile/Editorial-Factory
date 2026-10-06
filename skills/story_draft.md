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
| **Tactical insight** | What the people closest to the story are doing, what the consequences land on, and the next signals to watch — reported, never prescribed (`persona:` from `context/personas.json`). Signpost it **Where this bites:** / **What I'd watch:** and bulletize 3+ points. Never instruct the reader (`skills/claude_humanizer.md` §3.9). |
| **Nuanced takeaway** | The honest limitation or counter-argument (**The catch / Between the lines**). Ends on substance, not a cheerlead. |
| **TL;DR (At a Glance)** | 4-part Smart Brevity breakdown (**The Big Shift / What Happened**, **Why It Matters**, **What I'd Watch**, **The Catch / Fine Print**). Must clearly explain what the article is about in sentence 1, articulate the systemic stakes, name what the writer is watching next with plain-English definitions in sub-bullets, and state the trade-offs/caveats. **Long-form only.** |

The **TOC is render-time only** — the site derives it from the section headings. Never write a
"Table of Contents" into the article body.

## 3. Rules
- Inline citations: every factual sentence carries `[n]` mapping to a source list at the end.
- One length: the long-form draft. Do NOT write a LinkedIn/social variant — that channel was
  removed on 2026-10-06 (`skills/publisher.md` §3).
- **SEO frontmatter is optional to author and never invented:** if the brief carries a keyword set, write `meta_title` (≤60 chars) and `meta_description` (140–160 chars) grounded in the article's own headline and lead; if you have neither, omit the keys. The persistence pass derives both from your headline and lead paragraph (`scripts/article_assets.py`) so the CMS excerpt and the frontends' `<meta name="description">` are never empty — do not pad them with claims the article does not make.
- Any claim not in the brief is written as `[NEEDS-SOURCE]` and returned to the verifier — never filled with invention.
- Match the target reader's level from `context/personas.json` for the vertical (`persona:` in frontmatter).
- **Mandatory 'By the numbers:' section:** Every story must include a bolded `**By the numbers:**` section containing 2–4 scannable bullets with bold lead-ins pairing the figure with a concise 2–4 word metric title before an em-dash or colon (e.g. `- **88% — Diesel price jump:** ...` or `- **21% to 29.5% — UPS fuel fee:** ...`). Never start bullet explanations with narrative filler ("Diesel fuel started the year...", "The leap in the..."). This delivers load-bearing data cleanly and ensures automated SVG charts display meaningful, untruncated labels.
- **Observer voice (gated):** the body is a comment on the news, not a verdict and not a playbook:
  each interpreting section (`<!-- tension -->`, `<!-- tactical-insight -->`, `<!-- nuanced-takeaway -->`)
  carries a first-person observer cue, opinion is labelled as opinion, and the tactical section reports
  what the people closest to the story are doing instead of instructing the reader
  (`skills/claude_humanizer.md` §3.9, enforced by `verify.sh` §9).
- **Synthesis Frontmatter (gated):** when the angle brief says `Angle Type: Synthesis`
  (`skills/virality_judge.md` §2.5), the draft **must** carry both keys or `verify.sh` §8 fails the
  build:
  ```yaml
  synthesis: true
  sources:
    - <Signal A's primary anchor URL>
    - <Signal B's primary anchor URL>
  ```
  Inline form (`sources: [<url>, <url>]`) is accepted, and the anchors must be traceable to the
  matching `_signals.md`. This flag is what marks the article as a fusion on the dashboard's own
  surfaces (`/api/articles.json`, the article page badge) — an unflagged synthesis publishes as a
  single-signal story.
- **At a Glance (TL;DR) Schema:** The `<!-- tldr -->` section must be a complete executive briefing that explains what the article is about in ~30 seconds using this exact 4-part plain-English structure:
  1. `- **The Big Shift:** <1-2 sentences explaining what happened and what the article is about in clear, contextual terms>`
  2. `- **Why It Matters:** <1-2 sentences stating the systemic, financial, or architectural stakes for the reader>`
  3. `- **What I'd Watch:** <intro line naming what the writer is watching next, and why>` followed by indented sub-bullets:
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
# Synthesis articles only (Angle Type: Synthesis — see §3, gated by verify.sh §8):
# synthesis: true
# sources:
#   - <Signal A's primary anchor URL>
#   - <Signal B's primary anchor URL>
# Optional external links:
# article_url: https://pressflow.io/articles/... (or external illustrated post)
# promo_url: https://factory.example.com/tools/... (e.g. software factory tool)
# promo_label: "🛠️ Try the tool:"
---

<!-- lead -->
<concrete incident/stat — core news delivered immediately in sentence 1, hook first, no heading>

<!-- tension -->

## The big picture:

<the systemic shift / why now>

## By the numbers

- **<Stat 1> — <Metric Title>:** <concrete context and citation [1]>
- **<Stat 2> — <Metric Title>:** <concrete context and citation [2]>
- **<Stat 3> — <Metric Title>:** <concrete context and citation [3]>

<!-- tactical-insight -->

## What I'd watch:

<the doable moves — structured cleanly for the persona>
- **<Move 1>:** ...
- **<Move 2>:** ...

<!-- nuanced-takeaway -->

## The catch

<the honest limitation / counter-argument>

<!-- tldr -->

## At a glance

- **The Big Shift:** <1-2 sentences explaining what happened and what the article is about in plain English>
- **Why It Matters:** <1-2 sentences articulating the economic/operational impact>
- **The Winning Moves:** <what the writer is watching next, and why> (or **What I'd Watch:**)
  - **<Move 1>:** <plain English definition of what it does and why>
  - **<Move 2>:** <plain English definition of what it does and why>
  - **<Move 3>:** <plain English definition of what it does and why>
- **The Fine Print:** <practical caveats, trade-offs, and realistic constraints> (or **The Catch:**)

## Sources
[1] ...  [2] ...
```

## 5. Failure handling
Draft thinner than ~800 words despite a full brief → the brief is under-sourced; return to the
verifier, not to padding. Log the gap to `skills/self_improvement_eval.md`.

