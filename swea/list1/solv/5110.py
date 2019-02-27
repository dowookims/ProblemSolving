# 5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기
import sys
sys.stdin = open("5110.txt", "r")

for TC in range(1, int(input())+1):
    # N : 수열의 길이 / M : 수열의 개수 /
    N, M = map(int, input().split())
    case = [0]*M
    case[0] = list(map(int, input().split()))
    for i in range(M-1):
        case[1] = list(map(int, input().split()))
        C = max(case[0])
        for j in range(N):
            if case[1][0] < case[0][j]:
                b = case[0][:j]
                a = case[0][j:]
                case[0] = b + case[1] + a
                break
            elif case[1][0] >= C:
                case[0].extend(case[1])

    r = len(case[0])-1
    print(f"#{TC} {case[0][r:r-10:-1]}")

