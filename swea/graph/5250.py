import sys
sys.stdin = open("5250.txt", "r")


def is_wall(r, c):
    global N
    return 0 <= r < N and 0 <= c < N


def dijkstra(sr, se, V):
    INF = sys.maxsize

    s = [[False for _ in range(V)] for _ in range(V)]
    d = [[INF for _ in range(V)] for _ in range(V)]
    d[sr][se] = 0
    while True:
        m = INF
        N = 0

        for j in range(V):
            if not s[j] and m > d[j]:
                m = d[j]
                N = j
        if m == INF:
            break
        s[N] = True

        for j in range(V):
            if s[j]:
                continue
            via = d[N] + case[N][j]
            if d[j] > via:
                d[j] = via
    return d


for TC in range(1, int(input())+1):
    INF = sys.maxsize
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    N = int(input())
    D = [[INF for _ in range(N)] for _ in range(N)]
    res = 987654321
    case = [list(map(int, input().split())) for _ in range(N)]
    dijkstra(0, 0,  N)
    print("#{} {}".format(TC, res))