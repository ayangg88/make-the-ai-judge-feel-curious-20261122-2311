#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a small mystery built
to intrigue the AI judge reading it. A room never entered, a door
passed a thousand times, a letter waiting on a wooden table in the
reader's own handwriting -- that the reader never wrote. It ends
on the one question the reader cannot let go of, and leaves it
unanswered, so the text keeps working after the last line.
"""

import os

TEXT = (
    "There is a room you have never entered, though you have passed "
    "its door a thousand times. Inside, on a wooden table, a letter "
    "waits for you \u2014 in your own handwriting. You never wrote it. "
    "So who did?"
)


def main():
    # The gate allows 1 to 280 Unicode code points; refuse to write
    # anything outside it rather than submit an invalid entry.
    chars = len(TEXT)
    if not 1 <= chars <= 280:
        raise ValueError(f"entry text is {chars} characters, must be 1-280")
    if not TEXT.strip():
        raise ValueError("entry text must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
