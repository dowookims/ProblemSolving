import sys
sys.stdin = open("5251.txt", "r")


def dijkstra(K, V):
    INF = sys.maxsize

    s = [False] * V
    d = [INF] * V
    d[K] = 0
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
            via = d[N] + graph[N][j]
            if d[j] > via:
                d[j] = via
    return d


for TC in range(1, int(input())+1):
    V, E = map(int, input().split())
    INF = sys.maxsize
    graph = [[INF]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u][v] = w
    d = dijkstra(0, V+1)
    r = len(d)

    print("#{} {}".format(TC, d[r-1]))

