# 2606 바이러스
import sys
sys.stdin = open("2606.txt", "r")

def dfs(N):
    global n
    if not visited[N]:
        visited[N] = 1
        for i in range(n+1):
            if case[N][i] and not visited[i]:
                dfs(i)

n = int(input())
c = int(input())
case = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(c):
    a, b = map(int, input().split())
    case[a][b] = 1
    case[b][a] = 1
dfs(1)
res = 0
for i in range(2, n+1):
    if visited[i]:
        res +=1
print(res)
