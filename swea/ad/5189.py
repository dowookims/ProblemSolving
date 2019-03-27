import sys
sys.stdin = open("5189.txt", "r")


def cal(n=1, res=0, idx=0):
    global N
    if n != N:
        for i in range(1, N):
            if visited[i]:
                continue
            visited[i] = 1
            res += case[idx][i]
            cal(n+1, res, idx=i)
            visited[i] = 0
            res -= case[idx][i]
    else:
        res += case[idx][0]
        d.append(res)


for TC in range(1, int(input())+1):
    d = []
    N = int(input())
    case = [0] * N
    visited = [0] * N
    for i in range(N):
        case[i] = list(map(int, input().split()))
    cal()
    print('#{} {}'.format(TC, min(d)))

