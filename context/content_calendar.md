# Content Calendar

Cadence per vertical. The Editor-in-Chief dispatches the Radar Scout on these schedules.

| Vertical | Cadence | Day/Time (EST) | Status |
|---|---|---|---|
| agentic_ai | 2×/week | Mon + Thu 06:00 | active |
| enterprise_tech_leadership | 1×/week | Tue 06:00 | active |
| gpu_hardware | 1×/week | Wed 06:00 | active |
| supply_chain | 1×/week | Thu 06:00 | active |
| home_systems_reno | 1×/week | Fri 06:00 | active |

## Run log
| Date | Vertical | Result | Notes |
|---|---|---|---|
| 2026-09-03 | supply_chain | draft complete; halted at frontier gate (kie.ai down) | Winner: customs-enforcement-operational-risk (8.3). 5/5 claims VERIFIED, 0 removed. Draft written; Claude humanizer blocked by kie.ai "Internal error" (15+ retries). Editor re-checked 06:17 UTC — upstream still hard-down (credit 200/933.2 cr; messages 502); pre-flight scripted at scripts/kie_healthcheck.sh. |
| 2026-09-03 | agentic_ai | draft complete; halted at frontier gate (kie.ai hard-down) | Winner: OWASP GenAI LLM Top 10 2026 — Excessive Agency → No.3 (9.0). 5/5 claims VERIFIED, 0 removed. Draft + verified brief in recon_proposals/ + drafts/. Claude rewrite blocked by kie.ai "Internal error" (valid key, 933.2 cr). |
| 2026-09-04 | home_systems_reno | draft complete; halted at frontier gate (kie.ai hard-down, 3rd consecutive day) | Winner: electrification-rebate-window-closes (8.5). 7/7 claims VERIFIED, 0 removed. HEAR fuel-switching rebate ended Sept 1 + 25C credit expired Dec 31. Draft passes verify.sh; Claude rewrite blocked by kie.ai 502/503 "Internal error" (credit 200/933.2 cr). Re-queue final humanize when gateway recovers. |
