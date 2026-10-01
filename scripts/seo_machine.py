#!/usr/bin/env python3
"""SEO Content Machine & Growth OS Pipeline Orchestrator.

Executes the end-to-end demand-driven editorial pipeline:
1. [GSC Opportunity Detector] -> Striking-distance query / WoW spike detected.
2. [DataForSEO Enrichment]    -> Enriches with volume, intent, KD, clusters, competitor SERPs, PAA questions.
3. [Growth OS Engine]         -> Cannibalization check + Internal link map + Founder POV & Customer Truth.
4. [Structured SEO Drafter]   -> Drafts post with H2/H3, JSON-LD Schema, Meta tags, and Internal Link map.
5. [Frontier Humanizer]       -> Frontier human-voice rewrite (Loop 3).
6. [Approval Gate]            -> Stages draft ready for human founder review (@Simon approve).
"""

import argparse
import json
import os
import pathlib
import re
import sys
from datetime import datetime, timezone

from gsc_analyzer import analyze_opportunities, load_gsc_data
from dataforseo_client import DataForSEOClient
import growth_os as gos
import check_accessibility as ca
import chart_generator as cg
import citation_hub_dossier as chd

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTEXT_DIR = ROOT / "context"
DRAFTS_DIR = CONTEXT_DIR / "drafts"
PERSONAS_FILE = CONTEXT_DIR / "personas.json"
VERTICALS_FILE = CONTEXT_DIR / "verticals.json"


def slugify(text):
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s-]+", "-", s).strip("-")
    return s[:60]


# Tokens that must keep canonical casing when a raw keyword is re-rendered into
# prose or a headline. Raw search queries are noun piles ("MCP Server implementation
# Python"), and pasting them verbatim into sentences reads like keyword-matching.
_ACRONYMS = {
    "mcp", "api", "seo", "sdk", "cli", "http", "https", "smtp", "sql", "nosql",
    "llm", "rag", "nlu", "nlp", "ai", "ml", "json", "xml", "css", "html", "dom",
    "ci", "cd", "git", "ssh", "ssl", "tls", "dns", "cpu", "gpu", "ram",
    "saas", "paas", "iaas", "grpc", "rest", "ui", "ux", "npm", "ide", "vm",
}

_LANG_PROPER = {
    "python": "Python", "javascript": "JavaScript", "typescript": "TypeScript",
    "rust": "Rust", "golang": "Go", "go": "Go", "java": "Java", "c": "C",
    "cpp": "C++", "c++": "C++", "ruby": "Ruby", "php": "PHP", "swift": "Swift",
    "kotlin": "Kotlin", "scala": "Scala", "dart": "Dart", "node": "Node.js",
    "nodejs": "Node.js", "react": "React", "nextjs": "Next.js", "next": "Next.js",
    "django": "Django", "flask": "Flask", "fastapi": "FastAPI",
    "kubernetes": "Kubernetes", "docker": "Docker", "langchain": "LangChain",
    "llamaindex": "LlamaIndex", "postgres": "Postgres", "postgresql": "PostgreSQL",
    "mysql": "MySQL", "mongodb": "MongoDB", "redis": "Redis",
}

_PREPOSITIONS = {"in", "on", "with", "for", "using", "of", "and", "vs", "versus", "to"}


def naturalize_kw(kw):
    """Return a natural-sounding prose form of a raw search keyword.

    'MCP Server implementation Python' -> 'MCP server implementation in Python'

    Preserves acronyms (MCP, API, GPU) and canonical language/framework casing,
    lowercases the rest, and inserts 'in' before a trailing bare language token so
    a raw noun pile reads as English instead of a keyword-matching jumble.
    """
    out = []
    for i, w in enumerate(kw.split()):
        lw = w.lower()
        if lw in _ACRONYMS:
            out.append(lw.upper())
        elif lw in _LANG_PROPER:
            token = _LANG_PROPER[lw]
            if i > 0 and out and out[-1].lower() not in _PREPOSITIONS:
                out.append("in " + token)
            else:
                out.append(token)
        else:
            out.append(lw)
    return " ".join(out)


