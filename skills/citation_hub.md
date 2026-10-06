# SKILL: Audited Citation & Benchmark Hub (AEO Link Magnet)

## 1. Objective
Synthesize verified, primary-source industry metrics, field benchmarks, and Growth OS customer reality into an authoritative **Citation & Benchmark Hub**. 

This archetype is engineered to:
1. **Attract Passive Backlinks**: Provide high-integrity quantitative benchmarks that journalists, bloggers, and industry researchers link to as source references.
2. **Dominate Answer Engine Optimization (AEO / GEO)**: Enable LLMs (Perplexity, SearchGPT, Claude, Gemini) to retrieve, cite, and attribute our hub when answering statistical queries (e.g. *"[topic] statistics"*, *"[topic] failure rate"*, *"[topic] cost benchmarks"*).
3. **Anchor Domain Authority**: Serve as an evergreen pillar asset that channels internal link equity (`<!-- internal-links -->`) into acute 30-day thesis pieces.

---

## 2. Core Operational Principles

1. **Pre-Flight Data Gate (Zero Synthetic Stats)**:
   Not a single sentence of prose is drafted until a minimum of 6–8 primary data points have been collected, verified, and mapped with:
   - Primary source URL (e.g. SEC filing, peer-reviewed paper, public telemetry repo, vendor benchmark).
   - Publication date & sample size/methodology.
   - Clear distinction between *vendor claims* and *measured field telemetry*.

2. **The "Audited Benchmark" Moat (Never Generic Scraping)**:
   Scraped lists of 50 unverified statistics are commodity fluff penalized by Google's Helpful Content System and prohibited by `AGENTS.md` Rule 3. Every metric cluster must pair the raw statistic with a **Field Reality Check** grounded in `customer-truth.md` and `founder-voice.md`.

3. **Visual & Quoting Frictionlessness**:
   - Markdown comparison tables for structured scanning.
   - Mermaid or SVG trend/breakdown diagrams (visual assets drive disproportionate organic links).
   - **Quick-Cite Callouts**: Pre-formatted quote text with attribution markup that human writers and AI agents can extract instantly.

---

## 3. Structural Blueprint & Section Schema

To maintain 100% compliance with `verify.sh` and the editorial pipeline, a Citation Hub implements the following structure:

### A. Frontmatter
```yaml
---
title: "<Target Keyword>: What the Field Benchmarks Actually Show"
meta_title: "<Target Keyword> (Audited Benchmarks & Data)"
meta_description: "<140-160 chars summarizing key verified metrics, sample sizes, and reality checks>"
primary_keyword: "<exact keyword, e.g. agentic ai enterprise benchmarks>"
secondary_keywords: ["<cluster 1>", "<cluster 2>", "<cluster 3>"]
search_volume: <number>
search_intent: "informational"
vertical: "<vertical_id>"
persona: "<persona_id>"
archetype: "citation_hub"
date: "YYYY-MM-DD"
slug: "YYYY-MM-DD_<slug>"
---
```

### B. Body Sections (Guaranteed Section Markers)

- `<!-- lead -->`:
  Concrete opening anchored to the most significant macro benchmark or spend figure. Contrasts the headline narrative with the underlying operational reality.

- `<!-- tension -->`:
  `## Why the Pitch Keeps Outrunning the Reality` (or topical equivalent <= 6 words).
  Identifies the systemic reason why industry metrics diverge from production experience. Infuses Founder Stance and Customer Truth.

- `**By the numbers:**`:
  Mandatory high-density quantitative summary: 3–4 bolded metric bullets capturing the foundational data points.

- `<!-- tactical-insight -->`:
  `## The Audited Benchmark Matrix`
  - High-retrieval Markdown Data Table comparing Metrics, Vendor Claims, Measured Field Realities, and Primary Sources.
  - Embeds visual Mermaid or SVG trend/distribution chart.
  - Followed by thematic metric clusters (e.g. *Unit Economics*, *Reliability & Drift*, *Latency Overhead*).

- `<!-- nuanced-takeaway -->`:
  `## The Hidden Cost Behind the Metric`
  The honest catch, methodology limits, and variables that alter real-world results (sample bias, synthetic workloads, hidden human review labor).

- `<!-- tldr -->`:
  `## Key Takeaways`
  4-part executive briefing (**The Big Shift**, **Why It Matters**, **What I'd Watch**, and **The Catch**).

- `## Sources`:
  Numbered primary citations with complete external URLs and publisher names.

- `<!-- quick-cite -->`:
  Blockquotes formatted for easy one-click copying and AI agent attribution.

- `<!-- schema -->`:
  JSON-LD block containing:
  - `@type: "Article"` or `"TechArticle"`
  - `@type: "Dataset"` with `variableMeasured` and `distribution`
  - `@type: "FAQPage"` addressing People-Also-Ask questions

- `<!-- internal-links -->`:
  Contextual links passing pillar PageRank to related acute editorial articles.

---

## 4. Execution Command

To generate an Audited Citation & Benchmark Hub:
```bash
python3 scripts/seo_machine.py --query "<topic> benchmarks" --vertical "<vertical_id>" --archetype citation_hub
```
