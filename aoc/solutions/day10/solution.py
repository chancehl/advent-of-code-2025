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
        total_presses += calculate_required_presses(buttons, joltages)

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

    for i in range(1, len(buttons) + 1):
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


###############################################################################################################

#### ALL CODE BEYOND THIS POINT COMES FROM THIS /R/ADVENTOFCODE POST:
####
#### https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory
####
#### NOT GOING TO LIE, I DON'T UNDERSTAND A WORD OF THIS BLACK MAGIC MATH BULLSHIT
#### I ASKED CHATGPT TO MAP THEIR TERMINOLOGY TO MY OWN AND HELP ME IMPLEMENT WHAT THEY WERE TALKING ABOUT AND
#### BY SOME MIRACLE IT WORKED. I TAKE NO CREDIT.

###############################################################################################################


def generate_successful_button_combos(
    lights: str, buttons: list[list[int]]
) -> list[list[int]]:
    combos = []

    # include full-length combos
    for i in range(1, len(buttons) + 1):
        button_combos = combinations(buttons, i)
        for combo in list(button_combos):
            # calculate_flips now checks final state after all presses
            if calculate_flips(lights, list(combo)) is not None:
                combos.append(combo)

    return combos


def calculate_required_presses(buttons: list[list[int]], joltages: list[int]) -> int:
    if all(i == 0 for i in joltages):
        return 0

    answer = 1_000_000  # arbitrarily high, doesn't matter. we won't take 1 million button presses
    number_of_variables = len(joltages)
    pattern_costs = patterns_from_buttons(buttons, number_of_variables)

    def recurse(goal: tuple[int, ...]) -> int:
        if all(i == 0 for i in goal):
            return 0

        local_answer = answer
        for pattern, pattern_cost in pattern_costs.items():
            # pattern must be <= goal elementwise and parity must match
            if all(p <= g and (p % 2) == (g % 2) for p, g in zip(pattern, goal)):
                new_goal = tuple((g - p) // 2 for p, g in zip(pattern, goal))
                candidate = pattern_cost + 2 * recurse(new_goal)
                if candidate < local_answer:
                    local_answer = candidate

        return local_answer

    return recurse(tuple(joltages))


def patterns_from_buttons(
    buttons: list[list[int]], num_vars: int
) -> dict[tuple[int, ...], int]:
    out: dict[tuple[int, ...], int] = {}
    num_buttons = len(buttons)

    # convert button definitions to coeff tuples (0/1 per variable)
    coeffs = [tuple(int(i in b) for i in range(num_vars)) for b in buttons]

    for pattern_len in range(num_buttons + 1):
        for btn_indices in combinations(range(num_buttons), pattern_len):
            # sum selected coeff tuples elementwise
            pattern = tuple(
                map(sum, zip((0,) * num_vars, *(coeffs[i] for i in btn_indices)))
            )
            if pattern not in out:
                out[pattern] = pattern_len
    return out
