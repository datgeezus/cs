"""
 time: O(m^2 * n)
space: O(m^2)
"""


def best_sum(target: int, nums: list, memo: dict = None) -> list[int]:
    memo = {} if memo is None else memo
    if target == 0:
        return []
    if target < 0:
        return None
    if target in memo:
        return memo[target]

    shortest = None
    for num in nums:
        rem = target - num
        ans = best_sum(rem, nums, memo)
        if ans is not None:
            comb = ans + [num]
            if shortest is None or len(comb) < len(shortest):
                shortest = comb

    memo[target] = shortest
    return shortest


if __name__ == "__main__":
    print(best_sum(7, [5, 3, 4, 7]))  # [7]
    print(best_sum(8, [2, 3, 5]))  # [3, 5]
    print(best_sum(8, [1, 4, 5]))  # [4, 4]
    print(best_sum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
