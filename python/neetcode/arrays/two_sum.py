# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(nums: list[int], target: int) -> list[int]:
    mem = {}
    
    for i,n in enumerate(nums):
        diff = target - n
        if diff in mem:
            return [mem[diff], i]
        mem[n] = i
    
    return []

if __name__ == "__main__":
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert two_sum([3,2,4], 6) == [1,2]
    assert two_sum([3,3], 6) == [0,1]
