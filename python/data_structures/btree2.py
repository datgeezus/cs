
from dataclasses import dataclass
from collections import deque
from collections.abc import Callable

@dataclass
class Node:
    value: str
    left: 'Node | None' = None
    right: 'Node | None' = None


def from_list(nodes_list: list[str]) -> Node | None:
    # create forest, assumen non empty values
    forest = [Node(v) if v else None for v in nodes_list]

    n_nodes = len(nodes_list)

    # connect children
    for i,node in enumerate(forest):
        if node is None:
            continue
        offset = i * 2
        left_i = offset + 1
        right_i = offset + 2
        if left_i < n_nodes:
            node.left = forest[left_i]
        if right_i < n_nodes:
            node.right = forest[right_i]

    return forest[0]

def bfs(root: Node | None, cb: Callable[[str], None] | None = None) -> None:
    if not root:
        return
    q = deque[Node]()
    q.append(root)
    visited = set()


    visit = lambda cb, v: cb(v) if cb else None

    while q:
        node = q.popleft()
        visit(cb, node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


if __name__ == "__main__":
    """
    Building Tree
         A
        / \
       B   C
      / \ / \
     D  E F  G
    """

    strategy = lambda v: print(f"node_value:{v}")
    btree = from_list(["A", "B", "C", "D", "E", "F", "G"])
    print(f"btree: {btree}")

    print("BFS")
    bfs(btree, strategy)
    bfs(btree)

    # print("Level Order Traversal")
    # btree.level_order_traversal(btree.root, strategy)

    # print("DFS pre order")
    # btree.dfs(DfsType.PRE_ORDER, strategy)

    # print("DFS in order")
    # btree.dfs(DfsType.IN_ORDER, strategy)

    # print("DFS post order")
    # btree.dfs(DfsType.POST_ORDER, strategy)
