import sys
sys.stdin = open("2001.txt", "r")

for TC in range(1, int(input())+1):
    n, m = map(int, input().split())

    case = [[] for _ in range(n)]
    res = 0
    for i in range(n):
        case[i] = list(map(int, input().split()))
    for i in range(n-m+1):
        for j in range(n-m+1):
            d = 0
            for k in range(0,m):
                for l in range(0,m):
                    d +=case[i+k][j+l]
            if d>res:
                res = d
    print("#{} {}".format(TC,res))
