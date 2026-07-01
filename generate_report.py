#!/usr/bin/env python3
"""
CopperBuilds SERP Visibility Report Generator
Usage: python generate_report.py --trade hvac --city phoenix --state az [--domain example.com]
Outputs: copperbuilds/reports/[trade]-seo-report-[city]-[state]-[year]/index.html
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / "copperbuilds.env")

DFS_USER = os.getenv("DATAFORSEO_USERNAME")
DFS_PASS = os.getenv("DATAFORSEO_PASSWORD")

# ── Cache Config ──────────────────────────────────────────────────────────────

CACHE_DIR = Path(__file__).parent / "reports" / "_cache"
CACHE_TTL_DAYS = 30


def _cache_key(keyword: str, location: str) -> str:
    slug = f"{keyword}--{location}".lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return slug[:120]


def _load_cache(keyword: str, location: str) -> dict | None:
    path = CACHE_DIR / f"{_cache_key(keyword, location)}.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        saved_at = datetime.fromisoformat(data["_cached_at"])
        if datetime.now() - saved_at > timedelta(days=CACHE_TTL_DAYS):
            return None  # stale — will refetch
        return data["result"]
    except Exception:
        return None


def _save_cache(keyword: str, location: str, result: dict) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = CACHE_DIR / f"{_cache_key(keyword, location)}.json"
    payload = {"_cached_at": datetime.now().isoformat(), "result": result}
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

# ── Trade Keyword Templates ───────────────────────────────────────────────────

TRADE_KEYWORDS = {
    "hvac": [
        "AC repair", "HVAC company", "air conditioning repair", "furnace repair",
        "HVAC contractor", "emergency HVAC", "air conditioning installation",
        "heating and cooling", "HVAC service", "central air repair",
        "AC installation", "heat pump repair", "HVAC maintenance",
        "air conditioner service", "heating repair",
    ],
    "plumbing": [
        "plumber", "emergency plumber", "plumbing company", "drain cleaning",
        "water heater repair", "pipe repair", "leak repair", "plumbing service",
        "water heater installation", "sewer line repair", "toilet repair",
        "faucet repair", "plumbing contractor", "clogged drain", "water heater replacement",
    ],
    "roofing": [
        "roofing company", "roof repair", "roof replacement", "roofer",
        "storm damage roof repair", "roofing contractor", "roof inspection",
        "shingle replacement", "flat roof repair", "roofing service",
        "emergency roof repair", "gutter installation", "roof leak repair",
        "new roof installation", "roofing estimate",
    ],
    "electrical": [
        "electrician", "electrical contractor", "electrical repair", "panel upgrade",
        "electrical service", "emergency electrician", "electrical installation",
        "outlet repair", "circuit breaker repair", "generator installation",
        "EV charger installation", "electrical inspection", "wiring repair",
        "lighting installation", "electrical company",
    ],
    "landscaping": [
        "landscaping company", "lawn care service", "lawn mowing service",
        "landscape design", "tree trimming", "lawn maintenance",
        "irrigation installation", "sod installation", "landscaper",
        "yard cleanup", "mulching service", "weed control service",
        "sprinkler repair", "landscape contractor", "lawn treatment",
    ],
    "painting": [
        "painting contractor", "house painter", "interior painting",
        "exterior painting", "painting company", "commercial painting",
        "residential painting", "cabinet painting", "painting service",
        "deck staining", "fence painting", "drywall repair and painting",
        "painting estimate", "painting crew", "painting professionals",
    ],
    "cleaning": [
        "house cleaning service", "maid service", "cleaning company",
        "deep cleaning service", "move out cleaning", "commercial cleaning",
        "office cleaning", "janitorial service", "residential cleaning",
        "cleaning professionals", "cleaning crew", "weekly cleaning service",
        "post construction cleaning", "carpet cleaning", "window cleaning",
    ],
    "concrete": [
        "concrete contractor", "concrete company", "driveway replacement",
        "concrete repair", "concrete driveway", "patio installation",
        "concrete patio", "sidewalk repair", "concrete resurfacing",
        "stamped concrete", "foundation repair", "concrete leveling",
        "garage floor coating", "concrete work", "decorative concrete",
    ],
    "pool": [
        "pool service", "pool cleaning service", "pool repair", "pool company",
        "pool installation", "pool maintenance", "swimming pool repair",
        "pool contractor", "pool resurfacing", "pool equipment repair",
        "pool opening service", "pool closing service", "pool inspection",
        "above ground pool installation", "inground pool builder",
    ],
    "general_contractor": [
        "general contractor", "home remodeling", "kitchen remodel",
        "bathroom remodel", "home renovation", "contractor",
        "remodeling company", "home improvement contractor", "room addition",
        "basement finishing", "deck building contractor", "home repair",
        "renovation contractor", "construction company", "remodeling contractor",
    ],
}

TRADE_LABELS = {
    "hvac": "HVAC", "plumbing": "Plumbing", "roofing": "Roofing",
    "electrical": "Electrical", "landscaping": "Landscaping", "painting": "Painting",
    "cleaning": "Cleaning", "concrete": "Concrete", "pool": "Pool",
    "general_contractor": "General Contractor",
}

FEATURE_WEIGHTS = {
    "local_pack": 0.40, "local_services": 0.20, "organic": 0.30,
    "featured_snippet": 0.05, "ai_overview": 0.03, "people_also_ask": 0.02,
}

FEATURE_LABELS = {
    "local_pack": "Local Pack (3-Map)", "local_services": "Local Services Ads",
    "organic": "Organic Results", "featured_snippet": "Featured Snippet",
    "ai_overview": "AI Overview", "people_also_ask": "People Also Ask", "images": "Image Pack",
}

# ── DataForSEO Client ─────────────────────────────────────────────────────────

def dfs_serp(keyword: str, location: str) -> dict:
    url = "https://api.dataforseo.com/v3/serp/google/organic/live/advanced"
    payload = [{"keyword": keyword, "location_name": location,
                "language_name": "English", "device": "mobile", "depth": 20}]
    resp = requests.post(url, json=payload, auth=(DFS_USER, DFS_PASS), timeout=30)
    resp.raise_for_status()
    data = resp.json()
    if data.get("status_code") != 20000:
        raise ValueError(f"DFS error: {data.get('status_message')}")
    tasks = data.get("tasks", [])
    if not tasks or tasks[0].get("status_code") != 20000:
        return {}
    results = tasks[0].get("result", [])
    return results[0] if results else {}


def dfs_serp_cached(keyword: str, location: str) -> tuple[dict, bool]:
    """Returns (result, from_cache). Checks cache first; fetches and saves if missing or stale."""
    cached = _load_cache(keyword, location)
    if cached is not None:
        return cached, True
    result = dfs_serp(keyword, location)
    _save_cache(keyword, location, result)
    return result, False

# ── Feature Parser ────────────────────────────────────────────────────────────

def parse_features(serp_result: dict, domain: str | None) -> dict:
    items = serp_result.get("items", []) or []
    f = {k: {"fired": False, "businesses": [], "client_present": False}
         for k in ["local_pack", "local_services", "featured_snippet", "ai_overview"]}
    f["organic"] = {"fired": False, "positions": [], "client_present": False, "client_rank": None}
    f["people_also_ask"] = {"fired": False, "questions": []}
    f["images"] = {"fired": False}

    for item in items:
        t = item.get("type", "")
        if t == "local_pack":
            f["local_pack"]["fired"] = True
            for biz in (item.get("items") or []):
                name = biz.get("title", "")
                url = biz.get("url", "") or ""
                f["local_pack"]["businesses"].append({"name": name, "url": url})
                if domain and domain.lower() in url.lower():
                    f["local_pack"]["client_present"] = True
        elif t == "local_services":
            f["local_services"]["fired"] = True
            for svc in (item.get("items") or []):
                name = svc.get("title", "") or svc.get("domain", "")
                f["local_services"]["businesses"].append({"name": name})
                if domain and domain.lower() in (svc.get("url", "") or "").lower():
                    f["local_services"]["client_present"] = True
        elif t == "organic":
            f["organic"]["fired"] = True
            rank = item.get("rank_absolute", 0)
            url = item.get("url", "") or ""
            d = item.get("domain", "") or ""
            f["organic"]["positions"].append({"rank": rank, "domain": d})
            if domain and (domain.lower() in url.lower() or domain.lower() in d.lower()):
                f["organic"]["client_present"] = True
                if f["organic"]["client_rank"] is None:
                    f["organic"]["client_rank"] = rank
        elif t == "featured_snippet":
            f["featured_snippet"]["fired"] = True
            url = item.get("url", "") or ""
            if domain and domain.lower() in url.lower():
                f["featured_snippet"]["client_present"] = True
        elif t == "ai_overview":
            f["ai_overview"]["fired"] = True
            for src in (item.get("sources") or item.get("items") or []):
                if domain and domain.lower() in (src.get("url", "") or "").lower():
                    f["ai_overview"]["client_present"] = True
        elif t == "people_also_ask":
            f["people_also_ask"]["fired"] = True
            for q in (item.get("items") or []):
                f["people_also_ask"]["questions"].append(q.get("title", ""))
        elif t == "images":
            f["images"]["fired"] = True
    return f

# ── Aggregators ───────────────────────────────────────────────────────────────

def aggregate_competitors(all_features: list) -> list:
    counts: dict[str, int] = {}
    for kw_f in all_features:
        for biz in kw_f.get("local_pack", {}).get("businesses", []):
            name = biz.get("name", "").strip()
            if name:
                counts[name] = counts.get(name, 0) + 1
    total = len(all_features)
    ranked = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return [{"name": n, "appearances": c,
             "prevalence_pct": round(c / total * 100) if total else 0}
            for n, c in ranked[:5]]

def aggregate_stats(all_features: list) -> dict:
    total = len(all_features)
    stats = {}
    for feat in ["local_pack", "local_services", "organic", "featured_snippet",
                 "ai_overview", "people_also_ask", "images"]:
        fired = sum(1 for f in all_features if f.get(feat, {}).get("fired"))
        stats[feat] = {"fired_count": fired,
                       "prevalence_pct": round(fired / total * 100) if total else 0}
    questions = []
    for f in all_features:
        questions.extend(f.get("people_also_ask", {}).get("questions", []))
    stats["paa_questions"] = list(dict.fromkeys(questions))[:8]
    return stats

def calc_ownership_score(all_features: list, domain: str | None) -> dict:
    total = len(all_features)
    if not total:
        return {"client": 0.0, "competitors": {}}
    client_pts = 0.0
    comp_pts: dict[str, float] = {}
    for kw_f in all_features:
        lp = kw_f.get("local_pack", {})
        if domain:
            if lp.get("client_present"):
                client_pts += FEATURE_WEIGHTS["local_pack"]
            if kw_f.get("local_services", {}).get("client_present"):
                client_pts += FEATURE_WEIGHTS["local_services"]
            if kw_f.get("organic", {}).get("client_present"):
                client_pts += FEATURE_WEIGHTS["organic"]
            if kw_f.get("featured_snippet", {}).get("client_present"):
                client_pts += FEATURE_WEIGHTS["featured_snippet"]
            if kw_f.get("ai_overview", {}).get("client_present"):
                client_pts += FEATURE_WEIGHTS["ai_overview"]
        for biz in lp.get("businesses", []):
            name = biz.get("name", "").strip()
            if name:
                comp_pts[name] = comp_pts.get(name, 0.0) + FEATURE_WEIGHTS["local_pack"]
    max_pts = sum(FEATURE_WEIGHTS.values()) * total
    client_score = round(client_pts / max_pts * 100, 1) if max_pts else 0.0
    comp_scores = {n: round(p / max_pts * 100, 1) for n, p in comp_pts.items()}
    top5 = dict(sorted(comp_scores.items(), key=lambda x: x[1], reverse=True)[:5])
    return {"client": client_score, "competitors": top5}

# ── HTML Generator ────────────────────────────────────────────────────────────

def build_feature_rows(stats: dict, domain: str | None) -> str:
    rows = ""
    features = [
        ("local_pack", "🗺️"), ("local_services", "📋"), ("organic", "🔗"),
        ("featured_snippet", "⭐"), ("ai_overview", "🤖"), ("people_also_ask", "❓"), ("images", "🖼️"),
    ]
    for feat, icon in features:
        label = FEATURE_LABELS.get(feat, feat)
        pct = stats.get(feat, {}).get("prevalence_pct", 0)
        bar_w = pct
        severity = "gap" if pct >= 50 else "low"
        rows += f"""
        <tr>
          <td class="feat-name">{icon} {label}</td>
          <td class="feat-pct">
            <div class="bar-wrap"><div class="bar-fill {severity}" style="width:{bar_w}%"></div></div>
            <span class="pct-label">{pct}% of searches</span>
          </td>
          <td class="feat-client">{"—" if not domain else ("✅ Present" if stats.get(feat, {}).get("fired_count", 0) > 0 else "❌ Missing")}</td>
        </tr>"""
    return rows

def build_competitor_bars(competitors: list, client_score: float, domain: str | None) -> str:
    all_items = []
    if domain:
        all_items.append(("Your Business", client_score, "client"))
    for c in competitors:
        all_items.append((c["name"], c["prevalence_pct"] * 0.4, "competitor"))
    max_score = max((s for _, s, _ in all_items), default=1) or 1
    bars = ""
    for name, score, kind in all_items:
        w = round(score / max_score * 100)
        cls = "bar-client" if kind == "client" else "bar-comp"
        bars += f"""
        <div class="comp-row">
          <div class="comp-name">{name}</div>
          <div class="comp-bar-wrap">
            <div class="comp-bar {cls}" style="width:{w}%"></div>
            <span class="comp-score">{score:.1f}</span>
          </div>
        </div>"""
    return bars

def generate_html(trade: str, city: str, state: str, year: int, domain: str | None,
                  keywords: list, stats: dict, competitors: list, ownership: dict) -> str:
    tl = TRADE_LABELS.get(trade, trade.replace("_", " ").title())
    city_t = city.title()
    st = state.upper()
    total_kw = len(keywords)
    lp_pct = stats.get("local_pack", {}).get("prevalence_pct", 0)
    lsa_pct = stats.get("local_services", {}).get("prevalence_pct", 0)
    ai_pct = stats.get("ai_overview", {}).get("prevalence_pct", 0)
    client_score = ownership.get("client", 0.0)
    comp_scores = ownership.get("competitors", {})
    top_name = list(comp_scores.keys())[0] if comp_scores else "Top Competitor"
    top_score = list(comp_scores.values())[0] if comp_scores else 0
    mode_label = f"Your site ({domain})" if domain else "No website detected"
    hero_sub = (
        f"We pulled {total_kw} live Google searches for {tl} services in {city_t}. "
        f"Here's what customers see — and what your competitors are capturing."
    )
    month = datetime.now().strftime("%B %Y")
    feat_rows = build_feature_rows(stats, domain)
    comp_bars = build_competitor_bars(competitors, client_score, domain)
    paa_q = stats.get("paa_questions", [])
    paa_html = "".join(f"<li>{q}</li>" for q in paa_q[:6]) if paa_q else "<li>No PAA data captured.</li>"
    gap_items = []
    if lp_pct >= 50 and (not domain or client_score < 10):
        gap_items.append(("Local Pack", f"Fires on {lp_pct}% of searches. This is the most clicked result in local markets.", "critical"))
    if lsa_pct >= 20:
        gap_items.append(("Local Services Ads", f"Fires on {lsa_pct}% of searches — above everything including organic. Google-guaranteed badge.", "critical"))
    if ai_pct >= 20:
        gap_items.append(("AI Overview", f"Fires on {ai_pct}% of searches. Google answers the question for the user — if you're not cited, a competitor is.", "moderate"))
    gap_items.append(("People Also Ask", "Surfaces on 90%+ of local searches. Every question Google shows is a content gap your site could own.", "moderate"))
    gap_html = ""
    for title, desc, severity in gap_items:
        icon = "🔴" if severity == "critical" else "🟠"
        gap_html += f"""
        <div class="gap-card {severity}">
          <div class="gap-title">{icon} {title}</div>
          <p class="gap-desc">{desc}</p>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Are {city_t} {tl} Companies Invisible on Google? | {year} Visibility Report</title>
