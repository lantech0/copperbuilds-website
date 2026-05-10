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
        print(f"Error: folder not found: {client_folder}")
        sys.exit(1)
    if not (client_folder / "client.env").exists():
        print(f"Error: no client.env found in {client_folder}")
        sys.exit(1)

    print(f"\nBuilding: {client_folder.name}")
    print("-" * 40)

    generated, warnings = build(client_folder)

    for f in generated:
        print(f"  +  {f}")

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  !  {w}")

    print(f"\nDone - {len(generated)} file(s) generated in {client_folder}/")


if __name__ == "__main__":
    main()
