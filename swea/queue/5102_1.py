import sys
sys.stdin = open("5102.txt", "r")

def bfs(queue):
    global n
    if s==e:
        return

    while queue:
        size = len(queue)
        n += 1
        for i in range(size):
            t = queue.pop(0)
            for j in con[t]:
                if visit[j] == 1:
                    continue
                visit[j] = 1
                queue.append(j)
        if e in queue:
            return
    n=0

T = int(input())
for TC in range(1, T + 1):
    V, E = map(int, input().split())
    con = [[] for i in range(V + 1)]
    visit = [0] * (V + 1)
    for i in range(E):
        x, y = map(int, input().split())
        con[x].append(y)
        con[y].append(x)
    s, e = map(int, input().split())
    queue = [s]
    visit[s] = 1
    n = 0
    bfs(queue)
    print(f"#{TC} {n}")