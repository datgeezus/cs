"""
# Problem
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take
course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also
have finished course 1. So it is impossible.


# Solution
Build an adjacency list, find cycles
"""

from collections import defaultdict


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    pre = defaultdict(list)
    for course, prerequisite in prerequisites:
        pre[course].append(prerequisite)

    print(pre)
    visited = set()

    def dfs(course: int) -> bool:
        if course in visited:
            return False
        if pre[course] == []:
            return True

        visited.add(course)
        print(f"curr:{course}")
        for prerequisite in pre[course]:
            if not dfs(prerequisite):
                return False
        # Finished visiting nodes, remove from mem for next one
        visited.remove(course)
        pre[course] = []
        return True

    for course in range(num_courses):
        if not dfs(course):
            return False
    return True

if __name__ == "__main__":
    assert can_finish(2, [[1, 0]])
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(5, [[1, 4], [2, 4], [3, 1], [3, 2]])
