'''
3074 입국심사
#1 28
#2 8
'''
import sys
sys.stdin = open("3074.txt", "r")


for TC in range(1, int(input())+1):
    N, M = map(int, input().split())
    t = [0] * (10 **9 +1)
    ct = [0] * N
    a = len(ct)
    st = set(ct)
    res = 0
    for i in range(N):
        ct[i] = int(input())
        t[ct[i]] += 1
    M -= N
    while M:
        res += 1
        for i in range(a):
            if res % ct[i] == 0:
                M -= t[ct[i]]
                if M == 0:
                    res += ct[i]
                    break

    print("#{} {}".format(TC, res))