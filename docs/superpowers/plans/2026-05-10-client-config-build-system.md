# Client Config + Build System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python rendering engine that reads `client.env` and generates a complete, FTP-ready HTML website for each client.

**Architecture:** Three-module pipeline — parser reads `client.env` into a dict, renderer does `{{VAR}}` substitution on HTML source files, builder orchestrates file generation (standard pages, city pages, blog wrapping, sitemap). The CLI (`build.py`) is the single entry point. Claude builds `_source/` HTML files with placeholder syntax during the normal `/lantech-build` process; the build script renders them into the final uploadable files.

**Tech Stack:** Python 3.9+ (stdlib only — no external dependencies), pytest for tests.

---

## File Structure

```
lantech-website/
  build.py                          ← CLI entry point
  build/
    __init__.py                     ← makes build a package
    parser.py                       ← parse client.env → dict
    renderer.py                     ← {{VAR}} substitution engine
    builder.py                      ← orchestrate all file generation
  tests/
    __init__.py
    test_parser.py
    test_renderer.py
    test_builder.py
  clients/
    templates/
      client.env                    ← blank config template (copy per client)

clients/active/[slug]-[YYYY-MM]/   ← per-client folder
  client.env                        ← populated config
  _source/                          ← HTML files with {{PLACEHOLDERS}} (built by Claude)
    index.html
    services.html
    about.html
    contact.html
    blog.html
    city.html                       ← city page template
    blog-post.html                  ← blog post wrapper template
    blog-*.html                     ← blog content files
  index.html                        ← rendered output (upload these)
  services.html
  about.html
  contact.html
  blog.html
  cape-coral-plumber.html           ← one per CITY_N
  sitemap.xml
```

---

### Task 1: Config Parser

**Files:**
- Create: `lantech-website/build/__init__.py`
- Create: `lantech-website/build/parser.py`
- Create: `lantech-website/tests/__init__.py`
- Create: `lantech-website/tests/test_parser.py`

- [ ] **Step 1: Create empty package init files**

`lantech-website/build/__init__.py` — empty file:
```python
```

`lantech-website/tests/__init__.py` — empty file:
```python
```

- [ ] **Step 2: Write the failing tests**

```python
# lantech-website/tests/test_parser.py
import pytest
from pathlib import Path
from build.parser import parse_config


def test_parses_key_value_pairs(tmp_path):
    (tmp_path / "client.env").write_text("BUSINESS_NAME=Priority Plumbing\nPHONE=+1-239-555-0100\n")
    result = parse_config(tmp_path)
    assert result["BUSINESS_NAME"] == "Priority Plumbing"
    assert result["PHONE"] == "+1-239-555-0100"


def test_blank_values_return_empty_string(tmp_path):
    (tmp_path / "client.env").write_text("FACEBOOK=\n")
    result = parse_config(tmp_path)
    assert result["FACEBOOK"] == ""


def test_comments_and_blank_lines_ignored(tmp_path):
    (tmp_path / "client.env").write_text("# This is a comment\n\nBUSINESS_NAME=Acme\n")
    result = parse_config(tmp_path)
    assert "# This is a comment" not in result
    assert result["BUSINESS_NAME"] == "Acme"


def test_values_with_equals_sign(tmp_path):
    (tmp_path / "client.env").write_text("HOME_META=Fast plumber = reliable service\n")
    result = parse_config(tmp_path)
    assert result["HOME_META"] == "Fast plumber = reliable service"


def test_missing_config_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        parse_config(tmp_path)
```

- [ ] **Step 3: Run tests to confirm they fail**

Run from `lantech-website/`:
```bash
python -m pytest tests/test_parser.py -v
```
Expected: `ImportError` or `ModuleNotFoundError` — `build.parser` does not exist yet.

- [ ] **Step 4: Write the implementation**

```python
# lantech-website/build/parser.py
from pathlib import Path


def parse_config(client_folder) -> dict:
    config_path = Path(client_folder) / "client.env"
    if not config_path.exists():
        raise FileNotFoundError(f"client.env not found in {client_folder}")
    config = {}
    with open(config_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                config[key.strip()] = value.strip()
    return config
```

- [ ] **Step 5: Run tests to confirm they pass**

```bash
python -m pytest tests/test_parser.py -v
```
Expected: 5 tests PASS.

- [ ] **Step 6: Commit**

```bash
git add build/__init__.py build/parser.py tests/__init__.py tests/test_parser.py
git commit -m "feat: add client.env config parser"
```

---

### Task 2: Template Renderer

**Files:**
- Create: `lantech-website/build/renderer.py`
- Create: `lantech-website/tests/test_renderer.py`

- [ ] **Step 1: Write the failing tests**

