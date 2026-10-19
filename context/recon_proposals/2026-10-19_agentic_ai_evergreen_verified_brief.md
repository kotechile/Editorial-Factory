# Verified Brief: agentic_ai — 2026-10-19
**Topic:** the tool-call schema as a decoder input (evergreen, agentic_ai)
**Brief:** `context/recon_proposals/2026-10-19_agentic_ai_evergreen_brief.md` (gate PASS 2026-10-19T17:34:02+00:00, 8 rows, hosts arxiv.org + platform.openai.com)
**Persona:** ai_architect

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | single-signal (decode-side) | Claim 1 — a grammar engine refuses whole schema categories at compile time | VERIFIED | https://arxiv.org/html/2501.10868v1 | Failure type Outlines Llamacpp XGrammar Guidance Compile Error 42 37 3 25 Over-constrained 16 18 5 7 Under-constrained 8 7 38 1 Table 6 : Number of categories for which each failure type occurred at least once. |
| 2 | single-signal (decode-side) | Claim 2 — one engine under-constrains: it accepts invalid instances | VERIFIED | https://arxiv.org/html/2501.10868v1 | Failure type Outlines Llamacpp XGrammar Guidance Compile Error 42 37 3 25 Over-constrained 16 18 5 7 Under-constrained 8 7 38 1 Table 6 : Number of categories for which each failure type occurred at least once. |
| 3 | single-signal (decode-side) | Claim 3 — constrained decoding did not lower GSM8K accuracy in the benchmark's quality test | VERIFIED | https://arxiv.org/html/2501.10868v1 | Table 8 show that the constrained decoding, regardless of the framework, achieves higher performance than the unconstrained setting. Among the frameworks evaluated, Guidance consistently delivers the best performance across all tasks, with approximately a 3% improvement over the LM-only approach in every task. We believe this may be attributed to its token-healing implementation ( GuidanceAI, 2024a ) . Table 8 : Performance Percentages for Various Models Last Letters Shuffle Objects GSM8K LM only 50.7% 52.6% 80.1% XGrammar 51.2% 52.7% 83.7% Llamacpp 52.0% 52.6% 82.4% Outlines 53.3% 53.0% 81.6% |
| 4 | single-signal (decode-side) | Claim 4 — the benchmark's schema count and largest dataset | VERIFIED | https://arxiv.org/html/2501.10868v1 | GlaiveAI-2K Function Call 1707 Github-Trivial Misc 444 Github-Easy Misc 1943 Snowplow Operational API 403 Github-Medium Misc 1976 Kubernetes Kubernetes API 1064 Washington Post Resource Access API 125 Github-Hard Misc 1240 JSONSchemaStore Misc 492 Github-Ultra Misc 164 Total 9558 |
| 5 | single-signal (decode-side) | Claim 5 — field order set generation order, and reasoning fell | VERIFIED | https://arxiv.org/html/2408.02442v2 | Upon inspection, we found that 100% of GPT 3.5 Turbo JSON-mode responses placed the "answer" key before the "reason" key, resulting in zero-shot direct answering instead of zero-shot chain-of-thought reasoning. |
| 6 | single-signal (decode-side) | Claim 6 — clean parse, large accuracy gap | VERIFIED | https://arxiv.org/html/2408.02442v2 | In the LLaMA 3 8B setting, the parsing error rate for the Last Letter task in JSON format is only 0.148%, yet there exists a substantial 38.15% performance gap |
| 7 | single-signal (decode-side) | Claim 7 — enum-size ceiling in the vendor's schema subset | VERIFIED | https://platform.openai.com/docs/guides/structured-outputs | Limitations on enum size A schema may have up to 1000 enum values across all enum properties. For a single enum property with string values, the total string length of all enum values cannot exceed 15,000 characters when there are more than 250 enum values. |
| 8 | single-signal (decode-side) | Claim 8 — total schema string budget and the adherence comparison | VERIFIED | https://platform.openai.com/docs/guides/structured-outputs | Limitations on total string size In a schema, total string length of all property names, definition names, enum values, and const values cannot exceed 120,000 characters. |

## Drafter rulings

- The 38.15-point gap and the 0.148% parse-error rate belong to **one model on one task** (LLaMA-3-8B, Last Letter, JSON format) — never generalise them into a fleet-wide saving, and never subtract or ratio two source figures (no "halved the error" arithmetic).
- The 83.7% / 80.1% GSM8K pair is the JSONSchemaBench quality test and points the *opposite* way to the 2024 paper: when the schema leaves room for the working, constraining did not lower accuracy. Both readings must survive into the article; the reconciliation (field order and allowed working) is the thesis, not a source claim.
- "Twice as many" is the paper's own summary sentence for coverage spread; it carries no numeric token and is therefore prose-only, sourced to the same page.
- Vendor caps (250 enum values, 15,000 characters, 1,000 enum values, 120,000 characters) are the OpenAI Structured Outputs subset as retrieved 2026-10-19 — cite as a vendor ceiling, not as a standard.
- GPT-3.5 Turbo is the paper's own model; name it as the 2024 study's model, not as current practice.

## Removed claims

- None. No claim was reworded into plausibility; every figure above was fetched from its primary page on 2026-10-19.
