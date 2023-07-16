package org.example.arrays;

import java.util.Arrays;

/*
Given an integer array nums, return an array answer such that answer[i] is equal to the
product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Solution

Input = [1,2,3,4]

Build prefix and postfix arrays:

prefix[i] = nums[-i] * nums[i]

prefix[0] = nums[-1] = 1 * nums[0] = 1 => 1
prefix[1] = nums[0] = 1 * nums[1] = 2  => 2
prefix[2] = nums[1] = 2 * nums[2] = 3  => 6
prefix[3] = nums[2] = 3 * nums[3] = 4  => 12

prefix = [1, 2, 6, 24]


postfix[i] = nums[-i] * nums[i]

postfix[3] = nums[4] = 1 * nums[3] = 4 => 4
postfix[2] = nums[3] = 4 * nums[2] = 3 => 12
postfix[1] = nums[2] = 3 * nums[1] = 2 => 12
postfix[0] = nums[1] = 2 * nums[0] = 1 => 4

postfix = [24, 24, 12,4]

take prefix of values before and postfix of values after

ans[i]: prefix[i-1] * prefix[i]

ans[0]: prefix[-1] = 1 * postfix[1] = 24 => 24
ans[1]: prefix[0] = 1 * postfix[2] = 12  => 12
ans[2]: prefix[1] = 2 * postfix[3] = 4   => 8
ans[3]: prefix[2] = 6 * postfix[4] = 1   => 6

ans = [24, 12, 8, 6]
 */
public class ProductOfArray {
    public static Integer[] productOfArray(Integer[] nums) {
        var size = nums.length;
        // Build the answer array, filled with 1s
        Integer[] ans = Arrays.stream(new Integer[size]).map(ignore -> 1).toArray(Integer[]::new);

        var prev = 1;
        for (int index = 0; index < size; ++index) {
            var curr = nums[index];
            ans[index] = prev;
            prev *= curr;
        }

        prev = 1;
        for (int index = size-1; index >= 0; --index) {
            var curr = nums[index];
            var newValue = ans[index] * prev;
            ans[index] = newValue;
            prev *= curr;
        }

        return ans;
    }
}
