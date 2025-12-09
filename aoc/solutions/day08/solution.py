from aoc.common.timer import timed
from aoc.common.euclid import Coordinates3D, compute_distance
from aoc.common.unionfind import UnionFind

import math


@timed
def part_one(input_txt: str) -> int:
    coordinates = parse_input(input_txt)

    return make_connections(coordinates, 1000)


@timed
def part_two(input_txt: str) -> int:
    return -1


def make_connections(coords: list[Coordinates3D], n: int) -> int:
    pairs = {}

    for i in range(0, len(coords)):
        for j in range(0, len(coords)):
            target = (min(i, j), max(i, j))
            if i != j and target not in pairs:
                pairs[target] = compute_distance(coords[i], coords[j])

    # sort connections by distance
    sorted_pairs = sorted(pairs.keys(), key=lambda b: pairs[b])

    # use a union-find (disjoint set) to track circuits
    # - initialize each junction box to its own set
    # - initialize connections to 0
    union_find = UnionFind(len(coords))
    connections = 0

    # - for each pair starting with the shortest circuit:
    #       - if two boxes are in different sets, merge the sets and increment connections count
    #       - if they are in the same set, do nothing
    for i, j in sorted_pairs:
        union_find.union(i, j)
        connections += 1

        if connections == n:
            break

    # - multiply the 3 largest circuits
    circuit_sizes = sorted(union_find.size, reverse=True)
    return math.prod(circuit_sizes[0:3])


def parse_input(input_txt: str) -> list[Coordinates3D]:
    coordinates = []

    for line in input_txt.splitlines():
        parts = line.split(",")
        coordinates.append((int(parts[0]), int(parts[1]), int(parts[2])))

    return coordinates
