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
        forest = [cls(val) if val else None for val in nodes]
        n = len(forest)
        for i, node in enumerate(forest):
            if node is None: continue
            l_i = (i * 2) + 1
            r_i = (i * 2) + 2
            if l_i >= n: continue
            node.left = forest[l_i]
            if r_i >= n: continue
            node.right = forest[r_i]
        return forest[0]

@dataclass
class GraphNode(Generic[T]):
    val: T
    edges: list[Type["GraphNode"]] = field(default_factory=list)


if __name__ == "__main__":
    print(TreeNode.from_list([1,2,3,None,5,None,4]))
    print(TreeNode.from_list([1,10,4,3,None,7,9,12,8,6,None,None,2]))