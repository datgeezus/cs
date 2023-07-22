package org.example.twopointers;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class TwoSumTest {

    @Test
    public void test1() {
        int[] in = {2, 7, 11, 15};
        var target = 9;
        int[] out = {1, 2};

        var ans = TwoSum.twoSum(in, target);
        assertArrayEquals(out, ans);
    }

    @Test
    public void test2() {
        int[] in = {2, 3, 4};
        var target = 6;
        int[] out = {1, 3};

        var ans = TwoSum.twoSum(in, target);
        assertArrayEquals(out, ans);
    }

    @Test
    public void test3() {
        int[] in = {-1, 0};
        var target = -1;
        int[] out = {1, 2};

        var ans = TwoSum.twoSum(in, target);
        assertArrayEquals(out, ans);
    }
}
