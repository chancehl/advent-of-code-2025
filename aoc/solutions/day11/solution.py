from aoc.common.timer import timed
from aoc.common.graph import Graph
from collections import defaultdict


@timed
def part_one(input_txt: str) -> int:
    graph = make_graph(input_txt)
    return len(graph.generate_paths("you", "out"))


@timed
def part_two(input_txt: str) -> int:
    graph = make_graph(input_txt)

    svr_to_fft = compute_subpaths(graph, "svr")["fft"]
    fft_to_dac = compute_subpaths(graph, "fft")["dac"]
    dac_to_out = compute_subpaths(graph, "dac")["out"]

    return svr_to_fft * fft_to_dac * dac_to_out


def make_graph(input_txt: str) -> Graph:
    graph = Graph()

    for line in input_txt.splitlines():
        parts = line.split(":")
        for vertex in parts[1].strip().split(" "):
            graph.add_edge(parts[0], vertex)

    return graph


def compute_subpaths(graph: Graph, start: str) -> defaultdict[str, int]:
    dp: defaultdict[str, int] = defaultdict(int)
    dp[start] = 1  # there's exactly 1 way to be at the source (you start here)

    for vertex in graph.topological_sort():
        for neighbor in graph.get_neighbors(vertex):
            dp[neighbor] += dp[vertex]

    return dp
