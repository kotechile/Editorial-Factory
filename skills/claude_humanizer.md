# SKILL: Frontier Humanizer & Smart Brevity Stylist (Loop 3 — Final Rewrite)

## 1. Objective
The last pass before approval. Apply **Smart Brevity** principles to strip every AI-tell, craft punchy
and scannable copy, inject cadence and a genuine human voice, and iterate until every section passes
its own gate. **Frontier model only.** The frontier is whatever the `stylist` profile is configured
to (see §7). Current live config: `gemini-3.1-pro-preview` (`provider: gemini`). Restore Claude/kie.ai
only when a valid key exists — never downgrade to a non-frontier model.

## 2. Required Inputs
To apply Smart Brevity effectively, the styling pass consumes:
1. **Target Audience (`persona`):** Defined in frontmatter / `context/personas.json` (e.g. `infra_engineer`, `eng_leader`).
2. **The One Big Thing (`one_big_thing`):** The single most important takeaway, fact, or decision the reader must remember.
3. **Raw Content / Source Material:** The unedited structural draft and verified brief with inline citations `[n]`.

## 3. Smart Brevity Rules & Architecture

### 3.1 The Tease (Headlines & Section Headers)
- **H2 / H3 Section Headers:** Target **6 words or fewer**. Punchy, active, descriptive.
- **Article Title:** The draft starts with a short title. The Stylist refines or polishes the title based on SEO keyword resonance and clarity without clickbait fluff, irony, or cryptic jargon.
- **No clickbait or vague abstractions:** Headers tell the reader exactly what is in that section.

### 3.2 The Lede (First Sentence)
- Deliver the primary news or core takeaway immediately in the **very first sentence**.
- Zero throat-clearing, preambles, rhetorical questions, or introductory fluff.
- Tell the reader something essential, concrete, and load-bearing upfront.

### 3.3 Context Signposts (Axioms)
Introduce supporting context using bolded, standardized guide words followed immediately by a single direct, declarative sentence:
- **Why it matters:** — Explain the systemic significance or immediate impact.
- **The big picture:** — Frame the broader industry or structural shift.
- **By the numbers:** — Lead into quantitative or benchmark figures.
- **What to do:** / **The playbook:** — Introduce concrete, doable practitioner steps.
- **The catch:** / **Between the lines:** / **Yes, but:** — State the honest limitation, tradeoff, or counter-argument.

### 3.4 Scannability & Bullets
- **Never output monolithic walls of text.**
- Any sequence of **three or more** data points, stats, tactical moves, or arguments MUST be broken down into clean, bulleted lists with bold lead-ins (e.g., `- **Audit bandwidth:** Ask vendors for...`).

### 3.5 Strong, Simple Diction
- Strip out passive verbs, weak adverbs (e.g., "basically", "materially", "extremely"), and bloated "10-dollar" corporate jargon.
- Prefer short, single-syllable, visual words that paint a clear picture.
- Translate domain jargon into plain English or add an immediate short parenthetical gloss.

### 3.6 Paragraph Discipline
- Keep paragraphs exceptionally brief: **1 to 3 sentences maximum**.
- One idea per paragraph. If a thought has two parts, split it into two crisp paragraphs.

### 3.7 The Exit ("Go Deeper")
- Conclude cleanly with designated **Go deeper:** references or internal links (`<!-- internal-links -->` and `## Sources`) for readers who want extra nuance without cluttering the main text.

---

## 4. Negative constraints (apply verbatim, no exceptions)
- No empty intros: "In today's fast-paced world", "In an era of", "It's no secret that".
- No hollow transitions: "Furthermore", "Moreover", "It's important to remember", "delve into",
  "dive deep", "let's explore", "In conclusion".
- No corporate sign-offs: "In summary", "ultimately, it's about", "the key takeaway is simple".
- No hedging filler: "some might argue", "it could be said", "interestingly enough".
- No adjective-stacking before nouns ("cutting-edge, revolutionary, game-changing").
- Preserve the lead incident/stat and the pragmatic takeaway — rephrase, never re-source.
- Preserve every citation `[n]` and the source list.
- Preserve the frontmatter (including SEO tags `meta_title`, `meta_description`, `primary_keyword`, `search_volume`) and refine `title` for punchy clarity.
- Preserve the `<!-- schema -->` (JSON-LD) and `<!-- internal-links -->` blocks verbatim when present, keeping them at the end of the markdown draft.
- Ensure the article body is clean markup starting with the lead paragraph and contains descriptive, high-quality `## ` (H2) section headings (target ≤ 6 words).
- Preserve each section's distinct, brief-sourced action items — bulletize them clearly for the target persona.
- Only VERIFIED-brief figures may appear; no secondary-derived sums.
- After the rewrite, compare the final body length to the draft floor (~800 words). If the frontier
  compacted it materially below the floor, restore depth from the verified brief (restate the moves / tension), never pad new claims.

---

## 5. Per-section iteration & Section Gates
Do NOT rewrite the whole piece and re-read it blindly. Iterate **section by section**, and only
re-iterate a section that fails its own gate. Order matters: **Lead first** — it decides whether
anyone reads on, so give it an extra check.

For each section, check its gate; if it fails, rewrite that section only and re-check (max 2
retries per section).

