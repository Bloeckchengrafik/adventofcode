from lib import *
from y2020.dec03.trees import TreeGrid

@timed
def stage(data: list[str]):
    # Year 2020 / Day 03 / Stage 2
    grid = TreeGrid(data)

    trees = 1
    trees *= grid.solve_slope((1, 1))
    trees *= grid.solve_slope((3, 1))
    trees *= grid.solve_slope((5, 1))
    trees *= grid.solve_slope((7, 1))
    trees *= grid.solve_slope((1, 2))
    
    print(f"{GREEN_OK} Solution: {trees}")
