import math
import random

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

    def nxt(self, speed):
        spd_lst = []
        for i in [x/10 for x in range(-10, 10)]:
            spd_nxt = speed + i
            if spd_nxt <= 0:
                spd_nxt = 0.1
            spd_lst.append({'spd': spd_nxt, 'prob': self.prob(spd_nxt) / 10})
        # Normalizing
        summ = sum([x['prob'] for x in spd_lst])
        for spd in spd_lst:
            spd['prob'] /= summ
        # Random number
        rnd = random.random()
        summ = 0
        i = 0
        while summ < rnd:
            summ += spd_lst[i]['prob']
            i += 1
        return spd_lst[i-1]['spd']
