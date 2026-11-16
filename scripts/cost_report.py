#!/usr/bin/env python3
"""What the editorial pipeline actually cost — per run, per stage, per published article.

Two sources, joined only for the headline number:

  * `context/cost_ledger.jsonl` — every in-pipeline frontier call (article_reviewer, the art
    director, publish_gate's rewrite), written by `frontier_llm._log_usage`. Hermes' own
    accounting cannot see these, because they are subprocess calls.
  * `~/.hermes/state.db` — the agent sessions (source='cron'), which is where the orchestration
    spend lives: ~94 API calls re-reading a ~160k-token prefix.

    python3 scripts/cost_report.py                 # last 14 days
    python3 scripts/cost_report.py --days 30
    python3 scripts/cost_report.py --json          # machine-readable

Prices are the fleet's estimator constants (frontier_llm): cache hit is 50x cheaper than a miss,
which is why the split matters more than the total.
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import pathlib
import sqlite3
import statistics as st
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from frontier_llm import LEDGER, PRICE_IN_HIT, PRICE_IN_MISS, PRICE_OUT  # noqa: E402

DB = os.path.expanduser("~/.hermes/state.db")
EDITORIAL = ("Full Pipeline", "Evergreen Pipeline", "Review Pipeline")


def _ledger_rows(days: int) -> list[dict]:
    if not LEDGER.exists():
        return []
    since = (datetime.datetime.now(datetime.timezone.utc)
             - datetime.timedelta(days=days)).timestamp()
    rows = []
    for line in LEDGER.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except ValueError:
            continue
        if row.get("ts", 0) >= since:
            rows.append(row)
    return rows


def _runs(days: int) -> list[dict]:
    if not os.path.exists(DB):
        return []
    since = (datetime.datetime.now(datetime.timezone.utc)
             - datetime.timedelta(days=days)).timestamp()
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    rows = []
    for title, inp, out, cache, cost, calls, started in con.execute(
            """select title, input_tokens, output_tokens, cache_read_tokens,
                      estimated_cost_usd, api_call_count, started_at
               from sessions where source='cron' and coalesce(input_tokens,0)>0
                 and started_at >= ? order by started_at""", (since,)):
        if not (title or "").startswith(EDITORIAL):
            continue
        rows.append({
            "title": title or "", "in": inp or 0, "out": out or 0, "cache": cache or 0,
            "usd": cost or 0.0, "calls": calls or 0,
            "when": datetime.datetime.fromtimestamp(started, datetime.timezone.utc),
        })
    con.close()
    return rows


def _published(days: int) -> int:
    since = datetime.date.today() - datetime.timedelta(days=days)
    n = 0
    for p in (ROOT / "published").glob("*.md"):
        head = p.name[:10]
        try:
            d = datetime.date.fromisoformat(head)
        except ValueError:
            continue
        if d >= since:
            n += 1
    return n


def _split(row: dict) -> tuple[float, float, float]:
    # The session table does not say which input tokens were hits; the estimator bills the cache
    # fraction at the hit price and the rest at the miss price, which is what this reproduces.
    return row["in"] * PRICE_IN_MISS, row["cache"] * PRICE_IN_HIT, row["out"] * PRICE_OUT


def report(days: int, as_json: bool = False) -> dict:
    runs = _runs(days)
    calls = _ledger_rows(days)
    published = _published(days)
    agent_usd = sum(r["usd"] for r in runs)
    script_usd = sum(c.get("usd") or 0 for c in calls)

    by_stage: dict[str, dict] = {}
    for c in calls:
        key = c.get("stage") or "(unlabelled)"
        agg = by_stage.setdefault(key, {"calls": 0, "usd": 0.0, "in": 0, "out": 0,
                                       "hit": 0, "reasoning": 0})
        agg["calls"] += 1
        agg["usd"] += c.get("usd") or 0
        agg["in"] += c.get("miss") or 0
        agg["out"] += c.get("out") or 0
        agg["hit"] += c.get("hit") or 0
        agg["reasoning"] += c.get("reasoning") or 0

    split = {"in": 0.0, "cache": 0.0, "out": 0.0}
    for r in runs:
        a, b, c = _split(r)
        split["in"] += a
        split["cache"] += b
        split["out"] += c

    out = {
        "days": days,
        "runs": len(runs),
        "published": published,
        "agent_usd": round(agent_usd, 4),
        "script_usd": round(script_usd, 4),
        "total_usd": round(agent_usd + script_usd, 4),
        "usd_per_published": round((agent_usd + script_usd) / published, 4) if published else None,
        "median_run": {
            "calls": st.median([r["calls"] for r in runs]) if runs else 0,
            "in": st.median([r["in"] for r in runs]) if runs else 0,
            "out": st.median([r["out"] for r in runs]) if runs else 0,
            "cache": st.median([r["cache"] for r in runs]) if runs else 0,
            "usd": round(st.median([r["usd"] for r in runs]), 4) if runs else 0,
        },
        "split_usd": {k: round(v, 4) for k, v in split.items()},
        "split_pct": {k: round(100 * v / sum(split.values()), 1) if sum(split.values()) else 0
                      for k, v in split.items()},
        "script_stages": {k: {"calls": v["calls"], "usd": round(v["usd"], 4),
                              "in": v["in"], "out": v["out"], "cache_hit": v["hit"],
                              "reasoning": v["reasoning"]}
                          for k, v in sorted(by_stage.items(), key=lambda kv: -kv[1]["usd"])},
        "last_runs": [{"when": r["when"].strftime("%m-%d %H:%M"),
                       "title": r["title"].split(" · ")[0],
                       "calls": r["calls"], "in": r["in"], "out": r["out"],
                       "cache": r["cache"], "usd": round(r["usd"], 4)} for r in runs[-12:]],
    }
    if as_json:
        return out

    print(f"editorial pipeline — last {days} days")
    print(f"  runs {len(runs)} · published {published} · "
          f"${out['total_usd']:.2f} total ({'$%.2f' % out['usd_per_published'] if out['usd_per_published'] else 'n/a'} per article)")
    med = out["median_run"]
    print(f"  median run: {med['calls']:.0f} calls · in {med['in']:,.0f} · out {med['out']:,.0f} · "
          f"cache {med['cache']:,.0f} · ${med['usd']:.3f}")
    print(f"  agent ${agent_usd:.2f} · in-script ${script_usd:.2f} (ledger: {len(calls)} calls)")
    sp = out["split_pct"]
    print(f"  spend split: input {sp['in']}% · cache read {sp['cache']}% · output {sp['out']}%")
    if out["script_stages"]:
        print("\n  in-script calls by stage")
        for k, v in out["script_stages"].items():
            print(f"    {k:22s} {v['calls']:4d} calls  ${v['usd']:7.4f}  "
                  f"in {v['in']:>7,}  hit {v['cache_hit']:>7,}  out {v['out']:>6,}  "
                  f"reasoning {v['reasoning']:>6,}")
    if out["last_runs"]:
        print("\n  last runs")
        for r in out["last_runs"]:
            print(f"    {r['when']}  {r['calls']:3d}c  in {r['in']:>7,}  out {r['out']:>6,}  "
                  f"cache {r['cache']:>10,}  ${r['usd']:.3f}  {r['title'][:44]}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Editorial token/cost report")
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    out = report(args.days, as_json=args.json)
    if args.json:
        print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
