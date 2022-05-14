"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Solution
Backtracking

"""

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    ans = []
    n_candidates = len(candidates)
    
    def dfs(i: int, current: list[int], total: int) -> None:
        if total == target:
            ans.append(current.copy())
            return
        if i >= n_candidates or total > target:
            return
        
        current.append(candidates[i])
        dfs(i, current, total + candidates[i])
        current.pop()
        dfs(i + 1, current, total)
        
    dfs(0, [], 0)
    return ans


if __name__ == "__main__":
    assert combination_sum([2,3,6,7], 7) == [[2,2,3], [7]]
    assert combination_sum([2,3,5], 8) == [[2,2,2,2], [2,3,3], [3,5]]
    assert combination_sum([2], 1) == []
    