'''
5202 화물도크 / Greedy
 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면, 최대 몇 대의 화물차가 이용할 수 있는지
'''
import sys
sys.stdin = open("5202.txt", "r")
for TC in range(1, int(input()) + 1):
    N = int(input())
    res = 1
    case = [0] * N
    for i in range(N):
        case[i] = list(map(int, input().split()))
    case.sort(key=lambda x: x[1])
    idx = 0
    cnt = 0
    while True:
        t = case[idx][1]
        if t == 24:
            break
        if cnt >= N:
            break
        for i in range(idx+1, N):
            cnt += 1
            if case[i][0] >= t:
                idx = i
                res += 1
                break
    print("#{} {}".format(TC, res))