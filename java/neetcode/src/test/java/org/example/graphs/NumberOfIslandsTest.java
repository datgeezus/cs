package org.example.graphs;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class NumberOfIslandsTest {

    @Test
    public void test1() {
        char[][] grid = {
                {'1', '1', '0', '0', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '1', '0', '0'},
                {'0', '0', '0', '1', '1'}
        };

        var out = 3;
        var ans = NumberOfIslands.numberOfIslans(grid);

        assertEquals(out, ans);
    }

    @Test
    public void test2() {
        char[][] grid = {
                {'1', '1', '1', '1', '0'},
                {'1', '1', '0', '1', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '0', '0', '0'}
        };

        var out = 1;
        var ans = NumberOfIslands.numberOfIslans(grid);

        assertEquals(out, ans);
    }
}
