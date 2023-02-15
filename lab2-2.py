from math import *
import traceback

while True:
    try:
        r = x = y = ''
        r = float(input('Введите значение радиуса: '))
        x = float(input('Введите значение X: '))
        y = float(input('Введите значение Y: '))
    except ValueError:
        if r == '' or x == '' or y == '':
            r = 0
            x = 0
            y = 0
        print('r, x, y - float')
    else:
        if r < 0:
            print('Радиус должен быть больше 0')
        else:
            if (x >= -r and x < 0 and y >= sqrt(r**2 - (x + r)**2) - r and y < 0) or (x == 0 and y == 0) or (x > 0 and x <= 2*r and y <= sqrt(r**2 - (x - r)**2) and y > 0):
                print('Точка попадает в область')
            else:
                print('Точка не попадает в область')
                
