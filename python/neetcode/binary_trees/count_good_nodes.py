"""
# Problem:
Given a binary tree root, a node X in the tree is named good if in the path from root to X there
are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None
    
@dataclass
class NodeData:
    n_nodes: int

def good_nodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    data = NodeData(0)
    
    def dfs(root: Optional[TreeNode], target: int, node_data: NodeData):
        if not root:
            return
        if root.val >= target:
            node_data.n_nodes += 1
        new_max = max(target, root.val)
        dfs(root.left, new_max, node_data)
        dfs(root.right, new_max, node_data)
    

    dfs(root, root.val, data)
    return data.n_nodes


if __name__ == "__main__":
    n1b = TreeNode(1)
    n5 = TreeNode(5)
    n4 = TreeNode(4, n1b, n5)
    n3b = TreeNode(3)
    n1a = TreeNode(1, n3b)
    n3a = TreeNode(3, n1a, n4)
    assert good_nodes(n3a) == 4
    
    n2 = TreeNode(2)
    n4 = TreeNode(4)
    n3b = TreeNode(3, n4, n2)
    n3a = TreeNode(3, n3b)
    assert good_nodes(n3a) == 3

    assert good_nodes(TreeNode(1)) == 1
