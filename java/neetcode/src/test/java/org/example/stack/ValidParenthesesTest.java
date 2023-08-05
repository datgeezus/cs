package org.example.stack;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class ValidParenthesesTest {

    @Test
    public void test1() {
        var in = "()";
        var ans = ValidParentheses.isValid(in);
        assertTrue(ans);
    }

    @Test
    public void test2() {
        var in = "()[]{}";
        var ans = ValidParentheses.isValid(in);
        assertTrue(ans);
    }

    @Test
    public void test3() {
        var in = "(]";
        var ans = ValidParentheses.isValid(in);
        assertFalse(ans);
    }

    @Test
    public void test4() {
        var in = "{[]}";
        var ans = ValidParentheses.isValid(in);
        assertTrue(ans);
    }

    @Test
    public void test5() {
        var in = "(";
        var ans = ValidParentheses.isValid(in);
        assertFalse(ans);
    }

    @Test
    public void test6() {
        var in = "((";
        var ans = ValidParentheses.isValid(in);
        assertFalse(ans);
    }
}
