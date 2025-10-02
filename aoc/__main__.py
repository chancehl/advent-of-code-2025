import math
import os
import pathlib
import sys
import click
import dotenv
import requests

from aoc.resolver import resolve_function, resolve_input, resolve_module
from aoc.constants import CHRISTMAS_TREE, SOLUTION_TEMPLATE


@click.group()
def cli():
    pass


@cli.command()
@click.option("--day", type=int, required=True, help="Day number (1-25)")
@click.option("--part", type=int, required=True, help="Part number (1-2)")
@click.option("--example", is_flag=True, help="Use example input")
def execute(day, part, example):
    if day < 1 or day > 25:
        raise ValueError("day argument must be between 1 and 25")

    if part < 1 or part > 2:
        raise ValueError("part must be either 1 or 2")

    module = resolve_module(day)
    solution = resolve_function(module, part)
    input_data = resolve_input(day, example)

    (result, elapsed) = solution(input_data)

    click.echo("🎄Advent of Code 2025 🎄" + "\n" + CHRISTMAS_TREE)
    click.echo(
        f"[year 2025 / day {day} / part {part}]: {result} ({math.floor(elapsed)}ms)"
    )


@cli.command()
@click.option("--day", type=int, required=True, help="Day number (1-25)")
@click.pass_context
def generate(ctx, day):
    if not (1 <= day <= 25):
        click.echo("day must be between 1 and 25")
        sys.exit(1)

    day_dir = pathlib.Path(f"./aoc/solutions/day{day:02d}")

    if day_dir.exists():
        raise FileExistsError(f"Directory already exists: {day_dir}")

    day_dir.mkdir(parents=True)

    solution_file = day_dir / "solution.py"
    solution_file.write_text(SOLUTION_TEMPLATE)

    example_file = day_dir / "example.txt"
    example_file.touch()

    click.echo(f"🎊 Ho ho ho! Day {day} template created! 🎊")
    click.echo("")
    click.echo("Ready to solve? Run this command:")
    click.echo(f"   uv run -m aoc execute --day {day} --part 1 --example")
    click.echo("")
    click.echo("🎅 May your code be merry! 🎄")


@cli.command()
@click.option("--day", type=int, required=True, help="Day number (1-25)")
@click.pass_context
def fetch(ctx, day):
    dotenv.load_dotenv()

    session = os.getenv("AOC_SESSION")
    if session is None or session == "":
        click.echo("missing AOC_SESSION environment variable")
        sys.exit(1)

    url = f"https://adventofcode.com/2024/day/{day}/input"

    resp = requests.get(url, cookies={"session": session})
    if resp.status_code != 200:
        click.echo(f"failed to fetch input: {resp.status_code} {resp.text}")
        ctx.exit(1)

    click.echo(resp.text)


if __name__ == "__main__":
    cli()
