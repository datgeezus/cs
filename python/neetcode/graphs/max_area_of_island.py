"""
# Problem
You are given an m x n binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

# Solution
DFS

"""

def max_area_of_island(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    land = 1
    visit = set()
    moves = [(0,1), (1,0), (0,-1), (-1,0)]

    def is_valid(r: int, c: int) -> bool:
        return (r >= 0 and r < rows \
            and c >= 0 and c < cols \
            and (r,c) not in visit \
            and grid[r][c] == land)
    
    def dfs(r: int, c: int) -> int:
        if not is_valid(r,c):
            return 0
        
        visit.add((r,c))
        ans = 0
        for move in moves:
            dr = move[0]
            dc = move[1]
            ans += dfs(r + dr, c + dc)
        
        return 1 + ans
    
    area = 0
    for r in range(rows):
        for c in range(cols):
            area = max(area, dfs(r,c))
    return area


if __name__ == "__main__":
    grid1 = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0], 
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    assert max_area_of_island(grid1) == 6
    
    grid2 = [[0,0,0,0,0,0,0,0]]
    assert max_area_of_island(grid2) == 0

    