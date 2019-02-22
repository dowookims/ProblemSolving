import sys
sys.stdin = open("sample_input1.txt", "r")
T = int(input())
for TC in range(1,T+1):
    r = int(input())
    clue = [0]*r
    case = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0
    for i in range(r):
        clue[i] = list(map(int, input().split()))
    for i in range(r):
        s_x, s_y = clue[i][0:2]
        e_x, e_y = clue[i][2:4]
        color = clue[i][4]
        for y in range(s_y, e_y+1):
            for x in range(s_x, e_x+1):
                if case[y][x] ==0 or case[y][x]== color:
                    case[y][x] = color
                elif color + case[y][x] ==3:
                    case[y][x] =3
                    cnt += 1
    print(f"#{TC} {cnt}")