"""
# Adjacency list

ex:
{
  'a': ['b'],
  'b': ['c', 'd'],
  'c': ['a'],
  'd': [],
}

# Edge list
[
  ('a','b'),
  ('b','c'),
  ('b','d'),
  ('c','a'),
]

# Matrix

"""
from collections.abc import Callable

# DFS that (recursively) visits all nodes
def dfs(
        graph: dict[str, list[str]], 
        v: str, 
        cb: Callable[[str], None], 
        visited: set[str]
    ) -> None:

    visited = set() if visited is None else visited
    if v in visited:
        return
    visited.add(v)

    for edge in graph[v]:
        dfs(graph, edge, cb, visited)

    if cb is not None:
        cb(v)

    return

def dfs_it(
        graph: dict[str, list[str]], 
        v: str, 
        cb: Callable[[str], None], 
        visited: set[str]
    ) -> None:
    visited = set() if visited is None else visited
    if v in visited:
        return
    visited.add(v)

    for edge in graph[v]:
        dfs(graph, edge, cb, visited)

    if cb is not None:
        cb(v)
    return


if __name__ == "__main__":
    graph = {
        "a": ["b", "c"],
        "b": ["c", "d", "e"],
        "c": ["d", "g"],
        "d": ["e", "f", "g"],
        "e": ["h"],
        "f": ["h"],
        "g": ["h"],
        "h": [],
    }

    cb = lambda v: print(f"vertex:{v}")
    dfs(graph, "a", cb, set())
