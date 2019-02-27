# 5120. [파이썬 S/W 문제해결 기본] 7일차 - 암호
import sys
sys.stdin = open("5102.txt", "r")

for TC in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    case = list(map(int, input().split()))
    s = 0
    for i in range(1,K+1):

