import sys
sys.stdin = open("contact.txt", "r")

def bfs(case,s):
    queue = [s]
    n = 1
    while queue:
        size = len(queue)
        for i in range(size):
            t = queue.pop(0)
            for j in graph[t]:
                if visited[j] == 1:
                    continue
                visited[j] = 1
            queue.append(j)
        if t == 0:
            break

for TC in range(1,11):
    l, s = map(int, input().split())
    graph = [[0 for _ in range(100)] for _ in range(100)]
    case = list(map(int, input().split()))
    visited = [0]*100
    for i in range(0, len(case), 2):
        graph[case[i]-1][case[i+1]-1] = 1
    bfs(case,s)

    for i in range(100):
        if not visited[i]:
            print(i, end=" ")
    print()

