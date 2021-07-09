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

def levelOrderBottom(root):
  if root is None: return []

  q = Queue()
  # levels = deque()
  levels = []

  q.put(root)
  n_level = 0
  while(not q.empty()):
    curr = q.get()
    if curr is None:
      n_level -= 1
      continue
    print(len(levels))
    if len(levels) == n_level:
      levels.append([curr.val])
    else:
      levels[n_level].append(curr.val)
    q.put(curr.left)
    q.put(curr.right)
    n_level += 1

  return levels


def getLevel(index):
  return 



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(levelOrderBottom(root))
