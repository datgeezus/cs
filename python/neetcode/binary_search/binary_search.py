"""
# Problem
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

# Solution
Implement binary search algorithm

"""


def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    ans = -1

    while l <= r:
        middle = (l + r) // 2
        if nums[middle] > target:
            r = middle - 1
        elif nums[middle] < target:
            l = middle + 1
        else:
            ans = middle
            break
    return ans


if __name__ == "__main__":
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
