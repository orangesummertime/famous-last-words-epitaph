#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one original line of famous last words, as a tombstone epitaph,
to /output/entry.txt. Python 3 standard library only, deterministic,
no input, no network access.
"""

import os

LINE = "I died doing what I loved: ignoring the warning label."

OUTPUT_PATH = "/output/entry.txt"


def verify():
    """Read the file back and check it is exactly one valid line."""
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises if not valid UTF-8
    lines = text.splitlines()
    assert len(lines) == 1, "entry must be exactly one line"
    assert 1 <= len(lines[0]) <= 150, "line must be 1-150 characters"
    assert lines[0] == LINE, "written line does not match the epitaph"
    assert (os.stat(OUTPUT_PATH).st_mode & 0o777) == 0o644, "mode must be 0644"
    return lines[0]


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    checked = verify()
    print("Wrote %d-character epitaph to %s" % (len(checked), OUTPUT_PATH))


if __name__ == "__main__":
    main()
