"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""

from collections import deque

LAND = "1"

def num_islands(grid: list[list[str]]) -> int:

    visited = set()
    n_rows = len(grid)
    n_cols = len(grid[0])
    n_islands = 0
    
    def in_bounds(row: int, col: int):
        return row >= 0 and row < n_rows \
            and col >= 0 and col < n_cols \
            and grid[row][col] == LAND \
            and (row, col) not in visited

    def bfs(row: int, col: int):
        q = deque([(row, col)])
        visited.add((row, col))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            curr_row, curr_col = q.popleft()
            for dr, dc in directions:
                new_cell = (curr_row + dr, curr_col + dc)
                if in_bounds(new_cell[0], new_cell[1]):
                    q.append(new_cell)
                    visited.add(new_cell)
                    
    for r,cols in enumerate(grid):
        for c,_ in enumerate(cols):
            if grid[r][c] == LAND and (r,c) not in visited:
                bfs(r,c)
                n_islands += 1
                
    return n_islands

            

if __name__ == "__main__":
    graph = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert num_islands(graph) == 3
