package org.example.btrees;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import java.util.List;

class RightSideViewTest {

    @Test
    public void test1() {
        var n5 = new RightSideView.Node(5);
        var n2 = new RightSideView.Node(2, n5, null);
        var n4 = new RightSideView.Node(4);
        var n3 = new RightSideView.Node(3, null, n4);
        var n1 = new RightSideView.Node(1, n2, n3);

        var out = List.of(1, 3, 4);
        var ans = RightSideView.rightSideView(n1);

        assertEquals(out, ans);
    }

    @Test
    public void test2() {
        var n3 = new RightSideView.Node(3);
        var n1 = new RightSideView.Node(1, null, n3);

        var out = List.of(1, 3);
        var ans = RightSideView.rightSideView(n1);

        assertEquals(out, ans);
    }
}
