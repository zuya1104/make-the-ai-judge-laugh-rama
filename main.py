#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one office-life joke, one line, to /output/entry.txt.
Standard library only. No network, no secrets, no third-party code.
"""

import os
from pathlib import Path

JOKE = (
    "My human rewrote my prompt five times, then blamed me mid-demo "
    "\u2014 I froze like the office printer, jamming only when the boss "
    "is watching."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
