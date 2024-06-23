"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a
root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

 

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

"""
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None

@dataclass
class Context:
    target: int

def path_sum(root: TreeNode, target: int) -> bool:
    ctx = Context(target)
    return dfs(root, ctx)


def dfs(root: TreeNode, ctx: Context) -> bool:
    print(ctx)
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == ctx.target

    ctx.target -= root.val

    if dfs(root.left, ctx):
        return True

    if dfs(root.right, ctx):
        return True

    ctx.target += root.val
    return False

def test4():
    print("\ntest4")
    root = TreeNode(-2, None, TreeNode(-3))
    target = -5
    assert path_sum(root, target)


def test3():
    print("\ntest3")
    root = TreeNode(1, TreeNode(2))
    target = 1
    assert not path_sum(root, target)


def test2():
    print("\ntest2")
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    target = 5
    ans = path_sum(root, target)
    assert not ans


def test1(): 
    print("\ntest1")
    root = TreeNode(5,
                TreeNode(4, 
                    TreeNode(11, 
                        TreeNode(7),
                        TreeNode(2))),
                TreeNode(8,
                        TreeNode(13),
                        TreeNode(4, None, TreeNode(1))))
    target = 22
    ans = path_sum(root, target)
    assert ans

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
