import renew.wind.wheel as Wheel
import renew.acc.acc as Acc
import renew.wind.rayleigh as Ray

acc = Acc.Valve(15000, 4000, 700)

wheel_list = [Wheel.Wheel("2-blade", 8, 0.47)]

size = 20
avr = 0

rl = Ray.Rayleigh('8 average', 8.0)
wind_lst = [0.1]

for i in range(0, 2000):
    wind_lst.append(rl.nxt(wind_lst[-1]))

for wind in wind_lst:
    pwr = 0
    for wheel in wheel_list:
        wind_pwr = wheel.power(wind) * size
        pwr += acc.flow(wind_pwr)
    print("{:.1f} {:.0f} {:.0f} {:.0f}".format(wind, wind_pwr, pwr, acc.pwr))


