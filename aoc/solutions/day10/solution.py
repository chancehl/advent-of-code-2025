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
    total_presses = 0

    for line in input_txt.splitlines():
        _, buttons, joltages = parse_instructions(line)

        presses = solve_machine(buttons, joltages)

        if presses is not None:
            total_presses += sum(presses)

    return total_presses


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


def build_counter_register(buttons: list[list[int]], n: int) -> dict[int, list[int]]:
    register = {}

    for i in range(0, n):
        affectors = []

        for j, button in enumerate(buttons):
            if i in button:
                affectors.append(j)

        register[i] = affectors

    return register


def solve_machine(buttons: list[list[int]], targets: list[int]) -> list[int] | None:
    register = build_counter_register(buttons, len(targets))

    presses = [0] * len(buttons)
    counters = [0] * len(targets)

    best = {"total": float("inf"), "presses": None}

    search(0, buttons, presses, counters, register, targets, 0, best)

    return best["presses"]


def search(
    button_index: int,
    buttons: list[list[int]],
    presses: list[int],
    counters: list[int],
    register: dict[int, list[int]],
    targets: list[int],
    presses_so_far: int,
    best: dict,
) -> None:
    # BASE CASE
    if button_index == len(presses):
        if counters == targets and presses_so_far < best["total"]:
            best["total"] = presses_so_far
            best["presses"] = presses.copy()
        return

    b = button_index

    if buttons[b]:
        max_k = min(targets[i] for i in buttons[b])
    else:
        max_k = 0

    for k in range(0, max_k + 1):
        presses[b] = k

        # apply k presses
        for affected in buttons[b]:
            counters[affected] += k

        new_total = presses_so_far + k

        # bounding
        if new_total >= best["total"]:
            # undo and break — more k will only be worse
            for affected in buttons[b]:
                counters[affected] -= k
            presses[b] = 0
            return

        # prune overflow
        if any(counters[i] > targets[i] for i in range(len(counters))):
            for affected in buttons[b]:
                counters[affected] -= k
            presses[b] = 0
            continue

        # recurse
        search(b + 1, buttons, presses, counters, register, targets, new_total, best)

        # undo
        for affected in buttons[b]:
            counters[affected] -= k
        presses[b] = 0
