"""
Given an integer array nums, find the number of ways to split the array into two parts
so that the first section has a sum greater than or equal to the sum of the second section.
The second section should have at least one number.
"""

def ways_to_split(nums: list[int]) -> int:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = 0
    for i in range(len(nums)-1):
        left = prefix[i]
        right = prefix[-1] - prefix[i]
        if left >= right:
            ans += 1

    return ans


if __name__ == "__main__":
    assert ways_to_split([10,4,-8,7]) == 2

