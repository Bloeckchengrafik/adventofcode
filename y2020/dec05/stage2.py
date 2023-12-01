from lib import *
from y2020.dec05.stage1 import parse_boarding_pass

@timed
def stage(data: list[str]):
    # Year 2020 / Day 05 / Stage 2
    passes = [parse_boarding_pass(boarding_pass) for boarding_pass in data]

    # Find the missing seat ID
    seat_ids = [row * 8 + col for row, col in passes]
    seat_ids.sort()
    for i in range(len(seat_ids) - 1):
        if seat_ids[i] + 1 != seat_ids[i + 1]:
            print(f"{GREEN_OK} Solution: {seat_ids[i] + 1}")
            break
