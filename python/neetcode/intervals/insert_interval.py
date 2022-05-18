"""
# Problem
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""

def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    ans = []
    
    for i,interval in enumerate(intervals):
        if new_interval[1] < interval[0]:
            ans.append(new_interval)
            ans += intervals[i:]
            break
        elif new_interval[0] > interval[1]:
            ans.append(interval)
        else:
            new_interval = [min(new_interval[0], interval[0]), max(new_interval[1], interval[1])]
    else:
        ans.append(new_interval)

    return ans


if __name__ == "__main__":
    assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert insert([[3,5],[6,9]], [1,2]) == [[1,2],[3,5],[6,9]]