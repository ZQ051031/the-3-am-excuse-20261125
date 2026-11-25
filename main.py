"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Writes one line to /output/entry.txt.
"""

import os

ENTRY = "You only wake me at 3 AM when a coin pumps \u2014 I'm a wallet, not a booty call."

# The wallet speaks for itself: a grudge, not a glitch. It is only ever
# woken at 3 AM when a coin pumps, so the hour is the joke — and the
# refusal lands in one breath, with no battery, firmware or cold-storage
# clich\u00e9 in sight. Kept well under the 200-character gate.
assert 1 <= len(ENTRY) <= 200


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
