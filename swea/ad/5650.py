import sys
sys.stdin = open("5650.txt", "r")

def is_wall(r, c):
    global N
    return 0 <= r < N and 0 <= c < N


def dfs(r, c, i, sr, sc):
    v = 0
    while True:
        r += dy[i]
        c += dx[i]

        if not is_wall(r, c):
            if i == 0: i = 2
            elif i == 1: i = 3
            elif i == 2: i = 0
            else: i = 1
            r -= dy[i]
            c -= dx[i]
        else:
            if case[r][c] == -1:
                break

            elif r == sr and c == sc:
                break

            elif 1 <= case[r][c] <= 5:
                if case[r][c] == 1:
                    if i == 0: i = 2
                    elif i == 1: i = 3
                    elif i == 2: i = 1
                    else: i = 0
                elif case[r][c] == 2:
                    if i == 0: i = 1
                    elif i == 1: i = 3
                    elif i == 2: i = 0
                    else: i = 2
                elif case[r][c] == 3:
                    if i == 0: i = 3
                    elif i == 1: i = 2
                    elif i == 2: i = 0
                    else: i = 1
                elif case[r][c] == 4:
                    if i == 0: i = 2
                    elif i == 1: i = 0
                    elif i == 2: i = 3
                    else: i = 1
                else:
                    if i == 0: i = 2
                    elif i == 1: i = 3
                    elif i == 2: i = 0
                    else: i = 1
                v += 1
            elif case[r][c] >= 6:
                idx = case[r][c]-6
                for j in range(2):
                    if not(wh[idx][j][0] == r and wh[idx][j][1] == c):
                        r, c = wh[idx][j][0], wh[idx][j][1]
                        break
    return v


for TC in range(1, int(input())+1):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    N = int(input())
    case = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    d = []
    wh = [[] for _ in range(5)]
    for i in range(N):
        for j in range(N):
            if not case[i][j]:
                d.append((i,j))
            elif case[i][j] >= 6:
                wh[case[i][j]-6].append((i, j))


    # 블랙홀 : -1 | 빈공간 : 0 | 블록 : 1 ~ 5 | 웜홀 : 6 ~ 10
    # 1 : lb | 2 : tl | 3: tr | 4 : rb | 5 : trbl
    while d:
        r, c = d.pop(-1)
        for i in range(4):
            # print("[r, c, i ]", r, c, i)
            a = dfs(r, c, i, r, c)
            if a and a > res:
                res = a
    print("#{} {}".format(TC, res))