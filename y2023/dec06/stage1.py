from lib import *

@timed
def stage(data: list[str]):
    # Year 2023 / Day 06 / Stage 1
    time = [int(x) for x in data[0].split()[1:]]
    distance = [int(x) for x in data[1].split()[1:]]
    result = 1
    for t, d in zip(time, distance):
        left = t/2
        right = sqrt(t**2/4 - d)
        x1 = ceil(left - right+0.001)
        x2 = floor(left + right-0.001)
        inclusive_range = x2 - x1 + 1
        result *= inclusive_range


    print(f"{GREEN_OK} Result: {result}")
