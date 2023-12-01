from lib import *
from y2020.dec03.trees import TreeGrid

@timed
def stage(data: list[str]):
    # Year 2020 / Day 03 / Stage 1
    grid = TreeGrid(data)

    slope = (3, 1)
    trees = grid.solve_slope(slope)
    
    print(f"{GREEN_OK} Solution: {trees}")
