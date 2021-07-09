from queue import Queue
from node import TreeNode

def dfs_in_order(root: TreeNode, callback=None):
    if root is None: return

    callback(root)
    dfs_in_order(root.left, callback)
    dfs_in_order(root.right, callback)
    return

def bfs(root: TreeNode, q: Queue, callback=None):
    while(not q.empty()):
        curr = q.get()
        callback(curr)
        if curr.left: 
            q.put(curr.left)
        if curr.right: 
            q.put(curr.right)
    return

if __name__ == "__main__":
    """
    Building Tree
       1
      / \
     2   3
        / \
       4   5
    """
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5

    print("DFS")
    dfs_in_order(n1, lambda n: print(n.val))

    print("BFS")
    q = Queue()
    q.put(n1)
    bfs(n1, q, lambda n: print(n.val))