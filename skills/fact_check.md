# SKILL: Fact Verification (Loop 2 — Zero-Hallucination)

## 1. Objective
Convert the angle brief into 3–5 checkable claims and validate each against a **primary source**
before any drafting happens.

## 2. Claim extraction
A claim is a concrete, checkable statement: a number, benchmark, quote, ship date, policy change,
funding figure, or a named decision. Reject vague claims ("AI is transforming X") — they are not
checkable and do not belong in the brief.

**For Multi-Topic Synthesis Briefs:**
- Extract 2–3 load-bearing claims from **Signal A (Anchor 1)**.
- Extract 2–3 load-bearing claims from **Signal B (Anchor 2)**.
- Extract any relational/comparative claims bridging the two (e.g., cost-benefit ratios, timeline overlaps).
- Ensure both anchors independently trace to legitimate primary records.

## 3. Validation protocol
For each claim:
1. Fetch the primary URL. **Primary** = origin (paper, vendor changelog, regulator, court filing,
   earnings call transcript). Secondary writeups are corroboration only, never the source of record.
2. Record the verbatim quote or figure and the exact URL.
3. Assign status:
   - **VERIFIED** — matched to a primary source.
   - **FLAGGED** — partially supported or a conflict found; record the discrepancy.
   - **REMOVED** — no retrievable source; delete the claim.
4. **When a source carries both a data table and a prose gloss of it, the table is the claim of record.**
   Survey releases and reports routinely round or misstate their own numbers (observed: a survey whose
   prose said "54% of those building with AI replace vendors" while its own table gave 54.4% *of the
   vendor-replacers* using AI). Extract from the table, check the arithmetic (count ÷ base), record the
   discrepancy in the Verbatim cell, and tell the drafter not to repeat the prose gloss.
   A statistical agency's release and its own data table disagree too (observed 2026-10-12: the EIA's
   October 2026 Winter Fuels Outlook release says "the forecast 30% increase in heating oil prices"
   while the outlook's own heating-oil table gives a **+34%** price change and a +21% expenditure
   change). Quote the table, and write the divergence into the verified brief so the drafter cannot
   pick up the release's number by accident.
 5. **A program's own FAQ can contradict itself across sections — record the discrepancy, never reconcile it and never
 quote the smaller aggregate as a total (learned 2026-10-23).** California's Demand Side Grid Support program page
 says "up to $26.9 million of DEBA Program funds may be used to support the DSGS Program in the 2026 program season"
 in one answer and "up to $42.7 million is available to fund Option 3 performance-based capacity payments" in the
 next — a pool larger than the fund it is said to draw on. Both are the administrator's own words, so neither is
 wrong to cite; what is wrong is merging them into "$26.9M total". Write the Option 3 figure as the Option 3 pool,
 carry the DEBA line separately, and put the inconsistency in the brief as a FLAGGED row so the drafter cannot
 quietly total two numbers the source never totals. The same test catches a statute authorising a program to 2032
 beside an appropriation that funds one season: cite both, and never report the first as funding.

5. **A .gov page can be stale in one language and current in another — check the alternate locale before trusting either (learned 2026-10-28).** FEMA's English NFIP reauthorization page still read that Congress "must now reauthorize the NFIP by no later than 11:59 p.m. on Sept. 30, 2026", while the Spanish version of the same page, the CRS product and NAR's FAQ all gave Dec. 11, 2026 under P.L. 119-103 signed Sept. 2, 2026. Neither page is wrong to cite — they are the same page at two vintages — but a run that reads only the English one builds a deadline story on a date that has already passed. When a statutory or authorization date is load-bearing, read the page's other locale (`/es/…`), the enforcing agency's product, and one trade record, and put the divergence in the brief as a FLAGGED row so the drafter never prints the superseded date.

## 4. Output — the verified brief
Write `context/recon_proposals/YYYY-MM-DD_<vertical>_verified_brief.md`:
```markdown
# Verified Brief: <vertical> — YYYY-MM-DD
| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
```

