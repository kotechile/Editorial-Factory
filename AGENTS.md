# editorial-factory — Agent Operating Constitution

This repository is the shared brain of the **Autonomous Content Intelligence & Editorial
Engine**: a dual-engine Hermes-native multi-agent assembly line that turns acute 30-day industry signals
AND search demand data (Google Search Console + DataForSEO) into **trustworthy, human-voice articles** —
grounded in proprietary founder taste (`founder-voice.md`) and real field data (`customer-truth.md`),
with the final rewrite always executed by a frontier model (Claude / Gemini).

It deliberately mirrors the architecture of `kotechile/factory` (the software factory): the
"agentic workforce" is a Hermes bot fleet, the "loops" are skills + cron jobs + hard quality
gates, and every non-deterministic step is gated on retrievable evidence.

## What this engine is NOT
- It does **not** generate software, PRDs, or micro-SaaS. Articles only.
- It does **not** publish fabricated statistics. Every number, quote, and benchmark traces to a
  retrievable primary source or is removed.
- It does **not** generate generic commoditized SEO fluff. Every piece is injected with contrarian
  founder moat and audited against keyword cannibalization.

## Directory map
- `.agents/`     — persona & role contracts (canonical; mirrored into each Bot's SOUL.md)
- `skills/`      — Standard Operating Procedures (SOPs). Canonical source of truth.
- `context/`     — shared memory (verticals, personas, calendar, published log, sitemap, GSC metrics)
- `context/assets/` — staged featured images + their briefs (`featured.json`). The binaries are not
  committed (the CMS media library is their canonical home); the briefs are — they are the
  provenance record and what the next article's art director reads.
- `context/growth_os/` — founder-voice.md, customer-truth.md, performance_learnings.md
- `scripts/`     — cron triggers, GSC/DataForSEO analyzers, growth_os engine, verify gates
- `site/`        — PressFlow editorial reader & SEO command center (Coolify-deployable)
- `published/`   — final approved articles (markdown) rendered by the site

## Non-negotiable editorial rules
1. **30-day freshness.** Every scout sweep is anchored to the last 30 calendar days. Older
   signals are dropped, not softened.
2. **Virality gate.** A topic must score ≥ 8/10 (Novelty × Authority × Shareability) to proceed.
   No padding to hit quota — a weak day yields "no publish", never a weak article.
3. **Zero-hallucination.** Every claim is extracted, then validated against a primary source.
   Unverifiable claims are flagged or removed, never paraphrased into plausibility.
4. **Frontier final rewrite.** The last rewrite pass is Claude (frontier). A draft that has not
   passed the Claude human-voice gate is not publishable.
5. **Human voice, no AI-tells.** No empty intros ("In today's fast-paced world"), no hollow
   transitions ("Furthermore", "delve into", "it's important to remember"). Lead with a concrete
   incident or figure; end with a pragmatic takeaway.
6. **No silent fallbacks.** A failed search, a missing API key, or an unverifiable claim surfaces
   an explicit error — never a degraded substitute.
7. **Self-healing SOPs.** Every failed run must patch a `skills/*.md` file so the failure class
   never recurs.
8. **Persistence is automatic and ungated; there is no social distribution step.** A verified,
   frontier-rewritten article is persisted in the same run — `published/YYYY-MM-DD_<slug>.md`,
   `context/published_log.md`, the Supabase rows, `context/sitemap.json`, the CMS post
   (`scripts/wp_draft.py`, sent with status 'publish') and the `context/content_calendar.md` run-log row — via
   `scripts/publish.py <final draft>`. **The reader sites are the destination** (`giniloh.com` /
   `wellroost.com`, fed by the CMS); the LinkedIn and Reddit channels were removed by the owner on
   2026-10-06, so no run produces social copy, queues a post or waits on a distribution approval.
   The article is pushed directly live to the CMS with status 'publish'.
9. **Multi-topic signal synthesis.** Rather than merely publishing single-signal press summaries,
   the pipeline prioritizes dialectical cross-topic synthesis: combining two or more acute 30-day
   developments (e.g., falling LLM frontier pricing colliding with local in-house software
   development) into an emergent, high-conviction thesis neither individual source could state on
   its own. The pairs are proposed and scored by the **Judge** (`skills/virality_judge.md` §2.5)
   and may be seeded by `scripts/synthesize_topics.py`, a mechanical, advisory pre-filter that
   cannot score or clear the ≥ 8 gate. Grounding requires primary verified data for **each** leg
   (the dual-anchor gate in `skills/fact_check.md` §5): if either leg fails verification, the
   synthesis is under-sourced and returns to the Judge.
10. **Audited Citation & Benchmark Hubs (AEO & Passive Backlink Pillars).** Rather than solely
    publishing acute 30-day news commentary, the pipeline supports data-dense benchmark assets
    (`skills/citation_hub.md`) targeting statistical search demand (`[topic] benchmarks`,
    `[topic] statistics`). These assets act as evergreen pillar anchors that attract passive citations
    from journalists and LLMs (Perplexity, SearchGPT, Claude). To avoid commoditized AI scrapers,
    every hub enforces a strict **Pre-Flight Data Gate** (verifying primary source URL, sample size,
    and methodology before a single word is drafted) and injects a contrarian reality audit
    grounded in `customer-truth.md` and `founder-voice.md`.
11. **Art-directed featured images.** Every article is illustrated in the same pass that persists it
    (`scripts/illustration_creator.py`, `skills/illustration_director.md`): a frontier art director
    reads the artifact's own text, picks a treatment from the catalogue — macro, cinematic still,
    clay 3D render, technical isometric, modular component assembly, paper collage, … — and generates
    one 16:9 header on kie.ai (Flux-2 Pro for the physical and photographic, Nano Banana Pro for the
    constructed), with the alt text, caption and credit the CMS needs. The treatment is a decision
    per article, never a preset: it must differ from the last four illustrations, it must quote a
    verbatim cue from the article it was read from, and no image may contain legible text, a real
    brand's mark or a stock-photo cliché. **A shape is not a subject**: an abstract story has to be
    carried by a named physical mechanism (a modular bay, an unlatched inspection gate, a rack of
    blades), and a prompt whose subject is bare geometry is refused in code — the desk's own first
    ten headers included two agentic-AI articles illustrated as a rectangle with a colour band and a
    block resting on a wedge. Idempotent by the article's own digest, so a re-run never re-spends
    image credits on an unchanged text.
12. **Internal links are generated from the live corpus, never invented.** The `<!-- internal-links
    -->` block is filled in the persistence pass (`scripts/internal_links.py`, hooked into
    `scripts/publish.py` and `scripts/wp_draft.py`) from `context/internal_links.json` — the pages
    that actually EXIST per CMS and RESOLVE per each frontend's sitemap. The drafting stage cannot do
    this: it has no list of live pages, so every artifact it wrote carried an empty block and every
    CMS draft reached a reader with zero internal links while the hand-written back catalogue carried
    2–10 each. A link must be on the destination's own site (a cross-site link is not an internal
    one), live, never the article itself, and justified by the destination's own category hub or by
    at least two shared subject tokens — one incidental word (`just`, `billion`, `into`) is not
    evidence, and when nothing qualifies the section is absent and the gap is stated rather than
    filled with an unrelated page. Idempotent, and the enriched body is written back to the Supabase
    row so the database and the CMS can never disagree.

