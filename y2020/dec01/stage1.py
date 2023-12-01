from lib import *

@timed
def stage(data: list[str]):
    # Year 2020 / Day 01 / Stage 1
    entries = []
    for line in data:
        for line2 in data:
            if int(line) + int(line2) == 2020:
                entries.append(int(line) * int(line2))
                break

    print(f"{GREEN_OK} Solution: {entries[0]}")