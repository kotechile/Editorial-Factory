# Run log — nhil_infrastructure_ops, 2026-11-17 (news)

**Slot:** registry cadence `0 11 * * 2` (Tue 11:00 UTC). **Mode:** news. **Gate:** `generation_gate.py --mode news --vertical nhil_infrastructure_ops` → GENERATION OK (control=supabase, vertical=file), exit 0.
**Window:** 2026-10-18 → 2026-11-17. **Persona:** `it_ops_leader`. **Surface:** aichieve.net.

## 1. Scout (radar_30day)

17 web fan-outs across the vertical's six configured sources and six primary angles, 2 arXiv API queries (id_list + cs.NI date-bounded), 7 primary pages fetched and read in full. Three promising legs were **dropped on freshness** after reading their own publication dates, not their search snippets:

| candidate | own date | ruling |
|---|---|---|
| Cisco/Omdia *The Impact of Agentic AI on Network Operations* | 2026-09-23 (Cisco newsroom) | out of window by 25 days; the HBR sponsored piece (2026-11-11) and TechTarget's "released last month" are write-ups of it → dated background |
| OCP Mt. Diablo Disaggregated Power Rack Spec v1.0.0 | "Effective October 8th, 2026" | 10 days before the window → dated background |
| OCP Global Summit 800 VDC sidecar | 2026-10-12 → 15 | closed 3 days before the window → dated background |
| PJM BRAs ($333.44 for 27/28, $325.00 for 28/29) | Dec 2025 / Jul 2026 | auctions out of window |
| FERC RM26-4 large-load docket | June 2026 proceedings | no in-window action found |

5 in-window rows kept (4 event-dated, 1 arXiv submission date), intensities 70–95. Two rows share the BBC URL by design (scale vs. the BSI counter-example); the dual anchors are Reuters/Irish Examiner and arXiv.

## 2. Seed step

`synthesize_topics.py --seed` → **rows=5 candidates=0**. Recorded as input, not a verdict: the collision is on a *measurement* (a check reporting on a path the service has left), which the token layer has no archetype for. Re-run after the signals header was corrected to the true query count, so `verify.sh` §8 reads a fresh marker.

## 3. Judge (virality_judge §2.5)

**Winner: Synthesis — "Your Check Sees 0.086ms, Not 40"**, E=9 A=9 S=9 → **9.0**.
- Leg A: Microsoft's own account of the 2026-11-12/13 Exchange Online outage — "an issue during an earlier network capacity upgrade that surfaced following a recent network change", with the recovery certified by "validating stability at each stage" (Reuters via Irish Examiner, 2026-11-13); BBC: at least 74 countries.
- Leg B: arXiv 2611.00838 (2026-10-31) — a witness reporting 0.086 ms while the service runs at 40.139 ms against a 25 ms objective; 107 of 197 goal-matched agent plans blocked, 30 repaired, 0 of 270 revisions passing.
- Emergent collision: both are failures of the **evidence surface**, not of the change or the model; neither source states the fusion.
- Precedence: 9.0 vs the best single signal (the outage alone, 8.7) — margin 0.3, at the rule's threshold. Runner-ups scored and refused in the brief (paper alone 8.4; Cisco/Omdia, Mt. Diablo, PJM, FERC all refused on freshness).
- §3.5 de-dup: this vertical's last 30 days argue a certificate-renewal cadence (2026-11-10), a 1N power path (2026-11-03) and a backup-generation permit (2026-11-03) — none touches telemetry binding or an outage. Sibling check across the 18 verticals on aichieve.net: `ai_observability_qa` published today on agent tool-fault interventions (warn vs withhold); that thesis is an error-rate gate, this one is evidence validity, and no figure is shared.

## 4. Fact check (fact_check)

