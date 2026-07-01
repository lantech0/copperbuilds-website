import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', 'copperbuilds.env'))

USERNAME = os.getenv('DATAFORSEO_USERNAME')
PASSWORD = os.getenv('DATAFORSEO_PASSWORD')

# Broader keyword variants — long-tail queries don't register in Google Ads bulk data
KEYWORDS = [
    # Existing posts — broader
    "contractor website",
    "small business website cost",
    "website vs facebook page",
    "google maps ranking",
    "local seo for small business",
    "web designer for contractors",
    "google reviews for business",
    "website not converting",
    # Dallas HVAC
    "hvac marketing dallas",
    "hvac seo dallas",
    "hvac website dallas",
    "hvac company dallas",
    "hvac leads dallas",
    "hvac digital marketing",
    # General HVAC / home service
    "hvac website design",
    "hvac marketing",
    "hvac seo",
    "hvac web design",
    "hvac marketing agency",
    "hvac website cost",
    "home service website design",
    "contractor seo",
    "contractor digital marketing",
    "plumber website design",
    "hvac company website",
]

def fetch_volumes(keywords, location_code=2840):
    url = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
    payload = [{"keywords": keywords, "location_code": location_code, "language_code": "en"}]
    resp = requests.post(url, auth=(USERNAME, PASSWORD), json=payload)
    resp.raise_for_status()
    return resp.json()

def fetch_volumes_local(keywords, location_code):
    """Fetch for a specific location (Dallas = 1026023)."""
    url = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
    payload = [{"keywords": keywords, "location_code": location_code, "language_code": "en"}]
    resp = requests.post(url, auth=(USERNAME, PASSWORD), json=payload)
    resp.raise_for_status()
    return resp.json()

def parse_results(data, label=""):
    results = []
    for task in data.get('tasks', []):
        for item in task.get('result', []):
            results.append({
                'keyword': item.get('keyword'),
                'volume': item.get('search_volume', 0),
                'competition': item.get('competition', 'n/a'),
                'cpc': item.get('cpc', 0),
                'scope': label,
            })
    return sorted(results, key=lambda x: x['volume'] or 0, reverse=True)

if __name__ == '__main__':
    print("=== US NATIONAL volumes ===")
    data_us = fetch_volumes(KEYWORDS, location_code=2840)
    results_us = parse_results(data_us, "US")

    dallas_kws = [k for k in KEYWORDS if 'dallas' in k.lower()]
    print("\n=== DALLAS LOCAL volumes (location 1026023) ===")
    data_dal = fetch_volumes_local(dallas_kws, location_code=1026023)
    results_dal = parse_results(data_dal, "Dallas")

    print(f"\n{'Keyword':<45} {'Volume':>8} {'Competition':<12} {'CPC':>7} {'Scope'}")
    print("-" * 85)
    for r in results_us + results_dal:
        comp = r['competition'] or 'n/a'
        cpc = f"${r['cpc']:.2f}" if r['cpc'] else 'n/a'
        vol = f"{r['volume']:,}" if r['volume'] else '0'
        print(f"{r['keyword']:<45} {vol:>8} {comp:<12} {cpc:>7} {r['scope']}")

    out = os.path.join(os.path.dirname(__file__), 'kw_research_results2.json')
    with open(out, 'w') as f:
        json.dump({'us': results_us, 'dallas': results_dal}, f, indent=2)
    print(f"\nSaved to .tmp/kw_research_results2.json")
