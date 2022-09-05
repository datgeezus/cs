"""
# Problem:
Given a binary tree root, a node X in the tree is named good if in the path from root to X there
are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

"""

from dataclasses import dataclass


@dataclass
class Node:
    val: int
    left: 'Node | None' = None
    right: 'Node | None' = None


@dataclass
class Context:
    n_nodes: int


def good_nodes(root: Node) -> int:
    if not root:
        return 0
    ctx = Context(0)

    dfs(root, root.val, ctx)
    return ctx.n_nodes

def dfs(root: Node | None, target: int, ctx: Context) -> None:
    if not root:
        return
    if root.val >= target:
        ctx.n_nodes += 1
    new_max = max(target, root.val)
    dfs(root.left, new_max, ctx)
    dfs(root.right, new_max, ctx)

if __name__ == "__main__":
    n1b = Node(1)
    n5 = Node(5)
    n4 = Node(4, n1b, n5)
    n3b = Node(3)
    n1a = Node(1, n3b)
    n3a = Node(3, n1a, n4)
    assert good_nodes(n3a) == 4

    n2 = Node(2)
    n4 = Node(4)
    n3b = Node(3, n4, n2)
    n3a = Node(3, n3b)
    assert good_nodes(n3a) == 3

    assert good_nodes(Node(1)) == 1
