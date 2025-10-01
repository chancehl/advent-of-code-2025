from itertools import combinations

from aoc.common.datastructs.matrix import make_matrix
from aoc.common.timer import timed


ASCENDING = 1
DESCENDING = 2


@timed
def part_one(input: str) -> int:
    safe = 0

    for list in make_matrix(input):
        if is_safe(list):
            safe += 1

    return safe


@timed
def part_two(input: str) -> int:
    safe = 0

    for list in make_matrix(input):
        if is_safe_with_dampener(list):
            safe += 1

    return safe


def is_safe(values: list[int]) -> bool:
    direction = get_direction(values)

    for i in range(0, len(values) - 1):
        curr = values[i]
        next = values[i + 1]

        if direction == ASCENDING and curr > next:
            return False

        if direction == DESCENDING and curr < next:
            return False

        diff = abs(curr - next)

        if diff < 1 or diff > 3:
            return False

    return True


def is_safe_with_dampener(values: list[int]) -> bool:
    lists = combinations(values, len(values) - 1)

    for l in lists:
        if is_safe(list(l)):
            return True

    return False


def get_direction(values: list[int]) -> int:
    if len(values) < 2:
        raise ValueError("list must be greater than size 2")
    elif values[0] < values[1]:
        return ASCENDING
    else:
        return DESCENDING
