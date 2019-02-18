TC = int(input())
for i in range (1, TC+1):
    a, b = list(map(int, input().split()))
    r = [0]*a
    for k in range(a):
        r[k] = input().split()

    print(f'{i} {r}')