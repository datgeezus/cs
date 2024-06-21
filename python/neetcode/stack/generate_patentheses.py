"""
Generate Parentheses

You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]

Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]

You may return the answer in any order.

Constraints:

    1 <= n <= 7
"""
from dataclasses import dataclass, field

@dataclass
class Context:
    n: int
    stack: list[str] = field(default_factory=list)
    ans: list[str] = field(default_factory=list)

def generate_parentheses(n: int) -> list[str]:
    ctx = Context(n=n)
    backtrack(0 , 0, ctx)
    print(ctx)
    return ctx.ans

def backtrack(open: int, closed: int, ctx: Context) -> None:
    if open == closed == ctx.n:
        ctx.ans.append("".join(ctx.stack))
        return

    if open < ctx.n:
        ctx.stack.append('(')
        backtrack(open + 1, closed, ctx)
        ctx.stack.pop()

    if closed < open:
        ctx.stack.append(')')
        backtrack(open, closed + 1, ctx)
        ctx.stack.pop()


def test1():
    out = ["((()))","(()())","(())()","()(())","()()()"]
    ans = generate_parentheses(3)
    assert ans == out

if __name__ == "__main__":
    test1()
