package org.example.twopointers;

import java.util.*;

/**
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
 * such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 *
 * Notice that the solution set must not contain duplicate triplets.
 *
 *
 *
 * Example 1:
 *
 * Input: nums = [-1,0,1,2,-1,-4]
 * Output: [[-1,-1,2],[-1,0,1]]
 * Explanation:
 * nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
 * nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
 * nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
 * The distinct triplets are [-1,0,1] and [-1,-1,2].
 * Notice that the order of the output and the order of the triplets does not matter.
 *
 * Example 2:
 *
 * Input: nums = [0,1,1]
 * Output: []
 * Explanation: The only possible triplet does not sum up to 0.
 *
 * Example 3:
 *
 * Input: nums = [0,0,0]
 * Output: [[0,0,0]]
 * Explanation: The only possible triplet sums up to 0.
 *
 *
 *
 * Constraints:
 *
 *     3 <= nums.length <= 3000
 *     -105 <= nums[i] <= 105
 */
public class ThreeSum {

    public static List<List<Integer>> threeSum(int[] nums) {
        var target = 0;
        Arrays.sort(nums);
        var len = nums.length;
        List<List<Integer>> ans = new ArrayList<>();

        for (int i = 0; i < len; ++i) {
            var now = nums[i];
            if ((i > 0) && (nums[i] == nums[i-1])) {
                continue;
            }

            var l = i + 1;
            var r = len - 1;
            while (l < r) {
                var left = nums[l];
                var right = nums[r];
                var sum = now + left + right;

                if (sum > target) {
                    r -= 1;
                } else if(sum < target){
                    l += 1;
                } else {
                    ans.add(List.of(now, nums[l], nums[r]));
                    l += 1;
                    while (nums[l] == nums[l-1] && l < r) {
                        l += 1;
                    }
                }
            }

        }

        return ans;

    }
}
