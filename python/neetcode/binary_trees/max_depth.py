"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
from dataclasses import dataclass

@dataclass
class Node:
    val: int
    left: 'Node | None' = None
    right: 'Node | None' = None

def max_depth(root: Node | None) -> int:
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    depth = 1 + max(left, right)

    return depth


if __name__ == "__main__":
    n7 = Node(7)
    n15 = Node(15)
    n9 = Node(9)
    n20 = Node(20, n15, n7)
    n3 = Node(3, n9, n20)
    assert max_depth(n3) == 3
