import sys
sys.stdin = open("input5.txt", "r")

for _ in range(10):
    TC = int(input())
    res = 0
    case = [[] for _ in range(100)]
    e = []
    for i in range(100):
        case[i] = list(map(int ,input().split()))
    for i in range(100):
        if case[99][i] == 2:
            e = i
    for i in range(98, 0, -1):
        while True:
            if e>0 and case[i][e-1]:
                while case[i][e-1]:
                    e -= 1
                    if e==0:
                        break
                break
            elif e <99 and case[i][e+1] :
                while case[i][e+1]:
                    e += 1
                    if e==99:
                        break
                break
            else:
                break
    res = e

    print(f"#{TC} {res}")