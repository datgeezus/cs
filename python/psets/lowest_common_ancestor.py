from data_structures.node import TreeNode

def lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root is None: return None
    if root.val == p.val or root.val == q.val: return root

    l = lca(root.left, p, q)
    r = lca(root.right, p ,q)
    if l is None: return r
    if r is None: return l
    return root

if __name__ == "__main__":
    print(lca(TreeNode.from_list([3,5,1,6,2,0,8,None,None,7,4]),TreeNode(5),TreeNode(1)).val)
    print(lca(TreeNode.from_list([3,5,1,6,2,0,8,None,None,7,4]),TreeNode(5),TreeNode(4)).val)
    print(lca(TreeNode.from_list([3,5,1,6,2,0,8,None,None,7,4]),TreeNode(6),TreeNode(8)).val)
    print(lca(TreeNode.from_list([3,5,1,6,2,0,8,None,None,7,4]),TreeNode(0),TreeNode(8)).val)