"""Deadpan forecast for Vexford, a city that does not exist.

Writes a single weather line of at most 160 characters to
/output/entry.txt, in the flat tone of a TV meteorologist who has
seen it all and is no longer surprised by any of it.
"""

from pathlib import Path

FORECAST = (
    "In Vexford, expect 19 degrees and a light rain of confetti, "
    "clearing by noon, with winds gusting to 47 and a 60% chance "
    "the mayor apologises by Friday."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate allows 1 to 160 characters; fail loudly rather than
    # hand in a line the judge never sees.
    if not 1 <= len(FORECAST) <= 160:
        raise ValueError(f"forecast is {len(FORECAST)} characters, must be 1-160")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORECAST, encoding="utf-8")


if __name__ == "__main__":
    main()
