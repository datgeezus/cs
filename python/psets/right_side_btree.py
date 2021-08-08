"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
"""

from data_structures.btree import BTree, BTreeNode
from typing import List
from collections import deque

def right_side_view(root: BTreeNode) -> List[int]:
    if root is None: return []
    q = deque()
    q.append(root)
    ans = []
    while q:
        n = len(q)
        right = None
        for _ in range(n):
            curr = q.popleft()
            if curr is None: continue
            q.append(curr.left)
            q.append(curr.right)
            right = curr

        if right:
            ans.append(right.val)

    return ans


if __name__ == "__main__":
    print(right_side_view(BTree.from_list([1,2]).root)) # Expected [1,2]
    print(right_side_view(BTree.from_list([1,None,3]).root)) # Expected [1,2]
    print(right_side_view(BTree.from_list([1,2,3,None,5,None,4]).root)) # Expected [1,3,4]
