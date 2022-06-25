"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""

from dataclasses import dataclass
from typing import Optional, Callable


@dataclass
class StrategyData:
    diameter: int


@dataclass
class TreeNode:
    val: int
    left: "TreeNode" = None
    right: "TreeNode" = None


def get_diameter(root: Optional[TreeNode]) -> int:
    def strategy(left: int, right: int, data: StrategyData):
        data.diameter = max(left + right, data.diameter)

    def dfs(
        root: Optional[TreeNode],
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
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n2 = TreeNode(2, n4, n5)
    n3 = TreeNode(3)
    n1 = TreeNode(1, n2, n3)
    assert get_diameter(n1) == 3

    n = TreeNode(1, TreeNode(2))
    assert get_diameter(n) == 1

    print("All tests passed")
