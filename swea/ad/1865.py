import sys
sys.stdin = open('1865.txt', "r")


def cal(s=1, d=0):
    global N
    global res
    if d == N:
        if s > res:
            res = s
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            cal(s * case[d][i], d+1)
            visited[i] = 0


for TC in range(1, int(input())+1):
    N = int(input())
    visited = [0]*N
    case = [0]*N
    m = 0
    res = 0
    for i in range(N):
        case[i] = list(map(int, input().split()))
    cal()
    print(res)