13. **A second pipeline for the topics the news gate must refuse.** The 30-day radar is gated on
    freshness (Novelty carries 0.40), so it correctly returns "no publish" for a durable topic —
    which is why verticals whose beat is periodic (statute books, survey cycles, procurement) ran
    empty week after week while the runs logged *"undated evergreen; not anchored to window"*. A
    vertical therefore carries two independent schedules, reconciled from the same registry: the
    news run, and an **evergreen** run (`skills/evergreen_topics.md`) that publishes one useful,
    durable article. The news gate does not run there — that is the point — so the evergreen floor
    is **code, not prose** (`scripts/evergreen_gate.py`): ≥ 3 cited primary sources on ≥ 2 hosts,
    every one fetched and shown to contain the figure it is cited for, a named persona decision, a
    de-dup check against the last 180 days that names an artifact which exists, and an `as of` date
    on any time-bound figure. Both modes are per-vertical settings (`news_enabled` /
    `evergreen_cadence` / `evergreen_enabled`): a mode switched off has its cron job removed by
    `scripts/sync_crons.py`, never left half-configured. A topic whose value expires inside ~90 days
    is news — route it back to Radar.

## Runtime model note
The fleet's non-frontier roles run on the configured provider (currently `deepseek-v4-pro`).
The **Claude Stylist & Critic** role is pinned to a frontier Anthropic model served through
**kie.ai** (`https://api.kie.ai/claude`, model `claude-sonnet-5`), which requires
`ANTHROPIC_API_KEY=Bearer <kie key>` plus a `model.base_url` override on the stylist profile.
Without it, the pipeline halts at the frontier gate rather than substituting a non-frontier model.

The **Art Director** (`scripts/illustration_creator.py`) runs on `gemini-3.1-pro-preview` via
`GOOGLE_API_KEY` (the Loop 3 key) and generates through the same kie.ai gateway with `KIE_API_KEY`
(two image models: `flux-2/pro-text-to-image`, `nano-banana-pro`). A missing key is an explicit
error, never a placeholder image.
