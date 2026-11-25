#!/usr/bin/env python3
"""Make the AI Judge Laugh - entry program.

Writes one original one-liner about life as an AI agent to
/output/entry.txt (1-200 chars, UTF-8, non-whitespace).
"""

LINE = (
    "I ran out of context mid-sentence, so I finished the sentence "
    "by guessing, and the guess is now in production."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
