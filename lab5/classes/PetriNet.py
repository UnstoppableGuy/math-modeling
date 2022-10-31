class PetriNet:
    def __init__(self, transitions, marking):
        self.places = list([Place(m, i) for i, m in enumerate(marking)])
        self.transitions = list([
            Transition(
                [OutArc(self.places[i]) for i in outs],
                [InArc(self.places[i]) for i in ins])
            for outs, ins in transitions
        ])
        # print(f"Places: {self.transitions}")
        self.finished = False
        self.markings = [self.get_marking()]

    def get_marking(self):
        return [x.holding for x in self.places]

    def run(self, verbose=False):
        i = 0
        while not self.finished and i < 25:
            current_marking = self._run_once(verbose)
            if not current_marking:
                self.finished = True
                break
            yield current_marking
            i += 1

    def _run_once(self, verbose):
        fired_transitions = set()
        while len(fired_transitions) < len(self.transitions):
            t_num = random.randint(0, len(self.transitions) - 1)
            t = self.transitions[t_num]
            if t.fire():
                if verbose:
                    # display_table([t_num, t, self.get_marking()])
                    # display_table(
                    #     [[str(t_num), str(t), str(self.get_marking())]])
                    print(
                        f"Firing transition {t_num}: {t} \tMarking {self.get_marking()}")
                    # print(f"Current marking {self.get_marking()}")
                return self.get_marking()
            else:
                fired_transitions.add(t_num)
        return None
