import sys
sys.stdin = open("dictionary.txt", "r")



for TC in range(1, int(input())+1):
    N = int(input())
    case = [0]*N
    for i in range(N):
        case[i] = input()
