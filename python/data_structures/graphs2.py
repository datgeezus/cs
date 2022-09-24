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
from collections import deque

# DFS that (recursively) visits all nodes
def dfs(
        graph: dict[str, list[str]], 
        v: str, 
        on_visit: Callable[[str], None], 
        visited: set[str] | None = None
    ) -> None:

    visited = set() if visited is None else visited
    if v in visited:
        return
    visited.add(v)

    for edge in graph[v]:
        dfs(graph, edge, on_visit, visited)

    on_visit(v)

    return

def dfs_it(
        graph: dict[str, list[str]], 
        v: str, 
        on_visit: Callable[[str], None], 
        visited: set[str] | None = None
    ) -> None:
    visited = set() if visited is None else visited
    if v in visited:
        return
    visited.add(v)

    stack = deque()
    stack.append(v)

    while stack:
        vertex = stack.pop()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

        on_visit(vertex)
    return

def bfs(
        graph: dict[str, list[str]], 
        v: str, 
        on_visit: Callable[[str], None], 
        visited: set[str] | None = None
    ) -> None:
    visited = set() if visited is None else visited
    if v in visited:
        return
    visited.add(v)

    q = deque()
    q.append(v)

    while q:
        vertex = q.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

        on_visit(vertex)
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

    on_visit = lambda v: print(f"vertex:{v}")

    print("Recursive DFS")
    dfs(graph, "a", on_visit)
    print("Iterative DFS")
    dfs_it(graph, "a", on_visit)
    print("BFS")
    bfs(graph, "a", on_visit)
