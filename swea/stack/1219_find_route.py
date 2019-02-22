import sys
sys.stdin = open("input7.txt", "r")

def dfs(s):
    visited[s]=1
    if s ==99:
        return

    for i in range(len(case_list[s])):
        if case_list[s][i] and not visited[i]:
            dfs(i)


for _ in range(10):
    # r = 간선
    TC, r = list(map(int, input().split()))
    case = list(map(int, input().split()))
    case_list = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(0, len(case), 2):
        case_list[case[i]][case[i+1]] = 1
    visited = [ 0 for _ in range(100)]
    dfs(0)
    print(f"#{TC} {visited[99]}")