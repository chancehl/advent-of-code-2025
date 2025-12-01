from aoc.common.timer import timed


@timed
def part_one(input_txt: str) -> int:
    zeroes = 0
    current = 50

    for operation in input_txt.splitlines():
        direction = operation[0]
        clicks = int(operation[1:])

        next_value = get_next_value(current, direction, clicks)

        if next_value == 0:
            zeroes += 1

        current = next_value

    return zeroes


@timed
def part_two(input_txt: str) -> int:
    passes = 0
    current = 50

    for operation in input_txt.splitlines():
        direction = operation[0]
        clicks = int(operation[1:])

        next_value = get_next_value(current, direction, clicks)

        if direction == "L" and next_value >= current:
            passes += 1
        elif direction == "R" and next_value <= current:
            passes += 1

        current = next_value

    return passes


def get_next_value(current: int, direction: str, clicks: int) -> int:
    if direction == "L":
        return (current - clicks) % 100
    else:
        return (current + clicks) % 100
