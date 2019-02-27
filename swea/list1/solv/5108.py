# 5108  [파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가
import sys
sys.stdin = open("5108.py.txt", "r")
for TC in range(1, int(input())+1):
    # N 수열의 길이 M 추가 횟수 L 출력할 인덱스
    N, M, L = map(int,input().split())
    case = list(map(int, input().split()))
    for _ in range(M):
        i, v = map(int, input().split())
        case.insert(i,v)
    print(f"#{TC} {case[L]}")
