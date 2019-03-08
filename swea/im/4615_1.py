import sys
sys.stdin = open("4615.txt", "r")


def isWall(r, c):
    global n
    return 0 <= r < n and 0 <= c < n


def isEnemy(r,c):
    v = case[r][c]
    d = []
    for i in range(6):
        mr = r + dr[i]
        mc = c + dc[i]
        if isWall(mr, mc) and case[mr][mc] and case[mr][mc] != v:
            d.append(i)

    return d

# 바뀔때 사이에 있는 것만 바뀌게
# 만약 벽을 만났을 때, 그 시작점에 대각선에 같은 색 돌이 있고, 연속으로 다른 색 돌이 있는지;
# 대각선도 고려해서 계싼해야함
def changeStone(r, c, i, cnt=0):
    global v
    mr = r + dr[i]
    mc = c + dc[i]
    if isWall(mr, mc) and case[mr][mc] and case[mr][mc] != v:
        cnt += 1
        changeStone(mr, mc, i, cnt)
    elif isWall(mr, mc) and case[mr][mc] == v and cnt > 0:
        for j in range(cnt):
            mr -= dr[i]
            mc -= dc[i]
            case[mr][mc] = v
    elif isWall(mr, mc) and case[mr][mc] == 0 and cnt > 0:
        for j in range(cnt):
            mr -= dr[i]
            mc -= dc[i]
            case[mr][mc] = v
    elif not isWall(mr, mc) and case[r][c] == v:
        for j in range(cnt):
            mr -= dr[i]
            mc -= dc[i]
            case[mr][mc] = v
    else:
        return


for TC in range(1, int(input()) + 1):
    dr = [1, 0, -1, 0, 1, -1]
    dc = [0, 1, 0, -1, 1, -1]
    n, m = map(int, input().split())
    case = [[0 for _ in range(n)] for _ in range(n)]
    case[n//2-1][n//2-1], case[n//2-1][n//2], case[n//2][n//2-1], case[n//2][n//2] = 2, 1, 1, 2
    for _ in range(m):
        c, r, s = map(int, input().split())
        case[r-1][c-1] = s
        directions = isEnemy(r-1, c-1)
        # print('착수 :', s)
        # print(r-1, c-1)
        if directions:
            v = case[r-1][c-1]
            for direction in directions:
                changeStone(r-1, c-1, direction)

    for line in case:
        print(line)
    print()