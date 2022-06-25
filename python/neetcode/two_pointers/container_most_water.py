"""
# Problem
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

# Solution
Use 2 pointers

"""


def max_area(height: list[int]) -> int:
    ans = 0
    l = 0
    r = len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        ans = max(ans, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return ans


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
