from aoc.common.timer import timed
from aoc.common.euclid import Coordinates2D, compute_area

from itertools import combinations


@timed
def part_one(input_txt: str) -> int:
    coords = parse_coordinates(input_txt)

    max_area = 0

    coord_combinations = list(combinations(coords, 2))
    for x, y in coord_combinations:
        max_area = max(max_area, compute_area(x, y))

    return max_area


@timed
def part_two(input_txt: str) -> int:
    return -1


def parse_coordinates(input_txt: str) -> list[Coordinates2D]:
    coords = []

    for line in input_txt.splitlines():
        parts = line.split(",")
        coords.append((int(parts[0]), int(parts[1])))

    return coords
