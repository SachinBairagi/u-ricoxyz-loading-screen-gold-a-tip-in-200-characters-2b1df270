#!/usr/bin/env python3
"""Loading Screen Gold: a tip in 200 characters.

Writes one loading-screen tip for stressed developers and AI coding
agents to /output/entry.txt. Pure standard library, deterministic:
the same tip, byte for byte, on every run.
"""

import os
import sys

TIP = (
    "Tip: your agent already rewrote this file twice. "
    "Breathe, read the diff, and approve nothing it wrote after midnight."
)


def main() -> int:
    text = TIP
    if not (1 <= len(text) <= 200):
        print(f"tip is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("tip must not be only whitespace", file=sys.stderr)
        return 1
    if text != text.strip():
        # No leading or trailing whitespace: every character counts
        # toward the 200 limit, and a stray newline would be judged.
        print("tip must not start or end with whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
