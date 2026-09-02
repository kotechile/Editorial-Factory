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

## 3. The hard gate
- **Score ≥ 8 → proceed.** Select the single winner.
- Score 7–7.9 → broaden keyword seeds once (back to Scout), re-score.
- Score < 7 → drop.

## 4. Output — the angle brief
Write `context/recon_proposals/YYYY-MM-DD_<vertical>_angle_brief.md`:
```markdown
# Angle Brief: <vertical> — YYYY-MM-DD
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
vector (e.g. "all signals were retreads of the prior 30 days") to `skills/self_improvement_eval.md`.
