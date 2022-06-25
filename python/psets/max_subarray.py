from typing import List

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""


def max_subarray_sum(nums: List[int]) -> int:
    ans = [0 for _ in nums]
    ans[0] = nums[0]
    for i in range(1, len(nums)):
        ans[i] = max(ans[i - 1] + nums[i], nums[i])
    return max(ans)


def max_subarray(nums: List[int]) -> List[int]:
    ans = [0 for _ in nums]
    ans[0] = nums[0]
    mapp = {}
    sum = 0
    si = 0
    for i in range(1, len(nums)):
        if ans[i - 1] + nums[i] > nums[i]:
            sum = ans[i - 1] + nums[i]
        else:
            sum = nums[i]
            si = i
        ans[i] = sum
        mapp[sum] = (si, i)
    best = max(ans)
    start, end = mapp[best]
    return nums[start : end + 1]


if __name__ == "__main__":
    print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
