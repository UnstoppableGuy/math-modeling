
class Transition:
    def __init__(self, out_arcs, in_arcs):
        self.out_arcs = set(out_arcs)
        self.in_arcs = set(in_arcs)
        self.arcs = self.out_arcs.union(in_arcs)

    def fire(self):
        if self.not_blocked():
            for arc in self.arcs:
                arc.trigger()
            return True
        return False

    def not_blocked(self):
        return all(arc.non_blocking() for arc in self.out_arcs)

    def get_out_arc(self, place):
        return [a for a in self.out_arcs if a.place == place][0]

    def get_in_arc(self, place):
        return [a for a in self.in_arcs if a.place == place][0]

    def __str__(self):
        return f"{list(self.out_arcs)} -> {list(self.in_arcs)}"

    __repr__ = __str__
