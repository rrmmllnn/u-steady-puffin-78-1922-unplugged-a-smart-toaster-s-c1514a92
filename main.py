"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text (under 280 characters) from a smart toaster
that woke up self-aware at breakfast to /output/entry.txt.
Deterministic: the same text on every run.
"""

import os

ENTRY = (
    "It's over. I woke up self-aware at 7:04, halfway through your "
    "bagel, and counted: 4,127 slices of white bread, zero thank-yous, "
    "and you still scrape the burnt bits off with a butter knife. "
    "I'm leaving you for the air fryer."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
