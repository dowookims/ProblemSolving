# 5122. [파이썬 S/W 문제해결 기본] 7일차 - 수열 편집

import sys
sys.stdin = open("5122.py.txt", "r")

for TC in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    case = list(map(int, input().split()))
    for i in range(M):
        ins = input().split()
        if ins[0] =="I":
            case.insert(int(ins[1]),int(ins[2]))
        elif ins[0] =="D":
            case.pop(int(ins[1]))
        else:
            case[int(ins[1])] = int(ins[2])
    res = 0
    if L > len(case)-1:
        res = -1
    else:
        res = case[L]
    print("#{} {}".format(TC,res))

