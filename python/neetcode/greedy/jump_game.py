"""
# Problem

You are given an integer array nums.
You are initially positioned at the array's first index, and each element in the array represents
your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

# Solution

## Brutforce
Compute all possible jumps

## Greedy
Traverse the array in reverse, set the goal at the end
if i + nums[i] >= goal:
    goal = i

return true if goal is 0


set goal at index 4
[2,3,1,1,4]
         g
the value to the left of g can jump to g

[2,3,1,1,4]
       g
new goal is at index 3

"""

def can_jump(nums: list[int]) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums) -1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0


if __name__ == "__main__":
    assert can_jump([2,3,1,1,4])
    assert can_jump([3,2,1,0,4]) is False