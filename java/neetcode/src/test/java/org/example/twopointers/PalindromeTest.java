package org.example.twopointers;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class PalindromeTest {

    @Test
    public void test1() {
        var in = "A man, a plan, a canal: Panama";
        var ans = Palindrome.isPalindrome(in);
        assertTrue(ans);
    }

    @Test
    public void test2() {
        var in = "race a car";
        var ans = Palindrome.isPalindrome(in);
        assertFalse(ans);
    }

    @Test
    public void test3() {
        var in = "0P";
        var ans = Palindrome.isPalindrome(in);
        assertFalse(ans);
    }
}
