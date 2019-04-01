import sys
sys.stdin = open("5208.txt", "r")


def cal(d, g, s=0):
    global N
    global res
    if d >= N:
        if res > s:
            res = s
        return
    if s > res:
        return
    else:
        for i in range(1, g + 1):
            if s >= res:
                break
            if d + i >= N:
                cal(d + i, case[d], s + 1)
                break
            else:
                cal(d + i, case[d + i], s + 1)


for TC in range(1, int(input()) + 1):
    case = list(map(int, input().split()))
    N = case[0]
    res = 987654321
    cal(1, case[1])

    print("#{} {}".format(TC, res-1))