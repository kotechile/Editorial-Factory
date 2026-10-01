# SKILL: DataForSEO Enrichment & SERP Competitor Analysis

## 1. Objective
Enrich GSC search signals with third-party keyword data, search intent, keyword clusters, and competitor SERP structures before drafting begins.

## 2. Ingestion
- **Input:** Target query from GSC Scout or manual trigger.
- **Tool:** `scripts/dataforseo_client.py` (via DataForSEO v3 API / MCP).

## 3. Enrichment Protocol

### Stage 1 — Keyword Metrics
Extract:
- **Search Volume**: Monthly average search queries in target region (US/Global).
- **Cost Per Click (CPC)**: Commercial value indicator.
- **Keyword Difficulty (KD)**: 0–100 scale measuring domain competition.
- **Search Intent**: `informational`, `commercial`, `transactional`, or `navigational`.

### Stage 2 — Semantic Keyword Clusters
Pull 5–8 related long-tail keywords and semantic variations to use as secondary keywords and H2/H3 subheadings in the draft.

### Stage 3 — SERP Competitor Landscape
Examine the top 10 ranking URLs:
1. **Headline Angle Analysis**: What promise are competitors making?
2. **Missing Gaps & Thin Content**: Where do generic competitor guides fail to provide concrete code, cost math, or operational realities?
3. **People Also Ask (PAA)**: the generator does NOT query Google PAA. `enrich_keyword()` emits three
   templated questions ("What is the biggest bottleneck in {keyword}?" …) that are embedded into
   `FAQPage` schema and answered from the article's own audited content. Treat them as the page's FAQ —
   self-authored Q&A, which is what FAQPage schema is for — and do not describe them as researched
   PAA questions. The client marks this as `paa_source: "generated"`.

## 4. Execution Command
```bash
python3 scripts/dataforseo_client.py --keyword "<target_query>" --json
```

## 5. Viability Gate
- If search volume < 200 AND KD > 80 without clear commercial intent, flag as low ROI and select the next candidate from the GSC shortlist.
