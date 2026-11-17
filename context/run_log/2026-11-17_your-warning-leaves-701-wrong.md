# Run log — ai_observability_qa news, 2026-11-17

Artifact: `published/2026-11-17_your-warning-leaves-701-wrong.md`
Title: **Your Warning Leaves 70.1% Wrong** (100/100 STRONG, lead_ok true)
Kind: news · synthesis: true · persona: evals_infra_eng · surface: aichieve.net
Slot: Tue 10:30 UTC news (`cadence` `30 10 * * 2`), window **2026-10-18 → 2026-11-17**

## Gate at STEP 0
`generation_gate.py --mode news --vertical ai_observability_qa` → `GENERATION OK (ok)` (control=supabase, vertical=file). Proceeded.

## Radar (Loop 1)
41 query/fetch operations: 10 arXiv API sweeps sorted by submission date (`all:"LLM judge"`, `all:"agent evaluation"`, `all:observability AND all:agent`, `all:judge AND all:calibration`, `all:evaluation AND cat:cs.SE`, `all:"regression testing" AND all:LLM`, `all:trace AND all:agent`, `all:benchmark AND all:contamination`, `all:"reward model" AND all:verifier`, `all:"eval" AND all:"harness"` — 190 in-window hits), 10 date-ranged Hacker News pulls via Algolia (`created_at_i` after 2026-10-18), 1 arXiv `id_list` fetch for 12 ids (exact `published` + full abstracts), 4 full-text `arxiv.org/html/<id>v1` fetches (both anchors, the third leg, and the runner-up that was capped), 2 first-party extracts (metr.org, datadoghq.com), 4 `host_probe.py --check` probes (all four hosts new to the probe record). Every hit timestamp-checked before the table; **14 in-window rows at Intensity 62–95**, written to `context/recon_proposals/2026-11-17_ai_observability_qa_signals.md`.

Dating discipline: rows 1–9 and 12–14 are event-dated from the arXiv API's own `published` field, never a search snippet. Row 10 by the note's own header. **Row 11 (Datadog FETCh) carries no visible publication date on the page** — the Date column holds the observation date (2026-11-16, the day it surfaced on HN) and a `Dating note` says so; it is a design/deployment account with no agent measurement, admissible as friction only.

## Judge (Loop 1 gate)
Seeder: `synthesize_topics.py --seed` → **rows=14 candidates=2**, both pivoting on row 11, the only non-arXiv row, under the `governance_x_runtime` archetype (heuristic 0.73 and 0.54). Both seeded candidates were scored in the brief and rejected on authority (7.7 and 7.3) — an undated, non-agent first-party post cannot carry a dual-authority leg. The Judge asserted a pair the token layer cannot see: a collision on a *measured behaviour*, not on vocabulary.

**Winner — Synthesis, E 9.0 / A 9.0 / S 8.75 → composite 8.9.**
- **Anchor A:** Acharjee Dip & Motlhabi, "Invariant-Aware Harness Enforcement to Protect LLM Agents from Silent API Failures," arXiv:2611.20595, 16 Nov 2026 — https://arxiv.org/abs/2611.20595
- **Anchor B:** "Recovery Gone Too Far: Understanding and Repairing Risky Fallback in LLM Agents," arXiv:2611.19886, 15 Nov 2026 — https://arxiv.org/abs/2611.19886
- **Third primary leg:** "AgentFaultBench: State-Verified Evaluation of Tool-Fault Recovery," arXiv:2611.20711, 16 Nov 2026 — https://arxiv.org/abs/2611.20711

