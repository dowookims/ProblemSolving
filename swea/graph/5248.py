import sys
sys.stdin = open("5248.txt", "r")


# def dfs(n):
#     global N
#     global res
#     for i in range(N):
#         if not V[i]:
#             if g[n][i]:
#                 V[i] = 1
#                 dfs(i)
#
#
# for TC in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     case = list(map(int, input().split()))
#     res = 0
#     g = [[0 for _ in range(N)] for _ in range(N)]
#     V = [False]*N
#     for i in range(0, len(case), 2):
#         r = case[i]-1
#         c = case[i+1]-1
#         g[r][c] = 1
#         g[c][r] = 1
#
#     for i in range(N):
#         if not V[i]:
#             res += 1
#             dfs(i)
#     print("#{} {}".format(TC, res))


def rep(n):
    if p[n] != n:
        n = p[n]
    return n


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    pairs = list(map(int, input().split()))
    p = [i for i in range(N + 1)]

    for i in range(M):
        a = pairs[2 * i]
        b = pairs[2 * i + 1]
        p[rep(b)] = rep(a)

    cnt = 0
    print(p)
    for i in range(1, N + 1):
        if p[i] == i:
            cnt += 1

    print('#%d' % tc, cnt)