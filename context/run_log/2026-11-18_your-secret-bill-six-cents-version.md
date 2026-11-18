# Run detail — 2026-11-18 — enterprise_build_vs_buy — evergreen

**Artifact:** `published/2026-11-18_your-secret-bill-six-cents-version.md`
**Title:** Your Secret Bill: 6 Cents a Version (headline_score 100/100 STRONG, lead_ok True)
**Vertical / persona:** enterprise_build_vs_buy / eng_leader · front: aichieve.net
**Slot:** evergreen cadence `0 19 * * 3` (Wed 19:00 UTC), gate ON at STEP 0 (mode evergreen, control=supabase, vertical=file).

## Topic

A secrets manager is billed on the object you keep, not the software you run. AWS bills 0.40 USD per
secret-month and does not charge for new versions; Google bills 0.06 USD per active version-month and
nothing for a destroyed one. Same 10,000-secret estate: about 4,060 USD/month on the AWS meter (the
vendor's own Example 4) against about 636 USD on the Google meter. Crossover at seven live versions
(0.40 ÷ 0.06 = 6.67). Build side: Vault's integrated storage needs a five-member Raft peer set
(quorum 3) before it commits a write, and each node is unsealed by hand.

## Scores and de-dup

- Axes: Usefulness 9 · Durability 9 · Evidence 8 · Actionability 9 → **composite 8.8** (≥ 8 to proceed).
- De-dup: nearest prior artifact `2026-11-11_your-rate-limit-1-39-a-second` (7 days, request budget);
  then `2026-10-28_your-sso-bill-125-a-connection` (units on one quote), `2026-11-04_your-support-bill-...`
  (support fee ladder). Cross-vertical checked and dropped: `2026-11-02_your-90-day-key-is-two-live-keys`
  (key lifetime), `2026-10-31_two-builds-one-vault` (licence split), `2026-10-27_your-label-bills-2500-series`
  (monitoring series). `grep -ril "secrets manager|Secret Manager|Key Vault|OpenBao" published/` → nothing.
- GSC export returned 0 opportunities (`2026-11-18_gsc_enterprise_build_vs_buy_opportunities.md`); bonus signal only.

## Gate and pipeline

- `evergreen_gate.py`: **PASS**, 9 rows, 9 fetched, 4 hosts (aws.amazon.com, cloud.google.com,
  developer.hashicorp.com, onetonline.org), dedup matched the 11-11 artifact.
- Review: attempt 1 **ACCEPT** (hard=0, regressions=0, Flesch 61.0, 790 words).
- Push battery (`run_pipeline.py gate`): accessibility, shape, critic, headline, sources,
  review_audit, voice, publish_gate — **all ok**.
- Publish: post **1781** on aichieve.net, status publish, category 7 (AI Stack & Tool TCO),
  vertical term 29, kind tag 44 (evergreen), featured media **1783**.

## Repairs made after acceptance (why this log exists)

1. The rewrite dropped the draft's only inline internal link; restored
   `[how long a self-hosted cluster stays supported](/your-cluster-hidden-clock/)` by hand — `article_shape`
   hard-fails a body with zero inline internal links.
2. The first link target (`/your-sso-bill-125-a-connection/`) tripped the review ledger as
   "figure lost: 125" because the number lives in the URL; the digit-free slug fixed it.
3. `publish.py` persisted the article without an illustration pass (no image fields, no notes), so the
   post went live hero-less: `illustration_creator.py --apply` (architectural_night / flux) then
   `wp_draft.py --slug ... --refresh --refresh-live` attached media 1783, and a status draft→publish
   toggle was needed before the static front rebuilt with the hero and `og:image`.
4. `"deletes"` in the At-a-glance box tripped the accessibility jargon list; "keeps every old copy" fixed it.

## Lessons recorded

- host: aws.amazon.com / cloud.google.com / developer.hashicorp.com fetch under the verifier; Azure
  Key Vault's pricing page renders `$-` placeholders and is unusable.
- pitfall: publish.py can persist without the illustration pass — check for `image_path` before calling
  the run done.
- pitfall: the frontier rewrite removes the inline internal link; restore it and re-run the battery.
