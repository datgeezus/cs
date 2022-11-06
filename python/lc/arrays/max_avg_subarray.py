"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

# Solution

## Brute force
Compute all possible subarrays

## Sliding window

"""

def max_subarray_avg(nums: list[int], k: int) -> float:
    left = k-1
    curr = sum(nums[:k])
    ans = curr / k

    for i,n in enumerate(nums[k::], k):
        curr -= nums[i-k]
        curr += n
        maybe = curr / k
        ans = max(ans, maybe)

    return ans


if __name__ == "__main__":
    assert max_subarray_avg([1,12,-5,-6,50,3], 4) == 12.75
    assert max_subarray_avg([5], 1) == 5.0

