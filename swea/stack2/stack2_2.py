import sys
sys.stdin = open("sample_input2.txt", "r")

for TC in range(1, int(input())+1):
    r = int(input())
    case = [[] for _ in range(r)]
    s = []
    e = []
    for i in range(r):
        case[i] = list(map(int,''.join(input())))

    for i in range(r):
        if s and e:
            break
        for j in range(r):
            if case[i][j] == 2:
                s = [i,j]
            elif case[i][j] == 3:
                e = [i,j]

    for

    print(f"#{TC} {int(res)}")