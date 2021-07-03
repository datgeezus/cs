"""
Write the function can_sum(target, numbers) that takes in a target sum and an array of numbers as
arguments. The function should return a boolean indicating wheter or not it is possible to
generate the target sum using numbers from the array.

You may use an elelement of the array as many times as needed.
You may assume that all input numbers are nonnegative
"""

def can_sum(target, nums, memo=None):
    memo = {} if memo is None else memo
    # base cases
    if target in memo: return memo[target]
    if target < 0: return False
    if target == 0: return True

    for num in nums:
        remainder = target - num
        if can_sum(remainder, nums, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False

if __name__ == "__main__":
    print(can_sum(7, [2, 3])) # true
    print(can_sum(7, [5, 3, 4, 7])) # true
    print(can_sum(7, [2, 4])) # false
    print(can_sum(8, [2, 3, 5])) # true
    print(can_sum(300, [7, 14])) # false