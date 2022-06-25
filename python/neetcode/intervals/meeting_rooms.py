"""
# Problem
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# Solution
Sort the intervals by start
compare last end > curr start

"""

from dataclasses import dataclass


def can_attend(intervals: list[list[int]]) -> bool:
    # Sort by start time
    intervals.sort(key=lambda i: i[0])

    prev_end = intervals[0][1]
    for start, _ in intervals[1:]:
        if prev_end > start:
            return False
    return True


if __name__ == "__main__":
    assert can_attend([[1, 30], [5, 10], [15, 20]]) is False
    assert can_attend([[5, 8], [9, 15]])
