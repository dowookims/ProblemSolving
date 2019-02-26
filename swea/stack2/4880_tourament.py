import sys
sys.stdin = open("4880.txt", "r")

for TC in range(1, int(input())+1):
    N = int(input())
    case = list(map(int, input().split()))
    print(case)