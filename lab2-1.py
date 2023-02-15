from math import *
import traceback

while True:
    try:
        x = input('Введите значение аргумента: ')
        x = float(x)
    except ValueError:
        if x == '':
            x = 0
        print('x - float')
    else:
        if x < -4:
            y = 2
        elif x >= -4 and x <= -2:
            y = 2 - sqrt(4 - (x + 2)**2)
        elif x > -2 and x <= 0:
            y = 0
        elif x > 0 and x < 3:
            y = -x
        elif x >= 3 and x <= 5:
            y = sqrt(4 - (x - 3)**2) - 1
        else:
            y = -1
        print('X = {0:.2f}    Y = {1:.2f}'.format(x, y))
