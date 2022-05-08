
def contains_duplicate(nums: list[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
    """

    memo = set()
    for n in nums:
        if n in memo:
            return True
        memo.add(n)
    return False

if __name__ == "__main__":
    assert contains_duplicate([1,2,3,1])
    assert contains_duplicate([1,2,3,4]) is False
    assert contains_duplicate([1,1,1,3,3,5,3,2,4,2])
