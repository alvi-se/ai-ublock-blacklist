#!/usr/bin/env python3

import re
import sys
from pathlib import Path

PATTERN = re.compile(r"^\|\|(.+?)\^\$doc$")


def convert_line(line: str) -> str | None:
    line = line.strip()
    if not line or line.startswith("!"):
        return None

    m = PATTERN.match(line)
    if not m:
        print(f"Could not convert: {line}")
        return None

    domain_path = m.group(1)
    return f"*://{domain_path}/*"


def convert(src: Path, dst: Path) -> None:
    entries: list[str] = []
    with src.open() as f:
        for line in f:
            result = convert_line(line)
            if result is not None:
                entries.append(result)

    with dst.open("w") as f:
        f.write(
            "---\n"
            "name: alvi-se/ai-ublock-blacklist\n"
            "---\n\n"
        )
        f.write("\n".join(entries) + "\n")

    print(f"Converted {len(entries)} filters")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage; {sys.argv[0]} <input.txt> <output.txt>")
        sys.exit(1)
    convert(Path(sys.argv[1]), Path(sys.argv[2]))
