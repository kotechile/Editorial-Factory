# Run log — enterprise_tech_leadership, news, 2026-11-17

**Slug:** `your-approval-gate-kills-20` — published as *"Your Approval Gate Kills 20%: The Bill Moved
Into Margin"*. Synthesis, 8.8 (E8.7 / A9.0 / S8.7). Persona `eng_leader`. Tagged `kind: news` (CMS
term 43).

## Radar (window 2026-10-18 → 2026-11-17)

19 query shapes: 11 date-agnostic web fan-outs across the four configured source classes
(`hacker_news`, `substack_tech_leads`, `cloud_cost_reports`, `x_ai`), 4 primary-page fetches, 2
HN/Algolia window checks, 2 Substack archive-API date probes. Five in-window rows (Intensity
66–92), the rest carried as dated background.

Dropped at Stage 1: Dev Interrupted's tokenmaxxing essay (read as current; its newsletter archive
API dates it well before the window and its body calls GitHub Copilot's June metered pricing "this
month"); Accenture CIO Pulse November 2026 (in window, but it re-opens the 2026-11-03 data-readiness
ground); D&B AI Momentum Q3 (July release); every monolith/microservices article in the window
(they all retail the same 2025 CNCF-linked 42% figure — no in-window primary).

## Judge — and the pivot §3.5 forced

The first candidate was the obvious collision: CloudZero's effective token price fell 34% July →
October while the median company's AI spend grew every month, against Gartner's 47.5% forecast rise.
**Refused as a sibling retread**: `enterprise_ai_finops` published exactly that on 2026-11-12
(`your-ai-bill-grew-165-you-cut-the-work` — "AI spending … rose only 1.65% while the price of a
million tokens fell 21%"), and its 2026-11-05 piece had already priced a dollar cap in a deflating
unit. Novelty capped at 6.0; the price movement survives only as a clause with no argument on it.

Pivoted to what neither sibling run argued: **where the spend now sits on the P&L, and which control
preserves a programme.** Leg A CloudZero AI Economics Pulse November 2026 (2026-11-10): 82.0% of
classified spend ran production at the median, up 3.2 points; the remaining 18% is the only part an
approval gate can reach; 27% named gates as their main FY2027 change and gate-led teams killed or
paused 20% of initiatives against 7% for unit-cost funding; the 23% who both allocate and measure
grew at the same rate and failed to secure an investment 3% of the time against 19%. Leg B Gartner
(2026-11-12): $2,746bn → $4,050bn (+47.5%), infrastructure 59% / $2.4tn (+53%), AI-optimised servers
$527.6bn → $957.2bn. Third host, OnlyCFO/OpenRouter (2026-10-22), corroborates the mechanism:
agentic 131tn tokens a week against 18tn human, cache share 88% vs 55%.

Seeder `rows=5 candidates=0` — a legitimate "no valid pair" (the collision is where a budget line
sits, which the archetype vocabulary has no token for). Precedence: synthesis 8.8 against the best
single-signal 8.3 (CloudZero alone), margin +0.5.

## Fact check

15 rows: **9 VERIFIED**, 1 DERIVED (the 18% = 100 − 82.0), 1 DERIVED (the ~$1.3tn gap),
4 FLAGGED — the 82.0% is a median across 70 tagged companies, not "of companies"; CloudZero sells
the software its panel bought; the 20%/7% split is self-reported with no published instrument;
Gartner is a forecast. Dual-anchor PASS (4 verified on A, 5 on B). Nothing REMOVED.

## Draft → frontier

Draft 787 words, Flesch 54.2, all three pre-flight checks clean after two pre-tunes (At a glance cut
from 62 to 45 words; two bullets rebuilt to one figure each; a 2×4 table added for the gate-versus-
meter comparison the critic asked for; observer cue added to `<!-- tension -->`). Headline
`headline_score.py` 100/100 STRONG with `lead_ok` true — "Your Approval Gate Kills 20%: The Bill
Moved Into Margin", 5 core words, 56 chars.

Frontier (`run_pipeline.py review`, deepseek-v4-pro): **attempt 1 ACCEPT** — hard=0, regressions=0,
rhythm 8.5→8.6, health 0.845→0.849, Flesch 53.9, 830 words. Two hand repairs after it landed, neither
visible to a gate: "grew at the same rate" → "plan to grow at the same rate" (the source is a
forward-looking FY2027 plan, not observed growth), and "My reading is" → "My read is" (the
documented voice-regex form).

`run_pipeline.py gate`: all eight pass (accessibility, shape, critic, headline, sources,
review_audit, voice, publish_gate).

## Persistence

`publish.py` → `published/2026-11-17_your-approval-gate-kills-20.md`; Supabase article
`38eb107b-bde4-4644-9d86-df775dc9e0ca`; WordPress post **1738** on cms.giniloh.com (status publish,
category 3 "Mental Models & Strategy", vertical term 17, kind tag 43 = news), featured media **1740**,
read back over REST. Reader surface https://aichieve.net/your-approval-gate-kills-20/ answers **200**
with its own `<h1>`.

**Header — three commissions before it landed.** `publish.py`'s art director rendered a
`paper_collage` whose hook line sat buried behind the collage and was illegible; re-compositing with
`--anchor top-right` moved the type but the hook still crossed the dial; clearing the hook in
`featured.json` did nothing because `illustration_overlay.py` re-derives copy from the article each
run. Re-commissioned as `cinematic_still` on flux-2 (5 credits): a barred gate across a dark data-hall
aisle with a wall-mounted meter, type block over a scrim at the bottom centre — every line legible
and no clipping. Open note: the meter face carries small printed dial numerals, which rule 11 reads
as model-drawn lettering; they are not legible at display size but a future run should commission a
blank-faced instrument. Alt text was the documented title-glued fragment and was rewritten to a
108-character sentence across the artifact, `featured.json`, media 1740 and the row.

**Internal links curated by hand.** The generator qualified three pages on one incidental token each
("wrong", "approval", "bill"). Two were refused under rule 12 and replaced with `/your-ai-bill-grew-
165-you-cut-the-work/` and `/your-200-cap-still-buys-2-85x/` (both live, both ≥2 shared subject
tokens), keeping `/the-cloud-bill-break-even-when-renting-servers-stops-paying/`. Written to the
artifact, the Supabase `content` and post 1738 in that order, then a draft→publish toggle to fire the
front's rebuild.

## Costs

Image credits: 18 (paper collage + two overlay revisions) + 5 (cinematic still) = 23. No image
regenerated after acceptance.

## Open items

1. `illustration_overlay.py` re-derives its copy from the article and ignores a cleared hook in
   `featured.json`, so "shorten the hook" is not reachable without code change.
2. The art director's picture-desk review passed a collage whose type block was unreadable — the
   legibility of the composite is only checked by a human eye, not by code.
3. `internal_links.py` still qualifies on a single incidental token (rule 12's known weakness).
4. `check_social_voice.mjs` still reds the repo on four pre-existing 2026-11-08/09 drafts, none of
   them this artifact.
