import sys
sys.stdin = open("5102.txt", "r")

def bfs(v,e):
    queue =[v]
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
        for i in range(len(visited)):
            if graph[t][i] and not visited[i]:
                queue.append(i)
                depth[i] = depth[t] + 1

        if visited[e]:
            return depth[e]
    return 0

for TC in range(1, int(input()) + 1):
    # V = 노드 개수 E = 간선
    V, E = list(map(int, input().split()))
    graph = [[0 for _ in range(V)] for _ in range(V)]
    depth = [0]*V

    for _ in range(E):
        P, C = list(map(int, input().split()))
        graph[P-1][C-1] = 1
        graph[C-1][P-1] = 1

    s, e = list(map(int, input().split()))
    visited = [0]*V
    #213
    print(s,e)
    for item in graph:
        print(item)
    print("#{} {}".format(TC, bfs(s-1,e-1)))