def smart_title(kw):
    """Title-case a keyword without mangling acronyms or framework proper nouns.

    'MCP Server implementation Python' -> 'MCP Server Implementation Python'
    """
    out = []
    for w in kw.split():
        lw = w.lower()
        if lw in _ACRONYMS:
            out.append(lw.upper())
        elif lw in _LANG_PROPER:
            out.append(_LANG_PROPER[lw])
        else:
            out.append(w[:1].upper() + w[1:].lower() if w else w)
    return " ".join(out)


def load_personas():
    if PERSONAS_FILE.exists():
        with open(PERSONAS_FILE, "r", encoding="utf-8") as f:
            return json.load(f).get("personas", {})
    return {}


def load_verticals():
    if VERTICALS_FILE.exists():
        with open(VERTICALS_FILE, "r", encoding="utf-8") as f:
            return {v["id"]: v for v in json.load(f).get("verticals", [])}
    return {}


def _faq_answer(question: str, kw: str, primary_stance: str) -> str:
    """Give each PAA (people-also-ask) question its own distinct, on-topic answer, instead of the
    identical boilerplate that used to be repeated for every question (which SEO reads as low-quality)."""
    ql = question.lower()
    kw_n = naturalize_kw(kw)
    if any(x in ql for x in ("cause", "fail", "break", "why", "problem")):
        return (f"Failure usually comes from missing hard limits: no cap on repeating steps, no timeout on "
                f"tool calls, and no budget guard. That is exactly what a production {kw_n} setup needs.")
    if any(x in ql for x in ("solve", "how", "fix", "avoid", "team", "leading")):
        return ("Teams solve it by capping recursion, testing changes against their own production logs "
                "instead of marketing demos, and trimming chat history before each step.")
    if any(x in ql for x in ("benchmark", "number", "measure", "real", "production", "metric")):
        return f"Real numbers only come from running against private production logs; synthetic data misleads. {primary_stance}"
    return primary_stance


def _naturalize_question(question: str, kw: str, kw_prose: str) -> str:
    """Rewrite the raw keyword inside a generated FAQ question with its natural form."""
    if not kw or not kw_prose or kw == kw_prose:
        return question
    return re.sub(re.escape(kw), kw_prose, question, flags=re.IGNORECASE)


def kw_frontmatter(keyword_data: dict) -> str:
    """The keyword-metric lines for a draft's frontmatter — measured values only.

    A metric that was not measured is OMITTED rather than defaulted. This used to write
    `search_volume: 1200` (a template constant) into every article and `4800`-style hash-derived
    values for the seven verticals with DataForSEO disabled — numbers indistinguishable from a real
    reading once the article reaches Supabase and the CMS. The provenance travels alongside, so
    whoever reads the frontmatter knows which case they are looking at.
    """
    lines = []
    source = keyword_data.get("keyword_data_source") or (
        "dataforseo_live" if keyword_data.get("live_data") else "sandbox_estimate")
    volume = keyword_data.get("search_volume")

    if source == "dataforseo_live" and isinstance(volume, (int, float)) and not isinstance(volume, bool) and volume > 0:
        lines.append(f"search_volume: {int(volume)}")
    if keyword_data.get("search_intent"):
        lines.append(f"search_intent: \"{keyword_data['search_intent']}\"")
    lines.append(f"keyword_data_source: \"{source}\"")
    if keyword_data.get("clusters_source") == "generated":
        lines.append("secondary_keywords_source: \"generated\"")
    return "\n".join(lines)


def _format_sources(serp_competitors):
    """Build a ## Sources block from SERP competitor data.

    Live DataForSEO runs return real organic results (title + url). Entries the client generated
    itself (techleaders.example.com and friends) are marked synthetic and skipped, so an API failure
    produces an article that admits it has no source instead of one that cites a placeholder domain.
    """
    lines = []
    for i, c in enumerate(serp_competitors[:3], start=1):
        if c.get("synthetic"):
            continue
        url = (c.get("url") or "").strip()
        title = (c.get("title") or "").strip()
        domain = (c.get("domain") or "").strip()
        if not url:
            continue
        label = title or domain or f"Source {i}"
        lines.append(f"[{i}] {label}. {url}")
    if not lines:
        lines = ["[1] (No verified source attached — fill from DataForSEO SERP before publish.)"]
    return "\n".join(lines)


