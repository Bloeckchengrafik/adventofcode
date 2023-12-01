from lib import *

@timed
def stage(data: list[str]):
    # Year 2020 / Day 06 / Stage 2
    # Groups are separated by double newlines
    groups = [group.split("\n") for group in "\n".join(data).split("\n\n")]
    # For each group, get the intersection of all sets
    nums = [len(set.intersection(*map(set, group))) for group in groups]
    print(f"{GREEN_OK} Solution: {sum(nums)}")
