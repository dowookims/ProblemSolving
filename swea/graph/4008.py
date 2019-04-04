import sys
sys.stdin = open("4008.txt", "r")


def cal(v, n=0):
    global N
    global maxV
    global minV

    if n == N-1:
        if maxV is None:
            maxV = v
            minV = v
        if v > maxV:
            maxV = v
        elif v < minV:
            minV = v
        return

    nn = nums[n + 1]
    t = [v + nn, v - nn, v * nn, int(v / nn)]

    for i in range(4):
        if case[i]:
            case[i] -= 1
            cal(t[i], n+1)
            case[i] += 1


for TC in range(1, int(input())+1):
    N = int(input())
    case = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    minV = None
    maxV = None
    cal(nums[0])
    print("#{} {}".format(TC, maxV-minV))
