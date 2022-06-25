import sys
from dataclasses import dataclass, field
from typing import Callable, Generic, Type, TypeVar, Union

T = TypeVar("T")


@dataclass
class Strategy:
    callback: Callable[[str, dict, T], None]
    data: T = None


@dataclass
class GraphNode(Generic[T]):
    val: T
    edges: list[Type["GraphNode"]] = field(default_factory=list)


@dataclass
class TopoSortData:
    ordered: list
    index: int


def dfs(node: str, graph: dict, visited: list = None, strategy: Strategy = None):
    visited = [] if visited is None else visited
    if node in visited:
        return
    visited.append(node)

    for (edge, _) in graph[node]:
        dfs(edge, graph, visited, strategy)

    if strategy is not None:
        strategy.callback(node, graph, strategy.data)
    return


def topo_sort(graph: dict):
    def build_path(curr: str, graph: dict, data: TopoSortData = None):
        data.ordered[data.index] = curr
        data.index -= 1
        return

    N = len(graph)
    ordering = ["" for _ in range(N)]
    visited = []
    i = N - 1
    strategy = Strategy(build_path, TopoSortData(ordering, i))
    for edge in graph:
        if edge in visited:
            continue
        dfs(edge, graph, visited, strategy)
    return ordering


def shortest_path(graph: dict, start, end=None) -> Union[int, list]:
    topo = topo_sort(graph)
    dist = {i: None for i in graph}
    dist[start] = (0, start)
    for idx in topo:
        if dist[idx] is None:
            continue
        for (edge, w) in graph[idx]:
            new_dist = (dist[idx][0] + w, idx)
            if dist[edge] is None:
                dist[edge] = new_dist
            else:
                dist[edge] = min(dist[edge], new_dist)
    return dist[end] if end is not None else dist


if __name__ == "__main__":
    # adjacency list with weights
    graph = {
        "a": [("b", 3), ("c", 6)],
        "b": [("c", 4), ("d", 4), ("e", 11)],
        "c": [("d", 8), ("g", 11)],
        "d": [("e", -4), ("f", 5), ("g", 2)],
        "e": [("h", 9)],
        "f": [("h", 1)],
        "g": [("h", 2)],
        "h": [],
    }

    strategy = Strategy(callback=lambda n, g, d: print(n), data=None)

    dfs("a", graph, strategy=strategy)
    print(f"Topological sort of graph is :{topo_sort(graph)}")
    print(f"The shortest paths from c are: {shortest_path(graph, 'c')}")
    print(f"The shortest distances from a are: {shortest_path(graph, 'a')}")
    paths = shortest_path(graph, "a")
    start = "a"
    x = "h"
    y = paths[x][1]
    while start != y:
        print(f"{x}->{y}")
        x = y
        y = paths[x][1]
    print(f"{x}->{start}")

    print(f"The shortest distance from a to h is: {shortest_path(graph, 'a', 'h')[0]}")
