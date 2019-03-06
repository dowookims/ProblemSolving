import sys
sys.stdin = open('ns.txt', "r")

for TC in range(1, int(input())+1):
    n = int(input())
    case = [[] for _ in range(n)]
    for i in range(n):
        case[i] = list(map(int, ''.join(input())))
    res = 0
    for i in range(n):
        s = abs(n//2-i)
        e = n - abs(n//2-i)
        for j in range(s, e):
            res += case[i][j]
    print("#{} {}".format(TC, res))