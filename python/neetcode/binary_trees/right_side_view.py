"""
# Problem
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.


# Solution
BFS
Level order traversal
each level add the last node

"""

from collections import deque
from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: Optional[int]
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def right_side_view(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    q = deque()
    q.appendleft(root)
    right_values = []

    while q:
        n = len(q)
        for i, _ in enumerate(range(n)):
            node = q.pop()
            if i + 1 == n:
                right_values.append(node.val)
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)

    return right_values


if __name__ == "__main__":
    n5 = TreeNode(5)
    n2 = TreeNode(2, n5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, right=n4)
    n1 = TreeNode(1, n2, n3)
    assert right_side_view(n1) == [1, 3, 4]

    n3 = TreeNode(3)
    n1 = TreeNode(1, right=n3)
    assert right_side_view(n1) == [1, 3]

    assert right_side_view(None) == []
