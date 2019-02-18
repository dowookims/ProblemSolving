a = int(input())
for i in range(1, a+1):
    b = int(input())
    e = []
    for j in range(b):
        r = list(map(int, input().split()))
        e.append(r)
    c = int(input())

    for k in range(c):
        input()
    
    result = [0]*c
    for item in e:
        for x in range((item[0]), item[1]+1):
            result[x-1] += 1
    result = list(map(str, result))
    fin = ' '.join(result)

    print(f'#{i} {fin}')

# runtime error
'''
t = int(input())
for T in range(t):
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = list(map(int,input().split()))
    p = int(input())
    c = [0] * 5010
    for i in range(n):
        for j in range(a[i],b[i]+1):
            c[j] += 1
    print("#%d" %(T+1), end= ' ')
    for i in range(p):
        print("%d" %c[int(input())],end = ' ')
    print()
'''