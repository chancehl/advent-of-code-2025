import dotenv
import os
import pathlib
import requests
import sys

from pathlib import Path


def main():
    dotenv.load_dotenv()

    if len(sys.argv) < 2:
        print("usage: uv run ./aoc/fetch.py <day>")
        sys.exit(1)

    session = os.getenv("AOC_SESSION")
    if session is None or session == "":
        print("missing AOC_SESSION environemnt variable")
        sys.exit(1)

    save = len(sys.argv) >= 3 and sys.argv[2] == "--save"

    day = int(sys.argv[1])
    url = f"https://adventofcode.com/2024/day/{day}/input"

    resp = requests.get(url, cookies={"session": session})
    if resp.status_code != 200:
        print(f"failed to fetch input: {resp.status_code} {resp.text}")
        sys.exit(1)

    if not save:
        print(resp.text)
    else:
        write_input_to_disk(day, resp.text)


def write_input_to_disk(day: int, text: str):
    dir = f"./aoc/days/{day:02d}"
    Path(dir).mkdir(exist_ok=True)

    file_path = Path(dir) / "input.txt"
    with file_path.open("w") as f:
        f.write(text.strip() + "\n")

    print(f"✅ Saved input to {file_path}")


if __name__ == "__main__":
    main()
