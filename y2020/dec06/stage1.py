from lib import *

@timed
def stage(data: list[str]):
    # Year 2020 / Day 06 / Stage 1
    # Drop all single newlines, then split on double newlines
    groups = [group.split("\n") for group in "\n".join(data).split("\n\n")]
    nums = [len(set("".join(group))) for group in groups]
    print(f"{GREEN_OK} Solution: {sum(nums)}")
