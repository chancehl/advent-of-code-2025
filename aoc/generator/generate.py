import sys
from pathlib import Path

TEMPLATE = """from aoc.common.timer import timed


@timed
def part_one(input_txt: str) -> int:
    return -1


@timed
def part_two(input_txt: str) -> int:
    return -1
"""


def main():
    if len(sys.argv) != 2:
        print("usage: uv run ./generate.py <day>")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
    except ValueError:
        print("day must be an integer")
        sys.exit(1)

    if not (1 <= day <= 25):
        print("day must be between 1 and 25")
        sys.exit(1)

    day_dir = Path(f"./aoc/solutions/day{day:02d}")

    if day_dir.exists():
        raise FileExistsError(f"Directory already exists: {day_dir}")

    # Create directory
    day_dir.mkdir(parents=True)

    # Create solution.py with template
    solution_file = day_dir / "solution.py"
    solution_file.write_text(TEMPLATE)

    # Create empty example.txt
    example_file = day_dir / "example.txt"
    example_file.touch()

    print(f"🎁 Generated placeholder solution files for day {day}. Good luck!")


if __name__ == "__main__":
    main()
