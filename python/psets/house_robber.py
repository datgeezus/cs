"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]
    if n < 3: return max(nums[0], nums[1])
    ans = [0 for _ in nums]
    ans[0] = nums[0]
    ans[1] = max(nums[0], nums[1])

    for i in range(2,n):
        ans[i] = max(nums[i]+ans[i-2], ans[i-1])
    return max(ans)

if __name__ == "__main__":
    print(rob([1,2,3,1]))  # Expected 4
    print(rob([2,7,9,3,1]))# Expected 12