"""
Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
return a boolean array that represents the answer to each query.
A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example,
given nums = [1, 6, 3, 2, 7, 2] and queries = [[0, 3], [2, 5], [2, 4]] and limit = 13,
the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
"""


def answer_queries(nums: list[int], queries: list[tuple[int, int]], limit: int) -> list[bool]:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = []
    for x,y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans


if __name__ == "__main__":
    assert answer_queries([1, 6, 3, 2, 7, 2], [(0, 3), (2, 5), (2, 4)], 13) == [True, False, True]
