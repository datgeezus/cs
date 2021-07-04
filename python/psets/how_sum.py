"""
Write a function how_sum(target, nums) that takes in a target sum and an array of numbers as arguments.

The funcion shoud return an array containing any combination of elements that add to exactly the
target sum. If there is no combination that adds up to the target sum, then return null.

If there are multiple combinations possible, you may return any single one
"""

# Complexity
#  time: O(n*m^2)
# space: O(m^2)
def how_sum(target, nums, memo=None):
    memo = {} if memo is None else memo
    # base cases
    if target < 0: return None
    if target == 0: return []
    if target in memo: return memo[target]

    for num in nums:
        remainder = target - num
        res = how_sum(remainder, nums, memo)
        if res is not None:
            memo[target] = res + [num]
            return memo[target]

    memo[target] = None
    return None

if __name__ == "__main__":
    print(how_sum(7, [2, 3])) # [3,2,2]
    print(how_sum(7, [5, 3, 4, 7])) # [4,3]
    print(how_sum(7, [2, 4])) # None
    print(how_sum(8, [2, 3, 5])) # [2,2,2,2]
    print(how_sum(300, [7, 14])) # None