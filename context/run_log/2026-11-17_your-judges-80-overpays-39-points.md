# Run log — 2026-11-17 ai_observability_qa (evergreen)

**Article:** `your-judges-80-overpays-39-points` — "Your Judge's 80% Overpays 39 Points"
**Track:** evergreen (`skills/evergreen_topics.md`), cadence `30 17 * * 2`
**Persona:** evals_infra_eng · **Surface:** aichieve.net

## Topic selection
- Lead: founder-voice §3 pillar ("LLM-as-a-judge calibrated against human consensus") + persona `wants` ("judge calibration") + customer-truth Anecdote 2 (judge pass rate drift 74% → 96%).
- Candidate scores: chance-corrected judge agreement 8.8 (winner) · redundant retry-cycle detection 7.8 (dropped: mechanism already published as `2026-10-15_agent-loop-bound-not-a-budget`) · human-label budget for calibration 7.1 (dropped: no primary source printed a sample size) · deterministic-vs-probabilistic tier split 6.8 (dropped: no measured ratio).
- De-dup: nearest prior `2026-11-03_your-grader-adds-22-points` (renderer/parser layer) and `2026-10-06_buying-ai-quality-when-the-score-belongs-to-the-judge` (judge discrimination / market). Cross-vertical grep for position bias / test-retest / chance-corrected returned no artifact arguing kappa deflation.

## Gate
- Brief: `context/recon_proposals/2026-11-17_ai_observability_qa_evergreen_brief.md` — 5 rows, 4 distinct sources, 3 hosts (arxiv.org, pmc.ncbi.nlm.nih.gov, papers.nips.cc). PASS at 17:33 UTC.
- First run reported `figure_absent` on the PMC row; the same URL refetched complete on the second run and every pattern matched (logged as a pitfall).

## Verification and rewrite
- Accessibility PASS (Flesch 59.0, floor 50), critic ok, shape ok, headline 100/100 with `lead_ok` true, 8/8 gates green.
- Frontier pass: first `run_pipeline review` returned a byte-identical body with ACCEPT hard=0; re-ran `article_reviewer.py` to a temp path and adopted that rewrite (rhythm health 0.885 → 0.896), then hand-repaired the lead to restore the title's "overpays" and keep `lead_ok`.

## Persistence
- Supabase row `4f1e0bdd-8719-4464-966e-db1044ffeb86`; WP post 1748 (publish), vertical term 12, kind tag 44 (evergreen), media 1750.
- Internal links: 3 related-reading links + 1 inline (`/100-case-eval-925-coverage/`), stamped site-relative.
- Illustration: art director truncated on the first call (`finish_reason=length`), so the first push went hero-less; re-commissioned (`cinematic_still` on flux-2), attached with `wp_draft.py --reimage`, alt rebuilt to 89 chars, then a draft→publish toggle to rebuild the static front. Front 200 with hero, `-1024x576` derivative and `og:image`.

## Open items
- The CMS delivery summary counts internal links in absolute form and reports "0 internal link(s)" although the artifact carries a site-relative block; worth a look in `wp_draft.delivery_problems`.
