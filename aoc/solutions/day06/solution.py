from aoc.common.timer import timed
import re
import math

type CephalapodHomeworkProblem = tuple[list[int], str]


@timed
def part_one(input_txt: str) -> int:
    worksheet = parse_worksheet(input_txt)

    running_sum = 0

    for problem in worksheet:
        if problem[1] == "+":
            running_sum += sum(problem[0])
        else:
            running_sum += math.prod(problem[0])

    return running_sum


@timed
def part_two(input_txt: str) -> int:
    return -1


def parse_worksheet(input_txt: str) -> list[CephalapodHomeworkProblem]:
    problems = []

    raw_grid = []
    for line in input_txt.splitlines():
        raw_grid.extend([re.findall("\\d+|\\*|\\+", line)])

    for col in range(0, len(raw_grid[0])):
        operands = []
        for row in range(0, len(raw_grid) - 1):
            operands.append(int(raw_grid[row][col]))
        problems.append((operands, raw_grid[-1][col]))

    return problems
