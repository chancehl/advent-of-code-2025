class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, value: int) -> int:
        if self.parent[value] == value:
            return value
        else:
            self.parent[value] = self.find(self.parent[value])
            return self.parent[value]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_y] = root_x
