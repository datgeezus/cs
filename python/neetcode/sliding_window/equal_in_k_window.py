"""
# Problem
Given an array, return true if there are two elements withing a window of size k that are equal

# Brute force
Compute all combinations of size k, return true if 2 repeated
## Complexity
- Time: n * k

# Sliding window
Traverse the array, use a rolling set to compute if a value is already in it
Removing traversing the k elements in the window
## Complexity
- Time: n

"""

def brute(nums: list[int], k: int) -> bool:
    n_nums = len(nums)
    for L, n in enumerate(nums):
        start = L + 1
        end = min(n_nums, L+k)
        for r in nums[start:end]:
            if n == r:
                return True
    return False


def are_elems_equal(nums: list[int], k: int) -> bool:
    if k < 2:
        return False
    n_nums = len(nums)

    window = set()
    L = 0
    for R in range(n_nums):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False



if __name__ == "__main__":
    assert brute([1, 2, 3, 2, 3, 3], 2)
    assert not brute([1, 2, 3, 2, 3, 3], 1)
    assert are_elems_equal([1, 2, 3, 2, 3, 3], 2)
    assert not are_elems_equal([1, 2, 3, 2, 3, 3], 1)