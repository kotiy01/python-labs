from math import *

fh = open("lab1_in.txt", mode="rt")
fo = open("lab1_out.txt", mode="wt")

a = []
for line in fh:
    if line == "\n":
        continue
    a.append(int(line))

fo.write("+-----+-----+-----+" + "\n")
fo.write("|  X  |  Z1 |  Z2 |" + "\n")
fo.write("+-----+-----+-----+" + "\n")

for i in range(5):
    z1 = (sin(a[i])**4 + 2*sin(a[i])*cos(a[i]) - cos(a[i])**4) / (tan(2*a[i]) - 1)
    z2 = (cos(2*a[i]))
    fo.write("+ " + str(int(a[i])) + " + " + str("{0:0.2f}".format(z1)) + " + " + str("{0:0.2f}".format(z2)) + " | " + "\n")
    fo.write("+-----+-----+-----+" + "\n")

fh.close()
fo.close()
