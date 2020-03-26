class Wheel:
    def __init__(self, name, working, max_eff, starting = 0.4, shutdown = 1.40):
        """Wind wheel.

        WORKING is working speed. MAX_EFF is effectiveness at WORKING
        speed.  STARTING is starting speed in ratio to WORKING.
        SHUTDOWN is turn-off speed in percentage to WORKING. """

        self.name = name
        assert working > 0
        self.working = working
        assert max_eff > 0 and max_eff < 1
        self.max_eff = max_eff
        assert starting > 0 and starting < 1
        self.starting = starting
        assert shutdown > 1
        self.shutdown = shutdown

    def __str__(self):
        return "{name} [v={spd}, max_eff={e}]".format(name = self.name, spd = self.working, e = self.max_eff)
        
    def eff(self, speed):
        """Calculates effectiveness at SPEED"""

        # variables
        starting = self.working * self.starting
        shutdown = self.working * self.shutdown
        k = self.max_eff / (self.working - starting)
        b = - k * starting

        # 1: Before starting
        if speed < starting:
            return 0

        # 2: Increasing
        if speed >= starting and speed < self.working:
            return k * speed + b

        # 3: Shutdown
        if speed >= self.working and speed < shutdown:
            return -k * (speed - self.working) + self.max_eff

        # 4: Off
        if speed >= shutdown:
            return 0

    def power(self, speed, rho = 1.2):

        wind_power = rho * (speed ** 3) / 2
        return wind_power * self.eff(speed)
