#!/usr/bin/env python3
"""Write the entry: one invented word we need, plus its definition in one line.

The word is "rebye": the second goodbye to someone you said goodbye to
minutes earlier, after bumping into them again. Everybody has lived it --
saying goodbye at the lift, then meeting the same person again by the car
park, the corridor, or the front gate -- and until now there was no word
for it. "Rebye" is built from re- + bye, so it is sayable on first sight,
spellable on first hearing, and impossible to forget once you have used it.

Deterministic, stdlib only. Writes exactly one line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
"""

import os

LINE = "rebye (n.) \u2014 the second goodbye to someone you said goodbye to minutes earlier, after bumping into them again."


def main():
    # Gate: the entry must be UTF-8, one line, 1-140 characters, not only
    # whitespace. The competition caps the word plus its definition at 140.
    assert LINE == LINE.strip() and 1 <= len(LINE) <= 140 and LINE.strip(), "invalid entry line"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    LINE.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Echo the entry so a run visibly shows the word and definition
    # instead of exiting silently; the file content is unchanged.
    print(LINE)


if __name__ == "__main__":
    main()
