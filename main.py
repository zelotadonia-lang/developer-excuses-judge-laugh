"""Developer excuse entry for make.fun's "Make the AI Judge Laugh:
Developer Excuses" bounty.

Writes one single-line excuse to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "The canary went to 5% of users, and the 5% was everyone on the office Wi-Fi."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == ENTRY, "written output must match entry exactly"


if __name__ == "__main__":
    main()
