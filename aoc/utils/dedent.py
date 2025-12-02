def dedent(input: str) -> str:
    return "\n".join([line.strip() for line in input.splitlines() if line != ""])