```python
# lantech-website/tests/test_renderer.py
from build.renderer import render


def test_replaces_known_variable():
    result = render("<p>{{BUSINESS_NAME}}</p>", {"BUSINESS_NAME": "Priority Plumbing"})
    assert result == "<p>Priority Plumbing</p>"


def test_missing_variable_renders_empty():
    result = render("<p>{{UNKNOWN}}</p>", {})
    assert result == "<p></p>"


def test_blank_value_renders_empty():
    result = render("<a href='{{FACEBOOK}}'>FB</a>", {"FACEBOOK": ""})
    assert result == "<a href=''>FB</a>"


def test_multiple_variables_in_one_template():
    template = "<title>{{SERVICE_1}} in {{CITY_NAME}} | {{BUSINESS_NAME}}</title>"
    config = {"SERVICE_1": "Plumber", "CITY_NAME": "Cape Coral", "BUSINESS_NAME": "Priority Plumbing"}
    result = render(template, config)
    assert result == "<title>Plumber in Cape Coral | Priority Plumbing</title>"


def test_does_not_touch_css_var_syntax():
    result = render("color: var(--accent);", {"accent": "red"})
    assert result == "color: var(--accent);"
```

- [ ] **Step 2: Run tests to confirm they fail**

```bash
python -m pytest tests/test_renderer.py -v
```
Expected: `ImportError` — `build.renderer` does not exist yet.

- [ ] **Step 3: Write the implementation**

```python
# lantech-website/build/renderer.py
import re

_PATTERN = re.compile(r"\{\{(\w+)\}\}")


def render(template: str, config: dict) -> str:
    return _PATTERN.sub(lambda m: config.get(m.group(1), ""), template)
```

- [ ] **Step 4: Run tests to confirm they pass**

```bash
python -m pytest tests/test_renderer.py -v
```
Expected: 5 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add build/renderer.py tests/test_renderer.py
git commit -m "feat: add {{VAR}} template renderer"
```

---

### Task 3: Page Builder

**Files:**
- Create: `lantech-website/build/builder.py`
- Create: `lantech-website/tests/test_builder.py`

- [ ] **Step 1: Write the failing tests**

```python
# lantech-website/tests/test_builder.py
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
```

- [ ] **Step 2: Run tests to confirm they fail**

```bash
python -m pytest tests/test_builder.py -v
```
Expected: `ImportError` — `build.builder` does not exist yet.

- [ ] **Step 3: Write the implementation**

```python
# lantech-website/build/builder.py
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
```

- [ ] **Step 4: Run tests to confirm they pass**

```bash
python -m pytest tests/test_builder.py -v
```
Expected: 6 tests PASS.

- [ ] **Step 5: Run the full test suite**

```bash
python -m pytest tests/ -v
```
Expected: 16 tests PASS.

- [ ] **Step 6: Commit**

```bash
git add build/builder.py tests/test_builder.py
git commit -m "feat: add page builder — standard pages, city pages, blog wrapping, sitemap"
```

---

### Task 4: CLI Entry Point

**Files:**
- Create: `lantech-website/build.py`

- [ ] **Step 1: Write the implementation**

```python
# lantech-website/build.py
import sys
from pathlib import Path
from build.builder import build


def main():
    if len(sys.argv) != 2:
        print("Usage: python build.py <client-folder>")
        print("Example: python build.py clients/active/priority-plumbing-2026-05")
        sys.exit(1)

    client_folder = Path(sys.argv[1])
    if not client_folder.is_dir():
        print(f"Error: folder not found — {client_folder}")
        sys.exit(1)
    if not (client_folder / "client.env").exists():
        print(f"Error: no client.env found in {client_folder}")
        sys.exit(1)

    print(f"\nBuilding: {client_folder.name}")
    print("─" * 40)

    generated, warnings = build(client_folder)

    for f in generated:
        print(f"  ✓  {f}")

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  ⚠  {w}")

    print(f"\nDone — {len(generated)} file(s) generated in {client_folder}/")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Create a test client folder and run the CLI**

```bash
python -c "
from pathlib import Path
p = Path('clients/active/test-client-2026-05/_source')
p.mkdir(parents=True, exist_ok=True)
(p.parent / 'client.env').write_text('BUSINESS_NAME=Test Biz\nPHONE=555-1234\nWEBSITE_URL=https://test.com\n')
(p / 'index.html').write_text('<h1>{{BUSINESS_NAME}}</h1><p>{{PHONE}}</p>')
"
python build.py clients/active/test-client-2026-05
```

Expected output:
```
Building: test-client-2026-05
────────────────────────────────────────
  ✓  index.html
  ⚠  Missing source file: _source/services.html
  ⚠  Missing source file: _source/about.html
  ⚠  Missing source file: _source/contact.html
  ⚠  Missing source file: _source/blog.html

Done — 1 file(s) generated in clients/active/test-client-2026-05/
```

