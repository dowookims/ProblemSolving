import sys
sys.stdin = open("1258.txt.txt", "r")

T = int(input())
for TC in range(1, T+1):
    r = int(input())
    case = [0]*r
    for i in range(len(case)):
        case[i] = list(map(int, input().split()))

    visit=[0]*r
    save = []

    for y in range(r):
        for x in range(r):
            if case[y][x]:
                pot_x = x
                pot_y = y
                while case[y][pot_x]:
                    pot_x += 1
                    if pot_x == r:
                        break
                while case[pot_y][x]:
                    pot_y += 1
                    if pot_y == r:
                        break

                if case[pot_y-1][pot_x-1]:
                    save.append([pot_y-y,pot_x-x])

                for i in range(y,pot_y):
                    for j in range(x,pot_x):
                        case[i][j] = 0

    print(f"#{TC} {len(save)}", end=" ")

    for i in range(len(save) - 1, 0, -1):
        for j in range(0, i):
            if save[j][0] * save[j][1] > save[j + 1][0] * save[j + 1][1]:
                save[j][0],save[j][1], save[j + 1][0], save[j+1][1] = save[j + 1][0], save[j + 1][1], save[j][0],save[j][1]
            elif (save[j][0] * save[j][1] == save[j + 1][0] * save[j + 1][1]) and save[j][0] > save[j+1][0]:
                save[j][0],save[j][1], save[j + 1][0], save[j+1][1] = save[j + 1][0], save[j + 1][1], save[j][0],save[j][1]
    for i in range(len(save)):
        for j in range(2):
            print(save[i][j], end=" ")
    print()