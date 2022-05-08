# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def two_sum(numbers: list[int], target: int) -> list[int]:
    l = 0
    r = len(numbers) - 1

    while l < r:
        current_sum = numbers[l] + numbers[r]
        
        if current_sum > target:
            r -= 1
        elif current_sum < target:
            l += 1
        else:
            return [l,r]
    return []

if __name__ == "__main__":
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert two_sum([2,3,4], 6) == [0,2]
    assert two_sum([-1,0], -1) == [0,1]