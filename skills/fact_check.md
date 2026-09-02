# SKILL: Fact Verification (Loop 2 — Zero-Hallucination)

## 1. Objective
Convert the angle brief into 3–5 checkable claims and validate each against a **primary source**
before any drafting happens.

## 2. Claim extraction
A claim is a concrete, checkable statement: a number, benchmark, quote, ship date, policy change,
funding figure, or a named decision. Reject vague claims ("AI is transforming X") — they are not
checkable and do not belong in the brief.

## 3. Validation protocol
For each claim:
1. Fetch the primary URL. **Primary** = origin (paper, vendor changelog, regulator, court filing,
   earnings call transcript). Secondary writeups are corroboration only, never the source of record.
2. Record the verbatim quote or figure and the exact URL.
3. Assign status:
   - **VERIFIED** — matched to a primary source.
   - **FLAGGED** — partially supported or a conflict found; record the discrepancy.
   - **REMOVED** — no retrievable source; delete the claim.

## 4. Output — the verified brief
Write `context/recon_proposals/YYYY-MM-DD_<vertical>_verified_brief.md`:
```markdown
# Verified Brief: <vertical> — YYYY-MM-DD
| # | Claim | Status | Source URL | Verbatim |
|---|-------|--------|-----------|----------|
```

## 5. Gate rules
- Only **VERIFIED** claims survive into drafting; FLAGGED claims carry their caveat.
- **REMOVED claims are deleted**, not reworded into plausibility.
- ≥ 2 REMOVED → the topic is under-sourced; return to the Judge for a different angle.

## 6. Failure handling
Log removed-claim patterns (e.g. "aggregator cited a vendor figure without a link") to
`skills/self_improvement_eval.md` so future scouts prioritize primary sources up front.
