"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:

Input: root = [4,2,7,1,3], val = 5
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [1, 5000].
    1 <= Node.val <= 107
    root is a binary search tree.
    1 <= val <= 107

"""
from dataclasses import dataclass

@dataclass
class Node:
    val: int
    left: 'Node | None' = None
    right: 'Node | None' = None

def bst_search(root: Node | None, val: int) -> Node | None:
    if not root or root.val == val:
        return root

    return bst_search(root.left, val) if val < root.val \
        else bst_search(root.right, val)

def bst_insert(root: Node | None, val: int) -> Node | None:
    if not root:
        return Node(val)

    if val > root.val:
        root.right = bst_insert(root.right, val)
    else:
        root.left = bst_insert(root.left, val)

    return root

def bst_to_list(root: Node | None) -> list[int]:
    def dfs(root: Node | None, l: list[int]) -> None:
        if not root:
            return

        l.append(root.val)
        dfs(root.left, l)
        dfs(root.right, l)

    ans = []
    dfs(root, ans)
    return ans



if __name__ == "__main__":
    bst = Node(4, Node(2, Node(1), Node(3)), Node(7))
    print(bst_to_list(bst))
    ans = bst_search(bst, 2)
    print(bst_to_list(ans))
