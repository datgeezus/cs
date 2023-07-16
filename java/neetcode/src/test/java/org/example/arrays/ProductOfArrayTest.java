package org.example.arrays;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import java.util.List;

class ProductOfArrayTest {

    @Test
    void productOfArray() {
        var in = List.of(1, 2, 3, 4);
        var out = List.of(24, 12, 8, 6);

        var ans = ProductOfArray.productOfArray(in);
        assertEquals(out, ans);
    }

    @Test
    void productOfArrayNeg() {
        var in = List.of(-1, 1, 0, -3, 3);
        var out = List.of(0, 0, 9, 0, 0);

        var ans = ProductOfArray.productOfArray(in);
        assertEquals(out, ans);
    }
}
