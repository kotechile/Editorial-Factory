# Run log — 2026-11-18 — agentic_resilience_failure (EVERGREEN)

**Slug:** `your-p99-is-a-product` · **Title:** "Your Timeout Is the Wrong Knob: 1 Turn in 9"
**Track:** evergreen (`skills/evergreen_topics.md`) · **Cadence:** `30 17 * * 3` · **Persona:** infra_engineer
**Destinations:** published/ artifact, published_log, Supabase row `de51dbb0-b8e2-4186-b4bf-5d27f183d60e`,
sitemap, CMS post 1776 (aichieve.net, status publish, media 1775, vertical term 15, kind tag 44).

## Gate (STEP 0)
`generation_gate.py --mode evergreen --vertical agentic_resilience_failure` → GENERATION OK (control=supabase, vertical=file).

## Topic selection (evidence, not invention)
- Vertical `primary_angles`: "compound reliability math", "cascading error containment" — taken at the **latency**
  axis, which this vertical had priced only at the error axis.
- Persona `infra_engineer` wants: "real numbers, caveats, reproduction details".
- `founder-voice.md` §3 (agentic_resilience_failure): "Cascading Error Loops … re-trying a failed strategy
  without backtracking" read as *what a duplicate costs*.
- Corpus grep (`hedge`, `p99`, `in flight`) found no prior artifact: the 13 published pieces in this vertical
  cover errors, undo, replay, admission, detection, recovery validity — none covers a copy sent *before* a failure.
- GSC 2026-11-11: candidate count 0 → neutral signal, no veto.

## Evergreen gate
Brief `context/recon_proposals/2026-11-18_agentic_resilience_failure_evergreen_brief.md`.
PASS: rows=6 fetched=6 sources=4 hosts=4, decision sha1:8dd6d64516, dedup matched
`2026-11-18_your-transcript-says-do` (180-day window). Hosts: raw.githubusercontent.com, grpc.io,
sre.google, nginx.org. Composite 8.6 (U9 D9 E8 A8).
Fetchability finding: `barroso.org`, `research.google.com/pubs/archive`, CACM, and three university PDF
mirrors of "The Tail at Scale" all return empty text through the verifier — no PDF anchor on this beat.

## Draft → frontier
Structural draft → `readability_critic` (structure fail: tldr needed "The architectural rule"), accessibility
Flesch 51.2 with an undefined `POST` and a 7-word H2 → rewritten to plainer words and shorter sentences
(Flesch 63.5). Headline: 100/100 STRONG, lead_ok True after planting "wrong"/"knob" in the lead
("Your Timeout Is the Wrong Knob: 1 Turn in 9").
Frontier (Loop 3): attempt 1 **ACCEPT**, hard=0, regressions=0, rhythm 7.9, health 0.939, Flesch 64.6.
Hand repairs after the rewrite: **re-added the inline internal link it stripped**
(`/agent-timeout-false-alarm-budget/`), and labelled the expected-max arithmetic as ours.
`run_pipeline.py gate`: 8/8 pass (accessibility, shape, critic, headline, sources, review_audit, voice, publish_gate).

## Arithmetic used (derived, labelled as ours in the body)
- 1 − (1 − 0.01)^12 = 11.4% (≈ 1 turn in 9); at k=20 → 18.2%.
- Expected slowest of k draws ≈ H_k × mean: H_12 = 3.103 × 800 ms = 2.48 s.
- gRPC throttle: maxTokens 10, tokenRatio 0.1, threshold maxTokens/2 = 5 → one failure costs 10 successes;
  quiet at ≈10% failure rate.
- gRPC hedge ladder at 0.5 s: 1 RPC at 1 ms, 2 at 501 ms, 3 at 1001 ms, 4 at 1501 ms (maxAttempts 4).

## Publish + verification (on the rendered front, not the CMS)
- post 1776 live; https://aichieve.net/your-p99-is-a-product/ returned **404 at t+0 (build lag), 200 at t+2 min**.
- hero `your-p99-is-a-product-featured.jpg`, og:image set, `-1024x576` derivative in srcset, alt 136 chars.
- internal links rendered: `/agent-timeout-false-alarm-budget/` ×2 (inline + related), `/gate-the-step-not-the-model/`,
  `/retry-permission-leaves-the-caller/`. publish.py's own delivery line printed "0 internal link(s)" because it
  counts the block before the static rebuild; the live HTML carries them.
