'''
2628 종이자르기
'''

c, r = map(int, input().split())
n = int(input())
rl = [0]*100
cl = [0]*100
ri = 1
ci = 1
for i in range(n):
    ln, l = map(int, input().split())
    if ln:
        cl[ci] = l
        ci += 1
    else:
        rl[ri] = l
        ri += 1
cl.sort()
rl.sort()

res = 0
for i in range(ri):
    if i == 0:
        rv = rl[i]
    elif i == ri-1:
        rv = r - rl[i - 1]
    else:
        rv = rl[i] - rl[i - 1]

    for j in range(ci):
        if j == 0:
            cv = cl[j]
        elif j == ci-1:
            cv = c-cl[j-1]
        else:
            cv = cl[j] - cl[j-1]

        if cv*rv > res:
            res = cv*rv

print(res)