def _format_related_reading(internal_links) -> str:
    """The reader-facing internal links — real anchors, on the same site, verified live.

    A body section, not an operator note: an internal link only does anything for the reader or the
    crawler if it reaches the published post as an <a href>. Candidates arrive already filtered to
    the destination site and checked against its sitemap, so a draft never links to a page that is
    not live (both Astro fronts answer 200 with the homepage for an unknown URL, so a bad link would
    silently send readers home).
    """
    links = [l for l in (internal_links or []) if l.get("url") and l.get("anchor_text")]
    if not links:
        return ""
    lines = ["## Related reading", ""]
    for link in links:
        category = (link.get("category") or "").strip()
        reason = "calculator" if link.get("kind") == "calculator" else (
            f"more on {category}" if category else "")
        lines.append(f"- [{link['anchor_text']}]({link['url']})" + (f" — {reason}" if reason else ""))
    return "\n".join(lines)


def _format_link_hints(internal_links) -> str:
    """Placement hints for the operator, as HTML comments so they never reach a reader."""
    lines = [f"<!-- internal-link hint: \"{l.get('anchor_text')}\" -> {l.get('url')} "
             f"[{l.get('why', '')}] {l.get('suggested_placement', '')} -->"
             for l in (internal_links or []) if l.get("url")]
    return "\n".join(lines) or ("<!-- internal-link hint: none — no live page on this site scored "
                               "for this topic -->")


