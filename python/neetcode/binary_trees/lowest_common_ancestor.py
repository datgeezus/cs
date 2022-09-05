"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
    “The lowest common ancestor is defined between two nodes p and q as the lowest node in T
    that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Solution:
Find the split in node

"""

from dataclasses import dataclass

@dataclass
class Node:
    val: int
    left: 'Node | None' = None
    right: 'Node | None' = None


def lca(root: Node | None, p: Node | None, q: Node | None) -> Node | None:
    if not p or not q:
        return None
    curr = root
    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr


if __name__ == "__main__":
    n3 = Node(3)
    n5 = Node(5)
    n0 = Node(0)
    n4 = Node(4, n3, n5)
    n2 = Node(2, n0, n4)
    n7 = Node(7)
    n9 = Node(9)
    n8 = Node(8, n7, n9)
    n6 = Node(6, n2, n8)

    ans = lca(n6, n2, n8)
    assert ans
    assert ans.val == 6
    print(f"LCA betwwen {n2.val} and {n8.val} is {ans.val}")
