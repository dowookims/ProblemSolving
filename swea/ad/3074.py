'''
3074 입국심사
#1 28
#2 8
'''
import sys
sys.stdin = open("3074.txt", "r")

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())

    t = [0] * N
    mt = 987654321
    for i in range(N):
        t[i] = int(input())
        if mt > t[i]:
            mt = t[i]

    r = mt * M
    s = 1

    while s < r:
        m = (s + r) // 2

        S = 0
        for i in range(N):
            S += m // t[i]

        if S < M:
            s = m + 1
        else:
            r = m

    print("#{} {}".format(TC, s))
