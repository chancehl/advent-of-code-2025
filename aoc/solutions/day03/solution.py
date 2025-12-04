from aoc.common.timer import timed


@timed
def part_one(input_txt: str) -> int:
    joltage = 0

    for line in input_txt.splitlines():
        batteries = [int(battery) for battery in list(line)]

        jolts = greedily_pick_largest(batteries, 2)
        joltage += jolts

    return joltage


@timed
def part_two(input_txt: str) -> int:
    joltage = 0

    for line in input_txt.splitlines():
        batteries = [int(battery) for battery in list(line)]

        jolts = greedily_pick_largest(batteries, 12)
        joltage += jolts

    return joltage


def greedily_pick_largest(nums: list[int], n: int) -> int:
    chosen = ""

    while n > 0:
        # you can only select certain batteries here...
        # example 8119, n = 2. largest is technically 9
        # but that's not a valid choice because there's not
        # anoter digit following it.
        (start, end) = (0, len(nums)) if n == 1 else (0, len(nums) - (n - 1))

        value = max(nums[start:end])
        index = nums.index(value)

        chosen = chosen + str(value)

        nums = nums[index + 1 :]
        n -= 1

    return int(chosen)
