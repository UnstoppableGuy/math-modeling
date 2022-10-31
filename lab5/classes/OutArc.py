class OutArc(Arc):
    def trigger(self):
        self.place.holding -= self.amount

    def non_blocking(self):
        return self.place.holding >= self.amount
