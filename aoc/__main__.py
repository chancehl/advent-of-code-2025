import sys
import time
import math

from aoc.resolver import resolve_function, resolve_input, resolve_module
from aoc.constants import CHRISTMAS_TREE


def main():
    if len(sys.argv) < 3:
        print("usage: uv run -m aoc <day> <part> (--example)")
        sys.exit(1)

    day = int(sys.argv[1])
    part = int(sys.argv[2])
    example = bool(len(sys.argv) > 3 and sys.argv[3] == "--example")

    if day < 1 or day > 25:
        raise ValueError("day argument must be between 1 and 25")

    if part < 1 or part > 2:
        raise ValueError("part must be either 1 or 2")

    (result, elapsed) = execute_solution(day, part, example)

    print("🎄Advent of Code 2025 🎄" + "\n" + CHRISTMAS_TREE)
    print(f"[year 2025 / day {day} / part {part}]: {result} ({math.floor(elapsed)}ms)")


def execute_solution(day: int, part: int, example: bool) -> tuple[int, float]:
    module = resolve_module(day)
    solution = resolve_function(module, part)
    input = resolve_input(day, example)

    start = time.perf_counter()
    result = solution(input)
    end = time.perf_counter()

    return (result, (end - start) * 1000)


if __name__ == "__main__":
    main()
