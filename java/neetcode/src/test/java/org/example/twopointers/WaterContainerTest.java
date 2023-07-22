package org.example.twopointers;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class WaterContainerTest {

    @Test
    public void test1() {
        int[] height = { 1, 8, 6, 2, 5 ,4, 8, 3, 7 };
        int out = 49;

        int ans = WaterContainer.maxArea(height);

        assertEquals(out, ans);
    }

    @Test
    public void test2() {
        int[] height = { 1, 1 };
        int out = 1;

        int ans = WaterContainer.maxArea(height);

        assertEquals(out, ans);
    }
}
