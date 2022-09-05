"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""

from dataclasses import dataclass
from collections.abc import Callable

@dataclass
class Node:
    val: int
    left: 'Node | None' = None
    right: 'Node | None' = None

@dataclass
class Context:
    diameter: int

def get_diameter(root: Node | None) -> int:
    def strategy(left: int, right: int, ctx: Context):
        ctx.diameter = max(left + right, ctx.diameter)

    ctx = Context(0)
    dfs(root, strategy, ctx)
    return ctx.diameter

def dfs(
    root: Node | None,
    strategy: Callable[[int, int, Context], None],
    ctx: Context,
) -> int:
    if not root:
        return 0

    left = dfs(root.left, strategy, ctx)
    right = dfs(root.right, strategy, ctx)

    strategy(left, right, ctx)
    return 1 + max(left, right)


if __name__ == "__main__":
    n5 = Node(5)
    n4 = Node(4)
    n2 = Node(2, n4, n5)
    n3 = Node(3)
    n1 = Node(1, n2, n3)
    assert get_diameter(n1) == 3

    n = Node(1, Node(2))
    assert get_diameter(n) == 1

    print("All tests passed")
