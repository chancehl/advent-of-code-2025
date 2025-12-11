from aoc.common.timer import timed
from aoc.common.graph import Graph


@timed
def part_one(input_txt: str) -> int:
    graph = make_graph(input_txt)
    return len(graph.generate_paths("you", "out"))


@timed
def part_two(input_txt: str) -> int:
    return -1


def make_graph(input_txt: str) -> Graph:
    graph = Graph()

    for line in input_txt.splitlines():
        parts = line.split(":")
        for vertex in parts[1].strip().split(" "):
            graph.add_edge(parts[0], vertex)

    return graph
