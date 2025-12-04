from aoc.common.timer import timed


@timed
def part_one(input_txt: str) -> int:
    joltage = 0

    for line in input_txt.splitlines():
        batteries = [int(battery) for battery in list(line)]

        max_value = max(batteries[0 : len(batteries) - 1])
        max_index = batteries.index(max_value)

        local_max = -1

        for index in range(max_index + 1, len(batteries)):
            local_max = max(local_max, batteries[index])

        battery_joltage = int(f"{max_value}{local_max}")
        joltage += battery_joltage

    return joltage


@timed
def part_two(input_txt: str) -> int:
    return -1


def get_max_index(nums: list[int]) -> int:
    """Returns the index of a max value in a list of nums (**important**: it cannot be the last number)"""
    max_value = max(nums[0 : len(nums) - 1])

    return nums.index(max_value)
