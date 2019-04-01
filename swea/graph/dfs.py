a = [1, 2, 1, 3, 2, 4, 2, 5, 4, 7, 5, 6, 6, 7, 3, 7]
g = [[0 for _ in range(7)] for _ in range(7)]
visited = [0]*8
for i in range(0, len(a), 2):
    g[a[i]-1][a[i+1]-1] = 1

stack = []


def dfs(v):
    stack.append(v)
    while not len(stack):
        r = stack.pop(-1)
        if not visited[r]:
            print(r, end=" ")
            visited[r] = 1
            for j in range(1, len(g[r-1])):
                if not visited[j+1]:
                    stack.append([j+1])


dfs(1)
