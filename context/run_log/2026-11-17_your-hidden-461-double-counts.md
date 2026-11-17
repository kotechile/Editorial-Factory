# Run log — control_tower_exception_orchestration — 2026-11-17 (`your-hidden-461-double-counts`)

**Track:** news · **Window:** 2026-10-18 → 2026-11-17 · **Persona:** supply_chain_architect ·
**Front:** aichieve.net · **Queries:** 24 (12 web fan-outs, 5 primary fetches, 1 supply_chain_intel MCP
pull of 10 generic items — none on beat, 1 GSC export returning 0 opportunities, 1 WP date probe, 3
verification fetches)

## Winner and scoring

`your-hidden-461-double-counts`, published as **"Your Hidden 461 Double Counts"** — **Single-Signal,
9.0** (N 9.0 / A 9.5 / S 8.5). Anchor: Sea-Intelligence's own correction press release of **7 November
2026** (https://www.sea-intelligence.com/press-room/419-glp-correction), which discloses that aggregated
alliance schedule-reliability figures had double-counted a subset of vessel arrivals since **April 2015**
— eleven years unnoticed by the publisher and by the alliance carriers receiving the raw data. Carrier
and trade scores were unaffected; only the aggregates. 461 calls affected = 2.28% of all alliance calls
Feb 2025–Sep 2026. The correction flips the Aug/Sep 2026 ranking: published MSC 68.9% / Gemini 68.4% /
Ocean 44.8%, corrected Gemini 70.4% / MSC 69.5% / Ocean 44.9% — a 1.4-point reversal (desk arithmetic,
labelled as such) against a published 0.5-point margin.

## Synthesis decision (§2.5 precedence)

The paired candidate was **the correction ⨂ Shipzil's cross-platform FedEx monitor** (162
carrier-affecting incidents, 90% reported by only one of four platforms run by three companies; 29% of
incidents with the carrier inferred from a title; uptime "as reported by the platforms, not
independently measured"; recorded totals 82/44/25/11). Scored E 9 / A 8 / S 9 → **8.7**, which does not
beat the 9.0 single signal by the 0.3 margin, so the piece publishes as a **single-signal document
analysis** with Shipzil carried as corroboration for the same failure class in the live feed. The draft
therefore carries **no `synthesis: true`**, and Supabase `metadata.synthesis` reads `None`. Seeder
(`synthesize_topics.py --seed`) returned **rows=7 candidates=0** — two measurement systems share no
archetype token; recorded as input, not a verdict.

## Runner-ups dropped

- **project44 Hormuz Week 34** — 7.6; carried as the positive example of a *disclosed* baseline
  (TSP dwell +12% to +59% against 5 Jan–23 Feb; Jebel Ali export 26.8 vs 8.5 days).
- **USPS 2027 rates with a permanent fuel surcharge (5.9%, 2027-01-17)** — 7.9; the fuel-surcharge half
  is a sibling-vertical retread (`supply_chain`, 2026-10-29), and a rate table is pricing, not
  orchestration.
- **Samsara Agent Studio / 7x adoption** — 7.4, dated 2026-10-13, five days before the window.
  **Descartes OpsForce** — its FreightWaves write-up is **2026-01-30** (WP `date` probe) and the launch
  2026-03-04; outside. **FourKites' Magic Quadrant withdrawal** — 2025-02-24.
- **Cold chain / LA-LB dwell / DCSA 3.0.0** — already published 2026-11-03 and 2026-10-20.

## De-dup

Prior 30 days inside the vertical (11-03 cold chain, 11-03 nine-day queue, 11-10 entry gap, 10-27 miss
cost and ETA, 10-20 feed and exception log, 10-19 exception bill) argue costs, queues and deadlines, not
how a count is assembled. Same-source caution answered: `2026-10-13_shippers-stuck-in-the-gap` used
Sea-Intelligence for the *level* of reliability 35 days ago; this piece deliberately does not argue the
level (50.6% appears once, as the report it dates). All four sibling verticals publishing to aichieve.net
on 2026-11-17 are software-operations beats with no shared event or figure.

## Fact check

`2026-11-17_control_tower_exception_orchestration_verified_brief.md`: **20 rows — 18 VERIFIED, 1
DERIVED, 0 REMOVED**. Binding rulings that shaped the copy: print the publisher's own characterisation
("minimal … barely discernible in most months"); state that carrier and trade scores were untouched; every
Shipzil uptime figure carries "reported", never "measured"; the 162-incident total has no stated period so
it is never presented as a 90-day count (the 90-day series is 2/10/5/1); the 1.4-point reversal is desk
arithmetic. `sea-intelligence.com`, `shipzil.com` and `project44.com` were registered in
`context/source_quality.json` `primary_hosts` (each is the origin of the measurement it publishes).

## Gates

Draft → `readability_critic` ok (no advisories), `check_accessibility` PASS (Flesch 59.0), `article_shape`
ok, headline **100/100 STRONG** with `lead_ok` true. Two pre-tune repairs: "MSC" glossed as the
Mediterranean Shipping Company (MSC), and a 7-sentence paragraph split. **Frontier pass**
(`run_pipeline.py review`, deepseek-v4-pro): **attempt 1 ACCEPT**, hard=0, regressions=0, rhythm 7.0→6.9,
health 0.816→0.797, Flesch 59.5, 862 words. The rewrite kept the structure but **dropped the earned
inline link** and left one verdict-framing phrase ("the lesson is", held by `check_social_voice.mjs`);
both repaired by hand, plus two wording fixes ("the publisher's two sentences" repeated; "follows" →
"applies to"). Final gate battery on the artifact: accessibility, shape, critic, headline, sources,
review_audit, voice, publish_gate — **all 8 green** (Flesch 58.9, 856 words, target 60 advisory).

## Persistence

`published/2026-11-17_your-hidden-461-double-counts.md` (`kind: news`, no synthesis flag). Supabase article
**df1b812c-be18-49d2-8d42-071413d6878f** (HTTP 201, links written back to the row so DB and CMS agree).
WordPress post **1746** on cms.giniloh.com — status **publish**, category 10 (Supply Chain & Operations),
vertical term 25, kind tag **43 (news)**, featured media **1745**, 7,169-char body, 4 site-relative hrefs
including the earned `/your-exception-log-owes-5-years/`, Sources heading present, 160-char excerpt —
read back over REST with an app password. Featured image: `long_lens_industry` on flux-2/pro-text-to-image,
5 credits, 2,400×1,350 — an unbranded container ship doubled by its reflection in the dock basin, overlay
legible, no brand mark (pixels read with vision).

**Two defects found and fixed in-run.** (1) The director's alt text arrived as the overlay copy ("The 461
Double Counts. Unbranded container ship …"), so it was retyped to a 115-character sentence and reconciled
across the sidecar `featured.json` (revision 3), the artifact's `image_alt`/`image_caption`, media **1745**
(REST PATCH, read back) and the row's `metadata.illustration.alt_text` / `metadata.wordpress.media_alt`.
(2) The reader front answered **404** for ~10 minutes after the push; the CMS `transition_post_status`
rebuild was fired with a draft→publish toggle on post 1746, after which
https://aichieve.net/your-hidden-461-double-counts/ answered **200** with its own `<h1>`, 11 upload
references, the earned inline link and a matching `og:image`.

## Open items (reported, not hand-fixed)

- `publish.py`'s delivery line still prints "0 internal link(s)" for relative hrefs — the documented
  false alarm; the CMS body carries 4.
- `internal_links.py` generated the Related-reading block on weak tokens (one hint reads "topical
  overlap: november"); left as generated because the body's inline link is the earned one.
- `check_social_voice.mjs` still reds the repo on 5 pre-existing drafts from earlier runs; this artifact
  is clean.
- Flesch 58.9 against the 60 target (floor 50) — carried by the sources' own nouns (alliance,
  reliability, transshipment).
- No social distribution and no LinkedIn/Reddit copy (channel removed 2026-10-06).
