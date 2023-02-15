from math import *
from random import *
import traceback

while True:
    try:
        r = ''
        r = float(input('Введите значение радиуса: '))
    except ValueError:
        if r == '':
            r = 0
        print('Радиус - float')
    else:
        if r < 0:
            print('Радиус должен быть больше 0')
        else:
            print('     X      Y    Result')
            for n in range(10):
                x = uniform(-r, 2*r)
                y = uniform(-r, r)
                if (x >= -r and x < 0 and y >= sqrt(r**2 - (x + r)**2) - r and y < 0) or (x == 0 and y == 0) or (x > 0 and x <= 2*r and y <= sqrt(r**2 - (x - r)**2) and y > 0):
                    print('{0: 7.2f} {1: 7.2f}'.format(x, y), '   Yes')
                else:
                    print('{0: 7.2f} {1: 7.2f}'.format(x, y), '   No')
