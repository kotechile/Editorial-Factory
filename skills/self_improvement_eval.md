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
| — | — | — | — |
