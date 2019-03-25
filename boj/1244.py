def inBound(s, i):
    global n
    return s-i > 0 and s+i < n

n = int(input())+1
btn = list(map(int, input().split()))
btn.insert(0, 0)
N = int(input())
for i in range(N):
    g, b = map(int, input().split())
    if g == 1:
        for j in range(b, n, b):
            if btn[j]:
                btn[j] = 0
            else:
                btn[j] = 1
    else:
        if btn[b]:
            btn[b] = 0
        else:
            btn[b] = 1
        k = 1
        while True:
            if inBound(b, k) and btn[b-k] == btn[b+k]:
                if btn[b-k] == 0:
                    btn[b-k], btn[b+k] = 1, 1
                else:
                    btn[b - k], btn[b + k] = 0, 0
                k += 1
            else:
                break

for i in range(1, n):
    if i > 1 and (i-1)%20 == 0:
        print()
    print(btn[i], end=" ")