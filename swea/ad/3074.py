'''
3074 입국심사
#1 28
#2 8
'''
import sys
sys.stdin = open("3074.txt", "r")

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())

    time = [0] * N
    for i in range(N):
        time[i] = int(input())

    # binary search
    r = min(time) * M
    l = 1

    while l < r:
        m = (l + r) // 2

        Sum = 0
        for i in range(N):
            Sum += m // time[i]

        if Sum < M:
            l = m + 1
        else:
            r = m

    print(f"#{TC} {l}")