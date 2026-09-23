---
title: "Skills Just Joined MCP — and That Changes How Agents Reuse Work"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "Skills — portable bundles of workflow instructions — became an official MCP extension on September 13, standardizing how agents discover, retrieve, and verify reusable procedures."
date: 2026-09-21
slug: mcp-skills-extension
---

<!-- lead -->
On September 13, 2026, the maintainers of the Model Context Protocol (MCP) merged SEP-2640, turning "skills" — the folders of markdown instructions that teach an agent a repeatable workflow — into an official, vendor-neutral protocol extension. A skill is now a directory of files, exposed to any MCP client as ordinary resources under a `skill://` URI and discovered through two new methods: `skills/list` and `skills/get` [1][2].

<!-- tension -->
**Why it matters:** The agent stack has been quietly splitting into two standardized layers. MCP answers one question — how does an agent connect to tools and data. Skills answer a different one — how does an agent learn a procedure.

MCP became the de facto tool standard after Anthropic donated it to the Linux Foundation in December 2025. Skills stayed fragmented. Anthropic published the Agent Skills format at agentskills.io, but a server and the skill that teaches an agent to use it were "versioned, discovered, and installed separately" [1]. Server instructions were practically bounded, so a real workflow like the 875-line `mcpGraph` skill could not ship alongside the tool it described [1].

SEP-2640 closes that gap by standardizing only the transport — how skills are served and retrieved — while leaving the skill *format* to the existing Agent Skills specification [3].

**By the numbers:**
- **875 lines:** the `mcpGraph` skill, a real workflow too large for the bounded `instructions` field servers were previously limited to — the exact problem this extension solves [1].
- **3 methods:** `skills/list` (enumerate), `skills/get` (fetch one by URI), plus an optional `resources/directory/read` for navigating supporting files [2].
- **512 files / 16 MiB:** the per-skill ceiling servers should stay under, and hosts must support [2].
- **2 layers:** tools (MCP) and procedures (Skills) — the split the extension now formalizes [3].

<!-- tactical-insight -->
**The playbook:** for an architect adopting this, four moves:

- **Model skills as resources, not code.** A skill is just files under `skill://`. Hosts that already treat MCP resources as a virtual filesystem consume skills identically to local folders, so adoption is a read-path change, not a rewrite [1].
- **Bind approvals to digests, not names.** Each entry carries a file manifest with SHA-256 digests and byte sizes. A changed, added, or removed file revokes approval — persist approval against the full file set [2].
- **Treat skill content as untrusted.** Code execution and `allowed-tools` grants require explicit per-skill user approval, and cross-server reads need per-call approval naming both servers [2].
- **Wire the fleet.** Claude Code 2.1.259 (September 3) added `managedMcpServers` — organizations inject HTTP/SSE MCP servers into every user — and `--permission-prompts none`, a deny-by-default mode for unattended headless agents. The same fabric is now reaching fleet management [5].

<!-- nuanced-takeaway -->
**The catch:** This standardizes transport, not format. Directory layout, YAML frontmatter, and the progressive-disclosure model still live in the Agent Skills spec at agentskills.io — so MCP and Agent Skills remain two separate standards that must stay in sync, and a breaking change to one ripples into the other [1][4].

The security burden also lands on hosts. There is no archive form: the maintainers removed it during review because unpacking a remote server's tarball is a decompression-bomb and path-traversal attack surface [1]. Skill content is untrusted input, full stop. The design is deliberately boring — files over resources — and that is exactly the point.

<!-- tldr -->
- **The Big Shift:** MCP now has an official Skills extension (SEP-2640, merged September 13). A "skill" — a folder of workflow instructions — is served as ordinary MCP resources and discovered with two new methods, `skills/list` and `skills/get`.
- **Why It Matters:** The agent stack is standardizing into two vendor-neutral layers — tools (MCP) and procedures (Skills). Skills stop being fragmented, vendor-adjacent folders and become a discoverable, integrity-verified protocol primitive.
- **The Winning Moves:**
  - **Model skills as resources:** read files under `skill://` as a virtual filesystem — a read-path change, not a rewrite.
  - **Bind approvals to digests:** persist approval against SHA-256 digests and byte sizes, so any changed file revokes it.
  - **Treat content as untrusted:** require per-skill approval for code execution and `allowed-tools` grants.
  - **Wire the fleet:** use `managedMcpServers` to inject servers org-wide and `--permission-prompts none` for deny-by-default headless agents.
- **The Catch:** It standardizes transport only — the skill format still lives at agentskills.io, and hosts carry the security burden (untrusted input, no archive form).

## Sources
[1] SEP-2640: Skills Extension — Model Context Protocol — https://modelcontextprotocol.io/seps/2640-skills-extension
[2] Skills — Model Context Protocol — https://modelcontextprotocol.io/extensions/skills/overview
[3] ext-skills repository — Skills Over MCP Working Group — https://github.com/modelcontextprotocol/ext-skills
[4] Agent Skills specification — https://agentskills.io/specification
[5] Claude Code changelog — https://code.claude.com/docs/en/changelog

<!-- linkedin -->
MCP just gained a second primitive. On Sept 13 the maintainers merged SEP-2640, making "skills" — folders of markdown that teach an agent a repeatable workflow — an official, vendor-neutral extension.

A skill is now just files served under a `skill://` URI, discovered with two new methods (`skills/list`, `skills/get`). The agent stack has split into two standardized layers: MCP for tools, Skills for procedures.

Why it matters for architects:
- Skills stop being fragmented folders and become a discoverable, digest-verified protocol resource.
- Approvals bind to SHA-256 digests and byte sizes — change one file, approval is revoked.
- Skill content is untrusted input: code execution and `allowed-tools` need per-skill consent.

The catch: this standardizes transport only. The skill format still lives at agentskills.io, and hosts carry the security burden — there's deliberately no archive form, because unpacking a remote server's tarball is an attack surface.

The same fabric is already reaching fleet management: Claude Code's `managedMcpServers` injects MCP servers org-wide, and `--permission-prompts none` gives headless agents deny-by-default behavior.

Reusable procedures are becoming protocol-level infrastructure. Build against the read path, not a vendor SDK.
