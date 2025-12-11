from aoc.common.timer import timed
from aoc.common.bitmask import Bitmask
from itertools import combinations


@timed
def part_one(input_txt: str) -> int:
    flips = 0

    for line in input_txt.splitlines():
        lights, buttons, _ = parse_instructions(line)
        flips += determine_min_flips(lights, buttons)

    return flips


@timed
def part_two(input_txt: str) -> int:
    return -1


def parse_instructions(s: str) -> tuple[str, list[list[int]], list[int]]:
    parts = s.split(" ")

    # lights
    lights = parts[0].replace("[", "").replace("]", "")

    # buttons
    buttons = [
        [int(value) for value in part.replace("(", "").replace(")", "").split(",")]
        for part in parts[1:-1]
    ]

    # joltages
    joltages = [
        int(value) for value in parts[-1].replace("{", "").replace("}", "").split(",")
    ]

    return (lights, buttons, joltages)


def determine_min_flips(lights: str, buttons: list[list[int]]) -> int:
    min_flips = len(buttons)

    for i in range(1, len(buttons)):
        button_combos = combinations(buttons, i)
        for combo in list(button_combos):
            current_flips = calculate_flips(lights, list(combo))
            if current_flips is not None:
                min_flips = min(min_flips, current_flips)

    return min_flips


def calculate_flips(lights: str, buttons: list[list[int]]) -> int | None:
    target = Bitmask.from_str(lights)
    current = Bitmask.from_str("." * len(lights))

    flips = 0

    for button in buttons:
        current = current.flip(button)
        flips += 1
        if current == target:
            return flips

    return None
