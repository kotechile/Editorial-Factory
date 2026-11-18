# Run log — 2026-11-18 · warehouse_automation_robotics_capex (news) · your-vendor-exit-costs-373

**Outcome:** published → `published/2026-11-18_your-vendor-exit-costs-373.md` ("Your Vendor Exit Costs $373"), Supabase row `00b79a27-5538-4312-970d-c47fd46ee55f`, WordPress post **1772** on cms.giniloh.com (status publish, category 10 Supply Chain & Operations, vertical term 20, kind tag 43 `news`, featured media 1771). Live: https://aichieve.net/your-vendor-exit-costs-373/

## Window and sweep
Window 2026-10-19 → 2026-11-18. 26 inputs: one `supply_chain_intel` MCP pull (`--recent 30 --vertical warehouse_automation_robotics_capex --format signals`, 10 items, 1 kept — US Foods), 12 date-agnostic web fan-outs across the four `primary_angles` plus a standards/interop fan-out, 9 primary-document reads in full, 2 host probes (`witron.de` **403** to a plain fetch — the release is cited as reproduced verbatim by Logistics Business; `sellercentral.amazon.com` 200 but JS-rendered, so the trade brief stands in), 2 publisher date probes. **6 signal rows** kept at Intensity 68–92.

## Winner
Synthesis **9.0** (E=9.0 A=9.0 S=9.0) over the best single signal (ISO 21423 alone, 8.5 — N8.5/A9.0/S8.0) — margin 0.5, clears the §2.5 precedence rule.
- **Leg A:** A3 published **ISO 21423:2026** on 2026-11-02 — ISO TC 299; robots, fleet managers and other equipment exchange location, speed, direction, condition, tasking and availability; scope reaches lifts, doors, alarms, ERP and workers with mobile devices; **$373** list / **$320** members; A3's first non-safety robot standard. Lineage: MassRobotics 2020 working group → 2021 open-source standard → ISO WG 10, ~90 participants from a dozen+ countries.
- **Leg B:** Amazon's 2026-11-05 seller announcement, reported 2026-11-17 — the **3.5%** fuel and logistics surcharge extends from **2027-02-01** to transport fees for Multi-Channel Distribution and Warehousing & Distribution; FBA fees **+$0.19/unit** from 2027-01-15 (vs $0.08 at the start of 2026); storage utilization surcharge eliminated, aged-inventory charge folded into one age-based rate; Q3 shipping **+11% YoY, 3 pt fuel/linehaul**.
- **Collision:** substitution vs captivity. The owned half acquired a published, trivial route to substitution; the rented half acquired a published, open-ended escalator. Neither document states the comparison.
- **Friction (not an anchor):** Witron bought Solwr Robotics on 2026-11-17 — its release sells the Grab robot as joining "its own systems within a very short time and with minimal investment". Low entry, proprietary exit: the counter-move, and evidence the standard is not what vendors optimise for. **No price disclosed**; the article never states or computes one.

## Seeder
`rows=6 candidates=0` — recorded as an input, not a verdict. Rows 1/2 (standards doc) and 3 (a fee schedule) share no archetype token with the cost-driver/governance registry, the same blind spot `skills/virality_judge.md` §2.5 documents for a "when/threshold" axis. Judge asserted the pair by hand.

## De-dup
Excluded at anchor level, not scored: **Walmart⨂Symbotic $6bn / 25 RDCs** — published by this desk 2026-11-04 as `second-layer-has-no-unit-price`. Named in the brief: `your-71-margin-is-your-exit-bill` (2026-11-11, the seller's margin as the buyer's exit cost — this piece argues the *technical* substitution route against a *contractual* escalator, and the catch names the earlier reading rather than contradicting it). Own-vs-rent frame treated as spent (`owned-shuttles-or-rented-robots`, 2026-10-14). Sibling-front check: the fuel-surcharge pieces on aichieve.net (`2026-10-29_parcel-fuel-percentage-weekly-january`, `2026-11-13_your-carrier-hike-moves-your-carbon`) are USPS weekly percentage and carrier Scope 1/3 — not rented warehouse capacity; the draft does not re-argue the peg mechanics.

## Dropped at Stage 1
- Symbotic's Q4 date (2026-10-29) — carried as date only, never a leg.
- US Foods' "roughly the equivalent cost of one worker" — a CEO's qualitative comparison with no dollar figure; 7.9 as a candidate, kept out of the body.
- THG Fulfil / AutoStore CapEx-RaaS-hybrid (2026-11-11) — 7.8, restates the spent own-vs-rent question.
- Amazon robotic-unit layoffs / Blue Jay — March 2026, out of window.
- Interact Analysis outlook — undated page, outside the window as an event.
- `cellumation` (Symbotic sortation acquisition) — 2026-10-13, one day outside the window start.

## Fact check
14 claim rows: **13 VERIFIED, 1 FLAGGED** (the Witron purchase price: undisclosed — the brief bars stating or computing one), 0 REMOVED. Dual-anchor gate passed: leg A 5 VERIFIED on automate.org, leg B 6 VERIFIED on supplychaindive.com. Binding rulings that changed the copy: the $373 is the *document's list price*, never the cost of switching; the standard is explicitly **not** a safety standard (A3's own product page); the FBA size/price table is not blended into a per-unit rate; no vendor is named as having implemented it.

## Gates
Draft: accessibility PASS (Flesch 57.1), readability_critic ok, article_shape ok, voice OK (1,152 checks), headline 100/100 STRONG with `lead_ok` true. `run_pipeline.py gate --file` **8/8 ok**. Frontier (`deepseek-v4-pro`) attempt 1 reject (1 regression), attempt 2 ACCEPT; **hand repairs after the rewrite**: restored the inline internal link the rewrite stripped (it had flattened `[payback tool …](/tools/warehouse-slotting-payback/)` to plain text) and split a 7-sentence paragraph. Post-push `gate --slug`: see below.

## Persistence
`publish.py` — WordPress post 1772 (publish), featured media 1771, Supabase row, sitemap, published/, auto-deploy push. **Two defects found and repaired after the push:**
1. `internal_links.py` wrote a third Related-reading entry, "51% Test Traps Your Plant", justified by `topical overlap: november, published` — incidental tokens, the exact case AGENTS.md rule 12 forbids. Removed from `published/`, from the CMS body (REST PATCH, post 1772, 8,140 → 8,025 chars) and from the Supabase row (verified byte-identical to the CMS body). The two remaining entries (`your-seller-wont-stay`, `second-layer-has-no-unit-price`) are justified on category + ≥2 subject tokens.
2. The front 404'd for ~4 minutes after the push (`aichieve.net/your-vendor-exit-costs-373/` → 404, sitemap without the slug, `context/sitemap.json` entry `public: false`) while the CMS reported status publish. It was deploy lag from the auto-deploy push, not a delivery defect: 200 and present in `sitemap-0.xml` at 12:48 UTC. `cms.giniloh.com/?p=1772` still canonical-redirects to `giniloh.com/<slug>/` (404) while the same query for post 1769 goes to aichieve.net — a CMS admin-host quirk worth a look, since the reader front is unaffected.

## Lessons recorded
`scripts/learn.py` — see the host and pitfall entries written at the end of this run.
