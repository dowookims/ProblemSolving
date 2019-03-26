n = 8
a = 4
b = 7
if a>b:
    a, b = b, a
answer = 0
flag = False
while True:
    if a % 2 and not b % 2 and a-b == -1:
        answer += 1
        break
    else:
        if a % 2:
            a = (a + 1) // 2
        elif a == 1:
            a = a
        else:
            a = a // 2
        if b % 2:
            b = (b+1) // 2
        else:
            b = b // 2
        answer += 1
print(answer)