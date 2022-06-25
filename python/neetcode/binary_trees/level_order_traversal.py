"""
# Problem
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

# Solution
BFS
Each level, get the len of the queue, this will get how many nodes are in this level

while there are elements in the queue:
    new list to hold nodes in this level
    for each node in current level:
        append node.left and node.right if they're valid (to continue BFS)
        add node.val to the list
    append list nodes in this level


"""

from dataclasses import dataclass
from typing import Optional
from collections import deque


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def level_order_traversal(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []

    q = deque()
    q.appendleft(root)
    levels = []

    while q:
        this_level = []
        n = len(q)
        for _ in range(n):
            node = q.pop()
            this_level.append(node.val)
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
        levels.append(this_level)

    return levels


if __name__ == "__main__":
    n7 = TreeNode(7)
    n15 = TreeNode(15)
    n20 = TreeNode(20, n15, n7)
    n9 = TreeNode(9)
    n3 = TreeNode(3, n9, n20)
    print(level_order_traversal(n3))

    assert level_order_traversal(TreeNode(1)) == [[1]]

    assert not level_order_traversal(None)
