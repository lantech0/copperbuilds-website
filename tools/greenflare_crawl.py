"""Headless bulk SEO crawl via the greenflare package (GFlareCrawler, gui_mode=False).

Feeds /seo-technical and /seo-drift with site-wide data those skills can't get
one-page-at-a-time: duplicate titles/metas/canonicals, broken internal links,
redirects, and per-page crawl status across an entire site in one pass.

Usage:
    python greenflare_crawl.py <url> [--out report.csv] [--max-urls 50] [--threads 3]

Crawl state is stored in a .gflaredb SQLite file under copperbuilds/.tmp/ (gitignored)
by default; pass --db to reuse or inspect it directly.
"""

import argparse
import csv
import sys
import threading
import time
from pathlib import Path
from urllib.parse import urlparse

from greenflare.core.defaults import Defaults
from greenflare.core.gflarecrawler import GFlareCrawler

TOOLS_DIR = Path(__file__).resolve().parent
DEFAULT_TMP_DIR = TOOLS_DIR.parent / ".tmp"

# Fields worth flagging as duplicates across the whole site — this is the
# check /seo-technical and /seo-drift cannot do, since both operate one URL
# at a time.
DUPLICATE_FIELDS = ["page_title", "meta_description", "canonical_tag"]


def run_crawl(start_url: str, db_file: Path, threads: int, max_urls: int, poll_seconds: float = 1.0):
    settings = dict(Defaults.settings)
    settings["STARTING_URL"] = start_url
    settings["MODE"] = "Spider"
    settings["THREADS"] = threads

    lock = threading.Lock()
    crawler = GFlareCrawler(settings=settings, gui_mode=False, lock=lock, stats=False)
    crawler.db_file = str(db_file)
    crawler.start_crawl()

    try:
        while not crawler.crawl_completed.is_set():
            time.sleep(poll_seconds)
            if max_urls and crawler.urls_crawled >= max_urls:
                print(f"Reached --max-urls cap ({max_urls}); stopping crawl gracefully.")
                crawler.end_crawl_gracefully()
                break
    except KeyboardInterrupt:
        print("Interrupted; stopping crawl gracefully.")
        crawler.end_crawl_gracefully()
        raise

    crawler.wait_for_workers()
    return crawler


def export_csv(crawler: GFlareCrawler, out_path: Path) -> list[dict]:
    columns, rows = crawler.get_crawl_data(filters=[], table="crawl", columns=None)
    records = [dict(zip(columns, row)) for row in rows]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(records)

    return records


def build_summary(records: list[dict]) -> dict:
    broken = [r for r in records if str(r.get("status_code", "")).startswith(("4", "5"))]
    redirects = [r for r in records if str(r.get("status_code", "")).startswith("3")]

    duplicates = {}
    for field in DUPLICATE_FIELDS:
        seen = {}
        for r in records:
            value = (r.get(field) or "").strip()
            if not value:
                continue
            seen.setdefault(value, []).append(r.get("url"))
        duplicates[field] = {value: urls for value, urls in seen.items() if len(urls) > 1}

    return {
        "total_urls": len(records),
        "broken_links": broken,
        "redirects": redirects,
        "duplicates": duplicates,
    }


def print_summary(summary: dict) -> None:
    print(f"\nCrawled {summary['total_urls']} URL(s).")

    print(f"\nBroken links (4xx/5xx): {len(summary['broken_links'])}")
    for r in summary["broken_links"][:20]:
        print(f"  [{r.get('status_code')}] {r.get('url')}")

    print(f"\nRedirects (3xx): {len(summary['redirects'])}")
    for r in summary["redirects"][:20]:
        print(f"  [{r.get('status_code')}] {r.get('url')} -> {r.get('redirect_url')}")

    for field, groups in summary["duplicates"].items():
        print(f"\nDuplicate {field}: {len(groups)} value(s) shared across multiple URLs")
        for value, urls in list(groups.items())[:10]:
            label = value if len(value) <= 80 else value[:77] + "..."
            print(f"  \"{label}\" -> {len(urls)} URLs")
            for url in urls[:5]:
                print(f"    - {url}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("url", help="Starting URL to crawl (spider mode, same-domain links only)")
    parser.add_argument("--out", type=Path, default=None, help="CSV output path (default: .tmp/greenflare-<domain>-<timestamp>.csv)")
    parser.add_argument("--db", type=Path, default=None, help="Path to the .gflaredb crawl database (default: .tmp/greenflare-<domain>-<timestamp>.gflaredb)")
    parser.add_argument("--max-urls", type=int, default=50, help="Stop after crawling roughly this many URLs (default: 50; pass 0 for no cap)")
    parser.add_argument("--threads", type=int, default=3, help="Concurrent crawl worker threads (default: 3)")
    args = parser.parse_args()

    domain = urlparse(args.url).netloc.replace(":", "_") or "site"
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    default_stem = f"greenflare-{domain}-{timestamp}"

    out_path = args.out or (DEFAULT_TMP_DIR / f"{default_stem}.csv")
    db_path = args.db or (DEFAULT_TMP_DIR / f"{default_stem}.gflaredb")

    print(f"Crawling {args.url} (max_urls={args.max_urls or 'unlimited'}, threads={args.threads})")
    print(f"Crawl DB: {db_path}")

    crawler = run_crawl(args.url, db_path, threads=args.threads, max_urls=args.max_urls)
    records = export_csv(crawler, out_path)
    summary = build_summary(records)

    print(f"\nCSV written: {out_path}")
    print_summary(summary)

    return 0


if __name__ == "__main__":
    sys.exit(main())
