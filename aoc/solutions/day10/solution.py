from aoc.common.timer import timed
from .ElfMachineManual import ElfMachineManual


@timed
def part_one(input_txt: str) -> int:
    manual = ElfMachineManual(input_txt)
    print(manual)

    return -1


@timed
def part_two(input_txt: str) -> int:
    return -1
