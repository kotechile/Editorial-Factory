#!/usr/bin/env python3
"""The pipeline spine: one command per mechanical step, so the agent spends its turns on judgment.

Why this exists: a run used to explore the repo by hand — `ls`, `grep`, ten `sed` reads of the gate
sources, four separate `verify.sh` invocations — and every one of those results then rode in the
context of ~94 API calls. That is 40% cache-read and 37% output on the fleet's bill for work a script
does deterministically and for free.

    python3 scripts/run_pipeline.py start      --vertical <id> --mode news|evergreen|review
    python3 scripts/run_pipeline.py seed       --vertical <id>                 # news only
    python3 scripts/run_pipeline.py gate-brief --vertical <id> --mode evergreen|review
    python3 scripts/run_pipeline.py review     --vertical <id> [--draft path]
    python3 scripts/run_pipeline.py gate       [--file path | --slug slug]
    python3 scripts/run_pipeline.py publish    --file path
    python3 scripts/run_pipeline.py finish

`start` prints a compact context pack (<= ~1,500 chars): the vertical, its persona and angles, the
three titles it must not repeat, the artifact paths, and the next command. It replaces the ten turns
of archaeology. `gate` runs the whole push-blocking battery and prints **failures plus one line per
gate** — nothing else, because its output is context too.

Exit codes: 0 ok · 1 a gate holds · 2 bad input. Nothing here writes an article.
"""
from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
DATE = datetime.date.today().isoformat()

MODES = ("news", "evergreen", "review")
SKILL = {"news": "skills/radar_30day.md", "evergreen": "skills/evergreen_topics.md",
         "review": "skills/review_comparison.md"}


# ------------------------------------------------------------------------------------------ helpers

def run(cmd: list[str], timeout: int = 900) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except subprocess.TimeoutExpired:
        return 124, f"timed out after {timeout}s: {' '.join(cmd)}"


def verticals() -> dict:
    data = json.loads((ROOT / "context" / "verticals.json").read_text())
    return {v["id"]: v for v in data.get("verticals", [])}


def personas() -> dict:
    try:
        return json.loads((ROOT / "context" / "personas.json").read_text())
    except (OSError, ValueError):
        return {}


def recent_titles(vertical: str, limit: int = 3) -> list[str]:
    """The last few published titles for this vertical — the de-dup check, without grepping 2.7 MB."""
    out: list[str] = []
    for path in sorted((ROOT / "published").glob("*.md"), reverse=True):
        text = path.read_text(encoding="utf-8", errors="ignore")[:900]
        if f"vertical: {vertical}" not in text:
            continue
        m = re.search(r"^title:\s*[\"']?(.+?)[\"']?$", text, re.M)
        out.append(f"{path.name[:10]} {(m.group(1) if m else path.stem)[:70]}")
        if len(out) >= limit:
            break
    return out


def one_today(pattern: str) -> pathlib.Path | None:
    hits = sorted((ROOT / "context" / "recon_proposals").glob(f"{DATE}_{pattern}"))
    if len(hits) == 1:
        return hits[0]
    return None


def artifact_for(slug_or_file: str) -> pathlib.Path | None:
    p = pathlib.Path(slug_or_file)
    if p.exists():
        return p if p.is_absolute() else ROOT / p
    for cand in (ROOT / "published").glob(f"*_{slug_or_file}.md"):
        return cand
    for cand in (ROOT / "context" / "drafts").glob(f"*_{slug_or_file}_final.md"):
        return cand
    return None


# -------------------------------------------------------------------------------------------- start

