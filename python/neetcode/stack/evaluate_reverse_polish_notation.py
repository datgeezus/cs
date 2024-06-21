"""
Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.

Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5

Constraints:

    1 <= tokens.length <= 1000.
    tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
"""
from collections import deque

def eval_reverse_polish_notation(tokens: list[str]) -> int:
    vals = deque()
    for token in tokens:
        if token.lstrip("-").isdigit():
            vals.append(int(token))
        else:
            a, b = vals.pop(), vals.pop()
            res = compute(a, b, token)
            vals.append(res)
        print(vals)
    return vals[0]

def compute(a: int, b: int, op: str) -> int:
    # print(a, b)
    if op == "-":
        return b - a
    elif op == "+":
        return a + b
    elif op == "*":
        return a * b
    else:
        return int(b / a)



def test1():
    print("test1")
    tokens = ["1","2","+","3","*","4","-"]
    ans = eval_reverse_polish_notation(tokens)
    assert ans == 5

def test2():
    print("test2")
    tokens = ["4","13","5","/","+"]
    ans = eval_reverse_polish_notation(tokens)
    assert ans == 6

def test3():
    print("test3")
    tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    ans = eval_reverse_polish_notation(tokens)
    assert ans == 22

if __name__ == "__main__":
    test1()
    test2()
    test3()
