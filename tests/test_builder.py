from pathlib import Path
from build.builder import build


def _make_client(tmp_path, config_lines, source_files):
    (tmp_path / "client.env").write_text("\n".join(config_lines))
    source = tmp_path / "_source"
    source.mkdir()
    for name, content in source_files.items():
        (source / name).write_text(content)
    return tmp_path


def test_renders_standard_page(tmp_path):
    client = _make_client(
        tmp_path,
        ["BUSINESS_NAME=Priority Plumbing", "PHONE=239-555-0100", "WEBSITE_URL=https://test.com"],
        {"index.html": "<h1>{{BUSINESS_NAME}}</h1><p>{{PHONE}}</p>"},
    )
    generated, warnings = build(client)
    assert "index.html" in generated
    content = (client / "index.html").read_text()
    assert "Priority Plumbing" in content
    assert "239-555-0100" in content


def test_generates_city_pages(tmp_path):
    client = _make_client(
        tmp_path,
        ["CITY_1=Cape Coral", "CITY_2=Fort Myers", "SERVICE_1=Plumber", "TRADE_KEYWORD=plumber", "WEBSITE_URL=https://test.com"],
        {"city.html": "<h1>{{SERVICE_1}} in {{CITY_NAME}}</h1>"},
    )
    generated, _ = build(client)
    assert "cape-coral-plumber.html" in generated
    assert "fort-myers-plumber.html" in generated
    assert "Cape Coral" in (client / "cape-coral-plumber.html").read_text()
    assert "Fort Myers" in (client / "fort-myers-plumber.html").read_text()


def test_stops_city_generation_at_first_blank(tmp_path):
    client = _make_client(
        tmp_path,
        ["CITY_1=Cape Coral", "CITY_2=", "CITY_3=Naples", "TRADE_KEYWORD=plumber", "WEBSITE_URL=https://test.com"],
        {"city.html": "<h1>{{CITY_NAME}}</h1>"},
    )
    generated, _ = build(client)
    assert "cape-coral-plumber.html" in generated
    assert "naples-plumber.html" not in generated


def test_wraps_blog_post(tmp_path):
    client = _make_client(
        tmp_path,
        ["BLOG_1_TITLE=Test Post", "BLOG_1_META=Test meta", "BLOG_1_FILE=blog-drains.html", "WEBSITE_URL=https://test.com"],
        {
            "blog-post.html": "<title>{{BLOG_TITLE}}</title>{{BLOG_CONTENT}}",
            "blog-drains.html": "<p>Blog body here</p>",
        },
    )
    generated, _ = build(client)
    assert "blog-drains.html" in generated
    content = (client / "blog-drains.html").read_text()
    assert "Test Post" in content
    assert "Blog body here" in content


def test_warns_on_missing_source_file(tmp_path):
    client = _make_client(tmp_path, ["WEBSITE_URL=https://test.com"], {})
    _, warnings = build(client)
    assert any("index.html" in w for w in warnings)


def test_generates_sitemap(tmp_path):
    client = _make_client(
        tmp_path,
        ["WEBSITE_URL=https://priorityplumbing.com"],
        {"index.html": "<html></html>"},
    )
    build(client)
    sitemap = (client / "sitemap.xml").read_text()
    assert "priorityplumbing.com" in sitemap
    assert "index.html" in sitemap
