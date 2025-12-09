from aoc.common.timer import timed
from aoc.common.euclid import Coordinates3D, compute_distance
from aoc.common.unionfind import UnionFind

import os
import math

CIRCUIT_SIZE = 10 if os.getenv("EXAMPLE") else 1000


@timed
def part_one(input_txt: str) -> int:
    coords = parse_input(input_txt)

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

        if connections == CIRCUIT_SIZE:
            break

    # - multiply the 3 largest circuits
    circuit_sizes = sorted(union_find.size, reverse=True)
    return math.prod(circuit_sizes[0:3])


@timed
def part_two(input_txt: str) -> int:
    coords = parse_input(input_txt)

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

    last_two = (sorted_pairs[0], sorted_pairs[1])

    # - for each pair starting with the shortest circuit:
    #       - if two boxes are in different sets, merge the sets and increment connections count
    #       - if they are in the same set, do nothing
    # - continue this operation until we have completed the circuit (aka one circuit size == len(coords))
    while not is_completed_circuit(union_find.size, len(coords)):
        for i, j in sorted_pairs:
            if union_find.find(i) != union_find.find(j):
                last_two = (coords[i], coords[j])
            union_find.union(i, j)

    # - multiply the last two X coordinates
    return last_two[0][0] * last_two[1][0]


def parse_input(input_txt: str) -> list[Coordinates3D]:
    coordinates = []

    for line in input_txt.splitlines():
        parts = line.split(",")
        coordinates.append((int(parts[0]), int(parts[1]), int(parts[2])))

    return coordinates


def is_completed_circuit(sizes: list[int], n: int) -> bool:
    for size in sizes:
        if size == n:
            return True
    return False
