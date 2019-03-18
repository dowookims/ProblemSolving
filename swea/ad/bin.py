import sys
sys.stdin = open("bin.txt", "r")


def isWall(r, c):
    global n
    return 0 <= r < n and 0 <= c < n


def move(r, c, s=0):
    global n
    global m
    if s>m:
        return
    if r == n-1 and c == n-1:
        s += case[r][c]
        if s < m:
            m = s

    if isWall(r+1, c):
        d = s + case[r][c]
        move(r+1, c, d)
    if isWall(r, c+1):
        e = s + case[r][c]
        move(r, c+1, e)


for TC in range(1,int(input())+1):
    n = int(input())
    case = [ [ 0 for _ in range(n)] for _ in range(n)]
    m = 99999999
    for i in range(n):
        case[i] = list(map(int, input().split()))
    move(0, 0)

    print("#{} {}".format(TC, m))