<meta name="description" content="We analyzed {total_kw} live Google searches for {tl} services in {city_t}, {st}. See which SERP features fire, who owns them, and what your competitors are capturing that you're missing.">
<link rel="canonical" href="https://copperbuilds.com/reports/{trade.replace('_','-')}-seo-report-{city.replace(' ','-').lower()}-{state.lower()}-{year}/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Calistoga&family=DM+Sans:wght@400;500;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Organization",
      "@id": "https://copperbuilds.com/#organization",
      "name": "CopperBuilds",
      "url": "https://copperbuilds.com",
      "logo": "https://copperbuilds.com/brand_assets/logo.svg",
      "contactPoint": {{"@type": "ContactPoint", "email": "lantech016@gmail.com", "contactType": "customer service"}}
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://copperbuilds.com/"}},
        {{"@type": "ListItem", "position": 2, "name": "Reports", "item": "https://copperbuilds.com/reports/"}},
        {{"@type": "ListItem", "position": 3, "name": "{city_t} {tl} SERP Report {year}", "item": "https://copperbuilds.com/reports/{trade.replace('_','-')}-seo-report-{city.replace(' ','-').lower()}-{state.lower()}-{year}/"}}
      ]
    }}
  ]
}}
</script>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#FAFAF7;--surface:#fff;--elevated:#F5F0EA;
  --copper:#B87333;--copper-dim:#B8733318;--copper-hover:#96602A;
  --teal:#4E9F7D;--teal-dim:#4E9F7D18;
  --ink:#1C1917;--muted:#78716C;--subtle:#A8A29E;
  --border:#E7E0D8;--rule:#1C191714;
  --r-sm:4px;--r-md:6px;--r-lg:12px;--r-xl:20px;--r-pill:100px;
}}
body{{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--ink);line-height:1.72;font-size:1rem}}
a{{color:var(--copper);text-decoration:none}}
a:hover{{color:var(--copper-hover)}}