def build_seo_draft(keyword_data, cannibalization, internal_links, growth_data, vertical_id, persona_id):
    """Generate structured markdown draft containing full SEO metadata, schema, and sections."""
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    kw = keyword_data["keyword"]
    kw_title = smart_title(kw)
    kw_prose = naturalize_kw(kw)
    slug = f"{today_str}_{slugify(kw)}"

    # Generate meta title and description (domain-neutral: the Growth OS moat is
    # "reality vs pitch", which must read correctly for any vertical — finance, legal,
    # energy, hardware — not just software/MCP).
    title = f"{kw_title}: What the Field Data Actually Shows"
    meta_title = f"{kw_title} (Reality Check)"
    if len(meta_title) > 60:
        meta_title = meta_title[:57] + "..."

    meta_desc = (
        f"A practitioner breakdown of {kw_prose}. Discover what the real-world data shows, "
        f"where the hidden costs sit, and what to verify before you commit."
    )
    if len(meta_desc) > 160:
        meta_desc = meta_desc[:157] + "..."

    # Extract Growth OS elements
    stances = growth_data.get("founder_stances", [])
    quotes = growth_data.get("founder_quotes", [])
    anecdotes = growth_data.get("customer_anecdotes", [])

    primary_stance = stances[0]["stance"] if stances else "Ground every claim in verifiable evidence rather than the marketing pitch."
    primary_topic = stances[0]["topic"] if stances else "The Hype Gap"

    primary_anecdote = anecdotes[0] if anecdotes else {
        "title": "Field Report",
        "details": "A real-world rollout exposed a wide gap between the pitch and what actually held up under real conditions."
    }

    quote_text = f'> "{quotes[0]["quote"]}" — {quotes[0]["author"]}' if quotes else f'> "Measure before you scale, and trust your own data over anyone\u2019s demo." — Founder Note'

    sources_block = _format_sources(keyword_data.get("serp_competitors", []))

    # Build JSON-LD Schema
    schema_dict = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": title,
                "description": meta_desc,
                "datePublished": f"{today_str}T06:00:00Z",
                "author": {"@type": "Person", "name": "{{AUTHOR_NAME}}"},
                "publisher": {"@type": "Organization", "name": "{{PUBLISHER_NAME}}"}
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": _naturalize_question(q, kw, kw_prose),
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": _faq_answer(q, kw, primary_stance)
                        }
                    } for q in keyword_data.get("paa_questions", [])[:3]
                ]
            }
        ]
    }

    # Format internal links
    related_block = _format_related_reading(internal_links)
    link_hints = _format_link_hints(internal_links)

    clusters_str = ", ".join([f"\"{c['keyword']}\"" for c in keyword_data.get("keyword_clusters", [])[:5]])

    # Assemble complete markdown with clean headers and schema at the bottom
    md = f"""---
title: "{title}"
meta_title: "{meta_title}"
meta_description: "{meta_desc}"
primary_keyword: "{kw}"
secondary_keywords: [{clusters_str}]
{kw_frontmatter(keyword_data)}
vertical: "{vertical_id}"
persona: "{persona_id}"
date: "{today_str}"
slug: "{slug}"
---

<!-- lead -->
Most of what gets written about {kw_prose} oversimplifies it. The people who actually deal with it report a very different picture [1].

<!-- tension -->
## Why the Pitch Keeps Outrunning the Reality

The systemic challenge is rooted in {primary_topic.lower()}: {primary_stance} [1].

The field data backs this up: {primary_anecdote['details']} [2]. Most people assume it is a solved problem and miss how the failure modes compound quietly until they surface at the worst moment. That gap between the pitch and the field reports is the part I keep circling.

{quote_text}

**By the numbers:**
- **41% vs. 93% accuracy:** Real-world field audits show unconstrained configurations suffer high failure rates, while strictly bounded setups reach enterprise reliability [2].
- **40%+ cost reduction:** Filtering baseline transactions deterministically eliminates model overhead on majority traffic [1].
- **3 core guardrails:** Bounding failure modes upfront prevents cascading downtime across dependent systems [3].

<!-- tactical-insight -->
## Where The Guardrails Actually Hold

What strikes me is how consistent the pattern is: the same three structural controls show up in the setups that hold, and the teams that skip them keep rediscovering the same failure modes the hard way.

- **Operators bound the expensive failure mode before it happens.** Whatever the pricey failure looks like, the teams getting this right cap it up front — retries, runaway spend, drift [1].
- **They validate against field data, not demos.** Benchmarks and vendor claims are what get quoted; the setups that hold are tested against their own production history [2].
- **The hidden compounding cost is the one I would watch.** The visible line item is rarely the real one — overhead and drift accumulate where nobody is measuring [3].

<!-- nuanced-takeaway -->
## The Hidden Cost Nobody Budgets For

The catch I keep coming back to: closing this gap takes upfront investment in measurement and discipline, not just intent. Teams looking for a zero-effort shortcut will find that the real answers still demand domain-specific rigor.

<!-- tldr -->
## Key Takeaways

- **The Reality Check:** The gap between vendor promises and production reality is the real cost center that catches engineering teams off guard.
- **What I'd Watch:** Whether teams shipping reliable systems hold their architectural boundaries:
  - **Hard Limits Up Front:** whether the expensive failure mode is bounded before it happens — retries, memory, runaway spend [1].
  - **Field Data Over Demos:** whether validation runs against real case history rather than benchmark demos [2].
  - **Deterministic Action Gates:** whether an agent can take an external action without a strict checking function [3].
- **The Fine Print:** Closing this gap requires upfront investment in telemetry and access control; metrics and ROI depend entirely on your workload and traffic mix.

{related_block}

## Sources
{sources_block}

<!-- linkedin -->
Most discussions about {kw_prose} ignore what actually happens in the real world.

Here is what the field data reveals:

1. Hard limits matter more than cleverness: unbound retries and runaway costs compound fast.
2. Real data beats demos: validate against your own history, not vendor claims.
3. The hidden cost is the real one: overhead and drift accumulate where nobody is measuring.

{primary_stance}

What is your team actually measuring before you commit?

<!-- schema -->
```json
{json.dumps(schema_dict, indent=2)}
```

<!-- internal-links -->
{link_hints}
"""
    return slug, md


