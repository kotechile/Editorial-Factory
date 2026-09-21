#!/usr/bin/env python3
"""Home & Lifestyle Intelligence Client (REST + MCP integration).

Connects to the Coolify-hosted home/lifestyle intelligence server at lifestyle.giniloh.com.
Exposes retrieval of real-time residential energy, smart tech & IoT, housing macro & real estate,
and architecture/DIY signals, reviews, and pipeline crawl triggers.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import requests

DEFAULT_BASE_URL = os.getenv("HOME_LIFESTYLE_INTEL_URL", "https://lifestyle.giniloh.com").rstrip("/")


class HomeLifestyleIntelClient:
    """Client for the Coolify-hosted Home & Lifestyle Intelligence service."""

    def __init__(self, base_url: str = DEFAULT_BASE_URL, timeout: int = 15):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "EditorialFactory-HomeLifestyle/1.0",
            "Accept": "application/json",
        })

    def check_health(self) -> Dict[str, Any]:
        """Check server health status."""
        resp = self.session.get(f"{self.base_url}/health", timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def get_stats(self) -> Dict[str, Any]:
        """Return total documents, breakdown by category and source, and metrics count."""
        resp = self.session.get(f"{self.base_url}/api/stats", timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def get_recent_insights(
        self,
        days_back: int = 30,
        limit: int = 20,
        category: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Retrieve recent intelligence items across categories.
        
        Strictly respects Editorial Factory Rule #1: 30-day freshness anchor.
        """
        params = {"days_back": days_back, "limit": limit}
        if category:
            params["category"] = category

        resp = self.session.get(
            f"{self.base_url}/api/insights/recent",
            params=params,
            timeout=self.timeout,
        )
        resp.raise_for_status()
        data = resp.json()
        items = data.get("items", [])
        if category:
            items = [item for item in items if item.get("category", "").lower() == category.lower()]
        return items

    def search_local(
        self,
        query: str,
        days_back: int = 30,
        limit: int = 10,
        category: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Search across recent intelligence items by keywords in title, summary, topics, takeaways, or metrics."""
        items = self.get_recent_insights(days_back=days_back, limit=100, category=category)
        terms = [t.lower().strip() for t in query.split() if t.strip()]
        if not terms:
            return items[:limit]

        scored: List[tuple[int, Dict[str, Any]]] = []
        for item in items:
            text = " ".join([
                item.get("title", ""),
                item.get("summary", ""),
                item.get("category", ""),
                " ".join(item.get("topics", [])),
                " ".join(item.get("takeaways", [])),
                " ".join(f"{km.get('metric', '')} {km.get('context', '')}" for km in item.get("key_metrics", [])),
            ]).lower()
            score = sum(text.count(t) for t in terms)
            if score > 0:
                scored.append((score, item))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [item for _, item in scored[:limit]]

    def trigger_crawl(self, category: str = "all", max_items: int = 5) -> Dict[str, Any]:
        """Trigger background ingestion webhook."""
        endpoint = f"{self.base_url}/api/crawl"
        params = {"category": category, "max": max_items}
        resp = self.session.post(endpoint, params=params, timeout=self.timeout)
        resp.raise_for_status()
        try:
            return resp.json()
        except Exception:
            return {"status": resp.status_code, "text": resp.text}

    @staticmethod
    def format_as_signals(items: List[Dict[str, Any]], vertical: str = "home_equity_tco") -> str:
        """Format intelligence items as markdown signals table per skills/radar_30day.md."""
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        lines = [
            f"# Signals: {vertical} (via Home Lifestyle Intel MCP) — {now}",
            f"**Window:** 30 calendar days",
            f"**Candidate Items:** {len(items)}",
            "",
            "| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |",
            "|---|--------|-----------|------|--------------|-------|-----------|",
        ]

        for idx, it in enumerate(items, 1):
            title = it.get("title", "").replace("|", "-")
            url = it.get("url", "")
            date_raw = it.get("published_at", "")[:16]

            # Extract highest value claim / figure
            key_metrics = it.get("key_metrics", [])
            takeaways = it.get("takeaways", [])
            if key_metrics:
                first_km = key_metrics[0]
                metric_val = first_km.get("metric", "")
                metric_ctx = first_km.get("context", "")
                claim = f"{metric_val}: {metric_ctx}"
            elif takeaways:
                claim = takeaways[0]
            else:
                summary = it.get("summary", "")
                claim = summary[:120] + "..." if len(summary) > 120 else summary
            claim = claim.replace("|", "-").replace("\n", " ")

            # Topics / Angle
            category = it.get("category", "")
            topics = it.get("topics", [])
            angle = topics[0] if topics else (category or "Home & Lifestyle")
            angle = angle.replace("|", "-")

            # Default intensity: 80+ if key_metrics present, else 72
            intensity = 84 if key_metrics else 72

            lines.append(f"| {idx} | {title} | {url} | {date_raw} | {claim} | {angle} | {intensity} |")

        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Home & Lifestyle Intelligence Client")
    parser.add_argument("--url", default=DEFAULT_BASE_URL, help="Base URL for intelligence server")
    parser.add_argument("--stats", action="store_true", help="Print pipeline stats")
    parser.add_argument("--health", action="store_true", help="Check server health")
    parser.add_argument("--recent", type=int, nargs="?", const=30, help="Retrieve recent insights (default: 30 days)")
    parser.add_argument("--search", type=str, help="Search query across recent insights")
    parser.add_argument("--category", type=str, help="Filter by category")
    parser.add_argument("--limit", type=int, default=10, help="Max results to return (default: 10)")
    parser.add_argument("--crawl", type=str, nargs="?", const="all", help="Trigger crawler webhook (category, default all)")
    parser.add_argument("--crawl-max", type=int, default=5, help="Max items for crawler")
    parser.add_argument("--format", choices=["json", "signals", "pretty"], default="pretty", help="Output format")
    parser.add_argument("--vertical", default="home_equity_tco", help="Vertical name for signals format")
    parser.add_argument("--out", type=str, help="Save output to file path")

    args = parser.parse_args()
    client = HomeLifestyleIntelClient(base_url=args.url)

    try:
        output = ""
        if args.health:
            res = client.check_health()
            output = json.dumps(res, indent=2)

        elif args.stats:
            res = client.get_stats()
            output = json.dumps(res, indent=2)

        elif args.crawl is not None:
            res = client.trigger_crawl(category=args.crawl, max_items=args.crawl_max)
            output = json.dumps(res, indent=2)

        elif args.search:
            items = client.search_local(
                query=args.search,
                days_back=args.recent or 30,
                limit=args.limit,
                category=args.category,
            )
            if args.format == "json":
                output = json.dumps(items, indent=2)
            elif args.format == "signals":
                output = client.format_as_signals(items, vertical=args.vertical)
            else:
                lines = [f"Found {len(items)} matching items for query '{args.search}':\n"]
                for it in items:
                    lines.append(f"[{it.get('category')}] {it.get('title')}")
                    lines.append(f"  Source: {it.get('source_name')} | URL: {it.get('url')}")
                    lines.append(f"  Date: {it.get('published_at')}")
                    for km in it.get("key_metrics", []):
                        lines.append(f"  * {km.get('metric')}: {km.get('context')}")
                    lines.append("")
                output = "\n".join(lines)

        elif args.recent is not None or len(sys.argv) == 1:
            days = args.recent if args.recent is not None else 30
            items = client.get_recent_insights(days_back=days, limit=args.limit, category=args.category)
            if args.format == "json":
                output = json.dumps(items, indent=2)
            elif args.format == "signals":
                output = client.format_as_signals(items, vertical=args.vertical)
            else:
                lines = [f"Recent {len(items)} insights (last {days} days):\n"]
                for it in items:
                    lines.append(f"[{it.get('category')}] {it.get('title')}")
                    lines.append(f"  Source: {it.get('source_name')} | URL: {it.get('url')}")
                    lines.append(f"  Date: {it.get('published_at')}")
                    for km in it.get("key_metrics", []):
                        lines.append(f"  * {km.get('metric')}: {km.get('context')}")
                    lines.append("")
                output = "\n".join(lines)

        if args.out:
            Path(args.out).parent.mkdir(parents=True, exist_ok=True)
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"Wrote output to {args.out}")
        else:
            print(output)

    except Exception as e:
        print(f"Error executing request: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
