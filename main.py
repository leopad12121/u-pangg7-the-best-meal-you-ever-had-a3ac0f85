"""Write the best meal ever had, in one line, to /output/entry.txt.

The best meal was not the most expensive one: a $3 bowl of pho on a
plastic stool in Saigon, and every fine dinner since has been an apology
for not being it. One line, no setup it does not need.
Deterministic: the same single line on every run.
"""

import os
from pathlib import Path

MEAL = "A $3 bowl of pho on a plastic stool in Saigon; every expensive dinner since has been an apology for not being it."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(MEAL, encoding="utf-8")


if __name__ == "__main__":
    main()
