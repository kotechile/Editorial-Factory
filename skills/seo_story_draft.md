# SKILL: SEO Story Draft & Growth OS Integration

## 1. Objective
Synthesize the enriched keyword dossier, cannibalization clearance, internal link map, and Growth OS founder voice into a complete, high-ranking, human-voice article.

## 2. Structural Requirements

Every SEO draft must contain the following components:

### A. Frontmatter Metadata
```yaml
---
title: "<headline — 50–70 chars>"
meta_title: "<SEO title tag — 50–60 chars>"
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

### B. Article Body Sections (Clean Markdown & Engaging H2 Headers)
- `<!-- lead -->`: Concrete hook featuring an incident, production metric, or specific cost figure.
- `<!-- tension -->`: Descriptive `## ` H2 header + systemic reasons why this happens now, reinforced with **Founder Voice stances** and **Customer Truth anecdotes**.
- `<!-- tactical-insight -->`: Descriptive `## ` H2 header + 3 actionable, sequential takeaways addressing secondary keyword clusters.
- `<!-- nuanced-takeaway -->`: Descriptive `## ` H2 header + the honest catch, limitation, or counter-argument.
- `<!-- tldr -->`: `## Key Takeaways` header + 3 bullet takeaways.

### C. Citations & Social Variants
- `## Sources`: Verifiable citations `[1]`, `[2]`, `[3]`.
- `<!-- linkedin -->`: ~1,300-char LinkedIn post summarizing the contrarian angle.

### D. Machine-Readable SEO Blocks (at document end)
- `<!-- schema -->`: JSON-LD schema block featuring `@type: "Article"` and `@type: "FAQPage"`.
- `<!-- internal-links -->`: 2–3 contextual links to existing published articles with exact anchor text.

## 3. Growth OS Moat Rules
1. **Taste Over Fluff**: Never define basic terms in a generic introductory paragraph (e.g., *"Artificial intelligence is changing software"*).
2. **Founder Contrarian Take**: Every piece must feature at least 1 highlighted founder quote or unshakeable stance.
3. **Field Grounding**: Must reference 1 real customer friction scenario or numerical metric.

## 4. Execution Command
```bash
python3 scripts/seo_machine.py --query "<keyword>" --vertical "<vertical_id>"
```
