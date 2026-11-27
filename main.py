"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

The entry is the Moon's answer at last to everyone staring up at it:
four billion years of wishes, howls and promises, and nobody has ever
said goodnight back. Wry, old, a little tired of being wished upon —
the turn lands in the second half, and nobody explains the joke.

How it runs: `python3 main.py` (Python 3.13, standard library only, no
network). It creates /output if needed and writes the entry line to
/output/entry.txt with no trailing newline, so the file holds exactly the
99 characters of the comeback. Verification, 2026-11-27: ran main.py,
read back /output/entry.txt — exact match with the intended line,
99 characters, 19 words, 1 line, UTF-8, inside the competition's 1-240
character gate; sha256 21fd9354a3f352f041a6419f529618607a5641730b034fe2b45624606259289b.
"""

import os

TEXT = "Four billion years of wishes, howls and promises — and not one of you has ever said goodnight back."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 99 characters, nineteen
# words; the Moon answers the wishes, the howls and the late-night
# promises in a single breath, and the comeback is the goodnight nobody
# ever gave back.
# Second edit: docstring extended with run instructions and verification
# notes; re-ran and confirmed byte-identical output (entry.txt sha256
# unchanged).
