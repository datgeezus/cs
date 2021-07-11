from dataclasses import dataclass, field
from typing import Generic, TypeVar, Type

T = TypeVar('T')

@dataclass
class TreeNode(Generic[T]):
    val: T
    left: Type["TreeNode"] = None
    right: Type["TreeNode"] = None

@dataclass
class GraphNode(Generic[T]):
    val: T
    edges: list[Type["GraphNode"]] = field(default_factory=list)