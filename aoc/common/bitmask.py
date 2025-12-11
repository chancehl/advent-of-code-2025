class Bitmask:
    def __init__(self, value: int, orig: str = "") -> None:
        self.value = value
        self.orig = orig

    def __str__(self) -> str:
        if self.orig == "":
            return bin(self.value)
        return format(self.value, f"0{len(self.orig)}b")

    @classmethod
    def from_str(cls, s: str, on_char: str = "#", off_char: str = "."):
        bitmask = 0
        for c in s:
            bitmask = (bitmask << 1) | (1 if c == on_char else 0)
        return cls(bitmask, s)

    def create_flipmask(self, positions: list[int]) -> int:
        flipmask = 0
        n = len(self.orig)
        for p in positions:
            translated = (n - 1) - p
            flipmask |= 1 << translated
        return flipmask

    def flip(self, posns: list[int]) -> "Bitmask":
        flipmask = self.create_flipmask(posns)
        new_value = self.value ^ flipmask

        return Bitmask(new_value, self.orig)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Bitmask):
            raise NotImplementedError("unsupported comparison between bitmask")

        return self.value == other.value
