#!/usr/bin/env python
"""List or export palettes bundled with the npj-writing skill."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PALETTE_FILE = ROOT / "assets" / "color-palettes" / "npj_figure_palettes.json"


def load_data() -> dict:
    return json.loads(PALETTE_FILE.read_text(encoding="utf-8"))


def resolve_palette(data: dict, name: str) -> dict:
    aliases = data.get("aliases", {})
    palette_id = aliases.get(name, name)
    for palette in data["palettes"]:
        if palette["id"] == palette_id:
            return palette
    raise SystemExit(f"Unknown palette: {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("palette", nargs="?", help="Palette id or alias. Omit to list all palettes.")
    parser.add_argument("--format", choices=["plain", "json", "r", "python"], default="plain")
    args = parser.parse_args()

    data = load_data()
    if not args.palette:
        for palette in data["palettes"]:
            print(f"{palette['id']}\t{palette['name']}\t{len(palette['hex'])} colors\t{palette['category']}")
        return 0

    palette = resolve_palette(data, args.palette)
    colors = palette["hex"]

    if args.format == "json":
        print(json.dumps(palette, ensure_ascii=False, indent=2))
    elif args.format == "r":
        quoted = ", ".join(f'"{c}"' for c in colors)
        print(f"c({quoted})")
    elif args.format == "python":
        print(repr(colors))
    else:
        print(" ".join(colors))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