## 5. Gate rules
- **A repair price is configuration-specific — pin the model, the case and the service tier before you compare it to a device price (learned 2026-10-23).** A manufacturer's out-of-warranty list prices the same labour differently by case material and connectivity, and a teardown's summary of it can flatten that away. Observed: iFixit read $599 for "any other service" on an Apple Watch Series 12 with GPS and Cellular and set it against a $399 aluminum watch, while MacRumors' read of the same list put a cellular aluminum model of the same size at $349 and the $599 on the ceramic case (from $899). Both readings are of one source, both are quotable, and only one supports "the repair costs more than the device". Extract the (model, case, service tier) triple with every repair price, carry the cheaper configuration beside it in the brief as a FLAGGED row, and bar the drafter from generalising the figure to the whole product line. The generalisable claim is usually the *spread* — same failure, same labour, a different case price — not the single high number.
- **A vendor's memory or capacity label is not its deployment envelope — verify the table, not the product name (learned 2026-10-20).** A model or box marketed at a round number fits that number only in the vendor's narrowest configuration. Observed: NVIDIA's Nemotron 3.5 Bolt ships as "the 24GB build", its research page sizes the architecture for "a footprint below 24 GB at batch size 1 and 128K context", and the model card's own deployment line reads "RTX discrete GPUs (32GB+ / 48GB+); 28GB and 32GB recipes below" — the label excluded the vision encoder, the speculative drafter and the context cache, so the card the label implied was four gigabytes short of the smallest recipe the vendor publishes. Extract the *envelope* (recipes, supported-hardware list, what the count excludes) beside the headline capacity, and check what hardware the benchmark number ran on: that run's 84 tokens a second came from a 128GB laptop, not the 24GB card the name implies. Apply the same test to any "runs on X GB" claim, to VRAM, and to a model's parameter count.
- **A severity score belongs to one link in a chain, and the aggregator's per-CVE gloss disagrees with the vendor's sentence by design (learned 2026-10-24).** On the Plex2Shell brief, CISA's KEV entry for the 8.6 file-write stage read "can allow an admin user to write arbitrary files" and NVD's own vector carries `PR:H`, while Plex's advisory says "Chained together, these issues let an unauthenticated remote attacker run code" — all three true, because the chain supplies the privilege the single link needs. Quote the *vendor's chain sentence* for "unauthenticated" and never attach the score to that word; the press's 8.6 is the CVSS 4.0 base (the 3.1 base of the same CVE is 7.2), so say which version the number is on. Two siblings from the same run: KEV's own `dateAdded` field is the source of record (a threat-intel blog dated the addition a day later — the registry wins), and a ">36,000 exposed" scanner count is a dated snapshot from one scan (Shadowserver, 2026-09-09), never a current count and never a count of *compromised* hosts.
- Only **VERIFIED** claims survive into drafting; FLAGGED claims carry their caveat.
- **REMOVED claims are deleted**, not reworded into plausibility.
- **Dual-Anchor Gate:** In a synthesis brief, *both* Signal A and Signal B must have at least 2 VERIFIED claims. If either leg fails primary verification, the synthesis is deemed under-sourced; return to the Judge to test a different pair or single signal.
- ≥ 2 REMOVED → the topic is under-sourced; return to the Judge for a different angle.

## 6. The floor is code, at the push (`scripts/source_gate.py`)

The verification above is done by the run, but a run that skips or fumbles it must not be able to
publish anyway. `scripts/publish_gate.py` therefore calls `scripts/source_gate.py` on the artifact
immediately before the push, and an article that fails is created as a CMS DRAFT instead of a live
post (owner, 2026-10-23). What it enforces, mechanically:

1. **Every cited URL resolves** — a 404/410 is a failure. A bot wall (403/429/timeout) is reported as
   UNVERIFIED, never as wrong: Reuters answers 403 to any scraper while a reader opens it fine.
2. **The page is the document it is cited as** — the citation's own numbers (a statute section, a
   report id) or its distinctive words must appear on the page, taken from the URL path when the
   Sources line is a bare URL. A path that collapsed to the site's root is the classic failure.
3. **No aggregator, mirror, social post or tertiary wiki** stands in for the origin it repeats
   (`context/source_quality.json` `blocked_hosts`), and a sources list of press-release wires alone
   is not corroboration.
4. **Not one host counted as several** — `min_sources` distinct citations across `min_hosts` hosts.
5. **Every figure in the body that appears in no cited source is listed** for the reviewer; pass
   `--strict-figures` to make that list a hold. Derived arithmetic (a spread, a sum, an interval)
   legitimately never appears in a source, which is why it is a list and not a default hold.

**A 404 is not always a dead citation either — some hosts answer the desk's User-Agent with 404 while serving the page to a browser (learned 2026-10-29).** `about.usps.com` returned **404** for three of
its own newsroom releases to the gate's `Python-urllib` User-Agent and **200** to a Chrome User-Agent,
and the gate's status-only rule held the article as a DRAFT for citations a reader opens fine. The
distinction that matters is the one the gate already makes for 403s: a *reader-openable* page is not a
broken one. `source_gate.fetch` now retries a 404/410/451 once with `BROWSER_UA` and, when the retry
serves, classifies the page as ok with the retry recorded in the report (`— bot-walled, not dead`); a
genuinely dead path stays 404 under both User-Agents and is still held, and `--self-test` still pins
all five hold classes. Two consequences when a `.com` subdomain of a government agency is cited:
`about.usps.com` never matches the `.gov` primary-suffix rule, so it must be listed in
`context/source_quality.json` `primary_hosts` (done for `usps.com` / `ups.com`) or every such citation
reads "no PRIMARY host".

Sources that are only partly checkable (JS shells, paywalls, PDFs with no text layer) are reported
as UNVERIFIED, not passed — the gate never claims a check it did not run.

## 7. Failure handling
Log removed-claim patterns (e.g. "aggregator cited a vendor figure without a link") to
`skills/self_improvement_eval.md` so future scouts prioritize primary sources up front.
