"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.
"""

from heapq import heapify, heappop, heappush


def last_stone_weight(stones: list[int]) -> int:
    # Use a min heap with negative values to represent a max heap
    stones = [-s for s in stones]
    heapify(stones)
    
    while len(stones) > 1:
        first = heappop(stones)
        second = heappop(stones)
        if second > first:
            diff = first - second
            heappush(stones, diff)
    
    return abs(stones[0])


if __name__ == "__main__":
    assert last_stone_weight([2,7,4,1,8,1]) == 1
    assert last_stone_weight([1]) == 1