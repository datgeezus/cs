package org.example.heaps;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class StoneWeightTest {

    @Test
    public void test1() {
        int[] stones = { 2, 7, 4, 1, 8, 1 };
        var out = 1;

        var ans = StoneWeight.lastStoneWeight(stones);

        assertEquals(out, ans);
    }

    @Test
    public void test2() {
        int[] stones = { 1 };
        var out = 1;

        var ans = StoneWeight.lastStoneWeight(stones);

        assertEquals(out, ans);
    }
}
