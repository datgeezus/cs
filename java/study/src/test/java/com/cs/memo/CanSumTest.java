package com.cs.memo;

import org.junit.Test;

import static org.junit.Assert.assertTrue;

import java.util.HashMap;

public class CanSumTest {

    @Test
    public void testCanSum() {
        Boolean res = CanSum.canSum(7, new int[]{2, 3}, new HashMap<>());
        assertTrue(res);
    }
}
