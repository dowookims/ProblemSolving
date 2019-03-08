import sys
sys.stdin = open("6109.txt", "r")


def isInside(r,c):
    global n
    return 0 <= r < n and 0 <= c < n


def getIndex(text):
    idx = 0
    for i in range(4):
        if texts[i] == text:
            idx = i
            break
    return idx


def calculate(index, r):
    global n
    if index == 0 or index == 3:
        s = r
        e = n
    else:
        s = n
        e = r




for TC in range(1, int(input())+1):
    n, text = input().split()
    n = int(n)
    case = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    texts = ["up","right","down","left"]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    for i in range(n):
        case[i] = list(map(int, input().split()))

    idx = getIndex(text)
    for i in range(n):
        calculate(idx,i)

    print("#{}".format(TC))
    for item in case:
        print(item)
'''
8 8 4 8 8
8 4 4 2 4
2 4 2 0 8
'''