from math import *
import traceback

while True:
    try:
        a = input('Введите значение a: ')
        a = float(a)
    except ValueError:
        if a == '':
            a = 0
        print('a - float')
    else:
        if tan(2*a) - 1 == 0:
            print('Нельзя делить на 0')
        else:
            z1 = (sin(a)**4 + 2*sin(a)*cos(a) - cos(a)**4) / (tan(2*a) - 1)
            print("{0:.2f} {1:.4f}".format(a, z1))
            z2 = cos(2*a)
            print("{0:.2f} {1:.4f}".format(a, z2))
        
