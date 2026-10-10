# Verified Brief: supplier_risk_reshoring_decision — 2026-10-10

**Archetype:** evergreen (Loop 1E) — the news gate does not run here. Evidence floor cleared by
`scripts/evergreen_gate.py` (4 rows fetched, 4 verified, 4 hosts) before this brief was written.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| C1 | Drawback — the refund | Drawback is the refund of certain duties, internal revenue taxes and fees collected on import, paid back when the merchandise is exported or destroyed; authority is 19 U.S.C. 1313 / 19 CFR 190 (title 19 of the Code of Federal Regulations). | VERIFIED | https://www.cbp.gov/trade/programs-administration/entry-summary/drawback-overview | "Drawback is the refund of certain duties, internal revenue taxes and certain fees collected upon the importation of goods and refunded when the merchandise is exported or destroyed. Please refer to 19 CFR 190." |
| C2 | Drawback — the cap | The amount of drawback allowable will not exceed 99 percent of the amount of duties, taxes and fees paid on the imported merchandise. | VERIFIED | https://www.ecfr.gov/current/title-19/chapter-I/part-190 | "The amount of drawback allowable will not exceed 99 percent of the amount of duties, taxes, and fees paid with respect to the imported merchandise." |
| C3 | Drawback — substitution + window | The refund is set by statute at 99 percent of the duties, taxes and fees paid; substitution allows a duty-paid import to be matched to an exported or destroyed article classifiable under the same 8-digit HTS subheading, within a period not to exceed 5 years from the date of importation. | VERIFIED | https://www.law.cornell.edu/uscode/text/19/1313 | "…shall provide for a refund of equal to 99 percent of the duties, taxes, and fees paid on the imported merchandise…"; "…classifiable under the same 8-digit HTS subheading number as such imported merchandise is used in the manufacture or production of articles within a period not to exceed 5 years from the date of importation…" |
| C4 | Drawback — trade-remedy duties | Section 301 and Section 201 duties are claimable for drawback (the filer reports both the Chapter 99 and the 1–97 HTS numbers for each line). | VERIFIED | https://www.cbp.gov/trade/programs-administration/entry-summary/drawback-overview | "As a reminder, for all drawback provisions claiming Section 301 and/or 201 duties, the filer must report both the Chapter 99 and the 1 - 97 HTS numbers, along with the QTY and Value for each line item…" |
| C5 | Drawback — the carve-out | Recovery is program-by-program: Section 232 (steel/aluminum/copper) and certain IEEPA-based duties are generally excluded from drawback, so "up to 99%" is real but not universal. **Vendor claim, dated by the source's own review date (June 2026) — carry the caveat, do not present as statute.** | FLAGGED (vendor claim) | https://borderless.us/blog/duty-drawback-2026 | "Some tariff programs are drawback-eligible. But key 2025–2026 programs are not. Notably, Section 232 (steel/aluminum/copper) and certain IEEPA-based duties are generally excluded from drawback." (page: "Last reviewed June 2026") |
| C6 | Field anchor (internal) | The desk's own field notes: a casting quoted at $18/unit offshore landed at $24.80/unit once freight, demurrage and audit travel were counted, against $21.50 nearshored; and a mid-sized importer took a retroactive $1.2M duty bill after a customs reclassification. | INTERNAL (house field notes, no external URL — `context/growth_os/customer-truth.md` Anecdotes 1 and 6) | context/growth_os/customer-truth.md | "raised the true landed cost to $24.80/unit … Nearshoring production to Monterrey, Mexico cut transit times from 42 days to 4 days at $21.50 landed cost"; "A mid-sized importer faced retroactive $1.2M duties because customs reclassified an electronic component under a different HTS code" |

**Evidence floor:** 4 external primary sources across 4 hosts (cbp.gov, ecfr.gov, law.cornell.edu,
borderless.us), each fetched and shown to contain the figure it is cited for. 1 FLAGGED (C5, a vendor
claim carrying its own review date). Nothing REMOVED.

**Drafter notes:**
- The load-bearing claims are C1–C4 (statute, regulation, and the issuing agency). C5 is the honest
  limitation and must be labelled as the vendor's reading with its date, never as the statute.
- Expand every acronym at first use: CBP, HTS, CFR, IEEPA, and trade-remedy section numbers get a
  plain-English gloss ("Section 232" → the steel, aluminum and copper tariffs).
- Do not state that drawback recovers "all" tariffs — the whole point of C5 is that it does not.
- C6 is the desk's own field case: use it as an illustrative composite, labelled as such, with no
  `[n]` citation. Never attach a customer-truth anecdote to an external source list.
- The decision this settles is not "reshore or not" — it is "net the recoverable duty out of the
  reshoring case before crediting the move with a saving". Reshoring still buys lead time and lower
  concentration risk; it just does not buy back a duty that was already refundable.
- No new figure may appear that is not in this table or the frontmatter (`skills/claude_humanizer.md`
  §7 post-rewrite audit).
