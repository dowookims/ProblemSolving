'''
 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색 D2
'''

import sys
sys.stdin = open("5176.txt", "r")


for TC in range(1, int(input())+1):

    n = int(input())
    r2 = n//2
    case = [0] * (n+1)
    tree = [0] * (n+1)
    idx = 0
    k = 0
    while n > 2**k-1:
        k += 1
    idx = 2**(k-1)

