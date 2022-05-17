"""
# Problem
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take
course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers,
return any of them. If it is impossible to finish all courses, return an empty array.

# Solution
Topological sort, if cycle detected, return empty

"""

from collections import defaultdict


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    pre = defaultdict(list)
    for course, prerequisite in prerequisites:
        pre[course].append(prerequisite)

    # possible stats of a couse: visited, visiting, unvisited
    visited = set()
    visiting = set()
    ans = []

    def dfs(course: int) -> bool:
        if course in visiting:
            return False
        if course in visited:
            return True

        visiting.add(course)
        for prerequisite in pre[course]:
            if not dfs(prerequisite):
                return False
        visiting.remove(course)
        visited.add(course)
        ans.append(course)
        return True

    for course in range(num_courses):
        if not dfs(course):
            return []
    return ans


if __name__ == "__main__":
    assert find_order(2, [[1, 0]]) == [0, 1]
    assert find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    assert find_order(1, []) == [0]
