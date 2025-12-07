from aoc.common.timer import timed
import re
import math
from enum import Enum

type CephalapodHomeworkProblem = tuple[list[int], str]


class WorksheetParser(Enum):
    HUMAN = 1
    CEPHALAPOD = 2


@timed
def part_one(input_txt: str) -> int:
    worksheet = parse_worksheet(input_txt, WorksheetParser.HUMAN)

    running_sum = 0

    for operands, sign in worksheet:
        if sign == "+":
            running_sum += sum(operands)
        else:
            running_sum += math.prod(operands)

    return running_sum


@timed
def part_two(input_txt: str) -> int:
    worksheet = parse_worksheet(input_txt, WorksheetParser.CEPHALAPOD)

    running_sum = 0

    for operands, sign in worksheet:
        if sign == "+":
            running_sum += sum(operands)
        else:
            running_sum += math.prod(operands)

    return running_sum


def parse_worksheet(
    input_txt: str, parser: WorksheetParser
) -> list[CephalapodHomeworkProblem]:
    if parser == WorksheetParser.HUMAN:
        return parse_worksheet_like_human(input_txt)
    else:
        return parse_worksheet_like_squid(input_txt)


def parse_worksheet_like_human(input_txt: str) -> list[CephalapodHomeworkProblem]:
    problems = []

    raw_grid = []
    for line in input_txt.splitlines():
        raw_grid.extend([re.findall("\\d+|\\*|\\+", line)])

    for col in range(0, len(raw_grid[0])):
        operands = []
        for row in range(0, len(raw_grid) - 1):
            operand = int(raw_grid[row][col])
            operands.append(operand)
        sign = raw_grid[-1][col]  # last element is always the sign
        problems.append((operands, sign))

    return problems


def parse_worksheet_like_squid(input_txt: str) -> list[CephalapodHomeworkProblem]:
    problems = []

    grid = [list(line) for line in input_txt.splitlines()]

    operand_rows = grid[0 : len(grid) - 1]

    operands = []
    current = []

    for col in range(0, len(operand_rows[0])):
        value = ""

        for row in range(0, len(operand_rows)):
            node = operand_rows[row][col]
            if node != " ":
                value = value + node

        if value == "":
            operands.append(current)
            current = []
        else:
            current.append(int(value))

    # always append the current when we exit the loop
    operands.append(current)

    sign_row = list(filter(lambda v: v != " ", grid[-1]))
    for i in range(0, len(sign_row)):
        problems.append((operands[i], sign_row[i]))

    return problems
