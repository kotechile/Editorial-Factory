# Plan — the reviewer stage: read a raw article, write a humanized whole, prove it

Status: built and tested (2026-10-27); first full-contract acceptance still open
Owner ask: *"review the content generation end to end to make sure it generates an article that is
accurate and flows like it was written by a human expert writer. The reviewer LLM should be able to
read a raw article generated and output a humanized article that reads easily as a whole."*

## What was measured first (216 committed `_draft.md` → `_final.md` pairs, plus the 216 published artifacts)

| Signal | Measured | Meaning |
|---|---|---|
| Sentence-length sd, draft → final | 8.1 → 6.3 words; **falls in 159/216 (74%)** | the reviewer flattens cadence — every sentence lands 14–18 words |
| Filler density (`really`, `actually`, `clearly`, `simply`…) | 0.75 → 1.19 per 1,000 words; **rises in 108/216** | the rewrite adds the words the voice rule bans |
| Hedge density | 1.47 → 1.38 | flat — no net gain |
| Figures lost | **128/216 articles lost ≥ 1 figure (314 total)** | e.g. `2026-10-27_your-eta-misses-27-hours`: draft "22.5% down to 10.9%" → final "roughly a tenth to a fifth"; `your-gpu-break-even`: "13.41 cents" and "22,269 tokens a second" gone |
| Figures invented | 36/216 gained ≥ 1 figure not in the draft (53 total) | rounding/normalisation explains some, not all |
| Repeated 4-grams inside one final | 135/216 carry ≥ 10 | restatement — the same idea in a new sentence |
| H2 sequence | **183/216 identical** (`The big picture: / By the numbers / What I'd watch: / The catch / At a glance`) | correct house skeleton, one template for 85% of the desk |
| Cross-article cue boilerplate | "the part I keep circling" × 56, "the catch my read is that" × 47, "what strikes me here is that" × 29 | the required observer cue became a fixed lexicon |

Two conclusions the code has to answer:

1. **The accuracy contract is prose.** `skills/claude_humanizer.md` §7 carries 25+ hand-audited
   pitfall classes ("a share-of-a-base figure is the first casualty of compaction", "audit each
   figure's unit noun", "audit derived intervals"). Every one of them is a *manual* post-rewrite
   diff, and the share-of-a-base class documented 2026-10-21 recurred on 2026-10-27. A rule that
   lives only in a skill recurs at the rate of human attention.
2. **Nothing measures flow.** `check_accessibility.py` gates Flesch + acronyms and advises on
   *mean* sentence length and the share of ≤8-word sentences. Both can be satisfied by a body whose
   sentences are uniformly 15 words — which is the measured failure. Variance is the missing signal.

## What gets built

### 1. `scripts/review_audit.py` — the mechanical contract (pure, offline, testable)

`ledger(draft, brief)` extracts what may not move:

- **figures** — every numeric token, normalised (`$1,175` → `1175`, `22,269` → `22269`, `13.41`
  stays `13.41`) with the sentence it sits in, so feedback quotes the claim, not just the number.
  Years (1900–2100) and citation markers are classified separately: a lost year is advisory, a lost
  measurement is a failure.
- **citations** — `[n]` → count, plus which source rows are cited at all.
- **quotes** — every `"…"` span ≥ 4 words, verbatim.
- **sources** — the `## Sources` lines, verbatim.

`audit(draft, final, brief)` returns hard failures and flow numbers:

- hard: missing figure (with the draft sentence), invented figure, dropped citation, altered quote
  or source line, missing section marker, body under the word floor, leaked deliberation
  (monologue / template placeholders), a self-graded `## Gate report` left in the artifact.
- flow: sentence-length mean **and sd**, staccato-paragraph rate, filler / hedge / abstraction
  density per 1,000 words, repeated 5-grams, restatement of the through-line across sections,
  identical section-openers, and the four boilerplate observer cues.
- `score(final)` orders candidate rewrites so the loop keeps the best attempt, not the last.

### 2. `scripts/article_reviewer.py` — the stage

Replaces the "one 100-line prompt + self-graded gate report" call with a read-then-write pass:

1. **Read** — the model states the article's through-line and the shape this story wants
   (a `review-note` block that is stripped into the report, never published).
2. **Write** — one whole-document humanized rewrite under an *ordered* contract: accuracy first
   (every figure, citation, quote, name), then cohesion (one argument, joins written, no restatement),
   then voice (connected prose, varied rhythm, no boilerplate cue), then shape.
3. **Audit** — `review_audit.audit()` on the result. A hard failure or a flow regression retries with
   the exact missing figures and the exact rhythm delta as feedback (max 3 attempts, best kept).
4. **Fail closed** — a rewrite that still drops a load-bearing figure exits non-zero and writes a
   review report; it never silently becomes the `_final.md` a publisher reads.

### 3. Tests

`scripts/test_review_audit.py` (offline, no LLM) pins each class against the real artifacts that
produced it: the share pair lost from `your-eta-misses-27-hours`, the invented/kept figure cases,
the flattened-rhythm case, the boilerplate cue, the leaked gate report, plus the negative cases (a
faithful rewrite must pass, a round `26.92 → 27` must not be called a loss).

### 4. Wiring

- `verify.sh` §8.57 runs the audit tests (hard gate).
- `skills/claude_humanizer.md` §5 becomes the reviewer-stage contract; §7's figure-audit prose is
  replaced by a pointer to the gate that now enforces it.
- Proven on two of today's drafts on the VPS (`your-eta-misses-27-hours`, `your-gpu-break-even-is-37-percent-busy`):
  old final vs reviewer output, audited side by side.

## Verification — what actually ran (2026-10-27)

| Run | Result |
|---|---|
| `test_review_audit.py` (local 3.9, VPS 3.12) | 18/18 pass — the real-artifact cases fail, the faithful rewrite passes, a rounding is not a loss |
| `check_social_voice.mjs --self-test` | pass, with the widened first-person rule and a new fixture for it |
| `check_social_voice.mjs` on the corpus | `OK — 625 check(s) read as an observer comment` (no published artifact regressed) |
| `verify.sh` (local) | the new §8.55c gate passes; the three failures it reports (cron drift, off-peak, off-peak contract) reproduce on a stashed clean tree — they are this host's clock, not the change |
| Reviewer, ETA draft, attempt 1 (`--attempts 2`) | rejected, then **ACCEPTED** at rhythm 8.6→8.1 and zero figures lost — that build predated the cue and accessibility checks |
| Reviewer, GPU draft, same build | rejected (rhythm 10.6→5.7, two figures lost), then **ACCEPTED** at 10.6→10.3, health 0.635→0.841 |
| Reviewer with the full contract (cue + accessibility + duplicates), 2–3 attempts, both drafts | **HELD** each time. Best candidates kept every figure (22.5%/10.9%, 13.41¢, 22,269 tok/s all restored) and lifted rhythm health (0.81→0.958), but missed one or two mechanical checks — mostly the observer cue, twice the Flesch floor by under a point |

Two things that run changed, beyond the plan:

- **The voice gate was wrong, not the writer.** A candidate opening the catch with "What I find
  limiting about the tolerance is…" was reported as having *no* observer cue: `OBSERVER_CUES`
  matched a closed verb list (I've/I have/I keep/I read/…). Widened to any first-person verb in
  both `site/social_voice.mjs` and `review_audit.py`, with fixtures on both sides.
- **A held run must not touch the final.** Held text and every report now land in
  `context/drafts/reviews/` — never as `<slug>_final.md`, and never in `context/drafts/` where the
  voice gate walks and would redden the repo build on a deliberately unfinished body.

**Open:** no run of the *full* contract has been accepted end to end yet. The hold path is correct
and the failures are mechanical, but until one of these runs passes inside its attempt budget the
stage needs a human on every article. Two levers, in order: give the model the shape of the cue
sentence per section (rather than a rule), and treat Flesch within a point of the floor as a
regression to fix rather than a hold — the desk already hand-tunes 49→57 before a push.

## Non-goals

- Not changing the house skeleton (five H2 slots) — that is an owner design decision. The audit
  *reports* cross-article sameness; it does not re-cut the shape.
- Not re-writing published articles. The gate applies to new runs; older artifacts are grandfathered
  the way `article_shape.json` and the voice gate already do.