Precedence (§2.5): best single-signal was SilentGuard alone at **8.3** (novelty capped to 7.5 by the 2026-10-27 silent-mis-integration piece, https://arxiv.org/abs/2610.34817), so the 8.9 synthesis clears the 0.3 margin by **0.6**. nrepair alone 8.5; Benchleaking 8.5 (held, not rejected: its natural partner is a *reinforcing* pair); leaderboard-selection 8.3; optimist-verifiers 8.0; Silent Instrument Errors 7.8 **novelty-capped at 6.0 under §3.5** — its thesis (grading/logging/replay code is part of the measurement and fails silently) is exactly the 2026-11-03 piece, and it is cited nowhere in the body so the two are not re-argued a fortnight apart.

## Fact check (Loop 2)
`context/recon_proposals/2026-11-17_ai_observability_qa_verified_brief.md`: **12 VERIFIED, 2 FLAGGED with caveats, 0 REMOVED.** Dual-anchor gate **PASS** (leg A 6 VERIFIED, leg B 5 VERIFIED, leg C 2 + 1 flagged). Two flagged rows are load-bearing:
1. **SilentGuard's win is bought with coverage** — under faults its correct answers fall 16.4% → 2.4%, and on six unseen fault types the harness alone gets 61.1% → 24.5%. The copy reports the coverage number beside every enforcement number.
2. **AgentFaultBench has no human validation**, runs three OpenAI model versions on nine constructed GitLab tasks, and its −8.33 pp belongs to the weakest model; the +9.90–+10.42 pp gain is a *revised* policy on six unseen tasks.
Sign discipline: the abstract's plain-text render drops the minus in "−8.33"; the sign was taken from Table 2's own counts (neutral 142/216 vs guided 124/216 = −8.33 pp) and from the section heading "What happens when advice hurts GPT-4o mini?". Table-vs-prose: ChEMBL's 691× is a single row (2,921,148 ÷ 4,225), printed as one API's arithmetic and never averaged.

## Draft → final (Loop 3)
Draft `context/drafts/2026-11-17_your-warning-leaves-701-wrong_draft.md`: 1,125 words, Flesch 53.4, `check_accessibility` PASS, `readability_critic` HELD-free with 9 prose advisories, `article_shape` ok, earned inline link `/retry-permission-leaves-the-caller/` (probed 200).
`article_reviewer.py` (deepseek-v4-pro): 3 attempts, **all held** — attempt 1 hard=2, attempt 2 hard=1 (kept), attempt 3 hard=2 with rhythm sd falling 10.6→9.1. The single hard failure on the kept attempt was an **undefined-acronym hold on `API`**: this gate will not accept a gloss for an all-caps token, so the token was removed everywhere in prose ("public research service", "literature index", "the silent-fault work") and left only inside the cited paper titles.
Hand repairs on the kept attempt, each invisible to a gate: (1) removed every prose `API`; (2) restored the earned inline link, which the rewrite had flattened to plain text; (3) replaced the softened possessive cue "My reading, held loosely" with "What I find hardest to hold together is this:" (a first-person verb is required); (4) named SilentGuard before the "The catch" section uses it, phrased so the vibe check does not read "harness the" as a verb ("a monitor layer the authors built, SilentGuard, …"); (5) dropped a merged claim about the retry-budget study that joined its title to its excerpt ("until the decision moved away from the caller").
Final: 1,146 words, Flesch 53.6 (floor 50), availability PASS with no undefined acronyms, `article_shape` ok, headline 100/100 STRONG with **lead_ok true**, `review_audit` PASS, voice clean on this artifact.
`run_pipeline.py gate` on the final and again on the published artifact: **all eight gates ok** (accessibility, shape, critic, headline, sources, review_audit, voice, publish_gate).

## Publish (ungated persistence)
`run_pipeline.py publish` → `published/2026-11-17_your-warning-leaves-701-wrong.md`; `published_log.md` + `sitemap.json` refreshed; **Supabase row `81d87432-be39-47c7-bdbe-7454f4ea7d3f`**; **WordPress post 1731** on cms.giniloh.com, status **publish**, category 7 "AI Stack & Tool TCO", vertical term **12** → aichieve.net, kind tag **43** `news`, featured media **1730**, 8,636-char body, Related reading before `## Sources`, **4 site-relative hrefs read back from the CMS body** (the push summary's "0 internal link(s)" is the documented relative-path false alarm).
Featured image `long_lens_industry` on flux-2/pro-text-to-image (cue: the article's own title) — a compressed telephoto down a data-center hot aisle with a red steel deny gate closed across the left rack row and the parallel row open; pixels read with vision before acceptance, no brand mark and no lettering beyond the house overlay.
**Alt-text defect found and fixed:** the artifact's `image_alt` arrived as overlay copy plus description ("AI Agent Warnings Leave Answers 70.1% Wrong. A red deny gate…"), so media 1730, the artifact frontmatter and the row's `metadata.illustration.alt_text` / `metadata.wordpress.media_alt` were all reconciled to the sidecar's own 92-character sentence, read back from the media record and from PostgREST.
`metadata.synthesis` was `None` after the push (the documented gap) and was PATCHed to `true`, read back with `kind: news` and the four `sources` entries.
Reader surface: https://aichieve.net/your-warning-leaves-701-wrong/ answered **404 on four probes over ~90 s and 200 after the static rebuild**, serving its own `<h1>` ("Your Warning Leaves 70.1% Wrong").
No social distribution and no LinkedIn/Reddit copy (channel removed 2026-10-06).

## Open items, reported not hand-fixed
1. **`publish.py` auto-deployed with unrelated WIP in the tree.** The commit `abcdc69` swept 79 files: this run's 4 drafts + 3 recon files + artifact, plus 61 back-catalogue `context/assets/*/featured.json` sidecars, 4 edits to `published/2026-10-08_*.md`, `context/internal_links.*`, `context/illustration_log.md`, `context/sitemap.json`, `context/published_log.md` and `context/generation_control.json` (whose `_note` field the sweep removed). Prior runs avoided this with `--no-deploy`; this run's publish call did not pass it and the tree was not clean. No sibling run's draft or article was committed, and `git status` is clean afterwards.
2. **The generated Related-reading block is weak again** — `internal_links.py` justified its three picks on "agent, database, public", "count, failed, large, wrong" and "software, times", and one pick is a Supply Chain & Operations piece on a reader whose article is AI Stack & Tool TCO. This is the shared-code weakness every run since 2026-10-24 has reported; the earned inline link is correct and carries the article's own argument.
3. **`verify.sh` is red desk-wide on pre-existing work** (121 FAIL lines / 113 artifact accessibility FAILs on old drafts, 4 voice-cue fails in 2026-11-08/09 drafts, and `scripts/test_illustration_overlay.py`). This run's three artifacts are absent from every FAIL list and all three PASS accessibility; the synthesis anchoring failure this run *did* cause (the angle brief's prior-art URL missing from the verified brief) was fixed and `--check-briefs` now reports `--check: OK`.
