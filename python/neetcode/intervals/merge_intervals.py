"""
# Problem
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Solution
Sort intervals by start value
Merge current with previous (starting from interval[1])

"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    # sort by start of the intervals
    intervals.sort(key=lambda i: i[0])
    ans = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = ans[-1][1]
        if start <= last_end:  # overlap
            ans[-1][1] = max(last_end, end)
        else:
            ans.append([start, end])
    return ans


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
