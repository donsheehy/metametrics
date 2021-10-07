class Point():
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __iter__(self):
        yield self.x
        yield self.y

    def __eq__(self, other):
        return list(self) == list(other)

    def __hash__(self):
        return hash((self.x, self.y))