14 rows — **12 VERIFIED, 2 FLAGGED, 0 REMOVED**. Dual-anchor gate PASS (leg A 5 verified, leg B 6 verified). The two FLAGGED rows (restored servers going unresponsive; the secure-connection process as bottleneck) come from one Greek outlet relaying Microsoft service-health wording via The Guardian; they are used as reported developments, never as Microsoft quotations, and no figure rests on them. Rulings carried into the draft: the 74-country count is the BBC's tally of Downdetector data, not a Microsoft statement; the October Azure Front Door outage is a different event and must not be merged; the paper's own limitation (deliberately constructed 15-plan set, eight-node testbed, intents not topologies) must survive.

## 5. Draft and frontier pass

Draft 1,012 words, Flesch 54.1, `readability_critic` ok, `check_accessibility` PASS after pre-tuning (At-a-glance label and length, one metric per bullet, a two-tag sentence split, KTH removed as an undefined acronym, figure-load and a 7-sentence paragraph fixed).
`article_reviewer.py` (deepseek-v4-pro, `run_pipeline.py review`): **attempt 1 ACCEPT** — hard=0, regressions=0, rhythm sd 7.9→8.1, health 0.901→0.862, Flesch 54.5, 1,003 words.

**Hand repair after the rewrite:** the frontier pass unwrapped the earned inline internal link (`/sla-credit-is-not-insurance/`) into plain text, which `article_shape` holds. Restored as a markdown link; `run_pipeline.py gate` then passed all eight checks (accessibility, shape, critic, headline, sources, review_audit, voice, publish_gate).

## 6. Persistence

`scripts/publish.py context/drafts/2026-11-17_your-check-sees-0086ms-not-40_final.md` → `published/2026-11-17_your-check-sees-0086ms-not-40.md`, published log, sitemap, Supabase row `824e7d0f-2a0e-4c81-9992-33c6f0967392`, WordPress post **1734** on cms.giniloh.com (status publish, category 7 "AI Stack & Tool TCO", vertical term 38, kind tag 43 = **news**, featured media 1736, 7,856-char body).

Featured image: `technical_isometric` on nano-banana-pro (in-run art director), an isometric cutaway of a rack where a tap probe stays clamped to an old route while a fresh patch cord carries the live path.

## 7. Defects found and fixed in-run

1. **The composite clipped its own hook.** The auto placement put a three-line title plus a two-line hook in the lower-right, and the hook's second line ran off the bottom edge; a vision read caught it. Re-composited with `illustration_overlay.py --anchor top-right` (contrast 6.13 against a 5.5 target, kicker/title/hook all inside the frame).
2. **The overlay's alt text was the headline glued to a truncated clause** (141 characters, cut at "…on a"). Rewritten to a 134-character sentence describing the pixels and reconciled across `featured.json`, the final artifact, the published artifact, media 1736 and the Supabase row's `metadata.illustration.alt_text` / `metadata.wordpress.media_alt`.
3. **The front served the wrong hero.** After the re-image, the built page still pointed at the deleted attachment's filename, which 301'd off-host and resolved to an unrelated robot-mower illustration from another property. Two further status toggles forced the rebuild; the live page now serves bytes hash-equal to the staged file (sha256 `1dd07c30…`, 401,321 B) with the corrected alt.
4. **`wp_draft --reimage` still reports "featured_media NOT yet switched"** although the read-back showed 1736 — the documented false alarm; verified by REST rather than by the message.

## 8. Reader surface

https://aichieve.net/your-check-sees-0086ms-not-40/ — **HTTP 200**, own `<h1>` ("Your Check Sees 0.086ms, Not 40"), hero on the new media URL with the corrected alt, `## Sources` as a list, the earned inline link to `/sla-credit-is-not-insurance/`, and a generated Related-reading block.

**Open item, reported not fixed:** the generated Related-reading block qualified three links on the single incidental tokens "check" and "spent" (`/duet-bills-your-five-hour-window/`, `/your-5-gate-breaks-at-261/`, `/your-chargeback-misses-40-of-the-bill/`) — the AGENTS.md rule-12 one-token defect in `internal_links.py`, unchanged by this run. No social distribution and no LinkedIn/Reddit copy (channels removed 2026-10-06).
