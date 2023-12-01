class TreeGrid:
    def __init__(self, grid: list[str]) -> None:
        self.grid = grid

    def __getitem__(self, key: tuple[int, int]) -> str:
        col, row = key
        return self.grid[row][col % len(self.grid[row])]
    
    def __len__(self) -> int:
        return len(self.grid)
    
    def solve_slope(self, slope):
        pos = (0, 0)
        trees = 0
        while pos[1] < len(self):
            if self[pos] == "#":
                trees += 1
            pos = (pos[0] + slope[0], pos[1] + slope[1])
        return trees
