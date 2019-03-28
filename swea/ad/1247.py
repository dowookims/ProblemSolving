'''
1247 최적 경로
'''
import sys
sys.stdin = open("1247.txt", "r")


def cal(d=0, s=0, f=0):
    global n
    global N
    global res
    if d == n:
        s += abs(case[f]-case[2]) + abs(case[f+1]-case[3])
        if s < res:
            res = s
    else:
        for i in range(4, N, 2):
            idx = ((i-2) // 2)-1
            if s > res:
                continue
            if not visited[idx]:
                visited[idx] = 1
                s += abs(case[f]-case[i]) + abs(case[f+1]-case[i+1])
                cal(d+1, s, i)
                s -= abs(case[f]-case[i]) + abs(case[f+1]-case[i+1])
                visited[idx] = 0

for TC in range(1, int(input())+1):
    n = int(input())
    visited = [0] * n
    case = list(map(int, input().split()))
    N = len(case)
    res = 987654321
    cal()
    print("#{} {}".format(TC, res))
'''
탐색공간에서 완전탐색 이후
이 공간을 줄여나가는 로직을 논리적이고 체계적으로 구현 할 수 있어야 함
'''


