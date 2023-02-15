import random

n = 6
A = []
B = []

for i in range(n):
    A.append([0]*n)
    B.append([3]*n)

string = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for Row in range(n):
    for Col in range(n):
        A[Row][Col]=random.choice(string)
        string.remove(A[Row][Col])
for Row in range(n):
    for Col in range(n):
        print("{}".format(A[Row][Col]), end=" ")
    print()
print()

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
    
print(sentence)
