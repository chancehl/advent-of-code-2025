from collections import defaultdict, deque


class Graph:
    def __init__(self) -> None:
        self.edges: defaultdict[str, list[str]] = defaultdict(list[str])

    def add_edge(self, a: str, b: str):
        if not self.has_edge(a, b):
            self.edges[a].append(b)

            if b not in self.edges:
                self.edges[b] = []

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

    def topological_sort(self) -> list[str]:
        # calculate in degrees
        in_degrees = {}
        for vertex in self.edges:
            connected = filter(
                lambda edges: any([vertex in value for value in edges]),
                self.edges.values(),
            )
            in_degrees[vertex] = len(list(connected))

        # initialize all vertices that have an in degree of 0
        queue = deque(
            list(filter(lambda vertex: in_degrees[vertex] == 0, in_degrees.keys()))
        )

        results = []

        while queue:
            current = queue.pop()
            results.append(current)

            for neighbor in self.get_neighbors(current):
                in_degrees[neighbor] -= 1

                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(self.edges.keys()) != len(results):
            raise ValueError(
                "topological sort is not possible because there is a cycle in the graph"
            )

        return results
