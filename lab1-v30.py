from math import *
a = float(input('Введите значение a: '))
z1 = (sin(a)**4 + 2*sin(a)*cos(a) - cos(a)**4) / (tan(2*a) - 1)
print("{0:.4f} {1:.4f}".format(a, z1))
z2 = cos(2*a)
print("{0:.4f} {1:.4f}".format(a, z2))
