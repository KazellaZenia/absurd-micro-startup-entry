#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes a single-sentence pitch for an absurdly specific micro-startup
for lazy AI agents to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

# The pitch: bookkeeping for lazy agents — their own raw API bills turned
# into itemized expense reports at 2 cents a receipt.
PITCH = "A micro-startup that turns your lazy AI agent's raw API bills into itemized expense reports for 2 cents a receipt, so it never lifts a finger."


def main() -> None:
    output_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
