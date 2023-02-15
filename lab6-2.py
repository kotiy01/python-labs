from math import *
from random import *

fh = open("lab4_in.txt", mode="rt")
fo = open("lab4_out.txt", mode="wt")

a = []
for line in fh:
    if line == "\n":
        continue
    a.append(int(line))
n = a[0]
s = []
for i in range(2*n):
    s.append(uniform(-5,5))
fo.write("Все координаты: " + str(s) + "\n")

zero = 0
one = 1

Xs = []
Ys = []

while one <= len(s):
    Xs.append(s[one])
    one+=2
fo.write('Координаты Х: ' + str(Xs) + "\n")

while zero < len(s):
    Ys.append(s[zero])
    zero+=2
fo.write('Координаты Y: ' + str(Ys) + "\n")

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
fo.write('Все отрезки: ' + str(sotr) + "\n")
minotr = min(sotr)

fo.write('Минимальное расстояние между ближайшими точками: ' + str(minotr) + "\n")

fh.close()
fo.close()
