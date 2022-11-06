"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation:  [1,1,1,0,0,1,1,1,1,1,1]
                         *         *
                         ~~~~~~~~~~~
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation:  [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
                       *         *
                   ~~~~~~~~~~~~~~~~~~~
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Solution

## Brute Force

## Sliding Window


"""

def longest_ones(nums: list[int], k: int) -> int:
    left = 0
    ans = 0
    n_zeroes = 0

    for right,n in enumerate(nums):
        if n == 0:
            n_zeroes += 1
        while n_zeroes > k:
            if nums[left] == 0:
                n_zeroes -= 1
            left += 1
        window_lenght = right - left + 1
        ans = max(ans, window_lenght)

    return ans


if __name__ == "__main__":
    assert longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    assert longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
