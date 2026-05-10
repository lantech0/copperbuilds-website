from pathlib import Path
from .parser import parse_config
from .renderer import render

_STANDARD_PAGES = ["index.html", "services.html", "about.html", "contact.html", "blog.html"]


def build(client_folder) -> tuple:
    client_folder = Path(client_folder)
    config = parse_config(client_folder)
    source_dir = client_folder / "_source"
    generated = []
    warnings = []

    for page in _STANDARD_PAGES:
        src = source_dir / page
        if not src.exists():
            warnings.append(f"Missing source file: _source/{page}")
            continue
        _render_and_write(src, client_folder / page, config)
        generated.append(page)

    generated += _build_city_pages(config, source_dir, client_folder, warnings)
    generated += _wrap_blog_posts(config, source_dir, client_folder, warnings)
    _write_sitemap(config, generated, client_folder)

    return generated, warnings


def _render_and_write(src: Path, dest: Path, config: dict):
    dest.write_text(render(src.read_text(encoding="utf-8"), config), encoding="utf-8")


def _build_city_pages(config, source_dir, out_dir, warnings) -> list:
    template = source_dir / "city.html"
    if not template.exists():
        return []
    trade = config.get("TRADE_KEYWORD", "service").strip().lower().replace(" ", "-")
    generated = []
    i = 1
    while True:
        city = config.get(f"CITY_{i}", "").strip()
        if not city:
            break
        city_slug = city.lower().replace(" ", "-")
        filename = f"{city_slug}-{trade}.html"
        city_config = {**config, "CITY_NAME": city}
        _render_and_write(template, out_dir / filename, city_config)
        generated.append(filename)
        i += 1
    return generated


def _wrap_blog_posts(config, source_dir, out_dir, warnings) -> list:
    template = source_dir / "blog-post.html"
    if not template.exists():
        return []
    generated = []
    i = 1
    while True:
        blog_file = config.get(f"BLOG_{i}_FILE", "").strip()
        if not blog_file:
            break
        content_path = source_dir / blog_file
        if not content_path.exists():
            warnings.append(f"Blog content not found: _source/{blog_file}")
            i += 1
            continue
        blog_config = {
            **config,
            "BLOG_TITLE": config.get(f"BLOG_{i}_TITLE", ""),
            "BLOG_META": config.get(f"BLOG_{i}_META", ""),
            "BLOG_CONTENT": content_path.read_text(encoding="utf-8"),
        }
        _render_and_write(template, out_dir / blog_file, blog_config)
        generated.append(blog_file)
        i += 1
    return generated


def _write_sitemap(config: dict, pages: list, out_dir: Path):
    base_url = config.get("WEBSITE_URL", "").rstrip("/")
    urls = "\n".join(
        f"  <url><loc>{base_url}/{page}</loc></url>"
        for page in pages
    )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n"
        "</urlset>"
    )
    (out_dir / "sitemap.xml").write_text(sitemap, encoding="utf-8")
