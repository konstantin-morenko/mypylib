import renew.wind.wheel as Wheel
import renew.acc.acc as Acc
import renew.wind.rayleigh as Ray
import random

import argparse
parser = argparse.ArgumentParser(description='Plot power graph')
parser.add_argument('--length', type=int, help='length of calcs', default=200)
parser.add_argument('--capacity', type=int, help='accumulator capacity', default=15000)
parser.add_argument('--output', type=int, help='output energy', default=700)
parser.add_argument('seed', type=int, help='random seed')

args = parser.parse_args()

random.seed(args.seed)


acc = Acc.Valve(args.capacity, args.capacity / 2, args.output)

wheel_list = [Wheel.Wheel("2-blade", 8, 0.47)]

size = 20
avr = 0

rl = Ray.Rayleigh('8 average', 8.0)
wind_lst = [0.1]

for i in range(0, args.length):
    wind_lst.append(rl.nxt(wind_lst[-1]))

with open('pwr.dat', 'w') as f:
    for wind in wind_lst:
        pwr = 0
        for wheel in wheel_list:
            wind_pwr = wheel.power(wind) * size
            pwr += acc.flow(wind_pwr)
        f.write("{:.1f} {:.0f} {:.0f} {:.0f}\n".format(wind, wind_pwr, pwr, acc.pwr))

with open('plot.gnuplot', 'w') as f:
    f.write("""set term png
    set output 'pwr.png'
    set title 'Мощность ветра, мощность на выходе и запас энергии в аккумуляторе (зерно={seed}, длина={length})'
    set xlabel 'Точки во времени'
    set ylabel 'Мощность ветра и на выходе'
    set y2tics 0, 1000
    set y2label 'Энергия в аккумуляторе'
    set terminal png size 2000, 1000
    set ytics nomirror
    plot 'pwr.dat' using 0:2 with line title 'Мощность ветра' axis x1y1, \
    'pwr.dat' using 0:3 with line title 'Мощность на выходе ({out_pwr})' axis x1y1, \
    'pwr.dat' using 0:4 with line title 'Энергия в аккумуляторе (емкость={acc_cap})' axis x1y2
    set output""".format(seed=args.seed, length=args.length, out_pwr=args.output, acc_cap=args.capacity))



