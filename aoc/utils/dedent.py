def dedent(input: str) -> str:
    """Dedents a multi-line string by removing all leading and trailing whitespace"""
    trimmed = input.strip()

    lines = []

    for line in trimmed.splitlines():
        lines.append(line.strip())

    return "\n".join(lines)
