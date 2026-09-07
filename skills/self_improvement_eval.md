# SKILL: Self-Improvement Eval (Self-Healing SOPs)

## 1. Objective
Every failed or degraded run must produce a patch to one of the `skills/*.md` files so the
failure class never recurs. This is a hard factory rule carried over from the software factory.

## 2. Protocol
After any run that produced: zero candidates, a sub-8 winner, removed claims, a failed
human-voice gate, a missing-key halt, or a distribution error —
1. Identify the **failure class** (not the single incident).
2. Find the owning skill and the owning stage.
3. Patch that skill with the concrete prevention (a query pattern, a source whitelist, a new
   negative constraint, a key-check precondition).
4. Record a one-line entry in this file's log section.

## 3. Log
| Date | Failure class | Patched skill | Fix |
|---|---|---|---|
| 2026-09-03 | Frontier gateway (kie.ai) hard-down: credit endpoint 200 (key valid) but `/claude/v1/messages` returns HTTP 403 "Internal error, please try again later" across 15+ retries (both `claude-sonnet-5` and `Claude-Opus-4-8`) | `claude_humanizer.md` | Added pre-flight ping precondition, documented 403 (not just 502/503) as an instability code, and pinned the working auth convention (`Authorization: Bearer <key>` / `x-api-key: Bearer <key>`; raw key via `x-api-key` returns HTTP 200 with a 401 body). |
| 2026-09-03 | Frontier gateway (kie.ai) hard-down, stylist route: `no_available_account` (HTTP 200 + JSON error body) and empty-stream on streaming mode; dated model IDs return "page does not exist" | `claude_humanizer.md` (+ stylist config, Hermes `runtime_provider.py`) | Documented non-streaming requirement (`model.streaming: false`), `no_available_account` as a hard-down code, and alias-only model IDs. Fixed stylist profile to `provider: anthropic` + `base_url: https://api.kie.ai/claude` and whitelisted `api.kie.ai` in `_anthropic_base_url_override_ok`. |
| 2026-09-04 | Frontier gateway (kie.ai) hard-down, 3rd consecutive day (Sept 2–4); scout→draft still runs on deepseek and holds at Loop 3 | `claude_humanizer.md` | Clarified the outage playbook: run scout→draft on schedule (30-day freshness is the scarce resource), pre-flight `scripts/kie_healthcheck.sh` immediately before Loop 3 only — do not gate the sweep on the gateway. |
| 2026-09-07 | Same-week vertical re-run produced only retreads: the 09-04 home_systems_reno run already won the 30-day window's sharpest acute story (HEAR fuel-switching rule death / 25C expiry / Sept 1 deadline), so a re-run 3 days later had no fresh ≥8 candidate (best was 7.2–7.7; a 7.9 contrarion hook failed the anchor-freshness gate — data dated Jul 13, out of window). Correctly returned NO PUBLISH, no padding. | `virality_judge.md` | Added §3.5 Prior-cycle thesis de-dup (HARD check): compare each candidate against prior-30-day angle briefs + published/drafted articles for the vertical; same-thesis candidates are retreads → cap Novelty at 6.0; if the window barely advanced and nothing fresh clears it, return "no publish" rather than rating a retread's novelty high. Also codified the anchor-freshness rule (out-of-window load-bearing date = drop). |
| 2026-09-07 | Radar `after:`/`since:` date operator silently ignored by the web_search backend: a nearshoring query with `after:<window_start>` returned zero results while date-agnostic phrasing returned results. Recovered by re-framing to site:/period-phrase queries, but the skill's Stage-2 templates still instruct date-filtered syntax that can return an empty set on a healthy source. | `radar_30day.md` | Added §3 Stage-2 backend note: the search backend may silently drop `after:`/`since:` filters (can yield empty result sets); run a date-agnostic site:/"past month"/"last 30 days" phrasing fallback for every angle, then timestamp-check each hit against the window rather than trusting the operator. |
| 2026-09-07 | Loop 3 whole-rewrite over-compressed a fully-sourced brief: Gemini collapsed three brief-sourced, persona-specific ops moves into one and cut the piece below the ~800-word long-form floor (691 body words). Voice was clean but operational depth for the persona was lost; two secondary figures ($400M CAT duties, $750M Deere net) were introduced and later removed as unverified. | `claude_humanizer.md` | Added a preservation rule: keep each section's distinct, brief-sourced action items — do not merge or drop a numbered move — and a post-rewrite length check against the draft (final must not fall materially below the draft/floor; restore depth from the verified brief, never pad new claims). Reaffirmed: only VERIFIED-brief figures may appear; no secondary-derived sums. |

