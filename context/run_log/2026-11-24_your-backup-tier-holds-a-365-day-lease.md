# Run log — 2026-11-24 enterprise_tech_leadership evergreen: your-backup-tier-holds-a-365-day-lease

## Topic and evidence
Backup storage-tier economics: pick a backup's storage class by restore-time requirement, not by
list price. Chosen from the vertical's founder-voice pillar (cloud as an operational agility loan),
customer-truth Anecdote 1 (the $68k/month transfer shock — an unpriced pricing line dominates the
bill) and the persona's wants (concrete numbers, Monday-morning decision).

- Brief: `context/recon_proposals/2026-11-24_enterprise_tech_leadership_evergreen_brief.md` — gate
  PASS, 5 rows on 3 hosts (aws.amazon.com, cloud.google.com, learn.microsoft.com), all fetched by
  the gate with the figure matched in the fetched text.
- Verified brief: `..._evergreen_verified_brief.md` (news-track filename collision avoided).
- De-dup named `2026-11-17_your-8-gib-node-sells-6-1` first; cross-vertical grep clean.
- Candidate table: winner 8.6; egress gravity 6.9 dropped (rate table client-rendered); PITR 6.6
  dropped (single-host evidence).

## Pipeline
- Draft pre-tuned: accessibility PASS (Flesch 55.7, acronyms glossed), critic ok, shape ok,
  headline 100/100 STRONG, lead_ok True.
- Review attempt 1: HELD hard=1 (undefined GB/TB after re-voice dropped the glosses). Repaired the
  held attempt by hand (spelled-out units, one re-voiced inference labelled as a read), then adopted
  it as `_final.md`. Accessibility PASS, critic ok, shape ok, voice ok.
- `run_pipeline.py gate`: 8/8 ok. `publish`: WordPress post 1849, live; Supabase row cd13bf00;
  media 1848; internal-links block stamped (3 links) and written back to Supabase; sitemap
  refreshed; auto-deploy pushed.
- kie.ai image generation attempt 1 failed (Internal Error); retry landed media 1848.
- Front verified live: HTTP 200 (after ~3 min build lag), hero `-1024x576` derivative present, 3
  internal links present, vertical term 17, kind tag 44 (evergreen).
- `run_pipeline.py finish` exits 1 on corpus-wide checks: remaining reds are other runs' drafts
  (`your-local-box...` missing primary_keyword + untraceable anchor, `your-substation...` missing
  `<!-- lead -->` + tactical observer cue, overlay unit tests). My artifact is clean on all of them.

## Flags for the next run
- `check_social_voice.mjs` reads every file in `context/drafts/` — a pre-rewrite draft that fails
  voice reds the sweep even after the `_final.md` is published. Fixed my own draft by hand; the two
  other runs' drafts still carry the same defect at sweep time.