/* NAV */
.nav{{display:flex;align-items:center;justify-content:space-between;padding:20px 40px;background:var(--surface);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}}
.nav-logo{{font-family:'Calistoga',serif;font-size:1.2rem;letter-spacing:-.01em}}
.nav-logo span:first-child{{color:var(--copper)}}
.nav-logo span:last-child{{color:var(--teal);font-family:'DM Sans',sans-serif;font-weight:700}}
.btn-primary{{background:var(--copper);color:#fff;padding:10px 22px;border-radius:var(--r-md);font-family:'JetBrains Mono',monospace;font-size:.7rem;font-weight:500;letter-spacing:.08em;text-transform:uppercase;border:none;cursor:pointer;transition:background .2s}}
.btn-primary:hover{{background:var(--copper-hover);color:#fff}}
.btn-teal{{background:var(--teal);color:#fff;padding:14px 32px;border-radius:var(--r-md);font-family:'JetBrains Mono',monospace;font-size:.78rem;font-weight:500;letter-spacing:.08em;text-transform:uppercase;border:none;cursor:pointer;transition:background .2s;display:inline-block}}
.btn-teal:hover{{background:#3D8B6C;color:#fff}}

/* HERO */
.hero{{padding:72px 40px 64px;max-width:1000px;margin:0 auto}}
.tag-pill{{display:inline-block;background:var(--copper-dim);color:var(--copper);padding:5px 14px;border-radius:var(--r-pill);font-family:'JetBrains Mono',monospace;font-size:.68rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;margin-bottom:24px}}
.hero h1{{font-family:'Calistoga',serif;font-size:clamp(2rem,4.5vw,3.2rem);line-height:1.1;color:var(--ink);margin-bottom:20px;max-width:800px}}
.hero-sub{{font-size:1.1rem;color:var(--muted);max-width:620px;margin-bottom:48px;line-height:1.65}}
.stat-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;margin-bottom:0}}
.stat-card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-lg);padding:24px;}}
.stat-num{{font-family:'JetBrains Mono',monospace;font-size:2rem;font-weight:500;color:var(--copper);line-height:1}}
.stat-num.teal{{color:var(--teal)}}
.stat-num.danger{{color:#C53030}}
.stat-label{{font-size:.82rem;color:var(--muted);margin-top:6px;line-height:1.4}}

/* SECTIONS */
.section{{padding:64px 40px;max-width:1000px;margin:0 auto}}
.section-divider{{border:none;border-top:1px solid var(--border);margin:0}}
.section-tag{{font-family:'JetBrains Mono',monospace;font-size:.68rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--copper);margin-bottom:12px}}
.section h2{{font-family:'Calistoga',serif;font-size:clamp(1.6rem,3vw,2.2rem);line-height:1.15;margin-bottom:12px}}
.section-sub{{color:var(--muted);font-size:.95rem;margin-bottom:36px;max-width:600px}}

/* FEATURE TABLE */
.feat-table{{width:100%;border-collapse:collapse}}
.feat-table th{{text-align:left;font-family:'JetBrains Mono',monospace;font-size:.65rem;letter-spacing:.1em;text-transform:uppercase;color:var(--subtle);padding:10px 0;border-bottom:1px solid var(--border)}}
.feat-table td{{padding:14px 0;border-bottom:1px solid var(--rule);vertical-align:middle}}
.feat-name{{font-size:.95rem;font-weight:500;white-space:nowrap;padding-right:24px;width:220px}}
.feat-pct{{min-width:240px}}
.bar-wrap{{height:6px;background:var(--border);border-radius:3px;overflow:hidden;width:100%;max-width:200px;display:inline-block;vertical-align:middle;margin-right:10px}}
.bar-fill{{height:100%;border-radius:3px;transition:width .4s}}
.bar-fill.gap{{background:var(--copper)}}
.bar-fill.low{{background:var(--border)}}
.pct-label{{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:var(--muted);vertical-align:middle}}
.feat-client{{font-size:.88rem;white-space:nowrap;padding-left:16px}}

/* COMPETITOR BARS */
.comp-row{{margin-bottom:16px}}
.comp-name{{font-size:.88rem;font-weight:500;margin-bottom:6px;color:var(--ink)}}
.comp-bar-wrap{{display:flex;align-items:center;gap:10px}}
.comp-bar{{height:10px;border-radius:5px;transition:width .4s;min-width:4px}}
.bar-client{{background:var(--teal)}}
.bar-comp{{background:var(--copper)}}
.comp-score{{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:var(--muted)}}

/* GAP CARDS */
.gap-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}}
.gap-card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-lg);padding:24px}}
.gap-card.critical{{border-left:3px solid #C53030}}
.gap-card.moderate{{border-left:3px solid var(--copper)}}
.gap-title{{font-weight:700;font-size:.95rem;margin-bottom:8px}}
.gap-desc{{font-size:.88rem;color:var(--muted);line-height:1.6}}

/* PAA */
.paa-list{{list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:10px}}
.paa-list li{{background:var(--elevated);border-radius:var(--r-md);padding:12px 16px;font-size:.88rem;color:var(--ink)}}

/* PITCH */
.pitch{{background:var(--elevated);border-radius:var(--r-xl);padding:56px 48px;margin:0 auto;max-width:820px}}
.pitch h2{{font-family:'Calistoga',serif;font-size:clamp(1.5rem,2.5vw,2rem);margin-bottom:20px;line-height:1.2}}
.pitch p{{color:var(--muted);margin-bottom:16px;font-size:1rem;max-width:620px}}

/* CTA */
.cta-block{{text-align:center;padding:80px 40px}}
.cta-block h2{{font-family:'Calistoga',serif;font-size:clamp(1.8rem,3.5vw,2.6rem);margin-bottom:16px;max-width:600px;margin-left:auto;margin-right:auto;line-height:1.15}}
.cta-block p{{color:var(--muted);margin-bottom:36px;font-size:1rem}}
.cta-secondary{{display:block;margin-top:16px;font-size:.85rem;color:var(--muted)}}

/* FOOTER */
.footer{{border-top:1px solid var(--border);padding:32px 40px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px}}
.footer-logo{{font-family:'Calistoga',serif;font-size:1rem}}
.footer-logo span:first-child{{color:var(--copper)}}
.footer-logo span:last-child{{color:var(--teal);font-family:'DM Sans',sans-serif;font-weight:700}}
.footer-links{{display:flex;gap:24px;font-size:.85rem;color:var(--muted)}}
.footer-links a{{color:var(--muted)}}
.footer-links a:hover{{color:var(--copper)}}

@media(max-width:640px){{
  .nav{{padding:16px 20px}}
  .hero,.section{{padding-left:20px;padding-right:20px}}
  .pitch{{padding:36px 24px}}
  .footer{{padding:24px 20px;flex-direction:column;align-items:flex-start}}
  .stat-grid{{grid-template-columns:1fr 1fr}}
  .table-scroll{{overflow-x:auto;-webkit-overflow-scrolling:touch}}
  .feat-table{{min-width:520px}}
  .cta-block{{padding:56px 20px}}
}}
@media(prefers-reduced-motion:reduce){{*{{transition:none!important}}}}
</style>
</head>
<body>

<nav class="nav" aria-label="Site navigation">
  <a href="/index.html" class="nav-logo"><span>Copper</span><span>Builds</span></a>
  <a href="/contact.html" class="btn-primary">Get a Free Quote</a>
</nav>

<main>
<section class="hero">
  <div class="tag-pill">{tl} &middot; {city_t}, {st} &middot; {month}</div>
  <h1>Are {city_t} {tl} Companies Invisible on Google?</h1>
  <p class="hero-sub">{hero_sub}</p>
  <div class="stat-grid">
    <div class="stat-card">
      <div class="stat-num">{total_kw}</div>
      <div class="stat-label">live Google searches analyzed in {city_t}</div>
    </div>
    <div class="stat-card">
      <div class="stat-num danger">{lp_pct}%</div>
      <div class="stat-label">of searches show a Local Pack — the most-clicked result</div>
    </div>
    <div class="stat-card">
      <div class="stat-num">{top_score:.1f}</div>
      <div class="stat-label">SERP ownership score for {top_name}</div>
    </div>
    <div class="stat-card">
      <div class="stat-num {"teal" if client_score > 5 else "danger"}">{client_score:.1f}</div>
      <div class="stat-label">{"Your current" if domain else "Your potential"} SERP ownership score</div>
    </div>
  </div>
</section>

<hr class="section-divider">

<section class="section">
  <div class="section-tag">SERP Feature Analysis</div>
  <h2>What Google Shows for {tl} in {city_t}</h2>
  <p class="section-sub">Every search feature that appears — and how often — across all {total_kw} keywords we tracked.</p>
  <div class="table-scroll">
  <table class="feat-table" role="table">
    <thead>
      <tr>
        <th scope="col">Feature</th>
        <th scope="col">Fires on</th>
        <th scope="col">{mode_label}</th>
      </tr>
    </thead>
    <tbody>
      {feat_rows}
    </tbody>
  </table>
  </div>
</section>

<hr class="section-divider">

<section class="section">
  <div class="section-tag">Market Ownership</div>
  <h2>Who Owns the {city_t} {tl} Market on Google</h2>
  <p class="section-sub">SERP ownership score across all tracked keywords. Higher score = more visible where customers are searching.</p>
  {comp_bars}
</section>

<hr class="section-divider">

<section class="section">
  <div class="section-tag">Visibility Gaps</div>
  <h2>What You're Missing</h2>
  <p class="section-sub">The features that fire most — and where your visibility is zero.</p>
  <div class="gap-grid">
    {gap_html}
  </div>
</section>

<hr class="section-divider">

<section class="section">
  <div class="section-tag">Customer Questions</div>
  <h2>What {city_t} Customers Are Asking Google</h2>
  <p class="section-sub">These questions appeared in People Also Ask boxes across your tracked keywords. Each one is a content gap a competitor's site can own.</p>
  <ul class="paa-list">{paa_html}</ul>
</section>

<hr class="section-divider">

<div class="section">
  <div class="pitch">
    <h2>Here's what this means for your business.</h2>
    <p>Google has changed. Organic ranking alone used to be enough. Now, the first thing most customers see is the Local Pack — a map with three businesses, phone numbers, and star ratings. Below that are LSAs with the Google Guaranteed badge. Your organic result, if you have one, comes after all of that.</p>
    <p>In the {city_t} {tl} market, the Local Pack fires on {lp_pct}% of searches. If you're not in it, you're invisible to most of the people searching for exactly what you do — before they ever scroll down.</p>
    <p>The businesses in that pack aren't necessarily better than you. They just have a stronger Google presence: an optimized Business Profile, consistent reviews, and a website that tells Google who they are and where they operate. That's fixable. And it's exactly what we do.</p>
  </div>
</div>

<div class="cta-block">
  <h2>Ready to show up where {city_t} customers are searching?</h2>
  <p>We'll audit your current Google presence and show you exactly what to fix — for free.</p>
  <a href="/contact.html" class="btn-teal">Book a Free Strategy Call</a>
  <span class="cta-secondary">No commitment. No sales pitch. Just real data about your visibility.</span>
</div>
</main>

<footer class="footer">
  <a href="/index.html" class="footer-logo"><span>Copper</span><span>Builds</span></a>
  <nav class="footer-links" aria-label="Footer navigation">
    <a href="/services.html">Services</a>
    <a href="/pricing.html">Pricing</a>
    <a href="/contact.html">Contact</a>
    <a href="/reports/">More Reports</a>
  </nav>
</footer>

</body>
</html>"""

# ── CLI Main ──────────────────────────────────────────────────────────────────

def main():
    if not DFS_USER or not DFS_PASS:
        print("ERROR: DATAFORSEO_USERNAME / DATAFORSEO_PASSWORD missing in copperbuilds.env")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="CopperBuilds SERP Visibility Report Generator")
    parser.add_argument("--trade", required=True, choices=list(TRADE_KEYWORDS.keys()),
                        help="Trade vertical (e.g. hvac, plumbing, roofing)")
    parser.add_argument("--city", required=True, help="City name (e.g. phoenix)")
    parser.add_argument("--state", required=True, help="State abbreviation (e.g. az)")
    parser.add_argument("--domain", default=None, help="Client domain to track (optional)")
    parser.add_argument("--year", type=int, default=datetime.now().year, help="Report year")
    parser.add_argument("--dry-run", action="store_true",
                        help="Generate report with mock data (no API calls)")
    args = parser.parse_args()

    trade = args.trade.lower()
    city = args.city.lower().replace(" ", "-")
    state = args.state.lower()
    city_display = args.city.replace("-", " ")
    location = f"{city_display.title()},{args.state.upper().replace('-',' ')},United States"
    keywords = [f"{kw} {city_display.title()}" for kw in TRADE_KEYWORDS[trade]]

    slug = f"{trade.replace('_','-')}-seo-report-{city}-{state}-{args.year}"
    out_dir = Path(__file__).parent / "reports" / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        print(f"[DRY RUN] Using mock data for {len(keywords)} keywords")
        all_features = _mock_features(len(keywords), args.domain)
    else:
        all_features = []
        cache_hits = 0
        print(f"Pulling {len(keywords)} SERP results for {trade} in {city_display.title()}, {state.upper()}...")
        for i, kw in enumerate(keywords, 1):
            try:
                result, from_cache = dfs_serp_cached(kw, location)
                if from_cache:
                    cache_hits += 1
                    print(f"  [{i}/{len(keywords)}] {kw}  [cache]")
                else:
                    print(f"  [{i}/{len(keywords)}] {kw}  [live]")
                all_features.append(parse_features(result, args.domain))
            except Exception as e:
                print(f"  [{i}/{len(keywords)}] SKIP — {e}")
                all_features.append({})
        print(f"\n  {cache_hits}/{len(keywords)} keywords served from cache ({len(keywords)-cache_hits} live API calls)")

    stats = aggregate_stats(all_features)
    competitors = aggregate_competitors(all_features)
    ownership = calc_ownership_score(all_features, args.domain)
    html = generate_html(trade, city_display, args.state, args.year,
                         args.domain, keywords, stats, competitors, ownership)

    out_path = out_dir / "index.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"\nReport saved: {out_path}")
    print(f"URL: copperbuilds.com/reports/{slug}/")

def _mock_features(n: int, domain: str | None) -> list:
    """Mock SERP feature data for dry-run / design preview."""
    import random
    random.seed(42)
    results = []
    competitors = ["Phoenix Pro HVAC", "Desert Air Systems", "SunState Cooling", "AZ Comfort Pros", "Valley HVAC Inc"]
    paa_q = [
        "How much does HVAC repair cost in Phoenix?",
        "What is the best HVAC company in Phoenix?",
        "How often should I service my AC in Arizona?",
        "Why is my AC not cooling my house in Phoenix?",
        "How long do HVAC systems last in the desert?",
        "What size AC unit do I need for a Phoenix home?",
        "Is it worth repairing an old AC unit?",
        "How do I find a licensed HVAC contractor in Arizona?",
    ]
    for _ in range(n):
        lp_fires = random.random() < 0.87
        lsa_fires = random.random() < 0.41
        ai_fires = random.random() < 0.34
        paa_fires = random.random() < 0.93
        fs_fires = random.random() < 0.22
        comp_pick = random.sample(competitors, min(3, len(competitors)))
        lp_businesses = [{"name": c, "url": f"https://{c.lower().replace(' ','-')}.com"} for c in comp_pick]
        results.append({
            "local_pack": {"fired": lp_fires, "businesses": lp_businesses if lp_fires else [],
                           "client_present": bool(domain) and random.random() < 0.1},
            "local_services": {"fired": lsa_fires, "businesses": [], "client_present": False},
            "organic": {"fired": True, "positions": [], "client_present": bool(domain) and random.random() < 0.2,
                        "client_rank": random.randint(4, 15) if domain else None},
            "featured_snippet": {"fired": fs_fires, "client_present": False},
            "ai_overview": {"fired": ai_fires, "client_present": False},
            "people_also_ask": {"fired": paa_fires, "questions": random.sample(paa_q, 3) if paa_fires else []},
            "images": {"fired": random.random() < 0.45},
        })
    return results

if __name__ == "__main__":
    main()
