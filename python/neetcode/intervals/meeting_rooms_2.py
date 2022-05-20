"""
# Problem
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

# Solution
create 2 sorted arrays, start and end
2 pointers will keep track of the start and end of the meetings
incrementing a counter each time there is an overlap, decrements when not
return the max number of rooms found over time

"""

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    # Sort by start
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])
    
    n_rooms = 0
    count = 0
    s = 0
    e = 0
    n_intervals = len(intervals)
    
    while s < n_intervals:
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        n_rooms = max(n_rooms, count)
    
    return n_rooms
    

if __name__ == "__main__":
    assert min_meeting_rooms([[0,30],[5,10],[15,20]]) == 2
    assert min_meeting_rooms([[2,7]]) == 1