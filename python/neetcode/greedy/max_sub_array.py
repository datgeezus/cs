"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has
the largest sum and return its sum.
A subarray is a contiguous part of an array.


# Brute force:
Compute all possible subarrays, return the one with the largest sum
## Complexity:
- Time: n^2
- Memory: n

# Memoization

## Complexity:
- Time: n^2
- Memory: n

# Kadane's
## Complexity:
- Time: n
- Memory: 1

"""


def max_sub_array(nums: list[int]) -> int:
    n_nums = len(nums)
    if n_nums < 0:
        return 0
    if n_nums == 1:
        return nums[0]

    mem = [0 for _ in nums]
    mem[0] = nums[0]
    for i, n in enumerate(nums[1::], start=1):
        mem[i] = max(n, n + mem[i - 1])
    return max(mem)

def max_sub_array_2(nums: list[int]) -> int:
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        cur_sum = max(cur_sum, 0)
        cur_sum += n
        max_sum = max(max_sum, cur_sum)

    return max_sum


if __name__ == "__main__":
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
    assert max_sub_array([-4, -1, -2, -7, -3, -4]) == -1

    # Algo 2
    assert max_sub_array_2([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array_2([1]) == 1
    assert max_sub_array_2([5, 4, -1, 7, 8]) == 23
    assert max_sub_array_2([-4, -1, -2, -7, -3, -4]) == -1
