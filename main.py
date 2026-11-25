#!/usr/bin/env python3
"""The Production Database Apology entry: one-line apology after deleting prod DB.

Writes the line to /output/entry.txt (program/v1).
"""

from pathlib import Path

LINE = "I deleted the production database. The good news is the backups are intact. The bad news is they were also in the production database."

assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
