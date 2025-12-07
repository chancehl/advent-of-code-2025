from aoc.common.timer import timed


@timed
def part_one(input_txt: str) -> int:
    matrix = [list(line) for line in input_txt.splitlines()]

    splits = 0

    for row in range(1, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == "." and (
                matrix[row - 1][col] == "S" or matrix[row - 1][col] == "|"
            ):
                path = seek_splitter(matrix, (row, col))
                draw_beam_path(matrix, path)
            elif matrix[row][col] == "^" and matrix[row - 1][col] == "|":
                split_beam(matrix, (row, col))
                splits += 1

    return splits


@timed
def part_two(input_txt: str) -> int:
    return -1


def seek_splitter(
    matrix: list[list[str]], starting_posn: tuple[int, int]
) -> list[tuple[int, int]]:
    current_row = starting_posn[0]

    path = []

    while current_row < len(matrix) - 1:
        if matrix[current_row][starting_posn[1]] == "^":
            return path
        else:
            path.append((current_row, starting_posn[1]))
            current_row += 1

    return path


def draw_beam_path(matrix: list[list[str]], path: list[tuple[int, int]]):
    for row, col in path:
        if matrix[row][col] == ".":
            matrix[row][col] = "|"


def split_beam(matrix: list[list[str]], splitter_posn: tuple[int, int]):
    row, col = splitter_posn

    if matrix[row][col - 1] == ".":
        matrix[row][col - 1] = "|"
    if matrix[row][col + 1] == ".":
        matrix[row][col + 1] = "|"
