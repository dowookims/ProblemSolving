import sys
sys.stdin = open("input4.txt", "r")

for _ in range(10):
    TC = int(input())
    case = [[] for _ in range(100)]
    for i in range(100):
        case[i] = list(map(int, input().split()))
    d = [0]*3
    res = 0
    for i in range(100):
        x_s = 0
        y_s = 0
        for j in range(100):
            x_s += case[i][j]
            y_s += case[j][i]
        d[0] = max(x_s, y_s, d[0])
        d[1] += case[i][i]
        d[2] += case[i][99-i]
    res = max(d)

    print(f"#{TC} {res}")