def dfs(G,v):

    if not visited[v]:
        print(v+1, end=" ")
        visited[v] = True
    for i in range(7):
        if visited[i]==0 and case[v][i]:

            dfs(G,i)

a = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

case = [[0 for _ in range(7)] for _ in range(7)]
visited = [0]*7
for j in range(0, len(a),2):
    case[a[j]-1][a[j+1]-1] = 1
    case[a[j+1]-1][a[j]-1] = 1

dfs(case,0)

