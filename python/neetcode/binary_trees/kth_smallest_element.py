"""
# Problem
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
of all the values of the nodes in the tree.

# Solution
In order traversal, return the kth
"""

from dataclasses import dataclass
from typing import Callable, Optional

@dataclass
class TreeNode:
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None
    
@dataclass
class NodeData:
    order: list[int]
    visit: Callable[[TreeNode, 'NodeData'], None]

def k_smallest(root: Optional[TreeNode], k: int) -> int:
    
    def visit(node: TreeNode, data: NodeData) -> None:
        data.order.append(node.val)
            
    def inorder(root: Optional[TreeNode], node_data: NodeData) -> None:
        if not root:
            return
        inorder(root.left, node_data)
        node_data.visit(root, node_data)
        inorder(root.right, node_data)
        
    ans = []
    ndata = NodeData(ans, visit)
    inorder(root, ndata)
    return ans[k-1]


if __name__ == "__main__":
    n2 = TreeNode(2)
    n1 = TreeNode(1, right=n2)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n1, n4)
    assert k_smallest(n3, 1) == 1
    
    n1 = TreeNode(1)
    n2 = TreeNode(2, left=n1)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n2, n4)
    n6 = TreeNode(6)
    n5 = TreeNode(5, n3, n6)
    assert k_smallest(n5, 3) == 3