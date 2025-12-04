from aoc.common.timer import timed


@timed
def part_one(input_txt: str) -> int:
    joltage = 0

    for line in input_txt.splitlines():
        batteries = [int(battery) for battery in list(line)]
        print(batteries)

    return joltage


@timed
def part_two(input_txt: str) -> int:
    return -1
