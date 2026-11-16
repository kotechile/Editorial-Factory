# Article generation: token-cost optimization plan

**Goal:** cut the token cost of one published article by roughly half (target −55%, `$0.13 → $0.06` all-in) without lowering any gate, and make the cost curve flat instead of rising with every run.

**Architecture:** the spend is not in the writing. It is in *how the agent sits in the pipeline*: one long `deepseek-flash` session (~94 API calls) carries a ~160k-token prefix and re-reads it on every call, while the skills it loads have grown into 637 KB of accumulated case law. The fix is (1) instrument the cost, (2) shrink what rides in the prefix, (3) collapse the mechanical steps into one script so the model takes ~45 calls instead of ~94, (4) stop the two write-back loops that grow the skills and the run log on every run.

**Tech stack:** Python 3.11 stdlib, `scripts/frontier_llm.py` (DeepSeek), `scripts/sync_crons.py` (fleet reconciler), `scripts/verify.sh` (gates), Hermes cron store `~/.hermes/cron/jobs.json`, `~/.hermes/state.db` (session token accounting).

> **For Hermes:** implement phase by phase. Phase 0 and 1 are safe to run fleet-wide; Phase 2 changes the job prompt and must go through `scripts/test_sync_crons.py` + `scripts/sync_crons.py --check`; Phase 3 is a two-vertical pilot and needs the owner's nod to scale.

---

## 1. Baseline — measured, not estimated

Editorial cron fleet, `~/.hermes/state.db`, 2026-11-02 → 2026-11-13 (12 days, complete):

| metric | value |
|---|---|
| editorial cron runs (`Full`/`Evergreen`/`Review Pipeline:`) | 117 in 12 days (≈10/day, 33 verticals × news+evergreen + 3 review) |
| articles published in the window | 115 → **$0.131 per published article** |
| input tokens (cache miss, editorial) | **20,562,148** in the window; 162,406 per median run |
| output tokens (editorial) | **8,463,928** in the window; 69,056 per median run |
| cache-read tokens (editorial) | **2,298,728,448** (2.3 **billion**) in the window; 15,718,848 per median run |
| estimated cost, editorial | **$15.06** in 12 days (≈$1.25/day) |
| estimated cost, all cron | $16.33 in 12 days (watchdogs + sweeps are the remaining $1.27) |

Median single editorial run:

| | value | share of run cost* |
|---|---|---|
| input (miss) | 162,406 tok | 22% |
| output | 69,056 tok | 37% |
| cache read | 15,718,848 tok | **41%** |
| API calls | ~94 | — |
| cost | **$0.128** | — |

\* solved exactly from the estimator's own prices: `$0.15/M` miss, `$0.0030/M` cache read, `$0.60/M` output (least-squares over 360 sessions, residual 0.0000).

Two facts follow directly:

1. **41% of every run is the same text being re-read.** 15.7M cache-read tokens per run is the ~160k-token context multiplied by ~94 calls. Calls × prefix is the whole game.
2. **37% is output** — 69k generated tokens for an article whose final text is ~2.6k tokens. That is per-turn reasoning (94 turns) plus whole-document rewrites plus two write-back habits (run log, skill appends).

Fleet aggregate over the same window: **$3.08 input (21%) / $6.90 cache read (46%) / $5.08 output (34%)** — cache read is the largest single line of the bill.

### What is actually in the context (measured from the stored transcripts)

| block | news run `consumer_asset_repair_replace_tco` 13 Nov | evergreen run `resilient_home_assets` 13 Nov |
|---|---|---|
| total added content | 643,838 chars ≈ 161k tok | 499,686 chars ≈ 125k tok |
| web_search results | **28%** | 11% |
| skill / source-code reads | **27% + 1%** | **26% + 6%** |
| other terminal output | 21% | **41%** |
| gate / verify.sh output | 14% | 15% |
| file writes (drafts, logs, patches) | 4% | 1% |
| assistant text | 0.5% | 0.6% |

Tool-call mix for the same news run: **104 terminal**, 17 web_search, 16 write_file, 12 patch, 11 read_file/skill_view, 7 process_manage — 323 messages for one article.

### The cost is designed to grow

