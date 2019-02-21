import sys
sys.stdin = open("input2.txt", "r")

for TC in range(1,11):
    x = int(input())
    case = list(map(int, input().split()))
    res = 0
    i = 2
    while i<x-2:
        c = max(case[i-2], case[i-1], case[i+1], case[i+2])
        if  c <= case[i]-1:
            res += case[i] - c
            i += 3
        else: i += 1
    print(f"#{TC} {res}")