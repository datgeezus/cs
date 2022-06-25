"""
# Problem
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells.
You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly
north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that
rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Solution
Traverse DFS from edges, keep track of visited cells (from paciffic and atlantic) 
and return the intersection of both visited sets

"""


def water_flow(heights: list[list[int]]) -> list[list[int]]:
    N_ROWS = len(heights)
    N_COLS = len(heights[0])
    MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pac = set()
    atl = set()

    def is_valid(r: int, c: int, visited: set[int], prev_h: int) -> bool:
        return (
            (r, c) not in visited
            and r >= 0
            and r < N_ROWS
            and c >= 0
            and c < N_COLS
            and prev_h <= heights[r][c]
        )

    def dfs(r: int, c: int, visited: set[int], prev_h: int) -> None:
        if not is_valid(r, c, visited, prev_h):
            return

        visited.add((r, c))
        height = heights[r][c]
        for dr, dc in MOVES:
            new_r = dr + r
            new_c = dc + c
            dfs(new_r, new_c, visited, height)

    for c in range(N_COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(N_ROWS - 1, c, atl, heights[N_ROWS - 1][c])

    for r in range(N_ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, N_COLS - 1, atl, heights[r][N_COLS - 1])

    ans = []
    for r in range(N_ROWS):
        for c in range(N_COLS):
            if (r, c) in pac and (r, c) in atl:
                ans.append([r, c])
    return ans


if __name__ == "__main__":
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    flow = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert water_flow(heights) == flow

    heights = [[2, 1], [1, 2]]
    flow = [[0, 0], [0, 1], [1, 0], [1, 1]]
    assert water_flow(heights) == flow
