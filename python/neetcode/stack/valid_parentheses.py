"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
"""

from collections import deque

def is_valid_parentheses(s: str) -> bool:
    stack = deque()
    close_to_open = { 
        ")": "(", 
        "}": "{", 
        "]": "[" }
               
    for c in s:
        if c in close_to_open: 
            if stack and stack[-1] == close_to_open[c]: 
                stack.pop() 
            else:
                return False
        else:
            stack.append(c)

    # valid if stack is empty
    return True if not stack else False
               

if __name__ == "__main__":
    assert is_valid_parentheses("()")
    assert is_valid_parentheses("()[]{}")
    assert is_valid_parentheses("(]") is False
