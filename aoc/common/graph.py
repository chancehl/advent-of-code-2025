from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.edges: defaultdict[str, list[str]] = defaultdict(list[str])

    def add_edge(self, a: str, b: str):
        if not self.has_edge(a, b):
            self.edges[a].append(b)

    def has_edge(self, a: str, b: str):
        return b in self.edges[a]

    def get_neighbors(self, a: str) -> list[str]:
        return self.edges[a]

    def generate_paths(self, start: str, end: str) -> list[list[str]]:
        paths = []

        current_path = []

        def dfs(
            current_node: str,
            end_node: str,
            current_path: list[str],
            all_paths: list[list[str]],
        ) -> None:
            current_path.append(current_node)

            if current_node == end_node:
                all_paths.append(list(current_path))
            else:
                for neighbor in self.get_neighbors(current_node):
                    if neighbor not in current_path:
                        dfs(neighbor, end_node, current_path, all_paths)

            current_path.pop()

        dfs(start, end, current_path, paths)

        return paths
