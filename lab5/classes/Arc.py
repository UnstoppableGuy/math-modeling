class Arc:
    def __init__(self, place: Place, amount=1):
        self.place = place
        self.amount = amount

    def __str__(self):
        return f"{self.place}" + (f"[{self.amount}]" if self.amount > 1 else "")

    __repr__ = __str__
