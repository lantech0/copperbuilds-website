import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', 'copperbuilds.env'))

USERNAME = os.getenv('DATAFORSEO_USERNAME')
PASSWORD = os.getenv('DATAFORSEO_PASSWORD')

# All keywords to validate — existing posts + proposed new topics
KEYWORDS = [
    # --- Existing blog posts ---
    "contractor website not ranking google",
    "how to choose a web designer for contractors",
    "how to get more google reviews",
    "small business website cost 2026",
    "website vs facebook page small business",
    "why isn't my website getting calls",
    "how to rank on google maps 2026",
    "local seo 2026",
    # --- Proposed Dallas-specific ---
    "hvac company website dallas tx",
    "hvac marketing dallas texas",
    "hvac seo dallas",
    "dallas hvac company not ranking google",
    "web design for hvac companies dallas",
    "how to get more hvac leads dallas",
    # --- Proposed general ---
    "how to choose a web designer for hvac company",
    "hvac marketing cost 2026",
    "hvac website design",
    "how to market an hvac company",
    "hvac company website cost",
    "web design for home service businesses",
]

def fetch_volumes(keywords, location_code=2840):
    """Fetch Google Ads search volumes via DataForSEO."""
    url = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
    payload = [{"keywords": keywords, "location_code": location_code, "language_code": "en"}]
    resp = requests.post(url, auth=(USERNAME, PASSWORD), json=payload)
    resp.raise_for_status()
    return resp.json()

def parse_results(data):
    results = []
    for task in data.get('tasks', []):
        for item in task.get('result', []):
            results.append({
                'keyword': item.get('keyword'),
                'volume': item.get('search_volume', 0),
                'competition': item.get('competition', 'n/a'),
                'competition_index': item.get('competition_index', 0),
                'cpc': item.get('cpc', 0),
            })
    return sorted(results, key=lambda x: x['volume'] or 0, reverse=True)

if __name__ == '__main__':
    print("Fetching keyword volumes from DataForSEO...")
    data = fetch_volumes(KEYWORDS)
    results = parse_results(data)

    print(f"\n{'Keyword':<50} {'Volume':>8} {'Competition':<14} {'CPC':>6}")
    print("-" * 82)
    for r in results:
        comp = r['competition'] if r['competition'] else 'n/a'
        cpc = f"${r['cpc']:.2f}" if r['cpc'] else 'n/a'
        vol = f"{r['volume']:,}" if r['volume'] else '0'
        print(f"{r['keyword']:<50} {vol:>8} {comp:<14} {cpc:>6}")

    # Save raw JSON for record
    out = os.path.join(os.path.dirname(__file__), 'kw_research_results.json')
    with open(out, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nRaw results saved to .tmp/kw_research_results.json")
