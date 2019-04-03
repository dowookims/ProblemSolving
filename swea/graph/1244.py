import sys
sys.stdin = open("1244.txt", "r")


def swaped(s, a, b):
    return s[:a] + s[b] + s[a + 1:b] + s[a] + s[b + 1:]


for TC in range(1, int(input())+1):
    L, C = input().split()
    l = len(L)
    C = int(C)
    POS = [(i, j) for i in range(l) for j in range(l) if i < j]
    now = set()
    now.add(L)
    after = set()
    for i in range(C):
        while now:
            s = now.pop()
            for i, j in POS:
                after.add(swaped(s, i, j))
        now, after = after, now
    print("#{} {}".format(TC, max(map(int, now))), sep='')