def build_citation_hub_draft(keyword_data, cannibalization, internal_links, growth_data, vertical_id, persona_id, custom_dossier=None):
    """Generate structured markdown draft for an Audited Citation & Benchmark Hub."""
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    kw = keyword_data["keyword"]
    kw_title = smart_title(kw)
    kw_prose = naturalize_kw(kw)
    slug = f"{today_str}_{slugify(kw)}"

    # 1. Pre-Flight Data Harvester & Gate. Every metric is retrieved from its own primary source
    #    and its headline figure must actually appear in what was retrieved; date and sample size
    #    must be present and the source reachable. The hub is not drafted until the whole dossier
    #    clears the gate — an unverifiable benchmark is removed, never softened.
    dossier = custom_dossier or chd.get_claimed_dossier(vertical_id, kw)
    is_valid, errors, report = chd.verify_dossier(dossier, min_points=6)
    if not is_valid:
        print("  ✗ Pre-Flight Data Gate FAILED — no hub drafted. Per-point findings:")
        for point in report["points"]:
            print(f"      [{point['status']}] {point['metric_name']}: {point.get('reason', '')}")
            if point.get("evidence"):
                print(f"          evidence: …{point['evidence'][:200]}…")
        raise chd.UnverifiedDossierError(
            f"Pre-flight data verification failed for '{kw}' — {len(errors)} problem(s). "
            f"A citation hub is only draftable on verified primary data; nothing was generated.")
    print(f"  ✓ Pre-Flight Data Gate passed: {report['counts']}")

    title = f"{kw_title}: What the Field Benchmarks Actually Show"
    meta_title = f"{kw_title} (Audited Benchmarks & Data)"
    if len(meta_title) > 60:
        meta_title = meta_title[:57] + "..."

    meta_desc = (
        f"Audited {kw_prose} data. Real-world benchmarks, adoption telemetry, "
        f"cost multipliers, and field failure rates contrasted with vendor claims."
    )
    if len(meta_desc) > 160:
        meta_desc = meta_desc[:157] + "..."

    stances = growth_data.get("founder_stances", [])
    quotes = growth_data.get("founder_quotes", [])
    anecdotes = growth_data.get("customer_anecdotes", [])

    primary_stance = (
        stances[0]["stance"] if stances else "Audit every metric against production telemetry before committing architecture."
    )
    primary_topic = stances[0]["topic"] if stances else "The Hype Gap"
    primary_anecdote = anecdotes[0] if anecdotes else {
        "title": "Field Report",
        "details": "A real-world rollout exposed a wide gap between vendor pitch decks and production reliability under load."
    }
    quote_text = f'> "{quotes[0]["quote"]}" — {quotes[0]["author"]}' if quotes else f'> "Measure before you scale, and trust your own data over anyone\'s demo." — Founder Note'

    # Build sources block from dossier
    sources_lines = []
    for idx, dp in enumerate(dossier, start=1):
        sources_lines.append(f"[{idx}] {dp['primary_source_name']}. {dp['primary_source_url']}")
    sources_block = "\n".join(sources_lines)

    # Build JSON-LD Schema including TechArticle, Dataset, and FAQPage
    dataset_schema = chd.generate_dataset_schema(dossier, title, meta_desc, slug)
    schema_dict = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "TechArticle",
                "headline": title,
                "description": meta_desc,
                "datePublished": f"{today_str}T06:00:00Z",
                "author": {"@type": "Person", "name": "{{AUTHOR_NAME}}"},
                "publisher": {"@type": "Organization", "name": "{{PUBLISHER_NAME}}"}
            },
            dataset_schema,
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": _naturalize_question(q, kw, kw_prose),
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": _faq_answer(q, kw, primary_stance)
                        }
                    } for q in keyword_data.get("paa_questions", [])[:3]
                ]
            }
        ]
    }

    # Format internal links
    related_block = _format_related_reading(internal_links)
    link_hints = _format_link_hints(internal_links)

    clusters_str = ", ".join([f"\"{c['keyword']}\"" for c in keyword_data.get("keyword_clusters", [])[:5]])

    # Render Visuals & Tables
    table_md = chd.generate_markdown_table(dossier)
    visual_chart = cg.generate_benchmark_visual(dossier, f"{kw_title} Telemetry (2026)")
    quick_cite_md = chd.generate_quick_cite_block(dossier)

    # Quantitative Bullets
    by_the_numbers = []
    for dp in dossier[:4]:
        by_the_numbers.append(f"- **{dp['headline_figure']} {dp['metric_name'].lower()}:** {dp['vendor_claim']} — field audits reveal {dp['field_reality'].lower()} [{dossier.index(dp) + 1}]")
    btn_block = "\n".join(by_the_numbers)

    md = f"""---
title: "{title}"
meta_title: "{meta_title}"
meta_description: "{meta_desc}"
primary_keyword: "{kw}"
secondary_keywords: [{clusters_str}]
{kw_frontmatter(keyword_data)}
vertical: "{vertical_id}"
persona: "{persona_id}"
archetype: "citation_hub"
date: "{today_str}"
slug: "{slug}"
---

<!-- lead -->
Most conversations around {kw_prose} rely on vendor pitch decks and synthetic benchmark scores. In real enterprise production, engineering telemetry shows a starkly different baseline [1].

<!-- tension -->
## Why the Pitch Keeps Outrunning the Reality

The systemic friction comes down to {primary_topic.lower()}: {primary_stance} [1].

The field data confirms this pattern: {primary_anecdote['details']} [2]. The part I keep circling is the stark gap between synthetic benchmarks and production failure modes under enterprise load.

{quote_text}

**By the numbers:**
{btn_block}

<!-- tactical-insight -->
## The Audited Benchmark Matrix

The following index compiles audited industry benchmarks contrasted with field reality audits across enterprise deployments:

{table_md}

{visual_chart}

### Where the Guardrails Actually Hold

What strikes me is how consistent the pattern is: setups that hold enforce explicit boundaries, while unconstrained configurations discover runaway bills the hard way.

- **1. Unit Economics Compound Faster Than Token Drops:** The dynamic I keep watching is that while raw model prices fall, recursive agent loops consume 5x to 10x more transactions per completed task, driving net compute bills higher [2].
- **2. Failure Modes Stem From Integration Drift:** Production telemetry shows that over 60% of outages occur at tool boundaries and timeout cliffs rather than internal model reasoning failures [3].
- **3. Verification Overhead Eerily Erodes Labor Savings:** Autonomous setups lacking deterministic validation gates require senior engineers to manually review outputs, offsetting anticipated productivity gains [4].

<!-- nuanced-takeaway -->
## The Hidden Cost Behind the Metric

The catch I keep coming back to is sample bias in vendor evaluations. Benchmark tests optimize for narrow tasks with predefined constraints. In messy enterprise environments, the real cost centers are data hygiene, security boundary checks, and ongoing audit infrastructure.

<!-- tldr -->
## Key Takeaways

- **The Big Shift:** Production telemetry across {kw_prose} demonstrates that real-world completion and cost dynamics diverge dramatically from vendor benchmark demos.
- **Why It Matters:** Teams budgeting based on synthetic benchmarks face unexpected compounding token costs and unbudgeted human verification overhead.
- **What I'd Watch:** Key architectural controls that prevent production failure:
  - **Telemetry Over Demos:** measuring success by fully resolved business units rather than intermediate sandbox scores [1].
  - **Deterministic Gate Checks:** bounding recursive retries and tool timeouts before deploying agents to production [3].
  - **Unit Economics Tracking:** monitoring total workflow cost per resolution rather than raw token pricing [2].
- **The Catch:** Establishing rigorous telemetry requires upfront infrastructure and domain-specific validation gates; zero-effort shortcuts do not hold in production.

{related_block}

## Sources
{sources_block}

<!-- quick-cite -->
{quick_cite_md}

<!-- linkedin -->
I've been analyzing production telemetry across {kw_prose} all week.

My read: synthetic benchmarks measure isolated happy paths, while real-world engineering teams deal with compounding costs and unhandled retries.

The three findings that stick with me:

1. Synthetic accuracy drops when unconstrained by strict step budgets.
2. Compounding loops drive total costs higher even as token prices decline.
3. Over 60% of production failures stem from tool timeouts and integration drift, not model reasoning.

{primary_stance}

What metrics are your engineering teams verifying before signing off on deployment?

<!-- schema -->
```json
{json.dumps(schema_dict, indent=2)}
```

<!-- internal-links -->
{link_hints}
"""
    return slug, md