| artefact | size now | growth |
|---|---|---|
| `skills/evergreen_topics.md` | 245,578 chars (36,320 words) | 108 commits; +2–4 KB **per run** (the run appends a "Hosts probed live …" paragraph) |
| of which §"Gate result" exemplars | 21,100 words (58% of the file) | 104 dated examples, 29 distinct dates |
| `skills/claude_humanizer.md` | 99,492 chars | 59 "learned 2026-…" incident paragraphs |
| `skills/illustration_director.md` / `publisher.md` / `story_draft.md` | 40,264 / 36,297 / 30,644 chars | same pattern, slower |
| `context/content_calendar.md` | **2,726,387 chars** | 117 Nov rows, avg **8,489 chars** each (max 11,493) — written as output, grepped as input |
| all skills | 637,614 chars ≈ 160k tokens | no size gate anywhere in `verify.sh` |

Proven in the transcript of the 13 Nov 18:00 evergreen run: turn 94 is `cat >> skills/evergreen_topics.md` (a 2,964-char case-law paragraph), turn 75 is a 7,914-char `content_calendar.md` append. Both grow on every run and both are read back by the next run. **There is no ceiling, so per-article cost rises forever.**

### Measurement gaps

- `scripts/frontier_llm.py` never reads the response `usage` object. Every in-pipeline `deepseek-v4-pro` call — `article_reviewer.py` (3 attempts), the art director, the push-time rewrite — is **invisible** to `state.db`. The $15.06 editorial figure is a floor, not the total.
- `humanize_one.py` (called by `publish_gate.attempt_rewrite`) duplicates the whole humanizer RULES block *and* goes through `humanize_loop3` with `thinking` left on and `max_tokens=32000`; the documented failure mode is a full 32k reasoning burn returning empty content (`finish_reason=length`). A failed push-rewrite can therefore cost a whole ceiling for nothing.

---

## 2. Step-by-step review of the pipeline

| # | step | who runs it | measured cost driver | verdict |
|---|---|---|---|---|
| 0 | job prompt → agent boots, reads skills | cron agent (flash) | skills are 160k tokens of the 637 KB tree; 26–32% of all added content, then re-read every turn | **primary waste** |
| 1 | Radar / signal sweep | agent, 17 `web_search` + fetches | 28% of a news run's content; 20+ turns; each result retained for the rest of the run | second-largest, partly irreducible |
| 2 | `synthesize_topics.py --seed` | script | reads the 2.7 MB `content_calendar.md` for de-dup each run | cheap in $, slow; fine |
| 3 | Virality Judge → angle brief | agent | ~15k-char skill + signals file; 1 pass | acceptable |
| 4 | Fact check → verified brief | agent, several fetches | 14k-char skill; brief ~7 KB | acceptable |
| 5 | Story draft | agent | 31k-char skill; writes ~7.5 KB | acceptable |
| 6 | Frontier rewrite (`article_reviewer.py`) | `deepseek-v4-pro`, 3 attempts | prompt 25.5–29.3k chars (≈7k tokens) each attempt; output 2.6k tokens; thinking already off | well-built, but **unmetered**; 3 blind attempts when 1 + targeted feedback would do |
| 6b | `publish_gate.attempt_rewrite` → `humanize_one.py` | pro | duplicated RULES, thinking ON, 32k ceiling, up to 5 attempts | **defect: expensive no-op path** |
| 7 | Gate battery (`check_accessibility`, `article_shape`, `readability_critic`, `headline_score`, `source_gate`, `review_audit`, `check_social_voice`, `publish_gate`) | agent, by hand | **14–15% of content**; the 13 Nov run executed `verify.sh` 4×, the critic 4×, accessibility 3×, and `sed`-read 10 source files to discover the thresholds | **primary waste** |
| 8 | Persistence (`publish.py`, `wp_draft.py`, illustration, Supabase, sitemap) | agent + pro art director | 40k-char illustration skill; 3–4 director refusals per header; long verbose output | moderate |
| 9 | Run log + skill write-back + commit | agent | 8.5 KB row (≈2.1k output tokens) + 2–3 KB skill append (≈0.8k) — **4% of output, and it compounds** | **primary waste** |

---

## 2b. Caching — what it already buys, and the four stability rules

Prompt caching is **already doing the heavy lifting**, and it is not a lever that can be pulled much
harder from our side. Measured on the live API (2026-11-16, 4 calls, ~$0.005):

