import importlib
import sys


def resolve_module(day: int):
    """
    Imports the solution module for the specified Advent of Code day.

    Args:
        day (int): The day number to resolve (e.g., 1 for day 01).

    Returns:
        module: The imported solution module for the given day.

    Exits:
        If the module cannot be found, prints an error and exits the program.
    """
    module_name = f"aoc.days.{day:02d}.solution"

    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError as ex:
        print(f"[error] Could not load module {module_name} ({ex.msg})")
        sys.exit(1)


def resolve_function(module, part: int):
    """
    Retrieves the function for the specified part from the given module.

    Args:
        module: The module object containing the solution functions.
        part (int): The part number (1 or 2).

    Returns:
        function: The function object for the specified part.

    Exits:
        If the function cannot be found, prints an error and exits the program.
    """
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
    """
    Loads the input or example file for the specified Advent of Code day.

    Args:
        day (int): The day number to resolve (e.g., 1 for day 01).
        use_example (bool, optional): If True, loads the example file; otherwise, loads the input file. Defaults to False.

    Returns:
        str: The contents of the input or example file as a string.
    """
    path = ""

    if use_example:
        path = f"./aoc/days/{day:02d}/example.txt"
    else:
        path = f"./aoc/days/{day:02d}/input.txt"

    with open(path, "r", encoding="utf-8") as f:
        return f.read()
