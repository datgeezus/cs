package org.example.greedy;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class JumpGameTest {

    @Test
    public void test1() {
        int[] nums = {2, 3, 1, 1, 4};
        var ans = JumpGame.canJump(nums);
        assertTrue(ans);
    }

    @Test
    public void test2() {
        int[] nums = {3, 2, 1, 0, 4};
        var ans = JumpGame.canJump(nums);
        assertFalse(ans);
    }
}
