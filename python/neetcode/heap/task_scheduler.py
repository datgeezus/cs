"""
# Problem
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter
represents a different task. Tasks could be done in any order. Each task is done in one unit of time.
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

# Solution
Process the most frequent tasks first

Group the tasks by their frequency:
{
    "A": 6,
    "B": 1,
    "C": 1,
    "D": 1,
    "E": 1,
    "F": 1,
}

Keep a max heap of the frequencies
[6,1,1,1,1,1]

"""

from collections import deque
import heapq
from typing import Counter


def least_interval(tasks: list[str], n: int) -> int:
    count = Counter(tasks)
    # Python's heapq is a min heap, to make it a max heap, use negative numbers
    max_heap = [-c for c in count.values()]
    heapq.heapify(max_heap)
    time = 0
    q = deque()
    while max_heap or q:
        time += 1
        if max_heap:
            cnt = 1 + heapq.heappop(max_heap)
            if cnt:
                q.append((cnt, time+n))
        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])
    return time

if __name__ == "__main__":
    assert least_interval(["A","A","A","B","B","B"], 2) == 8
    assert least_interval(["A","A","A","B","B","B"], 0) == 6
    assert least_interval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) == 16