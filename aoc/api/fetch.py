import dotenv
import os
import requests
import sys


def main():
    dotenv.load_dotenv()

    if len(sys.argv) < 2:
        print("usage: uv run ./aoc/fetch.py <day>")
        sys.exit(1)

    session = os.getenv("AOC_SESSION")
    if session is None or session == "":
        print("missing AOC_SESSION environemnt variable")
        sys.exit(1)

    day = int(sys.argv[1])
    url = f"https://adventofcode.com/2024/day/{day}/input"

    resp = requests.get(url, cookies={"session": session})
    if resp.status_code != 200:
        print(f"failed to fetch input: {resp.status_code} {resp.text}")
        sys.exit(1)

    print(resp.text)


if __name__ == "__main__":
    main()
