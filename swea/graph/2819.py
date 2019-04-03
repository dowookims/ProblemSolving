import sys
sys.stdin = open("2819.txt.txt", "r")


def isWall(r,c):
    return 0 <= r < 4 and 0 <= c < 4


def dfs(r, c, d=0, s=''):
    if d == 6:
        res.update({s: 1})
        return
    if d == 0:
        s = str(case[r][c])
    for i in range(4):
        rr = r + dy[i]
        cc = c + dx[i]
        if isWall(rr, cc):
            dfs(rr, cc, d+1, s + str(case[rr][cc]))


for TC in range(1, int(input())+1):
    case = [list(map(int, input().split())) for _ in range(4)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    res = {}
    for i in range(4):
        for j in range(4):
            dfs(i, j)
    print("#{} {}".format(TC, len(res)))
