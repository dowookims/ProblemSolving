dy = [-3, -3, -2, 2, 3, 3, 2, -2]
dx = [-2, 2, 3, 3, 2, -2, -3, -3]


def is_wall(y, x):
    global N
    return 0 <= x < N and 0 <= y < N


def moves(sy, sx, cnt = 0):
    global res
    if cnt > res:
        return
    if res == 0 or res == 1:
        return
    if sy == m[1] and sx == m[0]:
        if cnt < res:
            res = cnt
        return

    else:
        for i in range(8):
            r = sy + dy[i]
            c = sx + dx[i]
            if is_wall(r, c) and not visited[r][c]:
                visited[r][c] = 1
                cnt += 1
                moves(r, c, cnt)
                cnt -= 1
                visited[r][c] = 0


for TC in range(1, int(input())+1):
    N = int(input())
    s = [0]*2
    m = [0]*2
    visited = [[0 for _ in range(N)] for _ in range(N)]
    s[1], s[0], m[1], m[0] = map(int, input().split())
    res = 987654321
    moves(s[0], s[1])
    print("#{} {}".format(TC, res))