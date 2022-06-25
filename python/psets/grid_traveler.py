"""
You are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the
bottom-right corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimentions m*n?
____________________________________________________________________________________________________

Ex:

grid_traveler(3, 3) -> 3

[s][ ][ ]
[ ][ ][ ]
[ ][ ][g]

1. right, right, right
2. right, down, right
3. down, right, right

gird_traveler(1, 1) -> 1
[s/g]

grid_traveler(0, 0) -> 0
grid_traveler(0, 1) -> 0
grid_traveler(1, 0) -> 0
no way to travel a no-grid

"""


def grid_traveler(m, n, memo=None):
    memo = {} if memo is None else memo
    # base cases
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    if (m, n) in memo:
        return memo[(m, n)]

    memo[(m, n)] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)

    return memo[(m, n)]


def grid_traveler_tab(m, n):
    # base cases
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    table = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                table[i][j] = 1
            else:
                table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table[m - 1][n - 1]


if __name__ == "__main__":
    print(grid_traveler(1, 1))  # 1
    print(grid_traveler(2, 3))  # 3
    print(grid_traveler(3, 2))  # 3
    print(grid_traveler(3, 3))  # 6
    print(grid_traveler(18, 18))  # 2333606220
    print(grid_traveler(300, 500))
    print(grid_traveler_tab(1, 1))  # 1
    print(grid_traveler_tab(2, 3))  # 3
    print(grid_traveler_tab(3, 2))  # 3
    print(grid_traveler_tab(3, 3))  # 6
    print(grid_traveler_tab(18, 18))  # 2333606220
    print(grid_traveler_tab(300, 500))
