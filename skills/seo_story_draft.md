# SKILL: SEO Story Draft & Growth OS Integration

## 1. Objective
Synthesize the enriched keyword dossier, cannibalization clearance, internal link map, and Growth OS founder voice into a complete, high-ranking, human-voice article.

## 2. Structural Requirements

Every SEO draft must contain the following components:

### A. Frontmatter Metadata
```yaml
---
title: "<headline — 50–70 chars — MUST contain primary_keyword>"
meta_title: "<SEO title tag — 50–60 chars — MUST contain primary_keyword>"
meta_description: "<Meta description — 140–160 chars>"
primary_keyword: "<exact keyword>"
secondary_keywords: ["<cluster 1>", "<cluster 2>", "<cluster 3>"]
search_volume: <number>
search_intent: "<informational|commercial>"
vertical: "<vertical_id>"
persona: "<persona_id>"
date: "YYYY-MM-DD"
slug: "YYYY-MM-DD_<slug>"
---
```

> [!IMPORTANT]
> **Title Keyword Requirement:** The article `title:` and `meta_title:` MUST explicitly incorporate the `primary_keyword` (exact or naturalized proper casing, e.g. `<Primary Keyword>: <Punchy Hook/Angle>`). Never drop, omit, or paraphrase away the target keyword from the title.

### B. Article Body Sections (Clean Markdown & Engaging H2 Headers)
**Formatting requirement:** Every H2 header (`## `) MUST stand on its own separate line, preceded by an empty blank line and followed by an empty blank line. Never place body text or bullets on the same line as the H2 header, and never attach text directly on the line below without an intervening blank line.

- `<!-- lead -->`: Concrete hook featuring an incident, production metric, or specific cost figure (no heading, hook in sentence 1).
- `<!-- tension -->`: `## The big picture:` H2 header + systemic reasons why this happens now, reinforced with **Founder Voice stances** and **Customer Truth anecdotes**.
- `## By the numbers`: Mandatory quantitative H2 section with 2–4 bolded metric bullets pairing figures with concise 2–4 word metric titles before an em-dash (e.g. `- **88% — Diesel price jump:** ...` or `- **21% to 29.5% — UPS fuel fee:** ...`). No conversational filler lead-ins.
- `<!-- tactical-insight -->`: Descriptive `## What I'd watch:` or `## Where the money flows` H2 header + 3 actionable, sequential takeaways addressing secondary keyword clusters.
- `<!-- nuanced-takeaway -->`: `## The catch` H2 header + the honest catch, limitation, or counter-argument.
- `<!-- tldr -->`: `## At a glance` H2 header + 4-part structured breakdown (**The Big Shift**, **Why It Matters**, **The Winning Moves** / **What I'd Watch** with sub-bullet definitions, and **The Fine Print** in plain English), distinctly separated from "The catch".

### C. Citations
- `## Sources`: Verifiable citations `[1]`, `[2]`, `[3]`.

No social variant: the LinkedIn/Reddit channel was removed on 2026-10-06, so a `<!-- linkedin -->`
block is neither required nor wanted.

### D. Machine-Readable SEO Blocks (at document end)
- `<!-- schema -->`: JSON-LD schema block featuring `@type: "Article"` and `@type: "FAQPage"`.
- `<!-- internal-links -->`: leave the marker in place, empty. The links are **not** yours to write:
  they are generated deterministically at persistence/push time (`scripts/internal_links.py`) from the
  live corpus (`context/internal_links.json` — same-site, live, scored), because the drafting stage
  has no list of live pages and every block it filled by hand shipped empty. Never invent a URL,
  never write a site-relative path, and never add links anywhere else in the body.

## 3. Growth OS Moat Rules
1. **Taste Over Fluff**: Never define basic terms in a generic introductory paragraph (e.g., *"Artificial intelligence is changing software"*).
2. **Founder Contrarian Take**: Every piece must feature at least 1 highlighted founder quote or unshakeable stance.
3. **Field Grounding**: Must reference 1 real customer friction scenario or numerical metric.

## 4. Execution Command
```bash
python3 scripts/seo_machine.py --query "<keyword>" --vertical "<vertical_id>"
```
