'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from typing import List
from data_structures.node import TreeNode

def bfs(root: TreeNode) -> List[List[int]]:
    if root is None: return []
    levels = []
    q = deque()
    q.append(root)
    while q:
        n = len(q)
        this_level = []
        for _ in range(n):
            tmp = q.popleft()
            this_level.append(tmp.val)
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
        levels.append(this_level)
    return levels

def bfs_bootom_up(root: TreeNode) -> List[List[int]]:
    if root is None: return []
    levels = deque()
    q = deque()
    q.append(root)
    while q:
        n = len(q)
        this_level = []
        for _ in range(n):
            tmp = q.popleft()
            this_level.append(tmp.val)
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
        levels.appendleft(this_level)
    return list(levels)

if __name__ == '__main__':
    print(bfs(TreeNode.from_list([3,9,20,None,None,15,7])))
    print(bfs_bootom_up(TreeNode.from_list([3,9,20,None,None,15,7])))
