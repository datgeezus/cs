package org.example.intervals;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

class MergeTest {

    @Test
    public void test1() {
        var in = Arrays.asList(Arrays.asList(1, 3), Arrays.asList(2, 6), Arrays.asList(8, 10), Arrays.asList(15, 18));
        var out = List.of(List.of(1, 6), List.of(8, 10), List.of(15, 18));

        var ans = Merge.merge(in);

        assertEquals(out, ans);
    }

    @Test
    public void test2() {
        var in = Arrays.asList(Arrays.asList(1, 4), Arrays.asList(4, 5));
        var out = List.of(List.of(1, 5));

        var ans = Merge.merge(in);

        assertEquals(out, ans);
    }
}
