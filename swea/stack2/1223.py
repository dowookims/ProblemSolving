# 1223. [S/W 문제해결 기본] 6일차 - 계산기2

import sys
sys.stdin = open("1223.txt","r")

for TC in range(1, 11):
    r = int(input())
    case = input()
    d = [0] * r
    stack = [0] * r
    sum = 0
    for i in range(len(case)):
        if case[i].isdigit():
            

