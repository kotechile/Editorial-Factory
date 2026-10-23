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

## 4. Output — the verified brief
Write `context/recon_proposals/YYYY-MM-DD_<vertical>_verified_brief.md`:
```markdown
# Verified Brief: <vertical> — YYYY-MM-DD
| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
```

## 5. Gate rules
- **A vendor's memory or capacity label is not its deployment envelope — verify the table, not the product name (learned 2026-10-20).** A model or box marketed at a round number fits that number only in the vendor's narrowest configuration. Observed: NVIDIA's Nemotron 3.5 Bolt ships as "the 24GB build", its research page sizes the architecture for "a footprint below 24 GB at batch size 1 and 128K context", and the model card's own deployment line reads "RTX discrete GPUs (32GB+ / 48GB+); 28GB and 32GB recipes below" — the label excluded the vision encoder, the speculative drafter and the context cache, so the card the label implied was four gigabytes short of the smallest recipe the vendor publishes. Extract the *envelope* (recipes, supported-hardware list, what the count excludes) beside the headline capacity, and check what hardware the benchmark number ran on: that run's 84 tokens a second came from a 128GB laptop, not the 24GB card the name implies. Apply the same test to any "runs on X GB" claim, to VRAM, and to a model's parameter count.
- Only **VERIFIED** claims survive into drafting; FLAGGED claims carry their caveat.
- **REMOVED claims are deleted**, not reworded into plausibility.
- **Dual-Anchor Gate:** In a synthesis brief, *both* Signal A and Signal B must have at least 2 VERIFIED claims. If either leg fails primary verification, the synthesis is deemed under-sourced; return to the Judge to test a different pair or single signal.
- ≥ 2 REMOVED → the topic is under-sourced; return to the Judge for a different angle.

## 6. Failure handling
Log removed-claim patterns (e.g. "aggregator cited a vendor figure without a link") to
`skills/self_improvement_eval.md` so future scouts prioritize primary sources up front.