| call | prompt tokens | cache **hit** | cache **miss** |
|---|---|---|---|
| 1. a 7,791-token prefix, cold | 7,791 | 0 | 7,791 |
| 2. the same prefix 4 s later | 7,791 | **7,552 (97%)** | 239 |
| 3. the same text with **one line changed at the head** | 7,791 | **0** | 7,791 |
| 4. same head, longer tail | 7,795 | **7,552** | 243 |

Three properties fall out, and they are the ones that matter:

1. **Hits are strictly prefix-matched, in 64-token blocks.** Change a single token at the head and the
   whole prefix is re-billed as a miss. Append to the tail and nothing is lost.
2. **The discount is 50x** (`$0.0030/M` vs `$0.15/M` in our estimator). Over the 12-day window,
   2.30 **billion** cache-read tokens cost **$6.90**; at miss price they would have been **$345** — caching
   saved ≈$340 in 12 days (≈$10k/year). Fleet-wide hit rate on input: **99.1%**.
3. **Repetition is cheap, volume is not.** A block present for 90 of the 94 calls still costs
   90 × its size at hit price. That is why the bill is still 46% cache reads even at 1/50 the unit price.

Consequences to build into the plan (all of them are stability rules, not volume rules):

- **Append, never insert, in retry prompts.** `scripts/article_reviewer.py::build_prompt` inserts the
  retry feedback *before* "THE DRAFT TO REWRITE", so attempts 2 and 3 re-miss the draft and the
  output contract (~3k tokens) that could have hit. Move `{retry}` to the very end. Same audit for
  `humanizer_tools.retry_prompt` (already appends correctly).
