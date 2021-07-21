"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
"""

from typing import List
from data_structures.node import TreeNode
from collections import deque

def right_side_view(root: TreeNode) -> List[int]:
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
    print(right_side_view(TreeNode.from_list([1,2]))) # Expected [1,2]
    print(right_side_view(TreeNode.from_list([1,None,3]))) # Expected [1,2]
    print(right_side_view(TreeNode.from_list([1,2,3,None,5,None,4]))) # Expected [1,3,4]
