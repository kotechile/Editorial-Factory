# SKILL: Claude Frontier Humanizer (Loop 3 — Final Rewrite)

## 1. Objective
The last pass before approval. Strip every AI-tell, inject cadence and a genuine human voice, and
critique-read until the draft passes the human-voice gate. **Frontier model only (Claude).**

## 2. Negative constraints (apply verbatim, no exceptions)
- No empty intros: "In today's fast-paced world", "In an era of", "It's no secret that".
- No hollow transitions: "Furthermore", "Moreover", "It's important to remember", "delve into",
  "dive deep", "let's explore", "In conclusion".
- No corporate sign-offs: "In summary", "ultimately, it's about", "the key takeaway is simple".
- No hedging filler: "some might argue", "it could be said", "interestingly enough".
- No adjective-stacking before nouns ("cutting-edge, revolutionary, game-changing").
- Preserve the lead incident/stat and the pragmatic takeaway — rephrase, never re-source.
- Preserve every citation `[n]` and the source list.

## 3. Voice rules
- Vary sentence length; short declaratives next to longer causal sentences.
- Prefer concrete nouns and named actors over abstractions ("the vendor cut latency" not
  "the industry optimized performance").
- One idea per paragraph. Kill any sentence that doesn't earn its place.

## 4. The critique loop (max 3 iterations)
After rewriting, read back as a hostile reader and score the human-voice gate:
1. Would a colleague believe a human wrote this? (yes/no)
2. Does the first sentence force you to keep reading? (yes/no)
3. Any AI-tell or empty transition remaining? (no = pass)
4. Is every number still cited? (yes = pass)

Any "no" → rewrite and re-read. After 3 failed iterations, report the specific failing
criterion to the Editor — do not ship.

## 5. Output
`context/drafts/YYYY-MM-DD_<slug>_final.md` (long-form + LinkedIn) with the voice-gate report.

## 6. Failure handling
- Missing `ANTHROPIC_API_KEY` → halt with an explicit error; never substitute a non-frontier model.
- kie.ai upstream 502/503 "Internal error, please try again later" (their documented instability) →
  **retry up to 3 times with a short backoff before halting.** A transient gateway error is not a
  content failure — do not abandon a run over one flaky call.
- Recurring AI-tells in drafts → log the tell + the fix to `skills/self_improvement_eval.md` so
  the Drafter stops producing it upstream.
