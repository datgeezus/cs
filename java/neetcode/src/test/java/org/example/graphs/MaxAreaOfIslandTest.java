package org.example.graphs;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class MaxAreaOfIslandTest {

    @Test
    public void test1() {
        int[][] grid = {
                {0,0,1,0,0,0,0,1,0,0,0,0,0},
                {0,0,0,0,0,0,0,1,1,1,0,0,0},
                {0,1,1,0,1,0,0,0,0,0,0,0,0},
                {0,1,0,0,1,1,0,0,1,0,1,0,0},
                {0,1,0,0,1,1,0,0,1,1,1,0,0},
                {0,0,0,0,0,0,0,0,0,0,1,0,0},
                {0,0,0,0,0,0,0,1,1,1,0,0,0},
                {0,0,0,0,0,0,0,1,1,0,0,0,0}
        };

        var out = 6;
        var ans = MaxAreaOfIsland.maxArea(grid);

        assertEquals(out, ans);
    }

    @Test
    public void test2() {
        int[][] grid = {
                {0, 0, 0, 0, 0 ,0 ,0 ,0}
        };
        var out = 0;
        var ans = MaxAreaOfIsland.maxArea(grid);

        assertEquals(out, ans);
    }
}
