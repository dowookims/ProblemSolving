# 5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기
import sys
sys.stdin = open("5110.txt", "r")

for TC in range(1, int(input())+1):
    # N : 수열의 길이 / M : 수열의 개수 /
    N, M = map(int, input().split())
    case = [0]*M
    for i in range(M):
        if i>=2:
            i = 1
        case[i] = list(map(int, input().split()))
        if i>0:
            if case[1][0] >= max(case[0]):
                case[0] = case[0]+case[1]
            else:
                N = len(case[0])
                for j in range(N):
                    if case[1][0] < case[0][j]:
                        b = [0] * j
                        a = [0] * (N - j)
                        for q in range(j):
                            b[q] = case[0][q]
                        for w in range(j, N):
                            a[w - j] = case[0][w]
                        case[0] = b + case[1] + a
                        break

    r = len(case[0])-1
    print("#{}".format(TC), end=" ")
    for i in range(r,r-10,-1):
        print(case[0][i], end=" ")
    print()
    # print(f"#{TC} {case[0][r:r-10:-1]}")

