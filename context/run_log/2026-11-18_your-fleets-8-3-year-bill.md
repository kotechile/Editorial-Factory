# Run-log detail — 2026-11-18 · warehouse_automation_robotics_capex · evergreen

Slug: `your-fleets-8-3-year-bill` · title "Your Fleet's 8.3-Year Bill: The Wave Nobody Reserves For"
Post 1785 on cms.giniloh.com (aichieve.net, category 10, vertical term 20, kind tag 44 'evergreen'),
media 1784, featured derivatives 150/300/768/1024/1536/2048 all present, og:image on the canonical media.

## Where the topic came from
The vertical's `primary_angles` (AMR fleet payback / lease / maintenance) crossed with the persona's
actual artefact — a capital plan. Lead material: the *mature* mobile-equipment fleet already in these
buildings (mmh 2026 Lift Truck Acquisition & Usage Study) set against the Warehouse/DC Operations
Survey 2026 and the BLS producer price index for the equipment class.

## Candidates considered and why three were refused
1. **Peak is a rental problem** (temps 17.3% of the peak workforce; FLSA 1.5× overtime) — refused
   after grep: `published/2026-11-11_your-robot-adds-a-12260-premium.md` already carries the temp
   share (16.6%) and the 1.5× workweek rule in its own body. Re-argue of a 7-day-old piece.
2. **The constraint moved to the dock** (shipping dock now most congested) — refused twice: the
   mechanism is already argued in `published/2026-11-05_your-port-clears-35688-boxes-dont.md`
   ("constraint moved from berth capacity to railcar supply"), and the headline figure (31%) collides
   with "31% 2024" earlier on the page, so it could not hold a clean gate row.
3. **Service-contract tail / battery mid-life capex** — refused for want of a fetchable primary price
   (vendor service pages unreachable or numeric-token-free), and battery overlaps 10-28.

## Gate
`evergreen_gate` PASS: 5 rows, 5 fetched, 3 sources, 2 hosts
(mmh lift-truck survey ×3 rows, mmh DC survey ×1, FRED/BLS PPI ×1).
Row-craft checks done with `citation_hub_dossier.figure_evidence` before the brief was written:
- `31%` (shipping dock) → matched "31% 2024" (case/split-case outbound) — DROPPED as a row, carried in prose.
- `6%` (pick area) → matched the slideshow's "1. 2. 3." — DROPPED; the 25% row's own excerpt prints 25/6/16/38.
- `44%` and `39%` on the 2025 survey → collided ("down from 44% last year", "30% to 39%") — DROPPED.
- `14%` (parts cannibalisation) → collided — folded into the 35% row's excerpt, which prints 39/38/35/14.
- Clean rows used: 8.3 years · 35% store · $182,290 · 13% square footage · 383.858 (PPI).

## Numbers in the article and how they were derived
- Wave = capex ÷ life spread annually vs the same capex in one year → ≈8.3× the annual charge at an
  8.3-year life (pure division, no third-party input).
- Stretch effect: 1/7.2 = 13.9%/yr → 1/8.3 = 12.05%/yr, a 13.3% cut in the annual charge.
- Index: 383.858 / 379.526 = +1.14% over four months (Jun→Oct 2026) → 1.0114^3 ≈ 3.46%/yr →
  1.0346^8.3 = 1.327, so the replacement is ~33% above the invoice; a reserve at the invoice covers
  ≈75% of it. Both derivations were recomputed in the terminal before drafting.

## Repairs after the frontier pass (ACCEPT, hard=0)
1. The rewrite dropped the inline internal link entirely → re-inserted
   `[which schedule that invoice lands in](/your-robot-budget-39-year-gap/)` (same site, same
   category, earned on the 39-year/QIP article; url returned 200).
2. The rewrite moved the money figure into `## At a glance` as well as the tension and By the
   numbers → three sections carried $182,290; the box line was replaced with the index figure.
3. `article_shape` held on "8.3 years restated in 3 sections (lead, tension, nuanced-takeaway)" →
   the closing paragraph now says "the measured average".
4. Art director's alt shipped as "Your Fleet'S 8.3-Year Bill. Fleet of identical…" (overlay headline
   glued to a clipped phrase, 2 sentences, broken capital) → repaired to one 118-char sentence across
   sidecar / both artifacts / media 1784 / Supabase illustration metadata by
   `scripts/fix_alt_fleetrenewal_1118.py`.

## Verification on the rendered front (not the push report)
`publish.py` printed "0 internal link(s)" on delivery, but `curl https://aichieve.net/your-fleets-8-3-year-bill/`
returned 200 (first attempt 404 — build lag, ~90 s) and the page carries the inline link to
`/your-robot-budget-39-year-gap/`, the Related-reading block, hero + all derivatives and og:image.
