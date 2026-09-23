# Signals: agentic_ai — 2026-09-21

**Window:** 2026-08-22 → 2026-09-21
**Queries run:** 11 (web_search + web_extract across MCP spec/repos, vendor changelogs, arXiv, vendor newsrooms, Hacker News/The New Stack/Substack)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | MCP gains an official **Skills extension** (`io.modelcontextprotocol/skills`): SEP-2640 marked **Final**, PR #2640 merged into the spec | https://modelcontextprotocol.io/seps/2640-skills-extension + https://github.com/modelcontextprotocol/ext-skills | 2026-09-13 | Status: Final; "PR #2640 merged 2026-09-13"; a skill = directory of files (minimally SKILL.md) served as MCP resources under `skill://` | tool use / MCP protocol fabric | 90 |
| 2 | Skills served via the existing **Resources primitive**: `skills/list` (enumerate) + `skills/get` (fetch by URI) + optional `resources/directory/read`; format delegated to the Agent Skills spec | https://modelcontextprotocol.io/extensions/skills/overview | 2026-09 | "This SEP defines only the transport binding"; digests + byte sizes bind approvals | tool use / MCP protocol fabric | 85 |
| 3 | Motivation: **fragmented distribution** — a server and the skill teaching an agent to use it are "versioned, discovered, and installed separately"; **instruction size limits** — server instructions are practically bounded, and an 875-line `mcpGraph` skill does not fit | https://modelcontextprotocol.io/seps/2640-skills-extension | 2026-09-13 | 875-line mcpGraph skill; fragmented discovery | deterministic RPC boundaries / protocol fabric | 78 |
| 4 | Security model: skill content is **untrusted input**; code execution & `allowed-tools` need per-skill approval; ≤512 files / 16 MiB per skill; archives removed during review (decompression-bomb / path-traversal surface) | https://modelcontextprotocol.io/extensions/skills/overview | 2026-09 | 512 files / 16 MiB cap; "Treat skill content as untrusted input" | deterministic RPC boundaries / zero-trust | 75 |
| 5 | Claude Code 2.1.259 (Sept 3) adds **`managedMcpServers`** (orgs inject HTTP/SSE MCP servers to every user, same shape as `.mcp.json`) + **`--permission-prompts none`** (deny-by-default for unattended headless hosts) | https://releasebot.io/updates/anthropic/claude-code (mirrors https://code.claude.com/docs/en/changelog) | 2026-09-03 | managedMcpServers; `--permission-prompts none`; GitLab MR recognition | deterministic RPC boundaries / multi-agent coordination | 80 |
| 6 | Apple Xcode 26.3 introduces **native Claude Agent SDK integration** — full Claude Code harness (subagents, background tasks, plugins) inside the IDE | https://www.anthropic.com/news/apple-xcode-claude-agent-sdk | 2026-09 (RC) | harness = portable primitive embedded in a major IDE | distributed microservices architecture | 72 |
| 7 | "Researchers found that **1 in 5 MCP access policies came back broken or missing**" — enterprise MCP authorization hardening | https://thenewstack.io/mcp-gets-its-missing-enterprise-authorization-layer | 2026-09-10 | >20% of MCP access policies fail to enforce controls | tool use / MCP fabric (security) | 70 |
| 8 | DeepSeek V4.1-Flash (Sept 10): 552B multimodal model with **4× KV-cache memory reduction** for long-running agents (memory cost cut to 25%) | https://local-ai-zone.github.io/blog/September_2026_AI_Model_Updates.html | 2026-09-10 | 4× KV-cache reduction; 25% memory cost | memory tiering / subagent cost optimization | 68 |

**Dropped — outside 30-day window (freshness rule):**
- MCP 2026-07-28 "stateless core" spec — July 28, precedes window start (also already logged as out-of-window on 2026-09-17).
- Anthropic "Agent Skills" open standard (agentskills.io) — Dec 18, 2025, out of window (background lineage only).
- MEMTIER tiered-memory arXiv:2605.03675 — May 2026, out of window.
- NIST AI Agent Standards Initiative — Feb 17, 2026, out of window.

**Dropped — intensity < 60:** none.
