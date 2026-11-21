# Run log: your-899-blowers-9-day-window (outdoor_power_equipment, news) — 2026-11-21

Gate: `generation_gate.py --mode news --vertical outdoor_power_equipment` → OK (exit 0).

## Radar
Window 2026-10-22 → 2026-11-21. home_lifestyle_intel MCP returned 10 rows, all off-vertical (mortgage/energy policy, boilerplate intensity 84) — contributed nothing; all rows came from date-agnostic fallback searches with publisher-date verification (WP/JSON-LD date fields read before writing each row). 16 queries total. Signals file: 6 rows, 5 domains; two observation-dated rows (EGO vendor page 2026-11-21, Walmart grid 2026-11-21) carry Dating notes.

## Seeder + Judge
`synthesize_topics.py --seed` → rows=6 candidates=0. Structural: the archetype registry (PATTERNS.verticals) contains no outdoor_power_equipment pattern, so no pair can ever seed there — recorded in the brief's runner-ups. Judge scored the single-signal winner **8.3** (N8/A9/S8); the asserted pair EGO-disclaimer ⨂ guide-sellout scored 8.5 but beat the single by only 0.2, under the ≥0.3 precedence margin → single-signal kept. Topic was dropped at 5.5 by the evergreen track on 2026-11-07 for want of in-window anchors; the anchors now exist (vendor deadline page, guide re-check 11-20, deal ladders 10-26/11-08).

## Fact check
11 claim rows: 9 VERIFIED (incl. EGO's verbatim footnote "1-Offer valid through 11/30/26 … Subject to availability. U.S. Only." fetched live), 2 DERIVED ($51–$151 markdown spread; 9-day interval), 0 REMOVED. Ruling enforced: $220 is a banner ceiling across select tools, never a per-SKU cut. Background (never anchors): CR cold-derate (page 2026-02-09), Milwaukee M18 press release (2025), Toro's expired Sept promo still rendering, Ace/Acme 403s.

## Draft + Loop 3
Draft passed Flesch 51.7, headline body-aware 100 STRONG lead_ok true (kept "Your $899 Blower's 9-Day Discount Trap"). article_reviewer ran only ONE attempt and wrote HELD (Flesch 49.9 + EGO/SENIX acronyms in ITS OWN rewrite — it had replaced my passing parenthetical glosses with em-dash appositives, which the gate refuses). Hand repairs on the documented path: restored "EGO (the battery outdoor-tool brand)" / "SENIX (a budget cordless-tool brand)", restored the 1./2. enumeration labels, un-doubled the [3] tag before the price table, re-ran gates → PASS, `review_audit` PASS (718→754 words, figures 24, no shrink).

## Gates + publish
run_pipeline gate: 8/8 ok (accessibility, shape, critic, headline, sources 4/4 hosts, review_audit, voice, publish_gate). Publish → Supabase row 6ce14c97-8aa7-467b-8ad8-b66919737a70, CMS post 441 on cms.wellroost.com (two-call vertical sequence, term 25, kind tag 28 news, category 24).

## Post-publish repairs
1. **publish.py ran NO illustration pass** (no image lines in its output; featured_media 0 on a live post) — the documented hero-less class. Recovery: `illustration_creator.py published/<artifact> --apply` → `cinematic_still` on flux-2, 5 credits, 2400×1350, pixels read with vision (no brand mark, no legible text), then `wp_draft --reimage` → media 443, read back featured_media 443.
2. **The director's alt arrived as overlay copy cut mid-phrase** ("EGO's $220 Snow-Blower Deal Has Two Deadlines. A teal battery snow blower … falling over the") — media 443 PATCHed (Basic auth) to a 116-character sentence; sidecar featured.json, artifact image_alt/image_caption and row metadata.illustration/wordpress.media_alt reconciled in one commit.
3. **publish_gate.title_gate re-cut the headline to "$220 Off Your EGO Kit — If It's Still There"** and wrote it to the artifact + row `title` while the CMS push had already sent the pre-gate title — the documented six-surface split (row title new, CMS + metadata.headline old). Screened the adopted title body-aware: 100 STRONG, all figures in the piece ($220 banner ceiling), but lead_ok false → restored the missing content words into the lead ("banner caps the season's discount at $220 off your EGO kit… still there"), re-scored 100 STRONG lead_ok true, then reconciled: row `title` + `metadata.headline` PATCHed, `--retitle` pushed it to the CMS (was X → now adopted), sitemap synced.
4. **`publish.parse_draft(links=True)` on the re-titled artifact emptied the Related-reading block** — the internal-link scorer is title-sensitive: it had scored 1 of 480 ("Your Mower's 145-Minute Charge Trap", tokens aisle/trap) under the trap title, and after the retitle scored 0 of 480. Left empty deliberately (one incidental token "trap" was the fleet's known weak-evidence class; rule 12 says the section is absent when nothing qualifies) — the body keeps its earned inline link to /your-550-battery-spare-is-wrong/.
5. Re-synced the artifact's new lead into the row content, `wp_draft --refresh --refresh-live` (6082-char body), forced the wellroost rebuild from the CMS container. Reader: https://wellroost.com/your-899-blowers-9-day-window/ HTTP 200, `<h1>` = adopted title, new-lead phrase present, hero derivative + corrected alt served.

## Open items
- The Related-reading block ships empty on this page (scorer scored 0 under the adopted title); the hub link and the earned inline link carry the reader. Next `--refresh-live` re-scores it.
- verify.sh red on sibling rows >900 chars was fixed in-run by trimming both 2026-11-21 sibling cells (tinkering_tax, yard_robotics) with details preserved in their run_log files — mechanical, not editorial.
- verify.sh also red on pre-existing items: `test_illustration_overlay.py` (red since 2026-11-06) and legacy accessibility artifacts.
- Host ledger: egopowerplus.com, spearheadspade.com, shopping.yahoo.com, greenworkstools.ca fetched 200 (recorded); acehardware.com and acmetools.com 403 to plain curl (UNVERIFIED class).
