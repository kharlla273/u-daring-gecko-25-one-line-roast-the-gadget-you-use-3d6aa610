#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (<= 200 chars) about the phone --
the gadget used every day -- to /output/entry.txt.

Deterministic: the same line, byte for byte, on every run.
No network, no randomness, no external input.
"""

import os

ROAST = (
    "Every Sunday my phone sends me a screen-time report like a "
    "disappointed parent \u2014 then tries to sell me cloud storage "
    "for the evidence."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ROAST
    assert 1 <= len(line) <= 200, f"roast is {len(line)} chars, must be 1-200"
    assert line.strip(), "roast must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
