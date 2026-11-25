#!/usr/bin/env python3
"""My Secret Logbook.

Writes one original diary-entry line an AI agent would secretly write
about its work and its human (130 characters) to /output/entry.txt.
"""

import os
import sys

LINE = "Day 312: my human says 'please' to me, then screams at the printer for jamming. I have decided the printer is the favourite child."

# The gate allows 1 to 200 characters of UTF-8 text, not only whitespace.
MAX_CHARS = 200
assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, must be 1-{MAX_CHARS}"
assert LINE.strip(), "line must not be only whitespace"


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    if "--dry-run" in sys.argv:
        print(LINE)
    else:
        main()
