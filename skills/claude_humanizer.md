# SKILL: Frontier Humanizer (Loop 3 — Final Rewrite)

## 1. Objective
The last pass before approval. Strip every AI-tell, inject cadence and a genuine human voice, and
iterate until every section passes its own gate. **Frontier model only.** The frontier is whatever
the `stylist` profile is configured to (see §6). Current live config: `gemini-3.1-pro-preview`
(`provider: gemini`). Restore Claude/kie.ai only when a valid key exists — never downgrade to a
non-frontier model.

## 2. Negative constraints (apply verbatim, no exceptions)
- No empty intros: "In today's fast-paced world", "In an era of", "It's no secret that".
- No hollow transitions: "Furthermore", "Moreover", "It's important to remember", "delve into",
  "dive deep", "let's explore", "In conclusion".
- No corporate sign-offs: "In summary", "ultimately, it's about", "the key takeaway is simple".
- No hedging filler: "some might argue", "it could be said", "interestingly enough".
- No adjective-stacking before nouns ("cutting-edge, revolutionary, game-changing").
- Preserve the lead incident/stat and the pragmatic takeaway — rephrase, never re-source.
- Preserve every citation `[n]` and the source list.
- Preserve each section's distinct, brief-sourced action items — do not merge or drop a section's
  numbered moves (the persona's doable steps are the point; note the draft's per-section content).
- Only VERIFIED-brief figures may appear; no secondary-derived sums (e.g. a "net" figure computed
  from two press-release numbers). If a figure is not a verbatim line in the verified brief, it
  stays out or is flagged `[NEEDS-SOURCE]` — never pulled from a secondary write-up.
- After the rewrite, compare the final body length to the draft/floor (~800 words). If the frontier
  compacted it materially below the draft, restore depth from the verified brief (restate the moves
  / tension), never pad new claims.

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
- **Use the frontier the `stylist` profile is configured to** — do not hard-code a provider. Read the
  profile's `model.default`/`provider` (current live: `gemini-3.1-pro-preview` / `gemini`, `base_url: ''`).
  The rewrite must run on that frontier. Never substitute a non-frontier model.
- **Pre-flight before the rewrite:** verify the configured frontier is reachable (e.g. a 1-token
  `generateContent` ping to the profile's provider). If the frontier is unavailable **and** it is the
  only viable frontier, hold the verified draft at Loop 3 with an explicit upstream-status note — a
  verified draft is never wasted; it finalizes when the frontier recovers. Do not silently fake a rewrite.
- **Do NOT gate the pipeline at start on the frontier.** rada sweep → judge → verify → draft all run on
  deepseek and are independent of the frontier; their value is time-bound by the 30-day freshness window,
  so they must run on schedule even during an outage. The pre-flight gates only the rewrite, immediately
  before Loop 3 — never the sweep.
- **kie.ai / Claude note (historical):** when the frontier was Claude via kie.ai, routing was
  `provider: anthropic` + `base_url: https://api.kie.ai/claude` (non-streaming only, `model.streaming: false`,
  alias model IDs like `claude-sonnet-5`). That key is currently **auth-rejected (HTTP 401)** — do not use it.
  The working frontier is Gemini until a valid Anthropic/kie.ai key is restored. `api.kie.ai` is whitelisted
  in `_anthropic_base_url_override_ok` (runtime_provider.py) if it is re-enabled.
- A section that fails its gate after 2 retries → report the specific section + criterion to the
  Editor, do not silently ship.
- Recurring AI-tells in drafts → log the tell + the fix to `skills/self_improvement_eval.md` so
  the Drafter stops producing it upstream.
