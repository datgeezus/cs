from queue import Queue
from .node import TreeNode

def dfs_in_order(root: TreeNode, callback=None):
    if root is None: return
    dfs_in_order(root.left, callback)
    callback(root)
    dfs_in_order(root.right, callback)

def dfs_pre_order(root: TreeNode, callback=None):
    if root is None: return
    callback(root)
    dfs_pre_order(root.left, callback)
    dfs_pre_order(root.right, callback)

def dfs_post_order(root: TreeNode, callback=None):
    if root is None: return
    dfs_post_order(root.left, callback)
    dfs_post_order(root.right, callback)
    callback(root)

def bfs(root: TreeNode, callback=None):
    if root is None: return
    q = Queue()
    q.put(root)
    while not q.empty():
        curr = q.get()
        callback(curr)
        if curr.left: 
            q.put(curr.left)
        if curr.right: 
            q.put(curr.right)

if __name__ == "__main__":
    """
    Building Tree
       1
      / \
     2   3
        / \
       4   5
    """
    n1 = TreeNode('A')
    n2 = TreeNode('B')
    n3 = TreeNode('C')
    n4 = TreeNode('D')
    n5 = TreeNode('E')
    n6 = TreeNode('F')
    n7 = TreeNode('G')
    n8 = TreeNode('H')
    n9 = TreeNode('I')

    n6.left = n2
    n6.right = n7
    n2.left = n1
    n2.right = n4
    n4.left = n3
    n4.right = n5
    n7.right = n9
    n9.left = n8

    print("DFS")
    print("in order")
    dfs_in_order(n6, lambda n: print(n.val))
    print("pre order")
    dfs_pre_order(n6, lambda n: print(n.val))
    print("post order")
    dfs_post_order(n6, lambda n: print(n.val))

    print("BFS")
    bfs(n6, lambda n: print(n.val))