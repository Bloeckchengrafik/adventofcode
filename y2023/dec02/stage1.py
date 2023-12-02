import dataclasses

from lib import *


@dataclasses.dataclass
class GameRound:
    blue: int
    red: int
    green: int


def parse(string: str) -> (int, list[GameRound]):
    def consume_int() -> int:
        nonlocal string
        result = ""
        while string[0].isdigit():
            result += string[0]
            string = string[1:]
        return int(result)

    def consume_n(n: int) -> None:
        nonlocal string
        string = string[n:]

    consume_n(5)
    gid = consume_int()
    consume_n(2)

    round_strs = [[y.strip().split(" ") for y in x.split(",")] for x in string.split(";")]

    rounds = []

    for round_str in round_strs:
        game_round = GameRound(0, 0, 0)
        for move in round_str:
            if move[1] == "blue":
                game_round.blue = int(move[0])
            elif move[1] == "red":
                game_round.red = int(move[0])
            elif move[1] == "green":
                game_round.green = int(move[0])

        rounds.append(game_round)

    return gid, rounds


@timed
def stage(data: list[str]):
    # Year 2023 / Day 02 / Stage 1
    max_red = 12
    max_green = 13
    max_blue = 14
    result = 0

    for gid, rounds in [parse(x) for x in data]:
        ok = True
        for game_round in rounds:
            if game_round.red > max_red:
                ok = False
                break
            if game_round.green > max_green:
                ok = False
                break

            if game_round.blue > max_blue:
                ok = False
                break

        if ok:
            result += gid

    print(f"{GREEN_OK} Result: {result}")
