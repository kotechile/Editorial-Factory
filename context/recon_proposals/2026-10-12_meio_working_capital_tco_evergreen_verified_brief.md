# Verified Brief: meio_working_capital_tco — 2026-10-12

Evergreen track. Claims extracted from
`context/recon_proposals/2026-10-12_meio_working_capital_tco_evergreen_brief.md` (which passed
`scripts/evergreen_gate.py`: 6/6 sources fetched on 6 hosts, marker fresh at
2026-10-12T19:35:10+00:00) and validated against each primary URL.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | Tail size (velocity) | In a published distribution-center velocity analysis, C & D velocity SKUs are 67.76% of the SKU base, drive only 49.8% of unit activity, and hold 60.7% of on-hand units | VERIFIED | https://www.fortna.com/insights-resources/a-case-for-sku-management-the-implications-of-sku-proliferation | "The Bad: C & D velocity SKUs represent 67.76% of the total SKU base yet drive only 49.8% of the unit activity while accounting for 60.7% of the on hand units" |
| 2 | Head concentration | A & B SKUs are 16.54% of the SKU base, drive 50.2% of activity and hold 28.66% of on-hand units; E SKUs are 10.64% of units on hand and drive 0% of activity | VERIFIED | https://www.fortna.com/insights-resources/a-case-for-sku-management-the-implications-of-sku-proliferation | "The Good: A & B velocity SKUs represent 16.54% of the total SKU base yet drive 50.2% of the unit activity while accounting for 28.66% of the on hand units" / "The Ugly: E velocity SKUs drive 0% of the unit activity while accounting for 10.64% of the on hand units" |
| 3 | Tail size (count) | Of a 250,000-SKU retailer, nearly 10% were non-moving items and 10% were touched daily | VERIFIED | https://www.fortna.com/insights-resources/a-case-for-sku-management-the-implications-of-sku-proliferation | "SKU Analysis revealed that, of their 250,000 SKUs, nearly 10% were non-moving SKUs and 10% were touched daily." |
| 4 | Margin-blind case | A consumer-goods maker found 68 of its 156 SKUs (44 percent) generated only 8 percent of revenue, and the bottom 100 SKUs operated at a loss once fully loaded costs were applied; the top 25 SKUs produced 71 percent of revenue and 94 percent of profit | VERIFIED | https://lean6sigmahub.com/understanding-sku-proliferation-in-consumer-goods-how-to-recognize-the-challenge-before-it-becomes-a-crisis | "68 of their 156 SKUs (44 percent) generated only 8 percent of total revenue The bottom 100 SKUs collectively operated at a loss when fully loaded costs were applied Their top 25 SKUs generated 71 percent of revenue and 94 percent of profit" |
| 5 | Write-off trend | In the same case, obsolete-inventory write-offs rose 340 percent over five years and forecast accuracy outside the top 50 SKUs averaged only 42 percent | VERIFIED | https://lean6sigmahub.com/understanding-sku-proliferation-in-consumer-goods-how-to-recognize-the-challenge-before-it-becomes-a-crisis | "Forecast accuracy for products outside the top 50 SKUs averaged only 42 percent Obsolete inventory write-offs had increased by 340 percent over five years" |
| 6 | Dead-stock share | The average manufacturer carries 20-30% of its inventory as dead or obsolete stock — $600,000 to $900,000 that will eventually be written off on a $3 million inventory | VERIFIED | https://theassembly.io/blog/inventory-carrying-costs | "The average Canadian manufacturer carries 20-30% of its inventory as dead or obsolete stock. That's not a rounding error. That's $600,000 to $900,000 in parts that will eventually be written off on a $3 million inventory." |
| 7 | Health ceiling | Most successful businesses keep excess and obsolete inventory below 3% of total inventory value | VERIFIED | https://www.finaleinventory.com/guides/accounting-and-inventory-software/obsolete-inventory | "Most successful businesses aim to keep their excess and obsolete inventory below 3% of total inventory value – a critical indicator of inventory health." |
| 8 | Reserve ladder | Obsolescence reserve policy rises with age: 0-90 days 0%, 91-180 days 25%, 181-365 days 50%, 365+ days 100% | VERIFIED | https://qoblex.com/blog/how-to-identify-prevent-and-manage-obsolete-inventory-before-it-drains-your-profits | "Apply increasing reserve percentages based on how long inventory has been sitting: 0-90 days: 0% reserve 91-180 days: 25% reserve 181-365 days: 50% reserve 365+ days: 100% reserve" |
| 9 | Space share | The long tail takes up approximately 80% of warehouse space while accounting for 20% of revenue | VERIFIED | https://www.autostoresystem.com/insights/the-overlooked-80-why-your-slow-moving-skus-deserve-more-attention | "The long-tail items take up approximately 80% of warehouse space but account for 20% of revenue." |

**Derived claim (arithmetic only, both legs VERIFIED):** the tail holds 60.7% of on-hand units while
producing 49.8% of the activity [1] — about 22% more of the stock than of the work
(60.7 ÷ 49.8 = 1.22). Use only if labelled as arithmetic; do not present it as a source figure.

**Framing caveats the drafter must respect (recorded so the prose cannot overstate):**
- Row 6's share is stated by the source for the "average **Canadian** manufacturer". The article may
  use the dollar form (which is self-contained) or say "manufacturers" while keeping the source's
  frame; it must **not** claim the share is a global or US census measure. This is an industry
  reference, not government data.
- Rows 1–3 are one vendor's published client analysis, and rows 4–5 are a secondary write-up of a
  single consumer-goods case. Both are labelled as such in the brief; the article must attribute them
  ("one distribution center's velocity study", "one consumer-goods case") rather than present them as
  industry averages.
- Row 9 is a vendor claim (AutoStore sells automated storage). Attribute it or qualify it; do not
  state it as measured fact.
- Row 7 is a vendor/industry benchmark of an accounting target, not a measured industry rate.

**Verification method note (the gate's evidence excerpt is not the audit trail):** the gate's matcher
takes any numeric token in the figure cell, and four of the six rows initially matched a *navigation*
occurrence on the page (row 3 the page title, row 4 "3PL" in the industries list, row 5 a recovery-rate
table, row 6 the article title). Each claim was therefore re-confirmed inside its own sentence with a
surrounding-window extraction before drafting; the verbatim column above is that check. Rows 3 and 5
were re-cut to lead with a distinctive token ($600,000; 181-365 days) so the gate's own excerpt now
lands on the claim sentence.

**Field note (internal, not a citable primary — anonymized illustration only, from
`context/growth_os/customer-truth.md`, `meio_working_capital_tco` Anecdote 3):** a multi-brand apparel
retailer audited the bottom 30% of its slow-moving inventory; those items read positive on gross
margin but ran at a −18% net margin once pick travel time, pallet storage fees and annual markdowns
were counted. Pruning the bottom 2,400 SKUs lifted warehouse throughput 14% and freed 38,000 square
feet of racking. Carry it as the desk's own observation, never as a cited source.

**Gate rules:** 9/9 claims VERIFIED, 0 FLAGGED, 0 REMOVED → topic is fully sourced; proceed to
drafting. No `[NEEDS-SOURCE]` placeholders are required.
