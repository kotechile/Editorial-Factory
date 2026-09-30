#!/usr/bin/env python3
"""Tests for the Pre-Flight Data Gate — run: python3 scripts/test_citation_hub_gate.py

Hermetic: a stub HTTP server supplies the sources, so the assertions do not depend on the live
web. The final section audits the module's own claimed dossiers against the real sources and
asserts the gate rejects them, which is the whole point of the change.

  python3 scripts/test_citation_hub_gate.py --no-network   # skip the live audit
"""

from __future__ import annotations

import json
import pathlib
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import citation_hub_dossier as chd  # noqa: E402

PASS, FAIL = [], []


def check(name: str, condition: bool, detail: str = ""):
    (PASS if condition else FAIL).append(name)
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}{'' if condition else f'  <- {detail}'}")


class Source(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        if self.path == "/verified":
            body = (b"<html><head><title>SWE-bench</title><style>x{}</style></head><body>"
                    b"<script>var x=99;</script>"
                    b"<p>Our agent resolves 41.6% of the sampled GitHub issues, a new state of the art.</p>"
                    b"<p>Elsewhere 1620 tasks were reviewed.</p></body></html>")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/absent":
            body = b"<html><body><p>A page that never states the number at all.</p></body></html>"
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/pdf":
            body = b"%PDF-1.7 not really a pdf"
            self.send_response(200)
            self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.send_header("Content-Length", "0")
            self.end_headers()


server = ThreadingHTTPServer(("127.0.0.1", 0), Source)
threading.Thread(target=server.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{server.server_address[1]}"


def point(**over):
    base = {
        "metric_name": "Autonomous Task Completion",
        "headline_figure": "41.6%",
        "vendor_claim": "state of the art",
        "field_reality": "production telemetry is lower",
        "primary_source_name": "SWE-bench Verified",
        "primary_source_url": f"{BASE}/verified",
        "publication_date": "2026-03",
        "sample_size": "500 verified issues",
    }
    base.update(over)
    return base


print("\nfigure matching")
check("finds the figure in fetched text",
      chd.figure_evidence("41.6%", "resolves 41.6% of sampled issues") is not None)
check("returns the surrounding evidence, not just a boolean",
      "resolves 41.6%" in (chd.figure_evidence("41.6%", "x " * 200 + "resolves 41.6% of issues") or ""))
check("does not match a number inside a longer one ('62' vs '1620')",
      chd.figure_evidence("62%", "1620 tasks were reviewed") is None)
check("does not match a longer number for a short figure ('7.4x' vs '17.4x')",
      chd.figure_evidence("7.4x", "17.4x uplift") is None)
check("matches a decimal figure with its unit", chd.figure_evidence("42.8s", "p95 latency 42.8s") is not None)
check("empty figure never matches", chd.figure_evidence("", "anything") is None)

print("\nper-point verification")
r = chd.verify_point(point())
check("a figure present in the source verifies", r["status"] == "verified", r)
check("...and carries HTTP + body hash + evidence",
      r.get("http") == "200" and len(r.get("sha256", "")) == 64 and r.get("evidence"))
r = chd.verify_point(point(headline_figure="1,234%"))
check("a figure absent from the source fails", r["status"] == "figure_absent", r)
r = chd.verify_point(point(primary_source_url=f"{BASE}/2024/09/multi-agent-survey"))
check("a source that 404s fails closed", r["status"] == "unreachable" and r["http"] == "404", r)
r = chd.verify_point(point(primary_source_url="https://127.0.0.1:1/nothing-listens-here"))
check("a source that cannot be reached fails closed", r["status"] == "unreachable", r)
r = chd.verify_point(point(primary_source_url=f"{BASE}/pdf"))
check("a PDF source fails closed rather than passing unverified", r["status"] == "unsupported", r)
r = chd.verify_point(point(publication_date=""))
check("a blank publication date fails (the skill claims the gate checks it)",
      r["status"] == "incomplete" and "publication_date" in r["reason"], r)
r = chd.verify_point(point(sample_size=""))
check("a blank sample size fails", r["status"] == "incomplete" and "sample_size" in r["reason"], r)
r = chd.verify_point(point(primary_source_url="https://"))
check("a malformed URL fails", r["status"] == "incomplete", r)
r = chd.verify_point(point(field_reality=""))
check("a point with no field-reality audit fails", r["status"] == "incomplete", r)

print("\ndossier verdict")
good = [point() for _ in range(6)]
ok, errors, report = chd.verify_dossier(good, min_points=6)
check("six verified points pass the gate", ok and not errors, errors)
ok, errors, report = chd.verify_dossier(good[:5], min_points=6)
check("too few points fails the gate", not ok and any("insufficient" in e for e in errors), errors)
mixed = [point()] * 5 + [point(headline_figure="1,234%")]
ok, errors, report = chd.verify_dossier(mixed, min_points=6)
check("one bad point fails the whole dossier", not ok, errors)
check("...and the report names it", any("figure_absent" in e for e in errors), errors)
check("the report is auditable (per-point status, counts, timestamp)",
      report["counts"].get("verified") == 5 and report["points"][-1]["checked_at"] and report["ok"] is False)

print("\nno silent fallback")
try:
    chd.get_claimed_dossier("warehouse_automation_robotics_capex", "warehouse automation statistics")
    check("a vertical with no sourced data raises instead of substituting", False, "returned a dossier")
except chd.UnverifiedDossierError as exc:
    check("a vertical with no sourced data raises instead of substituting",
          "no data points sourced" in str(exc), exc)
except Exception as exc:                                   # noqa: BLE001
    check("a vertical with no sourced data raises instead of substituting", False, repr(exc))

print("\nthe hub builder refuses to draft on unverified data")
try:
    import seo_machine
    kw = {"keyword": "agentic ai enterprise benchmarks", "search_volume": 4800,
          "search_intent": "commercial", "keyword_clusters": [], "paa_questions": []}
    try:
        seo_machine.build_citation_hub_draft(kw, {}, [], {"founder_stances": [], "founder_quotes": [],
                                                          "customer_anecdotes": []},
                                             "agentic_ai", "ai_architect")
        check("build_citation_hub_draft refuses an unverified dossier", False, "it drafted a hub")
    except chd.UnverifiedDossierError as exc:
        check("build_citation_hub_draft refuses an unverified dossier", "Pre-flight data verification failed" in str(exc))
except ImportError as exc:
    check("build_citation_hub_draft refuses an unverified dossier", False, f"could not import seo_machine: {exc}")

if "--no-network" not in sys.argv:
    print("\nlive audit — the module's own claimed dossiers, against their real sources")
    try:
        claimed = chd.get_claimed_dossier("agentic_ai", "agentic ai enterprise benchmarks")
        report = chd.audit_dossier(claimed, min_points=6)
        print(f"  {len(claimed)} claimed point(s) — statuses: {report['counts']}")
        for p in report["points"]:
            print(f"      [{p['status']:13s}] {p['metric_name'][:46]:46s} {p.get('http', ''):>5}  {p['url'][:52]}")
            if p.get("reason"):
                print(f"                      {p['reason'][:104]}")
        check("the shipped claimed dossiers do NOT pass the gate (that is the point of the change)",
              not report["ok"], "they passed — the gate is still a rubber stamp")
        check("...every failing point names a concrete reason",
              all(p.get("reason") for p in report["points"] if p["status"] != "verified"))
    except chd.UnverifiedDossierError as exc:
        check("the shipped claimed dossiers do NOT pass the gate", False, f"unexpected: {exc}")

server.shutdown()
print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
for name in FAIL:
    print(f"  FAILED: {name}")
sys.exit(1 if FAIL else 0)
