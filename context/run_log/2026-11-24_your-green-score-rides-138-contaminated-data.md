# Run log — evergreen, ai_observability_qa, 2026-11-24

Topic: benchmark contamination — whether a green eval score may gate a release when the
test set sits in the model's training data. Fresh corpus-wide (grep "contaminat" in
published/ = empty), nearest prior vertical artifact `2026-10-27_your-green-passes-hide-31-wrong`
(test blindness) named and distinguished in the brief.

Anchors (gate PASS, 6 rows / 5 sources / 2 hosts):
- arXiv:2603.16197v1 — 13.8% MMLU contamination; 7.0 pp paraphrase drop
- arXiv:2405.00332v4 (GSM1k) — up to 8% mirror drop; HF papers abstract (host 2) — 13%
- arXiv:2606.03305 — 201 of 335 detector challenges solved
- arXiv:2410.05229v1 (GSM-Symbolic) — 21 of 25 models above paraphrased spread

Pipeline: draft held at Flesch 27/39 twice (rewrote by hand to 50.3), Loop 3 held at 49.5 +
2 dropped glosses → hand repair (casebook "adopt and repair"), final Flesch 50.6, all gates
PASS. Loop 3 emitted a self-graded `## Gate report` — stripped (review_audit hold).

Persistence: Supabase row dfe839d2, CMS post 1842 live (two-call publish, vertical term 12,
kind tag evergreen), Related-reading block generated (3 links), inline link
/100-case-eval-925-coverage/ (canonical verified 200). Illustration: document_flatlay on
flux-2 (5 credits), render review unavailable (frontier returned no text) — picture published
unchecked. Front build forced/in progress; hero to be verified on the rendered page.
