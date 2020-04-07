set term png
set output 'test.png'
set xlabel "Точки во времени"
set ylabel "Мощность"
set y2tics 0, 1000
set y2label "Энергия в аккумуляторе"
set terminal png size 3000, 1000
set ytics nomirror
plot 'test.csv' using 0:2 with line title 'Мощность ветра' axis x1y1, \
     'test.csv' using 0:3 with line title 'Мощность на выходе' axis x1y1, \
     'test.csv' using 0:4 with line title 'Энергия в аккумуляторе' axis x1y2
set output
