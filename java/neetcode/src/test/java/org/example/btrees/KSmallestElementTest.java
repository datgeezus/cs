package org.example.btrees;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class KSmallestElementTest {

    @Test
    public void test1() {
        var n2 = new Node(2);
        var n1 = new Node(1, null, n2);
        var n4 = new Node(4);
        var n3 = new Node(3, n1, n4);
        var out = 1;

        var ans = KSmallestElement.kSmallest(n3, 1);

        assertEquals(out, ans);
    }

    @Test
    public void test2() {
        var n1 = new Node(1);
        var n2 = new Node(2, n1, null);
        var n4 = new Node(4);
        var n3 = new Node(3, n2, n4);
        var n6 = new Node(6);
        var n5 = new Node(5, n3, n6);
        var out = 3;

        var ans = KSmallestElement.kSmallest(n5, 3);

        assertEquals(out, ans);
    }
}
