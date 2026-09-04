# SKILL: Claude Frontier Humanizer (Loop 3 — Final Rewrite)

## 1. Objective
The last pass before approval. Strip every AI-tell, inject cadence and a genuine human voice, and
iterate until every section passes its own gate. **Frontier model only (Claude).**

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

## 4. Per-section iteration (targeted — lead first)
Do NOT rewrite the whole piece and re-read it blindly. Iterate **section by section**, and only
re-iterate a section that fails its own gate. Order matters: **Lead first** — it decides whether
anyone reads on, so give it an extra check.

For each section, check its gate; if it fails, rewrite that section only and re-check (max 2
retries per section).

| Marker | Gate — it fails if… |
|---|---|
| `<!-- lead -->` | not a concrete incident/stat in the first 2 sentences; opens like a definition or "the world is changing". **Highest priority.** |
| `<!-- tension -->` | vague "the industry is evolving"; doesn't name what shifted and who it hurts/helps. |
| `<!-- tactical-insight -->` | generic advice ("invest in AI"); not one specific, doable move for the persona. |
| `<!-- nuanced-takeaway -->` | a hollow hedge or a cheerlead; not an honest limitation/counter-argument. |
| `<!-- tldr -->` | not exactly 3 scannable bullets; reads like a summary paragraph. |

After every section passes, run ONE final **whole-piece pass**: coherence, cadence, and confirm no
AI-tell or empty transition remains anywhere. Do not re-iterate sections that already passed.

## 5. Output
`context/drafts/YYYY-MM-DD_<slug>_final.md` (long-form + LinkedIn) with the per-section gate
report. Keep the **TL;DR as the structured `<!-- tldr -->` field** (3 bullets) — never write a
prose "in conclusion / key takeaways" paragraph. The **TOC is render-time only** — do not compose
one.

## 6. Failure handling
- Missing `ANTHROPIC_API_KEY` → halt with an explicit error; never substitute a non-frontier model.
- kie.ai upstream "Internal error, please try again later" (their documented instability — may surface as HTTP 502/503 **or 403**) → **retry up to 3 times with a short backoff before halting.** A transient gateway error is not a content failure — do not abandon a run over one flaky call.
- **`no_available_account`** (HTTP 200 with a JSON error body) is the same upstream hard-down class — halt Loop 3, do not substitute. A dated Anthropic model ID returns "page does not exist" — always request the alias (`claude-sonnet-5` / `Claude-Opus-4-8`), never a dated ID.
- **Non-streaming only:** kie.ai serves the Anthropic Messages protocol non-streaming. The stylist profile must set `model.streaming: false` — a streaming request returns an empty HTTP 200 (EmptyStreamError), which is config, not an outage. Routing is `provider: anthropic` + `model.base_url: https://api.kie.ai/claude`; `api.kie.ai` is whitelisted in Hermes's `_anthropic_base_url_override_ok` (runtime_provider.py).
- **Pre-flight before the rewrite:** hit `GET https://api.kie.ai/claude/v1/messages`-adjacent credit endpoint (`https://api.kie.ai/api/v1/chat/credit`, header `Authorization: Bearer *** key>`) AND a 1-token messages ping. Credit 200 + ping OK = gateway healthy; credit 200 + persistent "Internal error" = **gateway hard-down** — halt Loop 3 with an explicit upstream-status note, do not substitute a non-frontier model. A runnable pre-flight lives at `scripts/kie_healthcheck.sh` (exit 0 healthy / 1 hard-down / 2 key missing / 3 auth rejected).
- **Do NOT gate the pipeline at start on the gateway.** The radar sweep → judge → verify → draft all run on deepseek and are independent of kie.ai; their value is time-bound by the 30-day freshness window, so they must run on schedule even during an outage. A verified draft is never wasted — it holds at Loop 3 and finalizes the moment the gateway recovers. The pre-flight (`scripts/kie_healthcheck.sh`) gates only the rewrite, immediately before Loop 3 — never the sweep.
- **Auth convention (verified):** `Authorization: Bearer <kie.ai key>` and `x-api-key: Bearer <kie.ai key>` both authenticate. `x-api-key: <kie.ai key>` **without** the `Bearer ` prefix returns HTTP 200 with a `401 Unauthorized` body (a misleading status) — strip nothing, keep the `Bearer ` prefix.
- A section that fails its gate after 2 retries → report the specific section + criterion to the
  Editor, do not silently ship.
- Recurring AI-tells in drafts → log the tell + the fix to `skills/self_improvement_eval.md` so
  the Drafter stops producing it upstream.
