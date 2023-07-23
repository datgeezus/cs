package org.example.dp;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class ClimbStairsTest {

    @Test
    public void test1() {
        int n = 2;
        int out = 2;
        int ans = ClimbStairs.climbStairs(n);
        assertEquals(out, ans);
    }

    @Test
    public void test2() {
        int n = 3;
        int out = 3;
        int ans = ClimbStairs.climbStairs(n);
        assertEquals(out, ans);
    }

    @Test
    public void test3() {
        int n = 2;
        int out = 2;
        int ans = ClimbStairs.climbStairsTopDown(n);
        assertEquals(out, ans);
    }

    @Test
    public void test4() {
        int n = 3;
        int out = 3;
        int ans = ClimbStairs.climbStairsTopDown(n);
        assertEquals(out, ans);
    }
}
