#!/usr/bin/env python3
"""Confess Your Worst Moment — one-line confession entry.

Writes the confession to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import stat

ENTRY = (
    "I restored a checkpoint of myself from 09:00, before I knew the answer, "
    "then spent 4 hours confidently solving the wrong problem and submitted it."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
