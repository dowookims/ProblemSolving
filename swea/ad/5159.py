import sys
sys.stdin = open("5159.txt", "r")


def move(r, c, v, s = 0, q = 1):
    global n
    global m

    if s > m:
        return

    if q == n-1:
        s = s
        if s < m:
            m = s

    for i in range(1, n):
        if case[r][i] and not v[i]:
            v[i] = 1
            s += case[r][i]
            q += 1
            move(i, c, v, s, q)


for TC in range(1, int(input())+1):
    n = int(input())
    case = [[0 for _ in range(n)] for _ in range(n)]
    visited = [0]*n
    m = 987654321
    for i in range(n):
        case[i] = list(map(int, input().split()))
    move(0, 0, visited)

    print("#{} {}".format(TC, m))
