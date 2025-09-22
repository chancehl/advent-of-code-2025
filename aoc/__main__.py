import importlib
import sys
import time


def main():
    if len(sys.argv) < 3:
        print("usage: uv run -m aoc <day> <part> (--example)")
        sys.exit(1)

    day = int(sys.argv[1])
    part = int(sys.argv[2])
    example = bool(len(sys.argv) > 3 and sys.argv[3] == "--example")

    if day < 1 or day > 25:
        raise ValueError("day argument must be between 1 and 25")

    if part < 1 or part > 2:
        raise ValueError("part must be either 1 or 2")

    module = importlib.import_module(f"aoc.day{day:02d}")
    func = getattr(module, f"part_{"one" if part == 1 else "two"}")

    start = time.perf_counter()
    result = func(read_input(day, example=example))
    end = time.perf_counter()
    elapsed = (end - start) * 1000  # in ms

    print(f"[year 2025 / day {day} / part {part}]: {result} ({elapsed:.2f}ms)")


def read_input(day: int, **kwargs) -> str:
    use_example = kwargs.get("example", True)

    path = (
        f"./inputs/day{day:02d}.example.txt"
        if use_example
        else f"./inputs/day{day:02d}.txt"
    )

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    main()
