# 🎄 Advent of Code 2025 🎄

A festive Python CLI for solving Advent of Code 2025 challenges.

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Set your Advent of Code session token:
   ```bash
   echo "AOC_SESSION=your_session_token_here" > .env
   ```

## Usage

### Generate a new day's solution template
```bash
uv run -m aoc generate --day 1
```

### Fetch input for a day
```bash
uv run -m aoc fetch --day 1
```

### Execute a solution
```bash
# Run with example input
uv run -m aoc execute --day 1 --part 1 --example

# Run with actual input
uv run -m aoc execute --day 1 --part 1
```

## Project Structure

```
aoc/
├── solutions/          # Daily solution files
│   └── day01/
│       ├── solution.py # Your solution code
│       └── example.txt # Example input
├── common/            # Shared utilities
├── api/              # Input fetching
└── generator/        # Template generation
```

## Getting Your Session Token

1. Log into [Advent of Code](https://adventofcode.com)
2. Open browser dev tools (F12)
3. Go to Application/Storage → Cookies
4. Copy the `session` cookie value
5. Add it to your `.env` file

🎅 Happy coding and may your solutions be merry and bright! 🎄
