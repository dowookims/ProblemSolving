import sys
sys.stdin = open("1824.txt", "r")

def move(c):
    global value
    global flag
    if c == '<':
        return 3
    elif c == '^':
        return 0
    elif c == '>':
        return 1
    elif c == 'v':
        return 2
    elif c == '_':
        if value == 0:
            return 1
        else:
            return 3
    elif c == '|':
        if value == 0:
            return 2
        else:
            return 0
    elif c == '.':
        flag = False
    elif c =='@':
        flag = True
    elif c =='+':
        if value == 15:
            value = 0
        else:
            value += 1
    elif c =='-':
        if value == 0:
            value = 15
        else:
            value -= 1


for TC in range(1, int(input())+1):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    value = 0
    flag = 0
    R, C = map(int, input().split())
    case = [[ 0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        case[i] = input()
    for item in case:
        print(item)
