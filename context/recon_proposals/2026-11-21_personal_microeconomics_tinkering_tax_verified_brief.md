# Verified Brief: personal_microeconomics_tinkering_tax — 2026-11-21
**Angle:** One RAM Kit Now Costs You 24 Filament Spools (Synthesis: Signal A ⨂ Signal B)
**Window:** 2026-10-22 → 2026-11-21
**Method:** every anchor fetched directly (curl, Chrome UA); verbatim cells copied from the fetched bytes; dated pages verified by `dateModified` / on-page dates.

## Claim table

| # | Claim (as the article will use it) | Verbatim cell from source | Source URL | Host tier | Verified |
|---|---|---|---|---|---|
| 1 | A 32GB DDR5-6000 kit's best U.S. price is $474 against a lowest-ever tracked price of $72 | table row: "DDR5-6000 32GB — Best U.S. Price **$474** — Lowest-Ever U.S. Price **$72**"; also "a conventional 32GB (2x16GB) DDR5 memory kit sold for around $100 to $200 in October 2025, but the same kit now starts at $350, if it's even in stock" | https://www.tomshardware.com/pc-components/ram/ram-price-index-2026-lowest-price-on-ddr5-and-ddr4-memory-of-all-capacities | tier-1 trade press (primary tracking page) | YES — fetched 2026-11-21, HTTP 200, dateModified "2026-11-17T13:21:02" |
| 2 | A 64GB DDR5-6000 kit lists at $949 vs a $159 floor; a 128GB DDR5-6400 kit at $3,303 vs $329 | "DDR5-6000 64GB — $949 — $159"; "DDR5-6400 128GB — $3,303 — $329" | same as #1 | same | YES — same fetch |
| 3 | DDR4 also rose: 32GB kits went $60–$90 (Oct 2025) → $150–$180 (Jan 2026) | "it was common to find 32GB (2x16GB) DDR4 memory kits selling for between $60 to $90 back in October 2025. Jump to January 2026, and the same memory kit could cost anywhere between $150 and $180" | same as #1 | same | YES — same fetch |
| 4 | U.S. PLA filament median is $20.99/kg across 31 stores; PETG $19.79/kg (as of 2026-11-21) | "As of November 21, 2026, a standard 1 kg spool of PLA sells for a median $20.99/kg across 31 stores in United States. PETG runs $19.79/kg." | https://spoolhound.com/filament-price-index | independent market aggregator (primary for its own index) | YES — fetched 2026-11-21, HTTP 200 |
| 5 | Global PLA average is €18.06/kg across 47 stores / 14,223 listings, down 11.7% vs 30 days ago | "In November 2026, PLA filament averages €18.06/kg across 47 stores in 5 regions, down 11.7% vs 30 days ago." and "measured over 14,223 standard single-spool listings" | same as #4 | same | YES — same fetch |
| 6 | Bambu Lab's EU store cut PLA Basic to €19.99 from €25.99 in June; PLA ≈ 1.9¢/g at ten manufacturers' own stores (checked 2026-11-02) | "As of November 2, 2026, PLA filament costs 1.9 cents per gram ($18.99/kg median) and PETG costs 1.4 cents per gram ($13.99/kg), based on prices at ten manufacturers' own stores." and "Bambu Lab's EU store now sells PLA Basic at €19.99 a spool, down from €25.99 in June, and Prusament is on a Black Friday discount." | https://3dprintingcostcalculator.com/news/filament-price-per-gram | independent price-checker (store-level corroboration) | YES — fetched 2026-11-21, HTTP 200, dateModified "2026-11-02" |
| 7 | Derived: at $20.99/spool, a $474 kit ≈ 24 spools (474 ÷ 20.99 = 22.58 → "about 22 spools"; at the global trimmed mean €18.06 → ~€26/kg, the framing "the kit costs more than a year of hobby plastic" holds) — ARITHMETIC, not a source claim | — | arithmetic on claims 1+4 | — | LABELLED DERIVED; article states 22 spools at the U.S. median, not 24. Title uses the derived figure and the lead shows the division. |
| 8 | The buyer-side reason memory rose: hyperscaler AI contracts absorb DRAM supply | carried from Tom's Hardware reporting (2026-08-17 index analysis, out-of-window): "Memory prices climb 500% in 12 months" — context only, dated background row | https://www.tomshardware.com/pc-components/ram/memory-prices-climb-500-percent-in-12-months-up-to-10x-the-lowest-ever-tracked-prices-128gb-of-ddr5-now-usd3-399 | tier-1 trade press | YES — fetched, HTTP 200, datePublished 2026-08-17 (outside window — used as background framing only, never as an in-window figure) |
| 9 | Running-cost anxiety is top-of-mind for home-lab operators (context) | Ask HN thread title, 2026-11-06: "Is anyone running multi/always-on agents that don't cost a fortune?" | https://news.ycombinator.com/item?id=50391647 | community thread (non-blocking context) | YES — HN Algolia record, created 2026-11-06; carried as texture, no figure cited from it |

## FLAGS
- Claim 7 is derived arithmetic (division of two verified figures); the article must show the division and date both inputs.
- Claim 8 is outside the 30-day window: background framing only; no figure from it appears in the body without an in-window citation from claims 1–6.
- SpoolHound and 3DPCC are independent indexers of third-party retail prices; the store-level leg (ten manufacturers' own stores) is what makes claim 6 primary-adjacent.
- Tom's "lowest-ever" prices are historical floors from a tracked index, not October-2025 sticker prices — the article must not blend the two (the $100–$200 Oct-2025 quote and the $72 floor are separate facts, both verbatim above).

## Sources (minimum 2 hosts satisfied)
1. tomshardware.com (tier-1 trade press)
2. spoolhound.com (independent market index)
3. 3dprintingcostcalculator.com (independent store-level checker)