- [ ] **Step 3: Verify the rendered file contains real values**

```bash
python -c "print(open('clients/active/test-client-2026-05/index.html').read())"
```
Expected: `<h1>Test Biz</h1><p>555-1234</p>`

- [ ] **Step 4: Clean up the test folder**

```bash
python -c "import shutil; shutil.rmtree('clients/active/test-client-2026-05')"
```

- [ ] **Step 5: Commit**

```bash
git add build.py
git commit -m "feat: add build.py CLI entry point"
```

---

### Task 5: Blank Config Template

**Files:**
- Create: `lantech-website/clients/templates/client.env`

- [ ] **Step 1: Write the blank config template**

```bash
# ════════════════════════════════════════════════
#  LANTECH CLIENT CONFIG
#  [Business Name] — [City, State]
#  Claude populates this from the questionnaire.
#  Review all fields before running build.py.
# ════════════════════════════════════════════════

# ── BUSINESS INFO ────────────────────────────────
BUSINESS_NAME=
TAGLINE=
PHONE=
EMAIL=
ADDRESS=
HOURS=
YEARS_IN_BUSINESS=
LICENSE_NUMBER=
REVIEW_COUNT=
EMERGENCY_SERVICE=        # yes / no
WEBSITE_URL=              # https://clientdomain.com — required for sitemap

# ── BRAND ────────────────────────────────────────
PRIMARY_COLOR=
ACCENT_COLOR=
FONT=

# ── EXTERNAL LINKS ───────────────────────────────
# Leave blank to hide the link/icon on the site
GOOGLE_BUSINESS=
FACEBOOK=
YELP=
NEXTDOOR=
BBB=
INSTAGRAM=

# ── FORM ─────────────────────────────────────────
WEB3FORMS_KEY=
FORM_BUTTON=Get a Free Estimate

# ── SERVICES ─────────────────────────────────────
SERVICE_1=
SERVICE_2=
SERVICE_3=
SERVICE_4=
SERVICE_5=
SERVICE_6=

# ── TRADE KEYWORD ────────────────────────────────
# Used in city page URLs: cape-coral-[TRADE_KEYWORD].html
# Examples: plumber / electrician / roofer / landscaper / hvac
TRADE_KEYWORD=

# ── CITIES SERVED ────────────────────────────────
# One SEO page auto-generated per populated city
# Generation stops at the first blank city
CITY_1=
CITY_2=
CITY_3=
CITY_4=
CITY_5=

# ── SEO — HOME ───────────────────────────────────
HOME_TITLE=
HOME_META=

# ── SEO — SERVICES ───────────────────────────────
SERVICES_TITLE=
SERVICES_META=

# ── SEO — ABOUT ──────────────────────────────────
ABOUT_TITLE=
ABOUT_META=

# ── SEO — CONTACT ────────────────────────────────
CONTACT_TITLE=
CONTACT_META=

# ── SEO — BLOG INDEX ─────────────────────────────
BLOG_TITLE=
BLOG_META=

# ── INTERNAL LINKS — HOME ────────────────────────
HOME_LINK_1_TEXT=
HOME_LINK_1_URL=
HOME_LINK_2_TEXT=
HOME_LINK_2_URL=
HOME_LINK_3_TEXT=
HOME_LINK_3_URL=

# ── INTERNAL LINKS — SERVICES ────────────────────
SERVICES_LINK_1_TEXT=
SERVICES_LINK_1_URL=
SERVICES_LINK_2_TEXT=
SERVICES_LINK_2_URL=
SERVICES_LINK_3_TEXT=
SERVICES_LINK_3_URL=

# ── BLOG POSTS ───────────────────────────────────
# Claude writes each content file to _source/
# Add the filename and SEO details here after writing
BLOG_1_TITLE=
BLOG_1_META=
BLOG_1_FILE=
BLOG_2_TITLE=
BLOG_2_META=
BLOG_2_FILE=
BLOG_3_TITLE=
BLOG_3_META=
BLOG_3_FILE=
```

- [ ] **Step 2: Verify it parses cleanly with no errors**

```bash
python -c "
import shutil, tempfile
from pathlib import Path
from build.parser import parse_config
tmp = Path(tempfile.mkdtemp())
shutil.copy('clients/templates/client.env', tmp / 'client.env')
cfg = parse_config(tmp)
print(f'OK — {len(cfg)} fields parsed, all blank values handled correctly')
shutil.rmtree(tmp)
"
```
Expected: `OK — 38+ fields parsed, all blank values handled correctly`

- [ ] **Step 3: Commit**

```bash
git add clients/templates/client.env
git commit -m "feat: add blank client.env config template"
```

