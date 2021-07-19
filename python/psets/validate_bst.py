"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

from data_structures.node import TreeNode

def is_bst(root: TreeNode) -> bool:
    ans = []
    def dfs(root: TreeNode):
        if root is None: return
        dfs(root.left)
        ans.append(root.val)
        dfs(root.right)

    dfs(root)
    for i in range(1,len(ans)):
        if ans[i] <= ans[i-1]: return False
    return True

if __name__ == "__main__":
    print(is_bst(TreeNode.from_list([2,1,3])))
    print(is_bst(TreeNode.from_list([5,1,4,None,None,3,6])))
    print(is_bst(TreeNode.from_list([2,2,2])))