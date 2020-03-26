
"""Accumulating energy."""

class Acc:
    def __init__(self, cap, pwr):
        """Accumulator.

        CAP is the capacity in J.  PWR is the current energy state in
        J.

        """
        assert pwr <= cap
        self.cap = cap
        self.pwr = pwr

    def st(self):
        """Current state in %."""
        return self.pwr / self.cap

    def put(self, pwr):
        """Put energy into accumulator."""
        
        self.pwr += pwr
        if self.pwr > self.cap:
            self.pwr = self.cap

    def get(self, pwr):
        """Get energy from accumulator."""

        if self.pwr >= pwr:
            self.pwr -= pwr
            return pwr
        else:
            pwr = self.pwr
            self.pwr = 0
            return pwr

class Valve(Acc):
    def __init__(self, cap, pwr, level):
        """Valve."""
        assert pwr <= cap
        self.cap = cap
        self.pwr = pwr
        self.level = level
    def flow(self, inflow):
        if inflow >= self.level:
            acc = inflow - self.level
            out = inflow - acc
            self.put(acc)
            return out
        else:
            unload = self.level - inflow
            acc = self.get(unload)
            return inflow + acc
    def __str__(self):
        return "Valve ({}) {}/{}".format(self.level, self.pwr, self.cap)
