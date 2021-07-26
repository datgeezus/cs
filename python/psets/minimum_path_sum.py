"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

import sys
from typing import List

def num_path_sum(grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    memo = [[sys.maxsize for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
    memo[ROWS-1][COLS] = 0


    for r in range(ROWS - 1, -1, -1):
        for c in range(COLS - 1, -1, -1):
            memo[r][c] = grid[r][c] + min(memo[r+1][c], memo[r][c+1])
    return memo[0][0]

if __name__ == "__main__":
    print(num_path_sum([[1,3,1],[1,5,1],[4,2,1]])) # 7