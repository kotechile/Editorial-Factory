# Verified Brief: agentic_ai — 2026-10-29 (evergreen track)
**Archetype:** evergreen
**Companion to:** `context/recon_proposals/2026-10-29_agentic_ai_evergreen_brief.md` (gate PASS, 7 rows, 4 hosts)
**Topic:** what one sandbox boundary costs per action — substrate choice and warmth, priced from boot time and trajectory length.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | sandbox provisioning cost (independent) | Sandbox init costs a "second-level delay" before execution begins, per tool invocation | VERIFIED | https://arxiv.org/html/2607.23933v2 | "Each tool invocation may incur sandbox initialization overhead — such as image loading, filesystem preparation, namespace configuration, and runtime handshake — introducing a second-level delay before execution begins" |
| 2 | sandbox provisioning cost (independent) | Overlapping the boot with model inference cuts P99 end-to-end latency up to 2.9x against an on-demand baseline | VERIFIED | https://arxiv.org/html/2607.23933v2 | "our prototype demonstrates that SpecBox cuts P99 end-to-end latency by up to 2.9 × 2.9\times relative to the on-demand sandbox baseline" |
| 3 | sandbox provisioning cost (independent) | The same technique cuts peak memory 45.9% against permanently reserved sandboxes | VERIFIED | https://arxiv.org/html/2607.23933v2 | "slashing peak memory consumption by 45.9 % 45.9\% compared to permanently reserved sandbox deployments" |
| 4 | sandbox provisioning cost (independent) | The two naive policies are the horns of the same dilemma | VERIFIED | https://arxiv.org/html/2607.23933v2 | "Persistent long-lived sandbox reservations incur excessive memory overhead at scale, while lazy on-demand instantiation generates severe cold-start penalties that degrade response performance under multi-tenant, multi-turn agent workloads." |
| 5 | substrate comparison (vendor-authored) | Four substrates measured: single containers, hosted sandboxes, Kubernetes-orchestrated containers, cloud VMs | VERIFIED | https://arxiv.org/html/2607.01415v1 | "We present a comparative study of four execution substrates: single containers, hosted sandboxes, Kubernetes-orchestrated containers, and cloud virtual machines." |
| 6 | substrate comparison (vendor-authored) | Cold-start latency varies up to 110x; projected worker-hours spread 1.8x for one million 150-step trajectories | VERIFIED | https://arxiv.org/html/2607.01415v1 | "We find up to 110 × \times variation in cold-start latency and a 1.8 × \times spread in projected worker-hours for one million 150-step trajectories." |
| 7 | substrate comparison (vendor-authored) | Table 1 prices small overheads at scale: 1 s/rollout → 278 h; 100 ms/action over 150 actions → 4,167 h (1M rollouts) | VERIFIED | https://arxiv.org/html/2607.01415v1 | "1 s per rollout 1M rollouts 278 h 10 ms per action 1M × \times 150 actions 417 h 100 ms per action 1M × \times 150 actions 4,167 h" |
| 8 | substrate comparison (vendor-authored) | Hosted sandbox fastest, cloud VMs slowest; the gap compresses to ~1.9x by the longest workload tier | VERIFIED | https://arxiv.org/html/2607.01415v1 | "The hosted sandbox achieves the lowest cold-start latency, followed by the single-container configuration. Kubernetes-orchestrated containers add scheduling overhead, while cloud VMs have the highest provisioning cost in our measured configuration." / "by T2, the cloud VM–hosted-sandbox gap shrinks to approximately 1.9 × \times ." |
| 9 | microVM floor (project docs) | Firecracker boots in under 125 ms, under 5 MiB overhead, up to 150 microVMs per second per host | VERIFIED | https://firecracker-microvm.github.io/ | "Boot in <125ms." / "Create up to 150 microVMs per second per host." / "<5 MiB overhead per VM." |
| 10 | hosted sandbox vendor | Daytona states sandboxes spin up in under 90 ms | VERIFIED | https://www.daytona.io/docs/ | "Sandboxes are the core component of the Daytona platform, spinning up in under 90ms from code to execution and running any code in Python, TypeScript, and JavaScript." |
| 11 | metering (list price) | Sandbox cloud bills per second of running sandbox and sells concurrency in blocks ($500/mo for 600; $1,000/mo for 1,100) | VERIFIED | https://e2b.dev/pricing | "We charge per second of a running sandbox." / "Pro+ — 600 concurrent +$500/mo Pro++ — 1,100 concurrent +$1,000/mo" |

## Provenance notes the drafter must carry

- **Row 5–8's paper is vendor-authored.** All six authors are affiliated with Daytona, whose hosted
  sandbox the paper finds fastest, and the paper is a preprint submitted to ACM SoCC 2026 (not yet
  peer-reviewed). State the affiliation in the same paragraph as the 110x figure. The structural
  finding that survives the conflict of interest is the shape: fixed startup cost dominates short
  trajectories and is amortised by longer ones, and the author's own measurement shows the spread
  compressing to about 1.9x by the longest tier.
- **Row 9 is a design target, not a benchmark.** Firecracker's page publishes the characteristics of
  its own VMM ("Boot in <125ms"); it is AWS's open-source project page. Never present it as an
  independent measurement of the reader's workload.
- **Row 10 is a marketing line** on a vendor docs page; row 11 is a list price read 2026-10-29.
- **Date discipline:** arXiv 2607.01415v1 submitted 01 Jul 2026; arXiv 2607.23933v2 dated 05 Aug 2026;
  prices and project pages read 2026-10-29. Every time-bound figure in the article carries its date or
  an "as of".
- **No hands-on claim.** The desk ran no sandbox, no benchmark and no trace.

## Authorised arithmetic (the desk's own, computed from the cited rows — nothing else)

- Per-action provisioning tax = boot time S ÷ actions N. S = 90 ms over 6 actions → 15 ms per action;
  S = 1,000 ms over 6 actions → about 167 ms per action. Show the division, not a rounded verdict.
- Amortisation check on the paper's own ladder: 100 ms per action × 150 actions = 15 seconds per
  trajectory, which is why its Table 1 prices a per-action millisecond, not a per-run second.
- Do **not** compute a dollar payback for a warm pool: no row prices a sandbox-second except E2B's
  concurrency blocks, and mixing those with a boot time would be a derived ratio no source supports.
