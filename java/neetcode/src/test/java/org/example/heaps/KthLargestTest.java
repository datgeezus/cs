package org.example.heaps;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class KthLargestTest {

    @Test
    public void test1() {
        int k = 3;
        int[] nums = {4, 5, 8, 2};
        KthLargest obj = new KthLargest(k, nums);

        assertEquals(4, obj.add(3));
        assertEquals(5, obj.add(5));
        assertEquals(5, obj.add(10));
        assertEquals(8, obj.add(9));
        assertEquals(8, obj.add(4));
    }
}