def cmd_start(args) -> int:
    reg = verticals()
    v = reg.get(args.vertical)
    if not v:
        print(f"unknown vertical '{args.vertical}' — ids: {', '.join(sorted(reg)[:12])} …")
        return 2
    mode = args.mode
    if mode == "review" and not v.get("review_cadence"):
        print(f"{args.vertical} has no review cadence; modes are news/evergreen")
        return 2
    persona = v.get("target_persona") or v.get("persona", "")
    pdata = personas().get(persona) if isinstance(personas(), dict) else None
    wants = ""
    if isinstance(pdata, dict):
        w = pdata.get("wants") or pdata.get("pain_points") or ""
        wants = (w if isinstance(w, str) else "; ".join(map(str, w)))[:220]
    angles = v.get("primary_angles") or []
    angles = [a if isinstance(a, str) else str(a) for a in angles][:4]
    frontends = v.get("target_domain") or v.get("frontends") or v.get("frontend") or ""
    print(f"vertical  {args.vertical} — {v.get('label', args.vertical)}")
    print(f"mode      {mode}   (skill: {SKILL[mode]}; casebooks under skills/references/ only on demand)")
    row = [f"persona   {persona or 'n/a'}"]
    if wants:
        row.append(f"wants     {wants}")
    if frontends:
        row.append(f"surface   {frontends if isinstance(frontends, str) else ' '.join(frontends)}")
    print("\n".join(row))
    if angles:
        print("angles    " + " | ".join(a[:60] for a in angles))
    titles = recent_titles(args.vertical)
    if titles:
        print("no repeat " + " · ".join(titles))
    if mode == "news":
        print(f"artifacts context/recon_proposals/{DATE}_{args.vertical}_signals.md → _angle_brief.md →"
              f" _verified_brief.md → context/drafts/{DATE}_<slug>_draft.md → _final.md")
    else:
        print(f"artifacts context/recon_proposals/{DATE}_{args.vertical}_{mode}_brief.md →"
              f" _{mode}_verified_brief.md → context/drafts/{DATE}_<slug>_draft.md → _final.md")
    print("gates     accessibility Flesch>=50 (target 60) · article_shape · readability_critic ·"
          " headline 100/100 · source_gate · publish_gate (one `gate` call runs all of them)")
    print("rules     no skill appends (use scripts/learn.py) · probe a new host first"
          " (scripts/host_probe.py --check URL) · persistence is not approval-gated")
    nxt = (f"python3 scripts/run_pipeline.py seed --vertical {args.vertical}" if mode == "news"
           else f"python3 scripts/run_pipeline.py gate-brief --vertical {args.vertical} --mode {mode}")
    print(f"next      {nxt}")
    return 0


# --------------------------------------------------------------------------------------------- steps

def cmd_seed(args) -> int:
    path = pathlib.Path(args.signals) if args.signals else one_today(f"{args.vertical}_signals.md")
    if not path or not path.exists():
        print(f"no signals file for {args.vertical} on {DATE} — write the radar file first "
              f"(context/recon_proposals/{DATE}_{args.vertical}_signals.md)")
        return 2
    rc, out = run([sys.executable, str(SCRIPTS / "synthesize_topics.py"), "--seed", str(path)])
    print(out.strip().splitlines()[-1] if out.strip() else "(no output)")
    return rc


def cmd_gate_brief(args) -> int:
    suffix = "_review_brief.md" if args.mode == "review" else "_evergreen_brief.md"
    path = pathlib.Path(args.brief) if args.brief else one_today(f"{args.vertical}{suffix}")
    if not path or not path.exists():
        print(f"no {args.mode} brief today for {args.vertical} "
              f"(expected context/recon_proposals/{DATE}_{args.vertical}{suffix})")
        return 2
    script = "review_gate.py" if args.mode == "review" else "evergreen_gate.py"
    rc, out = run([sys.executable, str(SCRIPTS / script), "--brief", str(path)])
    lines = out.strip().splitlines()
    keep = [ln for ln in lines if re.search(r"PASS|FAIL|rows=|verdict|no publish", ln, re.I)]
    print("\n".join(keep[-14:]) or "(no verdict parsed)")
    return rc


def cmd_review(args) -> int:
    draft = pathlib.Path(args.draft) if args.draft else None
    if draft is None:
        hits = sorted((ROOT / "context" / "drafts").glob(f"{DATE}_*_draft.md"))
        hits = [h for h in hits if h.name.replace("_draft.md", "_final.md") not in
                {p.name for p in (ROOT / "context" / "drafts").glob("*_final.md")}] or hits
        if len(hits) != 1:
            print("pass --draft explicitly; today's drafts: "
                  + ", ".join(h.name for h in hits) if hits else "no draft today")
            return 2
        draft = hits[0]
    cmd = [sys.executable, str(SCRIPTS / "article_reviewer.py"), "--draft", str(draft)]
    brief = None
    for cand in (ROOT / "context" / "recon_proposals").glob(f"{DATE}_*_brief.md"):
        brief = cand
    if brief and "_verified" in brief.name:
        cmd += ["--brief", str(brief)]
    rc, out = run(cmd, timeout=2400)
    for line in out.strip().splitlines():
        if line.strip().startswith("attempt") or "wrote" in line or "HELD" in line:
            print(line.strip())
    print(f"review {'ACCEPTED' if rc == 0 else 'HELD'} — report: "
          f"context/drafts/reviews/{draft.name.replace('_draft.md', '')}_review.md")
    return rc


# ---------------------------------------------------------------------------------------------- gate

def _title_of(text: str) -> str:
    m = re.search(r"^title:\s*[\"']?(.+?)[\"']?$", text, re.M)
    return m.group(1) if m else ""


