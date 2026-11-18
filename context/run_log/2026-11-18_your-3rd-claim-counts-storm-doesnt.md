# Run detail — 2026-11-18 — your-3rd-claim-counts-storm-doesnt

Vertical: property_loss_insurance_mitigation · mode: evergreen (`0 20 * * 3`) · persona: pro_homeowner
Artifact: `published/2026-11-18_your-3rd-claim-counts-storm-doesnt.md` · CMS post 429 (wellroost.com)

## Step 0
`generation_gate.py --mode evergreen --vertical property_loss_insurance_mitigation` → GENERATION OK
(control=supabase, vertical=file), exit 0.

## Topic selection
Lead came from the vertical's own `primary_angles` #2 ("premium spikes after a claim versus the
actuarial value of preventative hardware") and #5 ("non-renewal and coverage-gap risk"), read through
`pro_homeowner`'s stated want ("TCO depreciation math") and founder-voice §3 `resilient_home_assets`
("The primary risk to suburban real estate equity is no longer mortgage interest rates; it is carrier
non-renewal"), applied to the claim file rather than the roof.

Candidates scored: counted-claims ladder 9.0 (winner); "sudden and accidental vs continuous leak" 7.9
(dropped — actionable lever is a past event); high-vs-low deductible break-even 7.0 (dropped — every
premium credit in circulation is a carrier quote, no filed actuarial table); HOA loss-assessment gap
7.4 (dropped — HO-6 limits only on carrier explainers); rebuild-cost vs market value 8.3 (dropped —
re-argument of `2026-11-04_your-70-limits-12-5-gap`).

GSC: `gsc_analyzer.py --vertical property_loss_insurance_mitigation --export-md` → 0 high-potential
striking-distance queries (bonus signal only, did not veto).

## Gate
`run_pipeline.py gate-brief` → PASS, marker `rows=7 fetched=7 sources=3 hosts=3
dedup="matched a prior artifact: 2026-11-18_your-6-fixes-one-hidden"`. Hosts: tdi.texas.gov,
iiat.org, iii.org. Probed and refused: statutes.capitol.texas.gov (navigation shell, 1,354 chars of
nav only) and law.justia.com (unreachable to the verifier's UA) — the Chapter 551 text is therefore
cited through the regulator's consumer guide and the agents' association summary, and the article says
so in prose.

Verified brief copied to `2026-11-18_property_loss_insurance_mitigation_evergreen_verified_brief.md`
so the reviewer's ledger picks it up (the plain `_evergreen_brief.md` name is what the gate writes).

## Draft and rewrite
Draft 1: Flesch 43.3, `FAIR` flagged as an undefined acronym, 51.9% figure load, two double-citation
sentences — all fixed by plain-word swaps and re-writing the FAIR Plan sentence as "a state plan"
rather than inventing an expansion for FAIR. Draft 2: Flesch 60.0, shape ok, critic ok.
Title re-scored: "Your Water Claim Counts, Storm Doesn't" 89/100 with the body (no figure anchor) →
"Your 3rd Claim Counts, Storm Doesn't" 100/100 standalone and with body, `lead_ok: True`. Slug
renamed to match; the superseded `_draft.md` deleted by name.

Frontier review: attempt 1 ACCEPT, hard=0, regressions=0, rhythm 6.5→6.5, Flesch 60.0, 784 words —
the accepted `_final.md` was byte-identical to the draft, so the manual post-rewrite audit (frontmatter
flags `kind/archetype/evergreen`, exactly one inline link, H2s, every figure earned) found nothing the
rewrite had changed.

## Gates
`run_pipeline.py gate` → 8/8 ok (accessibility, shape, critic, headline, sources, review_audit, voice,
publish_gate).

## Publish
Post 429, status publish, media 428 (hero + `-1024x576` derivative both 200), vertical term 21,
tag term 29 (`evergreen`), category 2 (Home Cost Decisions), Supabase row c3854e15.
Internal links: 3 generated (`your-5-deductible-risks-your-claim`, `your-6-fixes-one-hidden-code`,
`your-flood-gap-has-44-days`) and written back to the Supabase row. The publish transcript's
"0 internal link(s)" line counts absolute-href matches; the rendered front carries them (verified by
curl on `/your-3rd-claim-counts-storm-doesnt/`: 200, 43 KB, h1 + og:image + hero present).

## Open items
- The reviewer returned the draft unchanged; a no-op ACCEPT is not a defect but it means the voice is
  the drafting pass's, not a second frontier pass's.
- Two Texas-ladder pieces ran in eight days for this vertical (2026-11-18 reason codes, this one). The
  mechanisms differ (reason codes vs claims counting) but the next property run should leave Texas.
