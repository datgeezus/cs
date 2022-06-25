"""
Given the root of a binary tree, invert the tree and return its root
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    tmp = root.left
    root.left = root.right
    root.right = tmp

    invert_tree(root.left)
    invert_tree(root.right)
    return root


if __name__ == "__main__":
    n9 = TreeNode(9)
    n6 = TreeNode(6)
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n2 = TreeNode(2, n1, n3)
    n7 = TreeNode(7, n6, n9)
    n4 = TreeNode(4, n2, n7)
    ans = invert_tree(n4)
    assert ans.left == n7
    assert ans.right == n2
    assert ans.left.left == n9
