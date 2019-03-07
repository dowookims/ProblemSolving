import sys
sys.stdin = open("1211.txt", "r")

for _ in range(10):
    TC = int(input())
    case = [[] for _ in range(100)]

    e = 0
    for i in range(100):
        case[i] = list(map(int, input().split()))
        if i == 99:
            for j in range(100):
                if case[i][j] == 2:
                    e = j
    print(e)


