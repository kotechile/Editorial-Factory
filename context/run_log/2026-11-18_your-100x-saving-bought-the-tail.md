# Run log — 2026-11-18 · enterprise_build_vs_buy (news) · your-100x-saving-bought-the-tail

**Outcome:** published → `published/2026-11-18_your-100x-saving-bought-the-tail.md` ("Your 100x Saving: A Hidden Cap"), Supabase row `1ad18f72-cf07-44c1-87fd-53e05142c887`, WordPress post **1769** on cms.giniloh.com (status publish, category 7, vertical term 29, kind tag 43 `news`, featured media 1768).

## Window and sweep
Window 2026-10-19 → 2026-11-18. 23 Hacker News Algolia `search_by_date` sweeps bounded to the window across 18 term sets, 6 web fan-outs over the vertical's configured sources, 8 primary-source fetches, 4 host probes. 8 signal rows kept.

## Winner
Synthesis **8.8** (E=8.8 A=8.8 S=8.8) over the best single signal (Revolut alone, 8.4; novelty capped for adjacency) — margin 0.4, clears the §2.5 precedence rule.
- **Leg A:** Revolut's self-hosted GLM deployment, reported by The Register 2026-11-03 — 2,000 engineers, 56 B200s, $0.30/M blended "about a tenth" of Codex/Claude Code, 380 GB weights + 6–26 GB/user, 256k context cap, sub-3s TTFT, 200 tok/s (≈800 after 5 p.m.).
- **Leg B:** the 2026-11-15 Protomaps build post — 139 GB single file, ~$5/month storage, $0.05 per 1,000 map loads against Mapbox's $5.00 entry rate; four settings (referrer allow-list, large-object caching, 10 kB/s after 10 MB, bandwidth cap). Corroborated by Mapbox's own price table ("a map load includes unlimited Vector Tiles API and Raster Tile API requests") and bunny.net's ($0.01/GB, $1 minimum, no request fees).

## Seeder
`rows=8 candidates=2` (heuristic 0.77–0.78). Adopted #1⨂#2. Rejected #1⨂#4 (Revolut ⨂ bunny's price list): a rate card is an input to row 2, not a second development.

## De-dup
Named and distinguished in the brief: `your-44x-ticket-saving-needs-a-busy-box` (2026-11-11, utilisation of a fixed bill), `your-rate-limit-1-39-a-second` (2026-11-11 evergreen, page size inside a request budget — nearest neighbour in mechanism, novelty held at 8.8), `your-sso-bill-125-a-connection` (2026-10-28, revenue design of a denominator). Sibling fronts on aichieve.net in the last 7 days checked, nearest is `your-boxs-hidden-79-speed-cut` (11-17, what a rented unit delivers).

## Dropped at Stage 1 (dates checked)
- Gartner "AI coding costs will surpass average developer salary by 2028" — release dated **2026-06-24**; a November social repost made it look in-window. Excluded entirely.
- Uber's $1,500/tool cap — June 2026.
- Revolut's AI Engineer NYC talk — 2026-10-13, outside the window; The Register's 2026-11-03 write-up is the anchor.
- Microsoft 365 outage 2026-11-12/13 (≈20 hours, 140,000 reports, 74 countries) — best counterweight, but the only retrievable record in this sweep was a tertiary encyclopedia entry, which `source_gate` bars from Sources. Carried as context, never cited.
- EU AI Act GPAI enforcement — live since 2026-08-02, no in-window event.

## Fact check
18 VERIFIED (11 leg A on theregister.com, 7 leg B across bruceroettgers.eu, mapbox.com, bunny.net), 0 REMOVED. Six binding rulings written into the verified brief; the ones that changed the copy: the 30 cents is quoted for the **GLM-5.1** deployment while the 56-GPU fleet serves 5.3; Mapbox's $5.00 is the entry band (50,001–100,000), not a flat rate; the 100x is the author's per-1,000 estimate on a 5 MB assumption, and 100,000 loads on Mapbox's own tiers is $250 against ~$5 of delivery.

## Gates
Draft: accessibility PASS (Flesch 63.4), readability_critic ok, article_shape ok, voice OK (1,149 checks), headline 100/100 STRONG with `lead_ok` true. `run_pipeline.py gate --file` 8/8 ok; `--slug` re-run after the push 8/8 ok.

## Frontier rewrite
`run_pipeline.py review` → attempt 1 **ACCEPT**, hard=0, regressions=0, rhythm 8.3→8.3, health 0.819→0.822, Flesch 63.2, 948 words. Hand audit against the verified brief found six defects the gates cannot see:
1. "$5 a month" described the storage fee as though it covered serving — restored to "sits in storage".
2. "The cost fell to 30 cents" attached the published figure to the current model — repinned to "the earlier GLM-5.1 deployment".
3. "a volunteer project still produces" — an unverified characterisation of Protomaps; rewritten to "the project publishes on its own schedule".
4. "a dataset maintained on someone else's schedule" — flattened to "a dataset somebody else keeps current".
5. The $5 delivery figure in The catch cited Mapbox [1]; split into two sentences so the delivery cost rides the builder's own rate [2].
6. Lead attributed "its 30 cents" to Revolut's current stack; now "its published 30 cents".

## Persistence
`run_pipeline.py publish` → published artifact, published_log, sitemap, Supabase row, CMS post. Featured image generated (flux-2/pro-text-to-image, document_flatlay, a printed price list with one highlighted row under a steel straightedge). **Alt defect fixed in-run:** the director's alt arrived as the overlay headline glued to a clipped phrase ("…with its bottom row folded under a steel straightedge", 137 chars, wrong casing); replaced with a 103-character sentence plus a complete caption across the sidecar `featured.json`, the artifact's `image_alt`/`image_caption`, media 1768 (POST, read back) and the row's `metadata.illustration.alt_text` / `metadata.wordpress.media_alt`. `illustration_creator.py --check` ok. Because a CMS media PATCH does not fire the redeploy mu-plugin, all three fronts were rebuilt through `giniloh_coolify_redeploy_all()` inside the cms.giniloh.com container (giniloh/aichieve/wellroost, HTTP 200 each).

Reader surface: https://aichieve.net/your-100x-saving-bought-the-tail/ answered 404 three times across ~2 minutes, then **200** with its own `<h1>` — the documented static-build lag.

## Open items (reported, not hand-fixed)
- `scripts/publish.py` builds `metadata` from an explicit key list and never writes `metadata.synthesis`, so a synthesis row cannot be badged as a fusion by `/api/articles.json` even when the artifact declares `synthesis: true` (the 2026-11-12 supply_chain row carries `metadata.synthesis: true`, so something older or manual wrote that one). This run's row has `kind: news` and both anchors under `sources`, but no `synthesis` flag.
- The generated Related-reading block justified `/your-rate-limit-1-39-a-second/` on the two incidental tokens "100x" and "hidden"; it sits on the same front and the same "AI Stack & Tool TCO" category, so it was kept and recorded rather than stripped — another instance of the documented scorer weakness, and uncomfortably close to this article's nearest published neighbour.
- The director's alt still arrives as overlay copy on every run (fifth consecutive time); the hand fix is routine, not exceptional.
- `check_accessibility`'s Figure/At-a-glance advice sits at 47.9% figure load (cap 45%, advisory): the piece is a price comparison, and the remaining digits are the sources' own numbers.

No social distribution and no LinkedIn/Reddit copy (channels removed 2026-10-06).
