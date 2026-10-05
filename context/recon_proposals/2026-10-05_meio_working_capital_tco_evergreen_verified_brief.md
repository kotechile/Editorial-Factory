# Verified Brief: meio_working_capital_tco — 2026-10-05

Evergreen track. Claims extracted from
`context/recon_proposals/2026-10-05_meio_working_capital_tco_evergreen_brief.md` (which passed
`scripts/evergreen_gate.py`: 6/6 sources fetched on 6 hosts) and validated against each primary URL.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | Carrying-cost rate | Inventory carrying costs run 20% to 30% of inventory value a year for most businesses | VERIFIED | https://clearspider.net/blog/inventory-carrying-cost | "For most businesses, carrying costs range from 20% to 30% of inventory value annually, though this varies by industry, product type, and supply chain complexity." |
| 2 | Carrying-cost rate | Inventory holding costs run 20% to 30% of total inventory value annually (worked example lands at 25%) | VERIFIED | https://sourceday.com/blog/inventory-holding-costs | "Inventory holding costs typically range from 20% to 30% of total inventory value annually, depending on the business and industry." |
| 3 | Financing leg (cost of capital) | The bank prime loan rate is 7.00% | VERIFIED | https://www.federalreserve.gov/releases/h15 | "Bank prime loan … 7.00 7.00 7.00 7.00 7.00" (H.15 Selected Interest Rates, daily table) |
| 4 | Scale of the stock | Total US business inventories/sales ratio was 1.30 at end of July 2026; business inventories $2,764.7 billion | VERIFIED | https://www.census.gov/mtis/current/index.html | "The total business inventories/sales ratio based on seasonally adjusted data at the end of July was 1.30." / "…estimated at an end-of-month level of $2,764.7 billion…" |
| 5 | Expedited-freight leg | Global air cargo spot rates averaged USD 3.12 per kg in July 2026, up 28% year-on-year | VERIFIED | https://cargosolutionsnetwork.com/insights/air-cargo-spot-rates-july-2026-slowing-growth-no-peak-season | "Global air cargo spot rates averaged USD 3.12 per kg in July 2026, up 28% year-on-year but down 6% month-on-month." |
| 6 | Expedited-freight leg | Global air cargo spot rates reached $3.40 per kg in May 2026 (up 41% year-on-year); Taiwan–US lanes ran $7.02 per kg | VERIFIED | https://www.xeneta.com/blog/what-the-air-freight-market-looks-like-right-now-and-where-its-heading | "Global air cargo spot rates rose 41% year on year in May 2026, reaching $3.40 per kg…" / "In May 2026, air cargo rates from Taiwan to the US were running at $7.02 per kg, up 24% year on year." |

**Derived claim (arithmetic only, both legs VERIFIED):** with the financing leg at 7.00% [3] against a
fully-loaded rate of 20–30% [1][2], the borrowing rate is roughly a quarter to a third of the true cost
of holding, so a model fed only the borrowing rate under-costs a buffer by roughly 2.9–3.6×.

**Field note (internal, not a citable primary — used only as an anonymized illustration, from
`context/growth_os/customer-truth.md`, `meio_working_capital_tco` Anecdote 2):** a distributor holding
$2.5M of regional spare parts faced ~$575k/year in carrying cost versus ~$85k/year absorbing chartered
air freight on stockout events.

**Gate rules:** 6/6 claims VERIFIED, 0 FLAGGED, 0 REMOVED → topic is fully sourced; proceed to drafting.
