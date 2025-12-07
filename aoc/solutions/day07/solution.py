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
                path = seek_path(matrix, (row, col))
                draw_beam_path(matrix, path)
            elif matrix[row][col] == "^" and matrix[row - 1][col] == "|":
                split_beam(matrix, (row, col))
                splits += 1

    return splits


@timed
def part_two(input_txt: str) -> int:
    matrix = [list(line) for line in input_txt.splitlines()]

    timeline_counts = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    # always mark S as 1 so we hav something to begin computing our triangle
    start_row, start_col = (0, matrix[0].index("S"))
    timeline_counts[start_row][start_col] = 1

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            current_count = timeline_counts[row][col]

            if current_count > 0:
                current_symbol = matrix[row][col]

                if current_symbol == "." or current_symbol == "S":
                    if is_in_bounds(timeline_counts, (row + 1, col)):
                        timeline_counts[row + 1][col] += current_count
                elif current_symbol == "^":
                    # left
                    if is_in_bounds(timeline_counts, (row + 1, col - 1)):
                        timeline_counts[row + 1][col - 1] += current_count
                    # right
                    if is_in_bounds(timeline_counts, (row + 1, col + 1)):
                        timeline_counts[row + 1][col + 1] += current_count

    return sum(timeline_counts[-1])


def seek_path(
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


def is_in_bounds(matrix: list[list[int]], posn: tuple[int, int]) -> bool:
    row, col = posn

    if row < 0 or row > len(matrix) - 1:
        return False
    if col < 0 or col > len(matrix[0]) - 1:
        return False

    return True
