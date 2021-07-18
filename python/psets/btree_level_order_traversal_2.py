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

from queue import Queue
from collections import deque
from typing import List
from data_structures.node import TreeNode

def level_order(root): 
    return bfs(root)


def bfs(root: TreeNode) -> List[List[int]]:
    if root is None: return []
    levels = []
    q = Queue()
    q.put(root)
    while not q.empty():
        n = q.qsize()
        this_level = []
        while n > 0:
            tmp = q.get()
            this_level.append(tmp.val)
            if tmp.left:
                q.put(tmp.left)
            if tmp.right:
                q.put(tmp.right)
            n -= 1
        levels.append(this_level)
    return levels

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(level_order(root))
