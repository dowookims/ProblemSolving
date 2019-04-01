import sys
sys.stdin = open("3.txt", "r-")
def cal(d=0, cnt= 0):
    global res
    global N
    if cnt > res:
        return
    if d == N:
        if res > cnt:
            res = cnt
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                cnt += maps[d][i]
                d += 1
                cal(d, cnt)
                d -= 1
                cnt -= maps[d][i]
                visited[i] = 0



for TC in range(1, int(input()) +1):
    N = int(input())
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    snacks = list(map(int, input().split()))
    robots = list(map(int, input().split()))
    visited = [0]*N
    snack = [0] * N
    robot = [0] * N
    res = 987654321
    maps = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(0, len(snacks), 2):
        snack[i//2] = [snacks[i], snacks[i+1]]

    for j in range(0, len(robots), 2):
        robot[j//2] = [robots[j], robots[j+1]]

    for k in range(N):
        for l in range(N):
            maps[k][l] = abs(robot[k][0] - snack[l][0]) + abs(robot[k][1] - snack[l][1])
    cal()
    print("#{} {}".format(TC, res))