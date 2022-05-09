"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    depth = 1 + max(left, right)

    return depth


if __name__ == "__main__":
    n7 = TreeNode(7)
    n15 = TreeNode(15)
    n9 = TreeNode(9)
    n20 = TreeNode(20, n15, n7)
    n3 = TreeNode(3, n9, n20)
    assert max_depth(n3) == 3
