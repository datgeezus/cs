"""
# Problem
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.


# Solution
Bruteforce:
for every element in list:

[0,1]

i = 0
0 == 1 ? => false

    [0]

    i = 1
    1 == 1 ? => True
    ans = [[0,1]]


    [0]





"""


def permute(nums: list[int]) -> list[list[int]]:
    ans = []
    n_nums = len(nums)
    permutation = []
    used = set()

    def backtrack() -> None:
        if len(permutation) == n_nums:
            ans.append(permutation[:])
            return

        for val in nums:
            if val not in used:
                used.add(val)
                permutation.append(val)
                backtrack()
                permutation.pop()
                used.remove(val)

    backtrack()
    return ans


if __name__ == "__main__":
    print(permute([1,2,3]))
    assert permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert permute([0,1]) == [[0,1],[1,0]]
    assert permute([1]) == [[1]]
