package org.example.heaps;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class KClosestPointsTest {

    @Test
    public void test1() {
        int[][] points = {{ 1, 3 }, { -2, 2 }};
        int k = 1;
        int[][] out = {{-2, 2}};
        int[][] ans = KClosestPoints.kClosest(points, k);

        assertArrayEquals(out, ans);
    }

    @Test
    public void test2() {
        int[][] points = {{ 3, 3 }, { 5, -1 }, { -2, 4 }};
        int k = 2;
        int[][] out = {{ -2, 4}, {3, 3}};
        int[][] ans = KClosestPoints.kClosest(points, k);

        assertArrayEquals(out, ans);
    }
}
