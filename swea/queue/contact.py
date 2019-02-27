import sys
sys.stdin = open("contact.txt", "r")

def bfs(s):
    queue = [s]
    depth = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            t = queue.pop(0)
            for j in range(len(graph[t])):
                if graph[t][j] and visited[j] == 1:
                    continue
                visited[j] = 1
                d[depth].append(j)
                queue.append(j)
        depth += 1
    return depth-1

for TC in range(1,11):
    l, s = map(int, input().split())
    graph = [[0 for _ in range(100)] for _ in range(100)]
    case = list(map(int, input().split()))
    visited = [0]*100
    for i in range(0, len(case), 2):
        graph[case[i]-1][case[i+1]-1] = 1
    r = []
    d = [[] for _ in range(100)]
    c = bfs(s)

    res = 0
    for item in d[c]:
        if item>res:
            res = item
    print(f"#{TC} {res}")