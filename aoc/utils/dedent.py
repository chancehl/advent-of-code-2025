def dedent(input: str) -> str:
    """Dedents a multi-line string by removing all leading and trailing whitespace"""
    return "\n".join([line.strip() for line in input.splitlines() if line != ""])
