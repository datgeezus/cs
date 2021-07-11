import sys
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
        for (edge,_) in graph[node]:
            dfs(edge, graph, visited, strategy)
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
    for edge in graph:
        if edge in visited: continue
        strategy.data = []
        dfs(edge[0], graph, visited, strategy)
        for node in strategy.data:
            ordering[i] = node
            i -= 1
    return ordering

def shortest_path(graph: dict, start, end=None):
    topo = topo_sort(graph)
    dist = {i:None for i in graph}
    dist[start] = 0
    for idx in topo:
        if dist[idx] is None: continue
        for (edge, w) in graph[idx]:
            new_dist = dist[idx] + w
            if dist[edge] is None: 
                dist[edge] = new_dist
            else:
                dist[edge] = min(dist[edge], new_dist)
    return dist


if __name__ == "__main__":
    # adjacency list with weights
    graph = {
        'a': [('b', 1), ('c', 20), ('d', 5)],
        'b': [('d', 5)],
        'c': [('b', 2), ('d', 8)],
        'd': [('e', 11)],
        'e': []
    }

    strategy = Strategy(callback=lambda n,g,d: print(n), data=None)

    dfs('a', graph, strategy=strategy)
    print(topo_sort(graph))
    print(shortest_path(graph, 'c'))