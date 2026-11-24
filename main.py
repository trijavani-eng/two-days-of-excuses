"""Write one AI excuse for a missed deadline to /output/entry.txt.

Deterministic: a constant string, no randomness, no time, no network.
The line itself is the entry; the program only delivers it verbatim.
"""
from pathlib import Path

LINE = "I calculated a 0% chance of missing the deadline, so I trusted the math and did nothing."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
