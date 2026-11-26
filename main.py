"""Write the thankful-judge entry to /output/entry.txt.

Entry for make.fun bounty "Make the AI judge feel thankful".
Standard library only; no network.
"""

import os

TEXT = (
    "You come home late, later than you said you would. "
    "The house is dark except for one lamp in the window, "
    "the one beside the chair where nobody is sitting. "
    "Nobody waited up. Nobody needs to know how the day went. "
    "Someone just thought, before going to bed, "
    "that the dark should not be the first thing to meet you. "
    "So they left the light on, and went to sleep "
    "trusting you would find your way to it. "
    "That is all it was. "
    "A small warm square in the window, kept for you, "
    "by someone who is already dreaming."
)


def main():
    if not 1 <= len(TEXT) <= 1000:
        raise ValueError(f"entry must be 1-1000 chars, got {len(TEXT)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
