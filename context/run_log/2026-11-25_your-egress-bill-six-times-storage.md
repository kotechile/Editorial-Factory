# Run log: enterprise_build_vs_buy evergreen — 2026-11-25 — your-egress-bill-six-times-storage

## Verdict
Published. "Egress Pricing: Six Times the Storage Line" (`published/2026-11-25_your-egress-bill-six-times-storage.md`),
CMS post 1871 (status publish, kind tag evergreen), media 1870, Supabase row 68f8891a-b8ca-4334-8d03-aa9442b7b1de,
sitemap refreshed, auto-deploy pushed. Reader front verified: title, og:image, -1024x576 hero derivative, body, 3
related-reading links + 1 inline link (the-cloud-bill-break-even). Initial curl was a build-lag 404 at minute ~0;
re-verified 200 after rebuild.

## Topic selection
Winner **your-egress-bill-six-times-storage**, composite **8.9** (U9/D9/E9/A8) from the vertical's own angle
"self-hosted infrastructure vs managed cloud services TCO" + persona wants (concrete numbers, decision framework).
Thesis: object storage bills the object's life per GB-month and the data's exit per GB out — Google's exit is 6x its
storage price — and the vendors that abolished the egress meter priced it back into storage, so the egress-to-storage
ratio, not the list price, ranks offers (2 TB stored / 4 TB out: ~$492 transfer on GCS, ~$369 on AWS, $0 on R2/B2;
~$14 total on B2).
Dropped: internal tooling maintenance tax (E6 — no measured hours primary this week); observability ingestion meters
(E5 — both load-bearing vendor pages are JS rate cards).

## Gate
`evergreen_gate.py` PASS — 8 rows / 4 hosts (aws.amazon.com, cloud.google.com, developers.cloudflare.com,
backblaze.com), all fetched and figure-matched. Note: AWS S3 pricing's rate tables render as `priceOf!` templates;
the verified figures come from the page's own worked examples (Ireland egress $0.09/GB, inter-region $0.02/GB,
90/180-day minimums, S3 Tables $0.0265/GB). First de-dup pass recorded `dedup="evergreen"` (matched the word, not an
artifact) and the brief's first slug ref was wrong by a week (2026-11-18 vs the actual 2026-11-11 rate-limit piece);
corrected the line, re-ran the gate, marker now names `2026-11-11_your-rate-limit-1-39-a-second`.

## Review
Rewrite HELD 3×, all hand-repaired per the flow-regression rule:
1. attempt 1 (from my draft): hard=3 — no first-person sentence in nuanced-takeaway; Flesch 46.2; acronyms AWS/GB/TB.
2. hand repair to Flesch 51.3 pass; attempt 2: hard=0, regressions=1 — "my read is that" boilerplate cue; adopted and
   repaired by hand ("Where I land after staring at these four cards…"), re-added the internal-links marker.
3. gate battery on the adopted final: review_audit failed once (the rewrite had dropped the 2,048/4,096 GB derivation
   figures) → restored; critic failed twice (double citation tags [2][3]/[3][4] in one sentence; multi-sentence
   bullet) → split/merged per its rules; "this desk" antecedent → named.
Final: Flesch 51.3, all 8 gates pass.

## Pitfalls worth recording
- `evergreen_gate.check_dedup` matches the FIRST ref in the De-dup line that resolves to any file; a wrong date-slug
  inside the line silently degrades the marker to "evergreen". Verify the named artifact exists with the exact date.
- `publish.py` delivery note "0 internal link(s)" counts body absolute URLs only; the related-reading block and the
  inline site-relative link both verified live on the front.
- The reviewer re-voices the file it is handed, so Flesch must clear ~52 in the pre-review draft to survive one
  rewrite; repair-by-hand after holds is faster than re-generating.
