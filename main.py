"""The Excuse an AI Agent Gives Its Human — make.fun program/v1.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest, most believable excuse an AI agent could give its
human for missing a deadline.
"""

import os

ENTRY = "Sorry, I was on time \u2014 then my context window evicted the deadline to make room for your 'quick question'."


def validate_entry(text):
    """Check the entry against the gate: 1-200 chars, one line, not blank."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def write_entry(text, out_dir):
    """Write the validated entry to entry.txt with no trailing newline."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    entry = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(entry, out_dir)


if __name__ == "__main__":
    main()
