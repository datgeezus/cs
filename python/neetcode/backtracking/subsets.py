"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

def subsets(nums: list[int]) -> list[list[int]]:
    ans = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            ans.append(subset.copy())
            return

        # exclude
        dfs(i + 1)

        # include
        subset.append(nums[i])
        dfs(i + 1)
        subset.pop()

    dfs(0)
    return ans


if __name__ == "__main__":
    assert len(subsets([0])) == 2
    assert len(subsets([1,2,3])) == 8
    print(subsets([1,2,3]))
