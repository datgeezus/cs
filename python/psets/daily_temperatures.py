"""
Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

from typing import List
from collections import deque


def daily_temperatures(temperatures: List[int]) -> List[int]:
    ans = [0 for _ in range(len(temperatures))]
    stack = deque()
    stack.append((temperatures[0], 0))
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:  # peek top most temp
            curr = stack.pop()  # (temp, idx)
            ans[curr[1]] = i - curr[1]
        stack.append((t, i))
    return ans


if __name__ == "__main__":
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
    print(daily_temperatures([30, 40, 50, 60]))  # [1,1,1,0]
    print(daily_temperatures([30, 60, 90]))  # [1,1,0]
