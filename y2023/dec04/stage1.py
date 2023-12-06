from lib import *
from dataclasses import dataclass

@dataclass
class ScratchCard:
    id: int
    winning: list[int]
    owned: list[int]

def parse_card(line: str) -> ScratchCard:
    left, right = line.split(":")
    id = int(left.split(" ")[-1])
    winning, own = [x.strip() for x in right.split("|")]
    winning = [int(x) for x in winning.split(" ") if x != ""]
    owned = [int(x) for x in own.split(" ") if x != ""]

    return ScratchCard(id, winning, owned)

@timed
def stage(data: list[str]):
    # Year 2023 / Day 04 / Stage 1
    cards = [parse_card(x) for x in data]

    cardsum = 0
    for card in cards:
        thiscard = 0
        for winning in card.winning:
            if winning in card.owned:
                if thiscard == 0:
                    thiscard = 1
                else:
                    thiscard *= 2

        cardsum += thiscard

    print(f"{GREEN_OK} Result: {cardsum}")