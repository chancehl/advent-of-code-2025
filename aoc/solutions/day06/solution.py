from aoc.common.timer import timed
import re
import math

type CephalapodHomeworkProblem = tuple[list[int], str]


@timed
def part_one(input_txt: str) -> int:
    worksheet = parse_worksheet(input_txt)

    running_sum = 0

    for operands, sign in worksheet:
        if sign == "+":
            running_sum += sum(operands)
        else:
            running_sum += math.prod(operands)

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
            operand = int(raw_grid[row][col])
            operands.append(operand)
        sign = raw_grid[-1][col] # last element is always the sign
        problems.append((operands, sign))

    return problems
