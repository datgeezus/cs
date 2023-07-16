package org.example.arrays;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class ProductOfArrayTest {

    @Test
    void productOfArray() {
        var in = new Integer[]{1, 2, 3, 4};
        var out = new Integer[]{24, 12, 8, 6};

        var ans = ProductOfArray.productOfArray(in);
        assertArrayEquals(out, ans);
    }

    @Test
    void productOfArrayNeg() {
        var in = new Integer[]{-1, 1, 0, -3, 3};
        var out = new Integer[]{0, 0, 9, 0, 0};

        var ans = ProductOfArray.productOfArray(in);
       assertArrayEquals(out, ans);
    }
}
