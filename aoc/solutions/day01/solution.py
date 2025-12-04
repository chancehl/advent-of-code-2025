from aoc.common.timer import timed


@timed
def part_one(input_txt: str) -> int:
    zeroes = 0
    posn = 50

    for line in input_txt.splitlines():
        direction, clicks = line[0], int(line[1:])

        if direction == "L":
            posn = (posn - clicks) % 100
        else:
            posn = (posn + clicks) % 100

        if posn == 0:
            zeroes += 1

    return zeroes


@timed
def part_two(input_txt: str) -> int:
    passes = 0
    posn = 50

    for line in input_txt.splitlines():
        direction, clicks = line[0], int(line[1:])

        while clicks > 0:
            new_posn = posn

            if direction == "L" and posn == 0:
                new_posn = 99
            elif direction == "L":
                new_posn = posn - 1
            elif direction == "R" and posn == 99:
                new_posn = 0
            elif direction == "R":
                new_posn = posn + 1

            if new_posn == 0:
                passes += 1

            posn = new_posn
            clicks -= 1

    return passes
