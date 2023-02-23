package com.cs.arrays;

import org.junit.Test;

import static org.junit.Assert.assertTrue;

public class ContainsDuplicateTest {

    @Test
    public void testContains() {
        int[] input = new int[]{1,2,3,1};
        boolean ans = ContainsDuplicate.containsDuplicate(input);
//        boolean ans = ContainsDuplicate.duplicate(input);
        assertTrue(ans);
    }
}
