import sys
sys.stdin = open("1959.txt", "r")


def cal(q, w):
    global res
    c = len(q) - len(w)
    for i in range(c+1):
        sums = 0
        for j in range(len(w)):
            sums += q[i + j] * w[j]
        if sums > res:
            res = sums


for TC in range(1, int(input())+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = 0

    if len(A) >= len(B):
        cal(A, B)
    else:
        cal(B, A)
    print("#{} {}".format(TC, res))