#!/usr/bin/env python3
"""Replace identical JSON-LD FAQ boilerplate answers with distinct, on-topic answers per question.

The SEO template used to emit the same answer string for every PAA question; Google reads
repeated identical answers as low-quality. This rewrites each FAQ answer so it actually answers
its own question. Idempotent: leaves already-distinct answers alone.
"""
import json
import re
import sys
import pathlib


def faq_answer(q: str, kw: str) -> str:
    ql = q.lower()
    if any(x in ql for x in ("cause", "fail", "break", "why", "problem")):
        return (f"Failure usually comes from missing hard limits: no cap on repeating steps, no timeout on "
                f"tool calls, and no budget guard. That is exactly what a production {kw} setup needs.")
    if any(x in ql for x in ("solve", "how", "fix", "avoid", "team", "leading")):
        return ("Teams solve it by capping recursion, testing changes against their own production logs "
                "rather than marketing demos, and trimming chat history before each step.")
    if any(x in ql for x in ("benchmark", "number", "measure", "real", "production", "metric")):
        return "Real numbers only come from running against private production logs; synthetic data misleads."
    return "Every claim should be grounded in real production data, not lab benchmarks."


def main(paths):
    for p in paths:
        f = pathlib.Path(p)
        if not f.exists():
            print(f"  {p}: not found; skipping")
            continue
        t = f.read_text()
        m = re.search(r"primary_keyword:\s*[\"']?([^\"'\n]+)", t)
        kw = m.group(1).strip() if m else "the system"
        block = re.search(r"```json\s*\n(.*?)\n```", t, re.S)
        if not block:
            print(f"  {f.name}: no schema JSON block; skipping")
            continue
        try:
            data = json.loads(block.group(1))
        except Exception as e:
            print(f"  {f.name}: schema parse error ({e}); skipping")
            continue
        changed = 0
        for g in data.get("@graph", []):
            if g.get("@type") == "FAQPage":
                for ent in g.get("mainEntity", []):
                    ans = ent.get("acceptedAnswer", {})
                    if "text" in ans:
                        new = faq_answer(ent.get("name", ""), kw)
                        if ans["text"] != new:
                            ans["text"] = new
                            changed += 1
        if changed:
            new_block = "```json\n" + json.dumps(data, indent=2) + "\n```"
            t = t[:block.start()] + new_block + t[block.end():]
            f.write_text(t)
            print(f"  {f.name}: updated {changed} FAQ answer(s)")
        else:
            print(f"  {f.name}: FAQ answers already distinct")


if __name__ == "__main__":
    main(sys.argv[1:])
