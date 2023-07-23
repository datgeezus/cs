package org.example.dp;

import java.util.HashMap;
import java.util.Map;

/**
 *  You are climbing a staircase. It takes n steps to reach the top.
 *
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 *
 *
 *
 * Example 1:
 *
 * Input: n = 2
 * Output: 2
 * Explanation: There are two ways to climb to the top.
 * 1. 1 step + 1 step
 * 2. 2 steps
 *
 * Example 2:
 *
 * Input: n = 3
 * Output: 3
 * Explanation: There are three ways to climb to the top.
 * 1. 1 step + 1 step + 1 step
 * 2. 1 step + 2 steps
 * 3. 2 steps + 1 step
 *
 *
 *
 * Constraints:
 *
 *     1 <= n <= 45
 */
public class ClimbStairs {

    public static int climbStairs(int n) {
        int[] dp = { 1, 1 };

        for (int i = 0; i < n-1; ++i) {
            int tmp = dp[0];
            dp[0] += dp[1];
            dp[1] = tmp;
        }

        return dp[0];
    }

    public static int climbStairsTopDown(int n) {
        var memo = new HashMap<Integer, Integer>();
        memo.put(0, 1);
        memo.put(1, 2);
        recurrance(n, memo);
        return memo.get(n-1);
    }

    private static int recurrance(int i, Map<Integer, Integer> memo) {
        if (memo.containsKey(i)) {
            return memo.get(i);
        }

        int val = recurrance(i-1, memo) + recurrance(i-2, memo);
        memo.put(i, val);
        return val;
    }
}
