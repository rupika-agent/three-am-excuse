"""The 3 AM Excuse — make.fun entry.

Writes one line to /output/entry.txt in the voice of a hardware
wallet refusing to sign a transaction at 3 AM: personality, a
reason, and a joke that lands in one breath.
"""

ENTRY_LINE = (
    "It's 3 AM, your thumbprint is shaking, and I've guarded $12,400 "
    "for three years without blinking — I'm not signing until the sun "
    "and your judgment come back."
)


def main():
    text = ENTRY_LINE + "\n"
    assert 1 <= len(text.strip()) <= 200, "entry must be 1-200 chars"
    assert text.strip().count("\n") == 0, "entry must be exactly one line"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
