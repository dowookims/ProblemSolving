def BFS(G, v):
    visited = [0 for _ in range(7)]
    queue = [v]
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            print(t+1, end= ' ')
            visited[t] = True          
        for i in range(len(G[t])):
            if G[t][i] and not visited[i]:
                queue.append(i)

a = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

case =[[0 for _ in range(7)] for _ in range(7)]
for i in range(0,len(a),2):
    case[a[i]-1][a[i+1]-1]= 1
    case[a[i+1]-1][a[i]-1]= 1
BFS(case,0)