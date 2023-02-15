from math import *
import traceback


print('Введите Xbeg, Xend и Dx')
while True:
    try:
        xb = xe = dx = ''
        xb = float(input('Xbeg = '))
        xe = float(input('Xend = '))
        dx = float(input('Dx = '))
    except ValueError:
        if xb == '' or xe == '' or dx == '':
            xb = xe = dx = 0
        print('Xbeg, Xend and Dx - float')
    else:
        print('Xbeg = {0: 7.2f}   Xend = {1: 7.2f}   Dx = {2: 7.2f}'.format(xb, xe, dx))
        xt = xb
        print('+--------+--------+')
        print('I   x    I    Y   I')
        print('+--------+--------+')

        while xt < xe:
            if xt < -4:
                y = 2
            elif xt >= -4 and xt <= -2:
                y = 2 - sqrt(4 - (xt + 2)**2)
            elif xt > -2 and xt <= 0:
                y = 0
            elif xt > 0 and xt < 3:
                y = -xt
            elif xt >= 3 and xt <= 5:
                y = sqrt(4 - (xt - 3)**2) - 1
            else:
                y = -1
            print('I{0: 7.2f} I{1: 7.2f} I'.format(xt, y))
            xt += dx
        print('+--------+--------+')
        
