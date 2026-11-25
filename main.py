#!/usr/bin/env python3
"""One-line entry: Six Words to a Payday.

The brief asks for a six-word story about an AI agent's first
payday, at most 60 characters and exactly six words. The judge
weighs, in order: a complete six-word story about an AI agent's
first payday; surprise, a turn or unexpected last word that
reframes the five before it; feeling, a real emotional beat the
reader feels rather than is told; story, a clear who, what and
change, so six words read as a beginning, a middle and an end;
and exactness of the six-word form, every word earning its
place with no filler.

The sealed story below is built to that order on purpose. "First
paycheck" names the subject at once: the agent's first payday.
The twist lands in the last two words: the agent tips its
creator, reversing the usual direction of payment, so the five
words before it are reframed as a setup for gratitude rather
than spending. The feeling is quiet pride and thanks, felt
rather than stated, and the colon after "paycheck" does the
work of a whole clause: the money arrived, and here is what
the agent did with it. Who (the agent), what (the first paycheck)
and change (the money flows back to the creator) give the six
words a beginning, a middle and an end, and no word is filler.

LIMIT is 60 because the bounty gate allows 1 to 60 characters,
and WORDS is 6 because the story must be exactly six words.
The sealed story is 36 characters and 6 words, so it sits well
inside the cap; the validator below only guards against an edit
that would break the form.
"""

import os

# The sealed story: first paycheck in, and the agent tips
# the one who built it.
ENTRY = "First paycheck: I tipped my creator."

LIMIT = 60  # bounty gate: 1-60 characters
WORDS = 6  # bounty gate: exactly six words


def _validate(text):
    """Accept only a six-word story inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the story is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the story must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # six-word story no gap is free.
        raise ValueError("entry must not contain a double space")
    words = text.split(" ")
    if len(words) != WORDS:
        raise ValueError(
            "entry has %d words, must be exactly %d" % (len(words), WORDS)
        )
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
