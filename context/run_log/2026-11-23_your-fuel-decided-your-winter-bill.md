# Run log: home_infrastructure_lifecycle_tco news — 2026-11-23 (your-fuel-decided-your-winter-bill)

Gate at STEP 0: pass (generation_control on). Radar: 9 web queries + home_lifestyle_intel MCP sweep (10 candidates, 4 in-window kept) → signals file rows=7 (2 out-of-window/background, intensity 55/68). `synthesize_topics.py --seed` rows=7 candidates=2 (marker fresh).

## Judge
Single-signal 8.4 (N7.5/A9.5/S8.5): NEADA November 2026 Winter Heating Forecast, released 2026-11-10 (primary: press-release PDF fetched in full). De-dup: ACHR Nov price list retread (carried by our own 11-09 artifact → novelty cap); NAHB HMI 25 sibling-anchored 2026-11-23 (home_equity_tco, same front); pending home sales anchored 10-26; Canary heat batteries off-persona; seeded pair #2⨂#5 scored ~7.6 (< single, < +0.3 margin). §3.5: $2,115 EIA figure from 11-09 usable as corroboration only, labelled FLAGGED (different basis — EIA price×usage vs NEADA expenditure forecast; never presented as a revision of one agency's number).

## Fact check
11 rows: 8 VERIFIED (verbatim off the NEADA table — the table is the claim of record), 1 DERIVED (18× delta arithmetic), 2 context-FLAGGED (EIA $2,115 basis difference; ACHR/25C retread-capped). No REMOVED.

## Draft → review → gate
Draft: title "Your Fuel Decided Your Winter Bill: $686 or $2,977" (100/100 STRONG, lead_ok ok), internal link `/your-oil-heat-619-one-day-of-relief/` (live, 200). Critic clean after three advisory repairs. Review HELD 3×: the frontier rewrite kept (a) tagging EIA as [2] while the draft body never carried a [2] marker, and (b) dropping the tactical section's first-person cue. Fix applied on the DRAFT (add the [2] tag on the EIA weekly sentence) plus two hand repairs on the held rewrite ("My advice is to not treat" → first-person form; reading-level word swaps; Flesch 50.4). Gate 8/8.

## Persist + deliver
publish.py: Supabase row 2dfdae7c, CMS post 468 (publish, vertical term 17, kind tag 28 'news', category 4 Energy & Efficiency), sitemap refreshed, auto-deploy commit. Illustration: editorial_macro on flux-2/pro-text-to-image (split-pair: brass gas valve vs rusted oil tank; cue "the fuel the house already burns"); first attempt refused 3× (prompt >120 words, no light direction) → pinned --style --force, 5 credits, 2400×1350.

## Repairs in the delivery pass (report, not silent)
1. **--reimage run twice** (mine, to verify) uploaded a second media and removed the just-attached one, leaving featured_media on a 404; repaired by direct REST PATCH (media 471 attached). Lesson recorded via learn.py: --reimage is one-shot; verify by REST read-back.
2. **Alt text truncated mid-phrase** ("…, split") on the CMS media; repaired in sidecar featured.json + artifact + published copy + REST PATCH media + Supabase metadata (one complete 40–140-char sentence).
3. Front build was forced via Coolify (deployment aelpuudnnaf2vcaazdcq3jxc, finished); reader page 200, correct h1, hero img with the repaired alt, 2 generated internal links live (Related-reading block resolves on wellroost).

## Open defects found (owner-level, not fixed here)
- **Live 2026-11-09 artifact `your-condensers-repair-bill-2090-vs-700` states the R-410A install allowance "ran out at the start of 2026."** EPA finalized a rule (NAHB, 2026-05) removing that installation compliance date — pre-2025 R-410A stock is installable until depleted (NY excepted). The claim is now stale on a live page; a re-cut is the owner's call (grandfathering convention: report only).
- **scripts/test_illustration_overlay.py: 4 failures, pre-existing** (fails identically on HEAD~1; subject-map luminance regression, likely a numpy/scipy environment shift). It reds `verify.sh` for every run until fixed.
- verify.sh also lists 111 old draft accessibility FAILs (September artifacts) — pre-existing, unrelated to this run.
