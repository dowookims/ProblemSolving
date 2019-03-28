'''
5207 이진탐색
'''

import sys
sys.stdin = open("5207.txt", "r")

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    q = len(A) // 2
    B = set(map(int, input().split()))
    C =set(A)
    res = len(B.intersection(C))
    if A[q] in C:
        res -= 1
    print(f"{TC} {res}")