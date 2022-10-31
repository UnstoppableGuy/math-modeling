class InArc(Arc):
    def trigger(self):
        self.place.holding += self.amount
