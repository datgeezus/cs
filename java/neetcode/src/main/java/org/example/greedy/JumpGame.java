package org.example.greedy;

public class JumpGame {

    public static boolean canJump(int[] nums) {
        int nNums = nums.length;
        int last = nNums - 1;
        int goal = nums[last];

        for (int i = last; i >= 0; --i) {
            if (i + nums[i] >= goal) {
                goal = i;
            }
        }

        return goal == 0;
    }
}