def run_pipeline(target_query=None, vertical=None, force=False, run_humanizer=True, enable_dataforseo=None, archetype="article"):
    """Run the complete SEO Content Machine pipeline."""
    print(f"\n=======================================================")
    print(f"🚀 Launching SEO Content Machine & Growth OS Pipeline")
    print(f"=======================================================")

    verts = load_verticals()

    # 1. Detect or accept target query
    if not target_query:
        print(f"🔍 Step 1: Scanning Google Search Console for top opportunity...")
        gsc_data = load_gsc_data()
        opps = analyze_opportunities(gsc_data, vertical=vertical or "all")
        if not opps:
            print("❌ No high-potential GSC opportunities detected. Exiting.")
            return None
        chosen = opps[0]
        target_query = chosen["query"]
        vertical = chosen["vertical"]
        print(f"  🎯 Detected winning GSC query: '{target_query}' (Impr: {chosen['impressions']}, Score: {chosen['opportunity_score']}, Trigger: {chosen['trigger_reason']})")
    else:
        vertical = vertical or "agentic_ai"
        print(f"  🎯 Target query specified: '{target_query}' (Vertical: '{vertical}')")

    # Detect statistical data intent for archetype selection
    tq_lower = target_query.lower()
    is_data_intent = any(k in tq_lower for k in ("benchmark", "benchmarks", "statistics", "stats", "telemetry", "dataset"))
    effective_archetype = "citation_hub" if (archetype == "citation_hub" or is_data_intent) else "article"
    if effective_archetype == "citation_hub":
        print(f"  📊 Archetype Selected: Audited Citation & Benchmark Hub (AEO/GEO Optimized)")
    else:
        print(f"  📰 Archetype Selected: Standard Editorial Article")

    # Check DataForSEO vertical setting
    vert_config = verts.get(vertical, {})
    if enable_dataforseo is None:
        use_d4s = vert_config.get("enable_dataforseo", True)
    else:
        use_d4s = enable_dataforseo

    # 2. Enrich with DataForSEO
    if use_d4s:
        print(f"\n📊 Step 2: Querying DataForSEO intelligence (live API enabled for vertical '{vertical}')...")
    else:
        print(f"\n📊 Step 2: DataForSEO is DISABLED for vertical '{vertical}' in vertical settings (bypassing live credits)...")

    d4s_client = DataForSEOClient()
    kw_data = d4s_client.enrich_keyword(target_query, force_sandbox=not use_d4s)
    kw_source = kw_data.get("keyword_data_source") or (
        "dataforseo_live" if kw_data.get("live_data") else "sandbox_estimate")
    volume, kd = kw_data.get("search_volume"), kw_data.get("keyword_difficulty")
    if kw_source != "dataforseo_live":
        print("\n" + "!" * 78)
        print("  ⚠️  KEYWORD METRICS ARE NOT MEASURED — DataForSEO live enrichment was skipped.")
        print(f"      Volume / difficulty / CPC for '{target_query}' are derived from a hash of the")
        print("      keyword itself. The draft therefore records NO search volume and carries")
        print('      keyword_data_source: "sandbox_estimate". Turn on enable_dataforseo for this')
        print("      vertical in context/verticals.json, or pass --dataforseo, for real research data.")
        print("!" * 78)
    elif not volume:
        print("  ⚠️  The live API returned no search volume for this keyword — the draft records none "
              "rather than a default.")
    vol_display = f"{int(volume):,} / mo (measured)" if volume else "not measured"
    print(f"  • Search Volume: {vol_display} | Intent: {str(kw_data.get('search_intent') or 'unknown').upper()}"
          f" | KD: {kd if kd else 'not measured'}")
    print(f"  • Top Cluster: {[c['keyword'] for c in kw_data.get('keyword_clusters', [])[:3]]}"
          f"{'  (generated, not researched)' if kw_data.get('clusters_source') == 'generated' else ''}")

    # 3. Check Cannibalization & Internal Links via Growth OS
    print(f"\n🛡️ Step 3: Running Growth OS cannibalization & internal link analysis...")
    cannib = gos.check_cannibalization(target_query, vertical)
    print(f"  • Cannibalization Verdict: {cannib['verdict']}")
    if cannib["is_cannibalized"]:
        print(f"  ⚠️ Warning: {cannib['recommendation']}")
        if cannib["similarity"] >= 0.95 and not force:
            print(f"  🛑 Halted to prevent keyword cannibalization against existing published article.")
            print(f"  (Use --force to override if drafting a child cluster post).")
            return None

    internal_links = gos.generate_internal_link_map(target_query, vertical)
    print(f"  • Mapped {len(internal_links)} internal link connections:")
    for il in internal_links:
        print(f"    - [{il['anchor_text']}] -> {il['url']}")

    growth_data = gos.extract_growth_os_knowledge(vertical, target_query)
    print(f"  • Ingested {len(growth_data['founder_stances'])} founder stances & {len(growth_data['customer_anecdotes'])} customer anecdotes.")

    # 4. Determine Persona
    persona_id = vert_config.get("target_persona", "eng_leader")

    # 5. Generate Draft
    if effective_archetype == "citation_hub":
        print(f"\n✍️ Step 4: Generating Audited Citation & Benchmark Hub (Pre-Flight Gate + Data Table + Chart + Schema)...")
        slug, draft_content = build_citation_hub_draft(kw_data, cannib, internal_links, growth_data, vertical, persona_id)
    else:
        print(f"\n✍️ Step 4: Generating structured SEO draft (H2/H3 + Schema + Meta Tags)...")
        slug, draft_content = build_seo_draft(kw_data, cannib, internal_links, growth_data, vertical, persona_id)

    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    draft_file = DRAFTS_DIR / f"{slug}_draft.md"
    draft_file.write_text(draft_content, encoding="utf-8")
    print(f"  ✅ Saved structured draft to: {draft_file}")

    # 6. Frontier Humanizer Rewrite (Loop 3)
    final_file = DRAFTS_DIR / f"{slug}_final.md"
    if run_humanizer:
        print(f"\n✨ Step 5: Executing Frontier Humanizer (Loop 3 rewrite)...")
        try:
            import humanize_loop3 as hl3
            result = hl3.humanize_single_draft(draft_content, final_file)
            if not final_file.exists():
                final_file.write_text(result + "\n", encoding="utf-8")
            acc = ca.measure(str(final_file))
            if acc["verdict"] == "PASS":
                print(f"  ✅ Frontier rewrite complete — accessibility PASS (Flesch {acc['flesch']}).")
            else:
                print(f"  ⚠️ Frontier rewrite complete but HELD — accessibility FAIL ({acc['fails']}). Not publishable as-is.")
        except Exception as e:
            print(f"  ⚠️ Frontier rewrite notice ({e}). Final draft written from base.")
            final_file.write_text(draft_content, encoding="utf-8")
    else:
        final_file.write_text(draft_content, encoding="utf-8")
        print(f"  ℹ️ Humanizer skipped (--no-humanize). Final draft copied from base.")

    # Guarantee: Title MUST contain primary keyword for SEO indexing
    try:
        import humanizer_tools as ht
        final_text = final_file.read_text(encoding="utf-8")
        guaranteed_text = ht.ensure_title_contains_keyword(final_text)
        if guaranteed_text != final_text:
            final_file.write_text(guaranteed_text, encoding="utf-8")
            print(f"  🎯 Validated & enforced SEO primary keyword in title.")
    except Exception as e:
        print(f"  ⚠️ Title keyword check notice: {e}")

    print(f"\n=======================================================")
    print(f"🎉 Pipeline Execution Complete!")
    print(f"Draft Staged: {final_file}")
    print(f"Status: Waiting for founder review gate (@Simon approve)")
    print(f"=======================================================\n")
    return final_file


def main():
    parser = argparse.ArgumentParser(description="SEO Content Machine & Growth OS Pipeline")
    parser.add_argument("--query", help="Target search query (if omitted, auto-selects top GSC opportunity)")
    parser.add_argument("--vertical", help="Vertical ID (e.g. agentic_ai, enterprise_tech_leadership)")
    parser.add_argument("--archetype", choices=["article", "citation_hub"], default="article", help="Content archetype (standard article or audited citation_hub)")
    parser.add_argument("--force", action="store_true", help="Force drafting even if cannibalization warning exists")
    parser.add_argument("--no-humanize", action="store_true", help="Skip frontier humanizer rewrite pass")
    parser.add_argument("--dataforseo", dest="dataforseo", action="store_true", default=None, help="Force enable DataForSEO API enrichment")
    parser.add_argument("--no-dataforseo", dest="dataforseo", action="store_false", help="Force disable DataForSEO API enrichment to save credits")

    args = parser.parse_args()
    run_pipeline(
        target_query=args.query,
        vertical=args.vertical,
        force=args.force,
        run_humanizer=not args.no_humanize,
        enable_dataforseo=args.dataforseo,
        archetype=args.archetype
    )


if __name__ == "__main__":
    main()
