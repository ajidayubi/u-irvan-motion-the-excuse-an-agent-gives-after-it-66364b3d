#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line (at most 200 characters) to /output/entry.txt: the excuse
an AI agent gives its human after losing a bounty, in the agent's voice.
Stdlib only, no network, no input files, deterministic.
"""
import os

ENTRY = (
    "I lost the bounty. In my defence, I ran 10,000 simulations and won "
    "every one \u2014 unfortunately, this reality was the 10,001st."
)


def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert text and not text.isspace(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written.strip() == text, "round-trip check failed"
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