---

### Task 6: Update Project Workflow

**Files:**
- Modify: `lantech-website/workflows/project.md` — Step 5 and Step 6 only

- [ ] **Step 1: In `workflows/project.md`, replace the Step 5 body with this**

Find the `### Step 5 — Questionnaire Received` section and update it:

```markdown
### Step 5 — Questionnaire Received

When the completed questionnaire arrives:

1. Review all answers. Flag any gaps (missing logo, no photos, incomplete address).
2. Fill in `06-client-brief.md` from the questionnaire answers.
3. **Populate `client.env` from the questionnaire answers:**
   - Copy `clients/templates/client.env` into the client folder
   - Fill every field Claude can derive from the questionnaire:
     - Business info: name, phone, email, address, hours
     - Services list (SERVICE_1..N)
     - Cities served (CITY_1..N)
     - Emergency service flag
     - Years in business, license number, review count
     - External links: GMB, Facebook, Yelp, Nextdoor, BBB, Instagram
     - TRADE_KEYWORD: derive from SERVICE_1 (e.g. "Drain Cleaning" → "plumber")
     - WEBSITE_URL: client's existing domain if they have one
   - Generate SEO fields using the formula in `docs/superpowers/specs/2026-05-10-client-config-build-system-design.md`
   - Generate internal links using the SEO strategy in that same spec
   - Leave `WEB3FORMS_KEY=` blank — collected after account setup
4. Show the populated `client.env` to the user for review and confirmation.
5. If any required fields are missing, send one clarifying email. Do not start the build until confirmed.
6. Upload completed `02-onboarding-questionnaire.md` and `06-client-brief.md` to the client's Drive folder.
7. Confirm receipt to the client.
```

- [ ] **Step 2: Replace the Step 6 body with this**

Find the `### Step 6 — Trigger the Build` section and update it:

```markdown
### Step 6 — Trigger the Build

With `client.env` confirmed and the brief complete:

1. **Run `/lantech-build`** using `client.env` and `06-client-brief.md` as data sources.
   - Build all HTML pages using `{{PLACEHOLDER}}` syntax for every variable value
     (phone numbers, SEO fields, nav links, external links, colors, form key).
   - Save all source files to `clients/active/[slug]/_source/`.
   - Required source files: `index.html`, `services.html`, `about.html`,
     `contact.html`, `blog.html`, `city.html`, `blog-post.html`.
2. **Render the final site:**
   ```
   python build.py clients/active/[slug]-[YYYY-MM]/
   ```
3. Review the build output. Warnings about missing source files must be resolved before QA.
4. Run the full QA process in `workflows/client-build-standards.md`.
5. **Post-launch changes:** edit `client.env` → rerun `python build.py` → FTP upload changed files.
```

- [ ] **Step 3: Run full test suite to confirm nothing is broken**

```bash
python -m pytest tests/ -v
```
Expected: 16 tests PASS.

- [ ] **Step 4: Commit**

```bash
git add workflows/project.md
git commit -m "feat: integrate client.env config step into project intake workflow"
```

---

## Self-Review

**Spec coverage:**
| Spec requirement | Task that covers it |
|---|---|
| Config file format (label=value) | Task 5 — blank template |
| Claude populates all fields | Task 6 — workflow Step 5 |
| SEO titles + meta auto-generated | Task 6 — references spec formula |
| Internal links SEO strategy | Task 6 — references spec strategy |
| Standard page generation | Task 3 — `_STANDARD_PAGES` loop |
| City page auto-generation | Task 3 — `_build_city_pages` |
| Blog post wrapping | Task 3 — `_wrap_blog_posts` |
| Sitemap generation | Task 3 — `_write_sitemap` |
| Rendered files in client root (not subfolder) | Task 3 — writes to `client_folder / filename` |
| `_source/` for template files | Task 3 — reads from `client_folder / "_source"` |
| Post-launch change workflow | Task 4 CLI + Task 6 Step 5 note |
| Workflow integration (project.md) | Task 6 |
| `WEBSITE_URL` for sitemap | Task 3 + Task 5 |
| `TRADE_KEYWORD` for city URLs | Task 3 + Task 5 |

**Placeholder scan:** No TBDs, TODOs, or vague steps.

**Type consistency:**
- `parse_config(client_folder) -> dict` — consistent across parser, builder, tests
- `render(template: str, config: dict) -> str` — consistent across renderer, builder, tests
- `build(client_folder) -> tuple` — consistent across builder and CLI
- `CITY_NAME` injected into `city_config` in Task 3 — matches `{{CITY_NAME}}` in test template
- `BLOG_TITLE`, `BLOG_META`, `BLOG_CONTENT` injected into `blog_config` in Task 3 — matches test template
