# Run log — 2026-11-18 · property_loss_insurance_mitigation · `your-6-fixes-one-hidden-code`

**Track:** NEWS (window 2026-10-19 → 2026-11-18), registry `cadence` `0 13 * * 3`, Wed 13:00 UTC slot.
**Artifact:** `published/2026-11-18_your-6-fixes-one-hidden-code.md` — "Your 6 Fixes, One Hidden Code"
**CMS:** post 425 on wellroost.com (status publish), media 427, category 2 Home Cost Decisions, vertical term 21, kind tag 28.
**Synthesis:** 8.9 (E9.0 / A9.0 / S8.8); strongest single-signal alternative 8.3 (the NAIC count alone) — margin 0.6 ≥ 0.30 precedence.

## Step 0 — generation gate
`python3 scripts/generation_gate.py --mode news --vertical property_loss_insurance_mitigation` → EXIT 0,
`GENERATION OK (ok): vertical 'property_loss_insurance_mitigation' news mode is ON. [control=supabase, vertical=file]`.

## Step 1 — Radar (14 queries)
Date-agnostic fan-outs across the vertical's five primary angles (water-loss claim math, premium spikes
versus preventative hardware, wildfire defensible space and insurability at renewal, deductible
break-even, non-renewal), plus the configured `home_lifestyle_intel` MCP pull — which returned ten rows,
every one of them off-beat (Remodelista interiors, Canary Media grid pieces, Wirecutter Thanksgiving
copy) and all stamped Intensity 84 regardless of content. That feed is not usable for this vertical;
the sweep rested on the insurance/data sources instead.

Verified in-window candidates and their fates:
- **TDI's ZIP-level reason file** (live record, observed today; reporting began 2026-04-01; a Houston
  station walked readers through it 2026-10-28) — the anchor.
- **The Secretary of State's Texas Register carry of TDI's reason-code rulemaking** (proposed
  2026-05-22) — the second anchor, and the source of the sentence that carries the thesis.
- NAIC's 2,019,799 company-initiated non-renewals in 2024 (+61%, West 25.1 per 1,000), surfaced in-window
  by trade coverage on 2026-11-09 — **demoted to context, FLAGGED**: `content.naic.org` answers a
  Cloudflare challenge to the desk's fetcher and the report PDF returned a 5.9 KB interstitial, so the
  figure could not be anchored to the origin.
- Zone 0 emergency rule package with a 2026-11-05 notice date — **dropped on §3.5**: the compliance-versus-
  discount thesis is 2026-10-16 and 2026-11-11 in this corpus.
- Falling average rates versus removal from the book (Connecticut 2026-11-09, Texas filings 2026-11-13) —
  **dropped on §3.5**: `2026-11-04_your-43-cut-hides-751000-hikes` is that exact thesis, 14 days back.
- Home insurance now exceeding the property-tax bill in two-thirds of counties (2026-10-20) — dropped:
  a trade write-up of an analysis the desk could not retrieve.
- TransUnion renter-to-owner conversion 7.2% → 3.9% (2026-11-17) — dropped: broker-pipeline story, no
  household decision.

`python3 scripts/synthesize_topics.py --seed <signals>` → `rows=7 candidates=0`. Recorded as input, not a
verdict: the collision is a taxonomy plus a reporting clock, and the token layer has no archetype for
either. The Judge asserted the pair.

## Step 2-3 — Judge and Fact check
`2026-11-18_property_loss_insurance_mitigation_verified_brief.md`: **11 VERIFIED, 2 DERIVED (Socrata
queries), 1 FLAGGED (NAIC, secondary only)**, 0 REMOVED. Dual-anchor gate satisfied — each leg carries
≥ 2 VERIFIED primary claims (leg A: the codebook definitions and the publication regime; leg B: the
"reason codes are provided only for use in a statistical plan report" sentence, the written-description
expectation, the aerial-imagery indicator, the 2026-02-04 / 2026-10-01 dates).

Seven rulings were written to the drafter. Four shaped the copy:
1. "Six" is **desk counting** of the items in TDI's own parenthetical — the article must never write that
   the state says six.
2. A reason row is **not** a decision: TDI says the reasons report "isn't the total number of
   declinations, nonrenewals, and cancellations", so no claim about how many policies fell may be derived
   from 289,218.
3. The dataset's `action_type` (80/81/82), `policy_type` (1–6) and letter `reason_code` values have **no
   public code-to-label map this run could retrieve** — labelling them would have been invention. Only the
   row count, the four notice months and the six policy types are used.
