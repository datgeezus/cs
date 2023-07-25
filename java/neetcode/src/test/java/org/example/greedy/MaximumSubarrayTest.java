package org.example.greedy;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class MaximumSubarrayTest {

    @Test
    public void test1() {
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int out = 6;

        int ans = MaximumSubarray.maxSubArray(nums);
        assertEquals(out, ans);
    }

    @Test
    public void test2() {
        int[] nums = {1};
        int out = 1;

        int ans = MaximumSubarray.maxSubArray(nums);
        assertEquals(out, ans);
    }

    @Test
    public void test3() {
        int[] nums = {5, 4, -1, 7, 8};
        int out = 23;

        int ans = MaximumSubarray.maxSubArray(nums);
        assertEquals(out, ans);
    }
}
