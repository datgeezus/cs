"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import List


def word_search(board: List[List[str]], word: str) -> bool:
    ROWS = len(board)
    COLS = len(board[0])
    path = set()

    def in_bounds(r, c):
        return r < ROWS and c < COLS and c >= 0 and r >= 0

    def dfs(r, c, i):
        if i == len(word):
            return True
        if not in_bounds(r, c) or word[i] != board[r][c] or (r, c) in path:
            return False

        path.add((r, c))
        ans = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )
        path.remove((r, c))
        return ans

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True

    return False


if __name__ == "__main__":
    print(
        word_search(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
    )
