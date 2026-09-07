# Content Calendar

Cadence per vertical. The Editor-in-Chief dispatches the Radar Scout on these schedules.

| Vertical | Cadence | Schedule (EST) | Status |
|---|---|---|---|
| agentic_ai | 0 6 * * 1,4 | Mon + Thu 06:00 AM EST | active |
| enterprise_tech_leadership | 0 6 * * 2 | Tue 06:00 AM EST | active |
| gpu_hardware | 0 6 * * 3 | Wed 06:00 AM EST | active |
| supply_chain | 0 6 * * 4 | Thu 06:00 AM EST | active |
| home_systems_reno | 0 6 * * 5 | Fri 06:00 AM EST | active |

## Run log
| Date | Vertical | Result | Notes |
|---|---|---|---|
| 2026-09-03 | supply_chain | draft complete; halted at frontier gate (kie.ai down) | Winner: customs-enforcement-operational-risk (8.3). 5/5 claims VERIFIED, 0 removed. Draft written; Claude humanizer blocked by kie.ai "Internal error" (15+ retries). Editor re-checked 06:17 UTC — upstream still hard-down (credit 200/933.2 cr; messages 502); pre-flight scripted at scripts/kie_healthcheck.sh. |
| 2026-09-03 | agentic_ai | draft complete; halted at frontier gate (kie.ai hard-down) | Winner: OWASP GenAI LLM Top 10 2026 — Excessive Agency → No.3 (9.0). 5/5 claims VERIFIED, 0 removed. Draft + verified brief in recon_proposals/ + drafts/. Claude rewrite blocked by kie.ai "Internal error" (valid key, 933.2 cr). |
| 2026-09-04 | home_systems_reno | draft complete; halted at frontier gate (kie.ai hard-down, 3rd consecutive day) | Winner: electrification-rebate-window-closes (8.5). 7/7 claims VERIFIED, 0 removed. HEAR fuel-switching rebate ended Sept 1 + 25C credit expired Dec 31. Draft passes verify.sh; Claude rewrite blocked by kie.ai 502/503 "Internal error" (credit 200/933.2 cr). Re-queue final humanize when gateway recovers. |
| 2026-09-07 | agentic_ai | final draft complete; halted at @Simon approve gate (frontier now Gemini) | Winner: anthropic-multiagent-turf-war (9.0). 5/5 claims VERIFIED, 0 removed. Primary: Anthropic FRT "Patterns and problems in emerging multiagent systems" (Aug 13). Frontier rewrite ran on gemini-3.1-pro-preview (kie.ai retired). verify.sh OK. |
| 2026-09-07 | supply_chain | final draft complete; halted at @Simon approve gate (frontier Gemini) | Winner: ieepa-refund-wave-hits-earnings (8.2). 7/7 claims VERIFIED, 0 removed. Primaries: SCOTUS Learning Resources v. Trump (Feb 20), Caterpillar 2Q26 (Aug 4), Deere 3Q26 transcript (Aug 20), Calcbench $18.7B aggregate (Aug 28), Barclay Damon refund-process update. Frontier rewrite on gemini-3.1-pro-preview; verify.sh OK; 836 body words. Held at approval, not distributed. |
| 2026-09-07 | home_systems_reno | **no publish** (weak cycle; virality gate) | 30-day window (Aug 8–Sep 7) had no fresh ≥8 non-retread signal. 09-04 run already won the window's sharpest acute story (fuel-switching rule death / 25C expiry / Sept 1 deadline). Best fresh candidates scored 7.2 (WV $88M HOMES pilot, regional), 7.7 ("surviving money" reframe, retread-risk), 7.9 (heat-pump-demand-without-credit, but anchor data Jul 13 — out of window). Recon written to recon_proposals/2026-09-07_home_systems_reno_signals.md + _angle_brief.md. No draft/humanize/publish. Patched virality_judge.md §3.5 (prior-cycle thesis de-dup) + logged. |
