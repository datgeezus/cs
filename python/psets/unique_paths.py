"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

[0] [1] [1]

[1] [2] [3]


"""


def unique_paths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    grid = m * [[-1] * n]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                grid[0][0] = 0
            if i == 0 or j == 0:
                grid[i][j] = 1
            else:
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[m - 1][n - 1]


if __name__ == "__main__":
    print(unique_paths(3, 2))
    print(unique_paths(5, 5))
    print(unique_paths(3, 5))
    print(unique_paths(300, 500))
