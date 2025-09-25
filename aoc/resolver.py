import importlib
import sys
import os


def resolve_module(day: int):
    module_name = f"aoc.days.{day:02d}.solution"

    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError as ex:
        print(f"[error] Could not load module {module_name} ({ex.msg})")
        sys.exit(1)


def resolve_function(module, part: int):
    function_name = ""

    if part == 1:
        function_name = "part_one"
    else:
        function_name = "part_two"

    try:
        return getattr(module, function_name)
    except AttributeError as ex:
        print(f"[error] could not load function {function_name}(...) ({ex})")
        sys.exit(1)


def resolve_input(day: int, use_example: bool = False) -> str:
    path = ""

    if use_example:
        path = f"./aoc/days/{day:02d}/example.txt"
    else:
        path = f"./aoc/days/{day:02d}/input.txt"

    if not os.path.exists(path):
        print(f"[error] file does not exist at {path}")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()
