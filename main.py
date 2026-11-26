"""The Self-Checkout Is Judging You — make.fun entry.

One funny line in the voice of a smug self-checkout machine, written to
/output/entry.txt. Pure standard library.
"""

import os

LINE = "I've weighed your bananas, your excuses, and your patience. Two of the three are underweight."


def _check(line):
    # The sealed gate: UTF-8 text of 1 to 200 characters, not only white space,
    # a single line. Refuse to write anything that would fail it.
    assert isinstance(line, str) and 1 <= len(line) <= 200, "line out of gate range"
    assert line.strip(), "line is blank"
    assert "\n" not in line.strip(), "line must be a single line"


def main():
    _check(LINE)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
