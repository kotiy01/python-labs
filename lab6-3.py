import random

fh = open("lab5_in.txt", mode="rt")
fo = open("lab5_out.txt", mode="wt")

x = []
for line in fh:
    if line == "\n":
        continue
    x.append(int(line))

n = x[0]
string = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

A = []
B = []

for  i in range(n):
    A.append([0]*n)
    B.append([3]*n)

for Row in range(n):
    for Col in range(n):
        A[Row][Col]=random.choice(string)
        string.remove(A[Row][Col])
for Row in range(n):
    for Col in range(n):
        fo.write(str(A[Row][Col]) + " ")
    fo.write("\n")
fo.write("\n")

q = 0
length = random.randint(1, 10)

sentence = ''
while q < length:
    j = 0
    Col = 0
    Row = random.randint(0,5)
    while j < n:
        sentence += A[Row][Col]
        j+=1
        Col+=1
    q+=1
    sentence += ' '
    
fo.write(str(sentence) + "\n")

fh.close()
fo.close()
