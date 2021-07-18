from dataclasses import dataclass, field
from typing import Generic, TypeVar, Type, List
from queue import Queue

T = TypeVar('T')

@dataclass
class TreeNode(Generic[T]):
    val: T
    left: Type["TreeNode"] = None
    right: Type["TreeNode"] = None

    @classmethod
    def from_list(cls, nodes: List):
        forest = [cls(val) for val in nodes]
        count = len(forest)
        for index, tree in enumerate(forest):
            left_index = 2 * index + 1
            if left_index < count:
                node = forest[left_index]
                if node.val is None: continue
                tree.left = node
            right_index = 2 * index + 2
            if right_index < count:
                node = forest[right_index]
                if node.val is None: continue
                tree.right = node
        return forest[0]

@dataclass
class GraphNode(Generic[T]):
    val: T
    edges: list[Type["GraphNode"]] = field(default_factory=list)


if __name__ == "__main__":
    nodes = [1,10,4,3,None,7,9,12,8,6,None,None,2]
    r = TreeNode.from_list(nodes)
    print(r)