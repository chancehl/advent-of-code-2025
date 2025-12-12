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
├── common/             # Shared utilities
├── api/                # Input fetching
└── generator/          # Template generation
```

## Getting Your Session Token

1. Log into [Advent of Code](https://adventofcode.com)
2. Open browser dev tools (F12)
3. Go to Application/Storage → Cookies
4. Copy the `session` cookie value
5. Add it to your `.env` file

🎅 Merry Christmas! 🎄

## Retrospective

It's December 12th and I've just collected my 24th star - the final for this year. I feel a huge sense of accomplishment because not only is this the first year that I've completed Advent of Code; it's also the first year that I've completed it _on schedule_.

Admittedly, if the number of problems wasn't reduced this year from 25 to 12, I don't think I would have kept going. December always gets crazy and honestly this eats up a lot of my work day anyways (sorry boss). In the past my highest day was 14 and even then those were brute forced, unoptimized, bad solutions. This year I only brute forced a few and those that I did brute force were at least semi-optimized so that the runtime wasn't in the hours.

I'm going to include some data below about the problems I encountered, how long my solutions took to run, and things I learned along the way. This will be full of spoilers!

### Solutions

#### Day 1

**Summary**:

I am so embarassed to say that I struggled for so long with this one. The first part took like 5 minutes (like all day 1 AoC problems do), but the second part kicked my ass. I am almost certain that you can solve the second part with pure maths, but I couldn't figure out all the edge cases. I ended up just simulating the lock turns manually and incrementing a counter and that worked just fine.

**Runtimes**:

< 1ms (part 1), 16ms (part 2)

**Algorithms / keywords**:

Modulo (vs. remainder), math

#### Day 2

**Summary**:

This one was pretty easy, no tricks here. I suspect I could optimize this solution even more but the runtimes are perfectly acceptable for me.

**Runtimes**:

363ms (part 1), 2061ms (part 2)

**Algorithms / keywords**:

Batching

#### Day 3

**Summary**:

This one was fun. I hadn't solved many leetcode problems using greedy algorithms and I considered that kind of a weak area of mine.

**Runtimes**:

<1ms (part 1), 1ms (part 2)

**Algorithms / keywords**:

Greedy algorithms

#### Day 4

**Summary**:

I thought this one would be more difficult than it is after the patrolling robots question from last year. I ended up just simulating the roll movements and that worked just fine.

**Runtimes**:

8ms (part 1), 253ms (part 2)

**Algorithms / keywords**:

Simulation, recursion

#### Day 5

**Summary**:

I've seen variants of this problem before (overlapping meetings in a conference room on leetcode). I had an idea of how to solve it, but did not know there was a named algorithm for this.

**Runtimes**:

1ms (part 1), <1ms (part 2)

**Algorithms / keywords**:

Sweep line algorithm

#### Day 6

**Summary**:

This one wasn't hard, but parsing the input was. You had to think in non-standard reading orders (i.e. not left-to-right, top-to-bottom) and that was uncomfortable for an English speaker.

**Runtimes**:

<1ms (part 1), <1ms (part 2)

**Algorithms / keywords**:

Grid, parsing input

#### Day 7

**Summary**:

This one felt more difficult than it was. The prompt was clear, but it was just a hard one to understand. This is basically a giant pachinko machine.

I actually don't remember if there was any specific trick to this one or not.

**Runtimes**:

1ms (part 1), 1ms (part 2)

**Algorithms / keywords**:

Grid, backtracking

#### Day 8

**Summary**:

I learned a lot with this one, although several people were complaining on Reddit about the prompt being somewhat unclear.

**Runtimes**:

375ms (part 1), 559ms (part 2)

**Algorithms / keywords**:

Kruskal's algorithm, Prim's algorithm, Union find.

#### Day 9

**Summary**:

This one kicked my ass. Bad. I was able to write a class to generate a polgyon and keep track of its shape, but it took so much memory because I was keeping track of all the coordinates in memory.

I asked Copilot to optimize this by having it just keep track of the bounds (rather than the whole shape) and then checking to see if other shapes were within the bounds.

I could definitely still optimize this one further but I am too lazy. This was technically my last problem since I solved part 2 after day 12.

**Runtimes**:

12ms (part 1), 27998ms (part 2)

**Algorithms / keywords**:

Polgyon shape detection

#### Day 10

**Summary**:

Hahahaha oh my god this one made me rage. This was such a difficult math problem, but I suspect someone with a stronger background in math could have figured it out.

I had to have AI help me with this one. It gave up on me pretty fast too. It took like 2 whole prompts for it to be like "you know what, this is pretty hard... you should use a library".

I (luckily!) found a guide on /r/adventofcode on how to "bifurcate your way to victory" which I honestly didn't understand a word of, but it worked.

**Runtimes**:

240ms (part 1), 34863ms (part 2)

**Algorithms / keywords**:

Linear algebra, bifurcation, polynomial equations

#### Day 11

**Summary**:

Back to a sweet, sweet graph problem. Oh how I missed these... This one was easy peasy for me.

**Runtimes**:

733ms (part 1), 98ms (part 2)

**Algorithms / keywords**:

DFS (part 1), Topological sort + dynamic programming (part 2)

#### Day 12

**Summary**:

This one looked insanely difficult on paper. This is like PHD level math difficult. I'm pretty sure people have spent their whole lives writing whitepapers to optimize for fitting shapes inside other shapes like this. We're talking traveling salesman level of difficulty.

However, some kind soul on /r/adventofcode figured out that the input was structured in such a way that this problem was trivial to solve.

I think the creator of AoC put this one in there as a troll. I tried to solve this for the general case but failed and then saw that there was like almost literally a 1 liner you could use to solve it and that worked just fine.

**Runtimes**:

<1ms (part 1)

**Algorithms / keywords**:

Trickery!
