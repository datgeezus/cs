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


@dataclass
class Node:
    val: int
    left: 'Node | None' = None
    right: 'Node | None' = None


def right_side_view(root: Node | None) -> list[int]:
    if not root:
        return []

    q = deque()
    q.append(root)
    right_values = []

    while q:
        n = len(q)
        for i, _ in enumerate(range(n)):
            node = q.popleft()
            if i + 1 == n:
                right_values.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return right_values


if __name__ == "__main__":
    n5 = Node(5)
    n2 = Node(2, n5)
    n4 = Node(4)
    n3 = Node(3, right=n4)
    n1 = Node(1, n2, n3)
    assert right_side_view(n1) == [1, 3, 4]

    n3 = Node(3)
    n1 = Node(1, right=n3)
    assert right_side_view(n1) == [1, 3]

    assert right_side_view(None) == []
