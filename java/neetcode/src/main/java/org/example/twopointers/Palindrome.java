package org.example.twopointers;

/**
 * A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
 * removing all non-alphanumeric characters, it reads the same forward and backward.
 * Alphanumeric characters include letters and numbers.
 *
 * Given a string s, return true if it is a palindrome, or false otherwise.
 *
 *
 *
 * Example 1:
 *
 * Input: s = "A man, a plan, a canal: Panama"
 * Output: true
 * Explanation: "amanaplanacanalpanama" is a palindrome.
 *
 * Example 2:
 *
 * Input: s = "race a car"
 * Output: false
 * Explanation: "raceacar" is not a palindrome.
 *
 * Example 3:
 *
 * Input: s = " "
 * Output: true
 * Explanation: s is an empty string "" after removing non-alphanumeric characters.
 * Since an empty string reads the same forward and backward, it is a palindrome.
 *
 *
 *
 * Constraints:
 *
 *     1 <= s.length <= 2 * 105
 *     s consists only of printable ASCII characters.
 */

public class Palindrome {
    public static boolean isPalindrome(String s) {
        var len = s.length();
        var l = 0;
        var r = len - 1;
        var lower = s.toLowerCase();
        char left = ' ';
        char right = ' ';

        while (l < r) {
            left = lower.charAt(l);
            right = lower.charAt(r);
            while (!Character.isLetterOrDigit(left) && l < r) {
                l += 1;
                left = lower.charAt(l);
            }

            while (!Character.isLetterOrDigit(right) && l < r) {
                r -= 1;
                right = lower.charAt(r);
            }

            if (left != right) {
                return false;
            }

            l += 1;
            r -= 1;
        }
        return true;
    }
}
