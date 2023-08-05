package org.example.stack;

import java.util.Map;
import java.util.Stack;

/**
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 *
 * An input string is valid if:
 *
 *     Open brackets must be closed by the same type of brackets.
 *     Open brackets must be closed in the correct order.
 *     Every close bracket has a corresponding open bracket of the same type.
 *
 *
 *
 * Example 1:
 *
 * Input: s = "()"
 * Output: true
 *
 * Example 2:
 *
 * Input: s = "()[]{}"
 * Output: true
 *
 * Example 3:
 *
 * Input: s = "(]"
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *     1 <= s.length <= 104
 *     s consists of parentheses only '()[]{}'.
 */
public class ValidParentheses {
    private static final Map<Character, Character> parentheses = Map.of(
            '{', '}', '[', ']', '(', ')', ' ', ' '
    );

    public static boolean isValid(String s) {
        var nChars = s.length();
        var stack = new Stack<Character>();

        for (int i = 0; i < nChars; ++i) {
            var c = s.charAt(i);
            if (parentheses.containsKey(c)) {
                stack.add(c);
            } else {
                var now = stack.isEmpty() ? ' ' : stack.pop();
                if (c != parentheses.get(now)) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}
