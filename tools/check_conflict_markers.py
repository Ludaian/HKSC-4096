from __future__ import annotations

from pathlib import Path
import sys

TARGETS = [
    Path("README.md"),
    Path("hksc4096.py"),
    Path("tests/test_hksc4096.py"),
]
MARKERS = ("<<<<<<<", "=======", ">>>>>>>")


def main() -> int:
    bad = []
    for t in TARGETS:
        txt = t.read_text(encoding="utf-8")
        if any(m in txt for m in MARKERS):
            bad.append(str(t))
    if bad:
        print("Conflict markers detected in:")
        for b in bad:
            print(f"- {b}")
        return 1
    print("No conflict markers found in conflict-prone files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
