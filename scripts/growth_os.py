#!/usr/bin/env python3
"""Growth OS Knowledge, Cannibalization Prevention & Internal Linking Engine.

Functions:
1. Cannibalization Checker: Prevents competing against our own published URLs.
2. Internal Link Map Generator: Identifies high-relevance internal links and anchor texts.
3. Growth OS POV & Anecdote Extractor: Pulls founder opinions and customer truth from knowledge base.
"""

import argparse
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTEXT_DIR = ROOT / "context"
GROWTH_OS_DIR = CONTEXT_DIR / "growth_os"
FOUNDER_VOICE_FILE = GROWTH_OS_DIR / "founder-voice.md"
CUSTOMER_TRUTH_FILE = GROWTH_OS_DIR / "customer-truth.md"
SITEMAP_FILE = CONTEXT_DIR / "sitemap.json"
PUBLISHED_DIR = ROOT / "published"
DRAFTS_DIR = CONTEXT_DIR / "drafts"


def load_sitemap():
    """Load sitemap from JSON or rebuild dynamically from published/ directory."""
    if SITEMAP_FILE.exists():
        try:
            with open(SITEMAP_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[Growth OS] Warning reading sitemap.json: {e}", file=sys.stderr)

    # Rebuild basic sitemap from published directory
    articles = []
    if PUBLISHED_DIR.exists():
        for md_path in sorted(PUBLISHED_DIR.glob("*.md")):
            text = md_path.read_text(encoding="utf-8")
            title_m = re.search(r"^#\s+(.+)$", text, re.M) or re.search(r"title:\s*[\"']?([^\"\n\r]+)[\"']?", text)
            title = title_m.group(1).strip() if title_m else md_path.stem
            vert_m = re.search(r"vertical:\s*([a-z0-9_]+)", text)
            vert = vert_m.group(1).strip() if vert_m else "general"

            articles.append({
                "slug": md_path.stem,
                "title": title,
                "url": f"/published/{md_path.name}",
                "vertical": vert,
                "primary_keyword": md_path.stem.replace("_", " ").replace("-", " ").lower(),
                "secondary_keywords": [],
                "date": md_path.stem[:10] if re.match(r"^\d{4}-\d{2}-\d{2}", md_path.stem) else ""
            })
    return {"articles": articles, "base_url": "https://editorialfactory.io"}


def check_cannibalization(target_keyword, vertical=None, threshold=0.65):
    """Check if the keyword conflicts with an existing published piece."""
    sitemap = load_sitemap()
    articles = sitemap.get("articles", [])
    cleaned_target = target_keyword.strip().lower()
    target_words = set(re.findall(r"\w+", cleaned_target))

    conflicts = []

    for art in articles:
        p_kw = art.get("primary_keyword", "").lower()
        title = art.get("title", "").lower()
        sec_kws = [k.lower() for k in art.get("secondary_keywords", [])]

        # 1. Exact match check
        if cleaned_target == p_kw or cleaned_target in sec_kws:
            conflicts.append({
                "article": art,
                "similarity": 1.0,
                "reason": "Exact primary/secondary keyword match"
            })
            continue

        # 2. Token overlap similarity (Jaccard)
        all_art_words = set(re.findall(r"\w+", f"{p_kw} {title} {' '.join(sec_kws)}"))
        if not all_art_words or not target_words:
            continue

        intersection = target_words.intersection(all_art_words)
        jaccard = len(intersection) / len(target_words.union(all_art_words))

        # Check if target phrase is substantial subset
        overlap_ratio = len(intersection) / max(1, len(target_words))

        if jaccard >= threshold or overlap_ratio >= 0.8:
            conflicts.append({
                "article": art,
                "similarity": round(max(jaccard, overlap_ratio), 2),
                "reason": f"High semantic token overlap ({round(overlap_ratio*100)}% keyword tokens match)"
            })

    conflicts.sort(key=lambda x: x["similarity"], reverse=True)

    if conflicts:
        top = conflicts[0]
        verdict = "CANNOT_PUBLISH_DUPLICATE" if top["similarity"] >= 0.95 else "UPDATE_EXISTING_OR_SUBCLUSTER"
        return {
            "is_cannibalized": True,
            "verdict": verdict,
            "top_conflict": top["article"],
            "similarity": top["similarity"],
            "reason": top["reason"],
            "all_conflicts": conflicts,
            "recommendation": (
                f"Topic heavily cannibalizes '{top['article']['title']}'. "
                f"Either update '{top['article']['slug']}' with a fresh section or narrow target keyword to a distinct long-tail sub-topic."
            )
        }

    return {
        "is_cannibalized": False,
        "verdict": "CLEAR_TO_PUBLISH",
        "top_conflict": None,
        "similarity": 0.0,
        "recommendation": "No cannibalization detected. Clear to draft new pillar/cluster article."
    }


def generate_internal_link_map(target_keyword, vertical=None, max_links=3):
    """Scan published sitemap and propose internal links with context and anchor texts."""
    sitemap = load_sitemap()
    articles = sitemap.get("articles", [])
    target_words = set(re.findall(r"\w+", target_keyword.lower()))

    scored_candidates = []

    for art in articles:
        vert = art.get("vertical", "")
        title = art.get("title", "")
        p_kw = art.get("primary_keyword", "")
        sec_kws = art.get("secondary_keywords", [])
        h2s = art.get("h2_topics", [])

        score = 0
        if vertical and vert == vertical:
            score += 3  # same vertical bonus

        combined_text = f"{title} {p_kw} {' '.join(sec_kws)} {' '.join(h2s)}".lower()
        art_words = set(re.findall(r"\w+", combined_text))

        overlap = len(target_words.intersection(art_words))
        score += overlap * 2

        if score > 0:
            # Generate contextual anchor text
            anchor = p_kw if p_kw else title
            # Clean anchor
            anchor = re.sub(r"^(the|our|why|how to)\s+", "", anchor, flags=re.I).strip()

            scored_candidates.append({
                "title": title,
                "slug": art.get("slug"),
                "url": art.get("url"),
                "vertical": vert,
                "anchor_text": anchor,
                "relevance_score": score,
                "suggested_placement": f"Link in the background/tension section when referencing {anchor}."
            })

    scored_candidates.sort(key=lambda x: x["relevance_score"], reverse=True)
    return scored_candidates[:max_links]


def extract_growth_os_knowledge(vertical, keyword=""):
    """Extract matching founder voice stances, quotes, and customer truth anecdotes."""
    founder_voice_text = FOUNDER_VOICE_FILE.read_text(encoding="utf-8") if FOUNDER_VOICE_FILE.exists() else ""
    customer_truth_text = CUSTOMER_TRUTH_FILE.read_text(encoding="utf-8") if CUSTOMER_TRUTH_FILE.exists() else ""

    # 1. Parse Founder Voice section for vertical
    founder_stances = []
    founder_quotes = []

    v_pattern = re.compile(rf"### Vertical:\s*`?{vertical}`?([\s\S]*?)(?=### Vertical:|\Z)", re.I)
    v_match = v_pattern.search(founder_voice_text)
    if v_match:
        section = v_match.group(1)
        for bullet in re.findall(r"^-\s+\*\*([^*]+)\*\*:\s*(.+)$", section, re.M):
            founder_stances.append({"topic": bullet[0].strip(), "stance": bullet[1].strip()})
        for quote in re.findall(r"^>\s*\"([^\"]+)\"\s*—\s*(.+)$", section, re.M):
            founder_quotes.append({"quote": quote[0].strip(), "author": quote[1].strip()})

    # If no vertical section match, grab universal rules
    if not founder_stances:
        founder_stances.append({
            "topic": "Pragmatic Realism",
            "stance": "Ground every claim in an architectural or economic reality rather than theoretical hype."
        })

    # 2. Parse Customer Truth anecdotes
    customer_anecdotes = []
    ct_pattern = re.compile(rf"### Vertical:\s*`?{vertical}`?([\s\S]*?)(?=### Vertical:|\Z)", re.I)
    ct_match = ct_pattern.search(customer_truth_text)
    if ct_match:
        ct_section = ct_match.group(1)
        for anec in re.findall(r"^-\s+\*\*([^*]+)\*\*:\s*([\s\S]*?)(?=(?:^-\s+\*\*|\Z))", ct_section, re.M):
            customer_anecdotes.append({
                "title": anec[0].strip(),
                "details": anec[1].strip().replace("\n", " ")
            })

    return {
        "vertical": vertical,
        "keyword": keyword,
        "founder_stances": founder_stances,
        "founder_quotes": founder_quotes,
        "customer_anecdotes": customer_anecdotes
    }


def main():
    parser = argparse.ArgumentParser(description="Growth OS Knowledge, Cannibalization & Internal Linking Engine")
    parser.add_argument("--check-cannibalization", action="store_true", help="Check keyword for cannibalization")
    parser.add_argument("--internal-links", action="store_true", help="Generate internal link map for keyword")
    parser.add_argument("--extract-pov", action="store_true", help="Extract founder voice and customer truth")
    parser.add_argument("--keyword", default="agent evaluation bottlenecks", help="Target keyword")
    parser.add_argument("--vertical", default="agentic_ai", help="Vertical ID")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    if args.check_cannibalization:
        res = check_cannibalization(args.keyword, args.vertical)
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"\n[Cannibalization Check] Target: '{args.keyword}'")
            print(f"Verdict: {res['verdict']}")
            print(f"Recommendation: {res['recommendation']}")
            if res["top_conflict"]:
                print(f"Top Conflict: '{res['top_conflict']['title']}' (Similarity: {res['similarity']})")
            print("")

    elif args.internal_links:
        res = generate_internal_link_map(args.keyword, args.vertical)
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"\n[Internal Link Map] For '{args.keyword}' ({args.vertical}):")
            for idx, link in enumerate(res, 1):
                print(f"{idx}. [{link['anchor_text']}] -> {link['url']} ('{link['title']}')")
                print(f"   Placement: {link['suggested_placement']}")
            print("")

    elif args.extract_pov:
        res = extract_growth_os_knowledge(args.vertical, args.keyword)
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"\n[Growth OS Knowledge] Vertical: '{args.vertical}'")
            print(f"\n--- Founder Stances & Opinions ---")
            for st in res["founder_stances"]:
                print(f"• {st['topic']}: {st['stance']}")
            if res["founder_quotes"]:
                print(f"\n--- Founder Quotes ---")
                for q in res["founder_quotes"]:
                    print(f'> "{q["quote"]}" — {q["author"]}')
            if res["customer_anecdotes"]:
                print(f"\n--- Customer Truth / Field Anecdotes ---")
                for an in res["customer_anecdotes"]:
                    print(f"• {an['title']}: {an['details']}")
            print("")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
