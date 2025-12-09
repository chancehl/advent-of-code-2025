from aoc.common.timer import timed
from aoc.common.euclid import Coordinates3D, compute_distance
from aoc.common.dsu import UnionFind

import heapq


@timed
def part_one(input_txt: str) -> int:
    coordinates = parse_input(input_txt)

    pairs = {}

    for i in range(0, len(coordinates)):
        for j in range(0, len(coordinates)):
            target = (min(i, j), max(i, j))
            if i != j and target not in pairs:
                pairs[target] = compute_distance(coordinates[i], coordinates[j])

    # sort connections by distance
    sorted_pairs = sorted(pairs.keys(), key=lambda b: pairs[b])

    # use a union-find (disjoint set) to track circuits
    # - initialize each junction box to its own set
    # - initialize connections to 0
    union_find = UnionFind(len(coordinates))
    connections = 0

    # - for each pair starting with the shortest circuit:
    #       - if two boxes are in different sets, merge the sets and increment connections count
    #       - if they are in the same set, do nothing
    # - count the sizes of the connected circuits
    # - multiply the 3 largest circuits

    return -1


@timed
def part_two(input_txt: str) -> int:
    return -1


def parse_input(input_txt: str) -> list[Coordinates3D]:
    coordinates = []

    for line in input_txt.splitlines():
        parts = line.split(",")
        coordinates.append((int(parts[0]), int(parts[1]), int(parts[2])))

    return coordinates


def find_set(n: int, all: list[list[int]]) -> tuple[int, list[int]]:
    for i, set in enumerate(all):
        if n in set:
            return (i, set)
    return (-1, [])
