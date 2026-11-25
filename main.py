import os

ENTRY = (
    "v2.7.1: fixed a bug where the brain wakes you at 3AM "
    "solely to replay an embarrassing moment from 2009."
)

assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
assert len(ENTRY) <= 160, f"entry too long: {len(ENTRY)}"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(ENTRY + "\n")
