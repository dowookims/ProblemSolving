import sys
sys.stdin = open("6109.txt", "r")

for TC in range(1, int(input())+1):
    n, text = input().split()
    n = int(n)
    case = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        case[i] = list(map(int, input().split()))

    if text == "up":
        for i in range(0, n-1):
            for j in range(n):
                if case[i][j] == 0:
                    case[i][j] = case[i+1][j]
                    case[i + 1][j] = 0
        for i in range(0, n - 1):
            for j in range(n):
                if case[i][j] and case[i][j] == case[i+1][j]:
                    case[i][j] += case[i][j]
                    case[i+1][j] = 0
        for i in range(0, n-1):
            for j in range(n):
                if case[i][j] == 0:
                    case[i][j] = case[i+1][j]
                    case[i + 1][j] = 0
        for i in range(0, n-1):
            for j in range(n):
                if case[i][j] == 0:
                    case[i][j] = case[i+1][j]
                    case[i + 1][j] = 0

        for i in range(n):
            case[n-1][i] = 0
    for line in case:
        print(line)

