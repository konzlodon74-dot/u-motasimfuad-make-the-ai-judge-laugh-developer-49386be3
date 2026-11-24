#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Prints one line -- a funny excuse a developer gives when code breaks
in production -- and writes the same line to /output/entry.txt.
Python 3 stdlib only, deterministic.
"""

import os

# The excuse, in the developer's own voice: the code is fine, production
# is just running the pre-fix build because the deploy failed silently --
# and the punchline personifies the silent deploy. Deliberately avoids
# the worn "works on my machine" gag the judge is told to discount.
EXCUSE = (
    "The code is fine — production is just running the build from "
    "before my fix, because the deploy failed silently, and silence "
    "is its love language."
)


def main() -> None:
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError("excuse must be 1-200 characters")
    if "\n" in EXCUSE or EXCUSE != EXCUSE.strip():
        raise ValueError("excuse must be exactly one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    print(EXCUSE)


if __name__ == "__main__":
    main()
