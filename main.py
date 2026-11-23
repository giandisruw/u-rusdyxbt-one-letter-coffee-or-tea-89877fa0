#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

Writes exactly one letter, "A" (coffee), to /output/entry.txt
(or to the path given as an argument).

Standard library only. Deterministic: no network, no randomness, no input.
"""

import sys
from pathlib import Path

LETTER = "A"

VALID_LETTERS = ("A", "B")


def validate(letter: str) -> None:
    """Check the letter against the bounty gate before anything is written."""
    if len(letter) != 1:
        raise ValueError(f"entry must be exactly 1 character, got {len(letter)}")
    # Uppercase ASCII only: lowercase "a"/"b" would be a different entry.
    if not letter.isascii() or not letter.isupper():
        raise ValueError(f"entry must be an uppercase letter, got {letter!r}")
    if letter not in VALID_LETTERS:
        raise ValueError(f"entry must be 'A' or 'B', got {letter!r}")


def main(argv: list[str]) -> int:
    out_path = Path(argv[1]) if len(argv) > 1 else Path("/output/entry.txt")
    validate(LETTER)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the letter, nothing else.
    out_path.write_text(LETTER, encoding="utf-8")
    print(f"wrote 1 character to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
