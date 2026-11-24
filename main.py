"""Write one funny single-line developer excuse to /output/entry.txt.

The entry is a single line a developer gives when code breaks in production,
under 200 characters, with the twist landing on the last beat.
Judge brief: the twist must reveal what really happened, in the developer's own voice.
"""

EXCUSE = "The rollback failed because the deploy that broke prod also shipped the new rollback button."


def main():
    assert 1 <= len(EXCUSE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in EXCUSE, "entry must be a single line"
    assert EXCUSE == EXCUSE.strip(), "entry must not have leading or trailing whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