4. Nothing in the file supports a dollar figure, so no payback arithmetic was written.

## Step 4 — Draft
Structural draft 833 words, then pre-tuned: the first pass failed `check_accessibility` at **Flesch 41.3**
with three undefined acronyms (NAIC, TDI, ZIP) and a 51.5% figure load; the enumeration heading
promised six items it never labelled (held by `readability_critic`). Fixed by glosssing TDI and NAIC in
place, dropping "ZIP" from the prose in favour of "postal code", renaming the heading, and swapping long
words for plain ones rather than splitting sentences — **Flesch 54.4**, figure load back under the cap,
`readability_critic` ok, headline **100/100 STRONG** with `lead_ok` true.

**Frontier pass** (`deepseek-v4-pro`, 3 attempts): attempt 1 reject (hard=3, regressions=1), attempt 2
reject (hard=2), **attempt 3 ACCEPT** (hard=0, regressions=0, rhythm 6.7 → 8.1, health 0.672 → 0.903,
Flesch 53.1, 823 words). Two hand repairs after it landed: the rewrite had flattened the three
`By the numbers` bullets into unlabelled sentences (restored the `**figure:**` shape the critic checks),
and it had dropped source [4]; the Click2Houston citation was restored in the tension paragraph and the
source list renumbered rather than leaving an uncited reference. One phrase was also rewritten to remove
a four-preposition chain in the NAIC sentence.

## Step 5 — Gates
`run_pipeline.py gate` — **8/8**: accessibility, article_shape, readability_critic, headline, source_gate
(4 sources / 4 hosts), review_audit, social voice (clean for this artifact; repo-wide run still reds on
two older drafts elsewhere), publish_gate.

## Step 6 — Persistence
`publish.py` first run was killed by the tool timeout after writing `published/` and the log row; the
re-run completed the pass. Final state: Supabase article **1cdaba4b-0745-4991-b234-01861af857fa**; WordPress
post **425** on cms.wellroost.com, status **publish** through the two-call vertical-term sequence (term 21,
kind tag 28 `news`, category 2), featured media **427**, 7,461-char body carrying **4 site-relative
hrefs** (the summary's "0 internal link(s)" is the documented relative-path false alarm, confirmed over
REST); `context/sitemap.json` refreshed; auto-deploy commit pushed.

**Featured image — two defects found and fixed in-run.** `paper_collage` on `nano-banana-pro`, and the
collage itself is right: a torn-paper diptych on a workbench, one page's ochre band holding six white
cutouts (rake, brush, lit window, roof tile, branch, key) and the other page holding a single roof shape.
But the typography overlay had been set from the lead and **clipped mid-sentence** ("…refused to keep a
home policy. Each"), and the sidecar's `alt_text` had been overwritten with the headline glued to a
truncated phrase ("…roof type", 118 chars). Fixes: the overlay was re-typed free of charge from the
pristine `featured.base.jpg` with an explicit kicker/title/hook; alt and caption were rewritten to
sentences describing the picture (118 and 96 chars) in the sidecar, the artifact, the Supabase row and
the attachment; and the corrected bytes were pushed with `wp_draft.py --slug … --reimage`, which uploaded
**media 427** and removed 424. **The front was serving the old alt for a few minutes after the reimage**
(it had built against 424's metadata), and a plain re-fetch once the attachment meta landed returned the
correct alt and the `-featured-1` hero — no redeploy was needed this time, unlike 2026-11-12/13.

## Open items
- **Internal links are weak by the rule-12 test.** The generator stamped three same-category picks —
  `/your-43-cut-hides-751000-hikes/` (justified, Texas rates), `/your-49-discount-isnt-all-roof/`
  (justified on "home, insurers") and `/your-flood-gap-has-44-days/` (justified on "home, policy"). Two of
  the three rest on one incidental token. The earned inline link in the body is
  `/your-nonrenewal-isnt-final-count-120-days/`, verified 200; the block was left as generated and the
  weakness recorded rather than hand-edited, per the pattern of the last nine runs.
- The `home_lifestyle_intel` MCP feed returned ten irrelevant items at a flat Intensity 84 for this
  vertical — its relevance scoping, not its plumbing, is the defect.
- `content.naic.org` is behind a Cloudflare challenge for the desk's fetcher, so NAIC's own reports cannot
  be used as anchors; its figures arrive only through trade coverage and must stay flagged.

No social distribution and no LinkedIn/Reddit copy (channel removed 2026-10-06).
