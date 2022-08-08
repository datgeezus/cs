"""
# Problem
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police

# Soultion
DP: if i is the current house, we pick the max amount between
1 house back and the current + 2 houses back
"""


def rob(nums: list[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    dp = [0 for _ in nums]
    for house, money in enumerate(nums):
        if house == 0:
            dp[0] = money
        elif house == 1:
            dp[1] = max(dp[0], money)
        else:
            dp[house] = max(dp[house - 1], dp[house - 2] + money)
    return dp[-1]


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
