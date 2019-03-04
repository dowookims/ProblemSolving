import sys
sys.stdin = open("sdoku.txt", "r")

for TC in range(1, int(input())+1):
    r = 9
    case = [[] for _ in range(9)]
    for i in range(9):
        case[i] = list(map(int, input().split()))

    flag = True

    for i in range(0,9,3):
        for j in range(0,9,3):
            box = []
            for k in range(0,3):
                for l in range(0,3):
                    if case[i+k][j+l] not in box:
                        box.append(case[i+k][j+l])
                    else:
                        flag = False
                        break
    if flag:
        for i in range(9):
            if not flag:
                break
            row = []
            col = []
            for j in range(9):
                if case[j][i] not in col:
                    col.append(case[j][i])
                elif case[j][i] in col:
                    flag = False
                    break
                if case[i][j] not in row:
                    row.append(case[i][j])
                elif case[i][j] in row:
                    flag = False
                    break

    print(f"#{TC} {int(flag)}")
