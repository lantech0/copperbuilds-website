"""
inject.py — Lantech site pre-deploy injector
Reads lantech.env and substitutes {{VAR}} placeholders in site HTML files.
Output goes to dist/ — deploy that folder, not the root.

Usage: python inject.py
"""

import sys
from pathlib import Path
from build.renderer import render

TARGET_FILES = [
    "contact.html",
]


def parse_env(path: Path) -> dict:
    config = {}
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                config[key.strip()] = value.strip()
    return config


def main():
    env_file = Path("lantech.env")
    if not env_file.exists():
        print("Error: lantech.env not found.")
        print("Copy lantech.env.example to lantech.env and fill in your values.")
        sys.exit(1)

    config = parse_env(env_file)

    if not config.get("WEB3FORMS_KEY"):
        print("Warning: WEB3FORMS_KEY is blank in lantech.env.")
        print("The contact form will not submit. Fill it in before deploying.")

    out_dir = Path("dist")
    out_dir.mkdir(exist_ok=True)

    for filename in TARGET_FILES:
        src = Path(filename)
        if not src.exists():
            print(f"  ! Missing: {filename}")
            continue
        content = render(src.read_text(encoding="utf-8"), config)
        dest = out_dir / filename
        dest.write_text(content, encoding="utf-8")
        print(f"  + dist/{filename}")

    print(f"\nDone. Upload dist/ files to Hostinger.")


if __name__ == "__main__":
    main()
