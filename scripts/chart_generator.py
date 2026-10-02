#!/usr/bin/env python3
"""Visual Chart Generator for Citation Hubs & Audited Benchmarks.

Generates clean, embeddable Mermaid data charts and modern SVG bar charts
to drive passive link acquisition and visual engagement.
"""

from typing import List, Dict, Tuple
import html
import sys


def _shorten(text: str, limit: int = 30) -> str:
    """Trim a label to fit without cutting a word in half.

    The renderer used `label[:28]`, which put "Autonomous & Agentic Workf" into a figure that is
    meant to be quoted verbatim. Cut at the last whole word that fits and mark the elision.
    """
    text = " ".join(str(text).split())
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:-")
    return (cut or text[:limit].rstrip()) + "…"


def generate_mermaid_bar_chart(title: str, items: List[Tuple[str, float]], x_label: str = "Metric", y_label: str = "%") -> str:
    """Generate a Mermaid xychart-beta block for native markdown rendering."""
    # Truncate labels so they fit on mobile / small screens
    cats = [f'"{_shorten(cat, 16)}"' for cat, _ in items]
    vals = [str(round(val, 1)) for _, val in items]
    
    lines = [
        "```mermaid",
        "xychart-beta",
        f'    title "{title}"',
        f'    x-axis [{", ".join(cats)}]',
        f'    y-axis "{y_label}" 0 --> 100',
        f'    bar [{", ".join(vals)}]',
        "```"
    ]
    return "\n".join(lines)


def generate_svg_bar_chart(title: str, items: List[Tuple[str, float, str]], max_val: float = 100.0,
                           subtitle: str = "Audited Field Telemetry vs Industry Claims (2026)") -> str:
    """Generate a sleek, responsive SVG bar chart with dark-mode aesthetic.
    
    items: List of (label, percentage_value, subtext/annotation)

    `subtitle` is caller-supplied because it states what the bars are: the citation hub's default
    ("audited field telemetry vs industry claims") is a claim about the data, and an article that
    charts its own reported figures must not borrow it.
    """
    row_height = 48
    header_height = 56
    padding = 20
    height = header_height + (len(items) * row_height) + padding
    width = 680

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="background:#0f172a; border-radius:8px; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; margin:16px 0; max-width:100%; height:auto;">',
        f'  <text x="{padding}" y="36" fill="#f8fafc" font-size="16" font-weight="600">{html.escape(title)}</text>',
        f'  <text x="{padding}" y="52" fill="#94a3b8" font-size="12">{html.escape(subtitle)}</text>'
    ]

    bar_max_width = 300
    bar_start_x = 240

    for idx, (label, val, note) in enumerate(items):
        y = header_height + (idx * row_height) + 12
        pct = min(100.0, max(0.0, float(val)))
        bar_w = max(4, int((pct / max_val) * bar_max_width))
        
        # Color coding: higher failure / lower accuracy gets accent warning
        bar_color = "#38bdf8" if "success" in label.lower() or "retention" in label.lower() else "#f43f5e" if "fail" in label.lower() or "drift" in label.lower() else "#818cf8"
        
        svg_lines.append(f'  <!-- Row {idx+1} -->')
        svg_lines.append(f'  <text x="{padding}" y="{y+16}" fill="#e2e8f0" font-size="13" font-weight="500">{html.escape(_shorten(label, 32))}</text>')
        svg_lines.append(f'  <rect x="{bar_start_x}" y="{y+2}" width="{bar_max_width}" height="18" rx="4" fill="#1e293b"/>')
        svg_lines.append(f'  <rect x="{bar_start_x}" y="{y+2}" width="{bar_w}" height="18" rx="4" fill="{bar_color}"/>')
        # Label the bar with the figure it was given, never with the axis-clamped width: printing the
        # clamp turned a 116% growth rate into a quoted "100.0%" — a number the source never said.
        svg_lines.append(f'  <text x="{bar_start_x + bar_w + 10}" y="{y+16}" fill="#f1f5f9" font-size="13" font-weight="600">{round(float(val), 1):g}%</text>')
        if note:
            svg_lines.append(f'  <text x="{bar_start_x + bar_w + 64}" y="{y+16}" fill="#64748b" font-size="11">({html.escape(_shorten(note, 22))})</text>')

    svg_lines.append('</svg>')
    return "\n".join(svg_lines)


def generate_benchmark_visual(dossier: List[Dict[str, str]], title: str) -> str:
    """Chart the dossier's verified percentages — or emit no chart at all.

    Returns "" when fewer than two points carry a parseable percentage, and the caller embeds
    whatever it gets. There is deliberately no fallback: this used to emit a Mermaid chart with a
    hard-coded 50.0 for every bar, a figure invented purely so that a visual existed. A citation hub
    is only worth the links it earns if every number on the page traces to its source, and the chart
    is the most quotable part of it. Mixed units are excluded for the same reason — plotting
    "50 min" on a 0-100 percent axis is a wrong comparison dressed as a chart.
    """
    chart_items = []
    for dp in dossier:
        fig_str = str(dp.get("headline_figure", ""))
        if "%" not in fig_str:
            continue
        try:
            num = float(fig_str.replace("%", "").replace(",", "").strip())
        except ValueError:
            continue
        chart_items.append((str(dp.get("metric_name", "Metric")), num,
                            str(dp.get("primary_source_name", ""))))

    if len(chart_items) < 2:
        print(f"[chart] no chart for '{title}': {len(chart_items)} of {len(dossier)} dossier point(s) "
              f"carry a percentage. Emitting none rather than inventing the missing values.",
              file=sys.stderr)
        return ""

    return generate_svg_bar_chart(title, chart_items[:5])
