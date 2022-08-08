"""
# Problem
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Solution

"""


def climb_stairs(n: int) -> int:
    dp = [0 for _ in range(n)]
    for i, n in enumerate(range(n)):
        if i == 0 or i == 1:
            dp[i] = i + 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


if __name__ == "__main__":
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
