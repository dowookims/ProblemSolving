import sys
sys.stdin = open("sample_input.txt", 'r')
def dfs(s):
    visited[s] = 1

    for i in range(len(case[s])):
        if case[s][i] and not visited[i]:
            dfs(i)

TC = int(input())+1
for T in range(1, TC):
    # V=노드 / E= 간선
    V,E = list(map(int,input().split()))
    case = [[0 for _ in range(V)] for _ in range(V)]

    for i in range(E):
        a, b = list(map(int,input().split()))
        case[a-1][b-1] = 1

    s, g = list(map(int,input().split()))
    visited = [ 0 for _ in range(V)]
    dfs(s-1)
    print(f"#{T} {visited[g-1]}")