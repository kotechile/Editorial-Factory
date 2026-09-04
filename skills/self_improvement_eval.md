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
