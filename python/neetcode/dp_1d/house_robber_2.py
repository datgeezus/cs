"""
# Problem
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

# Solution
DP: Similar to house robber 1, compute rob() twice, once for nums[0,n-1] and once for nums[1,n]
"""

def rob(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    def rob_helper(houses: list[int]) -> int:
        dp = [0 for _ in houses]
        for house,money in enumerate(houses):
            if house == 0:
                dp[house] = money
                continue
            if house == 1:
                dp[house] = max(dp[house-1], money)
                continue
            dp[house] = max(dp[house-1], dp[house-2] + money)
        return dp[-1]
    
    rob_a = rob_helper(nums[1:])
    rob_b = rob_helper(nums[:-1])
    return max(rob_a, rob_b)

if __name__ == "__main__":
    assert rob([2,3,2]) == 3
    assert rob([1,2,3,1]) == 4
    assert rob([1,2,3]) == 3
    assert rob([0]) == 0