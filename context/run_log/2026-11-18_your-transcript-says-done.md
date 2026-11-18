# Run log — 2026-11-18 · agentic_resilience_failure (news)

**Window:** 2026-10-19 → 2026-11-18 · **Mode:** news (`30 10 * * 3`) · **Persona:** infra_engineer · **Surface:** aichieve.net
**Artifact:** `2026-11-18_your-transcript-says-done`

## 1. Radar

31 queries: 16 arXiv API sweeps sorted by submission date (LLM-agent failure, agentic fault, checkpoint, rollback,
context poisoning, recovery, incident, multi-agent reliability, verification, idempotent, retry, cascading failure,
silent failure, drift, orchestrator failover, human oversight), 12 Hacker News Algolia `search_by_date` pulls
bounded at epoch floor 2026-10-19 with points ≥ 6, 3 web searches on the incident/postmortem beat.
300 in-window arXiv hits; 80 titles matched resilience keywords; 8 arXiv HTML bodies fetched in full plus two
first-party pages (Epoch AI incident report, Eon 33-case corpus). 7 rows kept at Intensity 64–88.

## 2. The de-dup that decided the run

The strongest pair in the sweep — arXiv:2611.19886 (risky fallback) ⨂ arXiv:2611.20595 (SilentGuard), with
2611.20711 (AgentFaultBench) as a third leg — was **published yesterday** as
`ai_observability_qa`'s `2026-11-17_your-warning-leaves-701-wrong` on the same `aichieve.net` front.
`skills/virality_judge.md` §3.5's sibling rule caught it at the anchor level: all three papers are excluded from
this run and carried in the signals file's `## Dated background`. The fallback would have been the second
article on one experiment, one day later, in front of one reader.

What survived was a pair neither paper in that piece touches: 2611.14654 (history edits vs the world) and
2611.11581 (error placement at fixed content). Seeded block: `rows=7 candidates=0` — the documented
measurement-axis blind spot of `synthesize_topics.py`; recorded as input, not verdict.

## 3. Judge

Synthesis, E=8.8 A=9.0 S=8.7 → **8.8**. Best single-signal candidate (2611.14654 alone) 8.4 → margin 0.4, above
the §2.5 requirement. Runner-ups scored and answered in the brief: the API-translation pair (8.2, both legs
"the record is wrong", no tension), Airlock containment (8.0, beat already occupied on this front), the Eon
corpus alone (7.6, convenience sample), the Epoch incident (7.4), more-agents reliability (7.5, partial retread),
Reversibility Classes (7.2, retread of this vertical's 2026-11-04 undo piece).
Nearest corpus neighbour named in the brief and deliberately not re-argued:
`agentic_ai` 2026-10-29 `your-compaction-trap-87-forgeries-survive` (compaction **destroys provenance**); this
piece is about the **sign of an edit on decision quality**, not who is speaking.

## 4. Fact check

Dual-anchor gate PASS: Leg A 4/4 VERIFIED, Leg B 3/3 VERIFIED, plus one corroborating leg (Eon) and three
FLAGGED rows carried into the brief — the +15.20 pp table figure vs the appendix's +15.65 pp independent
estimate (quote the table only), the two-receiver scope of the 27-point interaction, and the limits of B's
delivery gain (explicit errors only).

## 5. Draft → frontier

Draft 1,020 words, Flesch 50.4 → 57.1 after a word-choice pass (no sentence-splitting for score), headline
`Your Transcript Says Done: Success Fails at 28%` scored **100/100** with `lead_ok`. First title attempt
("45% to 28%") scored 81 — no hook token — and was re-cut.
`article_reviewer.py`: attempt 1 rejected on one structural defect (regressions=1), attempt 2 **ACCEPT**,
hard=0, rhythm 9.5, Flesch 57.9, 1,030 words.

## 6. Gates

`run_pipeline.py gate` **8/8**: accessibility, shape, critic, headline, sources, review_audit, voice, publish_gate.

## 7. Persistence and the three defects repaired in-run

- `scripts/publish.py` wrote `published/`, the published log, Supabase row `2315ce97-10ea-4821-bc1c-14a556c76e83`,
  the sitemap and WordPress post **1761** (publish; category 9, vertical term 15, kind tag 43 `news`).
- **Defect 1 — the frontier stripped the inline internal link.** `article_shape` red-lit the final
  ("no inline internal link"): the rewrite had flattened
  `[durable execution leaves open](/durable-execution-not-a-transaction/)` to plain text. Re-linked by hand
  before the gate; both candidate targets were probed 200 first.
- **Defect 2 — the push shipped hero-less** (`featured_media: 0`, no illustration directory), the third time in
  three runs. The art director then refused three briefs in a row on the bare-geometry validator. Repaired with
  a pinned treatment: `illustration_creator.py published/… --apply --style architectural_night --model flux` →
  `architectural_night` on `flux-2/pro-text-to-image`, 2400×1350, 5 credits (a dusk exterior, one dark unlit
  data-hall wing beside a warm lit rack row — the same building in two states) → media **1763** attached by
  `wp_draft.py --slug … --reimage`.
- **Defect 3 — the hero did not reach the front.** The post was live with `featured_media: 1763` but
  `aichieve.net` served 404, then 200 with the default share image and no `<img>`. A status toggle
  (draft → publish) fired the front rebuild; the page then carried the featured hero and the correct `og:image`.
- **Defect 4 — alt text was overlay copy plus a truncated clause** (136 chars, "…claimed completion"). Replaced
  with one sentence describing the pixels (79 chars) and reconciled across the sidecar, the draft, the final, the
  published artifact, media 1763 and the Supabase row's `metadata.illustration.alt_text` /
  `metadata.wordpress.media_alt`.

## 8. Verification

- Front `https://aichieve.net/your-transcript-says-done/` **200**, hero present, `og:image` =
  `…/uploads/2026/11/your-transcript-says-done-featured.jpg`, 4 internal links (3 generated + 1 inline).
- CMS REST read-back: post 1761 `status: publish`, `featured_media: 1763`; media 1763 serves the exact bytes
  uploaded and carries the corrected alt.
- `verify.sh`: this run's three artifacts PASS accessibility; the 119 FAIL lines it reports are Sep–Oct
  grandfathers from other verticals (owner standard: never bulk retro-fix).

## 9. Lessons recorded

`scripts/learn.py` (kind `pitfall`):
1. A news sweep's strongest pair can be spent by a sibling vertical **the day before** — check `published_log.md`
   for the last 7 days across every vertical on the same front, at the *anchor* level, before scoring.
2. The frontier rewrite strips inline internal links; re-link the `_final.md` before `gate`, never after.
3. `illustration_creator.py` refuses bare-geometry briefs three times running; pin `--style` and `--model` rather
   than re-rolling the art director.
