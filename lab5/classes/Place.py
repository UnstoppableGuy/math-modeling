class Place:
    def __init__(self, holding, id=None):
        self.holding = holding
        self.id = id

    def __str__(self):
        return f"#{self.id+1}({self.holding})"

    __repr__ = __str__
