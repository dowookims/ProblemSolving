q1 = '00000010001101'
q2 = '0000000111100000011000000111100110000110000111100111100111111001100111'

a = len(q1)
b = len(q2)

for i in range (len(q1)//7):
    r = 0
    for j in range(0, 7):
        if q1[7*i+j] == '1':
            r += 2**(6-j)
    print(r, end=", ")
print()


for i in range (len(q2)//7):
    r = 0
    for j in range(0, 7):
        if q2[7*i+j] == '1':
            r += 2**(6-j)
    print(r, end=", ")
