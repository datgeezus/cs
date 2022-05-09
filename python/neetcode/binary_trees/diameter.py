"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def get_diameter(root: Optional[TreeNode]) -> int:
    diameter = 0
    def dfs(root: Optional[TreeNode]) -> int:
        nonlocal diameter
        if not root:
            return 0
    
        left = dfs(root.left)
        right = dfs(root.right)
        
        diameter = max(left + right, diameter)
        return 1 + max(left, right)

    dfs(root)
    return diameter

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