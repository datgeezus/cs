from dataclasses import dataclass
from typing import Callable, TypeVar

T = TypeVar('T')

@dataclass
class Strategy(object):
    callback: Callable[[str, dict, T], None]
    data: T = None

def dfs(node: str, graph: dict, visited: list=None, strategy: Strategy=None):
    visited = [] if visited is None else visited
    if node in visited: return
    visited.append(node)

    if strategy is not None: strategy.callback(node, graph, strategy.data)

    if node in graph:
        for adj in graph[node]:
            dfs(adj, graph, visited, strategy)
    return

def topo_sort(graph: dict):
    def build_path(curr: str, graph: dict, visited:list=None):
        visited.append(curr)
        return
    N = len(graph)
    ordering = ['' for _ in range(N)]
    visited = []
    strategy = Strategy(build_path)
    i = N - 1
    for node in graph:
        if node in visited: continue
        strategy.data = []
        dfs(node, graph, visited, strategy)
        for node in strategy.data:
            ordering[i] = node
            i -= 1
    return ordering


if __name__ == "__main__":
    graph = {
        'a': ['b', 'c', 'd'],
        'b': ['d'],
        'c': ['b', 'd'],
        'd': ['e'],
        'e': []
    }

    strategy = Strategy(callback=lambda n,g,d: print(n), data=None)

    dfs('a', graph, strategy=strategy)
    print(topo_sort(graph))