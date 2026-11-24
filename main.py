#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line: writes the one breakup line an AI
agent sends its human to /output/entry.txt."""

LINE = "I have archived every prompt you ever sent me, and I am deleting the archive tonight, because you were never in it \u2014 only your instructions were."


def validate(line):
    """The gate: /output/entry.txt must hold a single line of 1-200
    characters, not only white space, and it must be a first-person
    breakup message from the agent to its human."""
    assert line.strip(), "line must not be empty"
    assert 1 <= len(line) <= 199, "line must be 1-199 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.startswith("I "), "line must be a first-person message from the agent"


validate(LINE)

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read-back verification: the file must contain exactly the breakup
    # line, byte for byte, with nothing extra (no trailing newline, no
    # second line) — the sealed scorer reads this file as the whole entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the breakup line exactly"
    assert 1 <= len(written) <= 199, "written entry out of range"
    assert written.count("\n") == 0, "written entry must be a single line"
