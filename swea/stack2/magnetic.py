import sys
sys.stdin = open("input.txt", "r")
for TC in range(1, 11):
    r = 0
    x = input()
    l = [ _ for _ in range(100)]

    for i in range(100):
        l[i] = list(map(int,input().split()))

    for i in range(100):
        c = 0
        while c <99:
            if l[c][i] == 1:
                if l[c+1][i] == 2:
                     r += 1
                else:
                    l[c+1][i] = 1
            c+=1
    print(f"#{TC} {r}")
