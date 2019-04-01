v = 6
g = [[99 for _ in range(v+1)] for _ in range(v+1)]
Q = [987654321]*(v+1)
p = [None]*(v+1)
g[0][1] = 32
g[0][2] = 31
g[0][5] = 60
g[0][6] = 51
g[1][0] = 32
g[1][2] = 21
g[2][0] = 31
g[2][1] = 21
g[2][4] = 46
g[2][6] = 25
g[3][4] = 34
g[3][5] = 18
g[4][2] = 46
g[4][3] = 34
g[4][5] = 40
g[4][6] = 51
g[5][0] = 60
g[5][3] = 18
g[5][4] = 40
g[6][0] = 51
g[6][2] = 25
g[6][4] = 51



def MST_PRIM(r):
    p[r] = 0
    Q[r] = 0
    vx = 987654321
    vi = 0
    for i in range(1, v+1):
        if g[r][i] != 99:
            Q[i] = g[r][i]
            if Q[i] < vx:
                vx = Q[i]
                vi = i
            p[i] = r
    while True:
        if sum(Q) < 987654321:
            break
        mv = 987654321
        mi = 0
        for j in range(1, v+1):
            if g[vi][j] != 99:
                if Q[j] != 987654321 and g[vi][j] < Q[j]:
                    p[j] = vi
                    Q[j] = g[vi][j]
                    if mv > g[vi][j]:
                        mv = g[vi][j]
                        mi = j
                elif p[j] is None:
                    p[j] = vi
                    Q[j] = g[vi][j]
        vi = mi
MST_PRIM(0)
print(sum(Q))



