from collections import deque
from dataclasses import dataclass
from enum import Enum, unique, auto
from typing import Callable, Generic, List, Type, TypeVar

T = TypeVar("T")


@dataclass
class BTreeNode(Generic[T]):
    val: T = None
    left: Type["BTreeNode"] = None
    right: Type["BTreeNode"] = None


@dataclass
class BTreeStrategyData:
    data: T = None


@dataclass
class BTreeStrategy:
    apply: Callable[[T, BTreeStrategyData], None]
    data: BTreeStrategyData = None


@unique
class DfsType(Enum):
    PRE_ORDER = auto()
    IN_ORDER = auto()
    POST_ORDER = auto()


@dataclass
class BTree(Generic[T]):
    root: BTreeNode

    @classmethod
    def from_list(cls, nodes: List[T]) -> Type["BTree"]:
        forest = [BTreeNode(val) if val else None for val in nodes]
        n = len(forest)
        for i, node in enumerate(forest):
            if node is None:
                continue
            l_i = (i * 2) + 1
            r_i = (i * 2) + 2
            if l_i >= n:
                continue
            node.left = forest[l_i]
            if r_i >= n:
                continue
            node.right = forest[r_i]
        return cls(forest[0])

    def dfs(self, dfs_type: DfsType, strategy: BTreeStrategy):
        if dfs_type == DfsType.PRE_ORDER:
            return BTree.dfs_pre_order(self.root, strategy)
        elif dfs_type == DfsType.IN_ORDER:
            return BTree.dfs_in_order(self.root, strategy)
        elif dfs_type == DfsType.POST_ORDER:
            return BTree.dfs_post_order(self.root, strategy)
        else:
            raise ValueError

    @staticmethod
    def dfs_in_order(root: BTreeNode, strategy: BTreeStrategy):
        if root is None:
            return
        BTree.dfs_in_order(root.left, strategy)
        strategy.apply(root.val, strategy.data)
        BTree.dfs_in_order(root.right, strategy)

    @staticmethod
    def dfs_pre_order(root: BTreeNode, strategy: BTreeStrategy):
        if root is None:
            return
        strategy.apply(root.val, strategy.data)
        BTree.dfs_pre_order(root.left, strategy)
        BTree.dfs_pre_order(root.right, strategy)

    @staticmethod
    def dfs_post_order(root: BTreeNode, strategy: BTreeStrategy):
        if root is None:
            return
        BTree.dfs_post_order(root.left, strategy)
        BTree.dfs_post_order(root.right, strategy)
        strategy.apply(root.val, strategy.data)

    @staticmethod
    def bfs(root: BTreeNode, strategy: BTreeStrategy):
        if root is None:
            return
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            strategy.apply(curr.val, strategy.data)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

    @staticmethod
    def level_order_traversal(root: BTreeNode, strategy: BTreeStrategy):
        if root is None:
            return
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                if curr is None:
                    continue
                strategy.apply(curr.val, strategy.data)
                q.append(curr.left)
                q.append(curr.right)


if __name__ == "__main__":
    """
    Building Tree
         A
        / \
       B   C
      / \ / \
     D  E F  G
    """

    strategy = BTreeStrategy(lambda node_value, _: print(node_value), "")
    btree = BTree.from_list(["A", "B", "C", "D", "E", "F", "G"])

    print("BFS")
    btree.bfs(btree.root, strategy)

    print("Level Order Traversal")
    btree.level_order_traversal(btree.root, strategy)

    print("DFS pre order")
    btree.dfs(DfsType.PRE_ORDER, strategy)

    print("DFS in order")
    btree.dfs(DfsType.IN_ORDER, strategy)

    print("DFS post order")
    btree.dfs(DfsType.POST_ORDER, strategy)
