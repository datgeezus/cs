from queue import Queue
from data_structures.node import TreeNode

def is_even_odd(root: TreeNode) -> bool:
    q = Queue()
    q.put(root)
    this_level = 0
    while not q.empty():
        n = q.qsize()
        prev = None
        for _ in range(n):
            curr = q.get()
            # visit 
            if curr is None or prev is None: 
                if curr.left is not None: q.put(curr.left)
                if curr.right is not None: q.put(curr.right)
                prev = curr
                continue
            
            if this_level % 2 == 0:
                if not check_even_level(prev.val, curr.val): return False
            elif not check_odd_level(prev.val, curr.val): return False
            
            if curr.left is not None: q.put(curr.left)
            if curr.right is not None: q.put(curr.right)
            prev = curr
        this_level += 1
    return True

def check_odd_level(prev, curr):
    return (prev % 2 == 0) and (curr % 2 == 0) and prev > curr

def check_even_level(prev, curr):
    return (prev % 2 != 0) and (curr % 2 != 0) and prev < curr

if __name__ == "__main__":
    print(is_even_odd(TreeNode.from_list([5,4,2,3,3,7])))
    print(is_even_odd(TreeNode.from_list([1,10,4,3,None,7,9,12,8,6,None,None,2])))
    print(is_even_odd(TreeNode.from_list([5,9,1,3,5,7])))