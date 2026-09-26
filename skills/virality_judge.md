# SKILL: Virality Judge (Loop 1 — Gate)

## 1. Objective
Score the Scout's signals and return a single, defensible winning angle (or a hard "no publish").

## 2. Scoring axes (1–10 each)
| Axis | Question | Weight |
|---|---|---|
| Novelty | Is this genuinely new in the last 30 days, not a retread? | 0.40 |
| Authority | Does it trace to a primary source, not a thin aggregator? | 0.30 |
| Shareability | Contrarian / new benchmark / practical ROI / hidden trend — would a reader forward it? | 0.30 |

Composite = round(0.40·N + 0.30·A + 0.30·S, 1).

### 2.5 Multi-Topic Synthesis Protocol (Cross-Pollination Engine)
Single press articles are frequently commoditized vendor announcements, incremental version bumps, or isolated news items. To create defensible editorial moat, the Judge must actively combine **two or more related signals** into an emergent, synthesized article:

**Read the seeded candidate block first.** The signals file carries a
`<!-- synthesis-seed:start --> … <!-- synthesis-seed:end -->` block under `## Candidate Synthesis Pairs`,
written mechanically from that file's own rows by `scripts/synthesize_topics.py --seed` (rows are only
admissible with an `https://` source, an in-window date and Intensity ≥ 60; archetypes are scoped to the
registry verticals). If the file is dated on/after the enforcement date and has no seeded block, or the
block's marker row count disagrees with the table, run the seed step before scoring — `scripts/verify.sh`
§8 reads a missing or stale block as a build failure. The helper's `emergence_heuristic` is **advisory
only**: it is not a composite, it cannot clear the ≥ 8 gate, and a seeded candidate is a candidate, not a
verdict. *"No valid pair"* in the block is a legitimate input — look for a synthesis the token layer
missed, and if none clears the gate, publish the single-signal winner.

- **The Core Synthesis Question**: *What strategic tension or economic shift appears when Trend A collides with Trend B that neither article could state on its own?*
- **Canonical Example**:
  - *Signal A*: Frontier LLM API prices drop sharply (e.g., token pricing falling 70–80% across frontier models).
  - *Signal B*: Enterprise shift toward local, in-house software development and internal developer platforms.
  - *Emergent Synthesis*: *"Would lower LLM frontier model prices drive more reliable in-house development?"* — exploring how cheap intelligence tips the build-vs-buy calculation and whether deterministic self-correction eliminates external SaaS lock-in.

**Synthesis Scoring Axes (1–10 each):**
| Axis | Question | Weight |
|---|---|---|
| **Emergence (E)** | Does combining Signal A and Signal B create a genuinely new thesis that neither source posited on its own? | 0.35 |
| **Dual Authority (A)** | Do both legs trace to verifiable primary sources (benchmarks, filings, pricing releases, code commits)? | 0.30 |
| **Tension & Shareability (S)** | Does this intersection force a hard decision, debunk conventional wisdom, or alter the target reader's P&L / roadmap? | 0.35 |

Synthesis Composite = round(0.35·E + 0.30·A + 0.35·S, 1).

**Precedence rule (with a margin):** a Synthesis candidate is selected over single-topic candidates only
when it scores ≥ 8.0 **and** beats the best single-signal candidate by ≥ 0.3. A synthesis that wins on a
tie, or on novelty alone, is a contrived pairing displacing a stronger story — take the single-signal
winner instead. Synthesis buys a proprietary moat only when the intersection actually beats the parts.

**Carry-through (gated):** writing `**Angle Type:** Synthesis` here obliges the run to carry the flag
onto the artifact — the draft (or published copy) must declare `synthesis: true` plus both anchors under
`sources:` (see `skills/story_draft.md` §3). `scripts/verify.sh` §8 fails the build when a Synthesis
brief has no such artifact, matched on the artifact's date + `vertical`; the flag is what tells readers
(and `/api/articles.json`) that the thesis fuses two signals rather than reporting one.

## 3. The hard gate
- **Score ≥ 8 → proceed.** Select the single winner (a synthesis only when it clears ≥ 8.0 **and** beats
  the best single-signal candidate by ≥ 0.3 — see the precedence rule in §2.5).
- Score 7–7.9 → broaden keyword seeds once (back to Scout) or test alternate signal pairs, re-score.
- Score < 7 → drop.

### 3.5 Prior-cycle thesis de-dup (HARD check before scoring)
Before scoring any candidate, compare it against **every angle brief + drafted/published article for this
vertical within the prior 30 days** (read `context/recon_proposals/*_<vertical>_angle_brief.md`, the
verdict line in the matching `content_calendar.md` run-log rows, and `context/published_log.md`).
- If a candidate re-argues the same **thesis** (same underlying rule/event/figure already won or drafted),
  it is a **retread, not a fresh signal** → cap Novelty at 6.0 and flag it, even if the specific framing
  differs. The point of the 30-day window is NEW signals, not re-litigating last cycle's winner.
- Re-run cadence caveat (drives the common failure): a vertical re-run only days after its scheduled
  weekly slot has a window that has *barely advanced*, so same-thesis follow-ups dominate. If every
  candidate is a retread and nothing fresh clears the window, return **"no publish"** — do not pad a
  near-8 composite by rating a retread's novelty high.
- Anchor-freshness rule: a candidate whose load-bearing claim/figure is dated OUTSIDE the 30-day window
  is dropped by the radar at Stage 1; if it still surfaces here, do not let its authority/shareability
  carry it past the freshness gate.

## 4. Output — the angle brief
Write `context/recon_proposals/YYYY-MM-DD_<vertical>_angle_brief.md`:

### Format A: Multi-Topic Synthesis Brief (Preferred)
```markdown
# Angle Brief: <vertical> — YYYY-MM-DD
**Angle Type:** Synthesis (Cross-Topic Fusion)
**Winner:** <Provocative question or synthesis headline, e.g. "Would Lower LLM Frontier Model Prices Drive More Reliable In-House Development?">
**Scores:** E=.. A=.. S=.. → Composite=..
**Signal A (Anchor 1):** <Source URL, publication date, concrete figure/event>
**Signal B (Anchor 2):** <Source URL, publication date, concrete figure/event>
**Emergent Collision Point:** <Why Signal A alters the economics, reliability, or feasibility of Signal B>
**Hook:** <The concrete collision lead tying both primary anchors together in sentence 1>
**Tension:** <The systemic friction / who this empowers / who this threatens>
**Target reader:** <persona id from context/personas.json>
**Single claim to defend:** <The unified hypothesis linking both signals that the article must prove>
**Runner-ups + why rejected:** <brief list of individual signals and alternative pairs>
```

### Format B: Single-Signal Brief (Fallback when no viable pair emerges)
```markdown
# Angle Brief: <vertical> — YYYY-MM-DD
**Angle Type:** Single-Signal
**Winner:** <headline-worthy one-liner>
**Scores:** N=.. A=.. S=.. → Composite=..
**Hook:** <the concrete incident/figure that opens the piece>
**Tension:** <why now / who it hurts / who it helps>
**Target reader:** <persona id from context/personas.json>
**Single claim to defend:** <the one sentence the article must prove>
**Runner-ups + why rejected:** <brief list>
```

## 5. Failure handling
No candidate ≥ 8 after one broaden → return "no publish" with the scoring table. Log the weak
vector (e.g. "all signals were retreads of the prior 30 days; no valid synthesis pairs cleared the emergence gate") to `skills/self_improvement_eval.md`.
