package org.example.backtracking;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import java.util.Collections;
import java.util.List;

class CombinationSumTest {

    @Test
    void combinationSum() {
        int[] in = {2, 3, 6, 7};
        var out = List.of(List.of(2, 2, 3), List.of(7));
        var ans = CombinationSum.combinationSum(in, 7);

        assertEquals(out, ans);
    }

    @Test
    void combinationSum2() {
        int[] in = {2, 3, 5};
        var out = List.of(List.of(2, 2, 2, 2), List.of(2, 3, 3), List.of(3, 5));
        var ans = CombinationSum.combinationSum(in, 8);

        assertEquals(out, ans);
    }

    @Test
    void combinationSum3() {
        int[] in = {2};
        var out = Collections.emptyList();
        var ans = CombinationSum.combinationSum(in, 1);

        assertEquals(out, ans);
    }
}