def cmd_gate(args) -> int:
    path = artifact_for(args.file or args.slug) if (args.file or args.slug) else None
    if path is None:
        finals = sorted((ROOT / "context" / "drafts").glob(f"{DATE}_*_final.md"))
        path = finals[0] if len(finals) == 1 else None
    if path is None or not path.exists():
        print("gate: pass --file or --slug (no single artifact for today)")
        return 2
    text = path.read_text(encoding="utf-8", errors="ignore")
    name = path.name
    failures: list[str] = []
    summary: list[str] = []

    def gate(label: str, cmd: list[str], timeout: int = 600) -> None:
        rc, out = run(cmd, timeout=timeout)
        first_fail = next((ln.strip() for ln in out.splitlines()
                           if re.search(r"FAIL|HELD|VERDICT: FAIL", ln)), "")
        ok = rc == 0
        summary.append(f"{'ok  ' if ok else 'HOLD'} {label:16s} {'' if ok else first_fail[:90]}")
        if not ok:
            failures.append(f"{label}: {first_fail or out.strip().splitlines()[-1][:120]}")

    py = sys.executable
    gate("accessibility", [py, str(SCRIPTS / "check_accessibility.py"), "--floor", "50", str(path)])
    gate("shape", [py, str(SCRIPTS / "article_shape.py"), "--check", str(path)])
    gate("critic", [py, str(SCRIPTS / "readability_critic.py"), "--check", str(path)])
    title = _title_of(text)
    if title:
        gate("headline", [py, str(SCRIPTS / "headline_score.py"), title])
    gate("sources", [py, str(SCRIPTS / "source_gate.py"), "--file", str(path)], timeout=900)
    draft = path.with_name(name.replace("_final.md", "_draft.md"))
    if draft.exists():
        gate("review_audit", [py, str(SCRIPTS / "review_audit.py"), "--draft", str(draft),
                              "--final", str(path)])
    rc, out = run(["node", "scripts/check_social_voice.mjs", "--json"], timeout=300)
    try:
        problems = json.loads(out[out.index("{"):]).get("problems", [])
    except ValueError:
        problems = []
    mine = [p for p in problems if name in json.dumps(p)]
    other = len(problems) - len(mine)
    summary.append(f"{'ok  ' if not mine else 'HOLD'} {'voice':16s} "
                   + ("" if not mine else str(mine[0])[:90])
                   + (f" ({other} pre-existing elsewhere)" if other else ""))
    if mine:
        failures.append(f"voice: {mine[0]}")
    gate("publish_gate", [py, str(SCRIPTS / "publish_gate.py"), "--file", str(path)], timeout=900)

    print(f"gate {name}")
    print("\n".join("  " + s for s in summary))
    if failures:
        print("\nHOLDS:")
        print("\n".join("  - " + f for f in failures))
        return 1
    print("\nall gates pass — persist with `run_pipeline.py publish --file <path>`")
    return 0


def cmd_publish(args) -> int:
    path = artifact_for(args.file)
    if not path:
        print(f"no artifact for {args.file}")
        return 2
    rc, out = run([sys.executable, str(SCRIPTS / "publish.py"), str(path)], timeout=1800)
    print("\n".join(out.strip().splitlines()[-25:]))
    return rc


def cmd_finish(args) -> int:
    rc, out = run(["bash", "scripts/verify.sh"], timeout=1800)
    fails = [ln for ln in out.splitlines() if re.search(r"^\s*(FAIL|✗)|FAIL:", ln)]
    print("\n".join(fails[:20]) or "verify.sh: green")
    print(f"exit {rc}")
    return rc


# ----------------------------------------------------------------------------------------------- cli

def main() -> int:
    ap = argparse.ArgumentParser(description="Editorial pipeline spine (one command per step)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("start"); p.add_argument("--vertical", required=True)
    p.add_argument("--mode", default="news", choices=MODES); p.set_defaults(fn=cmd_start)

    p = sub.add_parser("seed"); p.add_argument("--vertical", required=True)
    p.add_argument("--signals", default=""); p.set_defaults(fn=cmd_seed)

    p = sub.add_parser("gate-brief"); p.add_argument("--vertical", required=True)
    p.add_argument("--mode", default="evergreen", choices=("evergreen", "review"))
    p.add_argument("--brief", default=""); p.set_defaults(fn=cmd_gate_brief)

    p = sub.add_parser("review"); p.add_argument("--vertical", required=True)
    p.add_argument("--draft", default=""); p.set_defaults(fn=cmd_review)

    p = sub.add_parser("gate"); p.add_argument("--file", default="")
    p.add_argument("--slug", default=""); p.set_defaults(fn=cmd_gate)

    p = sub.add_parser("publish"); p.add_argument("--file", required=True); p.set_defaults(fn=cmd_publish)
    p = sub.add_parser("finish"); p.set_defaults(fn=cmd_finish)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
