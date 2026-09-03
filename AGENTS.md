# editorial-factory — Agent Operating Constitution

This repository is the shared brain of the **Autonomous Content Intelligence & Editorial
Engine**: a Hermes-native multi-agent assembly line that discovers acute 30-day signals across
chosen verticals, scores them for virality, verifies every claim against primary sources, and
produces trustworthy, human-voice articles — with the final rewrite always executed by a
frontier model (Claude).

It deliberately mirrors the architecture of `kotechile/factory` (the software factory): the
"agentic workforce" is a Hermes bot fleet, the "loops" are skills + cron jobs + hard quality
gates, and every non-deterministic step is gated on retrievable evidence.

## What this engine is NOT
- It does **not** generate software, PRDs, or micro-SaaS. Articles only.
- It does **not** publish fabricated statistics. Every number, quote, and benchmark traces to a
  retrievable primary source or is removed.

## Directory map
- `.agents/`     — persona & role contracts (canonical; mirrored into each Bot's SOUL.md)
- `skills/`      — Standard Operating Procedures (SOPs). Canonical source of truth.
- `context/`     — shared long-term memory (verticals, voice personas, calendar, published log)
- `scripts/`     — cron triggers + verification gates
- `site/`        — minimal static reader for published articles (Coolify-deployable)
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
8. **Approval-gated auto-publish.** Articles are drafted and verified autonomously, but publishing
   to LinkedIn/Ghost requires the founder's `@Simon approve` gate (a hard gate). Approved articles
   are written to `published/` and `context/published_log.md`, then posted by the Publisher.

## Runtime model note
The fleet's non-frontier roles run on the configured provider (currently `deepseek-v4-pro`).
The **Claude Stylist & Critic** role is pinned to a frontier Anthropic model served through
**kie.ai** (`https://api.kie.ai/claude`, model `Claude-Opus-4-8`), which requires
`ANTHROPIC_API_KEY=Bearer <kie.ai key>` plus a `model.base_url` override on the stylist profile.
Without it, the pipeline halts at the frontier gate rather than substituting a non-frontier model.
