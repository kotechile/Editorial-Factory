# Run log — 2026-11-17 · enterprise_tech_leadership · EVERGREEN

**Artifact:** `published/2026-11-17_your-8-gib-node-sells-6-1.md`
**Title:** Your 8 GiB Node Sells 6.1: The Hidden Reserve
**Kind:** evergreen (archetype evergreen, evergreen: true) · persona `eng_leader` · front `aichieve.net`
**CMS:** post 1754 (publish) · vertical term 17 · kind tag 44 (`evergreen`) · media 1756
**Supabase row:** 0453402a-aa16-4015-a399-a826fcd365e6

## Topic selection (evidence, not invention)
- Lead: vertical `primary_angles` — "cloud repatriation" / "monolith vs microservices" both turn on the capacity a rented node actually delivers; the persona's `wants` ("concrete numbers, decision frameworks, what to do Monday morning") points at the number to commit.
- Founder position tested, not asserted: `founder-voice.md` §3 `enterprise_tech_leadership` — "the cloud is an operational agility loan"; the article's contrarian move is that the fine print is the never-schedulable share, which makes the small node the expensive one.
- Field friction used as context only: `customer-truth.md` Anecdote 2 (48 microservices / 3 clusters / 25-engineer org).
- GSC bonus signal: `gsc_analyzer.py --vertical enterprise_tech_leadership --export-md` → 0 opportunities (thin impressions; never a veto).
- Composite 8.7 (U8 / D9 / E9 / A9).

## Candidates refused (by hand)
- **Retry budget** (SRE book 10% retry ratio + 3 attempts, gRPC `maxAttempts` 4 with ±20% jitter, AWS Builder Library on amplification) — all four probes fetched first try, composite 9.0, refused as a retread: `2026-10-14_retry-permission-leaves-the-caller`, `2026-10-12_agent-timeout-false-alarm-budget` and `2026-11-11_your-rate-limit-1-39-a-second` already argue retry permission, retry deadlines and request budgets for this desk.
- **EU Data Act switching-charge exit date (12 January 2027)** — already carried as the exit-date leg of `2026-10-07_sla-credit-is-not-insurance` (enterprise_build_vs_buy).

## Gate
`evergreen_gate.py` PASS: rows=4, fetched=4, sources=4, hosts=3 (kubernetes.io, cloud.google.com, learn.microsoft.com), dedup → `2026-11-03_your-pool-becomes-2000`. Marker checked_at 2026-11-17T18:34:42+00:00.

## Verification and rewrite
- Draft pre-tuned: readability_critic ok, accessibility PASS (Flesch 60.7 → final 59.8, floor 50/target 60), shape ok, voice ok, headline 100/100 with `lead_ok True`.
- Frontier review: attempt 1 rejected (1 regression), attempt 2 ACCEPTED — rhythm 7.3, health 0.852.
- Hand repairs after accept: repointed the `At a glance` risk bullet from [3] to [2] (the "quarter on small nodes" figure is the GKE ladder, not Azure), added one figure-free sentence to keep figure load under 45%, and shortened two long nouns.
- `run_pipeline.py gate` → 8/8 ok (accessibility, shape, critic, headline, sources, review_audit, voice, publish_gate).

## Persistence
`run_pipeline.py publish` → published/, published_log, Supabase, sitemap, CMS post 1754 live; internal links: inline `/your-cluster-hidden-clock/` plus the generated Related-reading block (3 links, written back to the Supabase row).

## Defect found and repaired this run
`publish.py` completed with **no illustration at all** (the artifact left the push with no `image_*` frontmatter and the CMS post with `featured_media: 0`), so the first live render was hero-less. Repaired in-run: `illustration_creator.py --apply` (studio_object, flux-2, rev 1, +typography overlay) → `wp_draft.py --slug … --refresh --refresh-live` (media 1756 attached, post stayed live) → status toggle draft→publish to fire the front rebuild. The alt text is title-prefixed by the generator (131 chars, within the 40–140 band) rather than the one-sentence house shape; left as written because the sidecar and CMS agree.

## Figures carried (all from the four verified rows; derived sums recomputed)
- GKE ladder 25/20/10/6/2% + 100 MiB eviction buffer → 4 GiB: 2.90 usable; 8 GiB: 6.10; 128 GiB: 118.58.
- AKS lesser-of 20 MB × maxPods + 50 MB vs 25% → 8 GB / 30 pods: 650 MB reserved, 7.25 GB allocatable (90.625%).
- kubelet defaults: memory.available<100Mi, nodefs 10%, imagefs 15%, inodesFree 5%, 0s grace on hard thresholds.
- memory.high = requests + 0.9 × (limits − requests); 256 MiB request / 1 GiB limit → 947 MiB; no-limit Burstable inherits node allocatable; Guaranteed has no memory.high.
