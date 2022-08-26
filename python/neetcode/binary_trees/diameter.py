"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""

from dataclasses import dataclass
from typing import Callable


@dataclass
class StrategyData:
    diameter: int


@dataclass
class Node:
    val: int
    left: 'Node | None' = None
    right: 'Node | None' = None


def get_diameter(root: Node | None) -> int:
    def strategy(left: int, right: int, data: StrategyData):
        data.diameter = max(left + right, data.diameter)

    def dfs(
        root: Node | None,
        strategy: Callable[[int, int, StrategyData], None],
        data: StrategyData,
    ) -> int:
        if not root:
            return 0

        left = dfs(root.left, strategy, data)
        right = dfs(root.right, strategy, data)

        strategy(left, right, data)
        return 1 + max(left, right)

    data = StrategyData(0)
    dfs(root, strategy, data)
    return data.diameter


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
