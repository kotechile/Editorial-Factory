# Run-log detail — 2026-11-26, home_ops_execution, winning-630500-buys-97-years-of-125-checks

## STEP 0 gate
`scripts/generation_gate.py --mode news --vertical home_ops_execution` → GENERATION OK (ok), control=supabase, vertical=file. Exit 0.

## Loop 1 — Radar
- Home Lifestyle Intel MCP sweep returned 10 candidates; 6 rows off-vertical (Ladybird alpha, Kagi Mail, datacenter munitions, MS outage, bread bags, Uber EVs) — dropped; kept drone-crash and heat-pump rows.
- 7 web queries: lien waivers, permitting reform (BAAJA, Oklahoma), heat-pump rates, contractor payment disputes, Maine AG contractors, Maine restitution. Window 2026-10-27 → 2026-11-26.
- Signals file: 7 rows, intensities 65–88. Host probes: wgme.com and maine.gov/ag fetched live (full text retained); mass.gov known-reachable; hklaw/canarymedia rows not promoted.

## Judge
- `synthesize_topics.py --seed` → rows=7 candidates=0 (no valid pair; legitimate). Judge proceeds single-anchor + standing-primary corroboration (Maine AG page).
- Winner N9.0/A9.0/S8.5 = 8.8 ≥ 8. De-dup vs 10-22 deposit, 11-05 liens/bankruptcies, 11-12 bond ceiling: none covers post-judgment collection.
- Runner-ups: MA/CMP heat-pump rates (service note), BAAJA (federal, indirect), Oklahoma study (no rule yet), drone crash (liability unresolved), Redfin HPI (index).

## Fact check
Dual anchors, both fetched 2026-11-26: WGME I-Team 2026-11-19 (court documents: $281k fixed price, $20k demand text, no vapor barrier, Timberline administratively dissolved, HCCA violations, $630,500+interest, $125/week, jail warning, first check in 6 months) and Maine AG Home Construction Contracts (unlicensed, top complaint category, written contract >$3k, deposit ≤1/3, written change orders, state's own collection failure). Derived arithmetic in-run: 630,500/125 = 5,044 wks = 97.0 yrs. Do-not-assert list written (no bankruptcy/fraud/interest-total claims).

## Draft → review
- Draft written with one earned inline link ([fixed no matter what the job costs](/your-contractors-bond-dies-at-25000/)), curl-verified 200.
- Review attempt 1 HELD: Flesch 42.4 (long-word diction) + undefined acronym "AG". Rewrote draft by hand: builder/pay-back/plain nouns, "the attorney general's office"; Flesch → 58.2.
- Attempt 2 HELD: figure 25000 lost from prose. Restored "$25,000 flat in California" [3]. At-a-glance reworded off the lead.
- Attempt 3 ACCEPTED (Flesch 58.2, 768 w).
- Post-acceptance gate repairs: voice "the lesson is" → "this case reads to me"; critic jargon "after the fact" → "too late"; By-the-numbers bullet "1/3 of the deal price + $93,666" two-figure lead-in → single-metric $93,666 bullet.

## Gates
`run_pipeline.py gate` → 8/8 PASS (accessibility, shape, critic, headline, sources, review_audit, voice, publish_gate).

## Persistence
- `scripts/publish.py` → published/2026-11-26_winning-630500-buys-97-years-of-125-checks.md; internal-links block inserted before ## Sources (3 links: Discredited Proof, Remodel Loses, Tools & Equipment hub); Supabase row da2e15eb-aeee-42d6-b91e-d6e716088c60 updated with enriched body; CMS post 488 status publish, kind tag news (term 28), vertical term 18, category 3 Tools & Equipment, featured media 487.
- Delivery verified: CMS 200; wellroost.com front initially 404 (static build in flight), 200 after ~2.5 min with Related reading + internal links + hero.
- Calendar row appended (≤900 chars).

## Open items
- Heat-pump winter rates (MA auto-enroll + CMP 13.63¢/kWh) held as strong evergreen candidate for the next evergreen run.
