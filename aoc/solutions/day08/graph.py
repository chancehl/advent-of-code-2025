from aoc.common.euclid import Coordinates3D
from collections import defaultdict


class JunctionBoxGraph:
    def __init__(self) -> None:
        self._graph = defaultdict(dict)

    def get_vertices(self) -> list[Coordinates3D]:
        return list(self._graph.keys())

    def get_edge(self, u: Coordinates3D, v: Coordinates3D) -> float | None:
        if self.has_edge(u, v):
            return self._graph[u][v]
        return None

    def add_edge(self, u: Coordinates3D, v: Coordinates3D, weight: float):
        self._graph[u][v] = weight
        self._graph[v][u] = weight

    def has_edge(self, u: Coordinates3D, v: Coordinates3D) -> bool:
        if v in list(self._graph[u].keys()):
            return True
        return False

    def get_edges(self, u: Coordinates3D) -> dict[Coordinates3D, float]:
        return self._graph[u]
