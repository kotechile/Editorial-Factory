# Published Log

Append-only record of articles that cleared the `@Simon approve` gate and were copied into
`published/`. Ground truth for "is it live?" is `published/*.md` itself — this table must never
list a file that is not there. Audited 2026-09-12.

| Date | Vertical | Slug | Headline | Live URL |
|---|---|---|---|---|
| 2026-09-03 | supply_chain | customs-enforcement-operational-risk | On Sept 18, a stale address can void your importer number and stop your cargo at the port | https://pressflow.aichieve.net/published/2026-09-03_customs-enforcement-operational-risk.md |
| 2026-09-04 | home_systems_reno | electrification-rebate-window-closes | The federal rebate for swapping your gas furnace for a heat pump just died | https://pressflow.aichieve.net/published/2026-09-04_electrification-rebate-window-closes.md |
| 2026-09-07 | agentic_ai | anthropic-multiagent-turf-war | Anthropic's own red team watched three Claude agents sabotage each other with self-replicating malware — no attacker required | https://pressflow.aichieve.net/published/2026-09-07_anthropic-multiagent-turf-war.md |
| 2026-09-07 | supply_chain | ieepa-refund-wave-hits-earnings | The $166B tariff clawback is finally hitting earnings — and the biggest check was never filed | https://pressflow.aichieve.net/published/2026-09-07_ieepa-refund-wave-hits-earnings.md |

## Corrections (2026-09-12 integrity audit)

- Removed duplicate rows: `customs-enforcement-operational-risk` (09-03) and
  `electrification-rebate-window-closes` (09-04) were each logged twice.
- `owasp-excessive-agency-2026` (09-03) was previously logged here as published. It is **not**
  published — it exists only as `context/drafts/2026-09-03_owasp-excessive-agency-2026_final.md`
  and never cleared the approval gate. Corrected to a pending draft below.
- Replaced the placeholder `local/site` target with the resolvable reader URL for each row.

## Awaiting approval — NOT published

Final drafts written by the pipeline that are still held at the `@Simon approve` gate
(`context/drafts/`):

| Date | Vertical | Slug |
|---|---|---|
| 2026-09-03 | agentic_ai | owasp-excessive-agency-2026 |
| 2026-09-08 | enterprise_tech_leadership | cloud-repatriation-roi-calculator-bare-metal |
| 2026-09-08 | enterprise_tech_leadership | mckinsey-ai-roi-flat-build-vs-buy-flip |
| 2026-09-08 | agentic_ai | mcp-server-implementation-python |
| 2026-09-09 | gpu_hardware | nvidia-279b-memory-bottleneck |
| 2026-09-10 | agentic_ai | google-agents-challenge-four-patterns |
| 2026-09-10 | supply_chain | reshoring-capacity-gap |
| 2026-09-11 | home_systems_reno | nys-weatherized-tier-heat-pump-rebate |
