import sys
sys.stdin = open("5201.txt", "r")

for TC in range(1, int(input())+1):
    res = 0
    N, M = map(int, input().split())
    containers = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())))
    cidx = len(containers)-1
    tidx = len(trucks)-1

    while True:
        flag = False
        if cidx <= -1 or tidx <= -1:
            break
        if containers[cidx] > trucks[tidx]:
            while containers[cidx] > trucks[tidx]:
                cidx -= 1
                if cidx == -1:
                    flag = True
                    break
            if flag:
                break
            res += containers[cidx]
            cidx -= 1
            tidx -= 1
        else:
            res += containers[cidx]
            cidx -= 1
            tidx -= 1

    print("#{} {}".format(TC, res))