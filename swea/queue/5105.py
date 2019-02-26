import sys
sys.stdin = open("5105.txt", "r")
for TC in range(1, int(input())+1):
    r = int(input())
    case = [[] for _ in range(r)]
    for i in range(r):
        case[i] = list(map(int,''.join(input())))
    
    for i in range()