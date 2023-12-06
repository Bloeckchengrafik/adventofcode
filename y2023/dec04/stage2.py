from lib import *
from dataclasses import dataclass
import re

@timed
def stage(input: list[str]):
    # Year 2023 / Day 04 / Stage 2
    data = [
        len(
            [
                1
                for _ in set(map(lambda x: int(x), left.split()))
                & set(map(lambda x: int(x), right.split()))
            ]
        )
        for line in input
        for left, right in [re.sub(r"Card +\d+: ", "", line).split(" | ")]
    ]

    result = [1] * len(data)
    generator = ((j, result[i]) for i, count in enumerate(data) if count > 0 for j in range(i + 1, i + 1 + count))
    for i, add in generator:
        result[i] += add

    part2 = sum(result)

    print(f"{GREEN_OK} terminated. {part2} cards in total.")