import sys
sys.stdin = open("5356.txt", "r")

for TC in range(1, int(input())+1):
    case = [[] for _ in range(5)]
    m = 0
    for i in range(5):
        case[i] = input()
        if len(case[i])>m:
            m = len(case[i])
    print('#{}'.format(TC), end=" ")
    for j in range(m):
        for i in range(5):
            if len(case[i])>j:
                print(case[i][j], end="")
    print()

