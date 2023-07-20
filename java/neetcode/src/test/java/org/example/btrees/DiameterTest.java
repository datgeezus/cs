package org.example.btrees;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class DiameterTest {

    @Test
    void test1() {
        var n5 = new Diameter.Node(5);
        var n4 = new Diameter.Node(4);
        var n2 = new Diameter.Node(2, n4, n5);
        var n3 = new Diameter.Node(3);
        var n1 = new Diameter.Node(1, n2, n3);
        var out = 3;

        var ans = Diameter.diameter(n1);

        assertEquals(out, ans);
    }

    @Test
    void test2() {
        var n2 = new Diameter.Node(2);
        var n1 = new Diameter.Node(1, n2, null);
        var out = 1;

        var ans = Diameter.diameter(n1);

        assertEquals(out, ans);
    }
}
