import sys
sys.stdin = open("2115.txt", "r")


def isWall(r, c):
    global N
    return 0 <= r < N and 0 <= c < N


for TC in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    case = [list(map(int, input().split())) for _ in range(N)]
    V = [[False for _ in range(N)] for _ in range(N)]
    res = 0
    p = []
    for i in range(N):
        for j in range(N):
            if j+M <= N:
                FM = 0
                Note = [0]*M
                for k in range(j, j+M):
                    V[i][k] = True
                    Note[j+M-k-1] = case[i][k]

    print("#{} {}".format(TC, res))