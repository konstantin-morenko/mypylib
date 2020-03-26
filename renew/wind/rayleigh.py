import math

class Rayleigh:
    def __init__(self, name, avr):
        self.name = name
        assert avr > 0
        self.sigma = avr / math.sqrt(math.log(4))
    def prob(self, speed):
        assert speed > 0
        return (speed/self.sigma**2) * math.exp(-(speed**2)/(2*self.sigma**2))
    def avr(self):
        return self.sigma * math.sqrt(math.log(4))
    def __str__(self):
        return "{name} [vmean={v:3.1f}]".format(name = self.name, v = self.avr())

    def speed(self, prob):
        """Calculating speed from distribution function."""

        assert prob < 1
        assert prob > 0

        for speed in [x/10 for x in range(1, 200)]:
            if prob < 1 - math.exp(-(speed**2)/(2*self.sigma**2)):
                return speed - 1
        return 20
