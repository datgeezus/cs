package org.example.twopointers;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import java.util.List;

class ThreeSumTest {

    @Test
    public void test1() {
        int[] nums = { -1, 0, 1, 2, -1, -4 };
        var out = List.of(
                List.of(-1, -1, 2), List.of(-1, 0, 1)
        );

        var ans = ThreeSum.threeSum(nums);

        assertEquals(out, ans);
    }

    @Test
    public void test2() {
        int[] nums = { 0, 1, 1 };
        var out = List.of();

        var ans = ThreeSum.threeSum(nums);

        assertEquals(out, ans);
    }
}
