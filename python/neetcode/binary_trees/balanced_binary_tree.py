"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None
    
@dataclass
class NodeData:
    is_balanced: bool
    height: int
    

def is_balanced(root: Optional[TreeNode]) -> bool:
    
    def are_children_balanced(left: NodeData, right: NodeData) -> bool:
        return left.is_balanced and right.is_balanced \
            and abs(left.height - right.height) <= 1
    
    def dfs(root: Optional[TreeNode]) -> NodeData:
        if not root:
            return NodeData(True, 0)
        left = dfs(root.left)
        right = dfs(root.right)
        ans = are_children_balanced(left, right)
        max_height = max(left.height, right.height)
        return NodeData(ans, 1 + max_height)
    
    ans = dfs(root)
    return ans.is_balanced

if __name__ == "__main__":
    n7 = TreeNode(7)
    n15 = TreeNode(15)
    n20 = TreeNode(20, n15, n7)
    n9 = TreeNode(9)
    n3 = TreeNode(3, n9, n20)
    assert is_balanced(n3)
    
    n4l = TreeNode(4)
    n4r = TreeNode(4)
    n3l = TreeNode(3, n4l, n4r)
    n3r = TreeNode(3)
    n2l = TreeNode(2, n3l, n3r)
    n2r = TreeNode(2)
    n1 = TreeNode(1, n2l, n2r)
    assert is_balanced(n1) is False
    
    assert is_balanced(TreeNode())