from math import *
from random import *
import traceback

while True:
    try:
        n = input('Введите количество точек (2<= N <=30): ')
        n = int(n)
    except ValueError:
        if n == '':
            n = 0
        print('n - int')
    else:
        if n < 2: n = 2
        if n > 30: n = 30
        s = []
        for i in range(2*n):
            s.append(uniform(-5,5))
        print('Все координаты', s)
    break

zero = 0
one = 1

Xs = []
Ys = []

while one <= len(s):
    Xs.append(s[one])
    one+=2
print('Координаты Х', Xs)

while zero < len(s):
    Ys.append(s[zero])
    zero+=2
print('Координаты Y', Ys)

sotr = []

kx = 0
kxx = 1
ky = 0
kyy = 1

while kx < len(Xs):
    while kxx < len(Xs):
        while kyy < len(Ys):
            otr = sqrt((Xs[kxx]-Xs[kx])**2 + (Ys[kyy]-Ys[ky])**2)
            sotr.append(otr)
            kxx+=1
            kyy+=1
    kx+=1
    ky+=1
    kxx = kx+1
    kyy = ky+1
print('Отрезки', sotr)

print('Минимальное расстояние между ближайшими точками', min(sotr))


while True:
    try:
        x0 = input('X0: ')
        y0 = input('Y0: ')
        r1 = input('R1: ')
        r2 = input('R2: ')
        x0 = float(x0)
        y0 = float(y0)
        r1 = float(r1)
        r2 = float(r2)
    except ValueError:
        if x0 == '' or y0 == '' or r1 == '' or r2 == '':
            x0 = 0
            y0 = 0
            r1 = 0
            r2 = 0
        print('X0, Y0, R1, R2 - float')
    else:
        if r1 < 0 or r2 < 0:
            print('Радиус должен быть больше 0')
        else:
            kx = 0
            ky = 0
            while kx < len(Xs):
                if Xs[kx] >= x0-r2 and Xs[kx] <= x0+r2:
                    if Ys[ky] > y0 and Ys[ky] <= sqrt(r2 ** 2 - (Xs[kx] - x0)**2)+y0 and Ys[ky] >= sqrt(r1 ** 2 - (Xs[kx] - x0)**2)+y0:
                        print('+')
                    elif Ys[ky] < y0 and Ys[ky] >= sqrt(r2 ** 2 - (Xs[kx] - x0)**2)+y0 and Ys[ky] <= sqrt(r1 ** 2 - (Xs[kx] - x0)**2)+y0:
                        print('+')
                    else:
                        print('-')
                else:
                    print('-')
                kx +=1
                ky +=1
    break

Xs.sort()
print('Координаты точек по возрастанию их абсцисс', Xs)

