from typing import Any
from lib import *

class Segment:
    def __init__(self, data: str):
        split = data.split(" ")
        self.length = int(split[2])
        self.start = int(split[1])
        self.end = self.start + self.length - 1
        self.mapping_start = int(split[0])
        self.mapping_end = self.mapping_start + self.length - 1

    def __repr__(self):
        return f"Segment(start={self.start}, end={self.end}, mstart={self.mapping_start}, mend={self.mapping_end}, len={self.length})"
    
    def __contains__(self, item):
        return self.start <= item <= self.end
    
    def calculate(self, name: int) -> int:
        return self.mapping_start + (name - self.start)
    
@dataclass
class Block:
    from_name: str
    to_name: str
    segments: list[Segment]

    def __repr__(self):
        return f"Block({self.from_name}, {self.to_name}, {self.segments})"
    
    def __getitem__(self, name: int) -> int:
        for segment in self.segments:
            if name in segment:
                return segment.calculate(name)

        return name

def parse_blocks(data: list[str]) -> list[Block]:
    blocks: list[Block] = []
    block_data: list[Segment] = []
    block_from = ""
    block_to = ""
    for line in data[2:]:
        if line == "":
            blocks.append(Block(block_from, block_to, block_data))
            block_data = []
            continue
        if "map" in line:
            block_from, _, block_to = line.split(" ")[0].split("-")
            continue
        block_data.append(Segment(line))

    if len(block_data) > 0:
        blocks.append(Block(block_from, block_to, block_data))

    return blocks

@timed
def stage(data: list[str]):
    # Year 2023 / Day 05 / Stage 1
    seeds = [int(x) for x in data[0].split(":")[1].strip().split()]
    blocks = parse_blocks(data)

    for block in blocks:
        seeds = [block[x] for x in seeds]

    print(f"{GREEN_OK} Min:", min(seeds))