- **Don't churn the head.** The system prompt (memory, user profile, date, skill list) is the head of
  every request, so editing memory or a shared skill mid-day re-bills the head of *every* job's first
  call, and a middle-of-file skill edit invalidates everything after that point. Practical rule: skill
  and memory edits land at a boundary (after the day's 10:30–13:00 and 17:30–20:00 slots), and case law
  is appended at the tail of a `references/` file, never inserted into the middle of a live SKILL.md.
- **The vertical's own instruction forks the cache.** Each job's prompt differs in its first line, so the
  fleet keeps 33 separate cache lines for the same skill text; nothing is shared between verticals. That
  is a harness property (skills would have to live in the system prompt), not something a prompt edit can
  fix — so do not budget for cross-vertical reuse.
- **The diet's value is ~15%, not ~26%.** 26–32% of *added content* is skill text, but most of it is
  already billed at 1/50. Cutting it by 75% saves ≈$0.015/run (12%), not 26%. Fewer calls (L2/L3) is
  where the money is, because no discount applies to re-reading the prefix on call 94.

## 3. The five levers

Projection is per median run ($0.128 baseline), each applied cumulatively; the acceptance test in §5 decides whether a lever stays.

| lever | change | mechanism | projected run cost | saving |
|---|---|---|---|---|
| **L0** | meter everything (Phase 0) | makes the rest measurable | $0.128 | — |
| **L1** | **context diet**: skills 637 KB → ~150 KB, case law moved to `references/` + a queryable host ledger | skills are 26–32% of content but only ~15% of the *bill* (most of that text is already billed as cache hits); −75% skill text = −20% prefix, −18% content | $0.113 | −12% |
| **L2** | **turn collapse**: `run_pipeline.py` spine + one `gate` command, 94 calls → ~45 | cache read is linear in calls: −52% cache, −45% output | $0.084 | −34% (cumulative) |
| **L3** | **stage split** (pilot): research+judge / draft+review / persist as separate short sessions | no single session carries a 150k prefix; prefix per call 150k → ~45k | $0.055 | −57% (cumulative) |
| **L4** | **output hygiene**: 300-char run-log cell + JSONL detail, `learn.py` instead of skill appends, gate output failures-only | −4k output tokens/run, stops both growth loops | $0.052 | −59% (cumulative) |
| **L5** | **research scripted** (news only): `radar.py` pulls feeds + configured sources into a candidate table, agent scores | −25% of news-run content, −10 turns | $0.045 | −65% (cumulative) |

Fleet maths: $1.25/day → ~$0.55–0.65/day; $0.13/article → ~$0.055–0.065/article visible, plus the (now metered) pro calls. The diet's share is honestly the smaller half of that: caching already discounts most of the skill text to 1/50, so the turn cut is where the money is.

**Honest caveat:** L2/L3 change the shape of the agent's work, so they carry the real regression risk. L1/L4 are pure deletion of duplicated text and cannot lower quality *if* the case law is moved rather than dropped — which is why the host ledger (T7) exists: it turns 63 paragraphs of prose nobody can query into a lookup that answers "this host 403s to the verifier, don't probe it again". That is a quality **gain** (fewer dead-end topics, fewer held runs), not a trade.

---

## 4. Tasks

### Phase 0 — instrument (half a day, zero behaviour change)

**T1. Frontier usage ledger.**
Files: modify `scripts/frontier_llm.py`; create `scripts/cost_report.py`.

`_post()` already has the response body; add to `chat()` and `vision()`:

```python
def _log_usage(payload, model, stage, kind="chat"):
    u = payload.get("usage") or {}
    row = {"ts": time.time(), "stage": stage or os.environ.get("PIPELINE_STAGE", ""),
           "model": model, "kind": kind,
           "in": u.get("prompt_tokens", 0), "out": u.get("completion_tokens", 0),
           "cache_hit": (u.get("prompt_cache_hit_tokens") or 0),
           "reasoning": ((u.get("completion_tokens_details") or {}).get("reasoning_tokens") or 0)}
    row["usd"] = round(row["in"] * 0.15 / 1e6 + row["out"] * 0.60 / 1e6, 6)
    with open(ROOT / "context" / "cost_ledger.jsonl", "a") as fh:
        fh.write(json.dumps(row) + "\n")
```

Verification: `python3 scripts/article_reviewer.py --draft <a draft> --attempts 1` then `tail -1 context/cost_ledger.jsonl` shows non-zero `in`/`out`/`usd`. Then `python3 scripts/cost_report.py --days 14` prints per-stage medians (radar / draft / review / art / publish).

**T2. Per-run line in the report.** `cost_report.py` also reads `~/.hermes/state.db` (`sessions` + `session_model_usage`, source `cron`) and prints, per run: calls, in/out/cache, in-session $, in-script $ from the ledger, quality flags (reviewer attempt count, hand-repair edits, gate results). **Until this exists, nobody can prove a saving.**

**T3. Size ceilings in `verify.sh`** (new §, fail-closed):

```bash
# §11 skill & log size ceilings — the pipeline reads these into context on every run.
BIG=$(find skills -maxdepth 1 -name '*.md' -size +26k | sort)
[ -n "$BIG" ] && { echo "FAIL: SKILL.md over 26 KB (move case law to skills/references/):"; echo "$BIG"; FAIL=1; }
LONG=$(awk -F'|' '/^\| 2026-/ && length($0) > 900 {c++} END{print c+0}' context/content_calendar.md)
[ "$LONG" -gt 0 ] && { echo "FAIL: $LONG run-log row(s) over 900 chars (see T9)"; FAIL=1; }
```

Verification: `bash scripts/verify.sh` on today's tree must go **red** (it is over the ceiling) — that is the point; it goes green when T4–T6 land. Prove the gate by planting a 30 KB skill in a scratch branch, not by trusting the code.

### Phase 1 — context diet (1–2 days; the safe, fleet-wide win)

**T4. Split `skills/evergreen_topics.md` (245,578 → ≤ 24,000 chars).**
- Keep §1–§4 (objective, admissibility, the gate, the brief format) — 3,753 words — and the floors (≥3 sources / ≥2 hosts / 180-day de-dup, pinned by `scripts/test_evergreen_gate.py:63`).
- Move the 21,100-word `## Gate result` exemplar block and the 63 "Hosts probed live" paragraphs to `skills/references/evergreen_casebook.md` (read only when a probe or matcher question actually comes up).
- Extract the 63 host-probe paragraphs into `context/knowledge/host_probes.json` (see T7).
Verification: `wc -c skills/evergreen_topics.md` ≤ 24,000; `python3 scripts/test_evergreen_gate.py` and `test_synthesize_topics.py` pass; `bash scripts/verify.sh` green; `grep -c "Hosts probed" skills/evergreen_topics.md` = 0 and the casebook contains all 63.

**T5. Same for `skills/claude_humanizer.md` (99,492 → ≤ 26,000).** Keep the rules the gates actually enforce (`verify.sh` §3/§9, `check_accessibility`, `readability_critic`, `article_shape`); move the 59 "learned 2026-…" incidents to `skills/references/humanizer_casebook.md`. Verification: `grep -c "learned 2026" skills/claude_humanizer.md` = 0; casebook count = 59; `node scripts/check_social_voice.mjs` and `check_accessibility.py` unchanged on the last 5 finals (byte-identical verdicts).

**T6. Trim `story_draft.md` (30.6 KB), `publisher.md` (36.3 KB), `illustration_director.md` (40.3 KB)** to ≤ 26 KB each by the same move-not-delete rule; casebooks per skill.

**T7. Host ledger with a query interface** — the quality win inside the diet.
File: create `scripts/host_probe.py`; write `context/knowledge/host_probes.json` from T4's extraction (schema: `host`, `url_pattern`, `verdict` ∈ {fetchable, 403, 404, stub, js_only, no_figures}, `note`, `as_of`, `vertical`).

```bash
python3 scripts/host_probe.py --check https://bls.gov/ooh/   # → "403 to the verifier (2026-10-16) — do not plan a row on it"
python3 scripts/host_probe.py --vertical resilient_home_assets --fetchable
```

Wire it into `skills/radar_30day.md` and `skills/evergreen_topics.md` as a *required* first step before any fetch of an unknown host, and into `scripts/verify.sh` as a smoke test (`--selftest`). Verification: run `citation_hub_dossier.fetch_source` on 5 hosts the ledger calls unreachable and confirm the ledger agrees; a disagreement is a stale row, not a pass.

**T8. Replace the two write-back loops.**
- `scripts/learn.py --vertical <id> --kind host|pitfall --file <md>` → appends one JSONL row to `context/knowledge/<vertical>.jsonl`, then regenerates the relevant `skills/references/*.md` section deterministically.
- Update the three prompt templates (`prompt_for`, `evergreen_prompt_for`, `review_prompt_for` in `scripts/sync_crons.py`) to say: *record lessons with `scripts/learn.py`, never append to a SKILL.md*.
Verification: after a run, `git status` shows **no** modification to `skills/*.md`; the lesson is present in `context/knowledge/`; `python3 scripts/sync_crons.py --check` exits 0 (prompt drift class).

**T9. Compact the run log.** Change the row schema in the prompt templates to a ≤ 300-char cell (what shipped, the score, the gate verdicts, the open items) plus the full detail as `context/run_log/YYYY-MM-DD_<vertical>.md`, and a machine line in `context/cost_ledger.jsonl`.
**Prerequisite (verify first):** `site/server.mjs:17` (`CALENDAR_FILE`), `scripts/synthesize_topics.py`, `manage_verticals.py`, `sync_verticals.py` all parse this table — read each parser and pin the expected columns before shortening cells. Archive rows older than 60 days to `context/archive/content_calendar_YYYY-MM.md` with the parsers updated to read both.
Verification: dashboard `/api/…` still lists the vertical's runs; `synthesize_topics.py --check-seed` still reads prior rows; file stops growing at >1 MB.

### Phase 2 — turn collapse (2–3 days; the biggest lever)

**T10. `scripts/run_pipeline.py` — the deterministic spine.** Everything that is not judgment becomes one command:

```
python3 scripts/run_pipeline.py --vertical <id> --mode news|evergreen|review \
    [--start]            # resolve date/slot, load registry+persona, print the 6-line brief
    [--seed]             # synthesize_topics.py --seed on today's signals file
    [--gate-brief]       # evergreen_gate.py / review_gate.py on the brief
    [--review]           # article_reviewer.py --draft <autodiscovered>
    [--gate]             # the whole battery, one summary line per gate (T11)
    [--publish]          # publish.py + wp_draft + illustration + supabase + sitemap
    [--log]              # run-log row + cost line + commit (T9)
    [--finish]           # verify.sh, once, printing failures only
```

`--start … --finish` is the fleet path; each flag is also usable alone, so the agent can recover mid-run. Rules: no network, no LLM, no writes except the ones named; exit codes 0/1/2 as today.

**T11. One gate command.** `gate_all` inside T10 (or `scripts/gate_all.sh`): runs `check_accessibility`, `article_shape`, `readability_critic`, `headline_score`, `source_gate`, `review_audit`, `check_social_voice` (scoped to the file, not the repo), `publish_gate --file`; prints **only failures plus one summary line**, exits 1 on any hold. This replaces the 4× `verify.sh` + 4× critic + 3× accessibility pattern observed on 13 Nov (≈14% of context, ~10 turns).
Verification: on the last 5 published artifacts `gate_all` returns the same verdicts as the individual scripts (compare exit codes and the FAIL lists), and its total stdout is < 2 KB.

**T12. Update the fleet prompts.** Shorten `prompt_for()`/`evergreen_prompt_for()`/`review_prompt_for()` to: *the step sequence, the gate that must pass, the spine commands, and the "no skill appends, use `learn.py`" rule* — deleting the prose that restates skills. Then:
1. `python3 -m pytest scripts/test_sync_crons.py -q` (it pins `story_draft`/`claude_humanizer`/`evergreen_topics` mentions — keep those substrings).
2. `python3 scripts/sync_crons.py --check` → exit 0.
3. `python3 scripts/sync_crons.py` then prove from the store, not the summary:
   `python3 -c "import json,os;d=json.load(open(os.path.expanduser('~/.hermes/cron/jobs.json')));print(sum(1 for j in d['jobs'] if 'run_pipeline.py' in j.get('prompt','')))"` == the number of enabled pipeline jobs.
4. `python3 scripts/check_offpeak_crons.py` and `bash scripts/verify.sh` green.

### Phase 3 — stage split pilot (2 verticals, 2 weeks)

**T13.** Add `Full Pipeline (recon): <id>` and `Full Pipeline (publish): <id>` for two verticals (`home_infrastructure_lifecycle_tco`, `supply_chain`), slotted where the current job sits (10:30 / 10:30), second stage +45 min so the prefix never spans the research. The recon stage ends by writing signals + angle brief and appending its cost line; the publish stage starts from the briefs.
Verification: registry → `sync_crons.py --apply` → read the live store; both stages deliver to `slack` on `deepseek-flash`; `check_offpeak_crons.py` clean; `verify.sh` §7/§8 still green (the seed + marker contract lives in the artifacts, not the session).

**T14.** Two-week result table (cost/article, gate outcomes, hand-repair count) → scale or revert. **Owner nod required before scaling** — this is the change a reader could feel if it goes wrong.

### Phase 4 — frontier hygiene (parallel, independent, cheap)

**T15.** One RULES source, thinking off, bounded ceiling:
- `scripts/humanize_one.py` imports `humanize_loop3.RULES` instead of carrying a second copy (removes a ~14 KB drift-prone duplicate).
- `humanize_loop3.humanize_single_draft` passes `thinking=False`; `MAX_ATTEMPTS` 5 → 3; `frontier_llm.MAX_TOKENS` 32,000 → 12,000 for rewrites (a ≤1,300-word body needs ~2,600 with headroom; the code already raises on `finish_reason=length`).
- `publish_gate.attempt_rewrite`: one attempt, and only when the accessibility floor actually failed (it already gates on that — assert it).
Verification: `python3 -m pytest scripts/test_publish_gate.py -q`; a live rewrite on one draft returns non-empty content and lands `_final.md`; `context/cost_ledger.jsonl` shows `reasoning` ≈ 0.

**T15b. Cache-friendly retry prompt** (proved necessary by the probe in §2b).
`scripts/article_reviewer.py::build_prompt` inserts the mutable `{retry}` block before the draft, so a retry
re-bills the draft and the output contract at full miss price. Move the retry block, and the feedback lines,
to the very end of the prompt (after `THE DRAFT TO REWRITE`), leaving every byte before it identical between
attempts. Verification: `python3 scripts/article_reviewer.py --draft <slug>_draft.md --attempts 2`, then read
`prompt_cache_hit_tokens` in `context/cost_ledger.jsonl` — attempt 2's hit must cover the draft (≥ 90% of
attempt 1's prompt), where today it is a full miss.

**T16.** Art director: cache the chosen treatment per vertical in `context/state/`, and cap director attempts at 2 with the validation error fed back verbatim (3–4 refusals per header are currently normal — e.g. 13 Nov: 4 refusals for `cinematic_still`, 3 for the collar piece).
Verification: `python3 -m pytest scripts/test_illustration_creator.py -q`; one `--apply` on a scratch article reaches a validated brief in ≤ 2 calls (count in the ledger).

---

## 5. Quality guardrails and acceptance

Every phase is judged on the **same five metrics from the last 10 published articles** (baseline) vs the first five after the change, and only then fleet-wide — no bulk retro-fix of published output.

| metric | source | must hold |
|---|---|---|
| reviewer ACCEPT rate & attempts | `context/drafts/reviews/*_review.md` | ≥ baseline (currently ~1.5 attempts, with hand repairs common) |
| accessibility Flesch | `check_accessibility.py` | ≥ baseline median (≈55); floor 50 unchanged |
| critic holding defects | `readability_critic.py` | 0 |
| headline score | `headline_score.py` | ≥ baseline median; `lead_ok` true |
| publish rate the same slot | run log | no drop in published articles/week |
| hand-repair edits after ACCEPT | review report + `git diff --stat` | ≤ baseline |
| cost/article | `cost_report.py` | −25% (P1), −45% (P2), −55% (P3) |

Red lines — **do not** touch: the gate thresholds, `kind:`/markers contract, the 30-day window, the evergreen floors (3 sources / 2 hosts / 180-day de-dup), the no-social-distribution rule, the CMS push being ungated. The plan deletes duplicated *prose*, never a rule.

## 6. Risks and open questions

- **Case-law loss.** Moving 63 host paragraphs + 118 incidents out of the hot path could lose a lesson if the extraction is sloppy. Mitigation: move verbatim into `references/` + `host_probes.json` first, diff the counts (63/59/88) before deleting, and keep the casebook in-repo.
- **Prompt drift.** Any template edit must pass `test_sync_crons.py`, `sync_crons.py --check`, and be proved from `~/.hermes/cron/jobs.json` — the registry owns the instruction text.
- **Stage split failure modes.** A two-stage job needs its own loud failure (the run-log marker + `verify.sh` §8) so a dead recon stage cannot look like "no publish today".
- **`content_calendar.md` format.** Four consumers parse it (`site/server.mjs`, `synthesize_topics.py`, `manage_verticals.py`, `sync_verticals.py`). Shortening cells before reading those parsers breaks the dashboard.
- **Model tier.** Nothing here needs a frontier upgrade; the opposite — the pro calls are ~7k in / 2.6k out each and should be *fewer*, not bigger. Keeping `deepseek-flash` for the agent is correct.
- **Open question for the owner:** is the accumulated case law still wanted at all (it is what makes run N+1 better), or is a 2–3 example cap per hand-off acceptable? The plan assumes "keep it all, just out of the prefix".

## 7. Appendix — reproduce the measurements

```bash
# per-run cost/split (state.db): sessions where source='cron'
python3 - <<'PY'
import sqlite3,os,statistics as st
c=sqlite3.connect('file:'+os.path.expanduser('~/.hermes/state.db')+'?mode=ro',uri=True)
rows=list(c.execute("select input_tokens,output_tokens,cache_read_tokens,estimated_cost_usd,api_call_count from sessions where source='cron' and coalesce(input_tokens,0)>0 order by started_at desc limit 20"))
print({k:st.median([r[i] for r in rows]) for i,k in enumerate(['in','out','cache','usd','calls'])})
PY

# what the agent loaded: largest tool results in one session, by chars
# (same query, grouping messages by tool_name, length(content))

# skill growth
git log --format='%h %ad' --date=short -- skills/evergreen_topics.md | head -8
wc -c skills/*.md context/content_calendar.md

# review prompt size (no API call)
python3 scripts/article_reviewer.py --draft context/drafts/<slug>_draft.md --dry-run | wc -c

# cache behaviour probe (4 calls, ~$0.005): repeat a prefix, then change one line at its head
#   1 cold → hit 0 · 2 repeat → hit ~97% · 3 head line changed → hit 0 · 4 longer tail → hit unchanged
python3 .hermes/plans/cache_probe.py     # ~$0.005; prints prompt_cache_hit_tokens per call
```
