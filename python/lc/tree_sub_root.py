"""

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

 

Constraints:

    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -104 <= root.val <= 104
    -104 <= subRoot.val <= 104

"""

"""

class Solution:
    def isBubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

"""
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None


def is_sub_tree(root: TreeNode | None, sub_root: TreeNode | None) -> bool:

    ans = False

    def dfs(root: TreeNode, visit: callable) -> None:
        if not root:
            return

        dfs(root.left, visit)
        match = visit(root)
        dfs(root.right, visit)


    roots = []
    def find_sub_root(root: TreeNode) -> bool:
        match = root.val == sub_root.val
        if match:
            roots.append(root)
        return match

    def serialize(root: TreeNode, vals: list[int]) -> bool:
        vals.append(root.val)
        return False

    dfs(root, find_sub_root)

    print(roots)
    if not roots:
        return False

    preorder = lambda vals: lambda root: serialize(root, vals)

    sub_root_vals = []

    dfs(sub_root, preorder(sub_root_vals))
    print(sub_root_vals)

    for froot in roots:
        root_vals = []
        dfs(froot, preorder(root_vals))
        print(root_vals)
        if root_vals == sub_root_vals:
            return True


    return False



if __name__ == '__main__':
    # Example 1
    print("Example 1")
    root = TreeNode(3, 
                    TreeNode(4, TreeNode(1), TreeNode(2)), 
                    TreeNode(5))
    sub_root= TreeNode(4, TreeNode(1), TreeNode(2))

    assert is_sub_tree(root, sub_root)

    # Example 2
    print("Example 2")
    root = TreeNode(3, 
                    TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), 
                    TreeNode(5))
    sub_root= TreeNode(4, TreeNode(1), TreeNode(2))

    assert not is_sub_tree(root, sub_root)

    # Example 3
    print("Example 3")
    root = TreeNode(1, TreeNode(1))
    sub_root= TreeNode(1)

    assert is_sub_tree(root, sub_root)

    # Example 4
    print("Example 4")
    root = TreeNode(3, 
                    TreeNode(4, TreeNode(1), TreeNode(2)), 
                    TreeNode(5))
    sub_root= TreeNode(4, TreeNode(1, None, TreeNode(2)))

    assert not is_sub_tree(root, sub_root)