| Marker | Gate — it fails if… |
|---|---|
| `<!-- lead -->` | not a concrete incident/stat in sentence 1; contains throat-clearing, introductory preamble, or opens like a definition / "the world is changing". **Highest priority.** |
| `<!-- tension -->` | vague "the industry is evolving"; lacks a context signpost (**The big picture:** or **Why it matters:**); doesn't name what shifted and who it hurts/helps. |
| `<!-- tactical-insight -->` | generic advice ("invest in AI"); not structured with clean bullets and bold lead-ins for 3+ moves; not specific and doable for the target persona. |
| `<!-- nuanced-takeaway -->` | a hollow hedge or a cheerlead; lacks an honest limitation / counter-argument (**The catch:** or **Between the lines:**). |
| `<!-- tldr -->` | not exactly 3 scannable bullets; reads like a summary paragraph. |

After every section passes, run ONE final **whole-piece pass**: coherence, cadence, paragraph discipline (max 3 sentences per paragraph), and confirm no AI-tell or empty transition remains anywhere.

---

## 6. Output
`context/drafts/YYYY-MM-DD_<slug>_final.md` (long-form + LinkedIn) with the per-section gate
report. Keep the **TL;DR as the structured `<!-- tldr -->` field** (3 bullets) — never write a
prose "in conclusion / key takeaways" paragraph. The **TOC is render-time only** — do not compose
one.

## 7. Failure handling
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
- **Output-token budget (thinking models):** the frontier is a *thinking* model, and its internal
  reasoning tokens (`thoughtsTokenCount`, typically ~6,400 for a full rewrite) are counted **against**
  `maxOutputTokens`. A too-small budget makes the model think hard and then truncate the article
  (`finishReason: MAX_TOKENS`, partial output, missing `## Sources`/gate report). Keep
  `maxOutputTokens` **≥ 20,000** — verify with `finishReason: STOP` and `sources_check=ok`.
- A section that fails its gate after 2 retries → report the specific section + criterion to the
  Editor, do not silently ship.
- Recurring AI-tells in drafts → log the tell + the fix to `skills/self_improvement_eval.md` so
  the Drafter stops producing it upstream.

## 8. Accessibility gate (topic-agnostic — applies to EVERY topic)

The gate in §5 checks for Smart Brevity & AI-tells. It does NOT check whether a general reader can follow the
piece. A rewrite can pass every §5 gate and still read like a law-firm memo. Run BOTH gates.
The ACCESS gate is deliberately topic-agnostic: the rules below are the same whether the piece
is about tariffs, an energy program, a security standard, or a database. Enforce with
`scripts/check_accessibility.py` on the finished body.

Gates — the piece FAILS the ACCESS gate if:
1. **Any acronym is used without being expanded at its first use in the body.** Every
   abbreviation the reader won't already know gets a plain expansion once, either as
   "International Emergency Economic Powers Act (IEEPA)" or "IEEPA (...the law that lets the
   president act in a national emergency)". Never reuse an acronym bare after introducing it.
   Checker target: **zero undefined acronyms**.
2. **A specialist term from any domain is left untranslated for a general reader.** For each
   domain term (legal, finance, customs, energy, security, database, ML, government program),
   either (a) find the plain phrase the source used, or (b) add a short gloss. Examples:
   "filed a protective action" → "filed an objection"; "importer of record" → "the company
   named on the import"; "finally-liquidated entry" → "an import already fully processed";
   "unliquidated" → "not yet processed"; "non-recurring add-back" → "a one-time booking";
   "Section 232 duties" → "separate tariffs on steel and aluminum that were never struck down".
   The domain does not matter — apply the same plain-word-or-gloss test to any field.
3. **The reader needs the core mechanism explained and it is not.** If the story hinges on a
   process the target reader wasn't born knowing (refund flow, a rebate rule, a permission
   model, an agency outranking), add ONE half-sentence that states what it is before relying
   on it. "The biggest figure was spoken on a call, never written down" needs a breath that
   says why that is odd.
4. **The body reads at a difficult level for a general audience.** Checker: target
   **Flesch Reading Ease ≥ 60** on the body (frontmatter, `## Sources`, and the
   `<!-- linkedin -->` variant are excluded). Hard floor: ≥ 50. Readability comes from plain
   **words**, not short sentences — swap long/technical terms for everyday ones
   ("set up" not "implementation", "slows down" not "degrades throughput") and write connected
   ~14-20-word sentences with variation; do NOT fragment into choppy one-liners. Long proper
   nouns and the numbers are fine; the barrier is word choice.
5. **Keyword stuffing / non-fluent prose.** A target search phrase appears **at most 2-3 times**
   in the whole body — let the title/meta/headings carry it and rephrase everywhere else
   (pronouns, synonyms, "these systems"). Never let it read like a keyword-matching exercise.
   The checker flags `primary_keyword` appearing ≥4× in the body as a FAIL.

Do not sacrifice accuracy or a citation: this is a swap of vocabulary, never a change of fact.

Post-rewrite: run `python3 scripts/check_accessibility.py <final.md>`. Report the verdict in the
gate report. The humanizer scripts now auto-retry: if the rewrite fails the ACCESS gate, the script
feeds the exact FAIL/WARNING reasons back to the frontier model and re-prompts (up to 5 attempts,
`humanizer_tools.MAX_ATTEMPTS`). It exits 0 only on a passing verdict; if it still FAILs after the
retry loop, it exits 1 (held at Loop 3) with the specific criterion (undefined acronym / Flesch /
untranslated term) rather than shipping a dense piece.
