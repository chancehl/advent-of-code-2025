from aoc.common.timer import timed
from .operation import Operation

LEFT = "L"
RIGHT = "R"


@timed
def part_one(input_txt: str) -> int:
    zeroes = 0
    current = 50

    for line in input_txt.splitlines():
        operation = Operation(line)
        next = operation.get_next_value(current)

        if next == 0:
            zeroes += 1

        current = next

    return zeroes


@timed
def part_two(input_txt: str) -> int:
    total_passes = 0
    current = 50

    for line in input_txt.splitlines():
        operation = Operation(line)

        next = operation.get_next_value(current)
        passes = operation.get_passes(current)

        total_passes += passes
        current = next

    return total_passes



