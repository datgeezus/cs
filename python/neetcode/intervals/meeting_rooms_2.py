"""
# Problem
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

# Solution
Sort intervals by start time
Iterate over the intervals, if an overlap is found, increment n_rooms

"""

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    # Sort by start
    intervals.sort(key=lambda i: i[0])
    
    n_meetings = len(intervals)
    if n_meetings == 1:
        return 1
    n_rooms = 1
    prev_end = intervals[0][1]
    for start,end in intervals[1:]:
        if prev_end > start:
            n_rooms += 1
            prev_end = end
    return n_rooms

if __name__ == "__main__":
    assert min_meeting_rooms([[0,30],[5,10],[15,20]]) == 2
    assert min_meeting_rooms([[2,7]]) == 1