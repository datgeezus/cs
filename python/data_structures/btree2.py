
from dataclasses import dataclass
from collections import deque
from collections.abc import Callable
from typing import Generator

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

def bfs(root: Node | None, on_visit: Callable[[str], None] | None = None) -> None:
    if not root:
        return
    q = deque[Node]()
    q.append(root)

    visit = lambda fun, v: fun(v) if fun else None

    while q:
        node = q.popleft()
        visit(on_visit, node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

def level_order(root: Node | None, on_visit: Callable[[int, str],None]) -> None:
    if not root:
        return
    q = deque[Node|None]()
    q.append(root)
    level = 0
    while q:
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            if node is None:
                continue
            on_visit(level, node.value)
            q.append(node.left)
            q.append(node.right)
        level += 1


def in_order(root: Node | None, on_visit: Callable[[str], None]) -> None:
    if not root:
        return
    pre_order(root.left, on_visit)
    on_visit(root.value)
    in_order(root.right, on_visit)

def pre_order(root: Node | None, on_visit: Callable[[str], None]) -> None:
    if not root:
        return
    on_visit(root.value)
    pre_order(root.left, on_visit)
    pre_order(root.right, on_visit)

def post_order(root: Node | None, on_visit: Callable[[str], None]) -> None:
    if not root:
        return
    post_order(root.left, on_visit)
    post_order(root.right, on_visit)
    on_visit(root.value)

def post_order_generator(root: Node | None) -> Generator:
    if not root:
        return
    stack = deque()
    stack.append(root)

    while stack:
        node = stack.pop()
        if node is None:
            continue
        stack.append(node.left)
        yield node.value
        stack.append(node.right)

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

    print("Level Order Traversal")
    print_with_level = lambda level, v: print(f"level:{level}, value:{v}")
    level_order(btree, print_with_level)

    print("DFS pre order")
    pre_order(btree, strategy)

    print("DFS in order")
    in_order(btree, strategy)

    print("DFS post order")
    post_order(btree, strategy)

    print("DFS post order (Generator)")
    for node in post_order_generator(btree):
        print(f"node:{node}")
