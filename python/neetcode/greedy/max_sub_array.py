"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has
the largest sum and return its sum.
A subarray is a contiguous part of an array.
"""

def max_sub_array(nums: list[int]) -> int:
    mem = [0 for _ in nums]
    for i,n in enumerate(nums):
        if i == 0:
            mem[0] = n
            continue
        mem[i] = max(n, n + mem[i-1])
    return max(mem)

if __name__ == "__main__":
    assert max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5,4,-1,7,8]) == 23