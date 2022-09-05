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
from collections import deque


@dataclass
class Node:
    val: int
    left: 'Node | None' = None
    right: 'Node | None' = None


def level_order_traversal(root: Node | None) -> list[list[int]]:
    if not root:
        return []

    q = deque()
    q.append(root)
    levels = []

    while q:
        this_level = []
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            this_level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        levels.append(this_level)

    return levels


if __name__ == "__main__":
    n7 = Node(7)
    n15 = Node(15)
    n20 = Node(20, n15, n7)
    n9 = Node(9)
    n3 = Node(3, n9, n20)


    assert level_order_traversal(Node(1)) == [[1]]

    ans = level_order_traversal(n3)
    print(f"levels: {ans}")
    assert len(ans) == 3

    assert not level_order_traversal(None)
