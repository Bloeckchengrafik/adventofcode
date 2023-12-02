from lib import *
from y2023.dec02.stage1 import parse


@timed
def stage(data: list[str]):
    # Year 2023 / Day 02 / Stage 2
    result = 0

    for gid, rounds in [parse(x) for x in data]:
        max_red = 0
        max_green = 0
        max_blue = 0
        for game_round in rounds:
            if game_round.red > max_red:
                max_red = game_round.red
            if game_round.green > max_green:
                max_green = game_round.green
            if game_round.blue > max_blue:
                max_blue = game_round.blue

        set_power = max_red * max_green * max_blue
        result += set_power

    print(f"{GREEN_OK} Result: {result}")
