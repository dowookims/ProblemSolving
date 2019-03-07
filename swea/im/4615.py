# 4615 재미있는 오셀로 게임
import sys
sys.stdin =open("4615.txt", "r")


def isEnemy(r, c, v):
    direction = []
    for i in range(4):
        mr = r + dr[i]
        mc = c + dc[i]
        if isWall(mr, mc) and case[mr][mc] and case[mr][mc] != v:
            direction.append(i)
    return direction if direction else None


def changeStone(r, c, direction):
    v = case[r][c]
    for d in direction:
        mr = r + dr[d]
        mc = c + dc[d]
        cnt = 0

        while isWall(mr, mc):
            if case[mr][mc] and case[mr][mc] != v:
                cnt += 1
                mr += dr[d]
                mc += dc[d]
            else:
                break
        nr = r
        nc = c
        for _ in range(cnt):
            nr += dr[d]
            nc += dc[d]
            case[nr][nc] = v


def isWall(r, c):
    global n
    return 0 < r < n and 0 < c < n


for TC in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    case = [[0 for _ in range(n)] for _ in range(n)]
    case[n//2][n//2], case[n//2][n//2-1], case[n//2-1][n//2], case[n//2-1][n//2-1] = 2, 1, 1, 2
    for _ in range(m):
        c, r, v = map(int, input().split())
        case[r-1][c-1] = v
        dl = isEnemy(r-1, c-1, v)
        if dl:
            changeStone(r-1, c-1, dl)
    black = 0
    white = 0
    for i in range(n):
        for j in range(n):
            if case[i][j] == 1:
                black += 1
            elif case[i][j] == 2:
                white += 1
    for line in case:
        print(line)
    print("#{} {} {}".format(TC, black, white))

