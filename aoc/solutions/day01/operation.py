class Operation:
    def __init__(self, input: str) -> None:
        self.direction = input[0]
        self.clicks = int(input[1:])

    def __str__(self) -> str:
        return f"{self.direction}{self.clicks}"

    def get_next_value(self, current: int) -> int:
        if self.direction == "L":
            return (current - self.clicks) % 100
        else:
            return (current + self.clicks) % 100

    def get_passes(self, current: int) -> int:
        if current == 0 and self.clicks < 100:
            return 0
        elif self.direction == "L" and (current - self.clicks) <= 0:
            return max(1, abs((current - self.clicks) // 100))
        elif self.direction == "R" and (current + self.clicks) >= 99:
            return max(1, abs((current + self.clicks) // 100))
        else:
            return 0
